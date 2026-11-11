"""Policy Sciences manuscript text.

Numerical fields are populated by build_manuscript.py from analysis outputs.
"""

TITLE = (
    "Functional-Form Dependence in Evidence-Based Policymaking: "
    "Mapping Canonical Relationships and Two Policy Demonstrations"
)

ABSTRACT = (
    "Evidence-based policymaking often relies not only on whether two variables are "
    "associated, but also on the assumed shape of their relationship. Thresholds, "
    "turning points, diminishing returns, and monotonic risk functions can determine "
    "whether a policy is adopted, how intensive it is, and which consequences count "
    "as acceptable. We define functional-form dependence as a condition in which a "
    "policy's justification, expected benefit, threshold, direction, or intensity "
    "materially depends on a relationship shape that is insufficiently identified over "
    "the policy-relevant range. We develop a decision-facing appraisal framework that "
    "separates "
    "association, shape identification, range validity, decision dependence, consequence "
    "asymmetry, and reversibility. A cross-domain mapping exercise then applies one "
    "transparent quadratic diagnostic to {n_curves} canonical relationships. Under this "
    "deliberately common diagnostic, {n_not_robust} of {n_curves} relationship-dataset "
    "pairs ({share_not_robust_pct}%) did not meet the study's criteria for robust "
    "nonlinear identification, with a sensitivity range of "
    "{share_min_pct}-{share_max_pct}%. "
    "Two contrasting demonstrations then examine policies linked to assumed shapes: "
    "post-Fukushima evacuation under low-dose radiation-risk assumptions and the Kansas "
    "tax reform associated with claims about tax-rate and revenue or growth responses. "
    "Neither demonstration identifies a single correct policy. Instead, each shows why "
    "policy appraisal should test the specific shape and range on which a decision "
    "depends, compare plausible alternatives, and account for asymmetric consequences. "
    "The proposed appraisal complements causal evaluation by making model-form "
    "conditionality explicit before policy commitments become difficult to reverse."
)

KEYWORDS = (
    "evidence-based policymaking; functional form; model uncertainty; "
    "policy appraisal; robust policy design"
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
    ("h1", "Introduction"),
    (
        "p",
        "Many policy arguments depend on the shape of an empirical relationship. A "
        "threshold can trigger regulation, a U-shaped curve can identify an optimal "
        "interior level, diminishing returns can determine spending priorities, and a "
        "monotonic dose-response function can justify action even where direct evidence "
        "is sparse. These are stronger claims than the claim that two variables are "
        "associated. They specify how an outcome changes across values of an exposure, "
        "including where the direction, slope, or curvature changes. When a policy uses "
        "that shape to select a threshold, intensity, target group, or expected benefit, "
        "the functional form becomes part of the policy's evidentiary infrastructure.",
    ),
    (
        "p",
        "The evidence-based policy literature has long shown that evidence does not enter "
        "policy as a neutral input. Its meaning is shaped by institutions, problem frames, "
        "values, and practices of use (Head, 2008; Wesselink et al., 2014; Capano & "
        "Malandrino, 2022). Technical evidence can also narrow attention or be used beyond "
        "the conditions under which it is informative (Parkhurst, 2016). Models add a "
        "further layer: acceptance depends not only on technical properties but also on "
        "supporting infrastructure and organizational conditions (Kolkman et al., 2016). "
        "Yet appraisal often concentrates on the credibility of an estimate or causal "
        "design while leaving a prior question implicit: is the relationship shape needed "
        "by the decision actually identified where the policy will operate? This omission "
        "can reinforce established policy frames even when appraisal reveals a mismatch "
        "between objectives and consequences (Dunlop, 2010).",
    ),
    (
        "p",
        "Model uncertainty is the broader category. Functional-form uncertainty concerns "
        "the shape of a relationship, including thresholds, turning points, curvature, "
        "and extrapolation, while model-form uncertainty can also encompass other choices "
        "about the mathematical structure used to represent a process (Draper, 1995). "
        "Functional-form dependence is the decision-level condition in which that shape "
        "uncertainty materially changes a recommended action, threshold, expected benefit, "
        "or policy intensity. External-validity and transportability concerns ask whether "
        "evidence carries across populations, periods, institutions, and exposure ranges "
        "(Cartwright & Hardie, 2012). Extrapolation concerns the use of a relationship "
        "outside observed support. Functional-form sensitivity also appears in causal "
        "methods when identifying assumptions depend on outcome transformations (Roth & "
        "Sant'Anna, 2023). The policy problem examined here arises when one of these "
        "uncertainties reaches the decision rule: a materially different plausible shape "
        "would imply a different action, threshold, expected benefit, or distribution of "
        "consequences.",
    ),
    (
        "p",
        "Canonical relationships are especially consequential because they compress a "
        "multi-stage argument into a familiar picture. An inverted U suggests an optimum; "
        "a threshold suggests a boundary between acceptable and unacceptable exposure; a "
        "monotone curve suggests that more or less of an instrument will move an outcome "
        "in a predictable direction. The picture can therefore travel farther than the "
        "data, design, and scope conditions from which it originated. Once embedded in "
        "guidance, cost-benefit analysis, forecasting, or public communication, the curve "
        "may function as a decision premise even when its location, curvature, or relevant "
        "range was not estimated for the population facing the policy.",
    ),
    (
        "p",
        "The resulting problem cannot be resolved by asking only whether an estimate is "
        "statistically significant or a model fits historical observations. Significance "
        "addresses sampling uncertainty conditional on a specification; fit summarizes "
        "performance over observed data; neither establishes that the assumed shape is "
        "the one on which a decision may safely rely. Conversely, shape uncertainty need "
        "not invalidate action. If all credible shapes recommend the same action over the "
        "policy-relevant range, the decision is robust even though the scientific model "
        "remains uncertain. The policy question is therefore comparative: which shape "
        "alternatives remain plausible, and do they imply materially different actions or "
        "distributions of harm?",
    ),
    (
        "p",
        "We use functional-form dependence in this decision-facing sense: it occurs when "
        "the justification, expected benefit, threshold, direction, or intensity of a "
        "policy materially depends on an assumed relationship shape whose form is "
        "insufficiently identified over the range relevant to the policy decision. This "
        "definition does not require the assumed curve to be false. Nor does it imply that "
        "every policy should wait for definitive estimation. It identifies a condition "
        "that should change appraisal: analysts should expose the shape assumption, "
        "evaluate it over the relevant range, and examine decisions under plausible "
        "alternatives rather than presenting a single curve as settled evidence.",
    ),
    (
        "p",
        "Five questions operationalize the concept. First, is the relationship's shape "
        "identified over the policy-relevant range, rather than merely somewhere in the "
        "data? Second, would a plausible alternative shape change the recommended action? "
        "Third, are the consequences of acting under a wrong shape asymmetric across "
        "groups or outcomes? Fourth, is the relationship transported across population, "
        "period, institutional setting, and exposure range? Fifth, can the policy be "
        "reversed cheaply, staged, piloted, or adapted as evidence accumulates? These "
        "questions connect evidentiary appraisal to robust policy design, which values "
        "performance across uncertain conditions rather than optimization under one "
        "favored model (Lempert & Collins, 2007; Capano & Woo, 2017).",
    ),
    (
        "p",
        "The article makes four contributions. Conceptually, it separates evidence for an "
        "association from evidence for the shape required by a policy. Empirically, it "
        "maps functional-form identification across a non-probability sample of canonical "
        "relationships using a common transparent diagnostic. Analytically, it uses two "
        "contrasting demonstrations - Fukushima evacuation and Kansas tax reform - to "
        "show how risk and fiscal policies can depend on shapes at different stages of the "
        "policy process. Practically, it proposes a decision-facing appraisal framework "
        "that combines shape identification, decision sensitivity, consequence asymmetry, "
        "transportability, and reversibility. The mapping exercise motivates the problem; "
        "the demonstrations clarify its policy significance.",
    ),
    (
        "p",
        "The proposed concept is an organizing contribution rather than a claim that "
        "functional-form sensitivity is newly discovered. Econometrics, risk analysis, "
        "model-uncertainty research, and robust decision approaches already examine parts "
        "of the problem. Functional-form dependence links those parts to the policy "
        "argument itself. It asks when a disputed shape is not merely a technical modeling "
        "choice but a load-bearing premise connecting evidence to authority, resource "
        "allocation, exposure limits, or the scale and timing of intervention. That shift "
        "makes it possible to distinguish scientific uncertainty that is decision-"
        "irrelevant from uncertainty that should change policy design.",
    ),
    ("h1", "Analytical framework and methods"),
    ("h2", "From association to decision dependence"),
    (
        "p",
        "The decision-facing appraisal framework distinguishes linked layers from empirical "
        "association through policy commitment. Association existence asks whether an "
        "exposure and outcome covary. Functional-form identification asks which shapes "
        "remain compatible with the evidence. Policy-relevant-range identification asks "
        "whether those shapes are distinguished within the values to which the policy "
        "applies. Decision dependence asks whether choosing among those shapes changes the "
        "policy recommendation. Consequence asymmetry asks who bears the losses if the "
        "chosen shape is wrong. Transportability and reversibility determine how much "
        "confidence and commitment the decision requires. A relationship may be real "
        "while its turning point is unidentified; its turning point may be identified in "
        "one population but not transportable; or uncertainty may remain substantial but "
        "matter little because the same reversible action performs adequately under all "
        "plausible shapes.",
    ),
    (
        "p",
        "Association existence and shape identification are separated because evidence can "
        "be strong at one layer and weak at another. A randomized or quasi-experimental "
        "contrast may establish that a policy instrument changed an outcome between two "
        "observed levels while leaving the response between, below, or above those levels "
        "unknown. A large observational sample may estimate a smooth curve precisely while "
        "leaving confounding unresolved. A mechanistic model may justify monotonicity while "
        "providing little information about the slope at low exposure. Treating these "
        "claims as interchangeable encourages evidence from one layer to be used as if it "
        "identified the others.",
    ),
    (
        "p",
        "The policy-relevant range is the subset of values that the contemplated action can "
        "reasonably produce or regulate. It should be specified from the decision problem "
        "before model comparison, not selected after viewing where a preferred curve fits "
        "best. The range may be defined by an exposure standard, a feasible tax-rate "
        "change, a program dosage, or the characteristics of eligible populations. "
        "Uncertainty outside that interval can be immaterial, while uncertainty within a "
        "narrow interval can be decisive. This local emphasis also prevents abundant data "
        "at irrelevant values from creating false confidence about a sparsely supported "
        "policy margin.",
    ),
    (
        "p",
        "Decision dependence requires an explicit bridge from model output to action. Let "
        "the candidate set include shapes that remain scientifically credible after "
        "diagnostic testing and substantive review. The policy is functionally dependent "
        "when applying the stated decision rule to that set yields materially different "
        "thresholds, target groups, intervention intensities, rankings, or expected net "
        "benefits. Materiality is therefore contextual rather than a universal statistical "
        "cutoff. A small change can matter near a legal boundary or when many people are "
        "affected; a statistically large difference can be irrelevant if every model "
        "supports the same staged action.",
    ),
    (
        "p",
        "Consequence asymmetry and reversibility turn diagnosis into policy design. A false "
        "negative and a false positive need not impose comparable losses, and those losses "
        "may fall on different groups. Analysts can characterize plausible consequences, "
        "but the weights attached to mortality, displacement, revenue, distribution, "
        "rights, or institutional trust are normative and should not be hidden inside a "
        "single fitted curve. Reversibility changes the value of immediate precision: a "
        "pilot with monitoring and a stopping rule can tolerate more uncertainty than an "
        "irreversible relocation, infrastructure commitment, or statutory entitlement.",
    ),
    (
        "p",
        "This layered view treats model form as a policy variable rather than only a "
        "statistical nuisance. It complements, rather than substitutes for, causal "
        "identification. A well-identified causal effect at one exposure contrast does not "
        "necessarily identify a full response function. Conversely, a well-fitted curve "
        "does not establish that movement along it is causal. Policy appraisal requires "
        "both kinds of discipline when a decision depends on the response shape.",
    ),
    (
        "p",
        "The framework consequently differs from asking which model is globally best. A "
        "model can dominate on an information criterion and still be unsuitable for a "
        "policy that operates near an uncertain turning point. Model averaging can improve "
        "prediction yet conceal that alternative components imply different actions. "
        "Scenario analysis can display alternatives without explaining which assumptions "
        "generate them. Functional-form appraisal uses these tools but evaluates them "
        "against a decision-facing standard: the credible model set, the relevant range, "
        "the action rule, the distribution of error costs, and the option to learn after "
        "implementation.",
    ),
    (
        "p",
        "Figure 1 summarizes the decision-facing appraisal framework. The sections that "
        "follow demonstrate different parts of this architecture: the cross-domain mapping "
        "examines shape identification under a common diagnostic, Fukushima shows how "
        "low-dose extrapolation interacts with asymmetric competing risks, and Kansas "
        "shows why a theoretically possible curve does not identify a policy's local "
        "position, slope, or dynamic response. The cases are substantively heterogeneous "
        "but expose the same policy-analytic issue: a recommendation can depend on a more "
        "specific response shape than the available evidence establishes over the range "
        "where the policy operates.",
    ),
    ("fig", "fig_policy_pathway"),
    ("h2", "Cross-domain mapping exercise"),
    (
        "p",
        "We assembled an inventory of {n_inventory} named relationships commonly presented "
        "as nonlinear curves across economics, psychology, public health, biology, "
        "environmental science, management, and related fields. Two relationships were "
        "excluded because a reproducible dataset suitable for the common diagnostic could "
        "not be obtained, leaving {n_curves}. The unit is a relationship-dataset pair, not "
        "an independent study or a meta-analytic effect. The sample is purposive and "
        "non-probability based. It therefore cannot estimate the prevalence of invalid "
        "theories, failed replications, or policy dependence in any scientific population. "
        "Its role is to show that fragile shape identification can recur across domains "
        "and therefore warrants explicit policy appraisal.",
    ),
    (
        "p",
        "Each relationship was evaluated against a linear baseline using the same "
        "quadratic alternative. A relationship was classified as robustly nonlinear only "
        "if the quadratic term passed a nested F-test at alpha = {alpha_default}, remained "
        "significant after removal of the {k_default} observations with the largest Cook's "
        "distance, improved leave-one-out cross-validation root mean squared error, and "
        "was preferred by the Bayesian information criterion (Cook, 1977; Burnham & "
        "Anderson, 2004). An evidence item could "
        "instead be classified as not significant, outlier dependent, overfitting, "
        "insufficient data after influence removal, or BIC-preferred linear. Figure 2 "
        "shows the implemented decision sequence. This screen tests one simple nonlinear "
        "claim; failure does not establish linearity or rule out thresholds, splines, "
        "piecewise functions, interactions, or mechanistic alternatives.",
    ),
    ("fig", "fig_decision_tree"),
    (
        "p",
        "The common specification is intentionally austere. It makes the classification "
        "rule inspectable and limits domain-specific researcher discretion, but it also "
        "places unlike datasets on a shared statistical screen. Sample sizes, measurement "
        "quality, design strength, and substantive mechanisms differ across entries. We "
        "therefore preserve the diagnostic category rather than collapse all failures into "
        "a claim that a relationship is absent. Not significant indicates inadequate "
        "evidence for the tested curvature; outlier dependent indicates sensitivity to a "
        "small number of influential observations; overfitting indicates weaker "
        "out-of-sample performance; insufficient data indicates that the diagnostic could "
        "not support the classification after influence removal.",
    ),
    (
        "p",
        "We varied alpha over {alpha_grid} and the number of influential observations "
        "removed over k = {k_grid}. These sensitivity checks reveal how much the mapping "
        "depends on reasonable analyst choices. The original data, fitted models, "
        "diagnostics, and classification outputs are retained for each relationship.",
    ),
    (
        "p",
        "This exercise is consequently neither a replication count nor a ranking of fields. "
        "The underlying canonical claims were formulated at different times and may have "
        "been refined, bounded, or abandoned in later work. Some datasets are teaching or "
        "historical evidence rather than the strongest available study. The value of the "
        "map is diagnostic: it illustrates cases in which a recognizable nonlinear "
        "narrative outruns what a particular evidence base identifies. Policy use requires the "
        "next step of locating the decision, the relevant range, and the consequences of "
        "choosing among credible shapes.",
    ),
    ("h2", "Policy demonstrations and inferential scope"),
    (
        "p",
        "The two demonstrations were selected because both policy debates invoked a "
        "canonical shape, both involved consequential and partly irreversible choices, "
        "and both permit transparent post-policy analysis using public data. They are "
        "substantively heterogeneous and contrasting rather than representative cases, "
        "selected to expose the same decision-level dependence in different settings. "
        "Fukushima concerns a risk function "
        "used under emergency conditions, where errors can distribute health risks across "
        "radiation exposure, evacuation, displacement, and disrupted care. Kansas concerns "
        "a fiscal response function, where claims about revenue recovery and growth can "
        "affect budgets and public services. The analyses do not identify a universally "
        "correct radiation model or tax rate. They examine what can and cannot be learned "
        "when policy claims depend on assumed shapes.",
    ),
    (
        "p",
        "The cases are not offered as proof that a single curve mechanically caused either "
        "policy. Emergency evacuation and tax legislation reflect legal authority, "
        "political commitments, administrative capacity, values, and multiple streams of "
        "evidence. The demonstrations instead isolate a load-bearing empirical proposition "
        "within each policy rationale and ask how observed outcomes bear on it. This "
        "limited claim is important: identifying functional-form dependence does not "
        "require a monocausal account of policymaking, only that the assumed shape changes "
        "the justification, expected benefit, or scale of action.",
    ),
    (
        "p",
        "For Fukushima, annual municipal deaths and resident-register populations were "
        "assembled for {n_all_units} municipalities from the Japanese government's "
        "official-statistics portal (Ministry of Health, Labour and Welfare, 2021; "
        "Ministry of Internal Affairs and Communications, 2021). The primary treatment "
        "group (T1) "
        "contains {n_t1} municipalities subject to mandatory evacuation orders, with "
        "approximately {evac_pop_approx} residents in 2010. Municipalities with tsunami "
        "inundation exceeding {tsunami_cut}% were excluded to reduce direct-tsunami "
        "confounding; missing-data exclusions are reported in Appendix Table A1. We "
        "estimated two-way fixed-effects differences in log crude death rates, with "
        "municipality and year effects, excluding 2011 from the post-period average:",
    ),
    ("eq", "ln(CDR_it) = a_i + g_t + b D_it + e_it"),
    (
        "p",
        "The preferred comparison uses unweighted T1 municipalities and Fukushima "
        "municipal controls for 2012-2019. Robustness checks vary control pools, "
        "population weighting, age controls, treatment definitions, permutation "
        "inference, and synthetic controls (Abadie et al., 2010, 2015; Abadie, 2021). "
        "The fixed-effects event-study design follows standard cautions about serial "
        "correlation and dynamic treatment patterns (Autor, 2003; Bertrand et al., 2004). "
        "The estimand is a difference in deaths "
        "recorded in municipal vital statistics relative to a counterfactual trend. It is "
        "not a direct estimate of evacuation-caused mortality. Resident registration, "
        "migration, deaths recorded outside the municipality, demographic composition, "
        "and selective return can affect both numerator and denominator. The 2011 "
        "decomposition separately compares observed and trend-expected deaths and direct "
        "disaster deaths. Appendix Table A2 reports unit-level synthetic-control results.",
    ),
    (
        "p",
        "The Fukushima interpretation also separates distinct risk quantities. Low-dose "
        "radiation policy often uses linear no-threshold or related dose-response "
        "assumptions to project population risks at doses where direct epidemiological "
        "identification is difficult (ICRP, 2007). Evacuation thresholds translate those "
        "risk assumptions into action, but evacuation can produce other harms. Measured "
        "municipal deaths, certified disaster-related deaths, and projected radiological "
        "deaths are not interchangeable estimands. We place them side by side only to "
        "show differences in scope, construction, and decision relevance.",
    ),
    (
        "p",
        "For Kansas, we constructed a state-year panel for {ks_pre_years} and later years, "
        "then estimated synthetic controls for real gross domestic product per capita, "
        "nonfarm employment, real total tax revenue per capita, and real individual "
        "income-tax revenue per capita. The main donor pool excludes states with large "
        "contemporaneous rate changes or without broad individual income taxes, leaving "
        "{ks_n_donors} donors; an all-state pool provides a second specification. "
        "Permutation tests, leave-one-donor-out checks, in-time placebos, and neighboring-"
        "state event studies assess sensitivity. State-specific aircraft, agriculture, "
        "and oil shocks remain plausible confounders.",
    ),
    (
        "p",
        "The relevant functional-form distinction is between the general Laffer-curve "
        "proposition and claims made for the Kansas reform (Laffer, 2004; Kansas "
        "Legislature, 2012; Rothschild, 2012). A revenue-maximizing tax rate "
        "may exist in principle without Kansas beginning above it, and a local behavioral "
        "response does not imply that a large tax cut will recover its static revenue loss "
        "through growth. The demonstration therefore evaluates the observed reform against "
        "its synthetic counterfactual; it does not test the universal existence of a "
        "Laffer curve.",
    ),
    (
        "p",
        "The Kansas estimands are post-reform gaps between Kansas and weighted donor states, "
        "conditional on pre-reform fit and the chosen donor restrictions. They combine the "
        "tax changes with other Kansas-specific events that occur after treatment and "
        "cannot establish the contribution of every statutory provision. The individual "
        "income-tax result is nevertheless directly relevant to the policy-facing claim "
        "that behavioral growth would offset a substantial part of the static revenue "
        "loss. GDP and employment outcomes provide a separate check on the growth channel; "
        "they should not be used to infer that all distributional, service, or long-run "
        "effects were absent.",
    ),
    ("h1", "Results"),
    ("h2", "Mapping functional-form identification across canonical relationships"),
    (
        "p",
        "At the default thresholds, {n_not_robust} of {n_curves} relationship-dataset "
        "pairs ({share_not_robust_pct}%) were not classified as robustly nonlinear. The "
        "largest category was not significant ({n_not_sig}); {n_outlier} were outlier "
        "dependent, {n_overfit} failed predictive comparison, and {n_insufficient} became "
        "insufficient after influence removal. Sixteen passed all criteria. Across the "
        "study's alpha and influence-removal grid, the share not classified as "
        "robustly nonlinear ranged from {share_min_pct}% to {share_max_pct}% (Figure 3). "
        "Table 1 reports categories by field.",
    ),
    ("fig", "fig_sensitivity"),
    ("table", "tab_audit"),
    (
        "p",
        "These classifications should be read as a map of shape identification under a "
        "common diagnostic, not a verdict on whether each underlying theory is true. A "
        "quadratic can miss a genuine nonlinear mechanism, and small datasets can fail a "
        "screen despite meaningful curvature. Conversely, a quadratic that passes does "
        "not establish causality or transportability. Across the mapped "
        "relationship-dataset pairs, several familiar schematic forms were more specific "
        "than could be established by the common diagnostic over the observed data range. "
        "For the Laffer dataset, the quadratic term had p = "
        "{laffer_p} with n = {laffer_n}; for the low-dose radiation dataset, it had p = "
        "{lnt_p} with n = {lnt_n}, including {lnt_n_lowdose} observations below 0.1 Gy. "
        "These two items motivate, but do not resolve, the policy demonstrations.",
    ),
    (
        "p",
        "The category pattern is more informative than the aggregate share alone. Most "
        "non-passing items did not provide strong evidence for the tested curvature, "
        "whereas a smaller group changed classification after influence or predictive "
        "checks. These are different evidentiary problems and call for different responses. "
        "Weak curvature evidence may justify presenting several shapes; influence "
        "dependence calls for scrutiny of measurement and scope; poor prediction cautions "
        "against using in-sample fit to forecast policy effects; insufficient support may "
        "justify targeted data collection. The map thus directs attention toward the "
        "assumption that carries the decision rather than issuing a uniform rejection.",
    ),
    ("h2", "Fukushima: policy dependence on an assumed risk function"),
    (
        "p",
        "Figure 4 plots pooled crude death rates. T1 municipalities show a sharp 2011 "
        "increase and a lower recorded rate than the Fukushima control group in much of "
        "the 2012-2019 estimation window. The preferred difference-in-differences estimate "
        "is {t1_main_att} log points, corresponding to approximately "
        "{t1_main_att_pct}% fewer recorded deaths than the counterfactual trend "
        "(permutation p {t1_main_perm_p}; pre-trend p {t1_main_pretrend_p}). Across T1 "
        "specifications, estimates range from {t1_att_min} to {t1_att_max} log points. "
        "Table 2 reports the specification grid, and Figure 5 shows the preferred event "
        "study.",
    ),
    ("fig", "fig_pooled_cdr"),
    ("table", "tab_fuku_att"),
    ("fig", "fig_event_study"),
    (
        "p",
        "The negative post-2011 coefficient is not evidence that evacuation improved "
        "health. It is consistent with mechanisms that change who remains registered or "
        "where deaths are recorded, including displacement, selective return, and "
        "population composition. It also illustrates why a single observed outcome can "
        "be misleading when the policy reshapes the population at risk. Synthetic-control "
        "and treatment-scope checks produce the same broad warning but do not eliminate "
        "these interpretive limits.",
    ),
    (
        "p",
        "This measurement problem is itself part of functional-form appraisal. Evacuation "
        "changes residence, service access, household composition, and the location where "
        "events are registered. The observed municipal mortality series therefore does not "
        "trace a stable population through exposure levels. A policy comparison that "
        "treated the post-evacuation curve as a biological dose-response function would "
        "confound the response of individuals with changes in who remains in the dataset. "
        "The relevant evidence architecture must distinguish exposure models, population "
        "movement, health outcomes, and administrative recording before those components "
        "are combined in a decision model.",
    ),
    (
        "p",
        "The 2011 decomposition is different. T1 municipalities recorded "
        "{t1_obs_2011} deaths against {t1_exp_2011} expected from their pre-disaster "
        "trend, an excess of {t1_excess_2011}. Direct disaster deaths account for "
        "{t1_direct_2011}, leaving a residual of {t1_resid_2011} (Figure 6). The residual "
        "cannot be assigned wholly to evacuation: emergency disruption, indirect disaster "
        "effects, measurement, and model error are also possible. Certified disaster-"
        "related deaths for Fukushima Prefecture total {ra_related_deaths} as of "
        "{ra_date}, but that prefecture-wide administrative measure differs from the T1 "
        "municipal decomposition (Fukushima Prefecture, 2014; Reconstruction Agency, "
        "{ra_year}).",
    ),
    ("fig", "fig_acute"),
    (
        "p",
        "Table 3 places these measured quantities beside published radiological "
        "projections. Ten Hoeve and Jacobson (2012) projected a best estimate of "
        "{thj_best} worldwide cancer deaths from the release, with a range of "
        "{thj_range}; their model attributed a best estimate of "
        "{thj_averted_best} averted radiological deaths to evacuation, with a range of "
        "{thj_averted_range}. WHO (2013) and UNSCEAR (2014) report other modeled risk "
        "quantities and scopes. The comparison does not add these figures or treat them as "
        "commensurate. It shows that an evacuation decision can be highly sensitive to the "
        "assumed low-dose response while its consequences extend to outcomes that the "
        "radiation-risk curve does not represent.",
    ),
    ("table", "tab_lnt"),
    (
        "p",
        "The demonstration therefore supports a calibrated conclusion. It does not show "
        "that the linear no-threshold model is false, that the evacuation was definitively "
        "wrong, or that non-evacuation would have been superior. It shows that the "
        "decision combined uncertain low-dose extrapolation with asymmetric and partly "
        "irreversible consequences. A functional-form appraisal would have required "
        "policy performance to be examined under multiple dose-response assumptions and "
        "would have treated evacuation design, duration, exceptions, staged return, and "
        "support for vulnerable residents as adjustable policy variables.",
    ),
    (
        "p",
        "The case also illustrates why robust design can be more useful than a binary "
        "choice between accepting and rejecting a risk model. Zoning, assisted voluntary "
        "relocation, exemptions for medically fragile residents, transport and continuity "
        "of care, time-limited orders, exposure monitoring, and staged return can perform "
        "differently across plausible risk functions. Evaluating that portfolio would not "
        "remove ethical conflict or uncertainty, but it would prevent a single low-dose "
        "curve from determining every dimension of the intervention.",
    ),
    ("h2", "Kansas: policy dependence on an assumed fiscal response function"),
    (
        "p",
        "Figure 7 compares Kansas with synthetic Kansas. After the 2012 reform, real "
        "individual income-tax revenue per capita averaged approximately "
        "{ks_iit_pct}% below the main synthetic counterfactual (permutation p = "
        "{ks_iit_perm_p}); the all-state donor pool implies {ks_iit_pct_all}%. The "
        "estimated gap increased from about ${ks_iit_gap_2013} per capita in 2013 to "
        "${ks_iit_gap_2016} in 2016, with a cumulative counterfactual gap of approximately "
        "${ks_iit_cum_bn} billion in 2012 dollars. Real total tax revenue was "
        "{ks_tax_pct}% lower (p = {ks_tax_perm_p}).",
    ),
    ("fig", "fig_kansas"),
    (
        "p",
        "The corresponding post-reform gaps were {ks_gdp_pct}% for real GDP per capita "
        "(p = {ks_gdp_perm_p}) and {ks_emp_pct}% for employment (p = "
        "{ks_emp_perm_p}). Table 4 reports both donor pools, pre-period fit, in-time "
        "placebos, and leave-one-donor-out ranges. The individual income-tax estimate is "
        "stable across leave-one-donor-out checks ({ks_iit_loo_min} to "
        "{ks_iit_loo_max} log points) and has pre-period RMSPE {ks_iit_rmspe}. These "
        "comparisons do not eliminate state-specific shocks, especially in aircraft "
        "manufacturing, agriculture, and energy.",
    ),
    ("table", "tab_kansas"),
    (
        "p",
        "The result is not a universal rejection of the Laffer curve. It is a failure to "
        "observe a macroeconomic response large enough, within this period and design, to "
        "offset the reform's revenue loss. The functional-form issue lies in moving from a "
        "general possibility of a revenue maximum to a claim about Kansas's initial "
        "position, the local slope over a large policy change, and the timing and magnitude "
        "of dynamic growth. Those are separate empirical propositions. Treating the "
        "schematic curve as sufficient evidence compressed them into one policy claim.",
    ),
    (
        "p",
        "A decision-facing appraisal would have separated at least four quantities: the "
        "static mechanical revenue loss, the behavioral response of taxable income, the "
        "effect of the reform on broader economic activity, and the timing with which any "
        "growth returns to the tax base. Each quantity can have a different functional "
        "form and lag structure. Budget safeguards, staged rate changes, automatic review "
        "triggers, and sunset clauses could then be evaluated against scenarios in which "
        "the growth response is early, delayed, small, or concentrated outside the taxed "
        "base. The point is not that gradualism is always optimal, but that reversibility "
        "and monitoring have value when the fiscal response curve is uncertain.",
    ),
    ("h1", "Discussion"),
    ("h2", "Principal finding: association is not shape"),
    (
        "p",
        "The central finding is conceptual and practical. Evidence that two variables are "
        "associated does not by itself identify the functional form required for a policy "
        "decision. Across the mapped relationship-dataset pairs, classification under the "
        "common screen often depended on significance thresholds, influential "
        "observations, predictive comparison, or limited data. The policy demonstrations "
        "show why that distinction "
        "matters: a dose-response assumption can influence an emergency threshold, while "
        "a tax-response assumption can support a large fiscal change. In neither setting "
        "does uncertainty disappear merely because the curve has a recognized name.",
    ),
    (
        "p",
        "This argument is not a demand for model-free policy. All appraisal uses models, "
        "and emergency decisions often must be made before evidence is complete. The "
        "relevant standard is conditional transparency: identify which shape the "
        "recommendation needs, show the range where it is supported, compare plausible "
        "alternatives, and state whether the action changes. Model uncertainty becomes "
        "policy risk when alternatives imply materially different decisions or "
        "consequences.",
    ),
    (
        "p",
        "This distinction also qualifies common evidence hierarchies. A design that is "
        "credible for estimating an average contrast does not automatically rank highly "
        "for identifying a threshold, optimum, or tail response. The evidentiary question "
        "must match the policy claim. If the decision needs the sign of an average effect, "
        "a local contrast may be sufficient. If it needs a turning point or a projection "
        "far beyond observed support, the same study may provide only indirect evidence. "
        "Appraisal systems should therefore record not only study quality but which feature "
        "of the response function the design can identify.",
    ),
    (
        "p",
        "Named curves can obscure this matching problem because they provide a portable "
        "vocabulary for officials, experts, advocates, and the public. Portability is "
        "valuable, but it can detach the image from its provenance. A useful accountability "
        "practice is to maintain an assumption ledger: the dataset and design supporting "
        "the shape, the range actually observed, transformations used, influential cases, "
        "competing forms considered, and the part of the decision that changes if the "
        "shape changes. Such documentation makes disagreement traceable without requiring "
        "every decision maker to reproduce the underlying analysis.",
    ),
    ("h2", "Policy-relevant range and transportability"),
    (
        "p",
        "Functional-form identification must be local to the decision. Global fit can hide "
        "weak support near a threshold or turning point, and dense observations in one "
        "range cannot validate extrapolation into another. The relevant support should be "
        "reported alongside the policy range, including which populations and periods "
        "identify the slope or curvature. Where evidence is transported, analysts should "
        "state which causal mechanisms and institutional conditions are assumed to remain "
        "stable. This extends the familiar concern with external validity from average "
        "effects to the shape of the response function.",
    ),
    (
        "p",
        "The Fukushima case makes range validity especially salient because low-dose risk "
        "projections necessarily rely on assumptions where direct signal is weak. The "
        "Kansas case makes local policy position salient because the existence of a "
        "revenue maximum says little about whether a particular state is above or below it. "
        "In both cases, the policy-relevant claim is narrower and more demanding than the "
        "canonical relationship's general plausibility.",
    ),
    (
        "p",
        "Transportability should be decomposed rather than treated as a single yes-or-no "
        "judgment. Population transport asks whether effect modifiers and vulnerability "
        "differ; temporal transport asks whether technology, behavior, or baseline risk "
        "changed; institutional transport asks whether implementation and incentives are "
        "comparable; range transport asks whether the relevant values are represented. A "
        "claim can transport on some dimensions and fail on another. Recording these "
        "dimensions separately clarifies whether uncertainty should alter the model, the "
        "target population, the implementation plan, or the strength of commitment.",
    ),
    (
        "p",
        "Policies can also change the process used to learn the curve. Evacuation alters "
        "where people live and where health events are observed; tax reform changes "
        "reporting, avoidance, investment timing, and the composition of the tax base. "
        "Post-policy data are therefore not passive observations of the pre-policy "
        "relationship. Monitoring plans should anticipate these feedbacks and preserve "
        "measures capable of distinguishing substantive response from selection, "
        "adaptation, and administrative reclassification.",
    ),
    ("h2", "Functional-form dependence as policy risk"),
    (
        "p",
        "The seriousness of functional-form dependence depends on consequences, not only "
        "statistical uncertainty. A wrong shape may be tolerable when a policy is cheap, "
        "reversible, and produces similar outcomes across plausible models. It is more "
        "concerning when action is large, irreversible, distributionally uneven, or "
        "likely to create path dependence. Consequence asymmetry also cuts in both "
        "directions. Underreaction and overreaction may harm different groups, on different "
        "time horizons, through outcomes measured in different units. Appraisal should not "
        "allow one modeled outcome to eclipse harms omitted from the response function.",
    ),
    (
        "p",
        "This view connects evidence use to policy design. Robustness is not simply a "
        "property of a coefficient; it is a property of an action across uncertain states "
        "of the world. Staged implementation, pilots, adaptive thresholds, sunset clauses, "
        "monitoring triggers, and support for exposed groups can reduce the cost of being "
        "wrong. Policy appraisal should therefore ask not only which curve fits best, but "
        "which feasible policy remains acceptable if the curve differs.",
    ),
    (
        "p",
        "Four recurring forms of decision dependence deserve separate attention. Threshold "
        "dependence arises when small changes in a fitted boundary switch legal or "
        "administrative status. Turning-point dependence arises when policy assumes that "
        "an instrument lies on one side of an optimum. Extrapolation dependence arises "
        "when benefits or harms are projected into ranges with little direct support. "
        "Aggregation dependence arises when a population-level curve masks heterogeneous "
        "responses that matter for targeting or equity. The appropriate safeguard differs: "
        "buffer zones for thresholds, local identification around optima, scenario bounds "
        "for extrapolation, and subgroup or distributional analysis for aggregation.",
    ),
    (
        "p",
        "Robustness and resilience remain distinct. Robustness asks whether an action "
        "performs acceptably across the uncertainties considered at appraisal. Resilience "
        "concerns the capacity of a policy system to detect surprises, absorb disruption, "
        "and reorganize after implementation (Capano & Woo, 2017). A policy can be robust "
        "to several response shapes yet brittle to an omitted outcome, or initially "
        "non-robust yet governed by institutions capable of rapid correction. Functional-"
        "form appraisal should therefore inform both ex ante choice and the ex post "
        "capacity to learn.",
    ),
    ("h2", "Applying the decision-facing appraisal framework"),
    (
        "p",
        "Figure 1 introduced the decision-facing appraisal framework before the empirical "
        "demonstrations. Analysts first specify the empirical "
        "relationship and the functional-form assumption embedded in the policy claim. "
        "They then delimit the policy-relevant range and test whether alternative shapes "
        "change the decision. Next they map consequences, including asymmetries and "
        "outcomes outside the focal curve. Finally, they choose an action architecture: "
        "commitment may be justified when the form is well identified and alternatives "
        "converge, while staging, adaptation, or precaution may be preferable when "
        "decisions diverge and consequences are asymmetric.",
    ),
    (
        "p",
        "The decision-facing appraisal framework can be implemented without a large new "
        "modeling exercise. A minimum appraisal can display the observed support, compare "
        "a small set of theoretically plausible forms, report the induced policy "
        "recommendation under each, and explain which consequences are excluded. "
        "Sensitivity auditing is most useful when it follows the decision logic rather "
        "than varying parameters indiscriminately (Saltelli et al., 2020). Where "
        "disagreement concerns values rather than evidence, the appraisal should preserve "
        "that distinction instead of presenting technical uncertainty as the sole source "
        "of conflict.",
    ),
    (
        "p",
        "A fuller appraisal can be organized as a decision table. Rows represent credible "
        "functional forms or bounded scenarios; columns report the implied threshold or "
        "policy intensity, affected population, expected benefits, omitted outcomes, and "
        "distribution of losses if the scenario is wrong. A final column records whether "
        "the action can be paused, reversed, or revised and what evidence would trigger "
        "that change. The purpose is not to assign spurious probabilities to every model "
        "but to reveal whether the recommendation is stable and where learning has the "
        "highest decision value.",
    ),
    (
        "p",
        "The candidate model set should be theoretically and empirically disciplined. "
        "Including arbitrary curves can manufacture indecision; considering only the "
        "incumbent specification can manufacture confidence. Analysts should justify "
        "alternatives using mechanism, prior evidence, diagnostics, and known sources of "
        "extrapolation. Where the set remains contested, results can be reported under "
        "nested assumptions so that decision makers can see which conclusion requires "
        "which restriction. This is more informative than a single preferred estimate "
        "accompanied by a generic statement that results are robust.",
    ),
    (
        "p",
        "Institutional responsibility should be assigned for updating the appraisal. A "
        "monitoring indicator without a named decision, review date, and authority to act "
        "does not create adaptation. For high-consequence policies, the record should "
        "identify who maintains the data, who reassesses the functional form, which "
        "stakeholders review asymmetric consequences, and what procedural threshold "
        "permits revision. These governance details matter because model assumptions can "
        "persist through organizational routines after their empirical basis has changed.",
    ),
    ("h2", "Limitations"),
    (
        "p",
        "The mapping exercise is deliberately bounded. The inventory is not a probability "
        "sample, relationship-dataset pairs are not independent studies, and the common "
        "quadratic alternative cannot represent every scientifically plausible form. "
        "Several datasets are small, classifications depend on methodological judgments, "
        "and a single dataset cannot adjudicate a literature. The mapping therefore does "
        "not estimate how often canonical theories are false. Its sensitivity analysis "
        "shows that the headline share varies, although the broader pattern persists.",
    ),
    (
        "p",
        "The policy demonstrations also have important limits. The Fukushima analysis uses "
        "municipal vital statistics affected by displacement, registration, demographic "
        "change, and location of death. The resident-register denominator changes from "
        "Japanese residents through 2012 to total residents from 2013; year effects absorb "
        "a common level change, but differential foreign-resident composition may remain. "
        "The tsunami-inundation exclusion and treatment boundary are also design choices "
        "rather than randomized assignment. The analysis cannot attribute the full 2011 "
        "residual or the post-2011 difference to evacuation, nor can it estimate the "
        "unobserved health outcomes under a non-evacuation policy. The Kansas synthetic "
        "control cannot fully "
        "separate the tax reform from contemporaneous state-specific sectoral shocks; the "
        "neighboring-state event studies in Appendix Figure A1 are supplementary rather "
        "than definitive. Neither case isolates the causal effect of believing a curve.",
    ),
    (
        "p",
        "The article also stops short of a welfare analysis that places all case outcomes "
        "on a common scale. That omission is deliberate because monetizing or aggregating "
        "mortality, displacement, service loss, revenue, growth, and distribution would "
        "introduce additional functional forms and normative weights. The framework can "
        "structure such an analysis, but it cannot remove the need for transparent value "
        "judgments. Future applications should examine how stakeholder participation "
        "changes the candidate consequence set and the definition of material decision "
        "change.",
    ),
    (
        "p",
        "Finally, the decision-facing appraisal framework does not supply a universal rule "
        "for choosing among uncertain models. Decisions may still differ because of risk "
        "tolerance, equity weights, time horizons, or institutional responsibilities. Its "
        "value is diagnostic: it makes explicit when a named relationship is carrying more "
        "of the policy argument than the evidence over the relevant range can support.",
    ),
    ("h1", "Conclusion"),
    (
        "p",
        "Evidence-based policymaking should distinguish evidence for the existence of an "
        "association from evidence for the specific shape needed to justify a decision. "
        "Functional-form dependence identifies cases in which an insufficiently "
        "identified or transported shape determines a policy's threshold, direction, "
        "intensity, or expected benefit. The decision-facing appraisal framework does not "
        "imply automatic inaction. It requires analysts to expose the assumption, test the "
        "policy-relevant range, compare decisions under plausible alternatives, examine "
        "asymmetric consequences, and design policies that can learn or adapt where "
        "uncertainty remains. Before a canonical relationship is used to justify "
        "consequential policy, both the association and the decision-relevant shape should "
        "be validated.",
    ),
    ("h1", "Data availability"),
    (
        "p",
        "All data used in the analyses are from public sources. Archived source files, "
        "acquisition metadata, processed datasets, analysis code, machine-readable "
        "results, and document-generation code will be supplied to reviewers through an "
        "anonymized archive. The public repository URL is provided to the editor in the "
        "title-page materials and will be added to the manuscript after double-anonymous "
        "review. The archive README records the commands required to reproduce the "
        "analyses and submission files.",
    ),
    ("h1", AI_ASSISTANCE_HEADING),
    ("p", AI_ASSISTANCE_TEXT),
    ("refs", None),
]

CAPTIONS = {
    "fig_decision_tree": (
        "Figure 2. Diagnostic used in the cross-domain mapping exercise. Green paths "
        "continue toward robust nonlinear classification; orange paths indicate the "
        "first unmet criterion. Insufficient data is assigned when influence removal "
        "leaves too few observations for the nested comparison."
    ),
    "fig_sensitivity": (
        "Figure 3. Share of {n_curves} relationship-dataset pairs not classified as "
        "robustly nonlinear across significance levels and Cook-distance removal counts. "
        "Cell labels report percentages; the color scale spans 0-100%."
    ),
    "fig_pooled_cdr": (
        "Figure 4. Pooled crude death rates in Fukushima treatment and control groups. T1 "
        "contains {n_t1} mandatory-evacuation municipalities; T1w is the restricted "
        "complete-evacuation group; T2 contains comparison municipalities subject to "
        "other evacuation-related classifications. The shaded region is the 2012-2019 "
        "average-treatment-effect window."
    ),
    "fig_event_study": (
        "Figure 5. Preferred T1 event-study estimates using unweighted Fukushima municipal "
        "controls. Points are year-specific coefficients relative to the omitted reference "
        "year; bars are 95% confidence intervals. The acute disaster year 2011 is shown "
        "but excluded from the 2012-2019 average-treatment-effect window."
    ),
    "fig_acute": (
        "Figure 6. T1 acute-phase mortality decomposition for 2011. Expected deaths are "
        "projected from the pre-disaster municipal trend; direct disaster deaths are "
        "reported by Fukushima Prefecture; residual excess is the arithmetic difference "
        "and is not assigned to a single cause."
    ),
    "fig_kansas": (
        "Figure 7. Kansas and synthetic Kansas, 1997-2019. Panel (a) reports log real "
        "individual income-tax revenue per capita; panel (b) reports log real GDP per "
        "capita. Synthetic controls use the main {ks_n_donors}-state donor pool. Shading "
        "marks 2013-2017, between implementation and legislative reversal."
    ),
    "fig_policy_pathway": (
        "Figure 1. Decision-facing appraisal framework for functional-form dependence. "
        "The framework links the empirical relationship and assumed shape to the policy-"
        "relevant range, decision sensitivity, asymmetric consequences, and an action "
        "architecture that can include commitment, staging, adaptation, or precaution."
    ),
    "fig_a1": (
        "Appendix Figure A1. Kansas neighboring-state difference-in-differences event "
        "studies for real GDP per capita, employment, total tax revenue, and individual "
        "income-tax revenue. Coefficients are relative to 2012; bars are 95% confidence "
        "intervals."
    ),
    "tab_audit": (
        "Table 1. Cross-domain mapping classifications by category. Counts describe the "
        "purposive relationship-dataset inventory and are not prevalence estimates for "
        "scientific theories or literatures."
    ),
    "tab_fuku_att": (
        "Table 2. Fukushima difference-in-differences estimates. ATT is the 2012-2019 "
        "average difference in log crude death rates; 2011 is excluded. Permutation p "
        "values use {n_perm} assignments. Implied deaths are descriptive transformations "
        "of recorded municipal deaths and are not causal death counts."
    ),
    "tab_lnt": (
        "Table 3. Fukushima measured mortality quantities and published radiological-risk "
        "projections. Rows differ in population, geography, time horizon, measurement, and "
        "model basis and must not be added or interpreted as commensurate estimands."
    ),
    "tab_kansas": (
        "Table 4. Kansas synthetic-control estimates by outcome and donor pool. Mean gaps "
        "cover 2013-2017. Permutation p values compare Kansas with donor-state placebo "
        "gaps; LOO denotes leave-one-donor-out sensitivity."
    ),
    "tab_a1": (
        "Appendix Table A1. Municipalities excluded from the Fukushima panel because of "
        "missing mortality or population observations. Exclusions are determined before "
        "outcome estimation."
    ),
    "tab_a2": (
        "Appendix Table A2. Unit-level Fukushima synthetic-control results for T1 "
        "municipalities. Mean gaps cover 2012-2019; permutation p values compare treated "
        "and placebo-unit gaps."
    ),
}

REFERENCES = [
    (
        "Abadie, A. (2021). Using synthetic controls: Feasibility, data requirements, "
        "and methodological aspects. Journal of Economic Literature, 59(2), 391-425. "
        "https://doi.org/10.1257/jel.20191450"
    ),
    (
        "Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for "
        "comparative case studies: Estimating the effect of California's tobacco control "
        "program. Journal of the American Statistical Association, 105(490), 493-505. "
        "https://doi.org/10.1198/jasa.2009.ap08746"
    ),
    (
        "Abadie, A., Diamond, A., & Hainmueller, J. (2015). Comparative politics and the "
        "synthetic control method. American Journal of Political Science, 59(2), 495-510. "
        "https://doi.org/10.1111/ajps.12116"
    ),
    (
        "Autor, D. H. (2003). Outsourcing at will: The contribution of unjust dismissal "
        "doctrine to the growth of employment outsourcing. Journal of Labor Economics, "
        "21(1), 1-42. https://doi.org/10.1086/344122"
    ),
    (
        "Bertrand, M., Duflo, E., & Mullainathan, S. (2004). How much should we trust "
        "differences-in-differences estimates? Quarterly Journal of Economics, 119(1), "
        "249-275. https://doi.org/10.1162/003355304772839588"
    ),
    (
        "Burnham, K. P., & Anderson, D. R. (2004). Multimodel inference: Understanding "
        "AIC and BIC in model selection. Sociological Methods & Research, 33(2), 261-304. "
        "https://doi.org/10.1177/0049124104268644"
    ),
    (
        "Capano, G., & Malandrino, A. (2022). Mapping the use of knowledge in policymaking: "
        "Barriers and facilitators from a subjectivist perspective (1990-2020). Policy "
        "Sciences, 55(3), 399-428. https://doi.org/10.1007/s11077-022-09468-0"
    ),
    (
        "Capano, G., & Woo, J. J. (2017). Resilience and robustness in policy design: A "
        "critical appraisal. Policy Sciences, 50(3), 399-426. "
        "https://doi.org/10.1007/s11077-016-9273-x"
    ),
    (
        "Cartwright, N., & Hardie, J. (2012). Evidence-based policy: A practical guide to "
        "doing it better. Oxford University Press."
    ),
    (
        "Cook, R. D. (1977). Detection of influential observation in linear regression. "
        "Technometrics, 19(1), 15-18. https://doi.org/10.1080/00401706.1977.10489493"
    ),
    (
        "Draper, D. (1995). Assessment and propagation of model uncertainty. Journal of "
        "the Royal Statistical Society: Series B, 57(1), 45-70. "
        "https://doi.org/10.1111/j.2517-6161.1995.tb02015.x"
    ),
    (
        "Dunlop, C. A. (2010). The temporal dimension of knowledge and the limits of policy "
        "appraisal: Biofuels policy in the UK. Policy Sciences, 43(4), 343-363. "
        "https://doi.org/10.1007/s11077-009-9101-7"
    ),
    (
        "Fukushima Prefecture. (2014). Higashinihon daishinsai ni yoru higai jokyo sokuhou "
        "(dai 1260-ho) [Preliminary report on damage caused by the Great East Japan "
        "Earthquake (Report No. {fdr_no})]. {fdr_url}"
    ),
    (
        "Head, B. W. (2008). Three lenses of evidence-based policy. Australian Journal of "
        "Public Administration, 67(1), 1-11. "
        "https://doi.org/10.1111/j.1467-8500.2007.00564.x"
    ),
    (
        "International Commission on Radiological Protection. (2007). The 2007 "
        "recommendations of the International Commission on Radiological Protection. "
        "ICRP Publication 103. Annals of the ICRP, 37(2-4). "
        "https://doi.org/10.1016/j.icrp.2007.10.003"
    ),
    (
        "Kansas Legislature. (2012). House Bill 2117, enrolled. "
        "https://www.kslegislature.gov/li_2012/b2011_12/measures/documents/"
        "hb2117_enrolled.pdf"
    ),
    (
        "Kolkman, D. A., Campo, P., Balke-Visser, T., & Gilbert, N. (2016). How to build "
        "models for government: Criteria driving model acceptance in policymaking. Policy "
        "Sciences, 49(4), 489-504. https://doi.org/10.1007/s11077-016-9250-4"
    ),
    (
        "Laffer, A. B. (2004). The Laffer curve: Past, present, and future. Heritage "
        "Foundation Backgrounder, 1765, 1-16. "
        "https://www.heritage.org/taxes/report/the-laffer-curve-past-present-and-future"
    ),
    (
        "Lempert, R. J., & Collins, M. T. (2007). Managing the risk of uncertain threshold "
        "responses: Comparison of robust, optimum, and precautionary approaches. Risk "
        "Analysis, 27(4), 1009-1026. "
        "https://doi.org/10.1111/j.1539-6924.2007.00940.x"
    ),
    (
        "Ministry of Health, Labour and Welfare. (2021). Vital statistics of Japan "
        "[Data set]. Portal Site of Official Statistics of Japan. "
        "https://www.e-stat.go.jp/en/stat-search/database?page=1&toukei=00450011"
    ),
    (
        "Ministry of Internal Affairs and Communications. (2021). Population, "
        "demographics, and household counts based on the Basic Resident Registration "
        "[Data set]. Portal Site of Official Statistics of Japan. "
        "https://www.e-stat.go.jp/en/stat-search/files?toukei=00200241"
    ),
    (
        "Parkhurst, J. O. (2016). Appeals to evidence for the resolution of wicked "
        "problems: The origins and mechanisms of evidentiary bias. Policy Sciences, "
        "49(4), 373-393. https://doi.org/10.1007/s11077-016-9263-z"
    ),
    (
        "Reconstruction Agency. ({ra_year}). Higashinihon daishinsai ni okeru "
        "shinsai-kanrenshi no shisha-su [Number of disaster-related deaths in the Great "
        "East Japan Earthquake] (as of {ra_date}). {ra_url}"
    ),
    (
        "Roth, J., & Sant'Anna, P. H. C. (2023). When is parallel trends sensitive to "
        "functional form? Econometrica, 91(2), 737-747. "
        "https://doi.org/10.3982/ECTA19402"
    ),
    (
        "Rothschild, S. (2012, January 19). Consultant Laffer praises Brownback's tax "
        "plan. Lawrence Journal-World. https://www2.ljworld.com/news/2012/jan/19/"
        "consultant-laffer-touts-brownbacks-tax-plan/"
    ),
    (
        "Saltelli, A., Bammer, G., Bruno, I., Charters, E., Di Fiore, M., Didier, E., "
        "Espeland, W. N., Kay, J., Lo Piano, S., Mayo, D., Pielke, R., Portaluri, T., "
        "Porter, T. M., Puy, A., Rafols, I., Ravetz, J. R., Reinert, E., Sarewitz, D., "
        "Stark, P. B., Stirling, A., van der Sluijs, J., & Vineis, P. (2020). Five ways "
        "to ensure that models serve society: A manifesto. Nature, 582(7813), 482-484. "
        "https://doi.org/10.1038/d41586-020-01812-9"
    ),
    (
        "ten Hoeve, J. E., & Jacobson, M. Z. (2012). Worldwide health effects of the "
        "Fukushima Daiichi nuclear accident. Energy & Environmental Science, 5(9), "
        "8743-8757. https://doi.org/10.1039/C2EE22019A"
    ),
    (
        "United Nations Scientific Committee on the Effects of Atomic Radiation. (2014). "
        "Sources, effects and risks of ionizing radiation: UNSCEAR 2013 report, Volume I, "
        "Scientific Annex A. United Nations. "
        "https://www.unscear.org/unscear/uploads/documents/unscear-reports/"
        "UNSCEAR_2013_Report_Vol.I.pdf"
    ),
    (
        "Wesselink, A., Colebatch, H., & Pearce, W. (2014). Evidence and policy: "
        "Discourses, meanings and practices. Policy Sciences, 47(4), 339-344. "
        "https://doi.org/10.1007/s11077-014-9209-2"
    ),
    (
        "World Health Organization. (2013). Health risk assessment from the nuclear "
        "accident after the 2011 Great East Japan Earthquake and Tsunami, based on a "
        "preliminary dose estimation. World Health Organization. "
        "https://iris.who.int/handle/10665/78218"
    ),
]

APPENDIX = [
    (
        "h1",
        "Appendix: Supplementary municipality exclusions and robustness analyses",
    ),
    ("table", "tab_a1"),
    ("table", "tab_a2"),
    ("fig", "fig_a1"),
]
