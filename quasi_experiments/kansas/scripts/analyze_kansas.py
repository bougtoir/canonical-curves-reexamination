"""Synthetic-control and event-study analyses for the Kansas tax change."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT.parent
sys.path.insert(0, str(PROJECT))

from common.synth import did_event_study, permutation_inference, synthetic_control


DATA = ROOT / "data"
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
PANEL_PATH = DATA / "state_panel.csv"
MAIN_POST = list(range(2013, 2018))
EXTENSION = list(range(2018, 2020))
PRE = list(range(1997, 2013))
ANALYSIS_YEARS = list(range(1997, 2020))
OUTCOMES = ["ln_rgdp_pc", "ln_emp", "ln_real_tax_pc", "ln_real_iit_pc"]
CONTIGUOUS_PLUS_DC = {
    "AL", "AR", "AZ", "CA", "CO", "CT", "DC", "DE", "GA", "IA", "ID", "IL",
    "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", "MS", "MT",
    "NC", "ND", "NE", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", "PA", "RI",
    "SC", "SD", "TN", "TX", "UT", "VA", "VT", "WA", "WI", "WV", "WY",
}
RATE_CHANGE_EXCLUSIONS = ["NC", "OK", "WI", "OH", "ME", "IN", "ND"]
NO_BROAD_INCOME_TAX = ["TX", "FL", "WA", "NV", "SD", "WY", "AK", "NH", "TN"]
NEIGHBORS = ["NE", "MO", "CO", "IA"]


def confirm_english_font() -> dict[str, object]:
    labels = ["Year", "Kansas", "Synthetic Kansas", "Event-study coefficient"]
    if not all(label.isascii() for label in labels):
        raise ValueError("non-English figure label detected")
    figure, axis = plt.subplots(figsize=(2, 1))
    axis.set_xlabel(labels[0])
    axis.set_ylabel(labels[3])
    figure.canvas.draw()
    plt.close(figure)
    return {"font_family": plt.rcParams["font.family"], "labels_ascii": True}


def add_derived_outcomes(panel: pd.DataFrame) -> pd.DataFrame:
    frame = panel.copy()
    frame["ln_rgdp_pc"] = np.log(frame["rgdp"] * 1e6 / (frame["pop"] * 1e3))
    frame["ln_emp"] = np.log(frame["nonfarm_emp"])
    cpi_2012 = float(frame.loc[frame["year"] == 2012, "cpi"].mean())
    frame["real_tax_pc"] = frame["tax_total"] * 1e3 / (frame["pop"] * 1e3) / (
        frame["cpi"] / cpi_2012
    )
    frame["real_iit_pc"] = frame["tax_indiv_inc"] * 1e3 / (frame["pop"] * 1e3) / (
        frame["cpi"] / cpi_2012
    )
    frame["ln_real_tax_pc"] = np.log(frame["real_tax_pc"].where(frame["real_tax_pc"] > 0))
    frame["ln_real_iit_pc"] = np.log(frame["real_iit_pc"].where(frame["real_iit_pc"] > 0))
    return frame


def wide(panel: pd.DataFrame, outcome: str, units: list[str], years: list[int]) -> pd.DataFrame:
    return panel.loc[panel["state"].isin(units) & panel["year"].isin(years)].pivot(
        index="year", columns="state", values=outcome
    ).sort_index()


def complete_units(frame: pd.DataFrame, units: list[str], years: list[int], outcome: str) -> list[str]:
    wide_frame = wide(frame, outcome, units, years)
    return [unit for unit in units if unit in wide_frame and wide_frame[unit].notna().all()]


def save_sc_figures(
    outcome: str,
    result,
    permutation: pd.DataFrame,
    path_stem: str,
) -> None:
    years = result.gaps.index
    plt.figure(figsize=(8, 4.5))
    plt.plot(years, result.synthetic + result.gaps, label="Kansas", linewidth=2)
    plt.plot(years, result.synthetic, label="Synthetic Kansas", linewidth=2)
    plt.axvline(2013, color="black", linestyle="--", label="2013 treatment")
    plt.axvline(2017, color="gray", linestyle=":", label="2017 reversal")
    plt.xlabel("Year")
    plt.ylabel(outcome)
    plt.title(f"Kansas synthetic control: {outcome}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIGURES / f"{path_stem}_path.png", dpi=160)
    plt.close()

    plt.figure(figsize=(8, 4.5))
    plt.axhline(0, color="black", linewidth=0.8)
    plt.plot(years, result.gaps, color="tab:red")
    plt.axvline(2013, color="black", linestyle="--")
    plt.axvline(2017, color="gray", linestyle=":")
    plt.xlabel("Year")
    plt.ylabel("Kansas minus synthetic gap")
    plt.title(f"Kansas synthetic-control gap: {outcome}")
    plt.tight_layout()
    plt.savefig(FIGURES / f"{path_stem}_gap.png", dpi=160)
    plt.close()

    plt.figure(figsize=(6, 4))
    permutation = permutation.sort_values("ratio")
    plt.bar(permutation["unit"], permutation["ratio"], color="tab:blue")
    plt.xticks(rotation=90)
    plt.axhline(
        permutation.loc[permutation["is_treated"], "ratio"].iloc[0],
        color="tab:red",
        linestyle="--",
        label="Kansas ratio",
    )
    plt.ylabel("Post/pre RMSPE ratio")
    plt.title(f"Permutation inference: {outcome}")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIGURES / f"{path_stem}_permutation.png", dpi=160)
    plt.close()


def estimate_sc(
    frame: pd.DataFrame,
    outcome: str,
    pool_name: str,
    pool: list[str],
    pre_years: list[int],
    post_years: list[int],
    summary_rows: list[dict[str, object]],
    obstacles: list[dict[str, object]],
    write_figures: bool = False,
) -> None:
    years = [*pre_years, *post_years]
    units = complete_units(frame, ["KS", *pool], years, outcome)
    donors = [unit for unit in pool if unit in units]
    if "KS" not in units or not donors:
        obstacles.append(
            {
                "outcome": outcome,
                "pool": pool_name,
                "reason": "insufficient complete treated/donor units",
                "n_complete_total": len(units),
                "n_donors": len(donors),
            }
        )
        return
    Y = wide(frame, outcome, ["KS", *donors], years)
    try:
        result = synthetic_control(Y, "KS", donors, pre_years)
        permutation = permutation_inference(Y, "KS", donors, pre_years, post_years)
    except ValueError as exc:
        obstacles.append({"outcome": outcome, "pool": pool_name, "reason": str(exc)})
        return
    post_gap = result.gaps.loc[post_years]
    treated_mean = float(Y.loc[post_years, "KS"].mean())
    mean_gap = float(post_gap.mean())
    pct_gap = float(np.expm1(mean_gap))
    treated_perm = permutation.loc[permutation["is_treated"]]
    p_value = float(treated_perm["p_value"].iloc[0]) if not treated_perm.empty else np.nan
    summary_rows.append(
        {
            "outcome": outcome,
            "pool": pool_name,
            "post_mean_gap": mean_gap,
            "pct_gap": pct_gap,
            "perm_p": p_value,
            "rmspe_pre": result.rmspe_pre,
            "n_donors": len(donors),
            "treated_post_mean": treated_mean,
            "post_years": f"{post_years[0]}-{post_years[-1]}",
        }
    )
    suffix = "" if pool_name == "main" else f"_{pool_name}"
    result.weights.rename("weight").to_csv(RESULTS / f"sc_weights_{outcome}{suffix}.csv")
    permutation.to_csv(RESULTS / f"sc_permutation_{outcome}{suffix}.csv", index=False)
    if write_figures:
        save_sc_figures(outcome, result, permutation, f"sc_{outcome}")


def run_did(
    frame: pd.DataFrame,
    outcomes: list[str],
    units: list[str],
    pool_name: str,
    output_rows: list[pd.DataFrame],
    obstacles: list[dict[str, object]],
) -> None:
    sample = frame.loc[
        frame["state"].isin(["KS", *units]) & frame["year"].between(1997, 2019)
    ].copy()
    sample["treated"] = (sample["state"] == "KS").astype(int)
    for outcome in outcomes:
        try:
            result = did_event_study(
                sample,
                unit="state",
                time="year",
                y=outcome,
                treated_flag="treated",
                ref_year=2012,
                cluster="state",
            )
        except Exception as exc:
            obstacles.append(
                {
                    "analysis": "Kansas DiD event study",
                    "outcome": outcome,
                    "pool": pool_name,
                    "reason": f"{type(exc).__name__}: {exc}",
                }
            )
            continue
        result["outcome"] = outcome
        result["pool"] = pool_name
        output_rows.append(result)


def run_placebo(
    frame: pd.DataFrame,
    outcome: str,
    pool: list[str],
    obstacles: list[dict[str, object]],
) -> dict[str, object]:
    pre = list(range(1997, 2005))
    post = list(range(2005, 2013))
    units = complete_units(frame, ["KS", *pool], [*pre, *post], outcome)
    donors = [unit for unit in pool if unit in units]
    if "KS" not in units or not donors:
        return {
            "outcome": outcome,
            "post_mean_gap": np.nan,
            "n_donors": len(donors),
            "status": "not obtained: insufficient complete units",
        }
    try:
        result = synthetic_control(wide(frame, outcome, ["KS", *donors], [*pre, *post]), "KS", donors, pre)
        return {
            "outcome": outcome,
            "post_mean_gap": float(result.gaps.loc[post].mean()),
            "rmspe_pre": result.rmspe_pre,
            "n_donors": len(donors),
            "status": "ok",
        }
    except ValueError as exc:
        obstacles.append({"analysis": "Kansas in-time placebo", "outcome": outcome, "reason": str(exc)})
        return {"outcome": outcome, "post_mean_gap": np.nan, "status": str(exc)}


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    font_check = confirm_english_font()
    panel = add_derived_outcomes(pd.read_csv(PANEL_PATH))
    available = sorted(panel["state"].unique())
    main_pool = sorted(
        CONTIGUOUS_PLUS_DC
        - {"KS"}
        - set(RATE_CHANGE_EXCLUSIONS)
        - set(NO_BROAD_INCOME_TAX)
    )
    all_pool = sorted(set(available) - {"KS"})
    neighbors = [state for state in NEIGHBORS if state in available]
    summary_rows: list[dict[str, object]] = []
    obstacles: list[dict[str, object]] = []
    for outcome in OUTCOMES:
        estimate_sc(panel, outcome, "main", main_pool, PRE, MAIN_POST, summary_rows, obstacles, True)
        estimate_sc(panel, outcome, "all", all_pool, PRE, MAIN_POST, summary_rows, obstacles, False)

    placebo_rows = [
        run_placebo(panel, outcome, main_pool, obstacles) for outcome in OUTCOMES
    ]
    pd.DataFrame(placebo_rows).to_csv(RESULTS / "placebo_in_time.csv", index=False)

    loo_rows: list[dict[str, object]] = []
    for outcome in OUTCOMES:
        units = complete_units(panel, ["KS", *main_pool], [*PRE, *MAIN_POST], outcome)
        donors = [unit for unit in main_pool if unit in units]
        if "KS" not in units or not donors:
            obstacles.append({"analysis": "Kansas leave-one-out", "outcome": outcome, "reason": "insufficient complete units"})
            continue
        Y = wide(panel, outcome, ["KS", *donors], [*PRE, *MAIN_POST])
        base = synthetic_control(Y, "KS", donors, PRE)
        weighted_donors = [d for d, w in base.weights.items() if w > 0.05]
        for dropped in weighted_donors:
            remaining = [d for d in donors if d != dropped]
            try:
                fitted = synthetic_control(Y[["KS", *remaining]], "KS", remaining, PRE)
                loo_rows.append(
                    {
                        "outcome": outcome,
                        "dropped_donor": dropped,
                        "base_weight": float(base.weights[dropped]),
                        "post_mean_gap": float(fitted.gaps.loc[MAIN_POST].mean()),
                    }
                )
            except ValueError as exc:
                obstacles.append({"analysis": "Kansas leave-one-out", "outcome": outcome, "dropped": dropped, "reason": str(exc)})
    pd.DataFrame(loo_rows).to_csv(RESULTS / "loo_robustness.csv", index=False)
    loo_summary = {}
    if loo_rows:
        loo_frame = pd.DataFrame(loo_rows)
        loo_summary = {
            outcome: {
                "min_post_mean_gap": float(group["post_mean_gap"].min()),
                "max_post_mean_gap": float(group["post_mean_gap"].max()),
                "n_dropped_donors": int(len(group)),
            }
            for outcome, group in loo_frame.groupby("outcome")
        }

    did_rows: list[pd.DataFrame] = []
    run_did(panel, OUTCOMES, neighbors, "neighbors", did_rows, obstacles)
    run_did(panel, OUTCOMES, main_pool, "main", did_rows, obstacles)
    did_output = pd.concat(did_rows, ignore_index=True) if did_rows else pd.DataFrame()
    did_output.to_csv(RESULTS / "did_event_study.csv", index=False)
    if not did_output.empty:
        for (outcome, pool), subset in did_output.groupby(["outcome", "pool"]):
            plt.figure(figsize=(7, 4))
            plt.axhline(0, color="black", linewidth=0.8)
            plt.axvline(2012, color="gray", linestyle=":")
            plt.errorbar(
                subset["event_year"],
                subset["beta"],
                yerr=1.96 * subset["se"],
                fmt="o-",
            )
            plt.xlabel("Year")
            plt.ylabel("Event-study coefficient")
            plt.title(f"Kansas DiD event study: {outcome}, {pool}")
            plt.tight_layout()
            plt.savefig(FIGURES / f"did_{outcome}_{pool}.png", dpi=160)
            plt.close()

    revenue_rows = []
    for variable in ["real_tax_pc", "real_iit_pc"]:
        outcome = variable
        units = complete_units(panel, ["KS", *main_pool], [*PRE, *MAIN_POST], outcome)
        donors = [unit for unit in main_pool if unit in units]
        if "KS" not in units or not donors:
            obstacles.append({"analysis": "Kansas revenue counterfactual", "outcome": outcome, "reason": "insufficient complete units"})
            continue
        result = synthetic_control(
            wide(panel, outcome, ["KS", *donors], [*PRE, *MAIN_POST]),
            "KS",
            donors,
            PRE,
        )
        annual = panel.loc[
            (panel["state"] == "KS") & panel["year"].isin(MAIN_POST),
            ["year", "pop", outcome],
        ].set_index("year")
        annual["synthetic"] = result.synthetic.loc[MAIN_POST]
        annual["gap_per_capita_2012_dollars"] = annual[outcome] - annual["synthetic"]
        annual["counterfactual_gap_dollars"] = (
            annual["gap_per_capita_2012_dollars"] * annual["pop"] * 1e3
        )
        annual["variable"] = variable
        revenue_rows.append(annual.reset_index())
    revenue = pd.concat(revenue_rows, ignore_index=True) if revenue_rows else pd.DataFrame()
    revenue.to_csv(RESULTS / "revenue_counterfactual.csv", index=False)

    unit_verification = {
        "rgdp": {
            "used": "millions of chained dollars, as specified for XXRGSP",
            "sources_checked": "kansas/data/SOURCES.md and raw fred_KS_rgdp_KSRGSP.csv",
            "raw_header": ["observation_date", "KSRGSP"],
            "finding": "SOURCES.md and raw CSV header identify the series but do not print a unit label; the specified FRED convention was used.",
        },
        "pop": {
            "used": "thousands of persons, as specified for XXPOP",
            "sources_checked": "kansas/data/SOURCES.md and raw fred_KS_pop KSPOP CSV",
            "finding": "Raw FRED header is date/value only; the specified series unit convention was used.",
        },
        "tax": {
            "used": "thousands of dollars in STC historical database",
            "sources_checked": "kansas/data/SOURCES.md and STC raw workbook headers",
            "finding": "SOURCES.md records C105 (total), T40, T41, and T09; the extraction notes identify the STC values as thousands of dollars.",
        },
        "employment": {
            "used": "thousands of employees, annual mean of monthly FRED XXNA",
            "sources_checked": "kansas/data/SOURCES.md and raw FRED KSNA CSV",
            "finding": "Raw FRED header is date/value only; the specified series convention was used.",
        },
    }
    metadata = {
        "treatment": "KS, first treated year 2013; reversal year 2017, extension reported through 2019",
        "pools": {
            "main": main_pool,
            "all": all_pool,
            "neighbors": neighbors,
            "rate_change_exclusions": RATE_CHANGE_EXCLUSIONS,
            "no_broad_income_tax_exclusions": NO_BROAD_INCOME_TAX,
        },
        "n_units": {
            "available": len(available),
            "main": len(main_pool),
            "all": len(all_pool),
            "neighbors": len(neighbors),
        },
        "unit_verification": unit_verification,
        "matplotlib_font_check": font_check,
        "obstacles": obstacles,
        "analysis_years": {"pre": PRE, "main_post": MAIN_POST, "extension": EXTENSION},
        "loo_ranges": loo_summary,
    }
    (RESULTS / "analysis_summary.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )
    pd.DataFrame(summary_rows).to_csv(RESULTS / "sc_summary.csv", index=False)


if __name__ == "__main__":
    main()
