"""Threshold sensitivity and decision-tree outputs for canonical-curve verdicts."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
RESULTS = ROOT / "results"
FIGURES = ROOT / "figures"
sys.path.insert(0, str(SCRIPT_DIR))

from core_analysis import CurveReexamination  # noqa: E402
import run_all_analyses as pipeline  # noqa: E402


ALPHAS = (0.01, 0.05, 0.10)
TOP_K = (1, 2, 3, 4, 5)


def collect_fit_inputs() -> dict[str, tuple[np.ndarray, np.ndarray]]:
    """Re-run the existing constructors while capturing their source arrays."""
    captured: dict[str, tuple[np.ndarray, np.ndarray]] = {}
    original = CurveReexamination.run_full_analysis

    def capture(self, *args, **kwargs):
        captured[self.name] = (self.x.copy(), self.y.copy())
        return original(self, *args, **kwargs)

    CurveReexamination.run_full_analysis = capture
    try:
        results = []
        for function in [
            pipeline.run_economics_analysis,
            pipeline.run_health_analysis,
            pipeline.run_demography_analysis,
            pipeline.run_environment_analysis,
            pipeline.run_psychology_analysis,
            pipeline.run_physics_analysis,
            pipeline.run_political_analysis,
            pipeline.run_agriculture_analysis,
        ]:
            results.extend(function())
        results = pipeline._try_real_data_substitution(results)
        results = pipeline._try_additional_real_substitution(results)
    finally:
        CurveReexamination.run_full_analysis = original
    return captured


def sensitivity_verdict(result: dict, x: np.ndarray, y: np.ndarray, alpha: float, top_k: int) -> str:
    """Apply the existing decision order with explicit alpha and Cook k."""
    curve = CurveReexamination(result["name"], x, y)
    _, p_full = curve.nested_f_test()
    sensitivity = curve.sensitivity_analysis(top_k=top_k)
    p_clean = sensitivity["p_clean"]
    rmse_lin, rmse_quad = curve.loocv_rmse()
    comparison = curve.compute_aic_bic()
    best_bic = min(comparison, key=lambda model: comparison[model]["bic"])

    if p_full >= alpha:
        return "NOT_SIGNIFICANT"
    if np.isnan(p_clean):
        return "INSUFFICIENT_DATA"
    if p_clean >= alpha:
        return "OUTLIER_DEPENDENT"
    if rmse_quad >= rmse_lin:
        return "OVERFITTING"
    if best_bic == "linear":
        return "BIC_PREFERS_LINEAR"
    return "ROBUST_NONLINEAR"


def write_sensitivity_outputs() -> tuple[pd.DataFrame, pd.DataFrame]:
    source = json.loads((RESULTS / "full_results.json").read_text(encoding="utf-8"))
    captured = collect_fit_inputs()
    rows = []
    for result in source:
        if result["name"] not in captured:
            raise RuntimeError(f"source arrays unavailable for {result['name']}")
        x, y = captured[result["name"]]
        for alpha in ALPHAS:
            for top_k in TOP_K:
                rows.append(
                    {
                        "alpha": alpha,
                        "k": top_k,
                        "curve": result["name"],
                        "verdict": sensitivity_verdict(result, x, y, alpha, top_k),
                    }
                )
    sensitivity = pd.DataFrame(rows)
    sensitivity.to_csv(RESULTS / "verdict_sensitivity.csv", index=False)

    counts = (
        sensitivity.pivot_table(
            index=["alpha", "k"],
            columns="verdict",
            values="curve",
            aggfunc="count",
            fill_value=0,
        )
        .reset_index()
    )
    verdicts = [
        "NOT_SIGNIFICANT",
        "INSUFFICIENT_DATA",
        "OUTLIER_DEPENDENT",
        "OVERFITTING",
        "BIC_PREFERS_LINEAR",
        "ROBUST_NONLINEAR",
    ]
    for verdict in verdicts:
        if verdict not in counts:
            counts[verdict] = 0
    counts["n_curves"] = counts[verdicts].sum(axis=1)
    counts["share_not_robust"] = 1 - counts["ROBUST_NONLINEAR"] / counts["n_curves"]
    counts = counts[["alpha", "k", *verdicts, "n_curves", "share_not_robust"]]
    counts.to_csv(RESULTS / "verdict_sensitivity_summary.csv", index=False)
    return sensitivity, counts


def plot_sensitivity(summary: pd.DataFrame) -> None:
    matrix = summary.pivot(index="alpha", columns="k", values="share_not_robust")
    figure, axis = plt.subplots(figsize=(7, 4.5))
    image = axis.imshow(matrix.to_numpy(), vmin=0, vmax=1, cmap="viridis", aspect="auto")
    axis.set_xticks(range(len(matrix.columns)), [str(k) for k in matrix.columns])
    axis.set_yticks(range(len(matrix.index)), [f"{alpha:.2f}" for alpha in matrix.index])
    axis.set_xlabel("Cook top-k removed")
    axis.set_ylabel("Alpha threshold")
    axis.set_title("Share not classified as robust nonlinear")
    for row in range(matrix.shape[0]):
        for column in range(matrix.shape[1]):
            axis.text(column, row, f"{matrix.iloc[row, column]:.2f}", ha="center", va="center", color="white")
    figure.colorbar(image, ax=axis, label="Share not robust")
    figure.tight_layout()
    figure.savefig(FIGURES / "verdict_sensitivity.png", dpi=180)
    plt.close(figure)


def plot_decision_tree() -> None:
    figure, axis = plt.subplots(figsize=(13, 5))
    axis.axis("off")
    boxes = [
        (0.02, 0.42, "F-test p < alpha?"),
        (0.22, 0.42, "Cook top-k removed p < alpha?"),
        (0.47, 0.42, "LOOCV RMSE quadratic < linear?"),
        (0.72, 0.42, "BIC prefers nonlinear?"),
        (0.90, 0.42, "ROBUST"),
    ]
    for x, y, label in boxes:
        axis.text(
            x,
            y,
            label,
            transform=axis.transAxes,
            ha="center",
            va="center",
            bbox={"boxstyle": "round,pad=0.7", "facecolor": "#d9eaf7", "edgecolor": "#24557a"},
            fontsize=10,
        )
    for start, end in zip(boxes[:-1], boxes[1:]):
        axis.annotate(
            "",
            xy=(end[0] - 0.06, end[1]),
            xytext=(start[0] + 0.06, start[1]),
            xycoords="axes fraction",
            arrowprops={"arrowstyle": "->", "color": "#333333", "lw": 1.5},
        )
    axis.text(0.12, 0.22, "No: NOT_SIGNIFICANT", transform=axis.transAxes, ha="center")
    axis.text(0.35, 0.22, "No: OUTLIER_DEPENDENT", transform=axis.transAxes, ha="center")
    axis.text(0.60, 0.22, "No: OVERFITTING", transform=axis.transAxes, ha="center")
    axis.text(0.82, 0.22, "No: BIC_PREFERS_LINEAR", transform=axis.transAxes, ha="center")
    figure.suptitle("Canonical curve verdict decision tree")
    figure.savefig(FIGURES / "verdict_decision_tree.png", dpi=180, bbox_inches="tight")
    plt.close(figure)


def write_policy_linkage() -> pd.DataFrame:
    source = json.loads((RESULTS / "full_results.json").read_text(encoding="utf-8"))
    default = {row["name"]: row["verdict"]["verdict"] for row in source}
    rows = [
        {
            "curve": name,
            "verdict": verdict,
            "example_policy": "ICRP Publication 103 radiological-protection standard" if "LNT" in name else "",
            "jurisdiction": "International" if "LNT" in name else "",
            "year": 2007 if "LNT" in name else "",
            "policy_document_url": "https://www.icrp.org/docs/icrp_publication_103-annals_of_the_icrp_37(2-4)-free_extract.pdf" if "LNT" in name else "",
        }
        for name, verdict in default.items()
    ]
    output = pd.DataFrame(rows, columns=[
        "curve", "verdict", "example_policy", "jurisdiction", "year", "policy_document_url"
    ])
    output.to_csv(RESULTS / "policy_linkage.csv", index=False)
    (RESULTS / "SOURCES.md").write_text(
        "# Policy-linkage sources\n\n"
        "The LNT row is filled from the International Commission on Radiological "
        "Protection's official Publication 103 page, which identifies the "
        "publication and its radiological-protection recommendations: "
        "https://www.icrp.org/docs/icrp_publication_103-annals_of_the_icrp_37(2-4)-free_extract.pdf\n\n"
        "The Kansas Senate Substitute for HB 2117 official legislative summary "
        "was reviewed, but it does not explicitly invoke the Laffer curve, so "
        "the Laffer policy fields remain empty: "
        "https://www.kslegislature.gov/li_2012/b2011_12/measures/documents/summary_hb_2117_2012.pdf\n\n"
        "Rahn/TABOR, Hubbert/EISA, and Green Revolution/Malawi candidate links "
        "were not filled because an official or primary document explicitly "
        "invoking the named curve was not verified in this run.\n",
        encoding="utf-8",
    )
    return output


def main() -> None:
    RESULTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    _, summary = write_sensitivity_outputs()
    plot_sensitivity(summary)
    plot_decision_tree()
    write_policy_linkage()


if __name__ == "__main__":
    main()
