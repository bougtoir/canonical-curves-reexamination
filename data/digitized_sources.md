# Digitized / transcribed source data

Curves whose data cannot be fetched from a public API are taken directly from the
original published figure/table. Each entry records the paper, DOI, the specific
table/figure, and how the values were obtained. Values are transcribed exactly as
published (no rounding beyond the source) or extracted from the figure with
WebPlotDigitizer. These are stored in `data/*_real.csv` and read by
`scripts/data_additional_real.py`.

## #21 BMI-Mortality J-Curve — `bmi_mortality_real.csv`
- Source: The Global BMI Mortality Collaboration (2016). "Body-mass index and
  all-cause mortality: individual-participant-data meta-analysis of 239
  prospective studies in four continents." Lancet 388(10046):776-786.
  DOI: 10.1016/S0140-6736(16)30175-1 (Open Access, CC BY).
- Values: primary prespecified analysis — never-smokers without chronic disease
  at baseline, excluding the first 5 years of follow-up; study/age/sex-adjusted
  hazard ratios relative to BMI 22.5-<25.0 kg/m². The nine finer BMI groups and
  their HRs (95% CI) are stated verbatim in the Abstract/Findings and Table 2.
- Transcription (not figure digitization): HRs read from the reported numbers.
- x = BMI category midpoint (kg/m²); y = all-cause mortality hazard ratio.

## #36 Ebbinghaus Forgetting Curve — `ebbinghaus_real.csv`
- Source: Ebbinghaus H (1885) "Über das Gedächtnis" / Ruger & Bussenius (1913)
  translation "Memory: A Contribution to Experimental Psychology", Chapter VII,
  Sections 28-29 (public domain). Transcribed from the original savings table
  (verifiable at Wikisource and psychclassics.yorku.ca/Ebbinghaus/memory7.htm).
- Values (X = hours after learning, Q = % savings retained):
  0.33h→58.2, 1h→44.2, 8.8h→35.8, 24h→33.7, 48h→27.8, 144h→25.4, 744h→21.1.
- x = log(time in hours); y = retention (savings %). Not extrapolated — exactly
  the 7 intervals Ebbinghaus reported.

## #29 Species-Area Curve — `species_area_real.csv`
- Source: M. P. Johnson & P. H. Raven (1973) "Species number and endemism: The
  Galápagos Archipelago revisited." Science 179(4076):893-895. Distributed as the
  `gala` dataset in the R `faraway` package (extracted from the CRAN source
  tarball `faraway/data/gala.rda`).
- 30 Galápagos islands: island area (km²) and number of plant species.
- x = log₁₀(Area, km²); y = log₁₀(Species). Replaces the previous invented
  "representative" bird-species counts for Caribbean/global islands.

## #41 Kleiber's Law — `kleiber_real.csv`
- Source: AnAge database, build 14 (Human Ageing Genomic Resources; Tacutu et
  al. 2018 Nucleic Acids Res 46:D1083-D1090), fields "Metabolic rate (W)" and
  "Body mass (g)", downloaded from https://genomics.senescence.info/species/.
- Restricted to Class Mammalia with both fields present and >0 → 422 species.
  Body mass converted g→kg. This is a modern real-data test of Kleiber's law
  (not Kleiber's 1932 domestic-animal table, whose scanned original is not
  reliably machine-readable); the source is labelled accordingly.
- x = log₁₀(Body mass, kg); y = log₁₀(BMR, W). Replaces 22 hand-entered values.

## #45 Duverger's Law — `duverger_real.csv`
- Source: Nils-Christian Bormann & Matt Golder, Democratic Electoral Systems
  (DES) dataset, version 5.0 (Bormann & Golder 2022 Electoral Studies 78;
  Bormann & Kaftan 2024 Open Research Europe 4:73). Downloaded
  `es_data-v50.zip` from https://mattgolder.com/elections.
- Legislative elections with tier-1 average district magnitude and effective
  number of electoral parties (enep, Laakso-Taagepera) both present → 1660
  elections. Replaces 30 hand-entered country values.
- x = log(district magnitude + 1); y = effective number of electoral parties.

## #2 Laffer Curve — `laffer_real.csv`
- Sources (OECD, latest common year = 2022 cross-section, matched on ISO3):
  - x = top (statutory) personal income tax rate: OECD Tax Database, Table I.7
    ("Top statutory personal income tax rates"), series TAX=PERS_ITAX (combined
    central + sub-central), fetched from the OECD SDMX-JSON endpoint
    (dataset TABLE_I7).
  - y = total tax revenue as % of GDP: OECD Global Revenue Statistics
    (Data Explorer dataflow DSD_REV_COMP_GLOBAL@DF_RSGLOBAL; MEASURE=TAX_REV,
    SECTOR=S13 general government, STANDARD_REVENUE=_T total tax,
    UNIT_MEASURE=PT_B1GQ % of GDP).
- 29 OECD countries with both variables for 2022. Replaces the previous
  26 hand-transcribed OECD-2022 values (which mixed years/definitions, e.g. a
  central-only US top rate and older tax-revenue figures).
- x = top marginal PIT rate (%); y = total tax revenue (% of GDP).

## #11 Great Gatsby Curve — `great_gatsby_real.csv` (reconstruction)
- This is a modern public-data RECONSTRUCTION, not a replication of Corak's
  (2013) original figure. Matched on ISO3.
  - y = intergenerational income elasticity (IGE, father-son): World Bank
    Global Database on Intergenerational Mobility (GDIM), income mobility
    dataset (Munoz, Ercio & Roy van der Weide 2025, "Intergenerational income
    mobility around the world: A new database", WB Policy Research WP 11166),
    file `IGE_Munoz_VanderWeide_June2025.dta` (87 economies). Downloaded from
    the WB Development Data Hub (dataset 0066878).
  - x = Gini index: Our World in Data `economic-inequality-gini-index`
    (source: World Bank Poverty and Inequality Platform), most recent year
    2000-2022 per country, rescaled to 0-100.
- 83 economies with both variables. Replaces 23 hand-entered Gini/IGE values.
- IGE per-country literature source is retained in the CSV (`ige_source`).

## #32 HANPP vs Development — `hanpp_real.csv` (zonal aggregation of grids)
- Source: Haberl, H., K.-H. Erb, F. Krausmann, V. Gaube, A. Bondeau, C. Plutzar,
  S. Gingrich, W. Lucht & M. Fischer-Kowalski (2007) "Quantifying and mapping
  the human appropriation of net primary production in Earth's terrestrial
  ecosystems." PNAS 104(31):12942-12947 (doi:10.1073/pnas.0704243104).
- Haberl 2007 does NOT publish a country-level HANPP table — only gridded data
  (year 2000) and regional aggregates. Country values here are COMPUTED by
  zonal aggregation of the official 5-arc-minute grids from the Global HANPP
  Data package (all_grids.zip):
    country HANPP% = 100 * Σ(HANPP_gCm2 · area) / Σ(NPP0_gCm2 · area)
  over the country's land cells (cos-latitude area weights), using grids
  `thanpppallgcm` (HANPP, gC/m²/yr) and `tn0_all_gcm` (NPP0, gC/m²/yr).
  Country boundaries: Natural Earth 1:110m admin-0 (ISO_A3).
- x = GDP per capita PPP (OWID / World Bank), year 2000, matched on ISO3.
- 156 countries. Replaces 25 hand-entered HANPP/GDP values. Negative HANPP for
  a few arid, heavily-irrigated countries (e.g. EGY, Gulf states) is a genuine
  result of the aggregation (NPP0 near zero), retained rather than dropped.

## #48 Putnam Social Capital — `putnam_real.csv` (European proxy)
- PROXY reconstruction (not a replication of Putnam's US-community measures),
  matched on ISO3:
  - x = daily time watching television and video (hours): Eurostat Harmonised
    European Time Use Surveys (HETUS), dataset `tus_00age`, activity code
    AC82 "Television and video", unit TIME_SP (mean time, total sex/age),
    most recent survey round per country (2000 or 2010).
  - y = generalized trust (% agreeing "most people can be trusted"): Our World
    in Data `self-reported-trust-attitudes` (World Values Survey / integrated
    surveys), value from the year nearest the TV survey (recorded per row).
- 22 European countries. Replaces 25 hand-entered TV-hours/trust values.
  Coverage is European only; labelled as a proxy, not a Putnam replication.

## #27 Replacement Migration Curve — `replacement_migration_real.csv` (UN model output, transcribed)
- Source (values are UN MODEL OUTPUTS, not empirical observations):
  United Nations, Population Division (2000/2001) "Replacement Migration: Is
  It a Solution to Declining and Ageing Populations?" (ST/ESA/SER.A/206).
  PDF: https://www.un.org/development/desa/pd/sites/www.un.org.development.desa.pd/files/files/documents/2020/Jan/un_2001_replacementmigration.pdf
- Transcribed exactly from two report tables:
  - x = TFR gap = 2.1 - TFR(1995-2000), TFR from Table IV.1 "Total fertility
    rates, 1950 to 2050" (p.23), column 1995-2000 (based on the UN 1998
    Revision medium variant).
  - y = Table IV.6 "Average annual net number of migrants between 2000 and
    2050, per million inhabitants in 2000" (p.25), Scenario IV = migration
    required to keep the working-age population (15-64) constant.
- 8 study countries (France, Germany, Italy, Japan, Republic of Korea, Russian
  Federation, United Kingdom, United States). The two regional aggregates
  (Europe, European Union) are stored in the CSV but excluded from the curve
  to avoid double-counting member countries. Replaces 25 hand-invented values
  (the UN report only studied 8 countries + 2 regions).

---
# User-supplied figures (batch, 12 sources) — digitized/transcribed 2026-07

Method note: these were extracted from the published figure/table supplied by
the author. Figure curves were read against the printed axis ticks from a
high-resolution (≥300 dpi) render of the source page; where the paper states
exact anchor values in the text, those were used to pin the curve. Point-level
uncertainty is roughly ±1 minor tick unless noted. Each entry states whether
the value is a text/table transcription (exact) or a figure reading
(digitized, approximate). Small-N sources are analysed as-is and several return
NOT_SIGNIFICANT/INSUFFICIENT_DATA — the source values are kept unchanged even
when they do not reproduce the textbook shape.

## #16 Linear No-Threshold (LNT) — `lnt_real.csv`
- Source: Ozasa K et al. (2012) "Studies of the mortality of atomic bomb
  survivors, Report 14, 1950-2003: an overview of cancer and noncancer
  diseases." Radiat Res 177(3):229-243. DOI: 10.1667/RR2629.1. LSS Report 14.
- Figure: Fig. 4, excess relative risk (ERR) of solid-cancer mortality vs
  weighted colon dose (Gy). ERRATUM applied: the published erratum corrects the
  ERR=0 point printed at 0.5 Gy to 0.05 Gy; the corrected figure is used.
- x = weighted colon dose (Gy); y = ERR. Figure reading (approximate), N=21.

## #22 Alcohol-Mortality J-Curve — `alcohol_mortality_real.csv`
- Source: Di Castelnuovo A et al. (2006) "Alcohol dosing and total mortality in
  men and women: an updated meta-analysis of 34 prospective studies." Arch
  Intern Med 166(22):2437-2445. DOI: 10.1001/archinte.166.22.2437.
- Figure: pooled dose-response (fixed-effects) curve, relative risk of
  all-cause mortality vs alcohol intake (g/day). Figure reading (approximate),
  N=17. J-shape (nadir ~6 g/day).

## #17 Fries Compression of Morbidity — `fries_real.csv`
- Source: Fries JF (1980) "Aging, natural death, and the compression of
  morbidity." N Engl J Med 303(3):130-135. DOI: 10.1056/NEJM198007173030304.
- Figure: Fig. 2 idealized US 1980 survival curve, % surviving vs age.
- NOTE (variable-definition change, author-approved): the previous
  implementation used "year vs years of morbidity before death", which does not
  correspond to any figure/table in Fries 1980. The digitized data follow the
  paper's actual Fig. 2 (age vs % surviving). x = age (years); y = % surviving.
  Figure reading (approximate), N=17.

## #18 Barker Hypothesis — `barker_real.csv`
- Source: Osmond C, Barker DJP, Winter PD, Fall CHD, Simmonds SJ (1993) "Early
  growth and death from cardiovascular disease in women." BMJ 307:1519-1524.
  DOI: 10.1136/bmj.307.6918.1519.
- Tables I-II: standardised mortality ratios (SMR) for all cardiovascular
  disease by birth weight, women and men. TABLE TRANSCRIPTION (exact), N=12.
- x = birth weight (kg, category midpoint); y = SMR (all CVD).
- FINDING: the transcribed data are monotonically DECREASING in birth weight;
  the high-birth-weight up-turn (U-shape) that the previous hard-coded array
  contained is NOT present in Osmond & Barker 1993. Verdict: NOT_SIGNIFICANT.
  The canonical "U-shape" label is not supported by this source.

## #20 Wilkinson Curve — `wilkinson_real.csv`
- Source: Wilkinson RG (1992) "Income distribution and life expectancy." BMJ
  304:165-168. DOI: 10.1136/bmj.304.6820.165.
- Figure: Fig. 2, life expectancy vs % of income received by the least
  well-off 70% of families, 9 OECD countries. Figure reading (approximate),
  N=9. x = income share to least well-off 70% (%); y = life expectancy (yr).

## #38 Dunning-Kruger Effect — `dunning_kruger_real.csv`
- Source: Kruger J, Dunning D (1999) "Unskilled and unaware of it..." J Pers
  Soc Psychol 77(6):1121-1134. DOI: 10.1037/0022-3514.77.6.1121.
- Figures 1-4 (Studies 1-4): perceived ability vs actual performance quartile.
  Figure reading (approximate), 4 quartiles × 4 studies = N=16.
- x = actual performance (percentile); y = perceived ability (percentile).

## #51 Micronutrient U-shape (Vitamin D) — `vitamin_d_real.csv`
- Source: Durup D et al. (2012) "A reverse J-shaped association of all-cause
  mortality with serum 25-hydroxyvitamin D in general practice: the CopD
  study." J Clin Endocrinol Metab 97(8):2644-2652. DOI: 10.1210/jc.2012-1176.
- Figure: Fig. 1A, central restricted-cubic-spline hazard ratio for all-cause
  mortality vs serum 25(OH)D (nmol/L), reference 50 nmol/L. Anchor HRs from the
  Abstract (10 nmol/L→2.13; 140 nmol/L→1.42). Figure reading (approximate),
  N=16. x = serum 25(OH)D (nmol/L); y = hazard ratio. Reverse-J.

## #52 Body Weight Set-Point — `body_weight_setpoint_real.csv`
- Source: Leibel RL, Rosenbaum M, Hirsch J (1995) "Changes in energy
  expenditure resulting from altered body weight." N Engl J Med 332(10):621-628.
  DOI: 10.1056/NEJM199503093321001.
- Figure: Fig. 2, mean observed-minus-predicted total energy expenditure
  (kcal/day) at +10% gain, initial weight, return to initial, -10% and -20%.
- NOTE (variable-definition change): the previous implementation used an
  invented "caloric change vs weight change" linear array. The digitized data
  follow the paper's Fig. 2 (metabolic compensation opposing weight change).
  x = body-weight change (%); y = observed-minus-predicted TEE (kcal/day).
  Figure reading (approximate), N=5 → INSUFFICIENT_DATA.

## #24 Bongaarts-Feeney Tempo Effect — `bongaarts_feeney_real.csv`
- Source: Bongaarts J, Feeney G (1998) "On the quantum and tempo of fertility."
  Popul Dev Rev 24(2):271-291. DOI: 10.2307/2807974.
- Figure: Fig. 3, observed and tempo-adjusted TFR for the United States,
  1950-90. Figure reading (approximate), 14 year points.
- x = tempo-adjusted TFR; y = observed TFR (both births/woman). Verdict:
  NOT_SIGNIFICANT (the two track each other roughly linearly).

## #39 Happiness U-Curve (Age) — `happiness_u_real.csv`
- Source: Stone AA, Schwartz JE, Broderick JE, Deaton A (2010) "A snapshot of
  the age distribution of psychological well-being in the United States." PNAS
  107(22):9985-9990. DOI: 10.1073/pnas.1003744107. Gallup 2008, N=340,847.
- Figure: Fig. 1, Global WB (Cantril ladder) mean by 4-year age group,
  UNADJUSTED ("Age alone") series. Figure reading (approximate), N=17 age bins.
- x = age (4-year-group midpoint); y = ladder (0-10). Verdict:
  ROBUST_NONLINEAR (U-shape, nadir age 50-53). NOTE: this is a cross-sectional
  age profile, not a within-person life-course trajectory.

## #26 Coale-Trussell Fertility Schedule — `coale_trussell_real.csv`
- Source: Coale AJ, Trussell TJ (1974/1978) "Model fertility schedules...",
  Population Index 40(2):185-258 (rev. 1978). Public-domain standard
  natural-fertility schedule n(a). TABLE TRANSCRIPTION (exact), N=6 age groups
  → INSUFFICIENT_DATA (too few points for nested F-test with clean-set LOOCV).

## #47 Crime-Temperature Curve — `crime_temperature_real.csv`
- Source: Chicago Police Department "Crimes - 2001 to present" via Socrata
  (dataset ijzp-q8t2), violent-crime types only; joined to NOAA GHCN-Daily
  station USW00094846 (Chicago O'Hare) daily TMAX/TMIN. Daily reconstruction
  2015-2019, N=1,826. Fully re-fetchable (see scripts/fetch_additional_real.py).
- x = daily mean temperature (°F); y = daily violent-crime count.

## #15 McKeown Thesis (TB Mortality) — `mckeown_real.csv` (TRANSCRIBED)
- Source: McKeown T, Record RG, Turner RD (1975) "An interpretation of the
  decline of mortality in England and Wales during the twentieth century."
  Population Studies 29(3):391-422. DOI: 10.1080/00324728.1975.10412707.
  Table 4 ("Death rates, persons per million, standardized for age and sex to
  the 1901 population"), row **Tuberculosis (respiratory)**.
- Data (transcribed verbatim from Table 4): standardized respiratory-TB death
  rate per million, England & Wales, decades 1901-1971 —
  1901:1268, 1911:1060, 1921:846, 1931:684, 1941:566, 1951:214, 1961:38,
  1971:13 (N=8).
- x = year; y = respiratory TB deaths per million (standardized to 1901).
- Note: the McKeown thesis point is that most of the decline (1268→566, ~55%)
  occurred before effective chemotherapy (streptomycin ~1947, before which the
  1901-1941 fall is already large). Replaces the previous hard-coded 1840-1960
  placeholder array, whose values had no traceable source.

## #8 J-Curve (Trade) — `j_curve_real.csv` (RECONSTRUCTION)
- Source: World Bank WDI, indicators `PX.REX.REER` (US real effective exchange
  rate index, annual) and `NE.RSB.GNFS.ZS` (US external balance on goods &
  services, % of GDP), fetched via the `wbgapi` API. Fully re-fetchable
  (`fetch_additional_real.py j_curve`); FRED (the more natural quarterly
  source) is network-blocked in this environment.
- Construction: the US REER peaked in 1985 (Plaza Accord). The peak year is
  located programmatically (not hard-coded); x = years since that peak,
  y = trade balance (% of GDP), for years peak..2000 (N=16).
- The series shows the canonical J shape (balance worsens 1985→1987, then
  improves through 1991). Verdict: ROBUST_NONLINEAR.
- **IMPORTANT LABEL:** this is a RECONSTRUCTION of a single real US episode
  using annual data, **NOT** the textbook stylized quarterly J-curve averaged
  across unspecified devaluation episodes. It must not be presented as a
  multi-country post-devaluation average.

## #49 Mitscherlich Yield Curve — `mitscherlich_real.csv` (RECONSTRUCTION)
- Source: Engelstad OP, Parks WL (1971) "Variability in Optimum N Rates for
  Corn." Agronomy Journal 63:21-23. DOI: 10.2134/agronj1971.00021962006300010008x.
  Distributed as `agridat::engelstad.nitro` (kwstat/agridat R package) and
  fetched from the Rdatasets CSV mirror
  (vincentarelbundock.github.io/Rdatasets/csv/agridat/engelstad.nitro.csv).
- Data: corn yield response to N fertilizer, 2 Tennessee locations
  (Jackson, Knoxville) × 5 years (1962-66) × 6 N rates (0-335 kg/ha), N=60.
  Yields are the published means of 9 replicates. Fully re-fetchable.
- x = nitrogen (kg/ha); y = corn yield (quintals/ha). Verdict: ROBUST_NONLINEAR
  (diminishing-returns form supported).
- **IMPORTANT LABEL:** this is a RECONSTRUCTION of the diminishing-returns
  *form*, **NOT** Mitscherlich's original 1909 (Landwirtschaftliche Jahrbücher
  38:537-552) data. Mitscherlich's original tables are not available as a
  machine-readable source; a modern, citable, fully-reproducible N-response
  trial is substituted and labelled as such. It must not be presented as
  Mitscherlich's own dataset.

## #37 Weber-Fechner Law — WITHDRAWN (no traceable source)
- The former implementation used a hand-typed "representative" stimulus/
  perceived-intensity array with no primary source. Fechner (1860) *Elemente
  der Psychophysik* Vol. 2 (supplied scans) is a theory/formula volume: the
  cited pages contain only equations and a conceptual schema (p.540), no
  numerical data table. The empirical psychophysical tables are in Vol. 1,
  which was not obtainable as a reproducible machine-readable source, and no
  public-domain digitizable table was located.
- Decision: #37 is EXCLUDED from the analysis (as with #35 Yerkes-Dodson)
  rather than presented with invented values. No CSV is provided.
