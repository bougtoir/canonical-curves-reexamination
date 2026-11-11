"""Shared synthetic-control and event-study estimators."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd
import statsmodels.api as sm
from scipy.optimize import minimize


@dataclass
class SCResult:
    weights: pd.Series
    synthetic: pd.Series
    gaps: pd.Series
    rmspe_pre: float
    rmspe_post: float
    ratio: float


def synthetic_control(
    Y: pd.DataFrame,
    treated: str,
    donors: list[str],
    pre_years: list[int],
) -> SCResult:
    """Fit non-negative, sum-to-one donor weights by pre-period RMSPE."""
    columns = [treated, *donors]
    data = Y.loc[:, columns].copy().sort_index()
    pre_data = data.loc[data.index.intersection(pre_years)].dropna()
    pre = pre_data.index
    if len(pre) == 0:
        raise ValueError(f"no complete pre-period observations for {treated}")
    if not donors:
        raise ValueError(f"no donors available for {treated}")
    target = pre_data.loc[:, treated].to_numpy(dtype=float)
    donor_values = pre_data.loc[:, donors].to_numpy(dtype=float)
    equal = np.repeat(1.0 / len(donors), len(donors))

    def objective(weights: np.ndarray) -> float:
        residual = target - donor_values @ weights
        return float(np.mean(residual**2))

    fit = minimize(
        objective,
        equal,
        method="SLSQP",
        bounds=[(0.0, 1.0)] * len(donors),
        constraints={"type": "eq", "fun": lambda weights: np.sum(weights) - 1.0},
        options={"maxiter": 2000, "ftol": 1e-12},
    )
    if not fit.success:
        raise ValueError(f"SLSQP failed for {treated}: {fit.message}")
    weights = pd.Series(fit.x, index=donors, name="weight")
    synthetic = data[donors].mul(weights, axis=1).sum(axis=1, min_count=len(donors))
    gaps = data[treated] - synthetic
    post = data.index.difference(pre).intersection(gaps.dropna().index)
    rmspe_pre = float(np.sqrt(np.mean(gaps.loc[pre] ** 2)))
    rmspe_post = float(np.sqrt(np.mean(gaps.loc[post] ** 2))) if len(post) else np.nan
    ratio = float(rmspe_post / rmspe_pre) if rmspe_pre > 0 else np.inf
    return SCResult(weights, synthetic, gaps, rmspe_pre, rmspe_post, ratio)


def permutation_inference(
    Y: pd.DataFrame,
    treated: str,
    donors: list[str],
    pre_years: list[int],
    post_years: list[int],
) -> pd.DataFrame:
    """Run treated and donor-placebo synthetic controls and calculate rank p."""
    units = [treated, *donors]
    rows: list[dict[str, object]] = []
    result_map: dict[str, SCResult] = {}
    for unit in units:
        unit_donors = [candidate for candidate in units if candidate != unit]
        try:
            result = synthetic_control(Y, unit, unit_donors, pre_years)
        except ValueError:
            continue
        post = Y.index.intersection(post_years)
        post_gap = result.gaps.loc[post]
        post_rmspe = float(np.sqrt(np.mean(post_gap**2))) if len(post_gap) else np.nan
        result_map[unit] = result
        rows.append(
            {
                "unit": unit,
                "rmspe_pre": result.rmspe_pre,
                "rmspe_post": post_rmspe,
                "ratio": post_rmspe / result.rmspe_pre
                if result.rmspe_pre > 0
                else np.inf,
                "is_treated": unit == treated,
            }
        )
    output = pd.DataFrame(rows)
    if output.empty:
        return output.assign(p_value=pd.Series(dtype=float))
    treated_rows = output.loc[output["is_treated"]]
    if treated_rows.empty:
        output["p_value"] = np.nan
        return output
    treated_ratio = float(treated_rows.iloc[0]["ratio"])
    valid = output["ratio"].notna()
    n_units = int(valid.sum())
    p_value = float((output.loc[valid, "ratio"] >= treated_ratio).sum() / n_units) if n_units else np.nan
    output["p_value"] = p_value
    return output.sort_values("unit").reset_index(drop=True)


def did_event_study(
    panel: pd.DataFrame,
    unit: str,
    time: str,
    y: str,
    treated_flag: str,
    ref_year: int,
    weights: str | pd.Series | None = None,
    cluster: str = "unit",
) -> pd.DataFrame:
    """Estimate unit/year FE event-study coefficients with clustered SEs."""
    data = panel[[unit, time, y, treated_flag]].copy()
    data = data.dropna(subset=[unit, time, y, treated_flag])
    data[time] = data[time].astype(int)
    years = sorted(data[time].unique())
    interactions: list[str] = []
    X = pd.DataFrame(index=data.index)
    for year in years:
        if year == ref_year:
            continue
        name = f"event_{year}"
        X[name] = data[treated_flag].astype(float) * (data[time] == year)
        interactions.append(name)
    unit_dummies = pd.get_dummies(data[unit].astype(str), prefix="unit", drop_first=True)
    year_dummies = pd.get_dummies(data[time], prefix="year", drop_first=True)
    X = pd.concat([X, unit_dummies, year_dummies], axis=1)
    X = sm.add_constant(X.astype(float), has_constant="add")
    if isinstance(weights, str):
        fit_weights = pd.to_numeric(panel.loc[data.index, weights], errors="coerce")
    elif isinstance(weights, pd.Series):
        fit_weights = pd.to_numeric(weights.loc[data.index], errors="coerce")
    else:
        fit_weights = None
    model = sm.WLS(data[y].astype(float), X, weights=fit_weights) if fit_weights is not None else sm.OLS(data[y].astype(float), X)
    fitted = model.fit(
        cov_type="cluster",
        cov_kwds={"groups": data[cluster].astype(str)},
    )
    rows = []
    for year in years:
        if year == ref_year:
            continue
        name = f"event_{year}"
        beta = float(fitted.params.get(name, np.nan))
        se = float(fitted.bse.get(name, np.nan))
        rows.append(
            {
                "event_year": year,
                "beta": beta,
                "se": se,
                "ci_low": beta - 1.96 * se,
                "ci_high": beta + 1.96 * se,
                "ref_year": ref_year,
                "n_obs": int(fitted.nobs),
            }
        )
    return pd.DataFrame(rows)
