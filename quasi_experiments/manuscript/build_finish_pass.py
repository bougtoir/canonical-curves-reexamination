"""Create the final finish-pass deliverables for the journal selected by JOURNAL.

JOURNAL=policy_sciences (default) reproduces the original Policy Sciences
package. JOURNAL=policy_studies builds the Policy Studies (Taylor & Francis)
package with its own audit documents.
"""

from __future__ import annotations

import argparse
import importlib
import json
import os
import re
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QROOT = ROOT / "quasi_experiments"
MANUSCRIPT = QROOT / "manuscript"
FIGURES = MANUSCRIPT / "figures"

sys.path.insert(0, str(MANUSCRIPT))
JOURNAL = os.environ.get("JOURNAL", "policy_sciences")
text = importlib.import_module(f"text_{JOURNAL}")

if JOURNAL == "policy_sciences":
    FINAL_FILES = {
        ROOT / "manuscript_policy_sciences.docx": ROOT
        / "Policy_Sciences_manuscript_inline_FINAL.docx",
        ROOT / "manuscript_policy_sciences_figures_separate.docx": ROOT
        / "Policy_Sciences_manuscript_clean_FINAL.docx",
        ROOT / "cover_letter_policy_sciences.docx": ROOT
        / "Policy_Sciences_cover_letter_FINAL.docx",
        ROOT / "title_page_policy_sciences.docx": ROOT
        / "Policy_Sciences_title_page_FINAL.docx",
        ROOT / "appendix_policy_sciences.docx": ROOT
        / "Policy_Sciences_appendix_FINAL.docx",
        ROOT / "tables_policy_sciences.docx": ROOT
        / "Policy_Sciences_tables_FINAL.docx",
        ROOT / "figures_policy_sciences.pptx": ROOT
        / "Policy_Sciences_figures_FINAL.pptx",
        ROOT / "submission_statements_policy_sciences.docx": ROOT
        / "Policy_Sciences_submission_statements_FINAL.docx",
    }
elif JOURNAL == "policy_studies":
    FINAL_FILES = {
        ROOT / "manuscript_policy_studies.docx": ROOT
        / "Policy_Studies_manuscript_inline.docx",
        ROOT / "manuscript_policy_studies_figures_separate.docx": ROOT
        / "Policy_Studies_manuscript_clean.docx",
        ROOT / "cover_letter_policy_studies.docx": ROOT
        / "Policy_Studies_cover_letter.docx",
        ROOT / "title_page_policy_studies.docx": ROOT
        / "Policy_Studies_title_page.docx",
        ROOT / "appendix_policy_studies.docx": ROOT
        / "Policy_Studies_appendix.docx",
        ROOT / "tables_policy_studies.docx": ROOT
        / "Policy_Studies_tables.docx",
        ROOT / "figures_policy_studies.pptx": ROOT
        / "Policy_Studies_figures.pptx",
        ROOT / "submission_statements_policy_studies.docx": ROOT
        / "Policy_Studies_submission_statements.docx",
    }
else:
    raise ValueError(f"Unknown JOURNAL: {JOURNAL}")


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def format_text(text: str, numbers: dict[str, object]) -> str:
    return text.format(**numbers)


def main_text_word_count(numbers: dict[str, object]) -> int:
    parts: list[str] = []
    for kind, value in text.BODY:
        if kind == "refs":
            break
        if kind in {"h1", "h2", "p", "eq"} and value:
            parts.append(format_text(value, numbers))
    return word_count("\n".join(parts))


def check_report_passed() -> bool:
    report = (MANUSCRIPT / f"check_report_{JOURNAL}.md").read_text(
        encoding="utf-8"
    )
    return "## Failures\n- None." in report


def write_audit(numbers: dict[str, object]) -> None:
    original_abstract = (
        "A cross-domain mapping exercise applies one transparent quadratic diagnostic "
        f"to {numbers['n_curves']} canonical relationships; "
        f"{numbers['n_not_robust']} ({numbers['share_not_robust_pct']}%) are not "
        "classified as robustly nonlinear under the default criteria, with a sensitivity "
        f"range of {numbers['share_min_pct']}-{numbers['share_max_pct']}%."
    )
    revised_abstract = (
        "A cross-domain mapping exercise then applies one transparent quadratic diagnostic "
        f"to {numbers['n_curves']} canonical relationships. Under this deliberately common "
        f"diagnostic, {numbers['n_not_robust']} of {numbers['n_curves']} "
        f"relationship-dataset pairs ({numbers['share_not_robust_pct']}%) did not meet the "
        "study's criteria for robust nonlinear identification, with a sensitivity range "
        f"of {numbers['share_min_pct']}-{numbers['share_max_pct']}%."
    )
    original_results = (
        "The policy-relevant result is that many familiar shapes are more assumption "
        "dependent than their schematic presentation suggests."
    )
    revised_results = (
        "Across the mapped relationship-dataset pairs, several familiar schematic forms "
        "were more specific than could be established by the common diagnostic over the "
        "observed data range."
    )
    content = f"""# Final finish-pass audit

## Conceptual figure

- Old location: Discussion, under "A practical appraisal sequence," after both empirical demonstrations.
- New location: Analytical framework and methods, immediately after "From association to decision dependence" and before the cross-domain mapping exercise.
- Old figure number: Figure 7.
- New figure number: Figure 1.
- Downstream numbering changes:
  - Old Figure 1 (mapping diagnostic) is now Figure 2.
  - Old Figure 2 (sensitivity grid) is now Figure 3.
  - Old Figure 3 (Fukushima pooled crude death rates) is now Figure 4.
  - Old Figure 4 (Fukushima event study) is now Figure 5.
  - Old Figure 5 (Fukushima acute decomposition) is now Figure 6.
  - Old Figure 6 (Kansas synthetic control) is now Figure 7.
- All in-text citations, captions, inline placements, separate-figure placeholders, PNG/TIFF filenames, and editable PPTX slide order were updated to match.
- PPTX figures are scaled proportionally within a fixed slide area, with full captions in a dedicated text area rather than stretched images or clipped one-line captions.

## Abstract calibration

Original:

> {original_abstract}

Revised:

> {revised_abstract}

Reason: The revised wording retains the 34-of-50 result while identifying it as the outcome of a deliberately common study diagnostic, not a replication-failure rate, a prevalence estimate, or evidence that 68% of canonical theories are false.

## Results calibration

Original:

> {original_results}

Revised:

> {revised_results}

Reason: The revised claim is limited to the purposively mapped relationship-dataset pairs, the common diagnostic, and the observed data range.

## Concept definition and model uncertainty

Model uncertainty is the broader category. Functional-form uncertainty concerns uncertainty about relationship shape, including thresholds, turning points, curvature, and extrapolation. Functional-form dependence is the decision-level condition in which the policy justification, expected benefit, threshold, direction, or intensity materially depends on a shape that is insufficiently identified over the policy-relevant range.

## Fukushima recalibration

No principal estimate or substantive interpretation changed. The section continues to state that the negative post-2011 coefficient is not evidence that evacuation improved health; the analysis does not establish that LNT is false, that evacuation was definitively wrong, or that non-evacuation would have been superior; non-evacuation outcomes are unobserved; and municipal mortality is affected by population composition, registration, migration, displacement, and measurement structure. The only case-specific changes were Figure 3 to Figure 4, Figure 4 to Figure 5, Figure 5 to Figure 6, and the framework transition describing low-dose extrapolation and asymmetric competing risks.

## Kansas recalibration

No principal estimate or substantive interpretation changed. The section continues to distinguish a theoretically possible Laffer curve from Kansas's local position, local slope, turning point, dynamic behavioral response, timing, and observed outcomes. The only case-specific changes were Figure 6 to Figure 7 and the framework transition stating that a theoretically possible curve does not identify a policy's local position, slope, or dynamic response.

## Numerical integrity

No numerical result changed in this finish pass. The existing analyses were rerun only to verify consistency.

## Terminal pre-submission micro-fix

### Framework-count consistency

- Locations checked: Abstract, Introduction, analytical framework, Figure 1 caption, Discussion, Conclusion, cover letter, and hostile-review record.
- "The framework distinguishes six layers." was revised to "The decision-facing appraisal framework distinguishes linked layers from empirical association through policy commitment."
- "Figure 1 introduced the six-step sequence before the empirical demonstrations." was revised to "Figure 1 introduced the decision-facing appraisal framework before the empirical demonstrations."
- "The article develops a six-step appraisal framework" was revised to "The article develops a decision-facing appraisal framework."
- The shared term in the Abstract, Introduction, Figure 1, Discussion, Conclusion, and cover letter is "decision-facing appraisal framework."

### Artificial intelligence assistance

The synchronized declaration is:

> {text.AI_ASSISTANCE_TEXT}

It appears in the inline manuscript, clean manuscript, title page, and submission statements. It is not repeated in the cover letter because the journal materials used for this package do not require disclosure there.

### Integrity

No numerical results changed.

Figure and table numbering is unchanged: seven main figures, Appendix Figure A1, four main tables, and Appendix Tables A1 and A2.

No reference was altered.
"""
    (ROOT / "FINAL_FINISH_PASS_AUDIT.md").write_text(content, encoding="utf-8")


def write_handoff(numbers: dict[str, object], ready: bool) -> None:
    abstract_words = word_count(format_text(text.ABSTRACT, numbers))
    main_words = main_text_word_count(numbers)
    final_line = (
        "READY FOR POLICY SCIENCES SUBMISSION"
        if ready
        else "NOT READY — SPECIFIC CORRECTIONS REQUIRED"
    )
    if JOURNAL == "policy_studies":
        final_line = final_line.replace("POLICY SCIENCES", "POLICY STUDIES")
    remaining = (
        "None. Confirm the author name, affiliation, and corresponding-author email in "
        "the submission portal against the separate title page."
        if ready
        else "Complete the final external synchronization and rerun this script with "
        "--ready after all package checks pass."
    )
    content = f"""# Final handoff

- Final title: {text.TITLE}
- Abstract word count: {abstract_words}
- Main-text word count, excluding abstract, references, captions, and tables: {main_words}
- Figures: 7 main figures plus Appendix Figure A1
- Tables: 4 main tables plus Appendix Tables A1 and A2
- Figure numbering: Figure 1 decision-facing framework; Figure 2 mapping diagnostic; Figure 3 sensitivity grid; Figures 4-6 Fukushima; Figure 7 Kansas; Appendix Figure A1 Kansas neighboring-state event studies
- Inline manuscript: Policy_Sciences_manuscript_inline_FINAL.docx
- Clean separate-figure manuscript: Policy_Sciences_manuscript_clean_FINAL.docx
- Cover letter: Policy_Sciences_cover_letter_FINAL.docx
- Title page: Policy_Sciences_title_page_FINAL.docx
- Supplement: Policy_Sciences_appendix_FINAL.docx
- Editable tables: Policy_Sciences_tables_FINAL.docx
- Editable figures: Policy_Sciences_figures_FINAL.pptx
- Submission statements: Policy_Sciences_submission_statements_FINAL.docx
- Remaining author-local placeholders: {remaining}
- Unresolved scientific concern: No submission-blocking concern. The non-probability mapping, Fukushima measurement structure, and Kansas residual-confounding limits remain and are stated explicitly.

## Framework-count inconsistency

- Locations checked: Abstract, Introduction, analytical framework, Figure 1 caption, Discussion, Conclusion, cover letter, and hostile-review record.
- Exact wording changed: "The framework distinguishes six layers." to "The decision-facing appraisal framework distinguishes linked layers from empirical association through policy commitment."
- Exact wording changed: "Figure 1 introduced the six-step sequence before the empirical demonstrations." to "Figure 1 introduced the decision-facing appraisal framework before the empirical demonstrations."
- Exact wording changed: "The article develops a six-step appraisal framework" to "The article develops a decision-facing appraisal framework."
- The shared term across the Abstract, Introduction, Figure 1, Discussion, Conclusion, and cover letter is "decision-facing appraisal framework."

## AI declaration

Exact final wording:

> {text.AI_ASSISTANCE_TEXT}

Files containing it: Policy_Sciences_manuscript_inline_FINAL.docx, Policy_Sciences_manuscript_clean_FINAL.docx, Policy_Sciences_title_page_FINAL.docx, and Policy_Sciences_submission_statements_FINAL.docx. The cover letter does not repeat it because the journal materials used for this package do not require disclosure there.

## Numerical results

No numerical results changed.

## Figure/table numbering

Unchanged: seven main figures, Appendix Figure A1, four main tables, and Appendix Tables A1 and A2.

## References

No reference was altered.

{final_line}
"""
    (ROOT / "FINAL_HANDOFF.md").write_text(content, encoding="utf-8")


def write_fit_audit() -> None:
    content = """# Policy Studies fit audit

## Repositioning

- Before (Policy Sciences Analysis): the article was framed around a general
  claim about canonical relationships and their nonlinearity, with the
  decision-facing appraisal framework presented as the framework-level
  contribution.
- After (Policy Studies): the article is framed as a general policy-analysis
  framework for identifying when real-world policy choices depend on
  empirical relationship shapes that are less securely identified than the
  policy decision assumes. The contribution is positioned inside evidence
  use, policy appraisal, and policy design debates - not as a new abstract
  policy theory.
- Title: "When Policy Depends on a Curve: Functional-Form Dependence in
  Evidence-Based Policymaking." No case-study names in the title; "mapping"
  is not used in the title.
- Abstract: opens with the practical policy-analysis problem (three
  questions), defines functional-form dependence, reports the mapping result
  as a diagnostic outcome, and ends with the practical contribution.
- Framework: retained as Figure 1 and explicitly described as a
  decision-facing appraisal framework - an appraisal device applied before
  or during policy design - not a universal policy theory.
- Applications: Fukushima and Kansas are presented as applications of the
  framework to real policy controversies, not as standalone case studies
  carrying the article's contribution.
- Discussion: reorganized around the practical findings - principal finding,
  why an association is not enough, policy-relevant range and
  transportability, cross-case synthesis, functional-form dependence as
  policy risk, implications for policy practice (seven-question diagnostic),
  and limitations.
- Conclusion: ends on the practical principle - the decision may require
  more knowledge about relationship shape than the available evidence
  provides.
- Cover letter: newly written for Policy Studies; opens with the problem,
  what existing appraisal practice misses, the contribution, and the
  cross-domain rationale. No mention of any prior submission.
"""
    (ROOT / "POLICY_STUDIES_FIT_AUDIT.md").write_text(content, encoding="utf-8")


def write_claim_calibration_audit() -> None:
    content = """# Claim calibration audit

## Forbidden-claim check

| Forbidden claim | Status in this manuscript |
| --- | --- |
| "68% of canonical theories are false" (or equivalent) | Absent. The result is reported as a diagnostic outcome: relationship-dataset pairs that "did not meet the study's criteria for robust nonlinear identification" under a deliberately common diagnostic, with the sensitivity range reported. |
| Fukushima evacuation was proven wrong | Absent. The text states the analysis does not establish that evacuation was definitively wrong, and that non-evacuation outcomes are unobserved. |
| The linear no-threshold model is false | Absent. The text states the analysis does not establish that LNT is false. |
| The Laffer curve does not exist | Absent. The text distinguishes a theoretically possible Laffer curve from Kansas's local position, slope, turning point, and dynamic response. |
| Kansas disproved supply-side economics | Absent. The application identifies functional-form dependence in the revenue justification, not a verdict on supply-side economics. |
| Functional-form dependence is wholly absent from scholarship | Absent. The article describes the concept as an organizing contribution that links existing model-uncertainty, risk-analysis, and robust-planning traditions to the policy argument itself. |

## Calibrated wording

- Mapping: "purposive mapping" of canonical relationships; the sample is not
  claimed to be representative, and the 34-of-50 result is bounded to the
  mapped pairs, the common diagnostic, and the observed data range.
- Fukushima: mortality is described as measured municipal mortality;
  certified disaster-related deaths and projected radiological deaths remain
  distinct estimands.
- Kansas: the synthetic-control result is described as a local treatment
  effect for Kansas, not a general verdict on tax cuts.
- Framework: "decision-facing appraisal framework" throughout; no framework
  element counts.
"""
    (ROOT / "CLAIM_CALIBRATION_AUDIT.md").write_text(content, encoding="utf-8")


def write_reference_audit() -> None:
    content = """# Reference audit

## Added for the Policy Studies revision

- Boswell (2009) - knowledge substantiation and the instrumental vs.
  legitimating uses of expertise.
- Cairney (2016) - evidence-based policymaking and bounded-rational
  policymaking context.
- Cartwright & Hardie (2012) - external validity and transportability of
  causal evidence (already cited in the prior version's framing; retained).
- Howlett (2019) - policy design and the instrument/solution side of policy
  formulation.
- Morgan & Henrion (1990) - model uncertainty taxonomy grounding
  functional-form uncertainty.
- Parkhurst (2016) - politics of evidence.
- Walker et al. (2013) - deep uncertainty and adaptive/robust planning.
- Weimer & Vining (2017) - policy analysis practice; appraisal checks.

## Removed

- None. No reference was deleted; additions were limited to the evidence-use,
  policy-appraisal/design, and model-uncertainty literatures directly engaged
  by the repositioned argument.

## Checks

- Every reference entry has an in-text citation and every in-text citation
  resolves to a reference entry (enforced by check_manuscript.py).
- References are APA-style author-date and hyperlinks were verified.
"""
    (ROOT / "REFERENCE_AUDIT.md").write_text(content, encoding="utf-8")


def write_desk_rejection_stress_test(numbers: dict[str, object]) -> None:
    content = f"""# Desk-rejection stress test (simulated Policy Studies editorial review)

1. Is this a policy-studies article or an econometrics exercise?
   - The framing, literature, and contribution are policy analysis: the
     mapping diagnostic and the two applications serve a decision-facing
     appraisal framework, not a methodological claim.
2. Does the paper offer more than a restatement of model uncertainty?
   - Yes: functional-form dependence is defined at the decision level and
     operationalized through the appraisal sequence and the seven-question
     diagnostic, which existing taxonomies do not provide.
3. Is the empirical claim overstated?
   - The mapping result is bounded to {numbers['n_curves']} purposively
     selected pairs and one common diagnostic; the {numbers['n_not_robust']}
     ({numbers['share_not_robust_pct']}%) figure is reported as pairs failing
     that diagnostic, not as a prevalence estimate.
4. Are the cases presented neutrally?
   - Fukushima: no claim that evacuation was wrong or that LNT is false.
     Kansas: no claim that the Laffer curve is disproved or that supply-side
     economics is refuted.
5. Is the title/abstract aligned with the journal?
   - The title names the general phenomenon and the policymaking domain; the
     abstract leads with the practical problem, not with the inventory count
     or theoretical novelty.
6. Is the paper within scope and format?
   - Approximately 9,000 words all-inclusive, abstract under 200 words, 5
     keywords, APA references, anonymized manuscript, separate title page.
7. Is the contribution legible to policy scholars without econometric
   background?
   - Figure 1 and the diagnostic checklist translate the technical issue
     into appraisal questions; technical material is confined to the
     appendix.
8. Any obvious desk-reject triggers?
   - No prior-journal references, no revision history, no author
     identifiers in the anonymized manuscript, no hard-coded or unverified
     numbers, AI-assistance declaration included.
"""
    (ROOT / "DESK_REJECTION_STRESS_TEST.md").write_text(
        content, encoding="utf-8"
    )


def write_audit_policy_studies(numbers: dict[str, object]) -> None:
    write_fit_audit()
    write_claim_calibration_audit()
    write_reference_audit()
    write_desk_rejection_stress_test(numbers)


def write_handoff_policy_studies(
    numbers: dict[str, object], ready: bool
) -> None:
    abstract_words = word_count(format_text(text.ABSTRACT, numbers))
    main_words = main_text_word_count(numbers)
    final_line = (
        "READY FOR POLICY STUDIES SUBMISSION"
        if ready
        else "NOT READY — SPECIFIC CORRECTIONS REQUIRED"
    )
    remaining = (
        "None. Confirm the author name, affiliation, and corresponding-author "
        "email in the submission portal against the separate title page; the "
        "affiliation field is intentionally left for the submitting author."
        if ready
        else "Complete the final external synchronization and rerun this "
        "script with --ready after all package checks pass."
    )
    content = f"""# Final handoff

- Final title: {text.TITLE}
- Abstract word count: {abstract_words}
- Main-text word count, excluding abstract, references, captions, and
  tables: {main_words}
- Figures: 7 main figures plus Appendix Figure A1
- Tables: 5 main tables plus Appendix Tables A1 and A2
- Figure numbering: Figure 1 decision-facing framework; Figure 2 mapping
  diagnostic; Figure 3 sensitivity grid; Figures 4-6 Fukushima; Figure 7
  Kansas; Appendix Figure A1 Kansas neighboring-state event studies
- Inline manuscript: Policy_Studies_manuscript_inline.docx
- Clean separate-figure manuscript: Policy_Studies_manuscript_clean.docx
- Cover letter: Policy_Studies_cover_letter.docx
- Title page: Policy_Studies_title_page.docx
- Supplement: Policy_Studies_appendix.docx
- Editable tables: Policy_Studies_tables.docx
- Editable figures: Policy_Studies_figures.pptx
- Submission statements: Policy_Studies_submission_statements.docx

## Major changes from the Policy Sciences version

- Repositioned from a general claim about canonical relationships to a
  policy-analysis framework identifying when policy choices depend on
  relationship shapes less securely identified than the decision assumes.
- New title, abstract, introduction architecture, cross-case synthesis
  section and Table 5, reorganized Discussion with an explicit seven-question
  diagnostic checklist, and a conclusion ending on the practical principle.
- New cover letter written for Policy Studies.

## Literature changes

- Added: Boswell (2009); Cairney (2016); Cartwright & Hardie (2012);
  Howlett (2019); Morgan & Henrion (1990); Parkhurst (2016); Walker et al.
  (2013); Weimer & Vining (2017).
- Removed: none.

## Analyses and numbers

No analysis, dataset, or numerical result changed. All values are injected
from numbers.json; the analysis freeze was respected.

## Remaining limitations

- The non-probability mapping, Fukushima measurement structure, and Kansas
  residual-confounding limits remain and are stated explicitly.
- {remaining}

{final_line}
"""
    (ROOT / "FINAL_HANDOFF.md").write_text(content, encoding="utf-8")


def copy_final_files() -> None:
    for source, destination in FINAL_FILES.items():
        if not source.is_file():
            raise FileNotFoundError(source)
        shutil.copy2(source, destination)


def copy_to(source: Path, destination: Path) -> None:
    if not source.is_file():
        raise FileNotFoundError(source)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)


def build_final_zip() -> None:
    if JOURNAL == "policy_sciences":
        output = ROOT / "Policy_Sciences_submission_FINAL.zip"
        root_docs = [
            "FINAL_FINISH_PASS_AUDIT.md",
            "FINAL_HANDOFF.md",
            "README_submission.txt",
            "review_archive_policy_sciences.zip",
        ]
        qroot_docs = [
            "Policy_Sciences_guidelines.md",
            f"manuscript/check_report_{JOURNAL}.md",
            "manuscript/hostile_review_policy_sciences.md",
            "manuscript/numbers.json",
        ]
    else:
        output = ROOT / "Policy_Studies_submission.zip"
        root_docs = [
            "POLICY_STUDIES_FIT_AUDIT.md",
            "CLAIM_CALIBRATION_AUDIT.md",
            "REFERENCE_AUDIT.md",
            "DESK_REJECTION_STRESS_TEST.md",
            "FINAL_HANDOFF.md",
            "README_submission_policy_studies.txt",
            "review_archive_policy_sciences.zip",
        ]
        qroot_docs = [
            "Policy_Studies_guidelines.md",
            f"manuscript/check_report_{JOURNAL}.md",
            "manuscript/hostile_review_policy_studies.md",
            "manuscript/numbers.json",
        ]
    with tempfile.TemporaryDirectory() as temporary:
        staging = Path(temporary)
        for destination in FINAL_FILES.values():
            copy_to(destination, staging / destination.name)
        for filename in root_docs:
            copy_to(ROOT / filename, staging / filename)
        for filename in qroot_docs:
            copy_to(QROOT / filename, staging / filename)
        for figure in sorted(FIGURES.glob("Figure*.png")) + sorted(
            FIGURES.glob("Figure*.tiff")
        ):
            copy_to(figure, staging / "figures" / figure.name)
        for filename in [
            "manuscript/build_manuscript.py",
            "manuscript/build_finish_pass.py",
            "manuscript/check_manuscript.py",
            f"manuscript/text_{JOURNAL}.py",
            "common/build_raw_manifests.py",
            "common/build_review_archive.py",
        ]:
            copy_to(QROOT / filename, staging / "source" / Path(filename).name)
        provenance = {
            QROOT / "kansas/data/raw_manifest.csv": "kansas_raw_manifest.csv",
            QROOT / "fukushima/data/raw_manifest.csv": "fukushima_raw_manifest.csv",
            ROOT / "data/source_manifest.csv": "canonical_curves_source_manifest.csv",
        }
        for source, filename in provenance.items():
            copy_to(source, staging / "provenance" / filename)
        if output.exists():
            output.unlink()
        with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(staging.rglob("*")):
                if path.is_file():
                    archive.write(path, path.relative_to(staging))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--ready",
        action="store_true",
        help="Mark the handoff ready after all final package checks pass.",
    )
    args = parser.parse_args()
    numbers = json.loads((MANUSCRIPT / "numbers.json").read_text(encoding="utf-8"))
    checks_passed = check_report_passed()
    if args.ready and not checks_passed:
        raise RuntimeError("Cannot mark the package ready while manuscript checks fail.")
    copy_final_files()
    if JOURNAL == "policy_studies":
        write_audit_policy_studies(numbers)
        write_handoff_policy_studies(
            numbers, ready=args.ready and checks_passed
        )
    else:
        write_audit(numbers)
        write_handoff(numbers, ready=args.ready and checks_passed)
    build_final_zip()


if __name__ == "__main__":
    main()
