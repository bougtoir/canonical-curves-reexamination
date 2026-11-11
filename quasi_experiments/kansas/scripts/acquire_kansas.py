"""Download and assemble the Kansas state panel without hand-entered observations."""

from __future__ import annotations

import datetime as dt
import io
import json
import re
import zipfile
from pathlib import Path

import pandas as pd
import requests


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
DATA = ROOT / "data"
START_YEAR, END_YEAR = 1997, 2023
TODAY = dt.date.today().isoformat()
FRED_URL = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}"
STC_PAGE = "https://www.census.gov/programs-surveys/stc/data/datasets.html"

STATES = {
    "AL": "01", "AK": "02", "AZ": "04", "AR": "05", "CA": "06",
    "CO": "08", "CT": "09", "DE": "10", "DC": "11", "FL": "12",
    "GA": "13", "HI": "15", "ID": "16", "IL": "17", "IN": "18",
    "IA": "19", "KS": "20", "KY": "21", "LA": "22", "ME": "23",
    "MD": "24", "MA": "25", "MI": "26", "MN": "27", "MS": "28",
    "MO": "29", "MT": "30", "NE": "31", "NV": "32", "NH": "33",
    "NJ": "34", "NM": "35", "NY": "36", "NC": "37", "ND": "38",
    "OH": "39", "OK": "40", "OR": "41", "PA": "42", "RI": "44",
    "SC": "45", "SD": "46", "TN": "47", "TX": "48", "UT": "49",
    "VT": "50", "VA": "51", "WA": "53", "WV": "54", "WI": "55",
    "WY": "56",
}
FRED_SUFFIXES = {
    "rgdp": "RGSP",
    "ngdp": "NGSP",
    "pop": "POP",
    "pinc": "OTOT",
    "nonfarm_emp": "NA",
    "unemp_rate": "UR",
}


def get(url: str, **kwargs) -> requests.Response:
    response = requests.get(url, timeout=90, **kwargs)
    response.raise_for_status()
    return response


def record_source(lines: list[str], url: str, table: str, notes: str) -> None:
    lines.append(f"| {url} | {TODAY} | {table} | {notes} |")


def download_fred(series: str, destination: Path, sources: list[str], table: str) -> bool:
    url = FRED_URL.format(series=series)
    try:
        response = get(url)
        if response.text.lstrip().startswith("<!DOCTYPE") or "observation_date" not in response.text:
            raise ValueError("response did not contain a FRED CSV header")
        destination.write_text(response.text, encoding="utf-8")
        record_source(sources, url, table, f"Raw FRED CSV for {series}.")
        return True
    except Exception as exc:
        record_source(sources, url, table, f"not obtained: {type(exc).__name__}: {exc}")
        return False


def fred_id_for(abbr: str, suffix: str) -> str:
    return f"{abbr}{suffix}"


def read_fred(path: Path, value_name: str) -> pd.DataFrame:
    frame = pd.read_csv(path)
    date_col = "observation_date"
    value_col = [c for c in frame.columns if c != date_col][0]
    frame["year"] = pd.to_datetime(frame[date_col]).dt.year
    frame[value_name] = pd.to_numeric(frame[value_col], errors="coerce")
    return frame.loc[frame["year"].between(START_YEAR, END_YEAR), ["year", value_name]]


def discover_stc(sources: list[str]) -> Path | None:
    try:
        html = get(STC_PAGE).text
    except Exception as exc:
        record_source(sources, STC_PAGE, "Census STC historical database", f"not obtained: {exc}")
        return None
    hrefs = re.findall(r"""href=["']([^"']+)["']""", html, flags=re.I)
    candidates = []
    for href in hrefs:
        full = requests.compat.urljoin(STC_PAGE, href)
        if re.search(r"(STC[_-]?Historical|historical.*(zip|xlsx|xls|csv)|STC.*\.(zip|xlsx|xls|csv))", full, re.I):
            candidates.append(full)
    if not candidates:
        record_source(sources, STC_PAGE, "Census STC historical database", "not obtained: no downloadable historical link found on page")
        return None
    for url in candidates:
        try:
            response = get(url)
            suffix = ".zip" if url.lower().split("?")[0].endswith(".zip") else Path(url.split("?")[0]).suffix.lower()
            if suffix not in {".zip", ".xlsx", ".xls", ".csv"}:
                suffix = ".bin"
            destination = RAW / f"stc_historical{suffix}"
            destination.write_bytes(response.content)
            record_source(sources, url, "Census STC historical database", f"Downloaded candidate linked from {STC_PAGE}.")
            return destination
        except Exception as exc:
            record_source(sources, url, "Census STC historical database", f"not obtained: {exc}")
    return None


def extract_stc(path: Path | None, sources: list[str]) -> pd.DataFrame:
    if path is None:
        return pd.DataFrame(columns=["state", "year", "tax_total", "tax_indiv_inc", "tax_corp_inc", "tax_sales"])
    try:
        if path.suffix == ".zip":
            with zipfile.ZipFile(path) as archive:
                members = [m for m in archive.namelist() if Path(m).suffix.lower() in {".csv", ".xlsx", ".xls"}]
                if not members:
                    raise ValueError("zip contained no csv/xls/xlsx member")
                member = members[0]
                raw = archive.read(member)
                if Path(member).suffix.lower() == ".csv":
                    sheets = {"csv": pd.read_csv(io.BytesIO(raw), header=None)}
                else:
                    sheets = pd.read_excel(io.BytesIO(raw), sheet_name=None, header=None)
        elif path.suffix == ".csv":
            sheets = {"csv": pd.read_csv(path, header=None)}
        else:
            sheets = pd.read_excel(path, sheet_name=None, header=None)
    except Exception as exc:
        record_source(sources, str(path), "Census STC extracted items", f"not obtained: {type(exc).__name__}: {exc}")
        return pd.DataFrame(columns=["state", "year", "tax_total", "tax_indiv_inc", "tax_corp_inc", "tax_sales"])

    # The historical DB has changed layouts; retain a machine-readable layout dump.
    layout = []
    for sheet, frame in sheets.items():
        layout.append({"sheet": sheet, "rows": int(frame.shape[0]), "columns": int(frame.shape[1]), "sample": frame.iloc[:8, :12].fillna("").astype(str).values.tolist()})
    (RAW / "stc_layout.json").write_text(json.dumps(layout, ensure_ascii=False, indent=2), encoding="utf-8")
    record_source(
        sources,
        str(path),
        "Census STC extracted items",
        "Parsed exact item columns C105 (Total Taxes; no T00 column), T40, T41, and T09; state identified from Name.",
    )
    frame = next(iter(sheets.values())).copy()
    frame.columns = frame.iloc[0].astype(str).str.strip()
    frame = frame.iloc[2:].copy()
    frame["year"] = pd.to_numeric(frame["Year"], errors="coerce")
    frame["state"] = frame["Name"].astype(str).str.extract(r"^([A-Z]{2}) STATE GOVT", expand=False)
    frame = frame.loc[
        frame["state"].isin(STATES) & frame["year"].between(START_YEAR, END_YEAR)
    ].copy()
    output = pd.DataFrame({"state": frame["state"], "year": frame["year"].astype(int)})
    for source_column, output_column in {
        "C105": "tax_total",
        "T40": "tax_indiv_inc",
        "T41": "tax_corp_inc",
        "T09": "tax_sales",
    }.items():
        output[output_column] = pd.to_numeric(frame[source_column].replace({"X": pd.NA, "": pd.NA}), errors="coerce").to_numpy()
    return output


def annual_fred_state(abbr: str, sources: list[str], id_check: dict) -> pd.DataFrame:
    all_frames = []
    for value_name, suffix in FRED_SUFFIXES.items():
        series = fred_id_for(abbr, suffix)
        path = RAW / f"fred_{abbr}_{value_name}_{series}.csv"
        ok = download_fred(series, path, sources, f"FRED {value_name} {abbr}")
        id_check.setdefault(abbr, {})[value_name] = {"series": series, "obtained": ok}
        if ok:
            frame = read_fred(path, value_name)
            # GDP, population, and personal income are annual in the state series;
            # mean aggregation is safe if an endpoint ever returns subannual data.
            frame = frame.groupby("year", as_index=False)[value_name].mean()
        else:
            frame = pd.DataFrame(columns=["year", value_name])
        all_frames.append(frame)
    out = all_frames[0]
    for frame in all_frames[1:]:
        out = out.merge(frame, on="year", how="outer")
    return out


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    DATA.mkdir(parents=True, exist_ok=True)
    sources = [
        "# Kansas state-panel data provenance",
        "",
        f"Generated by `{Path(__file__).name}` on {TODAY}. Raw observations are downloaded, never hand-entered.",
        "",
        "| URL | Retrieval date | Table/series | Notes |",
        "|---|---|---|---|",
    ]
    id_check: dict = {}
    state_frames = []
    for abbr in STATES:
        frame = annual_fred_state(abbr, sources, id_check)
        frame.insert(0, "state", abbr)
        frame.insert(1, "fips", STATES[abbr])
        state_frames.append(frame)
    cpi_path = RAW / "fred_US_CPIAUCSL.csv"
    if download_fred("CPIAUCSL", cpi_path, sources, "FRED national CPI-U"):
        cpi = read_fred(cpi_path, "cpi")
        cpi = cpi.groupby("year", as_index=False)["cpi"].mean()
    else:
        cpi = pd.DataFrame(columns=["year", "cpi"])

    stc_path = discover_stc(sources)
    stc = extract_stc(stc_path, sources)
    panel = pd.concat(state_frames, ignore_index=True).merge(cpi, on="year", how="left")
    panel = panel.merge(stc, on=["state", "year"], how="left")
    columns = [
        "state", "fips", "year", "rgdp", "ngdp", "pop", "pinc", "nonfarm_emp",
        "unemp_rate", "tax_total", "tax_indiv_inc", "tax_corp_inc", "tax_sales", "cpi",
    ]
    for column in columns:
        if column not in panel:
            panel[column] = pd.NA
    panel = panel[columns].sort_values(["state", "year"]).reset_index(drop=True)
    panel.to_csv(DATA / "state_panel.csv", index=False)
    (DATA / "fred_id_check.json").write_text(json.dumps(id_check, indent=2), encoding="utf-8")
    missing = panel.isna().sum().rename("missing_cells").to_frame()
    missing.to_csv(DATA / "state_panel_missingness.csv")
    (DATA / "state_panel_summary.json").write_text(
        json.dumps(
            {
                "rows": int(len(panel)),
                "columns": columns,
                "year_min": int(panel["year"].min()),
                "year_max": int(panel["year"].max()),
                "states": int(panel["state"].nunique()),
                "missing_cells": {k: int(v) for k, v in missing["missing_cells"].items()},
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    (DATA / "SOURCES.md").write_text("\n".join(sources) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
