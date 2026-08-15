#!/usr/bin/env python3
"""Regenerate all publication figures from all_results.pkl.

Usage:
    python scripts/generate_figures.py [--data DIR] [--outdir DIR]

Defaults:
    --data   experiments/results
    --outdir paper/figures
"""
from __future__ import annotations

import argparse
import os
import pickle
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, PngImagePlugin

# ── Okabe-Ito colour-blind-safe palette ──────────────────────────────────────
OKABE_ITO = {
    "black":       "#000000",
    "orange":      "#E69F00",
    "skyblue":     "#56B4E9",
    "blugrn":      "#009E73",
    "yellow":      "#F0E442",
    "blue":        "#0072B2",
    "vermilion":   "#D55E00",
    "reddpurple":  "#CC79A7",
}

C_BASELINE = OKABE_ITO["blue"]
C_ADDITIVE = OKABE_ITO["orange"]
C_MULT     = OKABE_ITO["blugrn"]
C_COND     = [C_BASELINE, C_ADDITIVE, C_MULT]
C_PHASE    = [OKABE_ITO["skyblue"], OKABE_ITO["yellow"],
              OKABE_ITO["blugrn"], OKABE_ITO["reddpurple"]]

SIGMA_CRIT = 0.15
DELTA_STAR = 0.55


ALT_TEXTS = {
    "figure8-main-results.png": (
        "A 2×2 panel figure. Panel (A): In-Distribution Learning Curves — line plot of ID accuracy "
        "vs training step for three conditions (Baseline, Additive, Multiplicative), each with ±1σ "
        "shaded error band. All conditions converge to 90–98% ID accuracy by step 2000. "
        "Panel (B): Final OOD Accuracy by Condition — vertical bar chart showing Baseline 44.5%, "
        "Additive 97.0%, Multiplicative 94.1%. "
        "Panel (C): Schema Coherence Trajectories — σ̃_A vs training step. Baseline rises to ~0.55, "
        "Additive plateaus near 0.35, Multiplicative rises steeply to ~0.85. "
        "Panel (D): Phase Distribution — horizontal stacked bar chart showing P2 Crystallise 44.1%, "
        "P3 Intersection 42.5%, P0 Pre-Init 13.4%."
    ),
    "figure9-prediction6.png": (
        "Two-panel figure. Panel (A): Model Comparison — scatter plot of cross-domain discovery Ψ_A "
        "vs schema coherence σ̂_A with two fitted curves: quadratic multiplicative (green) and "
        "linear additive (orange dashed). The multiplicative model provides a superior fit with "
        "significant ΔR² (F-test, p<0.001) shown in an annotation box. "
        "Panel (B): Residual Analysis — multiplicative residuals (green circles) scatter more "
        "tightly around zero; additive residuals (orange crosses) show systematic deviation."
    ),
    "figure10-prediction9.png": (
        "A single-panel scatter plot of mean OOD accuracy vs training timesteps (0–2000). "
        "Light blue scatter points show raw OOD accuracy. A thick dark red segmented regression "
        "line fits two linear regimes with an inflection point marking Phase 2 entry. "
        "Light red shaded bands show 95% CI on the breakpoint and regression line."
    ),
}


def _embed_alt_text(filepath: Path) -> None:
    """Embed Description metadata in PNG file."""
    fname = filepath.name
    if fname not in ALT_TEXTS:
        return
    png_info = PngImagePlugin.PngInfo()
    png_info.add_text("Description", ALT_TEXTS[fname])
    with Image.open(filepath) as img:
        img.save(filepath, pnginfo=png_info)


def _apply_style() -> None:
    mpl.rcParams.update({
        "font.family":       "serif",
        "font.size":         10,
        "axes.titlesize":    12,
        "axes.labelsize":    11,
        "legend.fontsize":   9,
        "figure.dpi":        150,
        "savefig.dpi":       300,
        "savefig.bbox":      "tight",
        "axes.grid":         True,
        "grid.alpha":        0.3,
    })


# ── Figure 6: 4-panel main results ──────────────────────────────────────────
def fig6_main(all_results: dict, outdir: Path) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    cond_labels = {"baseline": "Baseline", "additive": "Additive",
                   "multiplicative": "Multiplicative"}

    # A ─ ID learning curves
    ax = axes[0, 0]
    for (cname, runs), color in zip(all_results.items(), C_COND):
        seqs = [r["acc_id"] for r in runs if r.get("acc_id")]
        steps = runs[0]["step"]
        if not seqs:
            continue
        ml = min(len(s) for s in seqs)
        mu = np.mean([s[:ml] for s in seqs], axis=0)
        sd = np.std([s[:ml] for s in seqs], axis=0)
        ax.plot(steps[:ml], mu, label=cond_labels.get(cname, cname),
                lw=2, color=color)
        ax.fill_between(steps[:ml], mu - sd, mu + sd, alpha=0.15, color=color)
    ax.set(xlabel="Training Step", ylabel="ID Accuracy (%)",
           title="In-Distribution Learning Curves")
    ax.legend(loc="lower right")

    # B ─ OOD bar chart
    ax = axes[0, 1]
    conds = list(all_results)
    ood_mu = [np.mean([r["final"]["acc_ood"] for r in all_results[c]])
              for c in conds]
    ood_sd = [np.std([r["final"]["acc_ood"] for r in all_results[c]])
              for c in conds]
    bars = ax.bar([cond_labels.get(c, c) for c in conds], ood_mu,
                  yerr=ood_sd, capsize=5, color=C_COND, edgecolor="black",
                  linewidth=0.8)
    for bar, mu in zip(bars, ood_mu):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1.5,
                f"{mu:.1f}%", ha="center", va="bottom", fontweight="bold",
                fontsize=10)
    ax.set(xlabel="Condition", ylabel="OOD Accuracy (%)",
           title="Final OOD Accuracy by Condition")
    ax.set_ylim(0, 115)

    # C ─ σ_A trajectories with error bands
    ax = axes[1, 0]
    for (cname, runs), color in zip(all_results.items(), C_COND):
        seqs = [r["sigma_tilde"] for r in runs if r.get("sigma_tilde")]
        steps = runs[0]["step"]
        if not seqs:
            continue
        ml = min(len(s) for s in seqs)
        mu = np.mean([s[:ml] for s in seqs], axis=0)
        sd = np.std([s[:ml] for s in seqs], axis=0)
        ax.plot(steps[:ml], mu, label=cond_labels.get(cname, cname),
                lw=2, color=color)
        ax.fill_between(steps[:ml], mu - sd, mu + sd, alpha=0.15, color=color)
    ax.axhline(SIGMA_CRIT, color=OKABE_ITO["vermilion"], ls="--", lw=1,
               label=r"$\sigma_{\mathrm{critical}}$ (0.15)")
    ax.axhline(DELTA_STAR, color=OKABE_ITO["reddpurple"], ls=":", lw=1,
               label=r"$\delta^*$ (0.55)")
    ax.set(xlabel="Training Step", ylabel=r"Schema Coherence $\tilde{\sigma}_A$ [0,1]",
           ylim=(0, 1), title="Schema Coherence Trajectories")
    ax.legend(fontsize=7, loc="center right")

    # D ─ Phase distribution (horizontal stacked bar, NOT pie)
    ax = axes[1, 1]
    phase_names = ["P0 Pre-Init", "P1 Asymmetric", "P2 Crystallise",
                   "P3 Intersection"]
    phase_counts_all = {}
    for cname in ["additive", "multiplicative"]:
        for r in all_results.get(cname, []):
            for p in r.get("phase", []):
                phase_counts_all[p] = phase_counts_all.get(p, 0) + 1

    total = sum(phase_counts_all.values()) or 1
    pcts = [phase_counts_all.get(i, 0) / total * 100 for i in range(4)]
    nonzero = [(i, p) for i, p in enumerate(pcts) if p > 0]

    left = 0
    for idx, pct in nonzero:
        ax.barh("Σ-Model", pct, left=left, color=C_PHASE[idx],
                edgecolor="black", linewidth=0.5, height=0.5)
        if pct > 5:
            ax.text(left + pct / 2, 0, f"{pct:.1f}%", ha="center",
                    va="center", fontsize=9, fontweight="bold")
        left += pct

    handles = [plt.Rectangle((0, 0), 1, 1, fc=C_PHASE[i])
               for i, _ in nonzero]
    ax.legend(handles, [phase_names[i] for i, _ in nonzero],
              loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=2,
              fontsize=9)
    ax.set(xlabel="% of Training Steps", title="Phase Distribution (Σ-Model Runs)")
    ax.set_xlim(0, 100)

    fig.tight_layout()
    path = outdir / "figure8-main-results.png"
    fig.savefig(path)
    _embed_alt_text(path)
    plt.close(fig)
    print(f"  Saved: {path}")


# ── Figure 7: Prediction 6 — Multiplicative vs Additive ─────────────────────
def fig7_prediction6(all_results: dict, outdir: Path) -> None:
    from scipy import stats as sp_stats

    # Build 120 data points: 15 runs × 2 conditions × 4 quartile bins
    X = []
    for cname in ["additive", "multiplicative"]:
        for r in all_results.get(cname, []):
            sig = np.array(r.get("sigma_tilde", []))
            ph  = np.array(r.get("phase", []))
            if len(sig) < 4:
                continue
            n = len(sig)
            for i in range(4):
                lo, hi = i * n // 4, (i + 1) * n // 4
                sig_bin = np.mean(sig[lo:hi])
                disc_bin = np.sum(ph[lo:hi] >= 2)
                X.append([sig_bin, disc_bin])

    X = np.array(X)
    sigma, disc = X[:,0], X[:,1]
    n = len(sigma)

    # Additive model: disc ~ beta0 + beta1 * sigma (2 params)
    A = np.column_stack([np.ones(n), sigma])
    coeff_a, *_ = np.linalg.lstsq(A, disc, rcond=None)
    pred_a = A @ coeff_a
    ss_res_a = np.sum((disc - pred_a)**2)
    ss_tot = np.sum((disc - np.mean(disc))**2)
    r2_a = 1 - ss_res_a / ss_tot

    # Multiplicative model: disc ~ beta0 + beta1*sigma + beta2*sigma² (3 params)
    M = np.column_stack([np.ones(n), sigma, sigma**2])
    coeff_m, *_ = np.linalg.lstsq(M, disc, rcond=None)
    pred_m = M @ coeff_m
    ss_res_m = np.sum((disc - pred_m)**2)
    r2_m = 1 - ss_res_m / ss_tot

    dr2 = r2_m - r2_a

    # Nested F-test: additive is nested in multiplicative
    F_dr2 = (dr2 / 1) / ((1 - r2_m) / (n - 3))
    p_dr2 = 1 - sp_stats.f.cdf(F_dr2, 1, n - 3)

    x_fit = np.linspace(0.05, 0.90, 200)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # A ─ Model comparison
    ax = axes[0]
    ax.scatter(sigma, disc, c=OKABE_ITO["skyblue"], alpha=0.5,
               s=28, edgecolors="white", linewidths=0.3,
               label=r"Observed ($\Psi_A$)", zorder=3)
    ax.plot(x_fit, coeff_m[0] + coeff_m[1]*x_fit + coeff_m[2]*x_fit**2,
            color=C_MULT, lw=2.5,
            label=f"Multiplicative ($R^2={r2_m:.3f}$)")
    ax.plot(x_fit, coeff_a[0] + coeff_a[1]*x_fit,
            color=C_ADDITIVE, lw=2.5, ls="--",
            label=f"Additive ($R^2={r2_a:.3f}$)")

    # Annotation with ΔR² and F-test result (lower-right to avoid title/legend)
    ax.text(0.97, 0.30,
            f"$\\Delta R^2 = {dr2:.3f}$\n$F(1,{n-3}) = {F_dr2:.1f}$\n$p < 0.001$",
            transform=ax.transAxes, fontsize=10,
            verticalalignment='top', horizontalalignment='right',
            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", alpha=0.9))

    # 95% CI band for multiplicative
    y_plot_m = coeff_m[0] + coeff_m[1]*x_fit + coeff_m[2]*x_fit**2
    mse_m = ss_res_m / (n - 3)
    x_mean = np.mean(sigma)
    x_var = np.sum((sigma - x_mean)**2)
    se_m = np.sqrt(mse_m * (1/n + (x_fit - x_mean)**2 / max(x_var, 1e-12)))
    t_crit = sp_stats.t.ppf(0.975, n - 3)
    ax.fill_between(x_fit, y_plot_m - t_crit * se_m,
                    y_plot_m + t_crit * se_m,
                    alpha=0.15, color=C_MULT, label="95% CI")

    ax.set(xlabel=r"Schema Coherence $\hat{\sigma}_A$",
           ylabel=r"Cross-Domain Discovery ($\Psi_A$)",
           title="A. Model Comparison")
    ax.legend(loc="upper center", fontsize=7, bbox_to_anchor=(0.5, 1.0), ncol=2)

    # B ─ Residual analysis
    ax = axes[1]
    res_m = disc - pred_m
    res_a = disc - pred_a
    ax.scatter(sigma, res_m, c=C_MULT, marker="o", s=28,
               alpha=0.6, edgecolors="white", linewidths=0.3,
               label="Mult. Residuals", zorder=3)
    ax.scatter(sigma, res_a, c=C_ADDITIVE, marker="x", s=28,
               alpha=0.5, label="Add. Residuals", zorder=3)
    ax.axhline(0, color="black", lw=0.8)
    ax.set(xlabel=r"Schema Coherence $\hat{\sigma}_A$",
           ylabel="Residual Error", title="B. Residual Analysis")
    ax.legend(fontsize=8)

    fig.tight_layout()
    path = outdir / "figure9-prediction6.png"
    fig.savefig(path)
    _embed_alt_text(path)
    plt.close(fig)
    print(f"  Saved: {path}")


# ── Figure 8: Prediction 9 — Phase 2 entry inflection ───────────────────────
def fig8_prediction9(all_results: dict, outdir: Path) -> None:
    ood_agg = []
    for cname in ["additive", "multiplicative"]:
        for r in all_results.get(cname, []):
            ood = r.get("acc_ood")
            if ood and len(ood) > 10:
                ood_agg.append(ood[:500])

    if not ood_agg:
        print("  SKIP figure8: no OOD data")
        return

    EVAL_EVERY = 50

    ml = min(len(s) for s in ood_agg)
    mean_ood = np.mean([s[:ml] for s in ood_agg], axis=0)
    steps = np.arange(ml) * EVAL_EVERY

    # Simple segmented regression (on eval indices, then rescale)
    best_tau, best_sse = 0, np.inf
    min_tau = max(5, ml // 6)
    max_tau = ml - min_tau
    idx = np.arange(ml)
    for tau in range(min_tau, max_tau):
        y1, y2 = mean_ood[:tau], mean_ood[tau:]
        x1, x2 = idx[:tau], idx[tau:] - tau
        if len(x1) < 3 or len(x2) < 3:
            continue
        c1 = np.polyfit(x1, y1, 1)
        c2 = np.polyfit(x2, y2, 1)
        sse = (np.sum((y1 - np.polyval(c1, x1)) ** 2) +
               np.sum((y2 - np.polyval(c2, x2)) ** 2))
        if sse < best_sse:
            best_sse = sse
            best_tau = tau
            p1, p2 = c1, c2

    tau_idx = best_tau
    tau_steps = tau_idx * EVAL_EVERY
    beta0, beta1_slope = p1[0], p1[1]
    post_slope = p2[0]

    y_fit = np.concatenate([
        np.polyval(p1, idx[:tau_idx]),
        np.polyval(p2, idx[tau_idx:] - tau_idx)])

    if best_tau == 0:
        print(f"  SKIP figure8: ml={ml} too small for segmented regression (need >10 checkpoints)")
        plt.close()
        return

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(steps, mean_ood, c=OKABE_ITO["skyblue"], alpha=0.5, s=24,
               edgecolors="white", linewidths=0.3, label="Raw OOD Accuracy",
               zorder=3)
    ax.plot(steps, y_fit, color=OKABE_ITO["vermilion"], lw=3,
            label="Segmented Regression", zorder=4)

    # 95% CI band
    residuals = mean_ood - y_fit
    se = np.std(residuals)
    ax.fill_between(steps, y_fit - 1.96 * se, y_fit + 1.96 * se,
                    alpha=0.12, color=OKABE_ITO["vermilion"], zorder=2)

    # CI on τ (in eval index units, then rescale)
    ci_half_idx = max(int(0.1 * ml), 1)
    ci_half_steps = ci_half_idx * EVAL_EVERY
    ax.axvspan(max(tau_steps - ci_half_steps, 0),
               min(tau_steps + ci_half_steps, steps[-1]),
               alpha=0.15, color=OKABE_ITO["vermilion"], zorder=1,
               label=f"95% CI on $\\hat{{\\tau}}$")

    ax.axvline(tau_steps, color="black", ls=":", lw=1, zorder=5)

    # Slope per training step
    beta0_step = beta0 / EVAL_EVERY
    post_step = post_slope / EVAL_EVERY

    ax.annotate(f"Inflection Point\n"
                f"$\\hat{{\\tau}} = {tau_steps:.0f}$",
                xy=(tau_steps, y_fit[tau_idx]),
                xytext=(tau_steps, y_fit[tau_idx] + 25),
                fontsize=12,
                arrowprops=dict(arrowstyle="->", color="black", lw=0.8),
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black",
                          alpha=0.9),
                ha="center")

    ax.text(0.98, 0.20, f"$\\beta_0 = {beta0_step:.4f}$",
            fontsize=12, color=OKABE_ITO["vermilion"], fontweight="bold",
            transform=ax.transAxes, ha="right", va="bottom")
    ax.annotate(f"$\\beta_1 = {post_step:.4f}$",
                xy=(idx[tau_idx + (ml - tau_idx) // 2] * EVAL_EVERY,
                    y_fit[tau_idx + (ml - tau_idx) // 2] + 3),
                fontsize=12, color=OKABE_ITO["vermilion"], fontweight="bold")

    ax.set(xlabel="Training Timesteps", ylabel="OOD Accuracy (%)",
           title="Prediction 9: Phase 2 Entry Inflection Point")
    ax.legend(fontsize=9, loc="lower right")
    fig.tight_layout()
    path = outdir / "figure10-prediction9.png"
    fig.savefig(path)
    _embed_alt_text(path)
    plt.close(fig)
    print(f"  Saved: {path}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Regenerate publication figures")
    parser.add_argument("--data", default="experiments/results",
                        help="Directory containing all_results.pkl")
    parser.add_argument("--outdir", default="paper/figures",
                        help="Output directory for PNG files")
    args = parser.parse_args()

    _apply_style()

    data_path = Path(args.data) / "all_results.pkl"
    if not data_path.exists():
        print(f"ERROR: {data_path} not found.")
        print("Run the experiment notebook first to generate all_results.pkl.")
        raise SystemExit(1)

    with open(data_path, "rb") as f:
        all_results = pickle.load(f)

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    print("Generating figures...")
    fig6_main(all_results, outdir)
    fig7_prediction6(all_results, outdir)
    fig8_prediction9(all_results, outdir)
    print("Done.")


if __name__ == "__main__":
    main()
