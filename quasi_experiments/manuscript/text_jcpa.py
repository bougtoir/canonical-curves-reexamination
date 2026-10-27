"""JCPA (Journal of Comparative Policy Analysis) manuscript text.

Explicit comparative rewrite of the functional-form dependence manuscript.
Numerical fields are populated by build_manuscript.py from analysis outputs.
"""

TITLE = (
    "When Policy Depends on a Curve: Comparing Functional-Form Dependence "
    "in Fukushima Evacuation and Kansas Tax Reform"
)

ABSTRACT = (
    "Policies often depend on the shape of an empirical relationship, not "
    "merely on an association. I define functional-form dependence as "
    "reliance on a threshold, slope, turning point, or extrapolated "
    "response that is less securely identified than the policy assumes. A "
    "structured comparison of post-Fukushima evacuation and Kansas tax "
    "reform examines decision-relevant shape, uncertainty, "
    "transportability, consequence asymmetry, reversibility, and learning "
    "capacity. The cases share the same mechanism but differ in its "
    "policy significance. A purposive mapping of {n_curves} canonical "
    "relationships provides background motivation. The comparison yields "
    "transferable lessons for policy appraisal under uncertain functional "
    "form."
)

KEYWORDS = (
    "comparative policy analysis; functional form; lesson-drawing; policy "
    "appraisal; evidence-based policymaking; uncertainty"
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
        "Policy arguments routinely depend on the shape of an empirical "
        "relationship rather than on the existence of an association alone. "
        "An evacuation order depends on how risk declines with dose. A tax "
        "cut is defended on how revenue and activity respond to rates. In "
        "each case, the policy requires a particular feature of the "
        "underlying curve - a threshold, a local slope, a turning point, or "
        "an extrapolated segment - to hold over the range where the policy "
        "operates.",
    ),
    (
        "p",
        "This creates what this article calls functional-form dependence: "
        "the condition in which a policy's justification, expected benefit, "
        "threshold, direction, or intensity materially depends on a "
        "relationship shape that is insufficiently identified over the "
        "policy-relevant range. Functional-form uncertainty is a form of "
        "model uncertainty about relationship shape (Draper, 1995; Morgan & "
        "Henrion, 1990); functional-form dependence is the decision-level "
        "condition in which that uncertainty changes what should be done.",
    ),
    (
        "p",
        "Existing discussions of model uncertainty, evidence use, and policy "
        "appraisal do not always show how such uncertainty changes policy "
        "choice under different institutional and consequence structures "
        "(Weimer & Vining, 2017; Walker et al., 2013). Evidence enters "
        "policy through institutions and routines that can privilege a "
        "familiar picture over a fragile empirical claim (Cairney, 2016; "
        "Parkhurst, 2016; Boswell, 2009). What remains underdeveloped is a "
        "comparative account: when does the same kind of evidentiary gap "
        "become decision-critical in one policy setting and manageable in "
        "another?",
    ),
    (
        "p",
        "The comparative puzzle is therefore: why does the same basic "
        "evidence problem - a decision that leans on an incompletely "
        "identified relationship shape - create different decision risks in "
        "different policy settings? Answering it requires cases that share "
        "the mechanism but differ on the conditions that could plausibly "
        "moderate it.",
    ),
    (
        "p",
        "This article compares post-Fukushima evacuation, justified under "
        "low-dose radiation-risk assumptions, with the Kansas tax reform of "
        "2012, defended under a claimed tax-rate-revenue and growth response. "
        "The two policies are deliberately dissimilar - different sectors, "
        "scientific traditions, institutional environments, temporal "
        "dynamics, and consequences of error - yet both committed resources "
        "and authority on functional-form assumptions whose decision-"
        "relevant features were incompletely identified. This maximum-"
        "contrast selection follows the logic of comparing unlike systems "
        "to identify which features of a phenomenon are general and which "
        "are context-dependent (Przeworski & Teune, 1970).",
    ),
    (
        "p",
        "The comparison is organized around common dimensions: the policy-"
        "dependent relationship, the decision-relevant functional feature, "
        "the location and type of uncertainty, decision sensitivity, "
        "transportability of evidence, consequence asymmetry, reversibility, "
        "and the opportunity for iterative learning. Figure 1 summarizes the "
        "shared analytical sequence with each case mapped onto the same "
        "dimensions.",
    ),
    ("fig", "fig_policy_pathway"),
    (
        "p",
        "A purposive mapping of {n_curves} canonical relationships supplies "
        "background motivation: the gap between association, empirical "
        "shape, and policy-relevant functional form is not unique to either "
        "case. The mapping is not the comparative core and is used only to "
        "establish that the problem class is broad.",
    ),
    (
        "p",
        "The article makes three contributions. Conceptually, it defines "
        "functional-form dependence as a decision-level manifestation of "
        "model-form uncertainty. Comparatively, it identifies the shared "
        "mechanism and the context-dependent moderators across two highly "
        "dissimilar policies, in the structured and focused tradition of "
        "comparative case analysis (George & Bennett, 2005). Practically, "
        "it derives comparative propositions and lesson-drawing for policy "
        "appraisal under uncertain functional form, in the tradition JCPA "
        "has long cultivated (Rose, 1991; Bennett & Howlett, 1992; Dolowitz "
        "& Marsh, 2000).",
    ),
    ("h1", "Comparative research design"),
    ("h2", "Case selection"),
    (
        "p",
        "Fukushima and Kansas were selected for maximum substantive contrast "
        "combined with a common analytical mechanism. They differ sharply in "
        "policy sector (radiation protection versus fiscal policy), "
        "institutional environment (emergency disaster governance versus "
        "legislative budget politics), scientific tradition (radiation "
        "epidemiology versus public economics), temporal dynamics, and the "
        "consequences of error. They nonetheless expose the same decision-"
        "level mechanism: in both, policy commitment depended on "
        "functional-form assumptions whose decision-relevant features were "
        "incompletely identified by the evidence available at the time.",
    ),
    (
        "p",
        "This design permits three things: identification of a recurring "
        "mechanism across heterogeneous contexts; examination of how "
        "consequence asymmetry and reversibility modify the importance of "
        "shape uncertainty; and comparative lesson-drawing about appraisal "
        "practice. It does not permit prevalence estimation, causal "
        "inference about all policies that use nonlinear models, or "
        "statistical generalization from N = 2. The cases are contrasting "
        "instrumental cases, not a representative sample (George & Bennett, "
        "2005).",
    ),
    ("h2", "Units and common comparative dimensions"),
    (
        "p",
        "The unit of comparison is the policy decision, not the country, "
        "program, or dataset. In each case, the analysis isolates the "
        "load-bearing empirical proposition within the policy rationale and "
        "asks how the decision depended on a specific functional feature of "
        "that relationship. Both cases are examined under the same eight "
        "dimensions: (1) the policy-dependent relationship; (2) the "
        "decision-relevant functional feature; (3) the location of "
        "functional-form uncertainty; (4) decision sensitivity - whether "
        "materially different plausible shapes imply materially different "
        "choices; (5) transportability of the available evidence to the "
        "relevant population, setting, range, and period; (6) consequence "
        "asymmetry - the relative harms of acting on a wrong form versus "
        "failing to act on a right one; (7) reversibility of the "
        "intervention; and (8) the learning architecture available to the "
        "policy - whether it could have been piloted, staged, updated, "
        "monitored, or adapted.",
    ),
    (
        "p",
        "The comparison is structured and focused rather than statistical: "
        "the same questions are asked of each case, and the answers are "
        "coded qualitatively into a common comparative table presented in "
        "the comparative findings. No numerical comparability is claimed "
        "between the cases' estimates; "
        "the shared object is the dependence structure between evidence and "
        "decision.",
    ),
    ("h2", "Evidence in each case"),
    (
        "p",
        "For Fukushima, annual municipal deaths and resident-register "
        "populations were assembled for {n_all_units} municipalities from "
        "the Japanese government's official-statistics portal (Ministry of "
        "Health, Labour and Welfare, 2021; Ministry of Internal Affairs and "
        "Communications, 2021). The primary treatment group (T1) contains "
        "{n_t1} municipalities subject to mandatory evacuation orders, with "
        "approximately {evac_pop_approx} residents in 2010; municipalities "
        "with tsunami inundation exceeding {tsunami_cut}% were excluded to "
        "reduce direct-tsunami confounding; missing-data exclusions are "
        "reported in Appendix Table A1. Two-way fixed-effects differences "
        "in log crude death rates were estimated for 2012-2019, with "
        "robustness across control pools, weighting, treatment definitions, "
        "permutation inference, and synthetic controls (Abadie et al., "
        "2010, 2015; Abadie, 2021; Bertrand et al., 2004); unit-level "
        "synthetic-control results are reported in Appendix Table A2.",
    ),
    (
        "p",
        "For Kansas, a state-year panel covering {ks_pre_years} and later "
        "years supports synthetic-control estimates of real GDP per capita, "
        "nonfarm employment, real total tax revenue per capita, and real "
        "individual income-tax revenue per capita. The main donor pool "
        "excludes states with large contemporaneous rate changes or without "
        "broad income taxes, leaving {ks_n_donors} donors; permutation "
        "tests, leave-one-donor-out checks, in-time placebos, and "
        "neighboring-state event studies assess sensitivity (Appendix "
        "Figure A1).",
    ),
    (
        "p",
        "Neither analysis claims to identify a universally correct "
        "radiation model or tax schedule, and neither treats a curve as the "
        "sole cause of policy. Emergency evacuation and tax legislation "
        "reflect legal authority, political commitments, and multiple "
        "streams of evidence; the design isolates the functional-form "
        "proposition each decision depended on.",
    ),
    ("h2", "Background: cross-domain mapping"),
    (
        "p",
        "To establish that the problem class extends beyond these cases, a "
        "purposive inventory of {n_inventory} named nonlinear relationships "
        "was screened with one common diagnostic; two pairs lacking a "
        "reproducible dataset were excluded, leaving {n_curves}. Each "
        "relationship-dataset pair was evaluated against a linear baseline "
        "with a quadratic alternative, requiring a nested F-test at alpha = "
        "{alpha_default}, robustness to removal of the {k_default} most "
        "influential observations, leave-one-out predictive improvement, and "
        "BIC preference (Cook, 1977; Burnham & Anderson, 2004). Figure 2 "
        "shows the decision sequence.",
    ),
    ("fig", "fig_decision_tree"),
    (
        "p",
        "Under the default criteria, {n_not_robust} of {n_curves} pairs "
        "({share_not_robust_pct}%) did not meet the criteria for robust "
        "nonlinear identification; the share ranged from {share_min_pct}% "
        "to {share_max_pct}% across the alpha and influence-removal grid "
        "(Figure 3). Table 1 reports categories by field. For the Laffer "
        "dataset the quadratic term had p = {laffer_p} (n = {laffer_n}); "
        "for the low-dose radiation dataset p = {lnt_p} (n = {lnt_n}), with "
        "{lnt_n_lowdose} observations below 0.1 Gy. These results are a "
        "diagnostic map, not a replication-failure rate: the mapping is "
        "purposive, estimates no prevalence, and does not falsify any "
        "underlying theory.",
    ),
    ("fig", "fig_sensitivity"),
    ("table", "tab_audit"),
    ("h1", "Case 1: Fukushima evacuation and the low-dose risk function"),
    ("h2", "Policy problem and decision"),
    (
        "p",
        "After the March 2011 Fukushima Daiichi accident, Japanese "
        "authorities ordered mandatory evacuations affecting roughly "
        "{evac_pop_approx} residents. The decision traded modeled radiation "
        "risk against immediate and continuing harms of displacement under "
        "emergency conditions.",
    ),
    ("h2", "Assumed empirical relationship"),
    (
        "p",
        "Radiation protection defaults to linear no-threshold and related "
        "dose-response assumptions that project population risks at doses "
        "where direct epidemiological identification is difficult (ICRP, "
        "2007). Evacuation thresholds translate those risk assumptions into "
        "action.",
    ),
    ("h2", "Decision-relevant functional feature"),
    (
        "p",
        "The decision required the slope of the dose-response function in "
        "the low-dose range: whether incremental exposure below the "
        "well-observed range carries proportional risk justifying broad and "
        "sustained evacuation. This is an extrapolation problem - the "
        "feature mattered precisely where direct evidence is weakest.",
    ),
    ("h2", "Evidence in the relevant range"),
    (
        "p",
        "The preferred specification estimates two-way fixed-effects "
        "differences in log crude death rates, with municipality and year "
        "effects, excluding 2011 from the post-period average:",
    ),
    ("eq", "ln(CDR_it) = a_i + g_t + b D_it + e_it"),
    (
        "p",
        "Figure 4 plots pooled crude death rates. T1 municipalities show a "
        "sharp 2011 increase and a lower recorded rate than Fukushima "
        "controls through much of 2012-2019; the preferred difference-in-"
        "differences estimate is {t1_main_att} log points, approximately "
        "{t1_main_att_pct}% fewer recorded deaths than the counterfactual "
        "trend (permutation p {t1_main_perm_p}; pre-trend p "
        "{t1_main_pretrend_p}). Table 2 reports the specification grid and "
        "Figure 5 the preferred event study.",
    ),
    ("fig", "fig_pooled_cdr"),
    ("table", "tab_fuku_att"),
    ("fig", "fig_event_study"),
    (
        "p",
        "The negative post-2011 coefficient is not evidence that evacuation "
        "improved health. Displacement, selective return, registration "
        "practice, and population composition change who remains in the "
        "series and where deaths are recorded - the post-evacuation curve "
        "does not trace a stable population through exposure levels. The "
        "2011 decomposition is more informative: T1 municipalities recorded "
        "{t1_obs_2011} deaths against {t1_exp_2011} trend-expected, an "
        "excess of {t1_excess_2011}; direct disaster deaths account for "
        "{t1_direct_2011}, leaving a residual of {t1_resid_2011} (Figure 6) "
        "that cannot be wholly assigned to evacuation. Certified disaster-"
        "related deaths for Fukushima Prefecture total {ra_related_deaths} "
        "as of {ra_date} (Reconstruction Agency, {ra_year}; Fukushima "
        "Prefecture, 2014).",
    ),
    ("fig", "fig_acute"),
    (
        "p",
        "Table 3 places measured quantities beside published radiological "
        "projections - for example, Ten Hoeve and Jacobson's (2012) best "
        "estimate of {thj_best} worldwide cancer deaths (range {thj_range}) "
        "with {thj_averted_best} averted by evacuation (range "
        "{thj_averted_range}), alongside WHO (2013) and UNSCEAR (2014) "
        "quantities that differ in scope and construction. These estimands "
        "are not commensurate; juxtaposing them shows that the evacuation "
        "decision was highly sensitive to an assumed low-dose response while "
        "its consequences extended to outcomes the curve does not "
        "represent.",
    ),
    ("table", "tab_lnt"),
    ("h2", "Decision sensitivity"),
    (
        "p",
        "Plausible alternative low-dose shapes - linear, threshold, "
        "hormetic, supralinear - imply materially different optimal "
        "evacuation scope, duration, and priority. The policy was therefore "
        "decision-sensitive to a feature the evidence could not sharply "
        "identify: functional-form dependence in its clearest form.",
    ),
    ("h2", "Consequence asymmetry"),
    (
        "p",
        "Error costs are asymmetric on both sides. Acting on an overstated "
        "low-dose slope imposes displacement, mortality risk among "
        "vulnerable groups, and disrupted care; failing to act on a real "
        "slope imposes exposure harms. These harms fall on identifiable "
        "groups and are measured in different units, so no single fitted "
        "curve can settle the trade-off.",
    ),
    ("h2", "Reversibility and learning"),
    (
        "p",
        "Reversibility was limited: displacement and institutional "
        "disruption are partly irreversible, and mid-crisis learning "
        "architecture was thin. Yet the appraisal space was not binary. "
        "Zoning, assisted voluntary relocation, exemptions for medically "
        "fragile residents, continuity of care, time-limited orders, "
        "exposure monitoring, and staged return are adjustable design "
        "variables that perform differently across plausible risk "
        "functions. The case does not show that LNT is false, that "
        "evacuation was definitively wrong, or that non-evacuation outcomes "
        "are observed; it shows functional-form uncertainty under "
        "extrapolation combined with high consequence asymmetry and limited "
        "reversibility.",
    ),
    ("h1", "Case 2: Kansas tax reform and the fiscal response function"),
    ("h2", "Policy problem and decision"),
    (
        "p",
        "In 2012 Kansas enacted large income-tax cuts justified partly by "
        "claims that behavioral and growth responses would recover much of "
        "the static revenue loss (Kansas Legislature, 2012; Rothschild, "
        "2012).",
    ),
    ("h2", "Assumed empirical relationship"),
    (
        "p",
        "The justification invoked the Laffer curve - the proposition that "
        "revenue eventually declines as rates rise past a maximum (Laffer, "
        "2004). The policy-relevant claim was not that such a curve exists, "
        "but that Kansas's position, the local slope, and the dynamic "
        "growth response would make the reform close to self-financing.",
    ),
    ("h2", "Decision-relevant functional feature"),
    (
        "p",
        "The decision required the state's local position and the local "
        "slope of the revenue response, plus the timing and magnitude of any "
        "dynamic feedback - features that curve existence alone does not "
        "identify.",
    ),
    ("h2", "Evidence in the relevant range"),
    (
        "p",
        "Figure 7 compares Kansas with synthetic Kansas. After the reform, "
        "real individual income-tax revenue per capita averaged about "
        "{ks_iit_pct}% below the main synthetic counterfactual (permutation "
        "p = {ks_iit_perm_p}); the all-state pool implies "
        "{ks_iit_pct_all}%. The gap grew from roughly ${ks_iit_gap_2013} "
        "per capita in 2013 to ${ks_iit_gap_2016} in 2016, a cumulative "
        "counterfactual gap near ${ks_iit_cum_bn} billion in 2012 dollars. "
        "Real total tax revenue was {ks_tax_pct}% lower (p = "
        "{ks_tax_perm_p}); post-reform gaps were {ks_gdp_pct}% for real GDP "
        "per capita (p = {ks_gdp_perm_p}) and {ks_emp_pct}% for employment "
        "(p = {ks_emp_perm_p}). Table 4 reports donor pools, pre-period "
        "fit, in-time placebos, and leave-one-donor-out ranges "
        "({ks_iit_loo_min} to {ks_iit_loo_max} log points; pre-RMSPE "
        "{ks_iit_rmspe}).",
    ),
    ("fig", "fig_kansas"),
    ("table", "tab_kansas"),
    (
        "p",
        "The result is not a universal rejection of the Laffer curve, nor "
        "does Kansas disprove supply-side economics. Within this period and "
        "design, no macroeconomic response large enough to offset the "
        "revenue loss is observed. A decision-facing appraisal would have "
        "separated the static revenue loss, the taxable-income response, "
        "the activity effect, and the timing of any return to the base.",
    ),
    ("h2", "Decision sensitivity"),
    (
        "p",
        "Plausible local slopes and growth paths imply materially different "
        "budget trajectories; the reform was decision-sensitive to "
        "unverified response geometry.",
    ),
    ("h2", "Consequence asymmetry"),
    (
        "p",
        "Error costs were primarily fiscal - revenue loss and compressed "
        "services - and asymmetric against optimistic assumptions, but less "
        "severe in kind than irreversible health harms.",
    ),
    ("h2", "Reversibility and learning"),
    (
        "p",
        "Reversibility was comparatively greater: statutory changes are "
        "revisable, outcomes are observable on budget timescales, and "
        "staged rate changes, automatic review triggers, and sunset clauses "
        "were feasible learning architectures. Kansas's 2017 partial repeal "
        "illustrates correction after observation. The case shows "
        "functional-form uncertainty about local position and response "
        "geometry in a setting with comparatively greater reversibility and "
        "ongoing observability.",
    ),
    ("h1", "Comparative findings"),
    ("h2", "A common mechanism"),
    (
        "p",
        "Both cases required decision-relevant knowledge of relationship "
        "shape that exceeded what the available evidence clearly "
        "established. In each, a named canonical relationship supplied "
        "content - an evacuation threshold, an expected revenue recovery - "
        "that the evidence over the relevant range did not deliver. The "
        "mechanism is identical even though the cases share no dataset, "
        "institution, or political context.",
    ),
    ("h2", "Where the cases diverge"),
    (
        "p",
        "The cases differ on nearly every moderating dimension (Table 5). "
        "Fukushima's uncertainty was extrapolative - the relevant feature "
        "lay below the observed dose range - whereas Kansas's was about "
        "local position and dynamic response within a theoretically "
        "possible curve. Fukushima combined severe, two-sided consequence "
        "asymmetry with limited reversibility; Kansas carried primarily "
        "fiscal costs with far greater reversibility and rapid "
        "observability. These differences predict the different decision "
        "architectures each case called for.",
    ),
    ("table", "tab_synthesis"),
    ("h2", "Comparative propositions"),
    (
        "p",
        "The comparison supports three analytical propositions, stated as "
        "interpretive generalizations rather than statistically tested "
        "hypotheses. Proposition 1: functional-form uncertainty becomes "
        "policy-critical when plausible alternative shapes imply materially "
        "different actions - decision sensitivity, not statistical "
        "significance, is the threshold. Proposition 2: the decision cost "
        "of functional-form uncertainty increases when consequences are "
        "asymmetric and commitments are difficult to reverse. Proposition "
        "3: where policies are reversible and outcomes observable on useful "
        "timescales, adaptive implementation can partially substitute for "
        "ex ante functional-form certainty (Lempert & Collins, 2007; Walker "
        "et al., 2013).",
    ),
    ("h2", "Lesson-drawing"),
    (
        "p",
        "Comparative policy analysis distinguishes what can travel from "
        "what cannot (Rose, 1991; Dolowitz & Marsh, 2000). One lesson is "
        "transferable across domains: before acting on a named empirical "
        "relationship, identify the exact functional feature the decision "
        "requires and test whether it is identified in the relevant range. "
        "A second lesson is context-dependent: how much shape uncertainty "
        "can be tolerated depends on consequence asymmetry, reversibility, "
        "transportability, observational feedback, and institutional "
        "capacity to update. Non-transferable elements include numerical "
        "thresholds, effect sizes, sector-specific causal mechanisms, and "
        "institutional details - transporting those would repeat the "
        "functional-form error the article diagnoses.",
    ),
    ("h1", "Discussion"),
    ("h2", "Principal comparative finding"),
    (
        "p",
        "The principal finding is comparative, not only conceptual: the "
        "policy significance of uncertain functional form depends not only "
        "on how poorly the curve is identified but on how that uncertainty "
        "interacts with decision sensitivity, consequence asymmetry, "
        "reversibility, transportability, and opportunities for learning. "
        "Finding the same mechanism across maximum-contrast cases indicates "
        "that functional-form dependence is a general appraisal problem "
        "rather than an artifact of one policy field.",
    ),
    ("h2", "What comparison adds"),
    (
        "p",
        "A single case could show that shape uncertainty mattered; it "
        "could not show which conditions make it matter more. Comparison "
        "reveals that identical evidentiary weakness produces different "
        "decision risks: in Fukushima it argued for staged, revisable "
        "protection with safeguards for asymmetric harms, while in Kansas "
        "it argued for staged implementation with triggers and monitoring. "
        "The comparative design thereby converts a cautionary observation "
        "into an appraisal variable - the joint configuration of "
        "uncertainty and decision structure - that comparative policy "
        "research can examine across further settings.",
    ),
    ("h2", "Implications for comparative policy analysis"),
    (
        "p",
        "The framework complements causal identification and evidence "
        "hierarchies: a credible average contrast need not identify the "
        "feature the decision requires, and functional form can matter "
        "even inside causal designs (Roth & Sant'Anna, 2023). For "
        "comparative policy analysis, the study suggests treating the "
        "relationship between evidence structure and decision architecture "
        "as itself a dimension of comparison - alongside the more familiar "
        "comparisons of instruments, institutions, and outcomes (Howlett, "
        "2019; Hall, 1993; Freeman, 2006).",
    ),
    ("h2", "Limitations"),
    (
        "p",
        "The design has clear limits. Two purposively selected cases "
        "cannot support statistical generalization; the reconstruction is "
        "retrospective; the two empirical designs are heterogeneous; and "
        "policymakers' actual information sets are not fully observed. The "
        "50-relationship mapping is purposive and estimates no prevalence. "
        "Fukushima's municipal mortality is affected by displacement, "
        "registration, demographic change, and recording location, and "
        "non-evacuation outcomes are unobserved. Kansas's synthetic control "
        "cannot fully separate the reform from contemporaneous state-"
        "specific shocks. The analysis also stops short of a welfare "
        "analysis placing all consequences on a common scale, which would "
        "introduce further functional forms and normative weights.",
    ),
    ("h1", "Conclusion"),
    (
        "p",
        "Comparing Fukushima and Kansas shows that functional-form "
        "dependence is one mechanism with different policy implications "
        "under different configurations of uncertainty, consequence "
        "asymmetry, reversibility, transportability, and learning capacity. "
        "The comparative lesson for policy appraisal is to expose the "
        "decision-relevant shape, test decisions under plausible "
        "alternatives, and match the action architecture to the cost of "
        "being wrong - before commitments become difficult to reverse.",
    ),
    ("h1", "Data availability"),
    (
        "p",
        "All data used in the analyses are from public sources. Archived "
        "source files, acquisition metadata, processed datasets, analysis "
        "code, machine-readable results, and document-generation code will "
        "be supplied to reviewers through an anonymized archive. The public "
        "repository URL is provided to the editor in the title-page "
        "materials and will be added to the manuscript after double-"
        "anonymous review. The archive README records the commands required "
        "to reproduce the analyses and submission files.",
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
        "individual income-tax revenue per capita; panel (b) reports log GDP per capita. "
        "Synthetic controls use the main {ks_n_donors}-state donor pool. Shading marks "
        "2013-2017, between implementation and legislative reversal."
    ),
    "fig_policy_pathway": (
        "Figure 1. Comparative appraisal sequence for functional-form dependence. The "
        "same analytical sequence is applied to both cases: the empirical relationship, "
        "the decision-relevant shape, evidence in the policy range, decision sensitivity, "
        "consequence asymmetry, and reversibility and learning. Fukushima entries appear "
        "before the vertical bar; Kansas entries after it."
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
    "tab_synthesis": (
        "Table 5. Comparative summary of the two cases across the common dimensions. The "
        "cases are not statistically comparable; the final column states the comparative "
        "lesson each contrast supports."
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
        "Bennett, C. J., & Howlett, M. (1992). The lessons of learning: Reconciling "
        "theories of policy learning and policy change. Policy Sciences, 25(3), 275-294. "
        "https://doi.org/10.1007/BF00138786"
    ),
    (
        "Bertrand, M., Duflo, E., & Mullainathan, S. (2004). How much should we trust "
        "differences-in-differences estimates? Quarterly Journal of Economics, 119(1), "
        "249-275. https://doi.org/10.1162/003355304772839588"
    ),
    (
        "Boswell, C. (2009). The political uses of expert knowledge: Immigration policy "
        "and social research. Cambridge University Press."
    ),
    (
        "Burnham, K. P., & Anderson, D. R. (2004). Multimodel inference: Understanding "
        "AIC and BIC in model selection. Sociological Methods & Research, 33(2), 261-304. "
        "https://doi.org/10.1177/0049124104268644"
    ),
    (
        "Cairney, P. (2016). The politics of evidence-based policymaking. Palgrave "
        "Macmillan. https://doi.org/10.1057/978-1-137-51781-4"
    ),
    (
        "Cook, R. D. (1977). Detection of influential observation in linear regression. "
        "Technometrics, 19(1), 15-18. https://doi.org/10.1080/00401706.1977.10489493"
    ),
    (
        "Dolowitz, D. P., & Marsh, D. (2000). Learning from abroad: The role of policy "
        "transfer in contemporary policy-making. Governance, 13(1), 5-24. "
        "https://doi.org/10.1111/0952-1895.00121"
    ),
    (
        "Draper, D. (1995). Assessment and propagation of model uncertainty. Journal of "
        "the Royal Statistical Society: Series B, 57(1), 45-70. "
        "https://doi.org/10.1111/j.2517-6161.1995.tb02015.x"
    ),
    (
        "Freeman, R. (2006). Learning in public policy. In M. Moran, M. Rein, & R. E. "
        "Goodin (Eds.), The Oxford handbook of public policy (pp. 367-388). Oxford "
        "University Press."
    ),
    (
        "Fukushima Prefecture. (2014). Higashinihon daishinsai ni yoru higai jokyo sokuhou "
        "(dai 1260-ho) [Preliminary report on damage caused by the Great East Japan "
        "Earthquake (Report No. {fdr_no})]. {fdr_url}"
    ),
    (
        "George, A. L., & Bennett, A. (2005). Case studies and theory development in the "
        "social sciences. MIT Press."
    ),
    (
        "Hall, P. A. (1993). Policy paradigms, social learning, and the state: The case "
        "of economic policymaking in Britain. Comparative Politics, 25(3), 275-296. "
        "https://doi.org/10.2307/422246"
    ),
    (
        "Howlett, M. (2019). Designing public policies: Principles and instruments "
        "(2nd ed.). Routledge. https://doi.org/10.4324/9781315232003"
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
        "Morgan, M. G., & Henrion, M. (1990). Uncertainty: A guide to dealing with "
        "uncertainty in quantitative risk and policy analysis. Cambridge University "
        "Press."
    ),
    (
        "Parkhurst, J. O. (2016). Appeals to evidence for the resolution of wicked "
        "problems: The origins and mechanisms of evidentiary bias. Policy Sciences, "
        "49(4), 373-393. https://doi.org/10.1007/s11077-016-9263-z"
    ),
    (
        "Przeworski, A., & Teune, H. (1970). The logic of comparative social inquiry. "
        "Wiley."
    ),
    (
        "Reconstruction Agency. ({ra_year}). Higashinihon daishinsai ni okeru "
        "shinsai-kanrenshi no shisha-su [Number of disaster-related deaths in the Great "
        "East Japan Earthquake] (as of {ra_date}). {ra_url}"
    ),
    (
        "Rose, R. (1991). What is lesson-drawing? Journal of Public Policy, 11(1), 3-30. "
        "https://doi.org/10.1017/S0143814X00004918"
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
        "Walker, W. E., Haasnoot, M., & Kwakkel, J. H. (2013). Adapt or perish: A review "
        "of planning approaches for adaptation under deep uncertainty. Sustainability, "
        "5(3), 955-979. https://doi.org/10.3390/su5030955"
    ),
    (
        "Weimer, D. L., & Vining, A. R. (2017). Policy analysis: Concepts and practice "
        "(6th ed.). Routledge."
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
