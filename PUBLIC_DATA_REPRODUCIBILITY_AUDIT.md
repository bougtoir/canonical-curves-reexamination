# Public data reproducibility audit (JCPA)

Commands executed this session in a fresh venv (`python3 -m venv .venv;
pip install -r requirements.txt`; Ubuntu Linux):

    make manuscript JOURNAL=jcpa      # acquire (skip) → analyze → manifests → build → check
    make final_package JOURNAL=jcpa   # + review archive + finish pass + zip

## Cross-domain mapping

| Output | Status | Evidence |
| --- | --- | --- |
| 50 relationship-dataset pairs | PASS (canonical preserved) | `results/summary_table.csv` = 50 rows; `full_results.json` = 50 entries; exclusion of 2 pairs documented in `results/SOURCES.md` and `run_all_analyses.py` header |
| 34/50 (68%) not-robust at default criteria | PASS-TOLERANCE | Re-derived from `summary_table.csv` Verdict column = 34 non-ROBUST_NONLINEAR; matches `numbers.json` and manuscript |
| Sensitivity range 60–74% | PASS | `verdict_sensitivity_summary.csv` share_not_robust ∈ [0.60, 0.74] over alpha {0.01,0.05,0.10} × k {1..5}; matches text |
| Table 1 / Figures 2–3 | PASS | `tab_audit`, `fig_decision_tree`, `fig_sensitivity` regenerated from these files by `build_manuscript.py` |
| Regeneration from live APIs | PARTIAL | `scripts/run_all_analyses.py` + fetchers depend on live public APIs (World Bank etc.); the audit uses the preserved canonical outputs and the archived `data/` snapshots + `source_manifest.csv`. A later provider update cannot silently change the reported results |

## Fukushima

| Output | Status | Evidence |
| --- | --- | --- |
| Panel build from e-Stat raw CSVs | PASS (snapshot) | 229-file raw snapshot under `fukushima/data/raw/` + `raw_manifest.csv` (SHA-256) + `SOURCES.md` URL/retrieval ledger; acquisition step skipped because the snapshot exists |
| DiD ATT grid | PASS-TOLERANCE | `analyze_fukushima.py` re-executed this session; regenerated `att_summary.csv` identical to committed file within ~1e-13 float noise (T1 ATT −0.085 log pts; perm p 0.001) |
| Permutation / pre-trend p | PASS-TOLERANCE | same run (deterministic seeds) |
| 2011 decomposition (2,996/2,060/936/732/204) | PASS-TOLERANCE | regenerated `acute_2011_decomposition.csv` equal at reported precision |
| Synthetic-control aggregates | PASS-TOLERANCE | regenerated `sc_*.csv` equal at reported precision |
| Figures 4–6, Appendix A1–A2 | PASS | rebuilt by `build_manuscript.py` |

## Kansas

| Output | Status | Evidence |
| --- | --- | --- |
| State panel from FRED | PASS (snapshot) | 309-file raw snapshot + `raw_manifest.csv` + `SOURCES.md` (FRED series IDs + retrieval dates) + `fred_id_check.json` |
| Synthetic-control IIT gap ≈27% (p 0.03) | PASS-TOLERANCE | `analyze_kansas.py` re-executed; headline values identical at reported precision; LOO range/pre-RMSPE equal within 1e-9 |
| Total tax, GDP, employment gaps + p | PASS-TOLERANCE | same run |
| In-time placebos / neighboring-state event study | PASS-TOLERANCE | same run |
| Figure 7 / Appendix Figure A1 | PASS | rebuilt by `build_manuscript.py` |

## Known limitations

- Live-source reacquisition was not re-run (snapshots preserved instead): e-Stat and FRED series may have been revised upstream; the archived snapshots + manifests fix the exact inputs used.
- `review_archive_policy_sciences.zip` regenerates the double-anonymous code tree; contents verified in prior audit.

No FAIL on any principal result.
