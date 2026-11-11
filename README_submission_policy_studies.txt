Policy Studies (Taylor & Francis) submission package

Article type: Original research article

Review files

- manuscript_policy_studies.docx: anonymized manuscript with figures and tables placed after first citation.
- manuscript_policy_studies_figures_separate.docx: anonymized upload variant with figure callouts and separate figure/table sections.
- appendix_policy_studies.docx: separate supplementary appendix containing Appendix Tables A1-A2 and Appendix Figure A1.

Editorial files

- title_page_policy_studies.docx: author, affiliation, corresponding email, journal name, article type, word count, repository URL, and declarations. The affiliation field is left for the submitting author.
- cover_letter_policy_studies.docx: cover letter addressed to the Policy Studies editors.
- submission_statements_policy_studies.docx: author contribution, funding, competing-interests, ethics, data-availability, and AI-assistance statements. The submission system remains authoritative for declarations entered as metadata.

Editable and production files

- tables_policy_studies.docx: editable tables.
- figures_policy_studies.pptx: one editable figure or table per slide with title and caption.
- figures/: numbered PNG and TIFF figure files.
- review_archive_policy_sciences.zip: double-anonymous data, code, and reproduction archive.
- source/: manuscript text, generator, and validation source files.
- provenance/: raw-file path, size, SHA-256, source, acquisition, and usage-term manifests.
- numbers.json: manuscript values derived from analysis outputs.
- check_report_policy_studies.md: automated compliance and consistency report.
- hostile_review_policy_studies.md: pre-submission critical review and resolutions.
- Policy_Studies_guidelines.md: journal-specific preparation checklist.
- POLICY_STUDIES_FIT_AUDIT.md, CLAIM_CALIBRATION_AUDIT.md, REFERENCE_AUDIT.md, DESK_REJECTION_STRESS_TEST.md, FINAL_HANDOFF.md: revision audit documents.

Double-anonymous review

Policy Studies operates double-anonymized peer review. The two manuscript files and the appendix omit author names, affiliation, email address, and the public author-identifying repository URL. Author information is confined to editorial files. The manuscript Data Availability statement refers reviewers to an anonymized archive supplied through the submission system. Before upload, confirm that the submission platform does not expose title-page or repository metadata to reviewers.

Data, code, and reproduction

Archived public source files, acquisition metadata, processed data, analysis code, and document-generation code are maintained at https://github.com/bougtoir/canonical-curves-reexamination. From canonical_curves_reexamination/quasi_experiments, run:

pip install -r requirements.txt
make all
JOURNAL=policy_studies python manuscript/build_manuscript.py
JOURNAL=policy_studies python manuscript/check_manuscript.py
make final_package JOURNAL=policy_studies

The acquisition scripts do not replace existing public-data snapshots when the expected local source panels are present. Consult the top-level data/source_manifest.csv and data/SOURCES.md plus data/raw_manifest.csv in each case directory for source URLs, timestamp precision, file sizes, SHA-256 hashes, acquisition notes, and usage terms. Exact historical request times were not retained, so the manifests identify the first repository commit as a UTC timestamp proxy rather than inventing precision. One unused legacy Fukushima workbook predates the current source ledger and is explicitly marked as such; the current analysis uses the archived prefecture CSV snapshots instead.

Submission checks

The abstract is approximately 150-200 words; the manuscript is approximately 9,000 words all-inclusive; keywords number 5-6; headings use no more than three displayed levels; references follow APA author-date style; and figures, tables, Data Availability, AI assistance, and declarations must be checked against the live Taylor & Francis submission portal immediately before upload.
