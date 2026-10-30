"""Evidence & Policy (Bristol University Press) manuscript text.

Evidence-to-policy translation rewrite of the functional-form dependence
manuscript. Numerical fields are populated by build_manuscript.py from
analysis outputs (numbers.json). No analytical result is changed here.
"""

TITLE = (
    "When Evidence Is Not Specific Enough for Policy: Functional-Form "
    "Dependence in Evidence-Based Decision-Making"
)

ABSTRACT = (
    "Introduction: Evidence-based policy is usually appraised in terms of "
    "whether research is credible, relevant, and used. Yet many decisions "
    "require something more specific than an association: a threshold, a "
    "local slope, a turning point, or an extrapolated response. This "
    "article asks how evidence adequate for establishing an association "
    "can become inadequate when translated into a decision requiring a "
    "more specific functional form. Methods/Data: A purposive mapping of "
    "{n_curves} named nonlinear relationships was screened with one "
    "transparent diagnostic, and two public-data applications follow the "
    "translation chain: post-Fukushima evacuation ({n_t1} evacuated "
    "municipalities) and the 2012 Kansas tax reform. Analytic plan: Each "
    "application reconstructs how evidence was interpreted into a "
    "policy-relevant shape, identifies the functional feature the decision "
    "required, and assesses whether evidence identified that feature in "
    "the policy-relevant range, using difference-in-differences and "
    "synthetic-control analyses. Results: {n_not_robust} of {n_curves} "
    "pairs failed the study's robust-nonlinear criteria, and in both "
    "applications the required functional feature was identified less "
    "securely than the policy assumed. Conclusion/Implications: "
    "Functional-form dependence names this evidence-to-policy mismatch; "
    "an appraisal checklist is derived for policymakers, practitioners, "
    "and knowledge brokers."
)

KEYWORDS = (
    "evidence use; functional form; evidence-based policymaking; uncertainty"
)

AI_ASSISTANCE_HEADING = "Artificial intelligence assistance"

AI_ASSISTANCE_TEXT = (
    "An AI coding assistant (Devin, Cognition AI) was used to assist with data-acquisition, "
    "analysis, and document-generation code and with manuscript drafting and editing under "
    "the author's direction. The author specified the research questions and analytical "
    "choices, verified the data sources and results, evaluated all interpretations, and "
    "takes full responsibility for the manuscript."
)

BODY = [
    ("h1", "Background"),
    (
        "p",
        "Evidence-based policy is most often appraised in terms of whether "
        "research is credible, relevant to the decision at hand, and "
        "actually used. Yet many policy decisions require something more "
        "specific than a claim that one variable affects another. An "
        "evacuation order requires a statement about how harm declines "
        "with exposure. A tax reform is defended on how revenue and "
        "activity respond to rates. In each case, the decision needs a "
        "particular feature of an empirical relationship - a threshold, a "
        "local slope, a turning point, a curvature, or an extrapolated "
        "segment - to hold over the range where the policy operates.",
    ),
    (
        "p",
        "A study can therefore be rigorous for what it directly estimates "
        "while remaining insufficient for the use made of it. A credible "
        "estimate of an average difference, an association, or a local "
        "effect does not by itself identify the shape a decision needs. "
        "This article calls the resulting condition functional-form "
        "dependence: a policy recommendation materially depends on a "
        "threshold, slope, turning point, curvature, or extrapolated "
        "response that is less securely identified than the policy use of "
        "that evidence assumes. Functional-form uncertainty is a "
        "component of model uncertainty about relationship shape (Draper, "
        "1995; Morgan and Henrion, 1990); functional-form dependence is "
        "the evidence-use condition in which that uncertainty enters the "
        "policy decision rule.",
    ),
    (
        "p",
        "The problem sits within, rather than outside, the evidence-use "
        "literature. Research on evidence-informed policymaking stresses "
        "that evidence is filtered through institutions, routines, and "
        "professional practices that can privilege a familiar picture "
        "over a fragile empirical claim (Cairney, 2016; Parkhurst, 2016; "
        "Boswell, 2009). Reviews of barriers to research use emphasise "
        "relevance, accessibility, timing, and contested interpretations "
        "of what counts as evidence (Oliver et al., 2014; Nutley et al., "
        "2007), while work on transportability asks when findings "
        "established in one setting can support inferences about another "
        "(Cartwright and Hardie, 2012). Less attended to is a distinct "
        "level of mismatch: not whether evidence exists or is used, but "
        "whether the decision demands more decision-relevant specificity "
        "from the evidence than the evidence can deliver - what might be "
        "called an evidence-specificity gap.",
    ),
    (
        "p",
        "This article asks: how can evidence that is adequate for "
        "establishing an association become inadequate when translated "
        "into a policy decision requiring a more specific functional "
        "form, and under what conditions does that gap become "
        "consequential for policy design? It answers empirically in two "
        "stages. First, a purposive mapping applies one transparent "
        "nonlinear diagnostic to {n_curves} named canonical relationships "
        "across fields, showing that familiar scientific relationships "
        "may be used at a level of functional-form specificity that "
        "exceeds what a common diagnostic can establish. Second, two "
        "deliberately dissimilar policy applications - post-Fukushima "
        "evacuation and the 2012 Kansas tax reform - follow the "
        "translation chain from evidence to assumed shape to decision to "
        "consequences, in settings that share no dataset, institution, or "
        "evidentiary tradition. Figure 1 summarises the analytical "
        "sequence.",
    ),
    ("fig", "fig_policy_pathway"),
    (
        "p",
        "The article makes three contributions. It identifies a specific "
        "evidence-to-policy mismatch that is distinct from the more "
        "studied problems of credibility, relevance, and uptake. It "
        "demonstrates the mismatch empirically across two unrelated "
        "policy domains, which is evidence that the problem is not an "
        "artefact of one field. And it derives a practical appraisal "
        "checklist for policymakers, practitioners, and knowledge brokers "
        "to use before uncertain functional form becomes embedded in "
        "policy.",
    ),
    ("h1", "Methods"),
    ("h2", "Study design"),
    (
        "p",
        "The study is a cross-domain evidence-use analysis with two "
        "policy applications. The unit of analysis is the translation "
        "chain connecting an empirical relationship to a policy decision: "
        "the evidence available, the functional feature the decision "
        "required, the interpretation that bridged them, and the "
        "consequences that lay outside the original relationship. "
        "Fukushima and Kansas were selected because they maximise "
        "substantive contrast - different sectors, scientific traditions, "
        "institutional environments, temporal dynamics, and consequences "
        "of error - while exposing the same evidence-use problem. Finding "
        "the problem in two such different settings supports the claim "
        "that it is domain-general; the design does not support "
        "prevalence estimation, causal inference about all policies that "
        "use nonlinear models, or statistical generalisation.",
    ),
    (
        "p",
        "To establish that the problem class extends beyond the "
        "applications, a purposive inventory of {n_inventory} named "
        "nonlinear relationships was screened with one common diagnostic; "
        "two pairs lacking a reproducible dataset were excluded, leaving "
        "{n_curves}. Each relationship-dataset pair was evaluated against "
        "a linear baseline with a quadratic alternative, requiring a "
        "nested F-test at alpha = {alpha_default}, robustness to removal "
        "of the {k_default} most influential observations, leave-one-out "
        "predictive improvement, and BIC preference (Cook, 1977; Burnham "
        "and Anderson, 2004). Supplement Figure S1 shows the decision "
        "sequence.",
    ),
    ("h2", "Data in the applications"),
    (
        "p",
        "For Fukushima, annual municipal deaths and resident-register "
        "populations were assembled for {n_all_units} municipalities from "
        "the Japanese government's official-statistics portal (Ministry "
        "of Health, Labour and Welfare, 2021; Ministry of Internal "
        "Affairs and Communications, 2021). The primary treatment group "
        "(T1) contains {n_t1} municipalities subject to mandatory "
        "evacuation orders, with approximately {evac_pop_approx} "
        "residents in 2010; municipalities with tsunami inundation "
        "exceeding {tsunami_cut}% were excluded to reduce direct-tsunami "
        "confounding; missing-data exclusions are reported in Supplement "
        "Table S1. Two-way fixed-effects differences in log crude death "
        "rates were estimated for 2012-2019, with robustness across "
        "control pools, weighting, treatment definitions, permutation "
        "inference, and synthetic controls (Abadie et al., 2010, 2015; "
        "Abadie, 2021; Bertrand et al., 2004); unit-level synthetic-"
        "control results are reported in Supplement Table S2.",
    ),
    (
        "p",
        "For Kansas, a state-year panel covering {ks_pre_years} and "
        "later years supports synthetic-control estimates of real GDP "
        "per capita, nonfarm employment, real total tax revenue per "
        "capita, and real individual income-tax revenue per capita. The "
        "main donor pool excludes states with large contemporaneous rate "
        "changes or without broad income taxes, leaving {ks_n_donors} "
        "donors; permutation tests, leave-one-donor-out checks, in-time "
        "placebos, and neighbouring-state event studies assess "
        "sensitivity (Supplement Figure S2)."
    ),
    (
        "p",
        "The preferred specification estimates two-way fixed-effects "
        "differences in log crude death rates, with municipality and "
        "year effects, excluding 2011 from the post-period average:",
    ),
    ("eq", "ln(CDR_it) = a_i + g_t + b D_it + e_it"),
    (
        "p",
        "Neither analysis claims to identify a universally correct "
        "radiation model or tax schedule, and neither treats a curve as "
        "the sole cause of policy. Emergency evacuation and tax "
        "legislation reflect legal authority, political commitments, and "
        "multiple streams of evidence; the analysis isolates the "
        "functional-form proposition each decision depended on.",
    ),
    ("h1", "Findings"),
    ("h2", "Mapping the evidence-specificity problem"),
    (
        "p",
        "Under the default criteria, {n_not_robust} of {n_curves} "
        "relationship-dataset pairs ({share_not_robust_pct}%) did not "
        "meet the criteria for robust nonlinear identification; the "
        "share ranged from {share_min_pct}% to {share_max_pct}% across "
        "the alpha and influence-removal grid (Figure 2). Table 1 "
        "reports categories by field. For the Laffer dataset the "
        "quadratic term had p = {laffer_p} (n = {laffer_n}); for the "
        "low-dose radiation dataset p = {lnt_p} (n = {lnt_n}), with "
        "{lnt_n_lowdose} observations below 0.1 Gy.",
    ),
    (
        "p",
        "These results are a diagnostic map, not a replication-failure "
        "rate: the mapping is purposive, estimates no prevalence, and "
        "does not falsify any underlying theory. Their evidential "
        "function here is different: they show that familiar scientific "
        "relationships - the kind that circulate in policy debates as "
        "established pictures - may be used at a level of functional-"
        "form specificity that exceeds what a single transparent "
        "diagnostic can establish. The mapping thereby quantifies an "
        "evidence-specificity gap that the two applications then "
        "examine in the settings where it became decision-relevant.",
    ),
    ("fig", "fig_sensitivity"),
    ("table", "tab_audit"),
    ("h2", "Fukushima: translating low-dose evidence into policy"),
    (
        "p",
        "After the March 2011 Fukushima Daiichi accident, Japanese "
        "authorities ordered mandatory evacuations affecting roughly "
        "{evac_pop_approx} residents. The translation chain runs from "
        "radiation-protection evidence, through low-dose dose-response "
        "assumptions - linear no-threshold and related projections of "
        "population risk at doses where direct epidemiological "
        "identification is difficult (ICRP, 2007) - to evacuation "
        "thresholds and orders, and onward to consequences that the "
        "dose-response curve does not represent: displacement, "
        "mortality risk among vulnerable groups, and disrupted care.",
    ),
    (
        "p",
        "The decision required the slope of the dose-response function "
        "in the low-dose range: whether incremental exposure below the "
        "well-observed range carries proportional risk justifying broad "
        "and sustained evacuation. This is an extrapolation problem - "
        "the feature mattered precisely where direct evidence is "
        "weakest. Plausible alternative low-dose shapes - linear, "
        "threshold, hormetic, supralinear - imply materially different "
        "optimal evacuation scope, duration, and priority, so the "
        "decision was decision-sensitive to a feature the evidence "
        "could not sharply identify: functional-form dependence in its "
        "clearest form.",
    ),
    (
        "p",
        "Figure 3 plots pooled crude death rates. T1 municipalities "
        "show a sharp 2011 increase and a lower recorded rate than "
        "Fukushima controls through much of 2012-2019; the preferred "
        "difference-in-differences estimate is {t1_main_att} log "
        "points, approximately {t1_main_att_pct}% fewer recorded deaths "
        "than the counterfactual trend (permutation p "
        "{t1_main_perm_p}; pre-trend p {t1_main_pretrend_p}). Supplement "
        "Table S3 reports the specification grid and Supplement Figure "
        "S3 the preferred event study.",
    ),
    ("fig", "fig_pooled_cdr"),
    (
        "p",
        "The negative post-2011 coefficient is not evidence that "
        "evacuation improved health. Displacement, selective return, "
        "registration practice, and population composition change who "
        "remains in the series and where deaths are recorded - the "
        "post-evacuation curve does not trace a stable population "
        "through exposure levels. The 2011 decomposition is more "
        "informative: T1 municipalities recorded {t1_obs_2011} deaths "
        "against {t1_exp_2011} trend-expected, an excess of "
        "{t1_excess_2011}; direct disaster deaths account for "
        "{t1_direct_2011}, leaving a residual of {t1_resid_2011} "
        "(Supplement Figure S4) that cannot be wholly assigned to "
        "evacuation. Certified disaster-related deaths for Fukushima "
        "Prefecture total {ra_related_deaths} as of {ra_date} "
        "(Reconstruction Agency, {ra_year}; Fukushima Prefecture, "
        "2014). Supplement Table S4 places measured quantities beside "
        "published radiological projections - for example, ten Hoeve "
        "and Jacobson's (2012) best estimate of {thj_best} worldwide "
        "cancer deaths (range {thj_range}) with {thj_averted_best} "
        "averted by evacuation (range {thj_averted_range}), alongside "
        "WHO (2013) and UNSCEAR (2014) quantities that differ in scope "
        "and construction.",
    ),
    (
        "p",
        "The evidence-to-policy lesson is that evidence about "
        "radiation risk was translated into policy at a level of "
        "functional specificity and consequence coverage that the "
        "underlying dose-response evidence alone could not supply. "
        "Error costs were asymmetric on both sides and partly "
        "irreversible, yet the appraisal space was not binary: zoning, "
        "assisted voluntary relocation, exemptions for medically "
        "fragile residents, continuity of care, time-limited orders, "
        "exposure monitoring, and staged return are adjustable design "
        "variables that perform differently across plausible risk "
        "functions. The case does not show that the linear no-threshold "
        "model is false, that evacuation was definitively wrong, or "
        "that non-evacuation outcomes are observed; it shows "
        "functional-form uncertainty under extrapolation combined with "
        "high consequence asymmetry and limited reversibility.",
    ),
    ("h2", "Kansas: translating fiscal-response evidence into policy"),
    (
        "p",
        "In 2012 Kansas enacted large income-tax cuts. The "
        "justification invoked the Laffer curve - the proposition that "
        "revenue eventually declines as rates rise past a maximum "
        "(Laffer, 2004) - and assumed, under expectations about "
        "tax-rate-revenue and growth responses, that behavioural and "
        "growth responses would recover much of the static revenue "
        "loss (Kansas Legislature, 2012; Rothschild, 2012). The "
        "translation chain runs from economic theory and "
        "cross-jurisdiction evidence, through an assumed fiscal-"
        "response shape, to a claim about Kansas's local position on "
        "that shape, to legislation, and to observed fiscal and "
        "economic outcomes.",
    ),
    (
        "p",
        "The decision required the state's local position on the "
        "revenue response, the local slope, and the timing and "
        "magnitude of any dynamic feedback - features that the "
        "existence of a Laffer-type relationship does not identify. "
        "Evidence that such a curve can exist does not locate Kansas "
        "on it, and the mapping exercise found the curve's quadratic "
        "shape statistically fragile even in its canonical dataset "
        "(p = {laffer_p}).",
    ),
    (
        "p",
        "Figure 4 compares Kansas with synthetic Kansas. After the "
        "reform, real individual income-tax revenue per capita "
        "averaged about {ks_iit_pct}% below the main synthetic "
        "counterfactual (permutation p = {ks_iit_perm_p}); the "
        "all-state pool implies {ks_iit_pct_all}%. The gap grew from "
        "roughly ${ks_iit_gap_2013} per capita in 2013 to "
        "${ks_iit_gap_2016} in 2016, a cumulative counterfactual gap "
        "near ${ks_iit_cum_bn} billion in 2012 dollars. Real total tax "
        "revenue was {ks_tax_pct}% lower (p = {ks_tax_perm_p}); "
        "post-reform gaps were {ks_gdp_pct}% for real GDP per capita "
        "(p = {ks_gdp_perm_p}) and {ks_emp_pct}% for employment (p = "
        "{ks_emp_perm_p}). Supplement Table S5 reports donor pools, "
        "pre-period fit, in-time placebos, and leave-one-donor-out "
        "ranges ({ks_iit_loo_min} to {ks_iit_loo_max} log points; "
        "pre-RMSPE {ks_iit_rmspe}), and Supplement Figure S2 the "
        "neighbouring-state event studies.",
    ),
    ("fig", "fig_kansas"),
    (
        "p",
        "The result is not a universal rejection of the Laffer "
        "curve, nor does Kansas disprove supply-side economics. "
        "Within this period and design, no macroeconomic response "
        "large enough to offset the revenue loss is observed. The "
        "evidence-use lesson is that a theoretically possible "
        "response shape was translated into a decision-relevant "
        "claim about local position and slope that the available "
        "evidence did not identify. Unlike Fukushima, however, the "
        "setting was comparatively reversible and observable: "
        "statutory changes are revisable, outcomes are visible on "
        "budget timescales, and staged rate changes, automatic "
        "review triggers, and sunset clauses were feasible learning "
        "architectures. Kansas's 2017 partial repeal illustrates "
        "correction after observation.",
    ),
    ("h2", "Cross-case synthesis: when evidence specificity matters"),
    (
        "p",
        "Both applications required decision-relevant knowledge of "
        "relationship shape that exceeded what the available evidence "
        "established. In each, a named canonical relationship "
        "supplied content - an evacuation threshold, an expected "
        "revenue recovery - that the evidence over the relevant "
        "range did not deliver. The evidence-use mechanism is the "
        "same even though the applications share no dataset, "
        "institution, or political context.",
    ),
    (
        "p",
        "The applications differ in the conditions that determine "
        "whether the specificity gap becomes consequential (Table "
        "2). Fukushima's uncertainty was extrapolative - the "
        "required feature lay below the observed dose range - "
        "whereas Kansas's concerned local position and dynamic "
        "response within a theoretically possible curve. Fukushima "
        "combined severe, two-sided consequence asymmetry with "
        "limited reversibility; Kansas carried primarily fiscal "
        "costs with far greater reversibility and rapid "
        "observability. Three interpretive findings follow, stated "
        "as generalisations rather than statistically tested "
        "hypotheses: functional-form uncertainty becomes policy-"
        "critical when plausible alternative shapes imply "
        "materially different actions - decision sensitivity, not "
        "statistical significance, is the threshold; the decision "
        "cost of functional-form uncertainty rises when "
        "consequences are asymmetric and commitments are difficult "
        "to reverse; and where policies are reversible and "
        "outcomes observable on useful timescales, adaptive "
        "implementation can partially substitute for ex ante "
        "shape certainty (Lempert and Collins, 2007; Walker et "
        "al., 2013).",
    ),
    ("table", "tab_synthesis"),
    ("h1", "Discussion"),
    ("h2", "Principal finding"),
    (
        "p",
        "The principal finding is that the specificity required "
        "by policy can exceed the specificity supported by "
        "evidence. This is an evidence-use problem in its own "
        "right, distinct from the better-studied problems of "
        "whether research is produced, credible, relevant, or "
        "taken up at all: evidence can be produced, credible, "
        "and used, and still be asked to support a more "
        "specific empirical claim than it identifies.",
    ),
    ("h2", "Why study quality is not enough"),
    (
        "p",
        "Appraisal practices concentrated on the quality or "
        "credibility of a study can miss the mismatch entirely. "
        "A rigorous causal estimate can fail to identify a "
        "shape, a threshold, a turning point, or behaviour "
        "outside the observed range, and functional form can "
        "matter even inside strong causal designs (Roth and "
        "Sant'Anna, 2023). Evidence hierarchies rank designs "
        "by internal validity; they say little about whether "
        "the feature a decision requires was ever estimated.",
    ),
    ("h2", "Relevance and transportability"),
    (
        "p",
        "Evidence may be credible yet insufficiently relevant "
        "to the policy-relevant range or context "
        "(Cartwright and Hardie, 2012). In Fukushima the gap "
        "was extrapolative - epidemiological strength at "
        "higher doses could not specify the low-dose slope. "
        "In Kansas it was locational - cross-jurisdiction and "
        "theoretical evidence could not place the state on "
        "the curve. Decomposing transportability by "
        "population, period, institution, and range makes "
        "these different gaps visible instead of a single "
        "judgement about whether evidence applies.",
    ),
    ("h2", "How evidence changes in translation"),
    (
        "p",
        "Named scientific relationships travel well: a curve "
        "summarises a multi-step argument in one portable "
        "picture. The applications show how that portability "
        "inflates claims - a relationship that evidences an "
        "association in the literature is rehearsed in policy "
        "reasoning as a threshold, a slope at a particular "
        "point, or an expected dynamic response, each a "
        "stronger claim than the source evidence licensed. "
        "The translation step is where specificity is gained "
        "on paper and lost in warrant.",
    ),
    ("h2", "Implications for policymakers and practitioners"),
    (
        "p",
        "Before evidence is used to justify policy, seven "
        "questions make the specificity gap visible: (1) what "
        "exactly does the evidence establish; (2) what "
        "specific functional feature does the policy require; "
        "(3) is that feature identified in the policy-"
        "relevant range; (4) is the evidence transportable "
        "to the target setting; (5) would plausible "
        "alternative shapes change the decision; (6) what "
        "are the consequences of acting on the wrong shape; "
        "and (7) can the policy be staged, monitored, or "
        "reversed? The checklist is an evidence-use tool, "
        "not a universal theory; its function is to keep "
        "the level of claim matched to the level of "
        "identification.",
    ),
    ("h2", "Implications for researchers"),
    (
        "p",
        "Researchers can make the specificity gap legible by "
        "distinguishing, in their reporting, between what the "
        "data identify, what model assumptions add, and what "
        "policy users may infer. Where a named relationship "
        "is likely to be translated into a decision, stating "
        "which features are identified in which ranges - and "
        "which are assumed - is itself an evidence-use "
        "contribution.",
    ),
    ("h2", "Implications for knowledge brokers"),
    (
        "p",
        "Intermediaries between research and policy are "
        "positioned to surface exactly this class of "
        "uncertainty (Ward et al., 2009). Brokers can ask "
        "the checklist questions on behalf of evidence "
        "users, flag extrapolation and shape dependence in "
        "summaries, and resist compressing multi-step "
        "arguments into the named curve that travels best.",
    ),
    ("h2", "Limitations"),
    (
        "p",
        "The design has clear limits. Two purposively "
        "selected applications cannot support statistical "
        "generalisation; the reconstruction is "
        "retrospective; the two empirical designs are "
        "heterogeneous; and policymakers' actual "
        "information sets are not fully observed, so the "
        "analysis isolates the functional-form proposition "
        "each decision depended on rather than the whole "
        "of each rationale. The {n_curves}-relationship "
        "mapping is purposive and estimates no prevalence. "
        "Fukushima's municipal mortality is affected by "
        "displacement, registration, demographic change, "
        "and recording location, and non-evacuation "
        "outcomes are unobserved. Kansas's synthetic "
        "control cannot fully separate the reform from "
        "contemporaneous state-specific shocks. The "
        "analysis also stops short of a welfare analysis "
        "placing all consequences on a common scale.",
    ),
    ("h1", "Conclusion"),
    (
        "p",
        "The gap between evidence and policy is not only "
        "about whether research is used; it is also about "
        "whether policy asks the evidence to support a "
        "more specific empirical claim than the evidence "
        "can identify. Functional-form dependence names "
        "that mismatch, and the mapping and applications "
        "show it appearing across unrelated domains. The "
        "governing principle for evidence use follows "
        "directly. Where a decision requires specificity "
        "the evidence lacks, the honest response is to "
        "narrow the claim, stage the commitment, or build "
        "in the capacity to learn. Evidence should not be "
        "translated into a more specific policy claim than "
        "the underlying data can support.",
    ),
    ("h1", "Data availability"),
    (
        "p",
        "All data used in the analyses are from public "
        "sources. Archived source files, acquisition "
        "metadata, processed datasets, analysis code, "
        "machine-readable results, and document-generation "
        "code will be supplied to reviewers through an "
        "anonymised archive. The public repository URL is "
        "provided to the editor in the title-page "
        "materials and will be added to the manuscript "
        "after double-anonymous review. The archive README "
        "records the commands required to reproduce the "
        "analyses and submission files.",
    ),
    ("h1", AI_ASSISTANCE_HEADING),
    ("p", AI_ASSISTANCE_TEXT),
    ("refs", None),
]

CAPTIONS = {
    "fig_policy_pathway": (
        "Figure 1. Evidence-to-policy appraisal sequence for functional-form "
        "dependence. The same analytical sequence is applied to both "
        "applications: the empirical relationship, the assumed functional "
        "form, the policy-relevant range, decision dependence, asymmetric "
        "consequences, and the action architecture. Transportability and "
        "reversibility condition every step."
    ),
    "fig_decision_tree": (
        "Supplement Figure S1. Diagnostic used in the cross-domain mapping "
        "exercise. Green paths continue toward robust nonlinear "
        "classification; orange paths indicate the first unmet criterion. "
        "Insufficient data is assigned when influence removal leaves too few "
        "observations for the nested comparison."
    ),
    "fig_sensitivity": (
        "Figure 2. Share of {n_curves} relationship-dataset pairs not "
        "classified as robustly nonlinear across significance levels and "
        "Cook-distance removal counts. Cell labels report percentages; the "
        "colour scale spans 0-100%."
    ),
    "fig_pooled_cdr": (
        "Figure 3. Pooled crude death rates in Fukushima treatment and "
        "control groups. T1 contains {n_t1} mandatory-evacuation "
        "municipalities; T1w is the restricted complete-evacuation group; "
        "T2 contains comparison municipalities subject to other "
        "evacuation-related classifications. The shaded region is the "
        "2012-2019 average-treatment-effect window."
    ),
    "fig_event_study": (
        "Supplement Figure S3. Preferred T1 event-study estimates using "
        "unweighted Fukushima municipal controls. Points are year-specific "
        "coefficients relative to the omitted reference year; bars are 95% "
        "confidence intervals. The acute disaster year 2011 is shown but "
        "excluded from the 2012-2019 average-treatment-effect window."
    ),
    "fig_acute": (
        "Supplement Figure S4. T1 acute-phase mortality decomposition for "
        "2011. Expected deaths are projected from the pre-disaster "
        "municipal trend; direct disaster deaths are reported by Fukushima "
        "Prefecture; residual excess is the arithmetic difference and is "
        "not assigned to a single cause."
    ),
    "fig_kansas": (
        "Figure 4. Kansas and synthetic Kansas, 1997-2019. Panel (a) "
        "reports log real individual income-tax revenue per capita; panel "
        "(b) reports log GDP per capita. Synthetic controls use the main "
        "{ks_n_donors}-state donor pool. Shading marks 2013-2017, between "
        "implementation and legislative reversal."
    ),
    "fig_a1": (
        "Supplement Figure S2. Kansas neighbouring-state "
        "difference-in-differences event studies for real GDP per capita, "
        "employment, total tax revenue, and individual income-tax revenue. "
        "Coefficients are relative to 2012; bars are 95% confidence "
        "intervals."
    ),
    "tab_audit": (
        "Table 1. Cross-domain mapping classifications by category. Counts "
        "describe the purposive relationship-dataset inventory and are not "
        "prevalence estimates for scientific theories or literatures."
    ),
    "tab_fuku_att": (
        "Supplement Table S3. Fukushima difference-in-differences "
        "estimates. ATT is the 2012-2019 average difference in log crude "
        "death rates; 2011 is excluded. Permutation p values use {n_perm} "
        "assignments. Implied deaths are descriptive transformations of "
        "recorded municipal deaths and are not causal death counts."
    ),
    "tab_lnt": (
        "Supplement Table S4. Fukushima measured mortality quantities and "
        "published radiological-risk projections. Rows differ in "
        "population, geography, time horizon, measurement, and model "
        "basis and must not be added or interpreted as commensurate "
        "estimands."
    ),
    "tab_kansas": (
        "Supplement Table S5. Kansas synthetic-control estimates by "
        "outcome and donor pool. Mean gaps cover 2013-2017. Permutation p "
        "values compare Kansas with donor-state placebo gaps; LOO denotes "
        "leave-one-donor-out sensitivity."
    ),
    "tab_synthesis": (
        "Table 2. Cross-case synthesis of the two applications across the "
        "evidence-to-policy dimensions. The applications are not "
        "statistically comparable."
    ),
    "tab_a1": (
        "Supplement Table S1. Municipalities excluded from the Fukushima "
        "panel because of missing mortality or population observations. "
        "Exclusions are determined before outcome estimation."
    ),
    "tab_a2": (
        "Supplement Table S2. Unit-level Fukushima synthetic-control "
        "results for T1 municipalities. Mean gaps cover 2012-2019; "
        "permutation p values compare treated and placebo-unit gaps."
    ),
}

REFERENCES = [
    (
        "Abadie, A, 2021, Using synthetic controls: Feasibility, data "
        "requirements, and methodological aspects, Journal of Economic "
        "Literature 59, 2, 391-425, https://doi.org/10.1257/jel.20191450"
    ),
    (
        "Abadie, A, Diamond, A, and Hainmueller, J, 2010, Synthetic "
        "control methods for comparative case studies: Estimating the "
        "effect of California's tobacco control program, Journal of the "
        "American Statistical Association 105, 490, 493-505, "
        "https://doi.org/10.1198/jasa.2009.ap08746"
    ),
    (
        "Abadie, A, Diamond, A, and Hainmueller, J, 2015, Comparative "
        "politics and the synthetic control method, American Journal of "
        "Political Science 59, 2, 495-510, "
        "https://doi.org/10.1111/ajps.12116"
    ),
    (
        "Bertrand, M, Duflo, E, and Mullainathan, S, 2004, How much "
        "should we trust differences-in-differences estimates?, "
        "Quarterly Journal of Economics 119, 1, 249-275, "
        "https://doi.org/10.1162/003355304772839588"
    ),
    (
        "Boswell, C, 2009, The political uses of expert knowledge: "
        "Immigration policy and social research, Cambridge: Cambridge "
        "University Press"
    ),
    (
        "Burnham, K P, and Anderson, D R, 2004, Multimodel inference: "
        "Understanding AIC and BIC in model selection, Sociological "
        "Methods & Research 33, 2, 261-304, "
        "https://doi.org/10.1177/0049124104268644"
    ),
    (
        "Cairney, P, 2016, The politics of evidence-based policymaking, "
        "London: Palgrave Macmillan, "
        "https://doi.org/10.1057/978-1-137-51781-4"
    ),
    (
        "Cartwright, N, and Hardie, J, 2012, Evidence-based policy: A "
        "practical guide to doing it better, Oxford: Oxford University "
        "Press"
    ),
    (
        "Cook, R D, 1977, Detection of influential observation in "
        "linear regression, Technometrics 19, 1, 15-18, "
        "https://doi.org/10.1080/00401706.1977.10489493"
    ),
    (
        "Draper, D, 1995, Assessment and propagation of model "
        "uncertainty, Journal of the Royal Statistical Society: Series "
        "B 57, 1, 45-70, "
        "https://doi.org/10.1111/j.2517-6161.1995.tb02015.x"
    ),
    (
        "Fukushima Prefecture, 2014, Higashinihon daishinsai ni yoru "
        "higai jokyo sokuhou (dai 1260-ho) [Preliminary report on "
        "damage caused by the Great East Japan Earthquake (Report No. "
        "{fdr_no})], {fdr_url}"
    ),
    (
        "International Commission on Radiological Protection, 2007, "
        "The 2007 recommendations of the International Commission on "
        "Radiological Protection, ICRP Publication 103, Annals of the "
        "ICRP 37, 2-4, https://doi.org/10.1016/j.icrp.2007.10.003"
    ),
    (
        "Kansas Legislature, 2012, House Bill 2117, enrolled, "
        "https://www.kslegislature.gov/li_2012/b2011_12/measures/"
        "documents/hb2117_enrolled.pdf"
    ),
    (
        "Laffer, A B, 2004, The Laffer curve: Past, present, and "
        "future, Heritage Foundation Backgrounder 1765, 1-16, "
        "https://www.heritage.org/taxes/report/the-laffer-curve-past-"
        "present-and-future"
    ),
    (
        "Lempert, R J, and Collins, M T, 2007, Managing the risk of "
        "uncertain threshold responses: Comparison of robust, "
        "optimum, and precautionary approaches, Risk Analysis 27, 4, "
        "1009-1026, https://doi.org/10.1111/j.1539-6924.2007.00940.x"
    ),
    (
        "Ministry of Health, Labour and Welfare, 2021, Vital "
        "statistics of Japan [Data set], Portal Site of Official "
        "Statistics of Japan, https://www.e-stat.go.jp/en/stat-search/"
        "database?page=1&toukei=00450011"
    ),
    (
        "Ministry of Internal Affairs and Communications, 2021, "
        "Population, demographics, and household counts based on the "
        "Basic Resident Registration [Data set], Portal Site of "
        "Official Statistics of Japan, https://www.e-stat.go.jp/en/"
        "stat-search/files?toukei=00200241"
    ),
    (
        "Morgan, M G, and Henrion, M, 1990, Uncertainty: A guide to "
        "dealing with uncertainty in quantitative risk and policy "
        "analysis, Cambridge: Cambridge University Press"
    ),
    (
        "Nutley, S, Walter, I, and Davies, H T O, 2007, Using "
        "evidence: How research can inform public services, Bristol: "
        "Policy Press"
    ),
    (
        "Oliver, K, Innvar, S, Lorenc, T, Woodman, J, and Thomas, J, "
        "2014, A systematic review of barriers to and facilitators of "
        "the use of evidence by policymakers, BMC Health Services "
        "Research 14, 2, https://doi.org/10.1186/1472-6963-14-2"
    ),
    (
        "Parkhurst, J O, 2016, Appeals to evidence for the "
        "resolution of wicked problems: The origins and mechanisms "
        "of evidentiary bias, Policy Sciences 49, 4, 373-393, "
        "https://doi.org/10.1007/s11077-016-9263-z"
    ),
    (
        "Reconstruction Agency, {ra_year}, Higashinihon daishinsai "
        "ni okeru shinsai-kanrenshi no shisha-su [Number of "
        "disaster-related deaths in the Great East Japan Earthquake] "
        "(as of {ra_date}), {ra_url}"
    ),
    (
        "Roth, J, and Sant'Anna, P H C, 2023, When is parallel "
        "trends sensitive to functional form?, Econometrica 91, 2, "
        "737-747, https://doi.org/10.3982/ECTA19402"
    ),
    (
        "Rothschild, S, 2012, Consultant Laffer praises Brownback's "
        "tax plan, Lawrence Journal-World, 19 January, "
        "https://www2.ljworld.com/news/2012/jan/19/consultant-laffer-"
        "touts-brownbacks-tax-plan/"
    ),
    (
        "ten Hoeve, J E, and Jacobson, M Z, 2012, Worldwide health "
        "effects of the Fukushima Daiichi nuclear accident, Energy & "
        "Environmental Science 5, 9, 8743-8757, "
        "https://doi.org/10.1039/C2EE22019A"
    ),
    (
        "United Nations Scientific Committee on the Effects of "
        "Atomic Radiation, 2014, Sources, effects and risks of "
        "ionizing radiation: UNSCEAR 2013 report, Volume I, "
        "Scientific Annex A, New York: United Nations, "
        "https://www.unscear.org/unscear/uploads/documents/unscear-"
        "reports/UNSCEAR_2013_Report_Vol.I.pdf"
    ),
    (
        "Walker, W E, Haasnoot, M, and Kwakkel, J H, 2013, Adapt or "
        "perish: A review of planning approaches for adaptation "
        "under deep uncertainty, Sustainability 5, 3, 955-979, "
        "https://doi.org/10.3390/su5030955"
    ),
    (
        "Ward, V, House, A, and Hamer, S, 2009, Knowledge "
        "brokering: The missing link in the evidence to action "
        "chain?, Evidence & Policy 5, 3, 267-279, "
        "https://doi.org/10.1332/174426409X463811"
    ),
    (
        "World Health Organization, 2013, Health risk assessment "
        "from the nuclear accident after the 2011 Great East Japan "
        "Earthquake and Tsunami, based on a preliminary dose "
        "estimation, Geneva: World Health Organization, "
        "https://iris.who.int/handle/10665/78218"
    ),
]

APPENDIX = [
    (
        "h1",
        "Online supplement: additional analyses, robustness results, and exclusions",
    ),
    ("fig", "fig_decision_tree"),
    ("fig", "fig_event_study"),
    ("fig", "fig_acute"),
    ("fig", "fig_a1"),
    ("table", "tab_fuku_att"),
    ("table", "tab_lnt"),
    ("table", "tab_kansas"),
    ("table", "tab_a1"),
    ("table", "tab_a2"),
]
