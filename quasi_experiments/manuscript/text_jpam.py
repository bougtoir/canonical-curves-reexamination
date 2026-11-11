"""Manuscript text for the JPAM submission.

Every numeric statement is a {placeholder} filled from the results files by
build_manuscript.py (see NUMBERS in that file). No numbers are typed here.
Element kinds: h1, h2, p, fig, table, eq, refs. Text is ASCII only; APA
author-date citations because JPAM uses author-date referencing.
"""

TITLE = ("When the Curve Is Not There: Evaluating Policies Justified by "
         "Canonical Relationships, with Evidence from the Fukushima Evacuation "
         "and the Kansas Tax Experiment")

ABSTRACT = (
    "Policy is often justified by a curve rather than by a measured effect: a "
    "linear dose-response relationship that makes any exposure worth avoiding, "
    "or a revenue curve that promises tax cuts will pay for themselves. This "
    "paper asks how well such canonical relationships hold up in public data, "
    "and what happened when governments acted on two of them. We first re-test "
    "{n_curves} textbook nonlinear relationships against current public data with "
    "a pre-specified decision tree; {share_not_robust_pct}% do not survive standard "
    "tests of nonlinearity, outlier removal, and out-of-sample fit, a share that "
    "moves only between {share_min_pct}% and {share_max_pct}% across thresholds. We "
    "then evaluate two policies that invoked relationships whose empirical support is weak precisely where the policy applied. "
    "For the evacuation orders issued after the 2011 Fukushima Daiichi accident, "
    "justified through the linear no-threshold model, municipal vital statistics "
    "for 2005-2019 show excess deaths concentrated in 2011 (about {t1_excess_2011} "
    "above expectation in the ten evacuated municipalities, of which {t1_direct_2011} "
    "were direct disaster deaths) and no persistent excess afterwards; the "
    "2012-2019 crude death rate in evacuated municipalities was {t1_main_att_pct}% "
    "below the difference-in-differences counterfactual (permutation p = "
    "{t1_main_perm_p}), a pattern we attribute mainly to how deaths of long-term "
    "evacuees are recorded rather than to a health benefit. For the 2012 Kansas "
    "income-tax cuts, justified through the Laffer curve, synthetic-control "
    "estimates show individual income-tax revenue per capita {ks_iit_pct}% below "
    "the counterfactual in 2013-2017 (permutation p = {ks_iit_perm_p}) with no "
    "detectable gain in output or employment. Neither policy delivered the "
    "outcome its curve promised. We argue that canonical relationships should be "
    "treated as hypotheses to be tested in the specific policy setting, not as "
    "settled evidence, and we show how routine robustness checks can do that "
    "before the policy is adopted."
)

KEYWORDS = ("policy evaluation; synthetic control; difference-in-differences; "
            "linear no-threshold; Laffer curve; Fukushima; Kansas; robustness")

# ---------------------------------------------------------------------------
BODY = [
    ("h1", "Introduction"),
    ("p",
     "Many policies rest on a shape rather than on a number. The linear "
     "no-threshold (LNT) model holds that cancer risk rises in proportion to "
     "radiation dose with no safe level, so protective action is warranted at "
     "any exposure above background (ICRP, 2007). The Laffer curve holds that "
     "revenue first rises and then falls with the tax rate, so a state on the "
     "wrong side of the peak can cut taxes and collect more (Wanniski, 1978; "
     "Laffer, 2004). Both underpinned the two episodes we study: the protracted "
     "evacuation orders around the Fukushima Daiichi plant after March 2011, "
     "whose 20 mSv reference level comes from LNT-based protection standards, "
     "and the Kansas income-tax reductions enacted in 2012, designed with the "
     "Laffer curve's originator as adviser and defended on the argument that "
     "growth would replace the lost revenue. Both curves also belong to a wider family of textbook "
     "relationships - the Phillips curve, the Kuznets curve, the Preston curve, "
     "the environmental Kuznets curve, and dozens more - that are taught as "
     "established facts and cited in policy debate as if they had been measured "
     "with the precision of a physical constant."),
    ("p",
     "This paper makes two connected arguments. The first is descriptive: when "
     "canonical nonlinear relationships are re-estimated on current public data "
     "with standard diagnostics, most of them are not robust. The second is "
     "evaluative: when policies are justified by such relationships, the "
     "outcomes the curve predicts often fail to appear, while the costs of the "
     "policy do. We do not claim that the underlying theories are false. Sample "
     "sizes are sometimes small, proxies imperfect, and aggregation coarse. Our "
     "claim is narrower and, we think, more useful for policy analysis: the "
     "empirical support for these relationships is weaker than their status "
     "suggests, and that weakness is a reason to test the relationship in the "
     "specific setting before committing resources on the strength of it "
     "(Cartwright & Hardie, 2012)."),
    ("p",
     "We proceed in two steps. Section 2 re-tests {n_curves} canonical curves "
     "drawn from economics, public health, demography, environmental science, "
     "psychology, physics, political science, and agriculture, using a single "
     "pre-specified decision tree and reporting how the verdicts change with the "
     "thresholds. This step is deliberately brief; its role is to show that the "
     "two cases we then study are not isolated. Sections 3 and 4 present the two "
     "policy evaluations. The Fukushima evacuation is the main case because the "
     "policy was explicitly justified by a dose-response model, because its "
     "costs were borne in lives, and because municipal vital statistics allow a "
     "difference-in-differences and synthetic-control design that, to our "
     "knowledge, has not been applied to all-cause mortality in the evacuated "
     "municipalities over the eight years that followed the acute phase. The Kansas tax cuts are the secondary "
     "case: their fiscal outcome is already well documented (Rickman & Wang, "
     "2018), which lets us check that the same methods recover a known answer "
     "before we lean on them for the harder case. Section 5 discusses what the "
     "results do and do not show, and Section 6 draws implications for how "
     "canonical relationships should enter policy analysis."),

    ("h1", "Canonical Curves in Public Data"),
    ("h2", "Design"),
    ("p",
     "We assembled {n_inventory} canonical nonlinear relationships from standard "
     "textbooks and review articles; {n_excluded} (the Yerkes-Dodson law and the "
     "Weber-Fechner law) had no traceable primary dataset and were dropped, "
     "leaving {n_curves} for analysis. For each curve we located a public dataset "
     "that matches the variables in the original claim, documented its source, "
     "and fitted a linear and a quadratic model in the variables as originally "
     "specified (logged where the canonical form is log-linear). Each curve "
     "receives one of five verdicts from a fixed decision tree (Figure 1): the "
     "quadratic term is tested with a nested F-test at level alpha; if "
     "significant, the k most influential observations by Cook's distance (Cook, "
     "1977) are removed and the test repeated; if nonlinearity survives, "
     "leave-one-out cross-validated root-mean-squared error must favour the "
     "quadratic model; and the Bayesian information criterion must not prefer "
     "the linear model (Burnham & Anderson, 2004). Curves with fewer than eight "
     "observations after removal are labelled insufficient. The default is "
     "alpha = {alpha_default} and k = {k_default}; because these choices are "
     "arbitrary, we report every verdict over alpha in {alpha_grid} and k in "
     "{k_grid}."),
    ("fig", "fig_decision_tree"),
    ("h2", "Findings"),
    ("p",
     "At the default thresholds, {n_not_robust} of {n_curves} curves "
     "({share_not_robust_pct}%) are not robustly nonlinear: {n_not_sig} show no "
     "significant curvature in the full sample, {n_outlier} lose it when the most "
     "influential points are removed, {n_overfit} fit worse out of sample than a "
     "straight line, and {n_insufficient} have too few observations to test "
     "(Table 1). The share that is not robust ranges from {share_min_pct}% to "
     "{share_max_pct}% across the threshold grid (Figure 2); no reasonable choice "
     "of alpha or k brings it below half. The two curves that motivate our policy "
     "cases illustrate two different ways in which a canonical relationship can "
     "be weakly supported. The Laffer curve, estimated on top statutory personal "
     "income-tax rates and total tax revenue for {laffer_n} OECD countries, shows "
     "no significant curvature at all (quadratic-term p = {laffer_p}): in the "
     "range of rates actually observed, revenue rises with the rate and there is "
     "no detectable peak. The LNT relationship, estimated on {lnt_n} "
     "dose-response points from the Life Span Study of atomic-bomb survivors "
     "(Ozasa et al., 2012), is consistent with a straight line (p = {lnt_p}), "
     "which is what the model asserts; but only {lnt_n_lowdose} of those points "
     "lie below 0.1 Gy, and in that region a linear, a threshold, and a "
     "curvilinear response fit equally well. The shape the model asserts is "
     "supported where doses are high and untested where protective policy "
     "operates, a limitation long recognised in radiation epidemiology (Brenner "
     "et al., 2003); LNT is adopted in protection standards as a prudent "
     "assumption, not as a measured curve (ICRP, 2007)."),
    ("table", "tab_audit"),
    ("fig", "fig_sensitivity"),
    ("p",
     "We stress what this exercise does not show. A non-significant quadratic "
     "term in a small aggregate dataset is not evidence that a relationship is "
     "absent, and several curves in the robust group (the Keeling curve, "
     "Kleiber's law) are physical regularities of a different character from "
     "the social-science curves that dominate the list. The point is that the "
     "empirical footing of these relationships varies enormously, in a way that "
     "their common label of canonical conceals, and that a policy analyst has no "
     "way of knowing which kind of curve is being invoked without checking."),

    ("h1", "The Fukushima Evacuation and the Linear No-Threshold Model"),
    ("h2", "Policy background"),
    ("p",
     "After the accident of 11 March 2011, the Japanese government ordered "
     "evacuation within 20 km of the plant (the restricted area), designated "
     "additional municipalities to the northwest where projected first-year "
     "doses exceeded 20 mSv as deliberate evacuation areas, and asked residents "
     "of a 20-30 km ring to prepare for evacuation. The 20 mSv per year "
     "reference level is the lower bound of the 20-100 mSv band that ICRP "
     "Publication 103 recommends for emergency exposure situations, itself "
     "derived from LNT risk coefficients (ICRP, 2007). Roughly {evac_pop_approx} "
     "residents of the affected municipalities were displaced; many remained "
     "displaced for years, and orders for parts of the area were not lifted until "
     "the 2020s. The health costs of protracted evacuation for the elderly were "
     "recognised early: mortality among evacuated nursing-home residents rose "
     "sharply in the months after relocation (Yasumura et al., 2013; Nomura et al., "
     "2013), and later analyses concluded that, for this group, the risk from "
     "relocation exceeded the radiation risk avoided (Murakami et al., 2015; "
     "Hasegawa et al., 2015). Population-level projections of radiation harm "
     "from the release, by contrast, were small: the best estimate of "
     "worldwide excess cancer deaths was {thj_best} (range {thj_range}) (ten Hoeve "
     "& Jacobson, 2012), and both the WHO and UNSCEAR assessments concluded that "
     "no discernible increase in radiation-related health effects was expected "
     "in the general population (WHO, 2013; UNSCEAR, 2014). The same authors "
     "estimated that the evacuation itself prevented {thj_averted_best} "
     "radiation-related deaths (range {thj_averted_range}) (ten Hoeve & "
     "Jacobson, 2012). These projections are themselves LNT-based, so they "
     "represent what the model itself says the evacuation could have averted."),
    ("p",
     "Two features of this setting matter for the design. First, the evacuation "
     "orders coincided with the earthquake and tsunami, which killed residents "
     "of coastal municipalities whether or not they were later evacuated, so a "
     "comparison of evacuated and non-evacuated municipalities in 2011 confounds "
     "the two. We therefore separate 2011 from the years that follow and "
     "decompose the 2011 spike using official counts of direct disaster deaths. "
     "Second, the population at risk is defined by registration rather than by "
     "residence: evacuees who kept their registration in the home municipality "
     "remain in the denominator, and their deaths are in principle attributed "
     "to the home municipality. Whether that attribution is complete in practice "
     "is a question we return to when interpreting the post-2011 estimates."),
    ("h2", "Data"),
    ("p",
     "We built a municipality-year panel for all {n_all_units} municipalities in "
     "Fukushima and the seven surrounding prefectures (Miyagi, Iwate, Yamagata, "
     "Ibaraki, Tochigi, Gunma, Niigata) for 2005-2022. Deaths come from the "
     "Vital Statistics municipal tables; population denominators come from the "
     "Basic Resident Register counts published by the Ministry of Internal "
     "Affairs and Communications, which record residents by registered address "
     "and therefore continue to count evacuees who kept their registration in "
     "the home municipality. Age structure comes from the 2010 Population "
     "Census. Municipal mergers are handled by aggregating predecessor units into "
     "the successor municipality; because several mergers were completed during "
     "2005, that year is used only descriptively and estimation starts in 2006. "
     "The resident-register series switched from Japanese nationals to all "
     "residents in 2013; we report a specification that uses a constant-scope "
     "series as a robustness check. Treatment status follows the official "
     "evacuation-order designations. The main treated group (T1) is the "
     "{n_t1} municipalities with any territory in the restricted or deliberate "
     "evacuation areas; a subset (T1w, {n_t1w} municipalities) was evacuated in "
     "its entirety; a separate group (T2, {n_t2} municipalities) was in the "
     "emergency evacuation preparation area only. Because the tsunami killed "
     "residents of coastal municipalities regardless of evacuation status, "
     "control municipalities whose 2011 deaths exceeded {tsunami_cut} times their "
     "2006-2010 mean are excluded, leaving {n_controls} controls with complete "
     "2005-2019 data. Of the {n_all_units} municipalities and wards that exist in "
     "2019, {n_dropped_missing} are dropped because a population or death count "
     "is missing in at least one year or because the unit cannot be followed "
     "under a single code over the whole period; {n_dropped_top_prefs} "
     "(Appendix Table A1 lists them by prefecture and reason). Direct disaster deaths by municipality are "
     "taken from the Fukushima Prefecture damage report (Fukushima Prefecture, "
     "{fdr_year}), and certified disaster-related deaths from the Reconstruction "
     "Agency (Reconstruction Agency, {ra_year})."),
    ("h2", "Empirical strategy"),
    ("p",
     "The outcome is the log crude death rate, ln(CDR), where CDR is deaths per "
     "1,000 registered residents. The main estimator is a two-way fixed-effects "
     "difference-in-differences model,"),
    ("eq", "eq_did"),
    ("p",
     "where D_it equals one for treated municipalities from 2012 onwards, a_i and "
     "g_t are municipality and year effects, and e_it is the error. The "
     "coefficient b is the average post-2011 treatment effect on log mortality; "
     "2011 is excluded from the estimation sample because it mixes the direct "
     "disaster with the first months of evacuation, and is analysed separately "
     "below. An event-study version replaces bD_it with year-specific "
     "coefficients relative to 2010, which we use to inspect pre-trends. We "
     "report eight specifications for T1: controls drawn from all eight "
     "prefectures or from Fukushima only, observations unweighted or weighted by "
     "2010 population, and with or without an interaction of the 2010 share aged "
     "65 and over with year effects. The unweighted, Fukushima-only "
     "specification is the preferred one, because Fukushima controls share the "
     "prefecture-level shocks of the accident (evacuee inflows, reconstruction "
     "spending) and because weighting would let the largest treated city, "
     "Minamisoma, dominate a group of ten. With ten treated clusters, "
     "cluster-robust standard errors are unreliable (Bertrand et al., 2004; "
     "Cameron et al., 2008; Conley & Taber, 2011), so inference is by permutation: "
     "we re-assign treatment to {n_perm} random sets of control municipalities of "
     "the same size and report the share of placebo effects at least as large in "
     "absolute value as the estimate. The same permutation distribution provides "
     "a pre-trend test based on the sum of squared 2006-2009 event-study "
     "coefficients. As a second design we estimate a synthetic control (Abadie et "
     "al., 2010; Abadie, 2021) for the pooled T1 series and for each treated "
     "municipality, with donors restricted to Fukushima controls whose 2010 "
     "share aged 65 and over lies within {sc_age_band} of the treated unit; with "
     "only five pre-treatment years and {n_sc_donors} donors the pre-period fit is "
     "exact, so we report a cross-fit (weights from 2006-2008, error in "
     "2009-2010) as the honest measure of fit and treat the synthetic-control "
     "results as secondary."),
    ("p",
     "The 2011 spike is decomposed as follows. Expected 2011 deaths for each "
     "treated municipality are its 2011 registered population times its 2010 "
     "death rate, scaled by the ratio of pooled control death rates in 2011 to "
     "2010; excess deaths are observed minus expected; and residual excess is "
     "excess minus the officially counted direct disaster deaths. The residual "
     "is an upper bound on deaths attributable to the acute phase of evacuation "
     "within the calendar year, because some indirect deaths would also have "
     "occurred without the evacuation orders."),
    ("h2", "Results"),
    ("p",
     "Figure 3 shows pooled crude death rates. Before 2011 the evacuated "
     "municipalities track the Fukushima controls; in 2011 the T1 rate jumps by "
     "about {t1_2011_jump_pct}%; from 2012 it falls below the control trend and "
     "stays there. Event-study coefficients (Figure 4) show no systematic "
     "pre-trend in the preferred specification (permutation p for the joint "
     "pre-period test = {t1_main_pretrend_p}), a 2011 coefficient of "
     "{t1_main_ev2011} log points, and negative coefficients in every year from "
     "2012 to 2019."),
    ("fig", "fig_pooled_cdr"),
    ("fig", "fig_event_study"),
    ("p",
     "Table 2 reports the difference-in-differences estimates. In the preferred "
     "specification the 2012-2019 log death rate in T1 municipalities is "
     "{t1_main_att} (permutation p = {t1_main_perm_p}), that is, about "
     "{t1_main_att_pct}% below the counterfactual. The estimate is negative and "
     "of similar size in all eight T1 specifications (range {t1_att_min} to "
     "{t1_att_max}), larger in magnitude for the wholly evacuated municipalities "
     "(T1w: {t1w_main_att}, p = {t1w_main_perm_p}), and close to zero with "
     "permutation p above {t2_perm_p_min} in every specification for the "
     "preparation-area group (T2), whose residents were largely not displaced. "
     "Pre-trend permutation p-values exceed 0.05 in all specifications except "
     "the unweighted all-prefecture T1 models ({t1_pretrend_min}), where the "
     "2009 coefficient is negative. Restricting the resident-register series to "
     "a constant scope changes the T1 estimate to {t1_scope_att}. The pooled "
     "synthetic control gives a 2012-2019 mean gap of {sc_agg_gap} log points "
     "(permutation p = {sc_agg_perm_p}; cross-fit RMSPE {sc_agg_crossfit}), and "
     "{n_sc_neg} of the {n_t1} municipality-level synthetic controls have "
     "negative post-period gaps (Appendix Table A2)."),
    ("table", "tab_fuku_att"),
    ("p",
     "The 2011 decomposition (Figure 5, Table 3) puts the acute-phase burden in "
     "perspective. The ten T1 municipalities recorded {t1_obs_2011} deaths in "
     "2011 against {t1_exp_2011} expected, an excess of {t1_excess_2011}. "
     "Officially counted direct disaster deaths in these municipalities number "
     "{t1_direct_2011}, {t1_direct_share_pct}% of the excess and concentrated in "
     "the coastal towns of Minamisoma and Namie. The residual, {t1_resid_2011} "
     "deaths, is our upper bound on evacuation-related mortality recorded in the "
     "home municipalities during 2011. Over 2012-2019 the preferred estimate "
     "implies {t1_main_excess_post} fewer deaths than the counterfactual, about "
     "{t1_main_excess_per_year} per year. Prefecture-wide, the Reconstruction "
     "Agency has certified {ra_related_deaths} disaster-related deaths in "
     "Fukushima as of {ra_date}, an administrative count based on family "
     "applications that is not confined to the evacuated municipalities and is "
     "not directly comparable to our estimates."),
    ("fig", "fig_acute"),
    ("table", "tab_lnt"),

    ("h1", "The Kansas Tax Cuts and the Laffer Curve"),
    ("h2", "Policy background"),
    ("p",
     "In May 2012 Kansas enacted Senate Substitute for House Bill 2117, which "
     "cut the top individual income-tax rate from 6.45% to 4.9%, collapsed the "
     "brackets, and exempted pass-through business income from taxation "
     "(Kansas Legislature, 2012), with further scheduled reductions enacted in "
     "2013. Arthur Laffer advised the governor on the plan, and the argument that "
     "growth would offset the revenue loss was central to its public defence "
     "({kansas_laffer_cite}). The "
     "legislature reversed most of the cuts in June 2017 over the governor's "
     "veto. The Kansas episode has been studied as a natural experiment "
     "(Rickman & Wang, 2018) and its fiscal outcome is not in serious dispute, "
     "which is why we use it here to calibrate the methods. Kansas is also a "
     "reminder that a state economy has shocks of its own: the aircraft "
     "industry around Wichita, farm incomes exposed to commodity prices, and oil "
     "and gas extraction all moved over 2013-2017 for reasons unrelated to the "
     "tax code. The synthetic-control design addresses this by weighting donor "
     "states to match the pre-2013 path of each outcome, and we check the "
     "result against a pool that excludes states with contemporaneous "
     "income-tax reforms and against a pool that does not."),
    ("h2", "Data and strategy"),
    ("p",
     "We assembled a panel of the 50 states and the District of Columbia for "
     "1997-2023 from the Federal Reserve Bank of St. Louis FRED database (real and "
     "nominal GDP, population, nonfarm employment, unemployment) and the Census "
     "Bureau's Annual Survey of State Government Tax Collections (total taxes "
     "and individual income taxes), deflated to 2012 dollars with the CPI. "
     "Outcomes are log real GDP per capita, log nonfarm employment, log real "
     "total tax revenue per capita, and log real individual income-tax revenue "
     "per capita. The synthetic control for Kansas is fitted on {ks_pre_years} "
     "with nonnegative weights summing to one; the main donor pool excludes "
     "{ks_n_excluded} states that either enacted large income-tax changes in the "
     "same window or levy no broad-based income tax, leaving {ks_n_donors} "
     "donors, and an all-state pool is reported as a check. Inference is by "
     "placebo-in-space permutation of the ratio of post- to pre-treatment "
     "root-mean-squared prediction error (Abadie et al., 2010). We also report an "
     "in-time placebo with a pseudo-treatment in 2005, leave-one-donor-out "
     "estimates, and difference-in-differences event studies against the four "
     "neighbouring states (Nebraska, Missouri, Colorado, Iowa) and against the "
     "main pool. The main post-period is 2013-2017; 2018-2019 are shown to cover "
     "the reversal, and 2020 onwards is descriptive only."),
    ("h2", "Results"),
    ("p",
     "Figure 6 and Table 4 summarise the results. Real individual income-tax "
     "revenue per capita fell {ks_iit_pct}% below its synthetic counterpart on "
     "average over 2013-2017 (permutation p = {ks_iit_perm_p}; {ks_iit_pct_all}% "
     "with the all-state pool), a gap that widened from {ks_iit_gap_2013} to "
     "{ks_iit_gap_2016} dollars per resident between 2013 and 2016 and cumulates "
     "to about {ks_iit_cum_bn} billion 2012 dollars over five years. Total tax "
     "revenue per capita was {ks_tax_pct}% below the counterfactual (p = "
     "{ks_tax_perm_p}), reflecting the sales-tax increases enacted to offset the "
     "shortfall. Real GDP per capita ({ks_gdp_pct}%, p = {ks_gdp_perm_p}) and "
     "employment ({ks_emp_pct}%, p = {ks_emp_perm_p}) show no detectable "
     "departure from the counterfactual; the in-time placebo produces gaps of "
     "{ks_placebo_min} to {ks_placebo_max} log points for these outcomes, so "
     "effects of the size observed for output and employment are within the "
     "range the method produces when nothing happened, while the income-tax gap "
     "is several times larger than its placebo. Leave-one-out estimates for the "
     "income-tax outcome lie between {ks_iit_loo_min} and {ks_iit_loo_max}. The "
     "neighbour-state event studies (Appendix Figure A1) agree in sign and "
     "show no pre-trend in the income-tax series."),
    ("fig", "fig_kansas"),
    ("table", "tab_kansas"),

    ("h1", "Discussion"),
    ("h2", "What the two cases show"),
    ("p",
     "In neither case did the outcome the curve promised materialise. Kansas cut "
     "income taxes and collected substantially less income tax, with no visible "
     "growth dividend within five years, which is the result the existing "
     "literature reports and which our methods recover. The Fukushima case is "
     "more complicated and we want to be careful about what it does and does not "
     "show. The mortality cost of the evacuation that is visible in municipal "
     "vital statistics is concentrated in 2011: several hundred deaths above "
     "expectation beyond those directly caused by the earthquake and tsunami, "
     "consistent with the cohort evidence on evacuated nursing-home residents. "
     "Over 2012-2019 we find no persistent excess; instead, recorded death rates "
     "in the evacuated municipalities run {t1_pct_min}-{t1w_pct_max}% below the "
     "counterfactual across the T1 and T1w specifications."),
    ("p",
     "We do not read the post-2011 deficit as a health benefit of evacuation. "
     "Three mechanisms could produce it, and the data cannot cleanly separate "
     "them. First, mortality displacement: the 2011 excess brought forward deaths "
     "of frail residents who would otherwise have died in the following years. "
     "This alone cannot explain the whole deficit, which cumulates to more than "
     "the 2011 residual excess. Second, recording: vital statistics attribute a "
     "death to the address on the death notification, and long-term evacuees who "
     "died in institutions elsewhere may have been recorded there even while they "
     "remained on the home municipality's resident register, which would depress "
     "the numerator relative to the denominator. Third, selective de-registration: "
     "residents who moved their registration to the host municipality were "
     "removed from both numerator and denominator, and if those who left the "
     "register were older or frailer than those who stayed, the remaining "
     "registered population is healthier than the pre-accident one. The second "
     "and third mechanisms are measurement artefacts of protracted displacement, "
     "and the fact that the deficit is largest in the wholly evacuated "
     "municipalities, where displacement was total, and absent in the "
     "preparation-area municipalities, where it was brief, points in their "
     "direction. The methodological lesson is that municipal vital statistics "
     "can measure the acute mortality cost of an evacuation but not its chronic "
     "cost; the latter requires individual follow-up of the displaced population."),
    ("p",
     "Against these costs stands the benefit the LNT model predicts the "
     "evacuation averted. The published LNT-based projections for the entire "
     "release put worldwide excess cancer deaths at {thj_best} (range {thj_range}), "
     "and the WHO and UNSCEAR assessments, which assume LNT, concluded that "
     "no increase would be discernible in the exposed population (Table 3). The "
     "acute-phase residual we measure in ten municipalities, {t1_resid_2011} "
     "deaths, exceeds the model's own best estimate of the deaths the evacuation "
     "prevented ({thj_averted_best}) and is of the same order as its estimate of "
     "the cancer deaths the entire release will eventually cause worldwide "
     "({thj_best}). It is also a count of recorded deaths rather than a "
     "projection. We do not "
     "conclude that the evacuation was wrong: the decision was taken under "
     "uncertainty about how the release would evolve, and the short-range "
     "evacuation in the first days is not what our estimates speak to. Our point "
     "concerns the protracted orders that followed, which were tied to a 20 mSv "
     "reference level whose empirical basis, as Section 2 shows, is an "
     "extrapolation into a dose range where the data used to support it cannot "
     "distinguish a linear response from a threshold. A policy that displaces tens of thousands of "
     "people for years on the strength of such a relationship deserves an "
     "explicit comparison of projected harm avoided against measured harm "
     "caused; that comparison was not made at the time and, when made "
     "retrospectively, does not favour the policy as implemented."),
    ("h2", "Implications for policy analysis"),
    ("p",
     "The two cases differ in almost every respect - country, outcome, unit of "
     "analysis, the direction of the error - and that is the point. What they "
     "share is a decision that treated the shape of a relationship as settled "
     "when the evidence for that shape, in the range where the decision "
     "operated, was thin. The audit in Section 2 suggests this is the normal "
     "condition of canonical curves rather than an unlucky pair. The practical "
     "question is what an analyst can do about it before a policy is adopted, "
     "rather than years afterwards."),
    ("p",
     "The decision tree we used for the audit is a reasonable template. Its four "
     "steps ask whether the curvature is statistically distinguishable from a "
     "straight line in data from the relevant population, whether that finding "
     "depends on a handful of observations, whether the curved model predicts "
     "better out of sample, and whether a penalised criterion still prefers it. "
     "None of these steps is novel; their value is in being applied to the "
     "specific relationship a policy invokes, at the specific range of the "
     "explanatory variable where the policy will operate. For LNT the relevant "
     "range is below 0.1 Gy, where the audit finds {lnt_n_lowdose} data points "
     "and no power to discriminate functional forms; for the Laffer curve it "
     "is the neighbourhood of a 6.45% state top rate, far below any rate at "
     "which the cross-country data show revenue turning down. A second, "
     "complementary step is to write down what the policy would cost if the "
     "curve were flat: a revenue loss equal to the static estimate in the "
     "Kansas case, and the mortality risk of relocating a population with a "
     "high share of elderly residents in the Fukushima case. Both quantities "
     "were knowable at the time, and both turned out to be the dominant term."),
    ("p",
     "The methodological contribution is narrower but, we hope, transferable. "
     "Municipal vital statistics with permutation inference can measure the "
     "acute mortality cost of a mass evacuation and can rule out a large "
     "persistent excess in the registered population, but they cannot measure "
     "the chronic cost of protracted displacement, because displacement itself "
     "changes who is counted where. Evaluations of future evacuations, or of "
     "other policies that move people, should plan for individual-level "
     "follow-up of the displaced from the outset rather than rely on "
     "place-based statistics."),
    ("h2", "Limitations"),
    ("p",
     "The audit in Section 2 uses one dataset per curve and a single quadratic "
     "alternative; a curve could be robustly nonlinear in a form we did not fit, "
     "and several datasets are small. The Fukushima design has ten treated "
     "units, so inference rests on permutation rather than asymptotics and the "
     "power to detect a modest persistent excess is limited; the complete-case "
     "sample drops {n_dropped_missing} of {n_all_units} municipalities, mainly "
     "where resident-register counts are unavailable for 2005-2010, and the tsunami "
     "exclusion rule conditions on a 2011 outcome, which we accept in order to "
     "keep the direct disaster out of the control group. The Kansas synthetic "
     "control has a pre-treatment fit of {ks_iit_rmspe} log points for the "
     "income-tax outcome and an in-time placebo gap of {ks_iit_placebo} for the "
     "same outcome, so the point estimate should be read with a margin of "
     "roughly that size. Finally, two cases cannot establish that policies "
     "justified by canonical curves fail in general; they establish that two "
     "prominent ones did, and Section 2 gives reason to expect they are not "
     "alone."),

    ("h1", "Conclusion"),
    ("p",
     "Canonical curves are efficient ways to teach and to argue, and they will "
     "continue to enter policy debate. What we argue against is treating them as "
     "evidence. Most of the relationships we re-tested are not robust in public "
     "data, and the two policies we evaluated in detail delivered their costs "
     "without their promised benefits. The remedy is not exotic. Before a curve "
     "is used to justify a policy, the analyst can ask whether the relationship "
     "holds in data from the relevant population, whether it survives the "
     "removal of a few influential observations, whether a straight line "
     "predicts as well out of sample, and what the policy would cost if the "
     "curve turned out to be flat. Those checks take days, not years, and they "
     "would have flagged both cases studied here."),

    ("h1", "Notes"),
    ("p",
     "Artificial-intelligence assistance. An AI coding assistant (Devin, Cognition AI) "
     "was used to write and debug the data-acquisition, analysis, and document-generation "
     "code, and to draft and edit the manuscript text under the author's direction. All "
     "data sources, analytical choices, results, and interpretations were specified and "
     "verified by the author, who takes full responsibility for the content."),
    ("h1", "Data Availability Statement"),
    ("p",
     "All data used in this paper are public. The raw downloads, the scripts "
     "that reproduce every number, table, and figure from them, and the "
     "generated results are deposited in a public repository; the link is "
     "provided on the title page and will appear here on publication."),
    ("refs", None),
]

# Captions -------------------------------------------------------------------
CAPTIONS = {
    "fig_decision_tree": (
        "Figure 1. Decision tree used to classify each canonical curve. Each "
        "curve is fitted with linear and quadratic models; the verdict depends "
        "on the nested F-test at level alpha, the same test after removing the "
        "k most influential observations by Cook's distance, leave-one-out "
        "cross-validated prediction error, and the Bayesian information "
        "criterion. Default alpha = {alpha_default}, k = {k_default}."),
    "fig_sensitivity": (
        "Figure 2. Share of the {n_curves} canonical curves not classified as "
        "robustly nonlinear, by significance level alpha and number of "
        "influential observations removed k. The default cell (alpha = "
        "{alpha_default}, k = {k_default}) gives {share_not_robust_pct}%."),
    "fig_pooled_cdr": (
        "Figure 3. Crude death rate per 1,000 registered residents, 2005-2022, "
        "for municipalities in the restricted or deliberate evacuation areas "
        "(T1), the subset evacuated in full (T1w), the emergency evacuation "
        "preparation area (T2), and Fukushima control municipalities. Deaths "
        "from Vital Statistics; population from the Basic Resident Register. "
        "Shaded years (2020-2022) are outside the estimation sample."),
    "fig_event_study": (
        "Figure 4. Event-study estimates of the effect of evacuation orders on "
        "log crude death rate, T1 municipalities versus Fukushima controls, "
        "unweighted, reference year 2010. Points are coefficients; bars are 95% "
        "confidence intervals from municipality-clustered standard errors, shown "
        "for reference only; inference in the text uses permutation."),
    "fig_acute": (
        "Figure 5. Decomposition of 2011 deaths in evacuated municipalities into "
        "expected deaths, direct disaster deaths, and residual excess. Expected "
        "deaths are 2011 population times the 2010 death rate, scaled by the "
        "change in the pooled control death rate. Direct deaths from the "
        "Fukushima Prefecture damage report."),
    "fig_kansas": (
        "Figure 6. Kansas versus synthetic Kansas, main donor pool: log real "
        "individual income-tax revenue per capita (left) and log real GDP per "
        "capita (right), 1997-2019. Vertical lines mark the 2012 enactment and "
        "the 2017 reversal. Synthetic series are convex combinations of "
        "{ks_n_donors} donor states fitted on {ks_pre_years}."),
    "tab_audit": (
        "Table 1. Verdicts for {n_curves} canonical curves at the default "
        "thresholds (alpha = {alpha_default}, k = {k_default}), by field."),
    "tab_fuku_att": (
        "Table 2. Difference-in-differences estimates of the effect of "
        "evacuation orders on log crude death rate, 2012-2019 versus 2006-2010, "
        "2011 excluded. Permutation p-values from {n_perm} random re-assignments "
        "of treatment among control municipalities; pre-trend p from the same "
        "distribution of the sum of squared 2006-2009 event-study coefficients. "
        "Excess deaths are implied by the estimate applied to observed deaths."),
    "tab_lnt": (
        "Table 3. Measured and projected mortality associated with the "
        "Fukushima Daiichi accident. Measured quantities are from this paper's "
        "estimates or official counts; projected quantities are LNT-based "
        "assessments, quoted from the cited source."),
    "tab_kansas": (
        "Table 4. Synthetic-control estimates for Kansas, 2013-2017 mean gap "
        "relative to synthetic Kansas. Permutation p is the rank of the Kansas "
        "post/pre RMSPE ratio among all donors. In-time placebo assigns a "
        "pseudo-treatment in 2005 and reports the 2005-2012 mean gap."),
    "tab_a1": (
        "Table A1. Municipalities excluded from the estimation sample, by "
        "prefecture and reason."),
    "tab_a2": (
        "Table A2. Municipality-level synthetic controls for the ten T1 "
        "municipalities: donors, pre- and post-period RMSPE, 2012-2019 mean gap, "
        "and permutation p."),
    "fig_a1": (
        "Figure A1. Difference-in-differences event studies for Kansas versus "
        "the four neighbouring states, reference year 2012, for the four "
        "outcomes."),
}

# Equations (OMML built by build_manuscript.py from these linear forms) -------
EQUATIONS = {
    "eq_did": "ln(CDR_it) = a_i + g_t + b D_it + e_it",
}

# References (APA 7, author-date). Existence verified via Crossref/URL in build.
REFERENCES = [
    "Abadie, A. (2021). Using synthetic controls: Feasibility, data requirements, and methodological aspects. Journal of Economic Literature, 59(2), 391-425. https://doi.org/10.1257/jel.20191450",
    "Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies: Estimating the effect of California's tobacco control program. Journal of the American Statistical Association, 105(490), 493-505. https://doi.org/10.1198/jasa.2009.ap08746",
    "Bertrand, M., Duflo, E., & Mullainathan, S. (2004). How much should we trust differences-in-differences estimates? Quarterly Journal of Economics, 119(1), 249-275. https://doi.org/10.1162/003355304772839588",
    "Brenner, D. J., Doll, R., Goodhead, D. T., Hall, E. J., Land, C. E., Little, J. B., Lubin, J. H., Preston, D. L., Preston, R. J., Puskin, J. S., Ron, E., Sachs, R. K., Samet, J. M., Setlow, R. B., & Zaider, M. (2003). Cancer risks attributable to low doses of ionizing radiation: Assessing what we really know. Proceedings of the National Academy of Sciences, 100(24), 13761-13766. https://doi.org/10.1073/pnas.2235592100",
    "Burnham, K. P., & Anderson, D. R. (2004). Multimodel inference: Understanding AIC and BIC in model selection. Sociological Methods & Research, 33(2), 261-304. https://doi.org/10.1177/0049124104268644",
    "Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. Review of Economics and Statistics, 90(3), 414-427. https://doi.org/10.1162/rest.90.3.414",
    "Cartwright, N., & Hardie, J. (2012). Evidence-based policy: A practical guide to doing it better. Oxford University Press.",
    "Conley, T. G., & Taber, C. R. (2011). Inference with \"difference in differences\" with a small number of policy changes. Review of Economics and Statistics, 93(1), 113-125. https://doi.org/10.1162/REST_a_00049",
    "Cook, R. D. (1977). Detection of influential observation in linear regression. Technometrics, 19(1), 15-18. https://doi.org/10.1080/00401706.1977.10489493",
    "Fukushima Prefecture. ({fdr_year}). Heisei 23 Tohoku Chiho Taiheiyo-oki Jishin ni yoru Higai Jokyo Sokuho (No. {fdr_no}) [Damage situation bulletin on the 2011 Tohoku Pacific Coast earthquake, No. {fdr_no}]. {fdr_url}",
    "Hasegawa, A., Tanigawa, K., Ohtsuru, A., Yabe, H., Maeda, M., Shigemura, J., Ohira, T., Tominaga, T., Akashi, M., Hirohashi, N., Ishikawa, T., Kamiya, K., Shibuya, K., Yamashita, S., & Chhem, R. K. (2015). Health effects of radiation and other health problems in the aftermath of nuclear accidents, with an emphasis on Fukushima. The Lancet, 386(9992), 479-488. https://doi.org/10.1016/S0140-6736(15)61106-0",
    "ICRP. (2007). The 2007 recommendations of the International Commission on Radiological Protection. ICRP Publication 103. Annals of the ICRP, 37(2-4). https://doi.org/10.1016/j.icrp.2007.10.003",
    "Kansas Legislature. (2012). House Bill No. 2117, enrolled. 2012 Session Laws of Kansas, Chapter 135. https://kslegislature.org/li_2012/b2011_12/measures/documents/hb2117_enrolled.pdf",
    "Rothschild, S. (2012, January 19). Consultant Laffer praises Brownback's tax plan. Lawrence Journal-World. https://www2.ljworld.com/news/2012/jan/19/consultant-laffer-touts-brownbacks-tax-plan/",
    "Laffer, A. B. (2004). The Laffer curve: Past, present, and future (Backgrounder No. 1765). The Heritage Foundation.",
    "Murakami, M., Ono, K., Tsubokura, M., Nomura, S., Oikawa, T., Oka, T., Kami, M., & Oki, T. (2015). Was the risk from nursing-home evacuation after the Fukushima accident higher than the radiation risk? PLoS ONE, 10(9), e0137906. https://doi.org/10.1371/journal.pone.0137906",
    "Ozasa, K., Shimizu, Y., Suyama, A., Kasagi, F., Soda, M., Grant, E. J., Sakata, R., Sugiyama, H., & Kodama, K. (2012). Studies of the mortality of atomic bomb survivors, Report 14, 1950-2003: An overview of cancer and noncancer diseases. Radiation Research, 177(3), 229-243. https://doi.org/10.1667/RR2629.1",
    "Nomura, S., Gilmour, S., Tsubokura, M., Yoneoka, D., Sugimoto, A., Oikawa, T., Kami, M., & Shibuya, K. (2013). Mortality risk amongst nursing home residents evacuated after the Fukushima nuclear accident: A retrospective cohort study. PLoS ONE, 8(3), e60192. https://doi.org/10.1371/journal.pone.0060192",
    "Reconstruction Agency. ({ra_year}). Number of disaster-related deaths from the Great East Japan Earthquake [in Japanese]. {ra_url}",
    "Rickman, D. S., & Wang, H. (2018). Two tales of two U.S. states: Regional fiscal austerity and economic performance. Regional Science and Urban Economics, 68, 46-55. https://doi.org/10.1016/j.regsciurbeco.2017.10.008",
    "ten Hoeve, J. E., & Jacobson, M. Z. (2012). Worldwide health effects of the Fukushima Daiichi nuclear accident. Energy & Environmental Science, 5(9), 8743-8757. https://doi.org/10.1039/c2ee22019a",
    "UNSCEAR. (2014). Sources, effects and risks of ionizing radiation: UNSCEAR 2013 report to the General Assembly, Volume I, Scientific Annex A. United Nations. https://www.unscear.org/unscear/uploads/documents/unscear-reports/UNSCEAR_2013_Report_Vol.I.pdf",
    "Wanniski, J. (1978). Taxes, revenues, and the \"Laffer curve\". The Public Interest, 50, 3-16.",
    "WHO. (2013). Health risk assessment from the nuclear accident after the 2011 Great East Japan earthquake and tsunami, based on a preliminary dose estimation. World Health Organization. ISBN 9789241505130. https://iris.who.int/server/api/core/bitstreams/3cc74066-fdcf-46ed-8e94-e2c7bc6e7eae/content",
    "Yasumura, S., Goto, A., Yamazaki, S., & Reich, M. R. (2013). Excess mortality among relocated institutionalized elderly after the Fukushima nuclear disaster. Public Health, 127(2), 186-188. https://doi.org/10.1016/j.puhe.2012.10.019",
]

APPENDIX = [
    ("h1", "Appendix"),
    ("table", "tab_a1"),
    ("table", "tab_a2"),
    ("fig", "fig_a1"),
]
