PYTHON ?= python
JOURNAL ?= policy_sciences

ifeq ($(JOURNAL),jcpa)
JLABEL := JCPA
README_FILE := README_submission_jcpa.txt
else ifeq ($(JOURNAL),policy_studies)
JLABEL := Policy_Studies
README_FILE := README_submission_policy_studies.txt
else
JLABEL := Policy_Sciences
README_FILE := README_submission.txt
endif

.PHONY: kansas fukushima provenance all manuscript review_archive package final_package package_policy_studies final_package_policy_studies

kansas:
	@if [ -f kansas/data/state_panel.csv ]; then echo "Kansas acquisition data already exist; skipping acquisition"; else $(PYTHON) kansas/scripts/acquire_kansas.py; fi
	$(PYTHON) kansas/scripts/analyze_kansas.py

fukushima:
	@if [ -f fukushima/data/municipal_panel.csv ]; then echo "Fukushima acquisition data already exist; skipping acquisition"; else $(PYTHON) fukushima/scripts/acquire_fukushima.py; fi
	$(PYTHON) fukushima/scripts/analyze_fukushima.py

provenance:
	$(PYTHON) common/build_raw_manifests.py

all: kansas fukushima
	$(PYTHON) common/build_raw_manifests.py

manuscript: all
	JOURNAL=$(JOURNAL) $(PYTHON) manuscript/build_manuscript.py
	JOURNAL=$(JOURNAL) $(PYTHON) manuscript/check_manuscript.py

review_archive:
	$(PYTHON) common/build_review_archive.py

package: manuscript review_archive
	@set -eu; \
	staging=$$(mktemp -d); \
	trap 'rm -rf "$$staging"' EXIT; \
	mkdir -p "$$staging/figures" "$$staging/source" "$$staging/provenance"; \
	cp ../manuscript_$(JOURNAL).docx \
		../manuscript_$(JOURNAL)_figures_separate.docx \
		../appendix_$(JOURNAL).docx \
		../title_page_$(JOURNAL).docx \
		../tables_$(JOURNAL).docx \
		../figures_$(JOURNAL).pptx \
		../cover_letter_$(JOURNAL).docx \
		../submission_statements_$(JOURNAL).docx \
		../review_archive_policy_sciences.zip \
		../$(README_FILE) \
		$(JLABEL)_guidelines.md \
		manuscript/check_report_$(JOURNAL).md \
		manuscript/hostile_review_$(JOURNAL).md \
		manuscript/numbers.json \
		"$$staging/"; \
	cp manuscript/figures/*.png manuscript/figures/*.tiff "$$staging/figures/"; \
	cp manuscript/build_manuscript.py manuscript/check_manuscript.py \
		manuscript/build_finish_pass.py manuscript/text_$(JOURNAL).py \
		common/build_raw_manifests.py \
		common/build_review_archive.py \
		"$$staging/source/"; \
	cp kansas/data/raw_manifest.csv \
		"$$staging/provenance/kansas_raw_manifest.csv"; \
	cp fukushima/data/raw_manifest.csv \
		"$$staging/provenance/fukushima_raw_manifest.csv"; \
	cp ../data/source_manifest.csv \
		"$$staging/provenance/canonical_curves_source_manifest.csv"; \
	rm -f ../submission_$(JOURNAL).zip; \
	(cd "$$staging" && zip -qr "$(CURDIR)/../submission_$(JOURNAL).zip" .)
	JOURNAL=$(JOURNAL) $(PYTHON) manuscript/build_finish_pass.py

final_package: package
	JOURNAL=$(JOURNAL) $(PYTHON) manuscript/build_finish_pass.py --ready

package_policy_studies:
	$(MAKE) package JOURNAL=policy_studies

final_package_policy_studies:
	$(MAKE) final_package JOURNAL=policy_studies

package_jcpa:
	$(MAKE) package JOURNAL=jcpa

final_package_jcpa:
	$(MAKE) final_package JOURNAL=jcpa
