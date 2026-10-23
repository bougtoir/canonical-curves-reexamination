# Data-text-figure consistency audit (JCPA)

## Numeric provenance

All manuscript numbers are injected by build_manuscript.py from
numbers.json, which is regenerated from current analysis outputs
(fukushima/results, kansas/results, results/). No numerical value is
hand-edited in text_jcpa.py; the analysis freeze was respected — no
analysis, dataset, or result changed relative to the Policy Studies
version.

## Prose ↔ tables ↔ figures

- Figure 1 (comparative sequence): box contents match the eight common
  dimensions named in "Units and common comparative dimensions" and the
  comparative narrative (Fukushima | Kansas entries).
- Figure 2/Table 1: mapping diagnostic and category counts match
  numbers.json (n_curves, n_not_robust, category counts, sensitivity range).
- Figures 4-6/Table 2-3 (Fukushima): DiD ATT, permutation p, pre-trend p,
  2011 decomposition (observed/expected/excess/direct/residual), LNT
  comparison quantities all sourced from numbers.json.
- Figure 7/Table 4 (Kansas): IIT gap %, total-tax gap %, GDP and employment
  gaps, cumulative gap, LOO range, pre-RMSPE from numbers.json.
- Table 5: qualitative comparative coding; cells match case-section claims
  (reversibility: Fukushima limited / Kansas comparatively greater with
  2017 statutory revision; uncertainty type: extrapolation vs. local
  position/dynamic response).
- Captions: numbering and group membership match figure files and in-text
  citations (enforced by check_manuscript.py).
- Appendix (Tables A1-A2, Figure A1): unchanged from prior version;
  referenced as supplementary.

## Stale-value check

- Policy Studies-specific phrases (journal name, "Policy Studies"
  formatting, prior cover-letter text) do not appear in text_jcpa.py.
- Abstract/keywords/title regenerated for JCPA; word and keyword limits
  enforced by check_manuscript.py (8,000 / 5-6 / <=250).
