# Hostile pre-submission review: Policy Sciences

Date: 2026-10-01

Scope: manuscript, statistical design, figures and tables, reproducibility, and
claim calibration. Severity describes the likely editorial consequence before
the recorded response.

## Final finish-pass re-review

### Highest priority: mandatory before submission

No unresolved item. The abstract now identifies 34 of 50 as the result of a
deliberately common study diagnostic; the framework figure appears before the
mapping and empirical demonstrations; and the manuscript distinguishes broader
model uncertainty, shape-specific functional-form uncertainty, and
decision-level functional-form dependence.

### High priority

No unresolved item. Fukushima retains the non-causal municipal-mortality
interpretation and all LNT, evacuation, migration, registration, and
non-evacuation safeguards. Kansas retains the distinction between a possible
Laffer curve and Kansas's unidentified local position, slope, turning point,
dynamic response, and timing.

### Medium priority

No unresolved item. Figure numbering, first citation, inline placement,
separate-figure placeholders, captions, PNG/TIFF filenames, and editable PPTX
slide order are internally consistent after moving the framework from Figure 7
to Figure 1.

### Optional

The additional analyses listed in the final table remain future work. They
would change the frozen analysis and are not required for the article's stated
diagnostic contribution.

## Highest priority: mandatory before submission

| Criticism | Domain | Severity | Revision benefit | Feasibility | Resolution |
|---|---|---:|---:|---:|---|
| The article could be read as claiming that functional-form uncertainty is a new discovery, although econometrics, model uncertainty, and robust decision research already study it. | Manuscript / novelty | Desk-reject potential | High | Existing literature | Resolved. The contribution is now an organizing, decision-facing concept: it identifies when a shape is load-bearing for a policy action rather than claiming discovery of functional-form sensitivity. |
| The cross-domain count could be mistaken for a prevalence estimate or a claim that 68% of canonical theories are false. | Claims / statistical design | Desk-reject potential | High | Existing analysis | Resolved. The inventory is explicitly purposive, relationship-dataset pairs are not independent studies, and the exercise is described as a diagnostic map rather than a prevalence estimate or field ranking. |
| The negative Fukushima post-2011 coefficient could be misreported as an evacuation health benefit or causal mortality effect. | Causal inference / claims | Major-revision potential | High | Existing data | Resolved. The estimand is defined as recorded municipal deaths relative to a counterfactual trend. The text foregrounds displacement, registration, selective return, denominator change, death location, and the absence of an observed non-evacuation counterfactual. |
| The Fukushima denominator changes definition during the preferred post-period, and the tsunami exclusion and treatment boundary are analyst choices. | Statistical design / measurement | Major-revision potential | High | Existing data | Resolved by explicit limitation. The manuscript states that resident-register counts change from Japanese residents through 2012 to total residents from 2013, notes what year effects can and cannot absorb, and identifies the treatment and inundation boundaries as non-random design choices. |
| Measured deaths, certified disaster-related deaths, and modeled LNT quantities could appear to be commensurate or additive. | Radiation-risk interpretation / claims | Major-revision potential | High | Existing evidence | Resolved. They are labeled as different estimands and are placed together only to compare construction, scope, and decision relevance. The manuscript does not claim that LNT is false or that evacuation was definitively wrong. |
| The Kansas findings could be read as disproving the Laffer curve in general or isolating the causal contribution of every provision. | Causal inference / claims | Major-revision potential | High | Existing data | Resolved. The general existence proposition is separated from the Kansas-specific local offset claim. The estimand is a post-reform Kansas-versus-synthetic gap, and aircraft, agriculture, oil, concurrent policy, and donor restrictions remain explicit limitations. |
| A double-anonymous submission could reveal identity through the manuscript, appendix, document metadata, or repository URL. | Submission compliance | Desk-reject potential | High | Immediate | Resolved. The main manuscript and appendix are anonymized, including core properties. Identity and the public repository URL are confined to editorial files. |
| The submission could omit required Data Availability and generative-AI disclosures. | Submission compliance | Desk-reject potential | High | Immediate | Resolved. Both statements are present; the human author retains responsibility and the stated AI use does not assign authorship. |
| Persistent source snapshots lacked per-file checksums, sizes, timestamp precision, acquisition conditions, and usage-term fields. | Reproducibility | Major-revision potential | High | Existing files | Resolved for 49 cross-domain inputs and 538 Kansas and Fukushima archived files. Machine-readable manifests verify every current file and disclose that exact historical request times were not retained; the first repository commit is recorded as a timestamp proxy instead of fabricating precision. One unused legacy Fukushima workbook has unavailable source metadata and is labeled as unused by the current analysis. |

## High priority

| Criticism | Domain | Severity | Revision benefit | Feasibility | Resolution |
|---|---|---:|---:|---:|---|
| A common quadratic test is too narrow to adjudicate thresholds, splines, monotone nonlinearities, and mechanistic forms across heterogeneous disciplines. | Statistical design | Major-revision potential | High | Partial with existing data | Addressed as a design limit. The common screen is intentionally austere and inspectable; failure is not interpreted as linearity or absence. A full domain-specific model search would be a different study. |
| Significance-based categories and multiple relationship checks could invite dichotomous or multiplicity-insensitive interpretation. | Statistical design | Major-revision potential | Medium-high | Existing analysis | Addressed. Classification also uses influence, prediction, and information criteria; alpha and Cook-removal sensitivity spans 60-74% non-passing. The count is descriptive and is not presented as simultaneous confirmatory inference. |
| Fukushima municipal crude death rates cannot follow a stable cohort and may be dominated by migration and registration processes caused by treatment. | Statistical design | Major-revision potential | High | Additional individual data required | Retained as an identification limit and used to motivate the framework. No biological dose-response or individual health effect is inferred from the municipal series. |
| The Fukushima pre-trend test has low power with few treated municipalities and does not prove parallel trends. | Statistical design | Major-revision potential | Medium | Existing data cannot eliminate | Addressed by calibrated wording, event-study display, permutation inference, alternative control pools, treatment-scope checks, age controls, and synthetic-control results. No claim of proven parallel trends is made. |
| Kansas synthetic-control inference is discrete with 33 main donors and may be sensitive to donor restrictions and state-specific shocks. | Statistical design | Major-revision potential | High | Existing analysis | Addressed through all-state and restricted pools, permutation tests, leave-one-donor-out checks, in-time placebos, and neighboring-state event studies. The p-value and donor count are reported rather than described as generic strong significance. |
| The empirical demonstrations do not estimate the causal effect of policymakers believing a canonical curve. | Manuscript / focus | Major-revision potential | High | New historical design required | Addressed by narrowing the claim. The cases isolate a load-bearing proposition within a multi-causal policy rationale; they do not provide a monocausal model of policy adoption. |
| Reproducibility claims could exceed what an independent reviewer can verify if source snapshots, software versions, generated numbers, and package contents are not checked together. | Reproducibility | Major-revision potential | High | Existing materials | Resolved through pinned requirements, code-generated manuscript values, checksum manifests, a full analysis/build/check/package command sequence, and automated document and package validation. |

## Medium priority

| Criticism | Domain | Severity | Revision benefit | Feasibility | Resolution |
|---|---|---:|---:|---:|---|
| Figure 3 may overemphasize a headline share from a purposive inventory. | Figures / claims | Major-revision potential | Medium | Existing outputs | Retained because it displays sensitivity rather than a single estimate. The caption and text state that it maps a selected inventory and is not a population prevalence estimate. |
| Figures 4-6 may visually invite a causal Fukushima narrative despite the measurement caveats. | Figures / claims | Major-revision potential | Medium | Existing outputs | Addressed by defining recorded municipal mortality in text and captions, excluding 2011 from the post-period average, separating acute decomposition from post-period estimates, and placing interpretive caveats adjacent to the figures. |
| Figure 7 may encourage readers to attribute the entire Kansas gap to taxes. | Figures / claims | Major-revision potential | Medium | Existing outputs | Addressed by defining the synthetic-control gap as conditional on pre-fit and donor restrictions and by discussing contemporaneous shocks and the distinction among mechanical revenue loss, behavioral response, economic activity, and timing. |
| The conceptual Figure 1 could seem normative without an operational decision rule. | Framework / figures | Major-revision potential | Medium | Existing text | Addressed with a linked-layer definition, a decision-table procedure, candidate-model-set discipline, materiality tied to the action rule, and explicit reversibility and monitoring triggers. |
| No common welfare scale is used for mortality, displacement, revenue, growth, and distribution. | Claims / policy analysis | Major-revision potential | Medium | Normative data and judgments required | Retained deliberately. The article explains that aggregation would add unacknowledged functional forms and value weights; it calls for transparent stakeholder and distributional analysis instead. |
| The framework may overlap conceptually with robustness, resilience, model averaging, and scenario analysis. | Manuscript / novelty | Major-revision potential | Medium | Existing literature | Addressed by distinguishing decision dependence from global model fit and by separating ex ante robustness from ex post resilience. |

## Optional

| Criticism | Domain | Severity | Revision benefit | Feasibility | Proposed future work |
|---|---|---:|---:|---:|---|
| Re-estimate every mapped relationship with splines, generalized additive models, monotonic constraints, and domain-specific mechanistic forms. | Statistical design | Minor | Medium | Large new analysis | Reserve for a follow-up domain-specific study; it would change the present common-screen design. |
| Link Fukushima individuals across residence, dose, evacuation pathway, morbidity, and place of death. | Statistical design | Minor for current claim | High | New restricted data | Required for individual health-effect inference, which the present article does not claim. |
| Decompose Kansas effects by statutory provision, distributional incidence, public-service response, and sector. | Statistical design | Minor for current claim | High | New fiscal microdata | Valuable follow-up; not required for the narrower functional-form demonstration. |
| Elicit stakeholder-specific consequence weights and decision thresholds. | Policy design | Minor | Medium-high | New participatory study | Apply the framework prospectively in a future policy appraisal. |

## Review conclusion

No unresolved criticism judged likely to cause desk rejection or mandatory major
revision remains within the article's stated scope. Remaining high-priority
limitations require individual-level Fukushima data, a different Kansas
identification design, or a domain-specific reanalysis of all mapped
relationships; the manuscript now states those limits rather than implying that
the current evidence resolves them.
