# Hardcode and numeric provenance audit — FINAL (Evidence & Policy)

## Injection architecture

Every empirical value in `text_evidence_policy.py` is a `{placeholder}`
resolved from `manuscript/numbers.json`, which `build_manuscript.py`
writes by loading canonical pipeline outputs (mapping summary tables,
`att_summary.csv`, `acute_2011_decomposition.csv`, SCM result CSVs,
`analysis_summary.json`). No analytical value is hard-coded in the text
module; grep for numeric literals in prose returned only structural
values (years, counts of items, question numbering) and the frozen
reporting quantities that are themselves pipeline outputs.

## Frozen headline values (unchanged across the retarget)

- Mapping: 50 relationship–dataset pairs; 34 (68%) not robust;
  sensitivity range 60–74%; Laffer p=0.06 (n=29); LNT p=0.15 (n=21;
  6 observations <0.1 Gy).
- Fukushima T1: ATT −0.085 log points (perm p=0.001); pre-trend 0.314;
  2011 decomposition 2,996 observed / 2,060 expected / 936 excess /
  732 direct / 204 residual; spec grid −0.085…−0.057; T1w −0.129;
  T2 p≥0.421; SC gap −0.060 (p=0.077).
- Kansas: IIT gap ≈27% (p=0.03; all-state 26%); gap $91→$422 per
  capita; cumulative ≈$4.6bn; total tax 3.0% (p=0.18); GDP +1.5%
  (p=0.71); employment −1.3% (p=0.47); placebo p range 0.006–0.056;
  pre-RMSPE 0.025; 25 donors.
- External: certified disaster-related deaths 2,350 (2026-02-13);
  ~160,000 evacuees; WHO/THJ projections 130 (15–1,100) vs 28 averted
  (3–245).

## Independent re-derivation

`check_manuscript.py` re-derives headline values from the raw manifests
and reports them under "Independent headline values": share 68;
ATT −0.08473; perm p 0.001; excess 935.7; IIT 27%; IIT p 0.03030 —
all match text values. Check report: `manuscript/check_report_evidence_policy.md`
— Failures: None.

## numbers.json keys absent verbatim from the main DOCX

Expected and verified: values moved to the online supplement
(alpha_grid, k_grid, T1w/T2/pretrend/scope statistics, SC gap series,
n_perm, per-year excess decomposition, ks_placebo range, repo_url) do
not appear in the anonymised main manuscript — they appear in
`appendix_evidence_policy.docx` captions/tables or in editorial files.
No value appears in the main text that is absent from numbers.json
(`n_dropped_top_prefs` sentence retained as interpretive text, not a
number).

## Verdict

PASS. Frozen values respected; no new analysis; provenance chain
raw manifests → pipeline → numbers.json → text placeholders intact.
