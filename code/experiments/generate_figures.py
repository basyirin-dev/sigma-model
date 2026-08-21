"""Publication Figure Reproduction Script for the Sigma-Trap Paper.

Generates the core empirical figures presented in the manuscript:
- Figure 11: Four-arm OOD accuracy trajectories (mean ± 95% CI).
- Figure 12: Stage-1 measured schema-coherence proxy (GCA + RGA) dynamics.
- Figure 13: Segmented regression inflection latency analysis.

Usage:
    python code/experiments/generate_figures.py
    python code/experiments/generate_figures.py --results-dir paper/submission/supplementary/data/gate-results
"""

from __future__ import annotations

import argparse
import pickle
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

matplotlib.use("Agg")


CONDITION_ORDER = ["baseline", "fixed_weight", "additive", "multiplicative"]
CONDITION_LABELS = {
    "baseline": "Baseline ERM",
    "fixed_weight": "Fixed-Weight Loss (λ=1.0)",
    "additive": "Additive σ-Modulated",
    "multiplicative": "Multiplicative σ-Modulated",
}
COLORS = {
    "baseline": "#0d5a79",
    "fixed_weight": "#e35f2f",
    "additive": "#5aa01c",
    "multiplicative": "#8e44ad",
}


def mean_ci(vals: np.ndarray, alpha: float = 0.05) -> tuple[np.ndarray, np.ndarray]:
    """Calculate mean and 95% Student-t confidence interval across seeds."""
    n = vals.shape[-1]
    mu = vals.mean(-1)
    se = vals.std(-1, ddof=1) / np.sqrt(n)
    t_val = stats.t.ppf(1 - alpha / 2, max(n - 1, 1))
    return mu, t_val * se


def fit_broken_stick(x: np.ndarray, y: np.ndarray) -> tuple[float, float, float, float]:
    """Fit a two-segment continuous piecewise-linear model to find the inflection step."""
    best_tau = x[len(x) // 2]
    best_loss = float("inf")
    best_params = (0.0, 0.0, 0.0, 0.0)

    # Search interior points for the inflection
    for tau in x[4:-4]:
        x_left = np.minimum(x, tau)
        x_right = np.maximum(0, x - tau)
        mat_a = np.column_stack([np.ones_like(x), x_left, x_right])
        params, residuals, _, _ = np.linalg.lstsq(mat_a, y, rcond=None)
        pred = mat_a @ params
        loss = np.sum((y - pred) ** 2)
        if loss < best_loss:
            best_loss = loss
            best_tau = float(tau)
            best_params = (params[0], params[1], params[2], loss)

    return (best_tau,) + best_params


def generate_all_figures(results_dir: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    all_results_file = results_dir / "all_results.pkl"

    if not all_results_file.exists():
        # Fallback to loading per-run pickle files
        print(f"Loading individual run files from {results_dir} ...")
        all_results = {}
        for cond in CONDITION_ORDER:
            cond_runs = []
            for pkl_file in sorted(results_dir.glob(f"{cond}_run*.pkl")):
                with open(pkl_file, "rb") as f:
                    cond_runs.append(pickle.load(f))
            if cond_runs:
                all_results[cond] = cond_runs
    else:
        with open(all_results_file, "rb") as f:
            all_results = pickle.load(f)

    if not all_results:
        print(f"Error: No results found in {results_dir}")
        return

    # Extract steps from the first run
    first_cond = next(iter(all_results))
    first_run = all_results[first_cond][0]
    first_metrics = first_run["metrics"] if "metrics" in first_run else first_run
    steps = np.array(first_metrics["step"])

    # Helper to extract metric array across runs
    def get_metric_array(runs: list[dict], metric_key: str) -> np.ndarray:
        return np.array([
            (r["metrics"][metric_key] if "metrics" in r else r[metric_key])
            for r in runs
        ]).T

    # 1. Figure 11: OOD Accuracy Trajectories
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    for cond in CONDITION_ORDER:
        if cond not in all_results:
            continue
        ood_runs = get_metric_array(all_results[cond], "acc_ood")
        mu, ci = mean_ci(ood_runs)
        ax.plot(steps, mu * 100, label=CONDITION_LABELS[cond], color=COLORS[cond], lw=2.2)
        ax.fill_between(steps, (mu - ci) * 100, (mu + ci) * 100, color=COLORS[cond], alpha=0.15)

    ax.set_xlabel("Training Step", fontsize=11, fontweight="bold")
    ax.set_ylabel("Zero-Shot OOD Accuracy (%)", fontsize=11, fontweight="bold")
    ax.set_ylim(-2, 105)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(frameon=True, fontsize=10, loc="lower right")
    plt.tight_layout()
    fig_ood_path = output_dir / "figure11-gate-ood.png"
    fig.savefig(fig_ood_path)
    plt.close(fig)
    print(f"Saved: {fig_ood_path}")

    # 2. Figure 12: Stage-1 Proxy Dynamics
    fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
    for cond in CONDITION_ORDER:
        if cond not in all_results:
            continue
        proxy_runs = get_metric_array(all_results[cond], "sigma_tilde")
        mu, ci = mean_ci(proxy_runs)
        ax.plot(steps, mu, label=CONDITION_LABELS[cond], color=COLORS[cond], lw=2.2)
        ax.fill_between(steps, mu - ci, mu + ci, color=COLORS[cond], alpha=0.15)

    ax.set_xlabel("Training Step", fontsize=11, fontweight="bold")
    ax.set_ylabel(r"Measured Schema Coherence Proxy $\tilde{\sigma}_A(t)$", fontsize=11, fontweight="bold")
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(frameon=True, fontsize=10, loc="lower right")
    plt.tight_layout()
    fig_sigma_path = output_dir / "figure12-gate-sigma.png"
    fig.savefig(fig_sigma_path)
    plt.close(fig)
    print(f"Saved: {fig_sigma_path}")

    # 3. Figure 13: Inflection Latency Breakpoint
    if "additive" in all_results:
        fig, ax = plt.subplots(figsize=(7, 4.5), dpi=300)
        add_runs = get_metric_array(all_results["additive"], "acc_ood")
        mu, ci = mean_ci(add_runs)
        tau_hat, a, b1, b2, _ = fit_broken_stick(steps, mu * 100)

        # Plot empirical curve
        ax.plot(steps, mu * 100, label="Additive Arm Empirical Mean", color=COLORS["additive"], lw=2)
        ax.fill_between(steps, (mu - ci) * 100, (mu + ci) * 100, color=COLORS["additive"], alpha=0.15)

        # Plot fitted piecewise model
        x_left = np.minimum(steps, tau_hat)
        x_right = np.maximum(0, steps - tau_hat)
        pred = a + b1 * x_left + b2 * x_right
        ax.plot(steps, pred, label=f"Segmented Fit (Inflection $\\hat{{\\tau}} \\approx {tau_hat:.0f}$)", color="black", linestyle="--", lw=2)
        ax.axvline(tau_hat, color="red", linestyle=":", lw=1.8, label=f"Break Point $\\hat{{\\tau}} = {tau_hat:.0f}$ steps")

        ax.set_xlabel("Training Step", fontsize=11, fontweight="bold")
        ax.set_ylabel("Zero-Shot OOD Accuracy (%)", fontsize=11, fontweight="bold")
        ax.set_ylim(-2, 105)
        ax.grid(True, linestyle="--", alpha=0.5)
        ax.legend(frameon=True, fontsize=10, loc="lower right")
        plt.tight_layout()
        fig_inflect_path = output_dir / "figure13-gate-inflection.png"
        fig.savefig(fig_inflect_path)
        plt.close(fig)
        print(f"Saved: {fig_inflect_path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Publication Figures for the Sigma-Trap Paper.")
    parser.add_argument(
        "--results-dir",
        type=Path,
        default=Path("paper/submission/supplementary/data/gate-results"),
        help="Directory containing the gate experiment data files.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("paper/figures"),
        help="Directory where output figure PNGs will be saved.",
    )
    args = parser.parse_args()

    # Fallback to archive/gate-results if needed
    if not args.results_dir.exists():
        args.results_dir = Path("archive/gate-results")

    generate_all_figures(args.results_dir, args.output_dir)


if __name__ == "__main__":
    main()
