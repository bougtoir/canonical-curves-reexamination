# Figure/table citation audit — final (Evidence & Policy)

Method: parsed manuscript BODY for `Figure N` / `Table N` first
mentions and compared with physical object order in the rendered
inline DOCX. Citation order must equal numbering; every numbered
object must be cited; every citation must resolve to a real object.

| Object | First citation (order) | Physical object present | Order correct | Status |
| --- | --- | --- | --- | --- |
| Figure 1 (pathway) | 1 | yes (inline, fig_policy_pathway) | yes | PASS |
| Figure 2 (diagnostic sequence) | 2 | yes (fig_decision_tree) | yes | PASS |
| Table 1 (unit-level SCM grid) | 3 | yes (tab_a2) | yes | PASS |
| Figure 3 (Kansas neighbour event studies) | 4 | yes (fig_a1) | yes | PASS |
| Figure 4 (sensitivity grid) | 5 | yes (fig_sensitivity) | yes | PASS |
| Table 2 (audit summary) | 6 | yes (tab_audit) | yes | PASS |
| Figure 5 (pooled CDR) | 7 | yes (fig_pooled_cdr) | yes | PASS |
| Table 3 (Fukushima ATT grid) | 8 | yes (tab_fuku_att) | yes | PASS |
| Figure 6 (event study) | 9 | yes (fig_event_study) | yes | PASS |
| Figure 7 (acute decomposition) | 10 | yes (fig_acute) | yes | PASS |
| Table 4 (measured vs projected) | 11 | yes (tab_lnt) | yes | PASS |
| Figure 8 (Kansas SCM) | 12 | yes (fig_kansas) | yes | PASS |
| Table 5 (Kansas SCM summary) | 13 | yes (tab_kansas) | yes | PASS |
| Table 6 (cross-application synthesis) | 14 | yes (tab_synthesis) | yes | PASS |

Additional checks:
- No `Figure S*` / `Table S*` / `Appendix` citation remains in the text
  (supplement eliminated).
- No numbered object lacks an in-text citation (enforced by
  check_manuscript.py: first-mention order main=1..8 figures, 1..6
  tables; Failures: None).
- Figure 3 is cited in Methods and again in Results (Kansas robustness);
  repeat citations are permitted.
- PNG/TIFF stems, PPTX slide order, and captions match the numbering.
