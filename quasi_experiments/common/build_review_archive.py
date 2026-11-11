"""Build a double-anonymous data, code, and reproducibility archive."""

from __future__ import annotations

import re
import shutil
import tempfile
import zipfile
import zlib
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[2]
QUASI = PROJECT / "quasi_experiments"
OUTPUT = PROJECT / "review_archive_policy_sciences.zip"
TEXT_SUFFIXES = {
    ".csv",
    ".json",
    ".md",
    ".py",
    ".txt",
    ".yaml",
    ".yml",
}
REPLACEMENTS = {
    "Tatsuki Onishi": "Anonymous Author",
    "Onishi Tatsuki": "Anonymous Author",
    "Onishi T.": "Anonymous Author",
    "Shiga University": "Anonymous Institution",
    "bougtoir@gmail.com": "anonymous@example.invalid",
    "https://github.com/bougtoir/canonical-curves-reexamination": (
        "https://example.invalid/anonymous-review-repository"
    ),
    "bougtoir": "anonymous-review",
}
IDENTITY_MARKERS = tuple(REPLACEMENTS)
LOCAL_PROJECT_PATH = re.compile(
    r"(?:[A-Za-z]:)?[/\\][^|\r\n]*?canonical_curves_reexamination[/\\]"
)


def copy_tree(source: Path, destination: Path) -> None:
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns(
            "__pycache__",
            "*.pyc",
            "*.docx",
            "*.pptx",
            "*.zip",
        ),
    )


def anonymize_text_files(root: Path) -> None:
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="strict")
        except UnicodeDecodeError:
            continue
        for source, replacement in REPLACEMENTS.items():
            text = text.replace(source, replacement)
        text = LOCAL_PROJECT_PATH.sub("", text)
        path.write_text(text, encoding="utf-8")


def assert_anonymous(root: Path) -> None:
    for path in root.rglob("*"):
        relative_path = str(path.relative_to(root))
        if any(
            marker.lower() in relative_path.lower() for marker in IDENTITY_MARKERS
        ):
            raise RuntimeError(f"Identity marker in archive filename: {path}")
        if not path.is_file():
            continue
        data = path.read_bytes()
        assert_anonymous_bytes(data, relative_path)
        if path.suffix.lower() in TEXT_SUFFIXES:
            text = data.decode("utf-8", errors="ignore").lower()
            if LOCAL_PROJECT_PATH.search(text):
                raise RuntimeError(
                    f"Local project path in archive content: {relative_path}"
                )
        if zipfile.is_zipfile(path):
            with zipfile.ZipFile(path) as archive:
                for name in archive.namelist():
                    if not name.endswith("/"):
                        assert_anonymous_bytes(
                            archive.read(name), f"{relative_path}!{name}"
                        )
        if path.suffix.lower() == ".pdf":
            for index, match in enumerate(
                re.finditer(rb"stream\r?\n(.*?)\r?\nendstream", data, flags=re.S)
            ):
                try:
                    stream = zlib.decompress(match.group(1))
                except zlib.error:
                    continue
                assert_anonymous_bytes(stream, f"{relative_path}!stream-{index}")


def assert_anonymous_bytes(data: bytes, location: str) -> None:
    lowered = data.lower()
    for encoding in ("utf-8", "utf-16-le", "utf-16-be"):
        for marker in IDENTITY_MARKERS:
            encoded_marker = marker.lower().encode(encoding)
            if encoded_marker in lowered:
                raise RuntimeError(
                    f"Identity marker in archive content: {location}"
                )


def write_readme(root: Path) -> None:
    (root / "README_REVIEW_ARCHIVE.txt").write_text(
        """Policy Sciences anonymous reproducibility archive

Contents
- data/, results/, scripts/: cross-domain mapping data, outputs, and analysis code.
- quasi_experiments/kansas/: Kansas source snapshots, processed data, code, and outputs.
- quasi_experiments/fukushima/: Fukushima source snapshots, processed data, code, and outputs.
- quasi_experiments/manuscript/: anonymized manuscript text and document generator.
- data/source_manifest.csv: cross-domain input paths, sizes, SHA-256 hashes,
  source URLs, timestamp basis, acquisition notes, and usage terms.
- quasi_experiments/*/data/raw_manifest.csv: source paths, sizes, SHA-256 hashes,
  timestamp basis, acquisition notes, and usage terms.

Reproduction
1. Create an isolated Python environment.
2. Install pinned packages:
   pip install -r requirements.txt
3. Rebuild the cross-domain mapping:
   python scripts/run_all_analyses.py
   python scripts/verdict_sensitivity.py
4. Rebuild the policy demonstrations and manuscript from this archive root:
   cd quasi_experiments
   make manuscript

Exact historical request times were not retained. The machine-readable
manifests therefore label the first repository commit as a UTC timestamp proxy.
One unused legacy Fukushima workbook predates the ledger and is not read by the
current analysis.
""",
        encoding="utf-8",
    )


def main() -> None:
    with tempfile.TemporaryDirectory() as temporary:
        staging = Path(temporary) / "review_archive"
        staging.mkdir()
        for directory in ("data", "results", "scripts"):
            copy_tree(PROJECT / directory, staging / directory)
        shutil.copy2(PROJECT / "README.md", staging / "README.md")
        quasi_staging = staging / "quasi_experiments"
        quasi_staging.mkdir()
        for directory in ("common", "kansas", "fukushima"):
            copy_tree(QUASI / directory, quasi_staging / directory)
        manuscript_staging = quasi_staging / "manuscript"
        manuscript_staging.mkdir()
        for filename in (
            "build_manuscript.py",
            "build_finish_pass.py",
            "check_manuscript.py",
            "text_policy_sciences.py",
            "numbers.json",
        ):
            shutil.copy2(QUASI / "manuscript" / filename, manuscript_staging / filename)
        shutil.copy2(QUASI / "requirements.txt", staging / "requirements.txt")
        shutil.copy2(QUASI / "Makefile", quasi_staging / "Makefile")
        write_readme(staging)
        anonymize_text_files(staging)
        assert_anonymous(staging)

        OUTPUT.unlink(missing_ok=True)
        with zipfile.ZipFile(
            OUTPUT, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9
        ) as archive:
            for path in sorted(staging.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(staging))


if __name__ == "__main__":
    main()
