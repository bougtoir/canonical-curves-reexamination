# Public-data reproducibility audit — FINAL (Evidence & Policy)

## Local raw-data persistence

- `kansas/data/raw_manifest.csv`: 309 files verified — SHA-256, size,
  source URL, acquisition conditions, usage terms, timestamp precision
  all present; 0 unmatched, 0 legacy-unknown.
- `fukushima/data/raw_manifest.csv`: 229 files verified; 1 unused
  legacy file whose source metadata is unavailable (disclosed, unused).
- `data/source_manifest.csv` (cross-domain mapping inputs): 49 files
  verified.
- All manifests re-checked during `check_manuscript.py` run for this
  package — see `manuscript/check_report_evidence_policy.md`.

## Public archive

- Public mirror: https://github.com/bougtoir/canonical-curves-reexamination
  (topic-named, no journal name — per repo-naming rule).
- Contains: mapping pipeline, case pipelines, canonical outputs
  (`numbers.json` sources), figure/table generators, manuscript
  builders, raw-data manifests.
- Not redistributed where terms forbid it: raw files whose usage terms
  bar republication are represented by source URL + checksum +
  acquisition script, not file copies (consistent with manifest
  `usage_terms` fields).

## Reproduction path

1. Clone public repo → run mapping pipeline → regenerates the
   50-pair diagnostic and Figure 2/Table 1 inputs.
2. Run `fukushima` and `kansas` pipelines from manifests → regenerates
   all ATT/SC estimates quoted.
3. `JOURNAL=evidence_policy python manuscript/build_manuscript.py`
   → regenerates this package's DOCX/PPTX outputs byte-comparable.

## Changes vs previous (JCPA) package

None to data or analyses. The retarget touched text, structure,
packaging, and citation format only; manifests and canonical outputs
are bit-identical to the audited JCPA package.

## Verdict

PASS. All quoted values reproduce from cited public data via the
public pipeline; persistence and ledger rules satisfied.
