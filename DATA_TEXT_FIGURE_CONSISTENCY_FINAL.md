# Data–text–figure consistency final audit (Evidence & Policy)

All values checked against canonical outputs via `numbers.json`
(injection manifest) and `check_report_evidence_policy.md`
(independent re-derivation). Numbering follows the E&P layout:
4 main figures, 2 main tables, Supplement Figures S1–S4,
Supplement Tables S1–S5.

## Mapping

| Claim | Canonical | Text/Abstract | Table 1 | Figure 2 | Status |
| --- | --- | --- | --- | --- | --- |
| 50 pairs, 34 not robust (68%) | summary_table.csv | 50 / 34 / 68% | 50 / category counts | 68% + range | consistent |
| Sensitivity range | verdict_sensitivity_summary.csv [0.60,0.74] | "60% to 74%" | — | grid | consistent |
| Laffer p=0.06 (n=29); LNT p=0.15 (n=21; 6 <0.1 Gy) | summary_table rows | same | — | — | consistent |

## Fukushima

| Claim | Canonical | Text | Supp. Tables S1–S3 | Figures 3 / S3–S4 | Status |
| --- | --- | --- | --- | --- | --- |
| ATT −0.085 log pts ≈8%, perm p 0.001, pre-trend 0.314 | att_summary.csv | same | S3 | Fig 3, S3 | consistent |
| 2011: 2,996 obs / 2,060 exp / 936 excess / 732 direct / 204 residual | acute_2011_decomposition.csv | same | S4 | S4 bars | consistent |
| Spec grid −0.085…−0.057; T1w −0.129; T2 p≥0.421 | att_summary.csv | same | S3 | — | consistent |
| SC gap −0.060 (p 0.077), 25 donors, 8 negative | sc_*.csv | same | S2 | — | consistent |
| Related deaths 2,350 (2026-02-13); THJ 130 (15–1,100), 28 averted (3–245) | external files | same | S4 | — | consistent; estimands kept non-commensurate |

## Kansas

| Claim | Canonical | Text | Supp. Table S5 | Figure 4 / S2 | Status |
| --- | --- | --- | --- | --- | --- |
| IIT gap ≈27% (p 0.03); all-state 26% | analysis_summary.json | same | S5 | Fig 4 | consistent |
| Gap $91→$422 pc; cumulative ≈$4.6bn | same | same | S5 | — | consistent |
| Total tax 3.0% (p 0.18); GDP +1.5% (0.71); emp −1.3% (0.47) | same | same | S5 | — | consistent |
| Placebo p range 0.006–0.056; LOO −0.322…−0.291; pre-RMSPE 0.025 | same | S5 | S5 | S2 | consistent |

## Cross-application synthesis

Table 2 rows (decision sensitivity, consequence asymmetry,
reversibility, transportability, observability) are qualitative
restatements of material already presented in each application
subsection — no new quantities introduced; wording check passed.

## Verdict

CONSISTENT. No discrepancies between canonical data, text claims,
figures, and tables in the E&P package.
