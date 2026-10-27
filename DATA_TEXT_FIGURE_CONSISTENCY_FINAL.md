# Data–text–figure consistency final audit (JCPA)

All values checked against canonical outputs via `numbers.json`
(injection manifest) and `check_report_jcpa.md` (independent re-derivation).

## Mapping

| Claim | Canonical | Text/Abstract | Table 1 | Figure 3 | Status |
| --- | --- | --- | --- | --- | --- |
| 50 pairs, 34 not robust (68%) | summary_table.csv | 50 / 34 / 68% | 50 / category counts 27,4,1,2 | 68% + range | consistent |
| Sensitivity range | verdict_sensitivity_summary.csv [0.60,0.74] | "60% to 74%" | — | grid | consistent |
| Laffer p=0.06 (n=29); LNT p=0.15 (n=21; 6 <0.1 Gy) | summary_table rows | same | — | — | consistent |

## Fukushima

| Claim | Canonical | Text | Table 2/3 | Figures 4–6 | Status |
| --- | --- | --- | --- | --- | --- |
| ATT −0.085 log pts ≈8%, perm p 0.001, pre-trend 0.314 | att_summary.csv | same | same | event study | consistent |
| 2011: 2,996 obs / 2,060 exp / 936 excess / 732 direct / 204 residual | acute_2011_decomposition.csv | same | — | Fig 6 bars | consistent |
| Spec grid −0.085…−0.057; T1w −0.129; T2 p≥0.421 | att_summary.csv | same | same | — | consistent |
| SC gap −0.060 (p 0.077), 25 donors, 8 negative | sc_*.csv | same | — | — | consistent |
| Related deaths 2,350 (2026-02-13); THJ 130 (15–1,100), 28 averted (3–245) | external files | same | Table 3 | — | consistent; estimands kept non-commensurate |

## Kansas

| Claim | Canonical | Text | Table 4 | Fig 7 / A1 | Status |
| --- | --- | --- | --- | --- | --- |
| IIT gap ≈27% (p 0.03); all-state 26% | analysis_summary.json | same | same | Fig 7 | consistent |
| Gap $91→$422 pc; cumulative ≈$4.6bn | same | same | same | — | consistent |
| Total tax 3.0% (p 0.18); GDP +1.5% (0.71); emp −1.3% (0.47) | same | same | same | — | consistent |
| LOO −0.322…−0.291; pre-RMSPE 0.025; placebos 0.006–0.056, IIT 0.103 | same | same | same | — | consistent |

## Discrepancies found and corrected

| A | B | Cause | Correction |
| --- | --- | --- | --- |
| Abstract: "claimed fiscal response curve" | — | loaded wording flagged in Phase 10 | → "assumed tax-rate-revenue and growth-response relationships" (abstract + Introduction + cover letter) |
| Case selection: "reconstructed from public evidence" point | — | required wording absent | added to Case selection paragraph |
| numbers.json verbatim misses (alpha_grid, repo_url, etc.) | docx text | values used inside sentences/config, not displayed verbatim | accepted as notes, not failures |

No unresolved material numerical contradictions across text, tables,
figures, captions, appendix, cover letter.

## Appendix integration update

All cited Appendix items (Tables A1, A2; Figure A1) are now embedded in the
main manuscript Appendix section. Values unchanged; single numbers.json
source guarantees text/Appendix consistency.
