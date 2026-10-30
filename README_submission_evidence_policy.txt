Evidence & Policy submission package — file guide
=================================================

Upload set (anonymised where the journal requires it)
----------------------------------------------------
Evidence_Policy_manuscript_inline.docx      anonymised manuscript, figures/tables inline
Evidence_Policy_manuscript_clean.docx       same manuscript, display items separate (use per portal preference)
Evidence_Policy_supplement.docx             online supplement: Figures S1-S4, Tables S1-S5 (not counted toward word limit)
Evidence_Policy_cover_letter.docx           cover letter (first-person, single-author)
Evidence_Policy_title_page.docx             title page with author details
Evidence_Policy_submission_statements.docx  declarations: originality, competing interests, funding, data availability, AI assistance
Evidence_Policy_tables.docx                 editable tables
Evidence_Policy_figures.pptx                editable figures
figures/                                  PNG/TIFF exports of the figure panels

Audit trail (internal; not required for upload)
-----------------------------------------------
EVIDENCE_POLICY_FIT_DIAGNOSIS.md            Phase-1 fit diagnosis vs journal scope
EVIDENCE_POLICY_CLOSEST_LITERATURE.md       closest-prior-work audit
ARTICLE_TYPE_FIT.md                         article-type selection audit
POLICY_RATIONALE_SOURCE_AUDIT.md            documentation class for each evidence→decision link
HOSTILE_EVIDENCE_POLICY_REVIEW.md           simulated 5-perspective hostile review
HARDCODE_AND_NUMERIC_PROVENANCE_AUDIT_FINAL.md
PUBLIC_DATA_REPRODUCIBILITY_AUDIT_FINAL.md
DATA_TEXT_FIGURE_CONSISTENCY_FINAL.md
FIGURE_TABLE_CITATION_AUDIT.md
REFERENCE_AUDIT_FINAL.md
numeric_claim_registry.csv                  every numeric claim -> canonical source file
FINAL_HANDOFF.md                            readiness statement and change log
Evidence_Policy_guidelines.md               compiled journal requirements
check_report_evidence_policy.md             automated compliance report (Failures: None)
hostile_review_evidence_policy.md           manuscript-level hostile review notes
numbers.json                                injection manifest (all empirical values)
provenance/                                 raw-data checksum manifests
source/                                     build scripts for this package
review_archive_policy_sciences.zip          anonymised reviewer archive (carried over)

Key constraints observed
------------------------
- Analysis freeze: no new data, cases, or specifications; all values
  injected from numbers.json.
- Journal limit: 7,000 words including display items (~300 words/half-
  page item). This package: 4,475 words + 6 display items ≈ 6,275.
- Double-anonymous: main manuscript contains no author identifiers or
  repository URL; those live only in the title page and cover letter.
