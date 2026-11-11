Evidence & Policy submission package — file guide
=================================================

Upload set (anonymised where the journal requires it)
----------------------------------------------------
Evidence_Policy_manuscript_inline_FINAL.docx      anonymised manuscript, 8 figures + 6 tables inline
Evidence_Policy_manuscript_clean_FINAL.docx       same manuscript, display items separate (use per portal preference)
Evidence_Policy_cover_letter_FINAL.docx           cover letter (first-person, single-author)
Evidence_Policy_title_page_FINAL.docx             title page with author details
Evidence_Policy_submission_statements_FINAL.docx  declarations: originality, competing interests, funding, data availability, AI assistance; "Supplementary files: none"
Evidence_Policy_tables_FINAL.docx                 editable tables
Evidence_Policy_figures_FINAL.pptx                editable figures
figures/                                          PNG/TIFF exports of Figure1-8

Supplementary files: NONE. The former online supplement is fully
integrated: Supplement Figures S1-S4 became Figures 2, 3, 6, 7;
Supplement Tables S2-S5 became Tables 1, 3, 4, 5; Supplement Table S1
(48-row exclusion list) is a prose summary plus the reproducibility
archive. See SUPPLEMENT_INTEGRATION_INVENTORY.md.

Audit trail (internal; not required for upload)
-----------------------------------------------
EVIDENCE_POLICY_FIT_DIAGNOSIS.md            Phase-1 fit diagnosis vs journal scope
EVIDENCE_POLICY_CLOSEST_LITERATURE.md       closest-prior-work audit
ARTICLE_TYPE_FIT.md                         article-type selection audit
POLICY_RATIONALE_SOURCE_AUDIT.md            documentation class for each evidence→decision link
CLAIM_CALIBRATION_AUDIT.md                  forbidden-claim and calibrated-wording check
SUPPLEMENT_INTEGRATION_INVENTORY.md         per-item disposition of all former supplement items
FIGURE_RENUMBERING_MAP.md                   S-figure/main-figure → new numbering
TABLE_RENUMBERING_MAP.md                    S-table/main-table → new numbering
FIGURE_TABLE_CITATION_AUDIT_FINAL.md        citation-order audit (all PASS)
HARDCODE_AND_NUMERIC_PROVENANCE_AUDIT_FINAL.md
PUBLIC_DATA_REPRODUCIBILITY_AUDIT_FINAL.md
DATA_TEXT_FIGURE_TABLE_CONSISTENCY_FINAL.md
REFERENCE_AUDIT_FINAL.md
HOSTILE_EVIDENCE_POLICY_REVIEW_FINAL.md     simulated 6-perspective hostile review
numeric_claim_registry.csv                  every numeric claim -> canonical source file
FINAL_HANDOFF.md                            readiness statement and change log
Evidence_Policy_guidelines.md               compiled journal requirements
check_report_evidence_policy.md             automated compliance report (Failures: None)
numbers.json                                injection manifest (all empirical values)
provenance/                                 raw-data checksum manifests
source/                                     build scripts for this package
review_archive_policy_sciences.zip          anonymised reviewer archive (carried over)

Key constraints observed
------------------------
- Analysis freeze: no new data, cases, or specifications; all values
  injected from numbers.json.
- Journal limit: 7,000 words including display items, counted at
  ~300 words per half-page of rendered figure space (tables count
  through their text). This package: 5,229 words + ~1,770 display
  equivalents ≈ 6,999.
- Double-anonymous: main manuscript contains no author identifiers or
  repository URL; those live only in the title page and cover letter.
