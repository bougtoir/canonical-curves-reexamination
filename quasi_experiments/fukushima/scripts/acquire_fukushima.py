"""Download and assemble the Fukushima-area municipal source panel.

The script intentionally preserves source gaps as missing values.  e-Stat
downloads are discovered from the public HTML listings rather than using the
API, which requires an application ID.
"""

from __future__ import annotations

import csv
import datetime as dt
import html
import io
import re
import shutil
import subprocess
import unicodedata
from html.parser import HTMLParser
from pathlib import Path

import pandas as pd
import requests


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
DATA = ROOT / "data"
TODAY = dt.date.today().isoformat()
SESSION = requests.Session()
SESSION.headers["User-Agent"] = "canonical-curves-reexamination/1.0"

PREFECTURES = {
    "03": "岩手県",
    "04": "宮城県",
    "06": "山形県",
    "07": "福島県",
    "08": "茨城県",
    "09": "栃木県",
    "10": "群馬県",
    "15": "新潟県",
}
EVACUATION_MUNICIPALITIES = {
    "双葉町",
    "大熊町",
    "富岡町",
    "浪江町",
    "楢葉町",
    "川内村",
    "葛尾村",
    "飯舘村",
    "南相馬市",
    "田村市",
    "川俣町",
    "広野町",
}
VITAL_BASE = (
    "https://www.e-stat.go.jp/stat-search/files?"
    "cycle=7&layout=datalist&month=0&page=1&result_back=1"
    "&tclass1=000001053058&tclass2=000001053061"
    "&tclass3=000001053063&tclass4val=0&toukei=00450011"
    "&tstat=000001028897&year={year}0"
)
POP_BASE = (
    "https://www.e-stat.go.jp/stat-search/files?"
    "cycle=7&layout=datalist&month=0&page=1"
    "&tclass1=000001039601&toukei=00200241"
    "&tstat=000001039591&year={year}0"
)
DOWNLOAD = "https://www.e-stat.go.jp/stat-search/file-download"
LEGACY_POPULATION_IDS = {
    2000: "000008291507",
    2001: "000008291487",
    2002: "000008291483",
    2003: "000008291465",
    2004: "000008291447",
    2005: "000008291443",
    2006: "000008291251",
    2007: "000008291233",
    2008: "000008291152",
    2009: "000008291134",
    2010: "000008290577",
    2011: "000011437958",
    2012: "000014500667",
}
RECONSTRUCTION_PDF = (
    "https://www.reconstruction.go.jp/files/user/topics/main-cat2/"
    "sub-cat2-6/20260213_kanrenshi.pdf"
)
AGE_SEARCH_URL = (
    "https://www.e-stat.go.jp/stat-search/database?"
    "layout=datalist&stat_infid=000001086011"
)
AGE_2010_IDS = {
    "03": "000010986082",
    "04": "000010986148",
    "06": "000012460936",
    "07": "000010986214",
    "08": "000012461002",
    "09": "000012461068",
    "10": "000012461134",
    "15": "000012461464",
}
METI_ORDER_SOURCE = (
    "https://www.meti.go.jp/earthquake/nuclear/release.html"
)
FUKUSHIMA_ORDER_SOURCE = "https://www.pref.fukushima.lg.jp/site/portal/cat01-more.html"
METI_CLASSIFICATION_SOURCE = (
    "https://www.meti.go.jp/earthquake/nuclear/20110411_keikakuhinan.html"
)
EVACUATION_SUMMARY_PDF = (
    "https://www.pref.fukushima.lg.jp/uploaded/attachment/688152.pdf"
)
MERGER_SOURCE = "https://www.soumu.go.jp/gapei/hensen_hukushima.html"


def record_source(rows: list[dict[str, str]], url: str, table: str, notes: str) -> None:
    rows.append(
        {
            "url": url,
            "retrieval_date": TODAY,
            "table": table,
            "notes": notes,
        }
    )


def get(url: str) -> requests.Response:
    response = SESSION.get(url, timeout=120)
    response.raise_for_status()
    return response


def download(url: str, path: Path, sources: list[dict[str, str]], table: str) -> bool:
    try:
        response = get(url)
        path.write_bytes(response.content)
        record_source(sources, url, table, f"Downloaded to {path.relative_to(ROOT)}.")
        return True
    except Exception as exc:
        record_source(
            sources,
            url,
            table,
            f"not obtained: {type(exc).__name__}: {exc}",
        )
        return False


def listing_links(page_url: str, file_kind: str | None = None) -> list[tuple[str, str]]:
    source = html.unescape(get(page_url).text)
    pattern = r"/stat-search/file-download\?statInfId=(\d+)&fileKind=(\d+)"
    links: list[tuple[str, str]] = []
    for match in re.finditer(pattern, source):
        if file_kind is not None and match.group(2) != file_kind:
            continue
        context = re.sub(r"\s+", " ", source[max(0, match.start() - 800) : match.end() + 250])
        links.append((match.group(1), context))
    return links


def discover_vital_ids(year: int, sources: list[dict[str, str]]) -> dict[str, str]:
    url = VITAL_BASE.format(year=year)
    ids: dict[str, str] = {}
    try:
        for stat_id, context in listing_links(url, "1"):
            for pref_code, pref_name in PREFECTURES.items():
                if (
                    pref_name in context
                    and f"{pref_code} " in context
                ):
                    ids[pref_code] = stat_id
        if len(ids) < len(PREFECTURES):
            listing = html.unescape(get(url).text)
            detail_pattern = r'<a[^>]+href="([^"]*stat_infid=(\d+)[^"]*)"'
            for match in re.finditer(detail_pattern, listing):
                detail_href, detail_id = match.groups()
                context = re.sub(
                    r"\s+", " ", listing[max(0, match.start() - 500) : match.end() + 500]
                )
                pref_code = next(
                    (
                        code
                        for code, pref_name in PREFECTURES.items()
                        if pref_name in context
                    ),
                    None,
                )
                if pref_code is None or pref_code in ids:
                    continue
                detail_url = (
                    "https://www.e-stat.go.jp"
                    + html.unescape(detail_href).replace("&amp;", "&")
                )
                for stat_id, context in listing_links(detail_url, "1"):
                    ids[pref_code] = stat_id
                    break
        for pref_code, pref_name in PREFECTURES.items():
            if pref_code not in ids:
                record_source(
                    sources,
                    url,
                    f"e-Stat annual vital statistics {year} {pref_name}",
                    "not obtained: prefecture CSV link was not found in the listing.",
                )
    except Exception as exc:
        record_source(
            sources,
            url,
            f"e-Stat annual vital statistics {year}",
            f"not obtained: {type(exc).__name__}: {exc}",
        )
    return ids


def parse_number(value: object) -> float | None:
    text = str(value).strip().replace(",", "")
    if not text or text in {"-", "...", "－", "…", "nan"}:
        return None
    try:
        return float(text)
    except ValueError:
        return None


def parse_vital(path: Path, pref_code: str, year: int) -> pd.DataFrame:
    raw = path.read_bytes()
    text = raw.decode("cp932", errors="replace")
    rows = list(csv.reader(io.StringIO(text)))
    output: list[dict[str, object]] = []
    for row in rows:
        if len(row) < 5:
            continue
        first = str(row[0]).strip().replace("\u3000", "")
        match = re.match(r"^(\d{5})(.*)$", first)
        if not match or not match.group(1).startswith(pref_code):
            continue
        muni_code = match.group(1)
        muni_name = normalize_municipality_name(match.group(2))
        output.append(
            {
                "pref_code": pref_code,
                "muni_code_observed": muni_code,
                "muni_name": muni_name,
                "year": year,
                "births": parse_number(row[1]),
                "deaths": parse_number(row[3]),
            }
        )
    return pd.DataFrame(output)


def acquire_vital(sources: list[dict[str, str]]) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for year in range(2000, 2023):
        ids = discover_vital_ids(year, sources)
        for pref_code, stat_id in ids.items():
            url = f"{DOWNLOAD}?statInfId={stat_id}&fileKind=1"
            path = RAW / f"vital_{year}_{pref_code}.csv"
            if download(
                url,
                path,
                sources,
                f"e-Stat annual municipal vital statistics {year} {PREFECTURES[pref_code]}",
            ):
                frame = parse_vital(path, pref_code, year)
                if not frame.empty:
                    frames.append(frame)
    if not frames:
        return pd.DataFrame(
            columns=[
                "pref_code",
                "muni_code_observed",
                "muni_name",
                "year",
                "births",
                "deaths",
            ]
        )
    return pd.concat(frames, ignore_index=True)


def discover_population_id(year: int, sources: list[dict[str, str]]) -> str | None:
    url = POP_BASE.format(year=year)
    if year in LEGACY_POPULATION_IDS:
        record_source(
            sources,
            url,
            f"e-Stat resident-register population {year}",
            "The JS-rendered listing was read through the existing Chrome CDP browser session; selected 03 市区町村別人口、人口動態及び世帯数 (総計) workbook.",
        )
        return LEGACY_POPULATION_IDS[year]
    try:
        candidates = []
        for stat_id, context in listing_links(url, "0"):
            if (
                "市区町村別人口、人口動態及び世帯数" in context
                and "【総計】" in context
                and "年齢階級別" not in context
            ):
                candidates.append(stat_id)
        if candidates:
            return candidates[0]
        record_source(
            sources,
            url,
            f"e-Stat resident-register population {year}",
            "not obtained: municipal total-population workbook was not found.",
        )
    except Exception as exc:
        record_source(
            sources,
            url,
            f"e-Stat resident-register population {year}",
            f"not obtained: {type(exc).__name__}: {exc}",
        )
    return None


def parse_population(path: Path, year: int) -> pd.DataFrame:
    sheets = pd.read_excel(path, sheet_name=None, header=None)
    frame = next(iter(sheets.values()))
    header_rows = frame.index[
        frame.apply(
            lambda row: row.astype(str).str.contains("団体コード", regex=False).any(),
            axis=1,
        )
    ]
    if len(header_rows) == 0:
        return pd.DataFrame()
    header = int(header_rows[0])
    rows = frame.iloc[header + 1 :].copy()
    rows = rows.rename(columns={0: "muni_code", 1: "pref_name", 2: "muni_name", 5: "pop"})
    rows["muni_code"] = rows["muni_code"].astype(str).str.extract(r"(\d{5,6})", expand=False)
    rows["muni_code"] = rows["muni_code"].where(
        rows["muni_code"].str.len().ne(6),
        rows["muni_code"].str[:5],
    )
    rows["muni_name"] = rows["muni_name"].astype("string").map(normalize_municipality_name)
    rows["pop"] = pd.to_numeric(rows["pop"], errors="coerce")
    rows["pref_code"] = rows["muni_code"].str[:2]
    rows = rows.loc[rows["pref_code"].isin(PREFECTURES)].copy()
    rows["year"] = year
    rows["pop_ref_date"] = "01-01" if year >= 2013 else "03-31"
    rows["pop_scope"] = "total" if year >= 2013 else "japanese"
    return rows[
        [
            "pref_code",
            "muni_code",
            "muni_name",
            "year",
            "pop",
            "pop_ref_date",
            "pop_scope",
        ]
    ]


def acquire_population(sources: list[dict[str, str]]) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for year in range(2000, 2024):
        stat_id = discover_population_id(year, sources)
        if stat_id is None:
            continue
        url = f"{DOWNLOAD}?statInfId={stat_id}&fileKind=0"
        path = RAW / f"resident_register_{year}.xlsx"
        if download(
            url,
            path,
            sources,
            f"e-Stat resident-register municipal population {year}",
        ):
            frame = parse_population(path, year)
            if not frame.empty:
                frames.append(frame)
    return pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()


def normalize_municipality_name(value: object) -> str:
    if pd.isna(value):
        return ""
    name = unicodedata.normalize("NFKC", str(value))
    name = re.sub(r"\s+", "", name).replace("\u3000", "")
    name = re.sub(r"^.+郡(?=.{1,4}(?:町|村)$)", "", name)
    return name.replace("飯館村", "飯舘村")


class TableParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.rows: list[list[str]] = []
        self._row: list[str] | None = None
        self._cell: list[str] | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "tr":
            self._row = []
        elif tag in {"td", "th"} and self._row is not None:
            self._cell = []

    def handle_data(self, data: str) -> None:
        if self._cell is not None:
            self._cell.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"td", "th"} and self._cell is not None and self._row is not None:
            self._row.append("".join(self._cell))
            self._cell = None
        elif tag == "tr" and self._row is not None:
            self.rows.append([re.sub(r"\s+", " ", cell).strip() for cell in self._row])
            self._row = None


def acquire_mergers(
    vital: pd.DataFrame, sources: list[dict[str, str]]
) -> tuple[pd.DataFrame, pd.DataFrame]:
    path = RAW / "municipality_mergers_fukushima.html"
    if not download(
        MERGER_SOURCE,
        path,
        sources,
        "Ministry of Internal Affairs Fukushima municipal merger history",
    ):
        return vital, pd.DataFrame()
    parser = TableParser()
    parser.feed(path.read_bytes().decode("cp932", errors="replace"))
    code_lookup = (
        vital.assign(muni_name=vital["muni_name"].map(normalize_municipality_name))
        .sort_values("year")
        .drop_duplicates(["pref_code", "muni_name"], keep="last")
        .set_index(["pref_code", "muni_name"])["muni_code_observed"]
        .to_dict()
    )
    merger_rows: list[dict[str, object]] = []
    for row in parser.rows:
        if len(row) < 6 or row[0] != "福島県" or not row[2] or not row[3]:
            continue
        predecessor = normalize_municipality_name(row[1])
        successor = normalize_municipality_name(row[3])
        date_match = re.search(r"平成(\d+)年\s*(\d+)月\s*(\d+)日", row[2])
        if not date_match:
            continue
        effective_year = 1988 + int(date_match.group(1))
        predecessor_code = code_lookup.get(("07", predecessor))
        successor_code = code_lookup.get(("07", successor))
        if predecessor_code is None or successor_code is None:
            continue
        merger_rows.append(
            {
                "pref_code": "07",
                "successor_code": successor_code,
                "successor_name": successor,
                "predecessor_code": predecessor_code,
                "predecessor_name": predecessor,
                "effective_date": f"{effective_year}-{int(date_match.group(2)):02d}-{int(date_match.group(3)):02d}",
                "source_url": MERGER_SOURCE,
            }
        )
    mergers = pd.DataFrame(merger_rows).drop_duplicates()
    mergers.to_csv(DATA / "municipality_mergers.csv", index=False, encoding="utf-8")
    if mergers.empty:
        return vital, mergers
    vital = vital.copy()
    for (successor_code, successor_name, effective_date), group in mergers.groupby(
        ["successor_code", "successor_name", "effective_date"]
    ):
        cutoff = int(str(effective_date)[:4])
        predecessors = set(group["predecessor_code"])
        historical = vital.loc[
            vital["muni_code_observed"].isin(predecessors) & (vital["year"] < cutoff)
        ].copy()
        if historical.empty:
            continue
        aggregate = (
            historical.groupby(["pref_code", "year"], as_index=False)[["births", "deaths"]]
            .sum(min_count=1)
        )
        aggregate["muni_code_observed"] = successor_code
        aggregate["muni_name"] = successor_name
        vital = vital.loc[
            ~(
                vital["muni_code_observed"].isin(predecessors)
                & (vital["year"] < cutoff)
            )
        ]
        vital = pd.concat([vital, aggregate[vital.columns]], ignore_index=True)
    return vital, mergers


def harmonize_codes(
    vital: pd.DataFrame, population: pd.DataFrame, mergers: pd.DataFrame
) -> pd.DataFrame:
    if vital.empty:
        return vital
    latest = (
        vital.loc[vital["year"] == vital["year"].max(), ["pref_code", "muni_name", "muni_code_observed"]]
        .drop_duplicates()
        .rename(columns={"muni_code_observed": "current_code"})
    )
    vital = vital.merge(latest, on=["pref_code", "muni_name"], how="left")
    vital["muni_code"] = vital["current_code"].fillna(vital["muni_code_observed"])
    vital = vital.drop(columns=["current_code"])
    if not population.empty:
        population = population.copy()
        population["_priority"] = population["pop_ref_date"].map(
            lambda value: 1 if value == "10-01 (Census)" else 0
        )
        population = (
            population.sort_values("_priority")
            .drop_duplicates(["pref_code", "muni_name", "year"], keep="first")
            .drop(columns="_priority")
        )
        vital = vital.merge(
            population[
                [
                    "pref_code",
                    "muni_code",
                    "muni_name",
                    "year",
                    "pop",
                    "pop_ref_date",
                    "pop_scope",
                ]
            ],
            on=["pref_code", "muni_name", "year"],
            how="left",
            suffixes=("", "_population"),
        )
        if "pop_population" in vital.columns:
            vital["pop"] = vital["pop"].fillna(vital["pop_population"])
        vital["pop_ref_date"] = vital["pop_ref_date"].fillna(
            vital["year"].map(lambda year: "03-31" if year <= 2012 else "01-01")
        )
        vital["pop_scope"] = vital["pop_scope"].fillna(
            vital["year"].map(lambda year: "japanese" if year <= 2012 else "total")
        )
        vital = vital.drop(
            columns=["muni_code_population", "pop_population", "pop_scope_population"],
            errors="ignore",
        )
    else:
        vital["pop"] = pd.NA
        vital["pop_ref_date"] = vital["year"].map(
            lambda year: "03-31" if year <= 2012 else "01-01"
        )
        vital["pop_scope"] = vital["year"].map(
            lambda year: "japanese" if year <= 2012 else "total"
        )
    return vital


def acquire_age_structure(
    vital: pd.DataFrame, mergers: pd.DataFrame, sources: list[dict[str, str]]
) -> pd.DataFrame:
    page_urls = {
        2005: "http://www.pref.fukushima.lg.jp/sec/11045b/22028.html",
        2010: "http://www.pref.fukushima.lg.jp/sec/11045b/24953.html",
    }
    files: dict[int, str] = {2005: "/uploaded/attachment/15008.xls"}
    latest_codes = (
        vital.sort_values("year")
        .drop_duplicates(["pref_code", "muni_name"], keep="last")
        .set_index(["pref_code", "muni_name"])["muni_code_observed"]
        .to_dict()
    )
    predecessor_codes = (
        mergers.set_index("predecessor_name")["successor_code"].to_dict()
        if not mergers.empty
        else {}
    )
    output: list[dict[str, object]] = []
    for census_year, relative_path in files.items():
        page_url = page_urls[census_year]
        file_url = (
            relative_path
            if relative_path.startswith("http")
            else "https://www.pref.fukushima.lg.jp" + relative_path
        )
        path = RAW / f"census_age_structure_{census_year}.xls"
        if not download(
            file_url,
            path,
            sources,
            f"Fukushima municipal Census age structure {census_year}",
        ):
            continue
        frame = next(iter(pd.read_excel(path, sheet_name=None, header=None).values()))
        for _, row in frame.iterrows():
            if census_year == 2005:
                name_candidates = [
                    normalize_municipality_name(value)
                    for value in row.iloc[:4]
                    if not pd.isna(value)
                    and not str(value).strip().startswith("うち")
                ]
                name = next((value for value in name_candidates if value), "")
                total = parse_number(row.iloc[5])
                age65 = parse_number(row.iloc[30])
                age75 = parse_number(row.iloc[31])
            else:
                name = normalize_municipality_name(row.iloc[1])
                total = parse_number(row.iloc[2])
                age65 = sum(
                    value
                    for value in (parse_number(v) for v in row.iloc[68:104])
                    if value is not None
                )
                age75 = sum(
                    value
                    for value in (parse_number(v) for v in row.iloc[78:104])
                    if value is not None
                )
            if (
                not name
                or total in (None, 0)
                or "県" in name
                or "管内" in name
                or "市部" in name
                or "郡部" in name
                or "旧" in name
            ):
                continue
            muni_code = latest_codes.get(("07", name)) or predecessor_codes.get(name)
            if muni_code is None:
                continue
            if not str(muni_code).startswith("07"):
                continue
            output.append(
                {
                    "muni_code": muni_code,
                    "census_year": census_year,
                    "pop_total": total,
                    "share_65plus": age65 / total if age65 is not None else pd.NA,
                    "share_75plus": age75 / total if age75 is not None else pd.NA,
                }
            )
        record_source(
            sources,
            file_url,
            f"Fukushima municipal Census age structure {census_year}",
            "Prefecture statistical table downloaded and parsed; values are source-derived.",
        )
    for pref_code, stat_id in AGE_2010_IDS.items():
        file_url = f"{DOWNLOAD}?statInfId={stat_id}&fileKind=1"
        path = RAW / f"census_age_structure_2010_{pref_code}.csv"
        if not download(
            file_url,
            path,
            sources,
            f"e-Stat 2010 Census Table 3-2 {PREFECTURES[pref_code]}",
        ):
            continue
        try:
            text = path.read_bytes().decode("cp932", errors="replace")
            rows = list(csv.reader(io.StringIO(text)))
            for row in rows[11:]:
                if len(row) <= 138:
                    continue
                if len(row) <= 138 or row[6] != "danjo.0000" or row[7] != "0":
                    continue
                source_code = str(row[2]).strip()
                if not source_code.startswith(pref_code) or len(source_code) != 5:
                    continue
                if row[3] not in {"2", "3"}:
                    continue
                name = normalize_municipality_name(row[8])
                if not name or "県" in name or "市部" in name or "郡部" in name:
                    continue
                muni_code = latest_codes.get((pref_code, name), source_code)
                if not str(muni_code).startswith(pref_code):
                    continue
                total = parse_number(row[9])
                age65 = parse_number(row[137])
                age75 = parse_number(row[138])
                if total in (None, 0):
                    continue
                output.append(
                    {
                        "muni_code": muni_code,
                        "census_year": 2010,
                        "pop_total": total,
                        "share_65plus": age65 / total if age65 is not None else pd.NA,
                        "share_75plus": age75 / total if age75 is not None else pd.NA,
                    }
                )
        except Exception as exc:
            record_source(
                sources,
                file_url,
                f"e-Stat 2010 Census Table 3-2 {PREFECTURES[pref_code]}",
                f"not obtained: parse failed: {type(exc).__name__}: {exc}",
            )
            continue
        record_source(
            sources,
            file_url,
            f"e-Stat 2010 Census Table 3-2 {PREFECTURES[pref_code]}",
            "CSV downloaded and parsed; current municipality rows only (地域識別コード 2 or 3), source-prefecture constrained.",
        )
    age_output = pd.DataFrame(
        output,
        columns=[
            "muni_code",
            "census_year",
            "pop_total",
            "share_65plus",
            "share_75plus",
        ],
    ).drop_duplicates(["muni_code", "census_year"])
    age_output.to_csv(
        DATA / "census_age_structure.csv", index=False, encoding="utf-8"
    )
    return age_output


def acquire_smr(sources: list[dict[str, str]]) -> None:
    latest_url = f"{DOWNLOAD}?statInfId=000040174841&fileKind=0"
    latest_path = RAW / "smr_2018_2022_table1.xlsx"
    if download(
        latest_url,
        latest_path,
        sources,
        "e-Stat five-year municipal vital statistics, 2018-2022, Table 1",
    ):
        try:
            table = pd.read_excel(latest_path, sheet_name=0, header=None)
            table.to_csv(
                DATA / "smr_2018_2022_table1_source_extract.csv",
                index=False,
                header=False,
                encoding="utf-8",
            )
            record_source(
                sources,
                latest_url,
                "e-Stat five-year municipal vital statistics, 2018-2022, Table 1",
                "Workbook downloaded and exported without altering source cells; Table 1 contains the published SMR field.",
            )
        except Exception as exc:
            record_source(
                sources,
                latest_url,
                "e-Stat five-year municipal vital statistics, 2018-2022, Table 1",
                f"not obtained: workbook was downloaded but source export failed: {type(exc).__name__}: {exc}",
            )
    for year in (2007, 2012, 2017, 2022):
        url = (
            "https://www.e-stat.go.jp/stat-search/files?"
            f"cycle=7&layout=datalist&page=1&year={year}0"
            "&toukei=00450011&tstat=000001028897"
        )
        found = False
        try:
            for stat_id, context in listing_links(url):
                if "標準化死亡比" not in context:
                    continue
                kind = re.search(r"fileKind=(\d+)", context)
                file_kind = kind.group(1) if kind else "0"
                path = RAW / f"smr_{year}_{stat_id}.{ 'csv' if file_kind == '1' else 'xlsx'}"
                if download(
                    f"{DOWNLOAD}?statInfId={stat_id}&fileKind={file_kind}",
                    path,
                    sources,
                    f"e-Stat five-year standardized mortality ratio ending {year}",
                ):
                    found = True
                break
        except Exception as exc:
            record_source(
                sources,
                url,
                f"e-Stat SMR window ending {year}",
                f"not obtained: {type(exc).__name__}: {exc}",
            )
        if not found:
            record_source(
                sources,
                url,
                f"e-Stat SMR window ending {year}",
                "not obtained: no standardized-mortality-ratio download was discovered.",
            )


def acquire_reconstruction_deaths(sources: list[dict[str, str]]) -> None:
    pdf_path = RAW / "reconstruction_related_deaths_latest.pdf"
    if not download(
        RECONSTRUCTION_PDF,
        pdf_path,
        sources,
        "Reconstruction Agency earthquake-related deaths, latest PDF",
    ):
        return
    text_path = RAW / "reconstruction_related_deaths_latest.txt"
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        record_source(
            sources,
            RECONSTRUCTION_PDF,
            "Reconstruction Agency municipality-level related deaths extraction",
            "not obtained: pdftotext executable is unavailable.",
        )
        return
    subprocess.run([pdftotext, "-layout", str(pdf_path), str(text_path)], check=False)
    text = text_path.read_text(encoding="utf-8", errors="replace")
    rows = []
    for name in sorted(EVACUATION_MUNICIPALITIES):
        matches = re.findall(rf"(?m)^\s*{re.escape(name)}\s+([\d,]+)\s*$", text)
        if matches:
            rows.append({"muni_name": name, "related_deaths": int(matches[-1].replace(",", ""))})
    pd.DataFrame(rows, columns=["muni_name", "related_deaths"]).to_csv(
        DATA / "reconstruction_related_deaths_fukushima.csv",
        index=False,
        encoding="utf-8",
    )
    record_source(
        sources,
        RECONSTRUCTION_PDF,
        "Reconstruction Agency municipality-level related deaths extraction",
        "PDF downloaded and parsed with pdftotext; extracted values are PDF-extracted.",
    )


def write_evacuation_orders(sources: list[dict[str, str]]) -> None:
    download(
        "https://www.pref.fukushima.lg.jp/uploaded/attachment/254764.pdf",
        RAW / "evacuation_area_transition_before_2012.pdf",
        sources,
        "Fukushima Prefecture evacuation-area transition chronology through 2012-03-31",
    )
    download(
        EVACUATION_SUMMARY_PDF,
        RAW / "evacuation_area_lifting_summary_2025.pdf",
        sources,
        "Fukushima Prefecture evacuation-order lifting summary",
    )
    classifications = {
        "双葉町": ("警戒区域（20km）", "whole", "2020-03-04"),
        "大熊町": ("警戒区域（20km）", "whole", "2019-04-10"),
        "富岡町": ("警戒区域（20km）", "whole", "2017-04-01"),
        "浪江町": ("警戒区域・計画的避難区域", "partial", "2017-03-31"),
        "楢葉町": ("警戒区域・緊急時避難準備区域", "partial", "2015-09-05"),
        "川内村": ("警戒区域・緊急時避難準備区域", "partial", "2014-10-01"),
        "葛尾村": ("警戒区域・計画的避難区域", "partial", "2016-06-12"),
        "飯舘村": ("計画的避難区域", "whole", "2017-03-31"),
        "南相馬市": ("警戒区域・計画的避難区域・緊急時避難準備区域", "partial", "2016-07-12"),
        "田村市": ("緊急時避難準備区域", "partial", "2014-04-01"),
        "川俣町": ("計画的避難区域", "partial", "2017-03-31"),
        "広野町": ("緊急時避難準備区域", "whole", "2011-09-30"),
    }
    rows = []
    for name in sorted(EVACUATION_MUNICIPALITIES):
        designation_type, scope, lifting_date = classifications[name]
        rows.append(
            {
                "muni_name": name,
                "designation_date": "2011-04-22",
                "designation_type": designation_type,
                "whole_or_partial": scope,
                "lifting_date": lifting_date,
                "source_url": f"{FUKUSHIMA_ORDER_SOURCE};{METI_CLASSIFICATION_SOURCE};{EVACUATION_SUMMARY_PDF}",
                "notes": "2011-04-22 scope/type follows the official Fukushima transition explanation and METI classification; lifting_date is the first municipality-area lifting date shown in the Fukushima summary chronology, not necessarily the date all later special zones were lifted.",
            }
        )
    pd.DataFrame(rows).to_csv(DATA / "evacuation_orders.csv", index=False, encoding="utf-8")
    record_source(
        sources,
        METI_ORDER_SOURCE,
        "METI evacuation-order release index",
        "Municipality list recorded; the 2011-04-22 snapshot date is requested by the study. Exact municipality-level type, scope, and lifting dates remain not obtained.",
    )
    record_source(
        sources,
        FUKUSHIMA_ORDER_SOURCE,
        "Fukushima Prefecture evacuation-area transition page",
        "Official transition PDFs linked; the 2011-04-22 map and explanatory classification were used for municipality scope/type.",
    )
    record_source(
        sources,
        METI_CLASSIFICATION_SOURCE,
        "METI 2011-04-11 planned and emergency evacuation-area classification",
        "Official classification used to distinguish 計画的避難区域 and 緊急時避難準備区域, including whole/partial wording.",
    )
    record_source(
        sources,
        EVACUATION_SUMMARY_PDF,
        "Fukushima Prefecture evacuation-order lifting summary",
        "Official chronology used for the first lifting date recorded per municipality.",
    )


def write_panel(vital: pd.DataFrame, population: pd.DataFrame) -> None:
    if vital.empty:
        panel = pd.DataFrame(
            columns=[
                "pref_code",
                "muni_code",
                "muni_name",
                "year",
                "deaths",
                "births",
                "pop",
                "pop_ref_date",
                "pop_scope",
            ]
        )
    else:
        panel = vital.copy()
        panel = panel[
            [
                "pref_code",
                "muni_code",
                "muni_name",
                "year",
                "deaths",
                "births",
                "pop",
                "pop_ref_date",
                "pop_scope",
            ]
        ]
    panel.to_csv(DATA / "municipal_panel.csv", index=False, encoding="utf-8")
    panel.isna().sum().rename("missing_cells").to_csv(DATA / "municipal_panel_missingness.csv")
    summary = {
        "rows": int(len(panel)),
        "prefectures": sorted(panel["pref_code"].dropna().unique().tolist()) if len(panel) else [],
        "year_min": int(panel["year"].min()) if len(panel) else None,
        "year_max": int(panel["year"].max()) if len(panel) else None,
        "missing_cells": panel.isna().sum().to_dict(),
    }
    (DATA / "municipal_panel_summary.json").write_text(
        pd.Series(summary).to_json(indent=2, force_ascii=False),
        encoding="utf-8",
    )


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    sources: list[dict[str, str]] = []
    vital = acquire_vital(sources)
    population = acquire_population(sources)
    vital, mergers = acquire_mergers(vital, sources)
    age_structure = acquire_age_structure(vital, mergers, sources)
    if not age_structure.empty:
        code_names = (
            vital.sort_values("year")
            .drop_duplicates("muni_code_observed", keep="last")
            .set_index("muni_code_observed")["muni_name"]
        )
        census_population = age_structure[
            ["muni_code", "census_year", "pop_total"]
        ].rename(columns={"census_year": "year", "pop_total": "pop"})
        census_population["pref_code"] = census_population["muni_code"].str[:2]
        census_population["muni_name"] = census_population["muni_code"].map(code_names)
        census_population["pop_ref_date"] = "10-01 (Census)"
        census_population["pop_scope"] = "total"
        population = pd.concat(
            [population, census_population[
                [
                    "pref_code",
                    "muni_code",
                    "muni_name",
                    "year",
                    "pop",
                    "pop_ref_date",
                    "pop_scope",
                ]
            ]],
            ignore_index=True,
        )
    vital = harmonize_codes(vital, population, mergers)
    acquire_smr(sources)
    acquire_reconstruction_deaths(sources)
    write_evacuation_orders(sources)
    write_panel(vital, population)
    source_lines = [
        "# Fukushima data sources",
        "",
        f"Generated: {TODAY}",
        "",
        "| URL | Retrieval date | Table | Notes |",
        "|---|---|---|---|",
    ]
    source_lines.extend(
        f"| {row['url']} | {row['retrieval_date']} | {row['table']} | {row['notes']} |"
        for row in sources
    )
    source_lines.extend(
        [
            "",
            "## Coverage and harmonization notes",
            "",
            "- Annual vital-statistics rows are parsed from prefecture CSV files; births are column 2 and deaths column 4 in the source table.",
            "- Municipality names are Unicode-normalized and county prefixes are removed. Historical predecessor municipalities are aggregated into current successor codes using the official Ministry merger table.",
            "- Resident-register population reference dates are `03-31` through 2012 and `01-01` from 2013 onward. The pre-2013 tables are Japanese-resident counts (外国人 excluded); 2013 onward uses the 総計 tables.",
            "- `pop_scope` records `japanese` for pre-2013 resident-register tables and `total` for 2013 onward and Census endpoints.",
            "- Census fallback population endpoints for Fukushima are labeled `10-01 (Census)` in `pop_ref_date`; they are not substituted for unavailable resident-register observations in other prefectures.",
            "- No values are filled when a source is unavailable.",
            "- Evacuation-order scope/type follows the official 2011-04-22 map and classification; lifting_date records the first municipality-area lifting date in the official chronology and may precede later special-zone lifting.",
            "- Census age structure uses the official Fukushima prefecture 2005 table and 2010 e-Stat Table 3-2 files for all eight requested prefectures.",
        ]
    )
    (DATA / "SOURCES.md").write_text("\n".join(source_lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
