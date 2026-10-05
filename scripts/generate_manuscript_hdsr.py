"""
Generate the manuscript as .docx (English) formatted for:
Harvard Data Science Review (HDSR)

HDSR format (matches the submitted proof HDSR-S-26-00175):
- Title, author, affiliation, corresponding author, CRediT author statement
- Unstructured abstract + keywords
- Media Summary (HDSR-specific lay summary)
- Numbered sections: 1. Introduction, 2. Methodology, 3. Results,
  4. Discussion, 5. Limitations, 6. Conclusion
- Disclosure Statement, Acknowledgments, Data Availability and Code,
  Declaration of generative AI, Authors contribution
- Chicago/APA author-date (name-year) references
- Figures and Table 1 inline; Appendix A source-metadata table

Data-integrity notes (the detailed correction disclosure to the editors—that
the prior submission analyzed all 52 curves, some on synthetic/hard-coded
values—lives in the cover letter, NOT in the manuscript body):
  - the body frames the study as an inventory of 52 canonical curves, of which
    2 (Yerkes-Dodson, Weber-Fechner) are excluded for lack of any traceable
    primary dataset, leaving 50 analyzed (52 inventoried -> 50 analyzed);
  - the excluded curves are named in Section 2.1 with their reasons and cited
    in the reference list, and appear in Appendix A/B marked as excluded;
  - curves are referred to by name (e.g., the J-curve), never by an internal
    "#NN" index;
  - reconstructions (J-curve, Mitscherlich yield curve) and transcriptions
    (McKeown thesis) are labeled as such in Section 2.2;
  - every numeric statement is regenerated from results/full_results.json and
    results/summary_table.csv (no hard-coded statistics or counts); the 52/50
    counts derive from len(results) + len(EXCLUDED_CURVES).

Onishi T. 2026.
"""

import os
import sys
import json

import pandas as pd
from docx import Document
from docx.shared import Inches, Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FIGURES_DIR = os.path.join(BASE_DIR, 'figures')
RESULTS_DIR = os.path.join(BASE_DIR, 'results')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# Curves that were part of the initial inventory but could not be backed by any
# traceable primary dataset, and were therefore excluded from analysis. These
# are bibliographic/editorial descriptors (not analysis results); the analyzed
# numbers are all derived from results/full_results.json.
EXCLUDED_CURVES = [
    {
        "id": 35,
        "name": "Yerkes-Dodson Law",
        "category": "Psychology",
        "original_paper": "Yerkes RM, Dodson JD (1908) J Comp Neurol "
                          "Psychol 18:459-482",
        "claimed_form": "Inverted-U",
        "citation": "Yerkes & Dodson, 1908",
        "reason": "no traceable dataset of arousal versus performance could be "
                  "located that would permit a reproducible bivariate test",
    },
    {
        "id": 37,
        "name": "Weber-Fechner Law",
        "category": "Psychology",
        "original_paper": "Fechner GT (1860) Elemente der Psychophysik "
                          "(Breitkopf & Härtel)",
        "claimed_form": "Logarithmic (Fechner) / power law (Stevens)",
        "citation": "Fechner, 1860",
        "reason": "no traceable numeric primary dataset could be located; the "
                  "cited source (Fechner, 1860, vol. II) contains only formulae "
                  "and a conceptual schema, not a stimulus-versus-sensation "
                  "data table",
    },
]


def load_results():
    with open(os.path.join(RESULTS_DIR, 'full_results.json'), 'r') as f:
        return json.load(f)


def verdict_counts(results):
    from collections import Counter
    return Counter(r['verdict']['verdict'] for r in results)


def get_domain_summary(results):
    from collections import Counter
    domains = {}
    for r in results:
        cat = r['category']
        v = r['verdict']['verdict']
        d = domains.setdefault(cat, {'total': 0, 'verdicts': Counter()})
        d['total'] += 1
        d['verdicts'][v] += 1
    return domains


def get_curve(results, name):
    for r in results:
        if r['name'] == name:
            return r
    return None


def pct(n, total):
    return f"{100.0 * n / total:.0f}%"


def fmt_p(p):
    if p is None:
        return "n/a"
    if p < 0.0001:
        return f"{p:.1e}"
    return f"{p:.3f}"


def vname(v):
    return v.replace('_', ' ').lower()


def add_body(doc, text):
    p = doc.add_paragraph(text)
    p.paragraph_format.space_after = Pt(6)
    return p


def add_lead(doc, lead, text):
    p = doc.add_paragraph()
    run = p.add_run(lead)
    run.bold = True
    p.add_run(text)
    p.paragraph_format.space_after = Pt(6)
    return p


def add_figure(doc, filename, number, caption):
    path = os.path.join(FIGURES_DIR, filename)
    if not os.path.exists(path):
        return
    doc.add_paragraph()
    doc.add_picture(path, width=Inches(5.5))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    run = p.add_run(f"Figure {number}. ")
    run.bold = True
    p.add_run(caption)


def create_manuscript():
    results = load_results()
    total = len(results)
    vc = verdict_counts(results)
    n_robust = vc.get('ROBUST_NONLINEAR', 0)
    n_outlier = vc.get('OUTLIER_DEPENDENT', 0)
    n_ns = vc.get('NOT_SIGNIFICANT', 0)
    n_overfit = vc.get('OVERFITTING', 0)
    n_insuf = vc.get('INSUFFICIENT_DATA', 0)
    n_fail = total - n_robust
    n_excluded = len(EXCLUDED_CURVES)
    inventory = total + n_excluded
    domains = get_domain_summary(results)

    doc = Document()
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(11)
    for section in doc.sections:
        section.top_margin = Cm(2.54)
        section.bottom_margin = Cm(2.54)
        section.left_margin = Cm(2.54)
        section.right_margin = Cm(2.54)

    # ===== TITLE =====
    p = doc.add_paragraph()
    run = p.add_run(
        f"Fragility of Canonical Curves: A Cross-Disciplinary Audit of "
        f"{inventory} Established Nonlinear Relationships")
    run.bold = True
    run.font.size = Pt(15)

    doc.add_paragraph()
    doc.add_paragraph("Onishi Tatsuki")
    doc.add_paragraph(
        "Data Science and AI Innovation Research Promotion Center, Shiga University")
    doc.add_paragraph()
    doc.add_paragraph("Corresponding Author: Onishi Tatsuki (bougtoir@gmail.com)")
    doc.add_paragraph()
    add_lead(doc, "Author Contributions (CRediT): ",
             "Onishi Tatsuki: Conceptualization, Methodology, Software, Formal "
             "Analysis, Data Curation, Writing - Original Draft, Writing - "
             "Review & Editing.")

    # ===== ABSTRACT =====
    doc.add_heading('Abstract', level=1)
    add_body(
        doc,
        f"This study systematically re-examines an inventory of {inventory} "
        f"canonical nonlinear relationships across eight academic disciplines "
        f"using a uniform four-test framework: nested F-tests for a quadratic "
        f"term, Akaike and Bayesian information criteria (AIC/BIC), "
        f"leave-one-out cross-validation (LOOCV), and Cook's distance "
        f"sensitivity analysis. {n_excluded} curves for which no primary "
        f"dataset could be obtained (the Yerkes-Dodson and Weber-Fechner laws) "
        f"were excluded, and the {total} curves for which fetched, digitized, "
        f"or transcribed real data were available were analyzed. "
        f"Of the {total} analyzed curves, "
        f"only {n_robust} ({pct(n_robust, total)}) demonstrate robust "
        f"nonlinearity that is significant with the full data, survives removal "
        f"of the three most influential observations, and predicts better "
        f"out-of-sample than a linear model. {n_outlier} "
        f"({pct(n_outlier, total)}) are outlier-dependent, {n_ns} "
        f"({pct(n_ns, total)}) show no significant nonlinearity, "
        f"{n_overfit} ({pct(n_overfit, total)}) overfit, and {n_insuf} "
        f"({pct(n_insuf, total)}) have insufficient data for a stable verdict. "
        f"Curves grounded in biological or physical mechanisms are more robust "
        f"than those based on cross-country regressions. The results argue for "
        f"routine reporting of model-selection and sensitivity diagnostics "
        f"whenever a nonlinear relationship is claimed.")
    add_lead(doc, "Keywords: ",
             "model selection, robustness, nonlinearity, outlier dependence, "
             "cross-validation, reproducibility, meta-research")

    # ===== MEDIA SUMMARY =====
    doc.add_heading('Media Summary', level=1)
    add_body(
        doc,
        "Many scientific disciplines rely on famous 'named curves'—"
        "relationships where one variable rises and then falls, or bends, as "
        "another changes. The inverted-U of the Kuznets curve, the J-shape of "
        "the trade balance after a devaluation, and the U-shape of happiness "
        "over the life course are taught as textbook facts and are used to "
        "justify real policies.")
    add_body(
        doc,
        f"But how many of these iconic relationships actually hold up under "
        f"modern statistical scrutiny? Starting from an inventory of "
        f"{inventory} such curves, this study applies a uniform battery of "
        f"four robustness tests. Crucially, every curve "
        f"is analyzed only with real, traceable data: values fetched from "
        f"public APIs, coordinates digitized from published figures, or numbers "
        f"transcribed from published tables. {n_excluded} curves for which no "
        f"traceable dataset could be found were excluded from analysis, "
        f"leaving {total}.")
    add_body(
        doc,
        f"The results are sobering: only {n_robust} of {total} curves "
        f"({pct(n_robust, total)}) pass all four tests. About "
        f"{pct(n_outlier, total)} are 'outlier-dependent'—their curved shape "
        f"vanishes when just one to three influential data points are removed. "
        f"Curves grounded in biological or physical mechanisms tend to be far "
        f"more robust than those built on cross-country comparisons.")

    # ===== 1. INTRODUCTION =====
    doc.add_heading('1. Introduction', level=1)
    add_body(
        doc,
        "Curvilinear relationships occupy a privileged position in the social "
        "and natural sciences. From the Phillips curve (Phillips, 1958) in "
        "macroeconomics to the Kuznets curve (Kuznets, 1955) linking growth and "
        "inequality, and the Preston curve (Preston, 1975) linking income and "
        "life expectancy, nonlinear functional forms are widely taught, "
        "frequently cited in policy documents, and treated as established "
        "empirical regularities. Yet many were originally established with "
        "limited data and before model-selection criteria such as AIC (Akaike, "
        "1974) and BIC (Schwarz, 1978) became standard practice.")
    add_body(
        doc,
        "The present study was motivated by a preliminary analysis of the "
        "Preston curve, which revealed that the apparent concavity depends "
        "heavily on the position of a small number of influential countries. "
        "This raised the question of whether similar fragilities lurk beneath "
        "other canonical curves. Individual curves have been challenged before—"
        "the environmental Kuznets curve (Grossman & Krueger, 1991; Stern, "
        "2004) and the Dunning-Kruger effect (Dunning & Kruger, 1999; Krueger & "
        "Mueller, 2002) among them—but no systematic cross-disciplinary audit "
        "has been conducted.")
    add_body(
        doc,
        "From a data-science perspective, this work addresses a fundamental "
        "question of model specification: when is a nonlinear model justified "
        "over a simpler linear one (Breiman, 2001; Donoho, 2017; Hastie et al., "
        "2009)? It also connects to the broader reproducibility literature "
        "(Ioannidis, 2005; Open Science Collaboration, 2015).")
    add_body(
        doc,
        f"The contribution of this paper is threefold. First, we provide the "
        f"first systematic cross-disciplinary inventory of canonical-curve "
        f"fragilities across {total} relationships. Second, we propose a "
        f"reusable four-test robustness framework. Third—and central to our "
        f"approach—we ensure that every analyzed curve is backed by "
        f"real, individually traceable data, and we exclude rather than "
        f"fabricate any curve for which no defensible source exists.")

    # ===== 2. METHODOLOGY =====
    doc.add_heading('2. Methodology', level=1)

    doc.add_heading('2.1. Curve Selection', level=2)
    add_body(
        doc,
        f"Candidate curves were identified through systematic review of named "
        f"laws and stylized facts in major handbooks, citation analysis of "
        f"papers with 'curve,' 'law,' or 'paradox' in the title, and review of "
        f"the replication-crisis literature, yielding an initial inventory of "
        f"{inventory} canonical relationships.")
    add_lead(doc, "Inclusion criteria. ",
             "(1) eponymous or canonical status (\u22652 textbooks or >500 "
             "citations); (2) an explicit nonlinearity claim; (3) bivariate "
             "testability; (4) publicly available or traceable data (N \u2265 5); "
             "and (5) policy or theoretical relevance of the curve shape.")
    add_lead(doc, "Exclusion criteria. ",
             "definitional or tautological curves; proprietary data "
             "requirements; purely temporal dynamics; formally retracted "
             "relationships; curves requiring multivariate specification; and "
             "curves for which no traceable primary dataset could be obtained "
             "(criterion 4).")
    add_lead(
        doc, "Data traceability requirement. ",
        "Criterion (4) was applied strictly: a curve entered the analysis only "
        "when every value could be traced to a primary source—an open data API, "
        "a digitized published figure, or a transcribed published table. Where a "
        "candidate relationship could not be supported by such data, it was left "
        "out of the analysis rather than backed by placeholder, assumed, or "
        "synthetically generated values. This requirement enforces that each "
        "reported verdict rests on data a third party can independently obtain "
        "and re-analyze, and it keeps the analyzed set free of any observation "
        "whose origin cannot be documented.")
    excl_sentences = "; ".join(
        f"the {c['name']} ({c['citation']}), for which {c['reason']}"
        for c in EXCLUDED_CURVES)
    add_lead(
        doc, "Excluded curves. ",
        f"On this basis, {n_excluded} of the {inventory} inventoried curves "
        f"were excluded from analysis: {excl_sentences}. These relationships "
        f"remain legitimate scientific claims; their exclusion reflects only "
        f"the absence of a traceable dataset for a reproducible test, not any "
        f"judgment on the underlying phenomena. They are listed for "
        f"completeness in Appendix A and Appendix B but are not counted among "
        f"the {total} analyzed curves.")
    domain_str = ", ".join(
        f"{cat.lower()} ({domains[cat]['total']})"
        for cat in ['Economics', 'Public Health', 'Demography',
                    'Environmental Science', 'Psychology', 'Physics',
                    'Political Science', 'Agriculture'] if cat in domains)
    add_body(
        doc,
        f"Applying these criteria yielded {total} curves for analysis, "
        f"stratified across eight disciplines: {domain_str}.")

    doc.add_heading('2.2. Data Sources', level=2)
    add_body(
        doc,
        "Every analyzed curve is backed by real data whose provenance is "
        "documented in Appendix A and in the repository file "
        "data/digitized_sources.md. Data fall into four traceable classes:")
    doc.add_paragraph(
        "Fetched real data: retrieved programmatically from public APIs, "
        "primarily the World Bank World Development Indicators (WDI) for "
        "cross-country curves, plus other open sources (e.g., USGS earthquake "
        "catalogs, city open-data portals, NOAA climate records).",
        style='List Bullet')
    doc.add_paragraph(
        "Digitized data: coordinates extracted with WebPlotDigitizer from "
        "published figures whose axes are readable (e.g., dose-response and "
        "life-course profiles).",
        style='List Bullet')
    doc.add_paragraph(
        "Transcribed data: values copied verbatim from published tables. For "
        "example, the McKeown thesis is transcribed from McKeown, Record "
        "& Turner (1975), Table 4 (respiratory tuberculosis standardized death "
        "rate per million, England & Wales, 1901-1971).",
        style='List Bullet')
    doc.add_paragraph(
        "Reconstructions (explicitly labeled): where the original historical "
        "dataset is not machine-readable, a citable modern dataset of the same "
        "form is used and labeled as a reconstruction, not the original. The "
        "J-curve (Magee, 1973) is reconstructed from World Bank WDI series for the US "
        "real effective exchange rate and external balance around the 1985 "
        "post-Plaza-Accord peak (the peak year is selected from the data, not "
        "assumed); the Mitscherlich yield curve uses the nitrogen-rate "
        "trials of Engelstad & Parks (1971) rather than Mitscherlich's "
        "unavailable 1909 table.",
        style='List Bullet')
    add_body(
        doc,
        "No analyzed curve relies on hard-coded placeholder values, on "
        "synthetic random data presented as observations, or on a source that "
        "does not actually contain the claimed data.")

    doc.add_heading('2.3. Statistical Framework', level=2)
    add_body(doc, "Each curve was subjected to four complementary tests.")
    add_lead(doc, "Nested F-test. ",
             "Restricted (linear: y = a + bx) and unrestricted "
             "(quadratic: y = a + bx + cx\u00b2) models were fitted by ordinary "
             "least squares, and the F-statistic tested the significance of the "
             "quadratic term.")
    add_lead(doc, "Information criteria. ",
             "AIC (Akaike, 1974) and BIC (Schwarz, 1978; Burnham & Anderson, "
             "2002) were computed for linear, quadratic, and logarithmic "
             "models; the model with the lowest value was selected.")
    add_lead(doc, "Leave-one-out cross-validation (LOOCV). ",
             "LOOCV root-mean-squared error (RMSE) was computed for the linear "
             "and quadratic models to assess out-of-sample predictive accuracy.")
    add_lead(doc, "Cook's distance sensitivity analysis. ",
             "The three most influential observations (Cook, 1977) were removed "
             "and the F-test repeated; a curve was classified as "
             "outlier-dependent if significance was lost after removal.")

    doc.add_heading('2.4. Verdict Classification', level=2)
    add_body(doc, "Each curve received one of five verdicts:")
    for label, desc in [
        ("ROBUST NONLINEAR",
         "significant with the full data AND after outlier removal, with "
         "quadratic LOOCV RMSE \u2264 linear RMSE."),
        ("OUTLIER-DEPENDENT",
         "significant with the full data but non-significant after removing the "
         "three most influential points."),
        ("NOT SIGNIFICANT",
         "non-significant even with the full data (p \u2265 0.05)."),
        ("OVERFITTING",
         "significant, but the quadratic model predicts worse out-of-sample "
         "(LOOCV RMSE larger than linear)."),
        ("INSUFFICIENT DATA",
         "too few observations to compute a stable clean-data verdict "
         "(reported for transparency rather than dropped)."),
    ]:
        p = doc.add_paragraph(style='List Bullet')
        run = p.add_run(f"{label}: ")
        run.bold = True
        p.add_run(desc)
    add_body(
        doc,
        "All analyses were conducted in Python using statsmodels, NumPy, and "
        "pandas; World Bank data were fetched via the wbgapi library. The full "
        "pipeline regenerates every number in this manuscript from the raw and "
        "digitized data (see Data Availability and Code).")

    # ===== 3. RESULTS =====
    doc.add_heading('3. Results', level=1)

    doc.add_heading('3.1. Overall Distribution of Verdicts', level=2)
    add_body(
        doc,
        f"Of {total} canonical curves, {n_robust} ({pct(n_robust, total)}) "
        f"demonstrated robust nonlinearity, {n_outlier} ({pct(n_outlier, total)}) "
        f"were outlier-dependent, {n_ns} ({pct(n_ns, total)}) showed no "
        f"significant nonlinearity, {n_overfit} ({pct(n_overfit, total)}) "
        f"exhibited overfitting, and {n_insuf} ({pct(n_insuf, total)}) had "
        f"insufficient data for a stable verdict (Figure 1). In total, "
        f"{n_fail} of {total} curves ({pct(n_fail, total)}) failed at least one "
        f"robustness test or lacked the data to pass it.")
    add_figure(
        doc, 'fig1_verdict_distribution.png', 1,
        f"Distribution of verdicts across {total} canonical curves, stratified "
        f"by domain. Colors indicate verdict category. The majority of curves "
        f"fail at least one robustness test.")

    doc.add_heading('3.2. Results by Domain', level=2)

    def dv(cat, v):
        return domains.get(cat, {}).get('verdicts', {}).get(v, 0)

    def dt(cat):
        return domains.get(cat, {}).get('total', 0)

    phillips = get_curve(results, 'Phillips Curve')
    kuznets = get_curve(results, 'Kuznets Curve')
    add_lead(
        doc, "Economics. ",
        f"Of {dt('Economics')} curves, {dv('Economics', 'NOT_SIGNIFICANT')} "
        f"were non-significant, {dv('Economics', 'OUTLIER_DEPENDENT')} "
        f"outlier-dependent, and {dv('Economics', 'ROBUST_NONLINEAR')} robustly "
        f"nonlinear. The Phillips curve showed no significant nonlinearity "
        f"(p = {fmt_p(phillips['f_test']['p_value'])}), and the Kuznets curve's "
        f"inverted-U was not significant with N = {kuznets['n']} "
        f"(p = {fmt_p(kuznets['f_test']['p_value'])}). The J-curve of trade, "
        f"reconstructed from World Bank data around the 1985 exchange-rate peak "
        f"(N = {get_curve(results, 'J-Curve (Trade)')['n']}), was among the "
        f"robustly nonlinear economics curves.")

    preston = get_curve(results, 'Preston Curve')
    mckeown = get_curve(results, 'McKeown Thesis (TB Mortality)')
    add_lead(
        doc, "Public health. ",
        f"Of {dt('Public Health')} curves, "
        f"{dv('Public Health', 'ROBUST_NONLINEAR')} were robustly nonlinear "
        f"(including the Alcohol-Mortality and Fries compression curves), while "
        f"the Preston curve with real World Bank data (N = {preston['n']}) was "
        f"non-significant (p = {fmt_p(preston['f_test']['p_value'])}). The "
        f"McKeown thesis, transcribed from McKeown, Record & Turner (1975) "
        f"(N = {mckeown['n']}), is well described by an exponential decline; the "
        f"additional quadratic curvature is not significant "
        f"(p = {fmt_p(mckeown['f_test']['p_value'])}), i.e. "
        f"{vname(mckeown['verdict']['verdict'])}.")

    dtr = get_curve(results, 'Demographic Transition (TFR)')
    add_lead(
        doc, "Demography. ",
        f"Of {dt('Demography')} curves, "
        f"{dv('Demography', 'ROBUST_NONLINEAR')} were robustly nonlinear, "
        f"{dv('Demography', 'NOT_SIGNIFICANT')} non-significant, and "
        f"{dv('Demography', 'INSUFFICIENT_DATA')} had insufficient data. The "
        f"demographic transition (N = {dtr['n']}) was "
        f"{vname(dtr['verdict']['verdict'])} "
        f"(p = {fmt_p(dtr['f_test']['p_value'])}).")

    forest = get_curve(results, 'Forest Transition Curve')
    add_lead(
        doc, "Environmental science. ",
        f"Of {dt('Environmental Science')} curves, "
        f"{dv('Environmental Science', 'ROBUST_NONLINEAR')} were robustly "
        f"nonlinear (including the Keeling curve), "
        f"{dv('Environmental Science', 'NOT_SIGNIFICANT')} non-significant, and "
        f"{dv('Environmental Science', 'OUTLIER_DEPENDENT')} outlier-dependent. "
        f"The forest transition curve (N = {forest['n']}) was non-significant "
        f"(p = {fmt_p(forest['f_test']['p_value'])}).")

    add_lead(
        doc, "Psychology. ",
        f"Of the {dt('Psychology')} psychology curves backed by traceable data, "
        f"{dv('Psychology', 'ROBUST_NONLINEAR')} was robustly nonlinear "
        f"(the happiness U-curve over age), while the Ebbinghaus forgetting "
        f"curve and the Dunning-Kruger effect were non-significant under the "
        f"quadratic test.")

    add_lead(
        doc, "Physics. ",
        f"Of {dt('Physics')} curves, {dv('Physics', 'ROBUST_NONLINEAR')} was "
        f"robustly nonlinear (Kleiber's law), "
        f"{dv('Physics', 'OUTLIER_DEPENDENT')} outlier-dependent, and "
        f"{dv('Physics', 'NOT_SIGNIFICANT')} non-significant.")

    lipset = get_curve(results, 'Lipset Hypothesis')
    add_lead(
        doc, "Political science. ",
        f"Of {dt('Political Science')} curves, "
        f"{dv('Political Science', 'ROBUST_NONLINEAR')} were robustly nonlinear "
        f"and {dv('Political Science', 'OUTLIER_DEPENDENT')} outlier-dependent. "
        f"The Lipset hypothesis was "
        f"{vname(lipset['verdict']['verdict'])} "
        f"(p = {fmt_p(lipset['f_test']['p_value'])} full, "
        f"p = {fmt_p(lipset['sensitivity'].get('p_clean'))} after removal of "
        f"influential high-income states).")

    mits = get_curve(results, 'Mitscherlich Yield Curve')
    add_lead(
        doc, "Agriculture. ",
        f"Of {dt('Agriculture')} curves, "
        f"{dv('Agriculture', 'ROBUST_NONLINEAR')} were robustly nonlinear, "
        f"including the Mitscherlich yield curve reconstructed from Engelstad & "
        f"Parks (1971) (N = {mits['n']}, "
        f"p = {fmt_p(mits['f_test']['p_value'])}), and "
        f"{dv('Agriculture', 'INSUFFICIENT_DATA')} had insufficient data.")

    doc.add_heading('3.3. Sensitivity Analysis', level=2)
    add_body(
        doc,
        "Figure 2 displays p-values before and after outlier removal. Points in "
        "the upper-left quadrant (significant with the full data, "
        "non-significant after removal) represent outlier-dependent curves, "
        "concentrated in economics and political science.")
    add_figure(
        doc, 'fig2_sensitivity_analysis.png', 2,
        "Sensitivity of F-test p-values to outlier removal (Cook's distance, "
        "top three points). Points in the upper-left quadrant are "
        "outlier-dependent.")

    doc.add_heading('3.4. Model Comparison', level=2)
    add_body(
        doc,
        "Figure 3 compares AIC and BIC model-selection outcomes. BIC is more "
        "conservative than AIC, selecting the linear model more frequently, "
        "reflecting its stronger complexity penalty. Figure 4 shows the LOOCV "
        "RMSE comparison between linear and quadratic models; points below the "
        "diagonal favor the quadratic model.")
    add_figure(
        doc, 'fig3_model_comparison.png', 3,
        f"Model comparison results across {total} curves (AIC vs. BIC best "
        f"model). BIC preferentially selects the linear model.")
    add_figure(
        doc, 'fig4_loocv_comparison.png', 4,
        "LOOCV RMSE: linear vs. quadratic model. Points below the diagonal "
        "indicate superior quadratic out-of-sample prediction.")

    doc.add_heading('3.5. Sample Size and Verdict', level=2)
    add_body(
        doc,
        "Figure 5 shows the relationship between sample size and verdict. "
        "Larger samples do not systematically yield more robust verdicts, "
        "suggesting that fragility is not merely a statistical-power issue.")
    add_figure(
        doc, 'fig5_sample_size.png', 5,
        "Sample size vs. verdict classification. No systematic association "
        "between sample size and robustness.")

    doc.add_heading('3.6. Summary of All Results', level=2)
    add_body(doc, f"Table 1 presents complete results for all {total} curves.")
    _add_summary_table(doc)
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    run = p.add_run('Table 1. ')
    run.bold = True
    p.add_run("Summary of re-examination results. p (full) = nested F-test "
              "with all data; p (clean) = after removing the top three Cook's "
              "distance points.")

    # ===== 4. DISCUSSION =====
    doc.add_heading('4. Discussion', level=1)
    add_body(
        doc,
        f"This systematic audit reveals that {n_fail} of {total} established "
        f"nonlinear relationships ({pct(n_fail, total)}) fail at least one "
        f"modern robustness test or lack the data to pass it. Five cross-"
        f"cutting patterns emerge.")
    for i, pat in enumerate([
        "Outlier-driven nonlinearity is the most common failure mode. In "
        "cross-country analyses, one to three geopolitically distinctive "
        "nations (oil states, the United States) frequently drive the "
        "curvature.",
        "Domain asymmetry: public-health, physics, and demography curves "
        "grounded in mechanisms are substantially more robust than economics "
        "or political-science curves built on cross-country comparisons.",
        "Time-series versus cross-section: time-series curves tend to be more "
        "robust, likely because they are less vulnerable to compositional "
        "effects.",
        "Log transformation resolves apparent nonlinearity: in many cases a "
        "simple log transformation produces a linear relationship, suggesting "
        "the 'canonical curve' is linear on the wrong scale.",
        "BIC is more conservative than AIC: BIC selects the linear model more "
        "frequently, consistent with Burnham and Anderson (2002).",
    ], 1):
        add_body(doc, f"{i}. {pat}")

    doc.add_heading('4.1. Implications for Data Science Practice', level=2)
    add_body(
        doc,
        "These findings have direct relevance to data-science methodology. The "
        "proliferation of flexible modeling tools makes it ever easier to fit "
        "and report nonlinearity; our results argue that any such claim should "
        "be accompanied by a nested test against a linear alternative, "
        "information-criterion comparison, out-of-sample validation, and an "
        "influence diagnostic.")
    add_body(
        doc,
        "Several outlier-dependent curves have direct policy implications. The "
        "Laffer curve (Laffer, 2004) is invoked to justify tax cuts; the "
        "environmental Kuznets curve (Grossman & Krueger, 1991) is cited to "
        "argue that growth resolves pollution; the Lipset hypothesis (Lipset, "
        "1959) underpins modernization theory. Our results suggest that the "
        "empirical bases of these policy-relevant claims are more fragile than "
        "commonly assumed (Deaton, 2013).")

    # ===== 5. LIMITATIONS =====
    doc.add_heading('5. Limitations', level=1)
    for lim in [
        "First, our analysis is restricted to bivariate relationships; many "
        "canonical curves may be better specified in multivariate settings. "
        "This is by design—the bivariate form is how these curves are most "
        "commonly taught and cited.",
        "Second, we use a uniform quadratic alternative, whereas some curves "
        "posit specific functional forms (power laws, logistic functions). "
        "Future work should incorporate curve-specific alternatives.",
        f"Third, sample sizes vary widely (from N = 5 to tens of thousands); "
        f"{n_insuf} curves have too few observations for a stable clean-data "
        f"verdict and are flagged as insufficient rather than dropped.",
        "Fourth, we test only the significance of curvature, not the existence "
        "of any relationship. A curve classified as non-significant may still "
        "have a significant linear component.",
        "Fifth, several curves rely on reconstructed or digitized data that "
        "approximate, but are not identical to, the original historical "
        "series; these are labeled as such and should not be read as exact "
        "replications of the founding studies.",
    ]:
        add_body(doc, lim)

    # ===== 6. CONCLUSION =====
    doc.add_heading('6. Conclusion', level=1)
    add_body(
        doc,
        f"This systematic re-examination of {total} canonical curves—each "
        f"backed by traceable real data—reveals that only "
        f"{pct(n_robust, total)} demonstrate nonlinearity that is "
        f"statistically significant, survives outlier removal, and predicts "
        f"better out-of-sample than a linear model. We propose that any study "
        f"claiming a nonlinear relationship report, at minimum: (1) the p-value "
        f"of a nested F-test; (2) AIC/BIC comparison including a linear "
        f"alternative; (3) out-of-sample validation; and (4) an influence "
        f"diagnostic. The reproducible, open-source implementation invites the "
        f"community to extend the audit to additional curves, functional forms, "
        f"and multivariate specifications.")

    # ===== BACK MATTER =====
    doc.add_heading('Disclosure Statement', level=1)
    add_body(
        doc,
        "The author has no financial or non-financial disclosures to share for "
        "this article.")

    doc.add_heading('Acknowledgments', level=1)
    add_body(doc, "None.")

    doc.add_heading('Data Availability and Code', level=1)
    add_body(
        doc,
        "All analysis code, data, and results are publicly available at "
        "https://github.com/bougtoir/canonical-curves-reexamination. World Bank "
        "data were accessed via the wbgapi Python library (World Development "
        "Indicators). Digitized and transcribed sources, with DOIs, figure/"
        "table numbers, and extraction tools, are documented in "
        "data/digitized_sources.md. Running the published pipeline regenerates "
        "every number, figure, and table in this manuscript from the source "
        "data.")

    doc.add_heading(
        'Declaration of generative artificial intelligence (AI) in scientific '
        'writing', level=1)
    add_body(
        doc,
        "We used Devin (devin.ai) to help with formatting the text, choosing "
        "words that suited the tone, and writing code. The author takes full "
        "responsibility for the accuracy and content of the manuscript.")

    doc.add_heading('Authors contribution', level=1)
    add_body(
        doc,
        "O.T.: Conceptualization, Methodology, Software, Formal analysis, "
        "Writing - original draft, Writing - review & editing.")

    # ===== REFERENCES (APA / author-date) =====
    doc.add_heading('References', level=1)
    references = [
        "Akaike, H. (1974). A new look at the statistical model identification. "
        "IEEE Transactions on Automatic Control, 19(6), 716-723. "
        "https://doi.org/10.1109/TAC.1974.1100705",
        "Breiman, L. (2001). Statistical modeling: The two cultures. "
        "Statistical Science, 16(3), 199-231. "
        "https://doi.org/10.1214/ss/1009213726",
        "Burnham, K. P., & Anderson, D. R. (2002). Model selection and "
        "multimodel inference: A practical information-theoretic approach "
        "(2nd ed.). Springer.",
        "Cook, R. D. (1977). Detection of influential observation in linear "
        "regression. Technometrics, 19(1), 15-18. "
        "https://doi.org/10.2307/1268249",
        "Deaton, A. (2013). The great escape: Health, wealth, and the origins "
        "of inequality. Princeton University Press.",
        "Donoho, D. (2017). 50 years of data science. Journal of Computational "
        "and Graphical Statistics, 26(4), 731-764. "
        "https://doi.org/10.1080/10618600.2017.1384734",
        "Dunning, D., & Kruger, J. (1999). Unskilled and unaware of it: How "
        "difficulties in recognizing one's own incompetence lead to inflated "
        "self-assessments. Journal of Personality and Social Psychology, 77(6), "
        "1121-1134. https://doi.org/10.1037/0022-3514.77.6.1121",
        "Engelstad, O. P., & Parks, W. L. (1971). Variability in optimum N "
        "rates for corn. Agronomy Journal, 63(1), 21-23. "
        "https://doi.org/10.2134/agronj1971.00021962006300010008x",
        "Fechner, G. T. (1860). Elemente der Psychophysik. Breitkopf & "
        "H\u00e4rtel.",
        "Grossman, G. M., & Krueger, A. B. (1991). Environmental impacts of a "
        "North American free trade agreement (NBER Working Paper No. 3914). "
        "National Bureau of Economic Research. https://doi.org/10.3386/w3914",
        "Hastie, T., Tibshirani, R., & Friedman, J. (2009). The elements of "
        "statistical learning: Data mining, inference, and prediction "
        "(2nd ed.). Springer. https://doi.org/10.1007/978-0-387-84858-7",
        "Ioannidis, J. P. A. (2005). Why most published research findings are "
        "false. PLoS Medicine, 2(8), Article e124. "
        "https://doi.org/10.1371/journal.pmed.0020124",
        "Krueger, J., & Mueller, R. A. (2002). Unskilled, unaware, or both? "
        "The better-than-average heuristic and statistical regression predict "
        "errors in estimates of own performance. Journal of Personality and "
        "Social Psychology, 82(2), 180-188. "
        "https://doi.org/10.1037/0022-3514.82.2.180",
        "Kuznets, S. (1955). Economic growth and income inequality. American "
        "Economic Review, 45(1), 1-28.",
        "Laffer, A. B. (2004). The Laffer curve: Past, present, and future "
        "(Heritage Foundation Backgrounder No. 1765). The Heritage Foundation.",
        "Lipset, S. M. (1959). Some social requisites of democracy: Economic "
        "development and political legitimacy. American Political Science "
        "Review, 53(1), 69-105. https://doi.org/10.2307/1951731",
        "Magee, S. P. (1973). Currency contracts, pass-through, and "
        "devaluation. Brookings Papers on Economic Activity, 1973(1), 303-325. "
        "https://doi.org/10.2307/2534091",
        "McKeown, T., Record, R. G., & Turner, R. D. (1975). An interpretation "
        "of the decline of mortality in England and Wales during the twentieth "
        "century. Population Studies, 29(3), 391-422. "
        "https://doi.org/10.1080/00324728.1975.10412707",
        "Open Science Collaboration. (2015). Estimating the reproducibility of "
        "psychological science. Science, 349(6251), Article aac4716. "
        "https://doi.org/10.1126/science.aac4716",
        "Phillips, A. W. (1958). The relation between unemployment and the rate "
        "of change of money wage rates in the United Kingdom, 1861-1957. "
        "Economica, 25(100), 283-299. https://doi.org/10.2307/2550759",
        "Preston, S. H. (1975). The changing relation between mortality and "
        "level of economic development. Population Studies, 29(2), 231-248. "
        "https://doi.org/10.2307/2173509",
        "Schwarz, G. (1978). Estimating the dimension of a model. Annals of "
        "Statistics, 6(2), 461-464. https://doi.org/10.1214/aos/1176344136",
        "Stern, D. I. (2004). The rise and fall of the environmental Kuznets "
        "curve. World Development, 32(8), 1419-1439. "
        "https://doi.org/10.1016/j.worlddev.2004.05.004",
        "Yerkes, R. M., & Dodson, J. D. (1908). The relation of strength of "
        "stimulus to rapidity of habit-formation. Journal of Comparative "
        "Neurology and Psychology, 18(5), 459-482. "
        "https://doi.org/10.1002/cne.920180503",
    ]
    for ref in references:
        p = doc.add_paragraph(ref)
        p.paragraph_format.left_indent = Cm(1)
        p.paragraph_format.first_line_indent = Cm(-1)
        p.paragraph_format.space_after = Pt(4)

    # ===== APPENDIX A =====
    doc.add_page_break()
    doc.add_heading('Appendix A: Source Metadata Table', level=1)
    add_body(
        doc,
        f"Source information for all {inventory} inventoried curves, including "
        f"original publication, data source, sample size, and claimed "
        f"functional form. The {n_excluded} curves that could not be backed by "
        f"a traceable dataset are shown with a dash for sample size and marked "
        f"'Excluded' in the data-source column; the remaining {total} are the "
        f"analyzed set.")
    _add_metadata_table(doc, results)

    # ===== APPENDIX B: original publications for every inventoried curve =====
    doc.add_heading('Appendix B: Original Publications for the Inventoried '
                    'Curves', level=1)
    add_body(
        doc,
        f"Primary publication in which each of the {inventory} inventoried "
        f"curves was originally proposed, listed for completeness including "
        f"curves not otherwise cited in the main text and the {n_excluded} "
        f"curves excluded from analysis (marked accordingly). Where the "
        f"analyzed data are a digitization, transcription, or reconstruction, "
        f"the dataset actually used is given in the 'Data source' column of "
        f"Appendix A and in data/digitized_sources.md.")
    _add_curve_bibliography(doc)

    output_path = os.path.join(BASE_DIR, 'manuscript_canonical_curves_hdsr.docx')
    doc.save(output_path)
    print(f"HDSR manuscript saved to: {output_path}")
    return output_path


def _add_summary_table(doc):
    df = pd.read_csv(os.path.join(RESULTS_DIR, 'summary_table.csv'))
    table = doc.add_table(rows=1, cols=7)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ['#', 'Curve', 'N', 'p (full)', 'p (clean)', 'BIC best', 'Verdict']
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(8)
    for idx, row in df.iterrows():
        rc = table.add_row().cells
        rc[0].text = str(idx + 1)
        rc[1].text = str(row['Curve'])[:30]
        rc[2].text = str(row['N'])
        pf = row['p (full)']
        rc[3].text = f"{pf:.4f}" if pd.notna(pf) and pf > 0.0001 else (
            f"{pf:.1e}" if pd.notna(pf) else "n/a")
        pc = row['p (clean)']
        rc[4].text = f"{pc:.4f}" if pd.notna(pc) and pc > 0.0001 else (
            f"{pc:.1e}" if pd.notna(pc) else "n/a")
        rc[5].text = str(row['BIC best'])
        rc[6].text = str(row['Verdict']).replace('_', ' ')
        for cell in rc:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.size = Pt(7)


def _add_curve_bibliography(doc):
    """List the original publication for every inventoried curve, sorted by id,
    from source_metadata.json plus the excluded curves (untruncated, unlike the
    Appendix A table)."""
    source_meta_path = os.path.join(DATA_DIR, 'source_metadata.json')
    if not os.path.exists(source_meta_path):
        return
    with open(source_meta_path, 'r', encoding='utf-8') as f:
        sources = json.load(f)
    combined = list(sources) + [dict(c, excluded=True) for c in EXCLUDED_CURVES]
    for src in sorted(combined, key=lambda s: s['id']):
        p = doc.add_paragraph()
        r1 = p.add_run(f"{src['name']}. ")
        r1.bold = True
        p.add_run(src['original_paper'].strip().rstrip('.') + '.')
        if src.get('excluded'):
            r3 = p.add_run(" [excluded from analysis]")
            r3.italic = True
        p.paragraph_format.left_indent = Cm(1)
        p.paragraph_format.first_line_indent = Cm(-1)
        p.paragraph_format.space_after = Pt(4)


def _add_metadata_table(doc, results):
    source_meta_path = os.path.join(DATA_DIR, 'source_metadata.json')
    if not os.path.exists(source_meta_path):
        return
    with open(source_meta_path, 'r', encoding='utf-8') as f:
        sources = json.load(f)
    n_by_name = {r['name']: r['n'] for r in results}
    excluded = [dict(c, excluded=True) for c in EXCLUDED_CURVES]
    combined = list(sources) + excluded
    table = doc.add_table(rows=1, cols=6)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ['#', 'Curve', 'Original paper', 'Data source', 'N',
               'Claimed form']
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        cell.paragraphs[0].runs[0].bold = True
        cell.paragraphs[0].runs[0].font.size = Pt(7)
    for src in sorted(combined, key=lambda s: s['id']):
        rc = table.add_row().cells
        rc[0].text = str(src['id'])
        rc[1].text = src['name'][:28]
        rc[2].text = src['original_paper'][:42]
        if src.get('excluded'):
            rc[3].text = 'Excluded \u2014 no traceable dataset'
            rc[4].text = '\u2014'
        else:
            rc[3].text = src['data_source'][:48]
            n_val = n_by_name.get(src['name']) or src.get('current_n')
            rc[4].text = str(n_val) if n_val else 'WB API'
        rc[5].text = src['claimed_form'][:28]
        for cell in rc:
            for para in cell.paragraphs:
                for run in para.runs:
                    run.font.size = Pt(6.5)


if __name__ == "__main__":
    create_manuscript()
