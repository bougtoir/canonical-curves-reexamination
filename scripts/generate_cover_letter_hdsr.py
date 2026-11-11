"""
Generate the HDSR resubmission cover letter as .docx.

This is a REVISED / CORRECTED cover letter for the resubmission of
"Fragility of Canonical Curves". It discloses the corrections made after the
original submission (52 curves) and reflects the finalized 50-curve analysis.
All numeric statements are pulled from results/full_results.json (no
hard-coded counts).

Onishi T. 2026.
"""

import os
import json
from collections import Counter

from docx import Document
from docx.shared import Pt, Cm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESULTS_DIR = os.path.join(BASE_DIR, 'results')


def load_counts():
    with open(os.path.join(RESULTS_DIR, 'full_results.json'), 'r') as f:
        results = json.load(f)
    total = len(results)
    vc = Counter(r['verdict']['verdict'] for r in results)
    return total, vc


def pct(n, total):
    return f"{100.0 * n / total:.0f}%"


def create_cover_letter():
    total, vc = load_counts()
    n_robust = vc.get('ROBUST_NONLINEAR', 0)
    n_outlier = vc.get('OUTLIER_DEPENDENT', 0)
    n_ns = vc.get('NOT_SIGNIFICANT', 0)
    n_overfit = vc.get('OVERFITTING', 0)
    n_insuf = vc.get('INSUFFICIENT_DATA', 0)

    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(11)
    for section in doc.sections:
        section.top_margin = Cm(2.54)
        section.bottom_margin = Cm(2.54)
        section.left_margin = Cm(2.54)
        section.right_margin = Cm(2.54)

    def para(text, space=6):
        p = doc.add_paragraph(text)
        p.paragraph_format.space_after = Pt(space)
        return p

    para("[Date]")
    para("Editorial Office")
    para("Harvard Data Science Review")
    p = doc.add_paragraph()
    run = p.add_run(
        f'Re: Revised resubmission — "Fragility of Canonical Curves: A '
        f'Cross-Disciplinary Audit of {total} Established Nonlinear '
        f'Relationships" (Manuscript ID: HDSR-S-26-00175)')
    run.bold = True
    p.paragraph_format.space_after = Pt(10)

    para("Dear Editors,")

    para(
        "I am submitting a corrected and revised version of the above "
        "manuscript, which was originally submitted as a proposal reporting 52 "
        "curves. Following submission, I conducted a thorough self-audit of the "
        "data provenance underlying every curve and disclosed the findings to "
        "the editorial office. This revision implements the resulting "
        "corrections. I am grateful for the opportunity to set the record "
        "straight and to strengthen the paper's reproducibility.")

    p = doc.add_paragraph()
    run = p.add_run("Summary of corrections. ")
    run.bold = True
    p.add_run(
        "The original submission contained values that were hard-coded or, in "
        "one case, synthetically generated, together with source-metadata "
        "descriptions that did not always match the implementation. In this "
        "revision:")
    p.paragraph_format.space_after = Pt(4)

    for item in [
        "every analyzed curve is now backed by real data whose provenance is "
        "individually traceable (values fetched from public APIs, coordinates "
        "digitized from published figures, or numbers transcribed from "
        "published tables);",
        "two curves were excluded because no traceable real dataset could be "
        "obtained — the Yerkes-Dodson law (its former data were generated with "
        "a random-number routine) and the Weber-Fechner law (the cited source "
        "contains only formulae and a conceptual schema, not a stimulus-vs-"
        "sensation data table);",
        "the J-curve of trade and the Mitscherlich yield curve are now "
        "explicitly labeled as reconstructions built from citable modern "
        "datasets, not the original historical series;",
        "the McKeown thesis is transcribed verbatim from McKeown, Record & "
        "Turner (1975), Table 4;",
        "every number in the text, figures, and tables is regenerated directly "
        "from the analysis pipeline, with no hard-coded statistics.",
    ]:
        b = doc.add_paragraph(item, style='List Bullet')
        b.paragraph_format.space_after = Pt(3)

    para(
        f"After these corrections, the audit covers {total} curves across eight "
        f"disciplines. Applying the same uniform four-test framework — nested "
        f"F-tests, AIC/BIC model selection, leave-one-out cross-validation, and "
        f"Cook's distance sensitivity analysis — I find that {n_robust} of "
        f"{total} curves ({pct(n_robust, total)}) demonstrate robust "
        f"nonlinearity surviving all tests. {n_outlier} ({pct(n_outlier, total)}) "
        f"are outlier-dependent, {n_ns} ({pct(n_ns, total)}) show no "
        f"significant nonlinearity, {n_overfit} ({pct(n_overfit, total)}) "
        f"overfit, and {n_insuf} ({pct(n_insuf, total)}) have insufficient data "
        f"for a stable verdict. The central message is unchanged and, if "
        f"anything, strengthened: a majority of canonical curves fail at least "
        f"one modern robustness test, and curves grounded in biological or "
        f"physical mechanisms are markedly more robust than those built on "
        f"cross-country regressions.")

    para(
        "I believe this work remains well-suited to HDSR. It addresses a "
        "fundamental data science question — when is a nonlinear model "
        "justified over a simpler linear alternative? — and operationalizes it "
        "as a reproducible, open-source audit framework that the community can "
        "extend. Several policy-relevant curves (the Laffer Curve, the "
        "Environmental Kuznets Curve, and the Lipset Hypothesis) remain "
        "outlier-dependent, meaning that influential policy claims rest on a "
        "handful of distinctive observations.")

    para(
        "All analysis code, data, and results are publicly available on GitHub "
        "(https://github.com/bougtoir/canonical-curves-reexamination), and "
        "running the published pipeline regenerates every number, figure, and "
        "table in the manuscript from the source data. Digitized and "
        "transcribed sources are documented with DOIs, figure/table numbers, "
        "and extraction tools. The manuscript includes a Media Summary suitable "
        "for broad audiences, and a Correction and Data-Integrity Statement "
        "describing the changes above.")

    para(
        "This manuscript is not under consideration elsewhere. I confirm that I "
        "have no conflicts of interest.")

    para(
        "Thank you for your continued consideration. I look forward to your "
        "response.", space=10)

    para("Sincerely,", space=4)
    para("Tatsuki Onishi", space=0)
    para("Data Science and AI Innovation Research Promotion Center, "
         "Shiga University", space=0)
    para("1-1-1, Bamba, Hikone, Shiga, 522-8522, Japan", space=0)
    para("Telephone: +81-749-27-1023", space=0)
    para("E-mail: bougtoir@gmail.com", space=0)

    output_path = os.path.join(BASE_DIR, 'cover_letter_hdsr_revised.docx')
    doc.save(output_path)
    print(f"Cover letter saved to: {output_path}")
    return output_path


if __name__ == "__main__":
    create_cover_letter()
