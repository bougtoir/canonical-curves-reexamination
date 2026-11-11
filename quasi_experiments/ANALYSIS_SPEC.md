# Quasi-experimental analysis specification

Two case studies evaluating policies justified by canonical curves whose
empirical support is fragile in the audit (Laffer: NOT_SIGNIFICANT; LNT:
NOT_SIGNIFICANT). Shared frame: canonical relationship -> policy adoption ->
real-world consequence. All numbers must be produced by scripts from the data in
`kansas/data/` and `fukushima/data/`; nothing hand-typed.

Common implementation: `common/synth.py` with

```python
def synthetic_control(Y: pd.DataFrame, treated: str, donors: list[str],
                      pre_years: list[int]) -> SCResult
    # Y: wide (index=year, columns=unit). Weights w >= 0, sum w = 1,
    # minimise pre-period RMSPE via scipy.optimize.minimize (SLSQP),
    # start from equal weights. No covariates (outcome-path matching only).
    # SCResult: weights (Series), synthetic (Series over all years), gaps,
    # rmspe_pre, rmspe_post, ratio = rmspe_post/rmspe_pre
def permutation_inference(Y, treated, donors, pre_years, post_years) -> DataFrame
    # run SC for treated and for every donor as pseudo-treated (donor pool =
    # other donors); return per-unit rmspe_pre, rmspe_post, ratio; p-value =
    # rank of treated ratio / (n_units).
def did_event_study(panel, unit, time, y, treated_flag, ref_year, weights=None,
                    cluster=unit) -> DataFrame
    # y ~ unit FE + year FE + sum_{t != ref} beta_t * 1[treated]*1[year==t]
    # statsmodels OLS with cluster-robust SE; optional analytic weights.
```

Use statsmodels/scipy/pandas (check installed; pip --user if missing).

## A. Kansas (Laffer -> 2012 Brownback tax cuts)

Data: `kansas/data/state_panel.csv`. Derived outcomes (per state-year):
- `ln_rgdp_pc` = log(rgdp*1e6 / (pop*1e3))  (check units of rgdp [millions
  of chained $] and pop [thousands] in SOURCES.md; adjust so per-capita is $).
- `ln_emp` = log(nonfarm_emp)
- `real_tax_pc` = tax_total*1e3 / (pop*1e3) / (cpi/cpi_2012)  (STC is in
  thousands of $; verify) ; `real_iit_pc` analogous with tax_indiv_inc.
- `ln_real_tax_pc`, `ln_real_iit_pc`.

Treatment: Kansas, first treated fiscal/calendar year 2013 (SB 2012 HB 2117
effective 2013-01-01). Reversal: SB 30 enacted 2017-06-06, effective tax year
2017 (retroactive); define post-reversal = 2018+.
Pre-period: 1997-2012. Post-period main: 2013-2017. Extension: 2018-2019
(exclude 2020+ from main estimates; report as descriptive).

Donor pools:
- `main`: 48 contiguous states + DC minus KS, minus states with major
  personal-income-tax rate changes 2012-2017 (NC, OK, WI, OH, ME, IN, ND) and
  minus states with no broad-based income tax (TX, FL, WA, NV, SD, WY, AK, NH,
  TN) -- record the list in results.
- `all`: every unit except KS (robustness).
- `neighbors` (DiD only): NE, MO, CO, IA (OK excluded, see above).

Analyses (each written to `kansas/results/`):
1. SC per outcome (4 outcomes) with `main` pool: weights, path figure
   (Kansas vs synthetic, vertical lines 2013 and 2017/18), gap figure, post-2013
   mean gap 2013-2017, permutation p-value, ratio-rank figure. Repeat with
   `all` pool (table only).
2. In-time placebo: pseudo-treatment 2005 using pre 1997-2004, report gap
   2005-2012 (should be ~0).
3. Leave-one-out donor robustness: drop each donor with weight > 0.05 and refit;
   report range of post-2013 mean gap.
4. DiD event study (unit+year FE, treated = KS, ref 2012), pools `neighbors`
   and `main`, outcomes ln_rgdp_pc, ln_emp, ln_real_tax_pc, ln_real_iit_pc;
   coefficient plot 2005-2019.
5. Revenue counterfactual: cumulative (Kansas real_tax_pc - synthetic) x pop,
   2013-2017, in 2012 dollars; and same for individual income tax.

Output: `kansas/results/sc_summary.csv` (outcome, pool, post_mean_gap,
pct_gap, perm_p, rmspe_pre, n_donors), `did_event_study.csv`,
`sc_weights_<outcome>.csv`, `placebo_in_time.csv`, `loo_robustness.csv`,
`revenue_counterfactual.csv`; figures PNG (English labels) in
`kansas/figures/`.

## B. Fukushima (LNT -> evacuation orders after 2011-03-11)

Data: `fukushima/data/municipal_panel.csv`, `evacuation_orders.csv`,
`census_age_structure.csv`, `reconstruction_related_deaths_fukushima.csv`.

Outcome: crude death rate `cdr` = 1000*deaths/pop and `ln_cdr`.
Denominator caveat: register population (住基) retains evacuees' residence,
and deaths are tabulated by registered address -> numerator and denominator
are consistent for evacuated municipalities; state this in Methods.
Pre-2013 pop covers Japanese residents only (use `pop_scope`); the change is
small in these rural municipalities but note it; robustness: interpolate
2012->2013 log-ratio adjustment (report both).

Sample: the all-unit universe is the municipality codes present in the 2019
panel year. Complete-case estimation uses those codes observed with
non-missing deaths and population for every year from 2005 through 2019.
Dropped 2019 codes are classified as population missing in at least one year
or not observed under a single code over 2005-2019; the full list, including
missing years, is written to `dropped_units.csv`. From the complete-case
sample, remove T1 and T2 municipalities from the control pool. From the
remaining complete-case units, exclude every municipality with mass-casualty
tsunami exposure, defined as
`deaths_2011 / mean(deaths_2006..2010) > 1.20`; the exact excluded units and
ratios are written to `control_exclusions.csv`. Treated municipalities keep
their 2011 value but 2011 is excluded from ATT (direct-disaster year).

Treatment groups (from evacuation_orders.csv):
- `T1` primary: municipalities with 警戒区域 or 計画的避難区域 on
  2011-04-22 (10: 双葉,大熊,富岡,浪江,楢葉,葛尾,飯舘,川内,南相馬,川俣).
- `T1w` whole-municipality subset per official scope (双葉,大熊,富岡,飯舘).
- `T2` 緊急時避難準備区域 only (広野, 田村).
Post-period main: 2012-2019 (COVID years excluded from main; 2020-2022
reported descriptively). Pre: 2006-2010; ref year 2010. Year 2005 is
retained only for descriptive plots because several municipality counts are
partial-year after mergers.

Analyses (`fukushima/results/`):
1. Descriptive: pooled CDR of T1 (sum deaths / sum pop) vs pooled control
   2000-2022, with 2011 marked.
2. DiD event study on ln_cdr, unit+year FE, treated x year, ref 2010,
   pop-weighted, cluster by municipality, control pool = all eligible
   non-evacuated municipalities in 8 prefectures; also control = Fukushima
   prefecture only; also unweighted. Age-structure control: interact
   share_65plus (2010 census) with year FE (i.e. add share65*year dummies) as
   a robustness spec.
   For every treatment x control-pool x weighting specification, draw 1,000
   random pseudo-treated sets of the same size from eligible controls (seed
   20260918). Report two-sided ATT randomization p-values and pre-trend
   randomization p-values based on the sum of squared 2006-2009 event
   coefficients. Cluster standard errors and Wald tests remain secondary
   diagnostics.
3. ATT 2012-2019 (single post dummy DiD) for T1, T1w, T2, with 95% CI, in log
   points and translated to excess deaths = sum over treated unit-years of
   pop * cdr_counterfactual*(exp(beta)-1)/1000. Report total and per year.
4. Synthetic control per T1 municipality (donor = eligible controls in
   Fukushima prefecture with pop within [0.25x, 4x] of the treated unit's 2010
   pop and 2010 share_65plus within +/-0.10), pre 2006-2010. Aggregate T1
   donors use the same Fukushima-only eligibility and compare share_65plus to
   the pooled T1 share. Report donor counts, pre/post RMSPE, and permutation
   p-value. If pre-RMSPE is below 1e-4, fit weights on 2006-2008 and evaluate
   2009-2010 as a leave-half-out cross-fit in sc_crossfit.csv.
   RMSPE-ratio permutation p per unit, and pooled T1 aggregate SC. Figures
   for the aggregate and a small-multiples panel for 10 units.
5. DiD placebo: pseudo-treatment 2008 using 2005-2010; this short-window
   diagnostic is reported with an explicit weakness note. The in-time
   synthetic-control placebo is omitted.
6. Compare excess deaths with (a) Reconstruction Agency 震災関連死 counts for
   the same municipalities (data file), and (b) LNT-projected radiation
   deaths averted -- do NOT compute your own dose estimate; leave a placeholder
   table `lnt_comparison.csv` with columns (quantity, value, source) filled
   only with values that have a documented source URL/DOI in SOURCES.md
   (WHO 2013 Health Risk Assessment; UNSCEAR 2013/2020 report; Waddington et
   al. 2017 Process Safety and Environmental Protection 112:16-49 J-value
   analysis; ten Hoeve & Jacobson 2012 Energy Environ Sci 5:8743). If you
   cannot verify a number against the source text, leave the row out.

Output: `did_event_study.csv`, `att_summary.csv`, `excess_deaths.csv`,
`sc_unit_summary.csv`, `sc_aggregate.csv`, `placebo_in_time.csv`,
`control_exclusions.csv`, `sample_summary.json`; figures PNG (English).

## C. Reproducibility

`quasi_experiments/Makefile` with targets `kansas`, `fukushima`, `all`
running acquisition (skippable if raw exists) then analysis. `requirements.txt`
listing pinned packages actually used.

The Policy Sciences manuscript package is reproducible from the analysis outputs:

```bash
make all
make manuscript
```

The `manuscript` target rebuilds `numbers.json`, English figures, editable
tables and figures, the two manuscript DOCX variants, title page, cover
letter, submission statements, and then runs `manuscript/check_manuscript.py`.
The checker writes `manuscript/check_report.md` and exits nonzero on
structural, anonymization, numerical, or journal-format validation failures.
