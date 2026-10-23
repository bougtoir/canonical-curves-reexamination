# Hostile JCPA review (adversarial pre-submission review)

Simulated reviewers: (1) JCPA editor, (2) comparative policy scholar,
(3) quantitative policy analyst, (4) radiation/public-health domain
specialist, (5) public-finance economist.

## R1 — JCPA editor

1. Is this genuinely comparative, or a generic framework with two examples?
   - The manuscript contains an explicit Comparative research design section
     (case-selection logic, unit of comparison, eight common dimensions,
     evidence sources, inferential limits), a symmetric seven-subsection
     structure for each case, a dedicated Comparative findings section, a
     comparative table with a lesson column, propositions, and a
     lesson-drawing subsection. Comparison is the organizing device, not an
     appended paragraph.
2. Does it fit JCPA rather than a generic policy journal?
   - The question is comparative ("how does functional-form dependence enter
     policy decisions under different evidentiary, institutional, and
     consequence structures"); the literature engages lesson-drawing, policy
     transfer, and comparative design scholarship (Rose; Dolowitz & Marsh;
     Bennett & Howlett; George & Bennett; Hall; Freeman; Przeworski & Teune).
3. Word limit / format?
   - check_manuscript.py enforces <= 8,000 words (all-inclusive docx count),
     abstract <= 250 words, 5-6 keywords, APA references, double-anonymized
     manuscript with separate title page.

## R2 — Comparative policy scholar

1. Why these two cases? Isn't this just two anecdotes?
   - Selection logic is stated explicitly: maximum substantive contrast with
     a common decision-level mechanism. The design's permits/non-permits are
     enumerated (no prevalence, no statistical generalization from N = 2).
   - What comparison adds that neither case provides alone is argued
     directly: identical evidentiary weakness produces different decision
     risks depending on the uncertainty-consequence-reversibility
     configuration.
2. Is the comparison symmetric?
   - Both cases use identical subsections (policy problem; assumed
     relationship; decision-relevant feature; evidence in the relevant
     range; decision sensitivity; consequence asymmetry; reversibility and
     learning) and a common comparative table.
3. Is lesson-drawing justified?
   - Lessons are split into transferable, context-dependent, and
     non-transferable; numerical thresholds and sector mechanisms are
     explicitly excluded from transfer.

## R3 — Quantitative policy analyst

1. Is functional-form dependence just renamed model uncertainty?
   - The article distinguishes them explicitly: functional-form uncertainty
     is a form of model uncertainty about relationship shape; dependence is
     the decision-level condition in which that uncertainty changes the
     action. The propositions make the distinction operational (decision
     sensitivity, not statistical significance, is the threshold).
2. Are the case analyses sound?
   - Fukushima: DiD with permutation inference, pre-trend checks, synthetic
     controls, scope/weighting variants; Kansas: synthetic control with two
     donor pools, in-time placebos, LOO, neighboring-state event studies.
   - Estimand discipline is maintained: municipal mortality is not an
     evacuation-causal estimate; the Kansas gap is a local treatment effect.

## R4 — Radiation / public-health specialist

- The text does not claim LNT is false, that evacuation was definitively
  wrong, or that municipal mortality is a clean causal estimate. Uncertainty
  from registration, displacement, composition, and counterfactual
  unobservability is retained. Measured deaths, certified disaster-related
  deaths, and modeled radiological projections are kept as distinct,
  non-commensurate quantities (Table 3 caption enforces this).

## R5 — Public-finance economist

- The text does not claim the Laffer curve does not exist or that Kansas
  disproves supply-side economics. Theoretical curve existence, Kansas's
  local position, local slope, turning point, dynamic response, and fiscal
  outcome are distinguished as separate propositions.

## Resolved items

- 50-relationship mapping reduced to background motivation with calibrated
  interpretation (no prevalence claim, no "68% of theories failed"
  framing).
- Figure 1 redrawn as a comparative sequence with both cases mapped onto
  the same analytical steps.
- Table 5 rebuilt with an explicit Comparative lesson column.
