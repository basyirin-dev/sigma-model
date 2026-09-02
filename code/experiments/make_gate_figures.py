"""Phase 07 gate figures + Prediction-9 breakpoint estimation.

Loads the Phase-04 gate results from ``archive/gate-results`` and produces:

- ``paper/figures/figure11-gate-ood.png`` — four-arm OOD accuracy trajectories
  (mean ± 95% CI over seeds).
- ``paper/figures/figure12-gate-sigma.png`` — measured σ̃_A (GCA+RGA proxy)
  trajectories per arm (mean ± 95% CI).
- ``paper/figures/figure13-gate-inflection.png`` — Prediction-9 inflection:
  additive-arm mean OOD trajectory with the segmented-regression breakpoint.

Also estimates the segmented-regression breakpoint τ per run and per arm
(mean/median + 95% CI) for Section 11's phase-transition timing.

Usage::

    python code/experiments/make_gate_figures.py --results-dir archive/gate-results
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

CONDITION_ORDER = ["baseline", "fixed_weight", "additive", "multiplicative"]
CONDITION_LABELS = {
    "baseline": "baseline",
    "fixed_weight": "fixed-weight comp loss",
    "additive": "additive σ-modulated",
    "multiplicative": "multiplicative σ-modulated",
}
COLORS = {
    "baseline": "#0d5a79",
    "fixed_weight": "#e35f2f",
    "additive": "#5aa01c",
    "multiplicative": "#8e44ad",
}


def load_results(results_dir: str):
    import pickle

    with open(Path(results_dir) / "all_results.pkl", "rb") as f:
        return pickle.load(f)


def mean_ci(vals: np.ndarray, alpha: float = 0.05) -> tuple[float, float]:
    """Mean and 95% CI (t-based) across the last axis."""
    n = vals.shape[-1]
    mu = vals.mean(-1)
    se = vals.std(-1, ddof=1) / np.sqrt(n)
    t = stats.t.ppf(1 - alpha / 2, max(n - 1, 1))
    return mu, t * se


def segmented_tau(steps: np.ndarray, y: np.ndarray) -> float:
    """Least-squares breakpoint for y = b0 + b1 t + b2 (t-tau)_+ over the grid.

    Returns the tau (in step units) minimising SSE, or NaN if fewer than 4 points.
    """
    steps = np.asarray(steps, dtype=float)
    y = np.asarray(y, dtype=float)
    if len(y) < 4:
        return float("nan")
    best_tau, best_sse = float("nan"), float("inf")
    for tau in steps[1:-1]:
        d = np.maximum(steps - tau, 0.0)
        x = np.column_stack([np.ones_like(steps), steps, d])
        beta, *_ = np.linalg.lstsq(x, y, rcond=None)
        sse = float(np.sum((x @ beta - y) ** 2))
        if sse < best_sse:
            best_sse, best_tau = sse, tau
    return best_tau


def main() -> None:
    ap = argparse.ArgumentParser(description="P07 gate figures + τ estimation")
    ap.add_argument("--results-dir", default="archive/gate-results")
    ap.add_argument("--outdir", default="paper01/figures")
    args = ap.parse_args()

    all_results = load_results(args.results_dir)
    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    steps = np.array(all_results[CONDITION_ORDER[0]][0]["step"])

    # Per-run matrices (n_runs × n_evals).
    ood = {c: np.array([r["acc_ood"] for r in all_results[c]]) for c in CONDITION_ORDER}
    sig = {c: np.array([r["sigma_tilde"] for r in all_results[c]]) for c in CONDITION_ORDER}

    # ---- Figure 11: OOD trajectories, mean ± 95% CI ----
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for c in CONDITION_ORDER:
        mu, ci = mean_ci(ood[c].T)  # CI across runs at each eval step
        ax.plot(steps, mu, label=CONDITION_LABELS[c], lw=2, color=COLORS[c])
        ax.fill_between(steps, mu - ci, mu + ci, alpha=0.15, color=COLORS[c])
    ax.set(xlabel="Training step", ylabel="OOD accuracy (%)",
           title="Mechanism gate: OOD accuracy trajectories (mean ± 95% CI, n=15)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(outdir / "figure11-gate-ood.png", dpi=200)
    plt.close(fig)

    # ---- Figure 12: measured σ̃_A trajectories ----
    fig, ax = plt.subplots(figsize=(7, 4.5))
    for c in CONDITION_ORDER:
        mu, ci = mean_ci(sig[c].T)  # CI across runs at each eval step
        ax.plot(steps, mu, label=CONDITION_LABELS[c], lw=2, color=COLORS[c])
        ax.fill_between(steps, mu - ci, mu + ci, alpha=0.15, color=COLORS[c])
    ax.set(xlabel="Training step", ylabel="σ̃_A (measured GCA+RGA proxy)",
           title="Measured schema-coherence proxy (mean ± 95% CI, n=15)", ylim=(0, 1))
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(outdir / "figure12-gate-sigma.png", dpi=200)
    plt.close(fig)

    # ---- Figure 13: Prediction-9 inflection (additive arm) ----
    tau_by_run = {
        c: [segmented_tau(steps, ood[c][i]) for i in range(ood[c].shape[0])]
        for c in CONDITION_ORDER
    }
    for c in CONDITION_ORDER:
        tau_by_run[c] = np.array([t for t in tau_by_run[c] if not np.isnan(t)], dtype=float)

    add = "additive"
    mu_ood = ood[add].mean(0)
    tau_mean = segmented_tau(steps, mu_ood)
    fig, ax = plt.subplots(figsize=(7, 4.5))
    ax.plot(steps, mu_ood, "o-", lw=2, ms=3, color=COLORS[add], label="additive arm, mean OOD")
    if not np.isnan(tau_mean):
        t_ = float(tau_mean)
        ax.axvline(t_, color="black", ls="--", lw=1.5,
                   label=f"segmented-regression breakpoint τ ≈ {t_:.0f}")
    ax.set(xlabel="Training step", ylabel="OOD accuracy (%)",
           title="Prediction 9: Phase-2 entry inflection in the OOD trajectory")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(outdir / "figure13-gate-inflection.png", dpi=200)
    plt.close(fig)

    # ---- τ summary (for §11) ----
    print("Segmented-regression breakpoint τ (steps):")
    for c in CONDITION_ORDER:
        taus = tau_by_run[c]
        if len(taus) == 0:
            print(f"  {c:14s}: no breakpoints (n<4 runs usable)")
            continue
        mu, ci = mean_ci(taus)
        print(f"  {c:14s}: mean={mu:6.1f}  95% CI=[{mu-ci:6.1f}, {mu+ci:6.1f}]  "
              f"median={np.median(taus):6.1f}  n={len(taus)}")

    print(f"figures written to {outdir}: figure11-gate-ood.png, "
          f"figure12-gate-sigma.png, figure13-gate-inflection.png")


if __name__ == "__main__":
    main()
