"""
Build CurveReexamination objects from the additional real datasets fetched by
fetch_additional_real.py. These replace previously hard-coded arrays for:

  - Environmental Kuznets Curve (CO2) (#4) : World Bank WDI cross-section
  - Keeling Curve (CO2) (#31)              : NOAA GML Mauna Loa annual means
  - Gutenberg-Richter Law (#42)            : USGS FDSN earthquake catalog
  - Moore's Law (#43)                      : Karl Rupp transistor-count dataset
  - Balassa-Samuelson Effect (#12)         : Penn World Table 10.01

Variable transformations mirror the original analysis so verdicts are
comparable (e.g. log10 counts for Gutenberg-Richter and Moore).
"""

import os

import numpy as np
import pandas as pd

from core_analysis import CurveReexamination

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

# World Bank aggregate/regional codes (not independent country observations)
WB_AGGREGATE_CODES = {
    'WLD', 'UMC', 'TSS', 'SSA', 'SSF', 'TSA', 'SAS', 'SST', 'PRE', 'PST',
    'PSS', 'OSS', 'OED', 'INX', 'NAC', 'MIC', 'TMN', 'MNA', 'MEA', 'LMC',
    'LIC', 'LMY', 'LDC', 'TLA', 'LAC', 'LCN', 'LTE', 'IDA', 'IDX', 'IDB',
    'IBT', 'IBD', 'HIC', 'HPC', 'FCS', 'EUU', 'TEC', 'ECA', 'ECS', 'EMU',
    'TEA', 'EAP', 'EAS', 'EAR', 'CEB', 'CSS', 'ARB', 'AFW', 'AFE',
}


def _load(fname):
    path = os.path.join(DATA_DIR, fname)
    if not os.path.exists(path):
        return None
    return pd.read_csv(path)


def get_laffer_real():
    df = _load('laffer_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['top_rate', 'tax_revenue_gdp'])
    df = df[(df['top_rate'] > 0) & (df['tax_revenue_gdp'] > 0)]
    labels = df['iso3'].values if 'iso3' in df.columns else None
    return CurveReexamination(
        "Laffer Curve",
        df['top_rate'].values, df['tax_revenue_gdp'].values,
        x_label="Top Marginal Personal Income Tax Rate (%)",
        y_label="Total Tax Revenue (% of GDP)",
        country_labels=labels, category="Economics",
    ), len(df)


def get_great_gatsby_real():
    df = _load('great_gatsby_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['gini', 'ige'])
    df = df[(df['gini'] > 0) & (df['ige'] > 0)]
    labels = df['iso3'].values if 'iso3' in df.columns else None
    return CurveReexamination(
        "Great Gatsby Curve",
        df['gini'].values, df['ige'].values,
        x_label="Gini Coefficient",
        y_label="Intergenerational Income Elasticity",
        country_labels=labels, category="Economics",
    ), len(df)


def get_hanpp_real():
    df = _load('hanpp_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['gdp_pc_ppp', 'hanpp_pct'])
    df = df[df['gdp_pc_ppp'] > 0]
    labels = df['iso3'].values if 'iso3' in df.columns else None
    return CurveReexamination(
        "HANPP vs Development",
        df['gdp_pc_ppp'].values, df['hanpp_pct'].values,
        x_label="GDP per capita (PPP, $)", y_label="HANPP (% of NPP0)",
        country_labels=labels, category="Environmental Science",
    ), len(df)


def get_putnam_real():
    df = _load('putnam_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['tv_hours', 'trust_pct'])
    df = df[(df['tv_hours'] > 0) & (df['trust_pct'] > 0)]
    labels = df['iso3'].values if 'iso3' in df.columns else None
    return CurveReexamination(
        "Putnam Social Capital",
        df['tv_hours'].values, df['trust_pct'].values,
        x_label="Daily TV Viewing (hours)", y_label="Social Trust (%)",
        country_labels=labels, category="Political Science",
    ), len(df)


def get_replacement_migration_real():
    df = _load('replacement_migration_real.csv')
    if df is None:
        return None
    df = df[df['unit_type'] == 'country'].dropna(
        subset=['tfr_gap', 'mig_per_million_sciv'])
    labels = df['iso3'].values if 'iso3' in df.columns else None
    return CurveReexamination(
        "Replacement Migration Curve",
        df['tfr_gap'].values, df['mig_per_million_sciv'].values,
        x_label="TFR Gap Below Replacement (2.1 - TFR)",
        y_label="Required Net Migration, Scenario IV (per million/yr)",
        country_labels=labels, category="Demography",
    ), len(df)


def get_ekc_co2_real():
    df = _load('ekc_co2_real.csv')
    if df is None:
        return None
    if 'country_code' in df.columns:
        df = df[~df['country_code'].isin(WB_AGGREGATE_CODES)]
    df = df.dropna(subset=['gdp_pc_ppp', 'co2_pc'])
    df = df[(df['gdp_pc_ppp'] > 500) & (df['co2_pc'] > 0)]
    labels = df['country'].values if 'country' in df.columns else None
    return CurveReexamination(
        "Environmental Kuznets Curve (CO2)",
        df['gdp_pc_ppp'].values, df['co2_pc'].values,
        x_label="GDP per capita (PPP, $)", y_label="CO2 per capita (tonnes)",
        country_labels=labels, category="Economics",
    ), len(df)


def get_keeling_real():
    df = _load('keeling_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['year', 'co2_ppm'])
    return CurveReexamination(
        "Keeling Curve (CO2)", df['year'].values, df['co2_ppm'].values,
        x_label="Year", y_label="CO\u2082 Concentration (ppm)",
        category="Environmental Science",
    ), len(df)


def get_gutenberg_richter_real():
    df = _load('gutenberg_richter_real.csv')
    if df is None:
        return None
    df = df[df['annual_count'] > 0].dropna(subset=['magnitude', 'annual_count'])
    return CurveReexamination(
        "Gutenberg-Richter Law",
        df['magnitude'].values, np.log10(df['annual_count'].values),
        x_label="Magnitude", y_label="log\u2081\u2080(Annual Frequency)",
        category="Physics",
    ), len(df)


def get_moores_law_real():
    df = _load('moores_law_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['year', 'transistors_thousands'])
    df = df[df['transistors_thousands'] > 0]
    return CurveReexamination(
        "Moore's Law",
        df['year'].values, np.log10(df['transistors_thousands'].values * 1e3),
        x_label="Year", y_label="log\u2081\u2080(Transistors)",
        category="Physics",
    ), len(df)


def get_omran_real():
    df = _load('omran_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['hdi', 'ncd_share'])
    df = df[(df['hdi'] > 0) & (df['ncd_share'] > 0)]
    labels = df['country'].values if 'country' in df.columns else None
    return CurveReexamination(
        "Omran Epidemiological Transition",
        df['hdi'].values, df['ncd_share'].values,
        x_label="Human Development Index", y_label="NCD deaths (% of total)",
        country_labels=labels, category="Public Health",
    ), len(df)


def get_lipset_real():
    df = _load('lipset_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['gdp_pc_ppp', 'democracy'])
    df = df[df['gdp_pc_ppp'] > 0]
    labels = df['Country'].values if 'Country' in df.columns else None
    return CurveReexamination(
        "Lipset Hypothesis",
        df['gdp_pc_ppp'].values, df['democracy'].values,
        x_label="GDP per capita (PPP, $)",
        y_label="Democracy score (Freedom House, 0-1)",
        country_labels=labels, category="Political Science",
    ), len(df)


def get_beveridge_real():
    df = _load('beveridge_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['unemployment_rate', 'vacancy_rate'])
    df = df[(df['unemployment_rate'] > 0) & (df['vacancy_rate'] > 0)]
    return CurveReexamination(
        "Beveridge Curve",
        df['unemployment_rate'].values, df['vacancy_rate'].values,
        x_label="Unemployment Rate (%)", y_label="Vacancy Rate (%)",
        category="Economics",
    ), len(df)


def get_engel_real():
    df = _load('engel_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['gdp_pc_ppp', 'food_share'])
    df = df[(df['gdp_pc_ppp'] > 0) & (df['food_share'] > 0)]
    labels = df['country'].values if 'country' in df.columns else None
    return CurveReexamination(
        "Engel Curve",
        df['gdp_pc_ppp'].values, df['food_share'].values,
        x_label="GDP per capita (PPP, $)", y_label="Food Expenditure Share (%)",
        country_labels=labels, category="Economics",
    ), len(df)


def get_rahn_real():
    df = _load('rahn_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['gov_expenditure_gdp', 'gdp_growth'])
    df = df[df['gov_expenditure_gdp'] > 0]
    labels = df['country'].values if 'country' in df.columns else None
    return CurveReexamination(
        "Rahn Curve",
        df['gov_expenditure_gdp'].values, df['gdp_growth'].values,
        x_label="Government Spending (% of GDP)",
        y_label="Real GDP Growth (%, 2010-2019 avg)",
        country_labels=labels, category="Economics",
    ), len(df)


def get_duverger_real():
    df = _load('duverger_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['district_magnitude', 'enep'])
    df = df[(df['district_magnitude'] > 0) & (df['enep'] > 0)]
    labels = None
    if 'country' in df.columns and 'year' in df.columns:
        labels = [f"{c} {int(y)}" for c, y in zip(df['country'], df['year'])]
    return CurveReexamination(
        "Duverger's Law",
        np.log(df['district_magnitude'].values + 1), df['enep'].values,
        x_label="log(District Magnitude + 1)",
        y_label="Effective Number of Parties",
        country_labels=labels, category="Political Science", x_is_logged=True,
    ), len(df)


def get_kleiber_real():
    df = _load('kleiber_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['body_mass_kg', 'bmr_watts'])
    df = df[(df['body_mass_kg'] > 0) & (df['bmr_watts'] > 0)]
    labels = df['species'].values if 'species' in df.columns else None
    return CurveReexamination(
        "Kleiber's Law",
        np.log10(df['body_mass_kg'].values), np.log10(df['bmr_watts'].values),
        x_label="log₁₀(Body Mass, kg)", y_label="log₁₀(BMR, Watts)",
        country_labels=labels, category="Physics", x_is_logged=True,
    ), len(df)


def get_species_area_real():
    df = _load('species_area_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['Area', 'Species'])
    df = df[(df['Area'] > 0) & (df['Species'] > 0)]
    labels = df['island'].values if 'island' in df.columns else None
    return CurveReexamination(
        "Species-Area Curve",
        np.log10(df['Area'].values), np.log10(df['Species'].values),
        x_label="log₁₀(Area, km²)", y_label="log₁₀(Species Count)",
        country_labels=labels, category="Environmental Science",
        x_is_logged=True,
    ), len(df)


def get_ebbinghaus_real():
    df = _load('ebbinghaus_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['time_hours', 'retention_pct'])
    df = df[df['time_hours'] > 0]
    return CurveReexamination(
        "Ebbinghaus Forgetting Curve",
        np.log(df['time_hours'].values), df['retention_pct'].values,
        x_label="log(Time in hours)", y_label="Retention (%)",
        category="Psychology", x_is_logged=True,
    ), len(df)


def get_bmi_mortality_real():
    df = _load('bmi_mortality_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['bmi_mid', 'hr'])
    return CurveReexamination(
        "BMI-Mortality J-Curve",
        df['bmi_mid'].values, df['hr'].values,
        x_label="BMI (kg/m²)", y_label="Relative Risk (all-cause mortality)",
        category="Public Health",
    ), len(df)


def get_gravity_real():
    df = _load('gravity_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['gdp_o', 'gdp_d', 'dist', 'tradeflow_baci'])
    df = df[(df['gdp_o'] > 0) & (df['gdp_d'] > 0)
            & (df['dist'] > 0) & (df['tradeflow_baci'] > 0)]
    gravity_index = np.log10(df['gdp_o'].values * df['gdp_d'].values
                             / df['dist'].values ** 2)
    trade_log = np.log10(df['tradeflow_baci'].values)
    return CurveReexamination(
        "Gravity Model of Trade", gravity_index, trade_log,
        x_label="log₁₀(GDP_i × GDP_j / Distance²)",
        y_label="log₁₀(Bilateral Trade)",
        category="Economics", x_is_logged=True,
    ), len(df)


def get_hubble_real():
    df = _load('hubble_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['distance_mpc', 'velocity_kms'])
    labels = df['object'].values if 'object' in df.columns else None
    return CurveReexamination(
        "Hubble's Law",
        df['distance_mpc'].values, df['velocity_kms'].values,
        x_label="Distance (Mpc)", y_label="Recession Velocity (km/s)",
        country_labels=labels, category="Physics",
    ), len(df)


def get_easterlin_real():
    df = _load('easterlin_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['gdp_pc_ppp', 'happiness'])
    df = df[(df['gdp_pc_ppp'] > 0) & (df['happiness'] > 0)]
    labels = df['country'].values if 'country' in df.columns else None
    return CurveReexamination(
        "Easterlin Paradox",
        df['gdp_pc_ppp'].values, df['happiness'].values,
        x_label="GDP per capita (PPP, $)", y_label="Happiness Score (0-10)",
        country_labels=labels, category="Public Health",
    ), len(df)


def get_lee_carter_real():
    df = _load('lee_carter_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['year', 'kappa_t'])
    return CurveReexamination(
        "Lee-Carter Mortality Model",
        df['year'].values, df['kappa_t'].values,
        x_label="Year", y_label="Mortality Index (\u03ba_t)",
        category="Demography",
    ), len(df)


def get_zipf_real():
    df = _load('zipf_cities_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['rank', 'population'])
    df = df[df['population'] > 0]
    return CurveReexamination(
        "Zipf's Law (US Cities)",
        np.log(df['rank'].values), np.log(df['population'].values),
        x_label="log(Rank)", y_label="log(Population)",
        category="Political Science",
    ), len(df)


def get_hubbert_real():
    df = _load('hubbert_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['year', 'production_kbd'])
    df = df[df['production_kbd'] > 0]
    return CurveReexamination(
        "Hubbert Peak Oil (US)", df['year'].values, df['production_kbd'].values,
        x_label="Year", y_label="US crude oil production (thousand bbl/day)",
        category="Environmental Science",
    ), len(df)


def get_jevons_real():
    df = _load('jevons_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['intensity_btu_per_usd', 'total_energy_tbtu'])
    df = df[(df['intensity_btu_per_usd'] > 0) & (df['total_energy_tbtu'] > 0)]
    return CurveReexamination(
        "Jevons Paradox (Energy)",
        df['intensity_btu_per_usd'].values, df['total_energy_tbtu'].values,
        x_label="Energy intensity (Btu per real $ GDP)",
        y_label="Total primary energy consumption (Trillion Btu)",
        category="Environmental Science",
    ), len(df)


def get_balassa_samuelson_real():
    df = _load('balassa_samuelson_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['productivity_rel_us', 'price_level_rel_us'])
    df = df[(df['productivity_rel_us'] > 0) & (df['price_level_rel_us'] > 0)]
    labels = df['country'].values if 'country' in df.columns else None
    return CurveReexamination(
        "Balassa-Samuelson Effect",
        df['productivity_rel_us'].values, df['price_level_rel_us'].values,
        x_label="Relative Labor Productivity (US=100)",
        y_label="Relative Price Level (US=1.0)",
        country_labels=labels, category="Economics",
    ), len(df)


def get_crime_temperature_real():
    df = _load('crime_temperature_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['tmean_f', 'violent_crimes'])
    df = df[df['violent_crimes'] > 0]
    return CurveReexamination(
        "Crime-Temperature Curve",
        df['tmean_f'].values, df['violent_crimes'].values,
        x_label="Daily mean temperature (deg F)",
        y_label="Daily violent-crime count (Chicago)",
        category="Political Science",
    ), len(df)


def get_coale_trussell_real():
    df = _load('coale_trussell_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['age_mid', 'n_a'])
    return CurveReexamination(
        "Coale-Trussell Fertility Schedule",
        df['age_mid'].values, df['n_a'].values,
        x_label="Age (midpoint of 5-year group)",
        y_label="Natural-fertility standard n(a)",
        category="Demography",
    ), len(df)


def get_lnt_real():
    df = _load('lnt_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['dose_gy', 'err'])
    return CurveReexamination(
        "Linear No-Threshold (LNT)",
        df['dose_gy'].values, df['err'].values,
        x_label="Weighted colon dose (Gy)",
        y_label="Excess relative risk (solid-cancer mortality)",
        category="Public Health",
    ), len(df)


def get_alcohol_mortality_real():
    df = _load('alcohol_mortality_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['alcohol_g_per_day', 'rr_total_mortality'])
    return CurveReexamination(
        "Alcohol-Mortality J-Curve",
        df['alcohol_g_per_day'].values, df['rr_total_mortality'].values,
        x_label="Alcohol (g/day)",
        y_label="Relative risk (all-cause mortality)",
        category="Public Health",
    ), len(df)


def get_barker_real():
    df = _load('barker_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['birth_weight_kg', 'smr_cardiovascular'])
    return CurveReexamination(
        "Barker Hypothesis (U-shape)",
        df['birth_weight_kg'].values, df['smr_cardiovascular'].values,
        x_label="Birth weight (kg)",
        y_label="SMR, all cardiovascular disease",
        category="Public Health",
    ), len(df)


def get_wilkinson_real():
    df = _load('wilkinson_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['pct_income_least_well_off_70', 'life_expectancy'])
    labels = df['country'].values if 'country' in df.columns else None
    return CurveReexamination(
        "Wilkinson Curve",
        df['pct_income_least_well_off_70'].values,
        df['life_expectancy'].values,
        x_label="% of income to least well-off 70%",
        y_label="Life expectancy (years)",
        country_labels=labels, category="Public Health",
    ), len(df)


def get_fries_real():
    df = _load('fries_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['age', 'pct_surviving_1980'])
    return CurveReexamination(
        "Fries Compression of Morbidity",
        df['age'].values, df['pct_surviving_1980'].values,
        x_label="Age (years)",
        y_label="Survival (%), US 1980",
        category="Public Health",
    ), len(df)


def get_dunning_kruger_real():
    df = _load('dunning_kruger_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['actual_percentile', 'perceived_ability_percentile'])
    return CurveReexamination(
        "Dunning-Kruger Effect",
        df['actual_percentile'].values,
        df['perceived_ability_percentile'].values,
        x_label="Actual performance (percentile)",
        y_label="Perceived ability (percentile)",
        category="Psychology",
    ), len(df)


def get_vitamin_d_real():
    df = _load('vitamin_d_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['serum_25ohd_nmol_l', 'hazard_ratio_all_cause'])
    return CurveReexamination(
        "Micronutrient U-shape (Vitamin D)",
        df['serum_25ohd_nmol_l'].values,
        df['hazard_ratio_all_cause'].values,
        x_label="Serum 25(OH)D (nmol/L)",
        y_label="Hazard ratio (all-cause mortality)",
        category="Agriculture",
    ), len(df)


def get_body_weight_setpoint_real():
    df = _load('body_weight_setpoint_real.csv')
    if df is None:
        return None
    df = df.dropna(
        subset=['weight_change_pct', 'observed_minus_predicted_tee_kcal_day'])
    return CurveReexamination(
        "Body Weight Set-Point",
        df['weight_change_pct'].values,
        df['observed_minus_predicted_tee_kcal_day'].values,
        x_label="Body-weight change (%)",
        y_label="Observed-minus-predicted total energy expenditure (kcal/day)",
        category="Agriculture",
    ), len(df)


def get_mckeown_real():
    df = _load('mckeown_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['year', 'tb_resp_death_rate_per_million'])
    return CurveReexamination(
        "McKeown Thesis (TB Mortality)",
        df['year'].values, df['tb_resp_death_rate_per_million'].values,
        x_label="Year", y_label="Respiratory TB deaths per million (std. to 1901)",
        category="Public Health",
    ), len(df)


def get_j_curve_real():
    df = _load('j_curve_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['years_since_peak', 'tb_pct_gdp'])
    return CurveReexamination(
        "J-Curve (Trade)",
        df['years_since_peak'].values, df['tb_pct_gdp'].values,
        x_label="Years since real-exchange-rate peak",
        y_label="Trade balance (% of GDP)",
        category="Economics",
    ), len(df)


def get_mitscherlich_real():
    df = _load('mitscherlich_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['nitrogen_kg_ha', 'yield_q_ha'])
    df = df[df['yield_q_ha'] > 0]
    return CurveReexamination(
        "Mitscherlich Yield Curve",
        df['nitrogen_kg_ha'].values, df['yield_q_ha'].values,
        x_label="Nitrogen fertilizer (kg/ha)",
        y_label="Corn yield (quintals/ha)",
        category="Agriculture",
    ), len(df)


def get_bongaarts_feeney_real():
    df = _load('bongaarts_feeney_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['adjusted_tfr', 'observed_tfr'])
    return CurveReexamination(
        "Bongaarts-Feeney Tempo Effect",
        df['adjusted_tfr'].values, df['observed_tfr'].values,
        x_label="Tempo-adjusted TFR (births/woman)",
        y_label="Observed TFR (births/woman)",
        category="Demography",
    ), len(df)


def get_happiness_u_real():
    df = _load('happiness_u_real.csv')
    if df is None:
        return None
    df = df.dropna(subset=['age_mid', 'wb_ladder_age_alone'])
    return CurveReexamination(
        "Happiness U-Curve (Age)",
        df['age_mid'].values, df['wb_ladder_age_alone'].values,
        x_label="Age (midpoint of 4-year group)",
        y_label="Global well-being (Cantril ladder, 0-10)",
        category="Psychology",
    ), len(df)


# curve_key -> (fetcher, exact result name it replaces, human source label)
ADDITIONAL_REAL = {
    'bongaarts_feeney': (
        get_bongaarts_feeney_real, 'Bongaarts-Feeney Tempo Effect',
        'Bongaarts & Feeney 1998 Popul Dev Rev 24:271-291, Fig. 3 '
        '(observed vs tempo-adjusted TFR, US 1950-90); digitized'),
    'happiness_u': (
        get_happiness_u_real, 'Happiness U-Curve (Age)',
        'Stone, Schwartz, Broderick & Deaton 2010 PNAS 107(22):9985-9990, '
        'Fig. 1 (Global WB ladder by 4-yr age group, unadjusted; '
        'Gallup 2008, N=340,847); digitized'),
    'vitamin_d': (get_vitamin_d_real, 'Micronutrient U-shape (Vitamin D)',
                  'Durup et al. 2012 J Clin Endocrinol Metab 97:2644-2652 '
                  '(CopD Study), Fig. 1A central spline (HR vs 25(OH)D, '
                  'ref 50 nmol/L); digitized'),
    'body_weight_setpoint': (
        get_body_weight_setpoint_real, 'Body Weight Set-Point',
        'Leibel, Rosenbaum & Hirsch 1995 NEJM 332:621-628, Fig. 2 '
        '(observed-minus-predicted TEE vs body-weight change); digitized'),
    'lnt': (get_lnt_real, 'Linear No-Threshold (LNT)',
            'Ozasa et al. 2012 Radiat Res 177:229-243 (LSS Report 14), Fig. 4 '
            '(erratum-corrected low-dose point); digitized from published figure'),
    'alcohol_mortality': (
        get_alcohol_mortality_real, 'Alcohol-Mortality J-Curve',
        'Di Castelnuovo et al. 2006 Arch Intern Med 166:2437-2445, '
        'total-mortality dose-response (fixed-effects curve); digitized'),
    'barker': (get_barker_real, 'Barker Hypothesis (U-shape)',
               'Osmond, Barker, Winter, Fall & Simmonds 1993 BMJ 307:1519-1524, '
               'Tables I-II (SMR all cardiovascular disease by birth weight, '
               'women+men); transcribed'),
    'wilkinson': (get_wilkinson_real, 'Wilkinson Curve',
                  'Wilkinson 1992 BMJ 304:165-168, Fig. 2 (life expectancy vs '
                  '% income to least well-off 70%, 9 OECD countries); digitized'),
    'fries': (get_fries_real, 'Fries Compression of Morbidity',
              'Fries 1980 NEJM 303:130-135, Fig. 2 (US 1980 survival curve, '
              'age vs % surviving); digitized'),
    'dunning_kruger': (get_dunning_kruger_real, 'Dunning-Kruger Effect',
                       'Kruger & Dunning 1999 JPSP 77:1121-1134, Figs. 1-4 '
                       '(perceived ability vs actual percentile, Studies 1-4); '
                       'digitized'),
    'crime_temperature': (get_crime_temperature_real, 'Crime-Temperature Curve',
                          'Chicago Police open crimes (Socrata ijzp-q8t2, '
                          'violent types) + NOAA GHCN-Daily O\'Hare TMAX/TMIN, '
                          'daily 2015-2019'),
    'coale_trussell': (get_coale_trussell_real,
                       'Coale-Trussell Fertility Schedule',
                       'Coale & Trussell (1974) Population Index 40(2):185-258, '
                       'standard natural-fertility schedule n(a) (rev. 1978); '
                       'public-domain table transcription'),
    'laffer': (get_laffer_real, 'Laffer Curve',
               'OECD Table I.7 (top PIT rate) + OECD Revenue Statistics '
               '(tax %GDP), 2022 cross-section'),
    'great_gatsby': (get_great_gatsby_real, 'Great Gatsby Curve',
                     'GDIM income mobility IGE (Munoz & van der Weide 2025) + '
                     'OWID/World Bank Gini; reconstruction'),
    'hanpp': (get_hanpp_real, 'HANPP vs Development',
              'Haberl et al. 2007 PNAS gridded HANPP/NPP0 (country zonal '
              'aggregation) + OWID/World Bank GDP pc, year 2000'),
    'putnam': (get_putnam_real, 'Putnam Social Capital',
               'Eurostat HETUS TV time (AC82) + OWID generalized trust; '
               'European proxy reconstruction'),
    'replacement_migration': (
        get_replacement_migration_real, 'Replacement Migration Curve',
        'UN (2000) Replacement Migration report, Tables IV.1 & IV.6 '
        '(model outputs, Scenario IV)'),
    'ekc_co2': (get_ekc_co2_real, 'Environmental Kuznets Curve (CO2)',
                'World Bank WDI (API)'),
    'keeling': (get_keeling_real, 'Keeling Curve (CO2)',
                'NOAA GML Mauna Loa'),
    'gutenberg_richter': (get_gutenberg_richter_real, 'Gutenberg-Richter Law',
                          'USGS FDSN earthquake catalog'),
    'moores_law': (get_moores_law_real, "Moore's Law",
                   'Karl Rupp microprocessor-trend-data'),
    'balassa_samuelson': (get_balassa_samuelson_real, 'Balassa-Samuelson Effect',
                          'Penn World Table 10.01'),
    'omran': (get_omran_real, 'Omran Epidemiological Transition',
              'UNDP HDI + World Bank WDI (NCD mortality)'),
    'lipset': (get_lipset_real, 'Lipset Hypothesis',
               'World Bank WDI + Freedom House (FIW)'),
    'hubbert': (get_hubbert_real, 'Hubbert Peak Oil (US)',
                'US EIA Total Energy (crude oil production)'),
    'jevons': (get_jevons_real, 'Jevons Paradox (Energy)',
               'US EIA Total Energy + World Bank WDI (US GDP)'),
    'beveridge': (get_beveridge_real, 'Beveridge Curve',
                  'US BLS (CPS unemployment + JOLTS job openings)'),
    'zipf': (get_zipf_real, "Zipf's Law (US Cities)",
             'US Census 2020 Decennial (place populations)'),
    'lee_carter': (get_lee_carter_real, 'Lee-Carter Mortality Model',
                   'HMD USA death rates (Lee-Carter SVD kappa_t)'),
    'easterlin': (get_easterlin_real, 'Easterlin Paradox',
                  'OWID Cantril ladder (WHR) + World Bank WDI GDP pc PPP'),
    'engel': (get_engel_real, 'Engel Curve',
              'OWID food expenditure share (USDA) + World Bank WDI GDP pc PPP'),
    'rahn': (get_rahn_real, 'Rahn Curve',
             'OWID govt expenditure (IMF) + World Bank WDI GDP growth'),
    'hubble': (get_hubble_real, "Hubble's Law",
               'Hubble (1929) PNAS Table 1 (24 nebulae, public domain)'),
    'gravity': (get_gravity_real, 'Gravity Model of Trade',
                'CEPII Gravity V202211 (GDP, distance, BACI trade; 2019)'),
    'bmi_mortality': (get_bmi_mortality_real, 'BMI-Mortality J-Curve',
                      'Global BMI Mortality Collaboration 2016 Lancet (HRs, transcribed)'),
    'ebbinghaus': (get_ebbinghaus_real, 'Ebbinghaus Forgetting Curve',
                   'Ebbinghaus (1885) Ch.7 Table (7 intervals, public domain)'),
    'species_area': (get_species_area_real, 'Species-Area Curve',
                     'Johnson & Raven (1973) Galapagos plant species (gala, N=30)'),
    'kleiber': (get_kleiber_real, "Kleiber's Law",
                'AnAge / HAGR build (422 mammal species: body mass vs BMR)'),
    'duverger': (get_duverger_real, "Duverger's Law",
                 'Bormann & Golder DES 5.0 (district magnitude vs ENEP, 1660 elections)'),
    'j_curve': (
        get_j_curve_real, 'J-Curve (Trade)',
        'World Bank WDI PX.REX.REER (US real effective exchange rate) + '
        'NE.RSB.GNFS.ZS (US external balance %GDP), years since the 1985 '
        'REER peak; reconstruction of the post-Plaza-Accord episode'),
    'mckeown': (
        get_mckeown_real, 'McKeown Thesis (TB Mortality)',
        'McKeown, Record & Turner 1975 Population Studies 29(3):391-422, '
        'Table 4 (respiratory tuberculosis standardized death rate per '
        'million, England & Wales, 1901-1971); transcribed'),
    'mitscherlich': (
        get_mitscherlich_real, 'Mitscherlich Yield Curve',
        'Engelstad & Parks 1971 Agronomy Journal 63:21-23, corn N-response '
        '(2 Tennessee locations x 5 years x 6 N rates; agridat::engelstad.nitro '
        'via Rdatasets); reconstruction of the diminishing-returns form '
        '(NOT Mitscherlich 1909 original data)'),
}


def get_all_additional_real():
    """Return dict of curve_name -> (CurveReexamination, N, source_label)."""
    out = {}
    for key, (fn, name, src) in ADDITIONAL_REAL.items():
        try:
            res = fn()
            if res is not None:
                crv, n = res
                out[name] = (crv, n, src)
                print(f"  Additional real data loaded: {name} (N={n}, {src})")
        except Exception as e:
            print(f"  Warning: {key} additional real data failed: {e}")
    return out


if __name__ == '__main__':
    d = get_all_additional_real()
    print(f"\nLoaded {len(d)} additional real curves")
    for name, (crv, n, src) in d.items():
        r = crv.run_full_analysis()
        print(f"{name}: N={n} verdict={r['verdict']['verdict']} "
              f"p_full={r['f_test']['p_value']:.4f} src={src}")
