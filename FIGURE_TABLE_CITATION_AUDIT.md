# Figure/table citation audit (Evidence & Policy)

Every display item is cited in text; every citation resolves to an
existing item; first-mention order equals numbering order
(verified programmatically by `check_manuscript.py` —
Failures: None).

## Main manuscript

| Item | Content | First cited | Section |
| --- | --- | --- | --- |
| Figure 1 | Evidence-to-policy translation pathway | Background | framing |
| Figure 2 | Mapping sensitivity grid | Findings — mapping |  |
| Table 1 | Mapping audit summary by field | Findings — mapping |  |
| Figure 3 | Fukushima pooled CDR series | Findings — Fukushima |  |
| Figure 4 | Kansas SCM IIT gap | Findings — Kansas |  |
| Table 2 | Cross-application synthesis (5 dimensions) | Findings — synthesis |  |

## Online supplement (`appendix_evidence_policy.docx`)

| Item | Content | Cited as | First-mention order |
| --- | --- | --- | --- |
| Supplement Figure S1 | Mapping decision-tree diagnostic | Background/Methods | 1 |
| Supplement Figure S2 | Kansas neighbouring-state event studies | Methods — Kansas | 2 |
| Supplement Figure S3 | Fukushima preferred event study | Findings — Fukushima | 3 |
| Supplement Figure S4 | Fukushima acute-phase decomposition | Findings — Fukushima | 4 |
| Supplement Table S1 | Municipalities excluded (missing data) | Methods — Fukushima | 1 |
| Supplement Table S2 | Unit-level Fukushima SCM results | Methods — Fukushima | 2 |
| Supplement Table S3 | Fukushima DiD specification grid | Findings — Fukushima | 3 |
| Supplement Table S4 | Fukushima measured vs projected quantities | Findings — Fukushima | 4 |
| Supplement Table S5 | Kansas SCM estimates by outcome/donor pool | Findings — Kansas | 5 |

## Checks

- In-text labels ("Figure 2", "Supplement Table S3", …) match caption
  labels one-to-one — verified by regex extraction in the checker.
- No orphan items; no citation to a non-existent item.
- Captions are self-contained (define abbreviations, state estimand,
  note exclusion/sample rules where relevant).
- Supplement numbering was re-assigned so that mention order and labels
  are aligned (S-order follows first mention).

## Verdict

PASS.
