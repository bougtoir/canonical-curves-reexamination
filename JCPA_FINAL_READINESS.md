# JCPA final readiness

| Gate | Description | Result |
| --- | --- | --- |
| R1 | Explicit comparative design | PASS — dedicated design section; symmetric seven-subsection cases; within-case → cross-case logic |
| R2 | Comparative yields non-additive knowledge | PASS — Comparative findings + three propositions + lesson-drawing; each item requires both cases |
| R3 | Within-case credible, cross-case interpretive | PASS — separate design diagnostics per case; no causal case-vs-case comparison |
| R4 | Case-selection justification | PASS — maximum contrast + common mechanism + public-evidence reconstructability; permits/non-permits |
| R5 | JCPA fit in title/abstract/intro/Discussion/lesson-drawing | PASS — mapping reduced to background; article type comparative |
| R6 | Journal compliance | PASS — 5,601 words ≤ 8,000; abstract 155; 6 keywords; double-anonymous split; statements files |
| R7 | Contribution identifiable | PASS — one-sentence comparative mechanism + config + appraisal-entry rule |
| R8 | Non-comparative overclaims removed | PASS — no prevalence/novelty/general-law claims; mapping not the contribution |

## Hostile review outcome

FATAL: 0. MAJOR: 0 remaining. MINOR: 2 disclosed limitations (common-diagnostic
generality; residual confounding). See HOSTILE_JCPA_REVIEW_FINAL.md.

## Reproducibility

Fresh-venv reruns of the Fukushima and Kansas pipelines reproduced all headline
values at reported precision (float diffs ≤ ~1e-13, ignored). Mapping canonical
outputs preserved and re-derived; live reacquisition documented as snapshot-based.
See PUBLIC_DATA_REPRODUCIBILITY_AUDIT.md.

## Numeric provenance

88 registered claims verified to canonical files; zero manual/hardcoded results.
See HARDCODE_AND_NUMERIC_PROVENANCE_AUDIT.md + numeric_claim_registry.csv.

## Data–text–figure consistency

No unresolved contradictions; three wording corrections applied and regenerated.
See DATA_TEXT_FIGURE_CONSISTENCY_FINAL.md.

## Rendered-document QC

Files convert to plain text via pandoc without artifacts; no markdown residue,
no track-changes/comments, numbering sequential, equation rendered as OMML.
No clipped figures: all figures are regenerated PNGs at fixed canvas size.

READY FOR JCPA SUBMISSION.
