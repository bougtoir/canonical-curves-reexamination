"""Build checksum manifests for archived Kansas and Fukushima source files."""

from __future__ import annotations

import csv
import hashlib
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parent
PROJECTS = ("kansas", "fukushima")

WORLD_BANK = "https://api.worldbank.org/v2/"
CROSS_DOMAIN_SOURCE_URLS = {
    "alcohol_mortality_real.csv": "https://doi.org/10.1001/archinte.166.22.2437",
    "balassa_samuelson_real.csv": "https://www.rug.nl/ggdc/productivity/pwt/",
    "barker_real.csv": "https://doi.org/10.1136/bmj.307.6918.1519",
    "beveridge_real.csv": "https://www.bls.gov/developers/",
    "bmi_mortality_real.csv": "https://doi.org/10.1016/S0140-6736(16)30175-1",
    "body_weight_setpoint_real.csv": (
        "https://doi.org/10.1056/NEJM199503093321001"
    ),
    "bongaarts_feeney_real.csv": "https://doi.org/10.2307/2807974",
    "coale_trussell_real.csv": "https://www.jstor.org/stable/2731143",
    "crime_temperature_real.csv": (
        "https://data.cityofchicago.org/resource/ijzp-q8t2.json; "
        "https://www.ncei.noaa.gov/pub/data/ghcn/daily/by_station/"
    ),
    "demographic_transition_real.csv": WORLD_BANK,
    "dunning_kruger_real.csv": (
        "https://doi.org/10.1037/0022-3514.77.6.1121"
    ),
    "duverger_real.csv": "https://mattgolder.com/elections",
    "easterlin_real.csv": (
        "https://ourworldindata.org/grapher/happiness-cantril-ladder.csv; "
        f"{WORLD_BANK}"
    ),
    "ebbinghaus_real.csv": (
        "https://psychclassics.yorku.ca/Ebbinghaus/memory7.htm"
    ),
    "ekc_co2_real.csv": WORLD_BANK,
    "engel_real.csv": (
        "https://ourworldindata.org/grapher/"
        "share-of-consumer-expenditure-spent-on-food.csv; "
        f"{WORLD_BANK}"
    ),
    "forest_transition_real.csv": WORLD_BANK,
    "fries_real.csv": "https://doi.org/10.1056/NEJM198007173030304",
    "global_cereal_yield.csv": WORLD_BANK,
    "gravity_real.csv": "https://www.cepii.fr/CEPII/en/bdd_modele/bdd_modele_item.asp?id=8",
    "great_gatsby_real.csv": (
        "https://datacatalog.worldbank.org/search/dataset/0066878; "
        "https://ourworldindata.org/grapher/economic-inequality-gini-index.csv"
    ),
    "gutenberg_richter_real.csv": (
        "https://earthquake.usgs.gov/fdsnws/event/1/"
    ),
    "hanpp_real.csv": (
        "https://doi.org/10.1073/pnas.0704243104; "
        "https://naciscdn.org/naturalearth/110m/cultural/"
    ),
    "happiness_u_real.csv": "https://doi.org/10.1073/pnas.1003744107",
    "hubbert_real.csv": "https://api.eia.gov/v2/total-energy/data/",
    "hubble_real.csv": (
        "https://raw.githubusercontent.com/behrouzz/astrodatascience/"
    ),
    "j_curve_real.csv": WORLD_BANK,
    "jevons_real.csv": "https://api.eia.gov/v2/total-energy/data/",
    "keeling_real.csv": (
        "https://gml.noaa.gov/webdata/ccgg/trends/co2/co2_annmean_mlo.csv"
    ),
    "kleiber_real.csv": "https://genomics.senescence.info/species/",
    "kuznets_curve_real.csv": WORLD_BANK,
    "laffer_real.csv": (
        "https://stats.oecd.org/SDMX-JSON/data/TABLE_I7/; "
        "https://sdmx.oecd.org/public/rest/data/"
    ),
    "lee_carter_real.csv": "https://www.mortality.org/",
    "lipset_real.csv": "https://freedomhouse.org/report/freedom-world",
    "lnt_real.csv": "https://doi.org/10.1667/RR2629.1",
    "mckeown_real.csv": "https://doi.org/10.1080/00324728.1975.10412707",
    "mitscherlich_real.csv": (
        "https://doi.org/10.2134/agronj1971.00021962006300010008x"
    ),
    "moores_law_real.csv": (
        "https://raw.githubusercontent.com/karlrupp/"
        "microprocessor-trend-data/master/50yrs/transistors.dat"
    ),
    "omran_real.csv": "https://hdr.undp.org/data-center/documentation-and-downloads",
    "preston_curve_real.csv": WORLD_BANK,
    "putnam_real.csv": (
        "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/; "
        "https://ourworldindata.org/grapher/self-reported-trust-attitudes.csv"
    ),
    "rahn_real.csv": (
        "https://ourworldindata.org/grapher/historical-gov-spending-gdp.csv; "
        f"{WORLD_BANK}"
    ),
    "replacement_migration_real.csv": (
        "https://www.un.org/development/desa/pd/sites/www.un.org.development."
        "desa.pd/files/files/documents/2020/Jan/"
        "un_2001_replacementmigration.pdf"
    ),
    "species_area_real.csv": (
        "https://cran.r-project.org/src/contrib/faraway_1.0.9.tar.gz"
    ),
    "us_macro_timeseries.csv": WORLD_BANK,
    "vitamin_d_real.csv": "https://doi.org/10.1210/jc.2012-1176",
    "wilkinson_real.csv": "https://doi.org/10.1136/bmj.304.6820.165",
    "world_bank_data.csv": WORLD_BANK,
    "zipf_cities_real.csv": "https://api.census.gov/data/2020/dec/pl",
}


def read_sources(path: Path) -> list[dict[str, str]]:
    records: list[dict[str, str]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) != 4 or parts[0] in {"URL", "---"}:
            continue
        records.append(
            {
                "url": parts[0],
                "retrieval_date": parts[1],
                "table": parts[2],
                "notes": parts[3],
            }
        )
    return records


def source_for_file(
    raw_file: Path, records: list[dict[str, str]]
) -> dict[str, str] | None:
    basename = raw_file.name
    if basename == "stc_historical.xlsx":
        source = next(
            (
                record
                for record in records
                if record["table"] == "Census STC historical database"
                and "not obtained" not in record["notes"]
            ),
            None,
        )
        derived = next(
            (
                record
                for record in records
                if record["table"] == "Census STC extracted items"
            ),
            None,
        )
        if source and derived:
            matched = source.copy()
            matched["table"] = derived["table"]
            matched["notes"] = derived["notes"]
            return matched

    direct = [
        record
        for record in records
        if basename in record["url"] or basename in record["notes"]
    ]
    if direct:
        return direct[0]

    if raw_file.suffix == ".txt":
        pdf_name = raw_file.with_suffix(".pdf").name
        parent_matches = [
            record
            for record in records
            if pdf_name in record["url"] or pdf_name in record["notes"]
        ]
        if parent_matches:
            parent = parent_matches[-1].copy()
            parent["notes"] = (
                f"Derived with pdftotext from {pdf_name}. " + parent["notes"]
            )
            return parent

    fred_match = re.search(r"_([A-Z0-9]+)\.csv$", basename)
    if basename.startswith("fred_") and fred_match:
        series = fred_match.group(1)
        matches = [
            record for record in records if f"fredgraph.csv?id={series}" in record["url"]
        ]
        if matches:
            return matches[0]

    if basename == "stc_layout.json":
        matches = [
            record
            for record in records
            if record["table"] == "Census STC historical database"
            and "not obtained" not in record["notes"]
        ]
        if matches:
            return matches[0]
    if basename == "census_age_structure_2010.xls":
        return {
            "url": "UNKNOWN_LEGACY_UNUSED",
            "retrieval_date": "",
            "table": "Legacy Fukushima age-structure workbook",
            "notes": (
                "Archived before the current acquisition ledger; not read by the current "
                "analysis, which uses the prefecture CSV snapshots."
            ),
        }
    return None


def usage_terms(url: str) -> str:
    if "fred.stlouisfed.org" in url:
        return (
            "FRED terms of use and the original data provider's terms apply; "
            "see https://fred.stlouisfed.org/legal/."
        )
    if "census.gov" in url:
        return (
            "U.S. Census Bureau public data; provider attribution and source-specific "
            "terms apply."
        )
    if any(
        domain in url
        for domain in (
            "e-stat.go.jp",
            "go.jp",
            "pref.fukushima.lg.jp",
            "soumu.go.jp",
            "meti.go.jp",
            "reconstruction.go.jp",
        )
    ):
        return (
            "Japanese government public information; provider terms at the source URL "
            "apply."
        )
    return (
        "Publicly accessible reference copy; copyright and provider-specific terms "
        "remain with the source."
    )


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def repository_first_seen(path: Path) -> str:
    completed = subprocess.run(
        [
            "git",
            "log",
            "--diff-filter=A",
            "--format=%cI",
            "--",
            str(path.relative_to(ROOT.parent.parent)),
        ],
        cwd=ROOT.parent.parent,
        check=False,
        capture_output=True,
        text=True,
    )
    timestamps = [line for line in completed.stdout.splitlines() if line]
    return timestamps[-1] if timestamps else ""


def existing_manifest_timestamp(path: Path) -> str:
    if not path.exists():
        return ""
    with path.open(encoding="utf-8", newline="") as stream:
        for row in csv.DictReader(stream):
            if row.get("acquisition_timestamp_utc"):
                return row["acquisition_timestamp_utc"]
    return ""


def build_manifest(project: str) -> None:
    data_dir = ROOT / project / "data"
    raw_dir = data_dir / "raw"
    records = read_sources(data_dir / "SOURCES.md")
    manifest_path = data_dir / "raw_manifest.csv"
    source_ledger_first_seen = repository_first_seen(
        data_dir / "SOURCES.md"
    ) or existing_manifest_timestamp(manifest_path)
    rows: list[dict[str, str | int]] = []
    for raw_file in sorted(path for path in raw_dir.iterdir() if path.is_file()):
        source = source_for_file(raw_file, records)
        if source is None:
            source = {
                "url": "UNMATCHED",
                "retrieval_date": "",
                "table": "",
                "notes": "No source row matched this archived file.",
            }
        retrieval_date = source["retrieval_date"]
        acquisition_timestamp = source_ledger_first_seen if retrieval_date else ""
        rows.append(
            {
                "path": str(raw_file.relative_to(ROOT)),
                "bytes": raw_file.stat().st_size,
                "sha256": sha256(raw_file),
                "source_url": source["url"],
                "data_identifier": source["table"],
                "acquisition_timestamp_utc": acquisition_timestamp,
                "timestamp_precision": (
                    "repository-first-seen proxy; source ledger records retrieval date "
                    f"{retrieval_date}"
                    if retrieval_date
                    else "unknown"
                ),
                "acquisition_conditions": (
                    "Archived source snapshot. The original ledger recorded only the "
                    "retrieval date; the UTC timestamp is the first repository commit "
                    "containing that ledger, not a fabricated request time. Request and "
                    "parsing notes are recorded in data/SOURCES.md."
                ),
                "usage_terms": usage_terms(source["url"]),
                "source_notes": source["notes"],
            }
        )

    fieldnames = list(rows[0])
    with manifest_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def build_cross_domain_manifest() -> None:
    data_dir = PROJECT_ROOT / "data"
    manifest_path = data_dir / "source_manifest.csv"
    fallback_timestamp = repository_first_seen(
        data_dir / "source_metadata.csv"
    ) or existing_manifest_timestamp(manifest_path)
    rows: list[dict[str, str | int]] = []
    source_files = sorted(
        path
        for path in data_dir.glob("*.csv")
        if path.name not in {"source_manifest.csv", "source_metadata.csv"}
    )
    for source_file in source_files:
        source_url = CROSS_DOMAIN_SOURCE_URLS.get(source_file.name, "")
        if not source_url:
            raise RuntimeError(f"No source URL recorded for {source_file.name}")
        acquisition_timestamp = (
            repository_first_seen(source_file) or fallback_timestamp
        )
        rows.append(
            {
                "path": str(source_file.relative_to(PROJECT_ROOT)),
                "bytes": source_file.stat().st_size,
                "sha256": sha256(source_file),
                "source_url": source_url,
                "data_identifier": source_file.stem,
                "acquisition_timestamp_utc": acquisition_timestamp,
                "timestamp_precision": (
                    "repository-first-seen proxy; exact request time was not retained"
                ),
                "acquisition_conditions": (
                    "Persistent analysis-input snapshot. The UTC timestamp is the first "
                    "repository commit containing this file, not a fabricated request "
                    "time. Source versions, transformations, and variable definitions are "
                    "documented in data/source_metadata.csv, "
                    "data/digitized_sources.md, and the acquisition scripts."
                ),
                "usage_terms": usage_terms(source_url),
                "source_notes": (
                    "The archived CSV is the input consumed by the reproducibility "
                    "pipeline; provider-specific attribution and transformation details "
                    "are recorded in the project source documentation."
                ),
            }
        )

    with manifest_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream, fieldnames=list(rows[0]), lineterminator="\n"
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    build_cross_domain_manifest()
    for project in PROJECTS:
        build_manifest(project)


if __name__ == "__main__":
    main()
