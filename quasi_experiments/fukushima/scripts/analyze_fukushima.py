"""Quasi-experimental analyses of Fukushima evacuation orders."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import statsmodels.api as sm

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parent
sys.path.insert(0, str(PROJECT))

from common.synth import did_event_study, permutation_inference, synthetic_control


DATA = ROOT / "data"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
PANEL = DATA / "municipal_panel.csv"
EVAC = DATA / "evacuation_orders.csv"
AGE = DATA / "census_age_structure.csv"
RELATED = DATA / "reconstruction_related_deaths_fukushima.csv"
RAW = DATA / "raw"
DAMAGE_REPORT = RAW / "fukushima_damage_report_1260.pdf"
DAMAGE_TEXT = RAW / "fukushima_damage_report_1260.txt"
DAMAGE_REPORT_URL = "https://www.pref.fukushima.lg.jp/uploaded/attachment/422314.pdf"
WHO_REPORT = RAW / "who_health_risk_assessment_2013.pdf"
UNSCEAR_REPORT = RAW / "unscear_2013_report_volume_i.pdf"
TEN_HOEVE_REPORT = RAW / "ten_hoeve_jacobson_2012.pdf"
WHO_URL = "https://iris.who.int/server/api/core/bitstreams/3cc74066-fdcf-46ed-8e94-e2c7bc6e7eae/content"
UNSCEAR_URL = "https://www.unscear.org/unscear/uploads/documents/unscear-reports/UNSCEAR_2013_Report_Vol.I.pdf"
TEN_HOEVE_URL = "http://web.stanford.edu/group/efmh/jacobson/TenHoeveEES12.pdf"
PREFECTURES = ["03", "04", "06", "07", "08", "09", "10", "15"]
PREF_ROMAJI = {
    "03": "Iwate",
    "04": "Miyagi",
    "06": "Yamagata",
    "07": "Fukushima",
    "08": "Ibaraki",
    "09": "Tochigi",
    "10": "Gunma",
    "15": "Niigata",
}
MUNI_ROMAJI = {
    "南相馬市": "Minamisoma",
    "双葉町": "Futaba",
    "大熊町": "Okuma",
    "富岡町": "Tomioka",
    "川俣町": "Kawamata",
    "川内村": "Kawauchi",
    "楢葉町": "Naraha",
    "浪江町": "Namie",
    "葛尾村": "Katsurao",
    "飯舘村": "Iitate",
    "広野町": "Hirono",
    "田村市": "Tamura",
    "八幡平市": "Hachimantai",
    "奥州市": "Oshu",
    "滝沢市": "Takizawa",
    "西和賀町": "Nishiwaga",
    "洋野町": "Hirono",
    "仙台市青葉区": "Aoba Ward, Sendai",
    "〃青葉区": "Aoba Ward, Sendai",
    "仙台市宮城野区": "Miyagino Ward, Sendai",
    "〃宮城野区": "Miyagino Ward, Sendai",
    "仙台市若林区": "Wakabayashi Ward, Sendai",
    "〃若林区": "Wakabayashi Ward, Sendai",
    "仙台市太白区": "Taihaku Ward, Sendai",
    "〃太白区": "Taihaku Ward, Sendai",
    "仙台市泉区": "Izumi Ward, Sendai",
    "〃泉区": "Izumi Ward, Sendai",
    "塩竈市": "Shiogama",
    "塩竃市": "Shiogama",
    "登米市": "Tome",
    "栗原市": "Kurihara",
    "東松島市": "Higashimatsushima",
    "大崎市": "Osaki",
    "富谷市": "Tomiya",
    "七ヶ宿町": "Shichikashuku",
    "七ケ宿町": "Shichikashuku",
    "七ヶ浜町": "Shichigahama",
    "七ケ浜町": "Shichigahama",
    "美里町": "Misato",
    "南三陸町": "Minamisanriku",
    "庄内町": "Shonai",
    "本宮市": "Motomiya",
    "かすみがうら市": "Kasumigaura",
    "かすみがうら": "Kasumigaura",
    "桜川市": "Sakuragawa",
    "神栖市": "Kamisu",
    "行方市": "Namegata",
    "鉾田市": "Hokota",
    "つくばみらい市": "Tsukubamirai",
    "小美玉市": "Omitama",
    "那須烏山市": "Nasukarasuyama",
    "下野市": "Shimotsuke",
    "那珂川町": "Nakagawa",
    "みどり市": "Midori",
    "東吾妻町": "Higashiazuma",
    "みなかみ町": "Minakami",
    "新潟市北区": "Kita Ward, Niigata",
    "新潟市東区": "Higashi Ward, Niigata",
    "新潟市中央区": "Chuo Ward, Niigata",
    "新潟市江南区": "Konan Ward, Niigata",
    "新潟市秋葉区": "Akiha Ward, Niigata",
    "新潟市南区": "Minami Ward, Niigata",
    "新潟市西区": "Nishi Ward, Niigata",
    "新潟市西蒲区": "Nishikan Ward, Niigata",
    "妙高市": "Myoko",
    "胎内市": "Tainai",
    "聖籠町": "Seiro",
    "聖篭町": "Seiro",
    "阿賀町": "Aga",
    "女川町": "Onagawa",
    "陸前高田市": "Rikuzentakata",
    "大槌町": "Otsuchi",
    "山元町": "Yamamoto",
    "山田町": "Yamada",
    "石巻市": "Ishinomaki",
    "名取市": "Natori",
    "気仙沼市": "Kesennuma",
    "釜石市": "Kamaishi",
    "相馬市": "Soma",
    "新地町": "Shinchi",
    "亘理町": "Watari",
    "大船渡市": "Ofunato",
    "宮古市": "Miyako",
    "栃木市": "Tochigi",
    "檜枝岐村": "Hinoemata",
    "田野畑村": "Tanohata",
    "野田村": "Noda",
    "多賀城市": "Tagajo",
    "岩沼市": "Iwanuma",
    "真岡市": "Moka",
    "村上市": "Murakami",
    "大衡村": "Ohira",
    "松島町": "Matsushima",
    "普代村": "Fudai",
    "北塩原村": "Kitashiobara",
    "桑折町": "Koori",
    "川崎町": "Kawasaki",
    "美浦村": "Miho",
    "古殿町": "Furudono",
    "守谷市": "Moriya",
    "戸沢村": "Tozawa",
    "南会津町": "Minamiaizu",
    "二本松市": "Nihonmatsu",
    "新庄市": "Shinjo",
    "弥彦村": "Yahiko",
    "牛久市": "Ushiku",
    "吉岡町": "Yoshioka",
    "須賀川市": "Sukagawa",
    "茨城町": "Ibaraki",
    "上三川町": "Kaminokawa",
    "西郷村": "Nishigo",
    "浅川町": "Asakawa",
    "益子町": "Mashiko",
    "榛東村": "Shinto",
    "利根町": "Tone",
    "矢巾町": "Yahaba",
    "柴田町": "Shibata",
    "常陸大宮市": "Hitachiomiya",
    "いわき市": "Iwaki",
    "中之条町": "Nakanojo",
    "村山市": "Murayama",
    "鏡石町": "Kagamiishi",
    "舟形町": "Funagata",
    "白河市": "Shirakawa",
    "岩泉町": "Iwaizumi",
    "一戸町": "Ichinohe",
}
T1_NAMES = {"双葉町", "大熊町", "富岡町", "浪江町", "楢葉町", "葛尾村", "飯舘村", "川内村", "南相馬市", "川俣町"}
T1W_NAMES = {"双葉町", "大熊町", "富岡町", "飯舘村"}
T2_NAMES = {"広野町", "田村市"}
PRE = list(range(2006, 2011))
POST = list(range(2012, 2020))
SC_PRE = list(range(2006, 2011))
PERMUTATION_DRAWS = 1000
PERMUTATION_SEED = 20260918


def confirm_english_font() -> dict[str, object]:
    labels = ["Year", "Observed", "Synthetic", "Crude death rate per 1,000"]
    if not all(label.isascii() for label in labels):
        raise ValueError("non-English figure label detected")
    figure, axis = plt.subplots(figsize=(2, 1))
    axis.set_xlabel(labels[0])
    axis.set_ylabel(labels[3])
    figure.canvas.draw()
    plt.close(figure)
    return {"font_family": plt.rcParams["font.family"], "labels_ascii": True}


def load_panel() -> pd.DataFrame:
    panel = pd.read_csv(PANEL, dtype={"pref_code": str, "muni_code": str})
    panel = panel.loc[panel["year"].between(2005, 2022)].copy()
    duplicate_mask = panel.duplicated(["muni_code", "year"], keep=False)
    duplicate_rows_collapsed = int(
        len(panel) - len(panel.drop_duplicates(["muni_code", "year"]))
    )
    if duplicate_mask.any():
        panel = (
            panel.sort_values(["muni_code", "year", "deaths", "births"])
            .drop_duplicates(["muni_code", "year"], keep="last")
            .sort_values(["muni_code", "year"])
            .reset_index(drop=True)
        )
    panel.attrs["duplicate_rows_collapsed"] = duplicate_rows_collapsed
    panel["cdr"] = 1000 * panel["deaths"] / panel["pop"]
    panel["ln_cdr"] = np.log(panel["cdr"].where(panel["cdr"] > 0))
    panel["treated_t1"] = panel["muni_name"].isin(T1_NAMES).astype(int)
    panel["treated_t1w"] = panel["muni_name"].isin(T1W_NAMES).astype(int)
    panel["treated_t2"] = panel["muni_name"].isin(T2_NAMES).astype(int)
    age = pd.read_csv(AGE, dtype={"muni_code": str})
    age = age.loc[age["census_year"] == 2010, ["muni_code", "share_65plus", "share_75plus"]]
    panel = panel.merge(age, on="muni_code", how="left")
    panel["pop_robust"] = panel["pop"]
    for code, group in panel.groupby("muni_code"):
        values = group.set_index("year")["pop"]
        if 2012 not in values or 2013 not in values or pd.isna(values.loc[2012]) or pd.isna(values.loc[2013]):
            continue
        ratio = np.log(values.loc[2013] / values.loc[2012])
        mask = (panel["muni_code"] == code) & panel["year"].between(2005, 2012)
        panel.loc[mask, "pop_robust"] = panel.loc[mask, "pop"] * np.exp(
            ratio * (2012 - panel.loc[mask, "year"]) / 7
        )
    panel["cdr_robust"] = 1000 * panel["deaths"] / panel["pop_robust"]
    panel["ln_cdr_robust"] = np.log(panel["cdr_robust"].where(panel["cdr_robust"] > 0))
    return panel


def sample_frame(panel: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    years = list(range(2005, 2020))
    eligible = panel.loc[panel["year"].isin(years)].copy()
    all_codes = sorted(panel.loc[panel["year"] == 2019, "muni_code"].unique())
    complete_codes = [
        code
        for code, group in eligible.groupby("muni_code")
        if len(group) == len(years)
        and group["deaths"].notna().all()
        and group["pop"].notna().all()
    ]
    dropped = sorted(set(all_codes) - set(complete_codes))
    dropped_rows = []
    for code in dropped:
        group = eligible.loc[eligible["muni_code"] == code].sort_values("year")
        missing_years = sorted(set(years) - set(group["year"]))
        missing_population = sorted(
            group.loc[group["pop"].isna(), "year"].astype(int).tolist()
        )
        if missing_years:
            reason = "Unit not observed under a single code 2005-2019"
            years_missing = sorted(set(missing_years + missing_population))
        else:
            reason = "Population missing in at least one year 2005-2019"
            years_missing = missing_population
        row = panel.loc[panel["muni_code"] == code].sort_values("year").iloc[-1]
        dropped_rows.append(
            {
                "pref_code": str(row["pref_code"]).zfill(2),
                "pref_name": PREF_ROMAJI.get(str(row["pref_code"]).zfill(2), "Unknown"),
                "muni_code": str(code).zfill(5),
                "muni_name_romaji": MUNI_ROMAJI.get(str(row["muni_name"]), str(code).zfill(5)),
                "reason": reason,
                "years_missing": ",".join(str(year) for year in years_missing),
            }
        )
    eligible = eligible.loc[eligible["muni_code"].isin(complete_codes)].copy()
    baseline = panel.loc[panel["year"].between(2006, 2011)].copy()
    baseline = baseline.loc[baseline["year"].isin([2006, 2007, 2008, 2009, 2010, 2011])]
    means = baseline.loc[baseline["year"].between(2006, 2010)].groupby("muni_code")["deaths"].mean()
    deaths_2011 = baseline.loc[baseline["year"] == 2011].set_index("muni_code")["deaths"]
    tsunami_ratio = (deaths_2011 / means).replace([np.inf, -np.inf], np.nan)
    mass_candidates = (
        tsunami_ratio[tsunami_ratio > 1.20]
        .dropna()
        .loc[lambda values: values.index.isin(complete_codes)]
        .sort_values(ascending=False)
    )
    t1_codes = sorted(eligible.loc[eligible["treated_t1"] == 1, "muni_code"].unique())
    t2_codes = sorted(eligible.loc[eligible["treated_t2"] == 1, "muni_code"].unique())
    mass_casualty_controls = [
        code for code in mass_candidates.index.tolist()
        if code not in set(t1_codes) | set(t2_codes)
    ]
    control_codes = sorted(
        set(complete_codes)
        - set(t1_codes)
        - set(t2_codes)
        - set(mass_casualty_controls)
    )
    metadata = {
        "years": years,
        "n_all_units": len(all_codes),
        "n_complete_units": len(complete_codes),
        "dropped_for_any_2005_2019_gap": dropped,
        "n_dropped_for_any_gap": len(dropped),
        "mass_casualty_control_exclusions": mass_casualty_controls,
        "mass_casualty_control_ratios": {
            code: float(mass_candidates.loc[code]) for code in mass_casualty_controls
        },
        "n_mass_casualty_control_exclusions": len(mass_casualty_controls),
        "n_control_units": len(control_codes),
        "control_codes": control_codes,
        "t1_codes": t1_codes,
        "t2_codes": t2_codes,
        "dropped_units": dropped_rows,
        "n_dropped_missing": len(dropped_rows),
    }
    return eligible, metadata


def design_matrix(
    data: pd.DataFrame,
    treated_col: str,
    time_col: str,
    unit_col: str,
    ref_year: int,
    post_start: int | None = None,
    post_end: int | None = None,
    event: bool = False,
    age_control: bool = False,
) -> tuple[pd.DataFrame, list[str]]:
    X = pd.DataFrame(index=data.index)
    terms = []
    years = sorted(data[time_col].unique())
    if event:
        for year in years:
            if year == ref_year:
                continue
            name = f"event_{year}"
            X[name] = data[treated_col] * (data[time_col] == year)
            terms.append(name)
    else:
        post = data[time_col].between(post_start, post_end)
        X["att"] = data[treated_col] * post
        terms.append("att")
    if age_control and "share_65plus" in data:
        for year in years:
            if year == ref_year:
                continue
            X[f"age65_{year}"] = data["share_65plus"] * (data[time_col] == year)
    X = pd.concat(
        [
            X,
            pd.get_dummies(data[unit_col].astype(str), prefix="unit", drop_first=True),
            pd.get_dummies(data[time_col], prefix="year", drop_first=True),
        ],
        axis=1,
    )
    return sm.add_constant(X.astype(float), has_constant="add"), terms


def estimate_att(
    data: pd.DataFrame,
    treated_col: str,
    outcome: str,
    pop_col: str = "pop",
    age_control: bool = False,
    post_start: int = 2012,
    post_end: int = 2019,
    exclude_years: list[int] | None = None,
    weighted: bool = True,
    start_year: int = 2006,
) -> dict[str, object]:
    frame = data.loc[data["year"].between(start_year, post_end)].copy()
    if exclude_years:
        frame = frame.loc[~frame["year"].isin(exclude_years)]
    frame = frame.dropna(subset=[outcome, treated_col, pop_col])
    X, terms = design_matrix(
        frame,
        treated_col,
        "year",
        "muni_code",
        2010,
        post_start,
        post_end,
        age_control=age_control,
    )
    weights = frame[pop_col].astype(float)
    model = (
        sm.WLS(frame[outcome].astype(float), X, weights=weights)
        if weighted
        else sm.OLS(frame[outcome].astype(float), X)
    )
    fit = model.fit(cov_type="cluster", cov_kwds={"groups": frame["muni_code"]})
    beta = float(fit.params["att"])
    se = float(fit.bse["att"])
    ci_low, ci_high = beta - 1.96 * se, beta + 1.96 * se
    X_cf = X.copy()
    X_cf["att"] = 0
    frame["cdr_counterfactual"] = np.exp(fit.predict(X_cf))
    post_mask = frame["year"].between(post_start, post_end) & (frame[treated_col] == 1)
    excess = (
        frame.loc[post_mask, pop_col]
        * frame.loc[post_mask, "cdr_counterfactual"]
        * (np.exp(beta) - 1)
        / 1000
    )
    excess_low = (
        frame.loc[post_mask, pop_col]
        * frame.loc[post_mask, "cdr_counterfactual"]
        * (np.exp(ci_low) - 1)
        / 1000
    )
    excess_high = (
        frame.loc[post_mask, pop_col]
        * frame.loc[post_mask, "cdr_counterfactual"]
        * (np.exp(ci_high) - 1)
        / 1000
    )
    annual = pd.DataFrame(
        {
            "year": frame.loc[post_mask, "year"].astype(int).to_numpy(),
            "excess_deaths": excess.to_numpy(),
            "excess_deaths_ci_low": excess_low.to_numpy(),
            "excess_deaths_ci_high": excess_high.to_numpy(),
        }
    ).groupby("year", as_index=False).sum()
    implied_excess_deaths = (
        frame.loc[post_mask, "deaths"] * (1 - np.exp(-beta))
    ).sum()
    return {
        "beta": beta,
        "se": se,
        "ci_low": ci_low,
        "ci_high": ci_high,
        "excess_deaths": float(excess.sum()),
        "excess_deaths_ci_low": float(excess_low.sum()),
        "excess_deaths_ci_high": float(excess_high.sum()),
        "excess_deaths_per_year": float(excess.sum() / (post_end - post_start + 1)),
        "excess_deaths_by_year": annual.to_dict(orient="records"),
        "implied_excess_deaths": float(implied_excess_deaths),
        "implied_excess_deaths_per_year": float(
            implied_excess_deaths / (post_end - post_start + 1)
        ),
        "n_obs": int(fit.nobs),
        "n_units": int(frame["muni_code"].nunique()),
        "post_years": f"{post_start}-{post_end}",
    }


def aggregate_treated(panel: pd.DataFrame, codes: list[str]) -> pd.DataFrame:
    frame = panel.loc[panel["muni_code"].isin(codes)].groupby("year", as_index=True)[["deaths", "pop"]].sum(min_count=1)
    frame["cdr"] = 1000 * frame["deaths"] / frame["pop"]
    return frame


def restricted_sc_donors(
    panel: pd.DataFrame,
    controls: list[str],
    treated_age: float,
    treated_pop: float | None = None,
    use_population_match: bool = False,
) -> list[str]:
    """Return eligible Fukushima donors with the required age match."""
    age = panel[["muni_code", "pref_code", "share_65plus"]].drop_duplicates("muni_code")
    pop = panel.loc[panel["year"] == 2010, ["muni_code", "pop"]].drop_duplicates("muni_code")
    lookup = age.merge(pop, on="muni_code", how="left").set_index("muni_code")
    eligible = []
    for code in controls:
        if code not in lookup.index or lookup.loc[code, "pref_code"] != "07":
            continue
        donor_age = lookup.loc[code, "share_65plus"]
        if pd.isna(donor_age) or pd.isna(treated_age) or abs(donor_age - treated_age) > 0.10:
            continue
        if use_population_match and treated_pop is not None:
            donor_pop = lookup.loc[code, "pop"]
            if pd.notna(donor_pop) and not (0.25 * treated_pop <= donor_pop <= 4 * treated_pop):
                continue
        eligible.append(code)
    return eligible


def pooled_age_share(panel: pd.DataFrame, codes: list[str]) -> float:
    age = (
        panel.loc[panel["year"] == 2010, ["muni_code", "share_65plus", "pop"]]
        .drop_duplicates("muni_code")
        .dropna()
    )
    age = age.loc[age["muni_code"].isin(codes)]
    return float(np.average(age["share_65plus"], weights=age["pop"]))


def crossfit_sc(result_data: pd.DataFrame, treated: str, donors: list[str]) -> dict[str, object]:
    fit = synthetic_control(result_data[[treated, *donors]], treated, donors, [2006, 2007, 2008])
    evaluation = result_data.index.intersection([2009, 2010])
    gap = fit.gaps.loc[evaluation].dropna()
    return {
        "treated": treated,
        "n_donors": len(donors),
        "fit_years": "2006-2008",
        "evaluation_years": "2009-2010",
        "fit_rmspe": fit.rmspe_pre,
        "evaluation_rmspe": float(np.sqrt(np.mean(gap**2))) if len(gap) else np.nan,
        "weights": json.dumps({str(k): float(v) for k, v in fit.weights.items()}),
    }


def run_synthetic_controls(
    panel: pd.DataFrame,
    metadata: dict[str, object],
    obstacles: list[dict[str, object]],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    controls = metadata["control_codes"]
    complete_codes = set(panel["muni_code"])
    pop_lookup = panel.loc[panel["year"] == 2010].set_index("muni_code")["pop"]
    unit_rows = []
    crossfit_rows = []
    fuku_controls = [
        code for code in controls
        if not panel.loc[panel["muni_code"] == code, "pref_code"].empty
        and panel.loc[panel["muni_code"] == code, "pref_code"].iloc[0] == "07"
    ]
    for treated in metadata["t1_codes"]:
        if treated not in complete_codes:
            continue
        treated_pop = pop_lookup.get(treated, np.nan)
        treated_age = float(
            panel.loc[panel["muni_code"] == treated, "share_65plus"].dropna().iloc[0]
        ) if panel.loc[panel["muni_code"] == treated, "share_65plus"].notna().any() else np.nan
        donors = restricted_sc_donors(
            panel, fuku_controls, treated_age, treated_pop, use_population_match=True
        )
        Y = panel.loc[panel["year"].between(2006, 2019) & panel["muni_code"].isin([treated, *donors])].pivot(
            index="year", columns="muni_code", values="ln_cdr"
        ).sort_index()
        donors = [
            donor
            for donor in donors
            if donor in Y and Y[donor].notna().all()
        ]
        if treated not in Y or Y[treated].isna().any() or not donors:
            obstacles.append({"analysis": "Fukushima unit synthetic control", "treated": treated, "reason": "insufficient complete pre-period donor pool", "n_donors": len(donors)})
            continue
        try:
            result = synthetic_control(Y[[treated, *donors]], treated, donors, SC_PRE)
            perm = permutation_inference(Y[[treated, *donors]], treated, donors, SC_PRE, list(range(2011, 2020)))
        except ValueError as exc:
            obstacles.append({"analysis": "Fukushima unit synthetic control", "treated": treated, "reason": str(exc)})
            continue
        p = float(perm.loc[perm["is_treated"], "p_value"].iloc[0])
        unit_rows.append(
            {
                "muni_code": treated,
                "muni_name": panel.loc[panel["muni_code"] == treated, "muni_name"].iloc[0],
                "rmspe_pre": result.rmspe_pre,
                "rmspe_post": result.rmspe_post,
                "ratio": result.ratio,
                "perm_p": p,
                "post_mean_gap": float(result.gaps.loc[2012:2019].mean()),
                "n_donors": len(donors),
            }
        )
        if result.rmspe_pre < 1e-4:
            crossfit_rows.append(crossfit_sc(Y, treated, donors))

    treated_codes = metadata["t1_codes"]
    agg = aggregate_treated(panel, treated_codes)
    aggregate_age = pooled_age_share(panel, treated_codes)
    donors = restricted_sc_donors(panel, fuku_controls, aggregate_age)
    Y = panel.loc[panel["year"].between(2006, 2019) & panel["muni_code"].isin(donors)].pivot(
        index="year", columns="muni_code", values="ln_cdr"
    ).sort_index()
    donors = [code for code in donors if code in Y and Y[code].notna().all()]
    aggregate_rows = []
    if len(donors) and agg["cdr"].notna().all():
        Y["T1_aggregate"] = np.log(agg["cdr"])
        Y = Y.dropna(subset=["T1_aggregate"])
        try:
            result = synthetic_control(Y[["T1_aggregate", *donors]], "T1_aggregate", donors, SC_PRE)
            perm = permutation_inference(Y[["T1_aggregate", *donors]], "T1_aggregate", donors, SC_PRE, list(range(2011, 2020)))
            aggregate_rows.append(
                {
                    "treated": "T1_aggregate",
                    "rmspe_pre": result.rmspe_pre,
                    "rmspe_post": result.rmspe_post,
                    "ratio": result.ratio,
                    "perm_p": float(perm.loc[perm["is_treated"], "p_value"].iloc[0]),
                    "post_mean_gap": float(result.gaps.loc[2012:2019].mean()),
                    "n_donors": len(donors),
                }
            )
            if result.rmspe_pre < 1e-4:
                crossfit_rows.append(crossfit_sc(Y, "T1_aggregate", donors))
            plot_aggregate_sc(result, agg)
            plot_unit_sc(panel, metadata["t1_codes"], fuku_controls)
        except ValueError as exc:
            obstacles.append({"analysis": "Fukushima aggregate synthetic control", "reason": str(exc), "n_donors": len(donors)})
    else:
        obstacles.append({"analysis": "Fukushima aggregate synthetic control", "reason": "insufficient complete aggregate or donor series", "n_donors": len(donors)})
    pd.DataFrame(crossfit_rows).to_csv(
        RESULTS / "sc_crossfit.csv",
        index=False,
        columns=[
            "treated", "n_donors", "fit_years", "evaluation_years",
            "fit_rmspe", "evaluation_rmspe", "weights",
        ],
    )
    return pd.DataFrame(unit_rows), pd.DataFrame(aggregate_rows)


def plot_aggregate_sc(result, aggregate: pd.DataFrame) -> None:
    years = result.gaps.index
    plt.figure(figsize=(8, 4.5))
    plt.plot(years, np.exp(result.synthetic), label="Synthetic T1")
    plt.plot(years, aggregate.loc[years, "cdr"], label="T1 observed")
    plt.axvline(2011, color="black", linestyle="--", label="2011 disaster year")
    plt.xlabel("Year")
    plt.ylabel("Crude death rate per 1,000")
    plt.title("Fukushima T1 aggregate synthetic control")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIGURES / "sc_t1_aggregate.png", dpi=160)
    plt.close()


def plot_unit_sc(panel: pd.DataFrame, treated_codes: list[str], controls: list[str]) -> None:
    fig, axes = plt.subplots(2, 5, figsize=(15, 6), sharex=True)
    for axis, treated in zip(axes.flat, treated_codes):
        Y = panel.loc[panel["year"].between(2006, 2019) & panel["muni_code"].isin([treated, *controls])].pivot(
            index="year", columns="muni_code", values="ln_cdr"
        ).sort_index()
        treated_age = panel.loc[panel["muni_code"] == treated, "share_65plus"].dropna()
        donors = restricted_sc_donors(
            panel,
            controls,
            float(treated_age.iloc[0]) if not treated_age.empty else np.nan,
            panel.loc[(panel["muni_code"] == treated) & (panel["year"] == 2010), "pop"].iloc[0]
            if not panel.loc[(panel["muni_code"] == treated) & (panel["year"] == 2010), "pop"].empty
            else None,
            use_population_match=True,
        )
        donors = [code for code in donors if code in Y and Y[code].notna().all()]
        if treated not in Y or not donors or Y[treated].isna().any():
            axis.set_title(str(treated))
            continue
        result = synthetic_control(Y[[treated, *donors]], treated, donors, SC_PRE)
        axis.plot(result.gaps.index, Y[treated], label="Observed")
        axis.plot(result.gaps.index, result.synthetic, label="Synthetic")
        axis.axvline(2011, color="black", linestyle="--")
        axis.set_title(str(treated))
        axis.set_xlabel("Year")
        axis.set_ylabel("ln CDR")
    handles, labels = axes.flat[0].get_legend_handles_labels()
    if handles:
        axes.flat[0].legend(handles, labels, fontsize=7)
    fig.suptitle("Fukushima T1 municipality synthetic controls")
    fig.tight_layout()
    fig.savefig(FIGURES / "sc_t1_small_multiples.png", dpi=160)
    plt.close(fig)


def _prepare_fe(
    data: pd.DataFrame,
    outcome: str,
    weighted: bool,
    age_control: bool,
) -> dict[str, object]:
    """Prepare a fixed-effect residualizer reused across placebo draws."""
    frame = data.dropna(subset=[outcome] + (["pop"] if weighted else [])).copy()
    unit_dummies = pd.get_dummies(frame["muni_code"].astype(str), drop_first=True)
    year_dummies = pd.get_dummies(frame["year"].astype(int), drop_first=True)
    z_parts = [np.ones((len(frame), 1)), unit_dummies.to_numpy(), year_dummies.to_numpy()]
    if age_control:
        for year in sorted(frame["year"].unique()):
            if year != 2010:
                z_parts.append(
                    (frame["share_65plus"].to_numpy() * (frame["year"].to_numpy() == year))[:, None]
                )
    z = np.column_stack(z_parts).astype(float)
    sqrt_w = np.sqrt(frame["pop"].to_numpy(float)) if weighted else np.ones(len(frame))
    zw = z * sqrt_w[:, None]
    z_pinv = np.linalg.pinv(zw)
    y = frame[outcome].to_numpy(float)
    y_res = y - z @ (z_pinv @ (y * sqrt_w))
    return {"frame": frame, "z": z, "z_pinv": z_pinv, "sqrt_w": sqrt_w, "y_res": y_res}


def _fast_fe_coefficients(
    prepared: dict[str, object],
    treated_units: set[str],
    att_only: bool = False,
) -> tuple[float, float]:
    """Estimate ATT and the pre-trend statistic after removing FE."""
    frame = prepared["frame"].copy()
    z = prepared["z"]
    z_pinv = prepared["z_pinv"]
    sqrt_w = prepared["sqrt_w"]
    y_res = prepared["y_res"]
    frame["placebo_treated"] = frame["muni_code"].isin(treated_units).astype(float)

    post = frame["year"].between(2012, 2019).to_numpy()
    q_att = frame["placebo_treated"].to_numpy() * post
    q_att_res = q_att - z @ (z_pinv @ (q_att * sqrt_w))
    denom = float(np.sum((q_att_res * sqrt_w) ** 2))
    att = float(np.sum(q_att_res * sqrt_w * y_res * sqrt_w) / denom) if denom > 1e-12 else np.nan
    if att_only:
        return att, np.nan

    event_years = [year for year in sorted(frame["year"].unique()) if year != 2010]
    q_event = np.column_stack(
        [
            frame["placebo_treated"].to_numpy() * (frame["year"].to_numpy() == year)
            for year in event_years
        ]
    )
    q_res = q_event - z @ (z_pinv @ (q_event * sqrt_w[:, None]))
    beta = np.linalg.lstsq(q_res * sqrt_w[:, None], y_res * sqrt_w, rcond=None)[0]
    pre = [beta[event_years.index(year)] for year in [2006, 2007, 2008, 2009] if year in event_years]
    return att, float(np.sum(np.square(pre)))


def permutation_fe_inference(
    panel: pd.DataFrame,
    treatment_codes: list[str],
    control_codes: list[str],
    outcome: str = "ln_cdr",
    weighted: bool = True,
    age_control: bool = False,
    n_draws: int = PERMUTATION_DRAWS,
    seed: int = PERMUTATION_SEED,
) -> dict[str, object]:
    """Randomization inference for ATT and the event-study pre-trend statistic."""
    units = [*treatment_codes, *control_codes]
    frame = panel.loc[
        panel["muni_code"].isin(units) & panel["year"].between(2006, 2019)
    ].copy()
    if age_control:
        frame = frame.dropna(subset=["share_65plus"])
    att_frame = frame.loc[frame["year"] != 2011].copy()
    att_prepared = _prepare_fe(att_frame, outcome, weighted, age_control)
    event_prepared = _prepare_fe(frame, outcome, weighted, age_control)
    actual_att, _ = _fast_fe_coefficients(att_prepared, set(treatment_codes), att_only=True)
    _, actual_pre = _fast_fe_coefficients(event_prepared, set(treatment_codes))
    rng = np.random.default_rng(seed)
    placebo_atts = []
    placebo_pre = []
    for _ in range(n_draws):
        pseudo = set(rng.choice(control_codes, size=len(treatment_codes), replace=False))
        placebo_atts.append(
            _fast_fe_coefficients(att_prepared, pseudo, att_only=True)[0]
        )
        placebo_pre.append(
            _fast_fe_coefficients(event_prepared, pseudo)[1]
        )
    placebo_atts = np.asarray(placebo_atts, dtype=float)
    placebo_pre = np.asarray(placebo_pre, dtype=float)
    return {
        "att": actual_att,
        "perm_p_att": float(np.mean(np.abs(placebo_atts) >= abs(actual_att))),
        "pretrend_stat": actual_pre,
        "perm_p_pretrend": float(np.mean(placebo_pre >= actual_pre)),
        "n_draws": n_draws,
    }


def event_studies(
    panel: pd.DataFrame,
    controls: list[str],
    obstacles: list[dict[str, object]],
) -> tuple[pd.DataFrame, pd.DataFrame]:
    rows = []
    wald_rows = []
    treatment_groups = {
        "T1": T1_NAMES,
        "T1w": T1W_NAMES,
        "T2": T2_NAMES,
    }
    for control_name, codes in {
        "all_prefectures": controls,
        "fukushima_only": [code for code in controls if panel.loc[panel["muni_code"] == code, "pref_code"].iloc[0] == "07"],
    }.items():
        for treatment, flag in [("T1", "treated_t1"), ("T1w", "treated_t1w"), ("T2", "treated_t2")]:
            treated_codes = sorted(
                panel.loc[panel["muni_name"].isin(treatment_groups[treatment]), "muni_code"].unique()
            )
            sample = panel.loc[
                panel["muni_code"].isin([*treated_codes, *codes])
                & panel["year"].between(2006, 2019)
            ].copy()
            for weighting, weight_col in [("weighted", "pop"), ("unweighted", None)]:
                for outcome in ["ln_cdr", "ln_cdr_robust"]:
                    if sample[flag].sum() == 0:
                        continue
                    try:
                        event = did_event_study(
                            sample,
                            unit="muni_code",
                            time="year",
                            y=outcome,
                            treated_flag=flag,
                            ref_year=2010,
                            weights=weight_col,
                            cluster="muni_code",
                        )
                    except Exception as exc:
                        obstacles.append({"analysis": "Fukushima DiD event study", "control": control_name, "treatment": treatment, "weighting": weighting, "outcome": outcome, "reason": f"{type(exc).__name__}: {exc}"})
                        continue
                    event["control_pool"] = control_name
                    event["treatment"] = treatment
                    event["weighting"] = weighting
                    event["outcome"] = outcome
                    event["age_control"] = False
                    rows.append(event)
                    event_names = [f"event_{year}" for year in range(2006, 2010)]
                    model_data = sample.dropna(subset=[outcome]).copy()
                    X, _ = design_matrix(
                        model_data,
                        flag,
                        "year",
                        "muni_code",
                        2010,
                        event=True,
                    )
                    fit_model = (
                        sm.WLS(model_data[outcome], X, weights=model_data["pop"])
                        if weight_col
                        else sm.OLS(model_data[outcome], X)
                    ).fit(
                        cov_type="cluster",
                        cov_kwds={"groups": model_data["muni_code"]},
                    )
                    if all(name in fit_model.params.index for name in event_names):
                        restriction = np.zeros((len(event_names), len(fit_model.params)))
                        for index, name in enumerate(event_names):
                            restriction[index, fit_model.params.index.get_loc(name)] = 1
                        test = fit_model.wald_test(restriction, use_f=False)
                        wald_rows.append(
                            {
                                "control_pool": control_name,
                                "treatment": treatment,
                                "weighting": weighting,
                                "outcome": outcome,
                                "age_control": False,
                                "test": "joint_pretrend_2006_2009",
                                "statistic_type": "chi2",
                                "statistic": float(np.asarray(test.statistic).squeeze()),
                                "p_value": float(np.asarray(test.pvalue).squeeze()),
                                "df": len(event_names),
                                "n_obs": int(fit_model.nobs),
                            }
                        )
                    if outcome == "ln_cdr" and sample["share_65plus"].notna().any():
                        try:
                            X, terms = design_matrix(
                                sample.dropna(subset=["share_65plus"]),
                                flag,
                                "year",
                                "muni_code",
                                2010,
                                event=True,
                                age_control=True,
                            )
                            aged = sample.dropna(subset=["share_65plus"])
                            fit_model = (
                                sm.WLS(aged["ln_cdr"], X, weights=aged["pop"])
                                if weight_col
                                else sm.OLS(aged["ln_cdr"], X)
                            ).fit(
                                cov_type="cluster",
                                cov_kwds={"groups": aged["muni_code"]},
                            )
                            if all(name in fit_model.params.index for name in event_names):
                                restriction = np.zeros((len(event_names), len(fit_model.params)))
                                for index, name in enumerate(event_names):
                                    restriction[index, fit_model.params.index.get_loc(name)] = 1
                                test = fit_model.wald_test(restriction, use_f=False)
                                wald_rows.append(
                                    {
                                        "control_pool": control_name,
                                        "treatment": treatment,
                                        "weighting": weighting,
                                        "outcome": "ln_cdr",
                                        "age_control": True,
                                        "test": "joint_pretrend_2006_2009",
                                        "statistic_type": "chi2",
                                        "statistic": float(np.asarray(test.statistic).squeeze()),
                                        "p_value": float(np.asarray(test.pvalue).squeeze()),
                                        "df": len(event_names),
                                        "n_obs": int(fit_model.nobs),
                                    }
                                )
                            age_rows = []
                            for year in sorted(aged["year"].unique()):
                                if year == 2010:
                                    continue
                                name = f"event_{year}"
                                beta = float(fit_model.params.get(name, np.nan))
                                se = float(fit_model.bse.get(name, np.nan))
                                age_rows.append(
                                    {
                                        "event_year": year,
                                        "beta": beta,
                                        "se": se,
                                        "ci_low": beta - 1.96 * se,
                                        "ci_high": beta + 1.96 * se,
                                        "ref_year": 2010,
                                        "n_obs": int(fit_model.nobs),
                                        "control_pool": control_name,
                                        "treatment": treatment,
                                        "weighting": weighting,
                                        "outcome": "ln_cdr",
                                        "age_control": True,
                                    }
                                )
                            rows.append(pd.DataFrame(age_rows))
                        except Exception as exc:
                            obstacles.append(
                                {
                                    "analysis": "Fukushima age-structure robustness",
                                    "control": control_name,
                                    "treatment": treatment,
                                    "weighting": weighting,
                                    "reason": f"{type(exc).__name__}: {exc}",
                                }
                            )
    events = pd.concat(
        [row if isinstance(row, pd.DataFrame) else pd.DataFrame([row]) for row in rows],
        ignore_index=True,
    ) if rows else pd.DataFrame()
    return events, pd.DataFrame(wald_rows)


def download_if_missing(path: Path, url: str) -> None:
    if path.exists() and path.stat().st_size > 0:
        return
    response = requests.get(url, timeout=180)
    response.raise_for_status()
    path.write_bytes(response.content)


def ensure_external_sources() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    download_if_missing(DAMAGE_REPORT, DAMAGE_REPORT_URL)
    download_if_missing(WHO_REPORT, WHO_URL)
    download_if_missing(UNSCEAR_REPORT, UNSCEAR_URL)
    download_if_missing(TEN_HOEVE_REPORT, TEN_HOEVE_URL)
    if not DAMAGE_TEXT.exists():
        subprocess.run(
            ["pdftotext", "-layout", str(DAMAGE_REPORT), str(DAMAGE_TEXT)],
            check=True,
        )


def parse_damage_counts() -> pd.DataFrame:
    names = sorted(T1_NAMES | T2_NAMES, key=len, reverse=True)
    rows = []
    in_table = False
    for line in DAMAGE_TEXT.read_text(encoding="utf-8", errors="replace").splitlines():
        if "直接死" in line and "関連死" in line:
            in_table = True
            continue
        if in_table and line.startswith("※1"):
            break
        if not in_table:
            continue
        if not re.match(r"^\s*\d{1,4}\s", line):
            continue
        name = next((candidate for candidate in names if candidate in line), None)
        if name is None:
            continue

        def parse_field(start: int, end: int | None = None) -> float:
            value = line[start:] if end is None else line[start:end]
            match = re.match(r"\s*([0-9][0-9,]*)", value)
            return float(match.group(1).replace(",", "")) if match else 0.0

        rows.append(
            {
                "muni_name": name,
                "direct_deaths_2011": parse_field(13, 19),
                "related_deaths_2011": parse_field(19),
                "source": "Fukushima prefecture disaster-damage report, report 1260, p. 4",
            }
        )
    result = pd.DataFrame(rows).drop_duplicates("muni_name")
    expected = T1_NAMES | T2_NAMES
    missing = sorted(expected - set(result["muni_name"]))
    if missing:
        raise ValueError(f"damage report counts missing municipalities: {missing}")
    return result


def acute_decomposition(panel: pd.DataFrame, metadata: dict[str, object]) -> pd.DataFrame:
    damage = parse_damage_counts()
    controls = metadata["control_codes"]
    control = panel.loc[
        panel["muni_code"].isin(controls) & panel["year"].isin([2010, 2011])
    ].groupby("year")[["deaths", "pop"]].sum(min_count=1)
    control["cdr"] = 1000 * control["deaths"] / control["pop"]
    control_ratio = float(control.loc[2011, "cdr"] / control.loc[2010, "cdr"])
    codes = panel[["muni_code", "muni_name"]].drop_duplicates()
    target = panel.loc[
        panel["muni_name"].isin(T1_NAMES | T2_NAMES)
        & panel["year"].isin([2010, 2011])
    ].merge(codes, on=["muni_code", "muni_name"], how="left")
    wide = target.pivot(index=["muni_code", "muni_name"], columns="year", values=["deaths", "pop"])
    wide.columns = [f"{a}_{b}" for a, b in wide.columns]
    result = wide.reset_index()
    result["cdr_2010"] = 1000 * result["deaths_2010"] / result["pop_2010"]
    result["expected_2011"] = result["pop_2011"] * (
        result["cdr_2010"] * control_ratio
    ) / 1000
    result["excess_2011"] = result["deaths_2011"] - result["expected_2011"]
    result = result.merge(damage, on="muni_name", how="left")
    result["group"] = np.where(result["muni_name"].isin(T1_NAMES), "T1", "T2")
    pooled = (
        result.groupby("group", as_index=False)[
            ["deaths_2011", "expected_2011", "excess_2011", "direct_deaths_2011", "related_deaths_2011"]
        ]
        .sum()
        .assign(muni_name="pooled")
    )
    pooled["muni_code"] = ""
    pooled["cdr_2010"] = np.nan
    pooled["pop_2010"] = np.nan
    pooled["pop_2011"] = np.nan
    pooled["source"] = "Summed municipality rows; direct counts are event counts approximately recorded in 2011"
    result["residual_2011"] = result["excess_2011"] - result["direct_deaths_2011"]
    pooled["residual_2011"] = pooled["excess_2011"] - pooled["direct_deaths_2011"]
    pooled["source"] = "Summed municipality rows; direct counts are event counts approximately recorded in 2011"
    for column in result.columns:
        if column not in pooled:
            pooled[column] = np.nan
    result = pd.concat([result, pooled[result.columns]], ignore_index=True)
    result["control_cdr_ratio_2011_to_2010"] = control_ratio
    result.to_csv(RESULTS / "acute_2011_decomposition.csv", index=False)
    return result


def write_lnt_comparison() -> pd.DataFrame:
    rows = [
        {
            "quantity": "WHO leukemia lifetime-risk relative increase",
            "value": "up to 7%",
            "unit": "relative increase over baseline",
            "verbatim_quote": "For leukaemia, the lifetime risks are predicted to increase by up to around 7% over baseline cancer rates in males exposed as infants;",
            "page": 8,
            "source_url": WHO_URL,
        },
        {
            "quantity": "WHO breast-cancer lifetime-risk relative increase",
            "value": "up to 6%",
            "unit": "relative increase over baseline",
            "verbatim_quote": "for breast cancer, the estimated lifetime risks increase by up to around 6% over baseline rates in females exposed as infants;",
            "page": 8,
            "source_url": WHO_URL,
        },
        {
            "quantity": "WHO all-solid-cancer lifetime-risk relative increase",
            "value": "up to 4%",
            "unit": "relative increase over baseline",
            "verbatim_quote": "for all solid cancers, the estimated lifetime risks increase by up to around 4% over baseline rates in females exposed as infants;",
            "page": 8,
            "source_url": WHO_URL,
        },
        {
            "quantity": "WHO thyroid-cancer lifetime-risk relative increase",
            "value": "up to 70%",
            "unit": "relative increase over baseline",
            "verbatim_quote": "and for thyroid cancer, the estimated lifetime risk increases by up to around 70% over baseline rates in females exposed as infants.",
            "page": 8,
            "source_url": WHO_URL,
        },
        {
            "quantity": "WHO conclusion outside Japan",
            "value": "no discernible increase",
            "unit": "health risks",
            "verbatim_quote": "This health risk assessment concludes that no discernible increase in health risks from the Fukushima event is expected outside Japan.",
            "page": 9,
            "source_url": WHO_URL,
        },
        {
            "quantity": "UNSCEAR collective effective dose, first year",
            "value": 18,
            "unit": "thousand man-sieverts, Japanese population",
            "verbatim_quote": "Collective effective dose (thousand man-sieverts) 18 36 48",
            "page": 60,
            "source_url": UNSCEAR_URL,
        },
        {
            "quantity": "UNSCEAR collective effective dose, first ten years",
            "value": 36,
            "unit": "thousand man-sieverts, Japanese population",
            "verbatim_quote": "Collective effective dose (thousand man-sieverts) 18 36 48",
            "page": 60,
            "source_url": UNSCEAR_URL,
        },
        {
            "quantity": "UNSCEAR collective effective dose, lifetime",
            "value": 48,
            "unit": "thousand man-sieverts, Japanese population",
            "verbatim_quote": "Collective effective dose (thousand man-sieverts) 18 36 48",
            "page": 60,
            "source_url": UNSCEAR_URL,
        },
        {
            "quantity": "UNSCEAR conclusion on discernibility",
            "value": "not expected to be discernible",
            "unit": "general radiation-related increase in health-effect incidence",
            "verbatim_quote": "A general radiation-related increase in the incidence of health effects among the exposed population would not be expected to be discernible over the baseline level.",
            "page": 77,
            "source_url": UNSCEAR_URL,
        },
        {
            "quantity": "ten Hoeve and Jacobson projected worldwide cancer mortalities",
            "value": "15–1100 (best estimate 130)",
            "unit": "excess cancer-related mortalities",
            "verbatim_quote": "We estimate an additional 130 (15–1100) cancer-related mortalities",
            "page": 1,
            "source_url": TEN_HOEVE_URL,
        },
        {
            "quantity": "ten Hoeve and Jacobson evacuation-avoided radiological mortalities",
            "value": "3–245 (best estimate 28)",
            "unit": "potentially prevented radiological mortalities",
            "verbatim_quote": "We calculated that evacuation procedures after the accident may have potentially reduced radiological mortalities by up to 22%. A 22% reduction translates into a prevention of 3–245 mortalities with a best estimate of 28 mortalities.",
            "page": 12,
            "source_url": TEN_HOEVE_URL,
        },
        {
            "quantity": "Reconstruction Agency Fukushima prefecture earthquake-related deaths",
            "value": 2350,
            "unit": "persons",
            "verbatim_quote": "福島県       2,350",
            "page": 2,
            "source_url": "https://www.reconstruction.go.jp/files/user/topics/main-cat2/sub-cat2-6/20260213_kanrenshi.pdf",
        },
    ]
    result = pd.DataFrame(rows, columns=["quantity", "value", "unit", "verbatim_quote", "page", "source_url"])
    result.to_csv(RESULTS / "lnt_comparison.csv", index=False)
    return result


def plot_descriptive(panel: pd.DataFrame, metadata: dict[str, object]) -> None:
    groups = {
        "T1": metadata["t1_codes"],
        "T1w": sorted(panel.loc[panel["treated_t1w"] == 1, "muni_code"].unique()),
        "T2": sorted(panel.loc[panel["treated_t2"] == 1, "muni_code"].unique()),
        "Control": metadata["control_codes"],
    }
    figure, axis = plt.subplots(figsize=(8, 4.5))
    for label, codes in groups.items():
        grouped = panel.loc[panel["muni_code"].isin(codes)].groupby("year")[["deaths", "pop"]].sum(min_count=1)
        axis.plot(grouped.index, 1000 * grouped["deaths"] / grouped["pop"], label=label)
    axis.axvline(2011, color="black", linestyle="--", linewidth=0.8)
    axis.set_xlabel("Year")
    axis.set_ylabel("Crude death rate per 1,000")
    axis.set_title("Pooled crude death rates")
    axis.legend()
    figure.tight_layout()
    figure.savefig(FIGURES / "pooled_cdr_groups.png", dpi=160)
    plt.close(figure)


def plot_event_coefficients(event: pd.DataFrame, treatment: str, weighting: str, filename: str) -> None:
    subset = event.loc[
        (event["control_pool"] == "all_prefectures")
        & (event["treatment"] == treatment)
        & (event["weighting"] == weighting)
        & (event["outcome"] == "ln_cdr")
        & (~event["age_control"])
    ].sort_values("event_year")
    if subset.empty:
        return
    figure, axis = plt.subplots(figsize=(7, 4))
    axis.errorbar(
        subset["event_year"],
        subset["beta"],
        yerr=[subset["beta"] - subset["ci_low"], subset["ci_high"] - subset["beta"]],
        fmt="o-",
    )
    axis.axhline(0, color="black", linewidth=0.8)
    axis.axvline(2010, color="black", linestyle="--", linewidth=0.8)
    axis.set_xlabel("Event year")
    axis.set_ylabel("Log crude death-rate coefficient")
    axis.set_title(f"{treatment} event study ({weighting})")
    figure.tight_layout()
    figure.savefig(FIGURES / filename, dpi=160)
    plt.close(figure)


def plot_acute(result: pd.DataFrame) -> None:
    subset = result.loc[result["muni_name"] == "pooled"].copy()
    figure, axis = plt.subplots(figsize=(7, 4))
    x = np.arange(len(subset))
    axis.bar(x - 0.18, subset["excess_2011"], width=0.36, label="Excess deaths")
    axis.bar(x + 0.18, subset["direct_deaths_2011"], width=0.36, label="Direct deaths")
    axis.set_xticks(x, subset["group"])
    axis.set_ylabel("Deaths")
    axis.set_title("Acute 2011 death decomposition")
    axis.legend()
    figure.tight_layout()
    figure.savefig(FIGURES / "acute_2011_decomposition.png", dpi=160)
    plt.close(figure)


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    ensure_external_sources()
    font_check = confirm_english_font()
    panel = load_panel()
    sample, metadata = sample_frame(panel)
    obstacles: list[dict[str, object]] = []
    controls = metadata["control_codes"]

    descriptive_rows = []
    descriptive_groups = {
        "T1": metadata["t1_codes"],
        "T1w": sorted(panel.loc[panel["treated_t1w"] == 1, "muni_code"].unique()),
        "T2": sorted(panel.loc[panel["treated_t2"] == 1, "muni_code"].unique()),
        "control": controls,
    }
    for label, codes in descriptive_groups.items():
        grouped = panel.loc[panel["muni_code"].isin(codes)].groupby("year")[["deaths", "pop"]].sum(min_count=1)
        grouped["cdr"] = 1000 * grouped["deaths"] / grouped["pop"]
        grouped["group"] = label
        descriptive_rows.append(grouped.reset_index())
    pd.concat(descriptive_rows, ignore_index=True).to_csv(RESULTS / "descriptive_cdr.csv", index=False)
    plot_descriptive(panel, metadata)

    event, wald = event_studies(sample, controls, obstacles)
    event.to_csv(RESULTS / "did_event_study.csv", index=False)
    wald.to_csv(RESULTS / "pretrend_wald_tests.csv", index=False)
    plot_event_coefficients(event, "T1", "weighted", "event_study_t1_weighted_all_prefectures.png")
    plot_event_coefficients(event, "T1", "unweighted", "event_study_t1_unweighted_all_prefectures.png")
    plot_event_coefficients(event, "T1w", "weighted", "event_study_t1w_weighted_all_prefectures.png")

    permutation_rows = []
    permutation_lookup = {}
    fuku_controls = [
        code for code in controls
        if not panel.loc[panel["muni_code"] == code, "pref_code"].empty
        and panel.loc[panel["muni_code"] == code, "pref_code"].iloc[0] == "07"
    ]
    treatment_name_map = {"T1": T1_NAMES, "T1w": T1W_NAMES, "T2": T2_NAMES}
    for treatment, names in treatment_name_map.items():
        treatment_codes = sorted(sample.loc[sample["muni_name"].isin(names), "muni_code"].unique())
        for control_name, pool in [
            ("all_prefectures", controls),
            ("fukushima_only", fuku_controls),
        ]:
            for weighting, weighted in [("weighted", True), ("unweighted", False)]:
                for age_control in [False, True]:
                    try:
                        inference = permutation_fe_inference(
                            sample,
                            treatment_codes,
                            pool,
                            weighted=weighted,
                            age_control=age_control,
                        )
                    except Exception as exc:
                        obstacles.append(
                            {
                                "analysis": "Fukushima permutation inference",
                                "treatment": treatment,
                                "control_pool": control_name,
                                "weighting": weighting,
                                "age_control": age_control,
                                "reason": f"{type(exc).__name__}: {exc}",
                            }
                        )
                        continue
                    row = {
                        "treatment": treatment,
                        "control_pool": control_name,
                        "weighting": weighting,
                        "outcome": "ln_cdr",
                        "age_control": age_control,
                        **inference,
                    }
                    permutation_rows.append(row)
                    if not age_control:
                        permutation_lookup[(treatment, control_name, weighting)] = inference["perm_p_att"]
    pd.DataFrame(permutation_rows).to_csv(
        RESULTS / "did_permutation_inference.csv", index=False
    )

    att_rows = []
    excess_rows = []
    annual_excess_rows = []
    for treatment, flag in [("T1", "treated_t1"), ("T1w", "treated_t1w"), ("T2", "treated_t2")]:
        treatment_names = T1_NAMES if treatment == "T1" else T1W_NAMES if treatment == "T1w" else T2_NAMES
        treatment_codes = sorted(
            sample.loc[sample["muni_name"].isin(treatment_names), "muni_code"].unique()
        )
        att_data = sample.loc[sample["muni_code"].isin([*treatment_codes, *controls])].copy()
        for adjustment, pop_col, outcome in [
            ("raw", "pop", "ln_cdr"),
            ("scope_robustness", "pop_robust", "ln_cdr_robust"),
        ]:
            try:
                estimate = estimate_att(att_data, flag, outcome, pop_col=pop_col, exclude_years=[2011])
            except Exception as exc:
                obstacles.append({"analysis": "Fukushima ATT", "treatment": treatment, "adjustment": adjustment, "reason": f"{type(exc).__name__}: {exc}"})
                continue
            estimate.update({"treatment": treatment, "adjustment": adjustment})
            if adjustment == "raw":
                estimate["perm_p"] = permutation_lookup.get(
                    (treatment, "all_prefectures", "weighted"), np.nan
                )
            att_rows.append(estimate)
            excess_rows.append(
                {
                    "treatment": treatment,
                    "adjustment": adjustment,
                    "quantity": "estimated excess deaths",
                    "value": estimate["excess_deaths"],
                    "ci_low": estimate["excess_deaths_ci_low"],
                    "ci_high": estimate["excess_deaths_ci_high"],
                    "source": "Fukushima municipal panel and ATT model",
                }
            )
            for annual in estimate["excess_deaths_by_year"]:
                annual_excess_rows.append(
                    {
                        "treatment": treatment,
                        "adjustment": adjustment,
                        **annual,
                    }
                )
    pd.DataFrame(att_rows).to_csv(RESULTS / "att_summary.csv", index=False)
    pd.DataFrame(annual_excess_rows).to_csv(RESULTS / "excess_deaths_by_year.csv", index=False)

    related = pd.read_csv(RELATED)
    related_map = related.set_index("muni_name")["related_deaths"].to_dict()
    for row in excess_rows:
        names = T1_NAMES if row["treatment"] == "T1" else T1W_NAMES if row["treatment"] == "T1w" else T2_NAMES
        row["reconstruction_related_deaths"] = sum(related_map.get(name, 0) for name in names)
    pd.DataFrame(excess_rows).to_csv(RESULTS / "excess_deaths.csv", index=False)

    unit_sc, aggregate_sc = run_synthetic_controls(panel, metadata, obstacles)
    unit_sc.to_csv(RESULTS / "sc_unit_summary.csv", index=False)
    aggregate_sc.to_csv(RESULTS / "sc_aggregate.csv", index=False)

    placebo_rows = []
    placebo_codes = sorted(
        sample.loc[sample["treated_t1"] == 1, "muni_code"].unique()
    )
    placebo_data = panel.loc[
        panel["muni_code"].isin([*placebo_codes, *controls])
        & panel["year"].between(2005, 2010)
    ].copy()
    placebo_data["placebo_t1"] = placebo_data["treated_t1"]
    try:
        placebo_att = estimate_att(
            placebo_data.rename(columns={"ln_cdr": "placebo_outcome"}),
            "placebo_t1",
            "placebo_outcome",
            post_start=2008,
            post_end=2010,
            exclude_years=[],
            start_year=2005,
        )
        placebo_att.update({"analysis": "DiD", "placebo_year": 2008})
        placebo_rows.append(placebo_att)
    except Exception as exc:
        obstacles.append({"analysis": "Fukushima in-time placebo DiD", "reason": f"{type(exc).__name__}: {exc}"})
    if placebo_rows:
        placebo_rows[0]["strength_note"] = (
            "Short placebo window (2005-2010); interpret as weak pre-treatment diagnostic."
        )
    else:
        placebo_rows.append(
            {
                "analysis": "DiD",
                "placebo_year": 2008,
                "strength_note": "Not estimable with complete 2005-2010 observations.",
            }
        )
    pd.DataFrame(placebo_rows).to_csv(RESULTS / "placebo_in_time.csv", index=False)

    acute = acute_decomposition(panel, metadata)
    plot_acute(acute)
    write_lnt_comparison()

    exclusion_rows = []
    for code in metadata["mass_casualty_control_exclusions"]:
        row = panel.loc[panel["muni_code"] == code].sort_values("year").iloc[-1]
        exclusion_rows.append(
            {
                "pref_code": str(row["pref_code"]).zfill(2),
                "pref_name": PREF_ROMAJI.get(str(row["pref_code"]).zfill(2), "Unknown"),
                "muni_code": str(code).zfill(5),
                "muni_name_romaji": MUNI_ROMAJI.get(
                    str(row["muni_name"]), str(code).zfill(5)
                ),
                "reason": "deaths_2011 / mean(deaths_2006-2010) > 1.20",
                "ratio": metadata["mass_casualty_control_ratios"][code],
            }
        )
    pd.DataFrame(
        exclusion_rows,
        columns=[
            "pref_code",
            "pref_name",
            "muni_code",
            "muni_name_romaji",
            "reason",
            "ratio",
        ],
    ).to_csv(RESULTS / "control_exclusions.csv", index=False)
    pd.DataFrame(
        metadata["dropped_units"],
        columns=[
            "pref_code",
            "pref_name",
            "muni_code",
            "muni_name_romaji",
            "reason",
            "years_missing",
        ],
    ).to_csv(RESULTS / "dropped_units.csv", index=False)
    treatment_groups = {
        "T1": sorted(
            {
                MUNI_ROMAJI.get(name, name)
                for name in T1_NAMES
            }
        ),
        "T1w": sorted(
            {
                MUNI_ROMAJI.get(name, name)
                for name in T1W_NAMES
            }
        ),
        "T2": sorted(
            {
                MUNI_ROMAJI.get(name, name)
                for name in T2_NAMES
            }
        ),
    }
    metadata.update(
        {
            "treatment_groups": treatment_groups,
            "treatment_groups_japanese": {
                "T1": sorted(T1_NAMES),
                "T1w": sorted(T1W_NAMES),
                "T2": sorted(T2_NAMES),
            },
            "control_arithmetic": {
                "complete_units": metadata["n_complete_units"],
                "treated_units": len(set(metadata["t1_codes"]) | set(metadata["t2_codes"])),
                "tsunami_excluded_control_units": metadata[
                    "n_mass_casualty_control_exclusions"
                ],
                "controls": len(controls),
                "formula": (
                    f"{metadata['n_complete_units']} complete units - "
                    f"{len(set(metadata['t1_codes']) | set(metadata['t2_codes']))} treated units - "
                    f"{metadata['n_mass_casualty_control_exclusions']} "
                    f"tsunami-excluded units = {len(controls)} controls"
                ),
            },
            "n_units": {
                "complete_sample": int(sample["muni_code"].nunique()),
                "control_pool": len(controls),
                "T1": len(T1_NAMES),
                "T1w": len(T1W_NAMES),
                "T2": len(T2_NAMES),
                "sc_unit_results": int(len(unit_sc)),
                "sc_aggregate_donors": int(aggregate_sc["n_donors"].iloc[0]) if not aggregate_sc.empty else 0,
                "analysis_years": "2005-2022",
                "complete_case_years": "2005-2019",
                "sc_pre_years": "2006-2010",
            },
            "denominator_caveat": "住民基本台帳 retains evacuees' registered residence and deaths are tabulated by registered address; numerator and denominator are therefore aligned. Pre-2013 population excludes foreign residents; the scope-adjusted robustness is reported.",
            "scope_robustness": "For units with 2012 and 2013 denominators, the 2013/2012 log ratio is linearly interpolated over 2005-2012 and used in pop_robust.",
            "pretrend_wald_test": "Cluster-robust chi-square tests that event-study coefficients for 2006-2009 equal zero are secondary; permutation statistics and p-values are in did_permutation_inference.csv.",
            "permutation_inference": {
                "draws": PERMUTATION_DRAWS,
                "seed": PERMUTATION_SEED,
                "att_p_value": "share of absolute placebo ATT values at least as large as the actual absolute ATT",
                "pretrend_statistic": "sum of squared event-study coefficients for 2006-2009",
            },
            "synthetic_control_donor_restriction": {
                "prefecture": "07 Fukushima",
                "municipal_population_match": "2010 population within 0.25x-4x treated population",
                "share_65plus_match": "2010 census share within +/-0.10",
                "aggregate_t1_age_reference": "population-weighted pooled T1 share_65plus",
                "crossfit_threshold": 1e-4,
            },
            "placebo_design": "DiD placebo uses pseudo-treatment year 2008 and observations from 2005-2010; the short window is flagged as weak. In-time placebo synthetic control is omitted.",
            "obstacles": obstacles,
            "duplicate_rows_collapsed_for_analysis": int(panel.attrs.get("duplicate_rows_collapsed", 0)),
            "matplotlib_font_check": font_check,
            "unit_verification": {
                "sources_checked": [
                    "fukushima/data/SOURCES.md",
                    "fukushima/data/raw/vital_2010_07.csv",
                    "fukushima/data/raw/resident_register_2010.xlsx",
                ],
                "vital_raw_header": ["出生数", "死亡数"],
                "panel_units": {
                    "deaths": "annual municipality death count",
                    "births": "annual municipality birth count",
                    "pop": "resident-register persons; 03-31 pre-2013 Japanese residents and 01-01 2013+ total residents",
                    "cdr": "1,000 * deaths / pop",
                },
                "denominator_scope_finding": "SOURCES.md documents Japanese-resident scope before 2013 and total scope from 2013; registered-address deaths and registered-residence population are aligned for evacuees.",
            },
        }
    )
    (RESULTS / "sample_summary.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
