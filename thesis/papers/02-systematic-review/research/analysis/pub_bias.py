#!/usr/bin/env python3
"""
Paper 02 — Phase 9 (Task 9.5): publication bias assessment.

Funnel plot, Egger's regression test, and trim-and-fill on the ID-OOD gap
pools (S3 peer-reviewed, S5 seeds>=3; k >= 10). Egger's test regresses
z = effect/se on precision 1/se; asymmetry signals small-study effects
(interpreted cautiously given benchmark-family heterogeneity).

Output: research/analysis/figures/funnel-*.{png,pdf,svg} + pub-bias-results.md

Usage: python3 pub_bias.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/mpl-cfg")

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
import statsmodels.api as sm  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent
DATA_CSV = BASE / "research" / "analysis" / "analysis-data.csv"
FIG_DIR = BASE / "research" / "analysis" / "figures"
OUT_MD = BASE / "research" / "analysis" / "pub-bias-results.md"


def egger(effects: np.ndarray, ses: np.ndarray) -> dict:
    """Egger regression: z = a + b * precision; test intercept a == 0."""
    z = effects / ses
    prec = 1.0 / ses
    x = sm.add_constant(prec)
    model = sm.OLS(z, x).fit()
    return {"slope": float(model.params[1]), "intercept": float(model.params[0]),
            "intercept_se": float(model.bse[0]),
            "intercept_p": float(model.pvalues[0])}


def trim_fill(effects: np.ndarray, ses: np.ndarray, iters: int = 50) -> dict:
    """Iterative trim-and-fill (one-sided, fixed-effect funnel)."""
    e, s = effects.copy(), ses.copy()
    for _ in range(iters):
        w = 1.0 / s**2
        est = np.sum(w * e) / np.sum(w)
        z = (e - est) / s
        if len(e) < 3:
            break
        if z.max() > abs(z.min()):
            drop = np.argmax(z)
            e = np.delete(e, drop)
            s = np.delete(s, drop)
        else:
            break
    n_trimmed = len(effects) - len(e)
    w = 1.0 / s**2
    est = np.sum(w * e) / np.sum(w)
    se = np.sqrt(1.0 / np.sum(w))
    return {"n_trimmed": n_trimmed, "adjusted_est": est,
            "ci_lower": est - 1.96 * se, "ci_upper": est + 1.96 * se}


def funnel(effects: np.ndarray, ses: np.ndarray, label: str, fname: str) -> None:
    fig, ax = plt.subplots(figsize=(6.5, 5))
    ax.scatter(effects, 1.0 / ses, s=22, color="#4C72B0", alpha=0.8)
    # pseudo-95% CI funnel around pooled FE estimate
    w = 1.0 / ses**2
    est = np.sum(w * effects) / np.sum(w)
    prec = np.linspace(1 / ses.max(), 1 / ses.min() + 2, 100)
    ax.plot(est + 1.96 / prec, prec, color="#888", lw=1, ls="--")
    ax.plot(est - 1.96 / prec, prec, color="#888", lw=1, ls="--")
    ax.axvline(est, color="#C0392B", lw=1)
    ax.set_xlabel("ID-OOD gap")
    ax.set_ylabel("precision (1/SE)")
    ax.set_title(f"Funnel plot — {label}")
    fig.tight_layout()
    for ext in ("png", "pdf", "svg"):
        fig.savefig(FIG_DIR / f"{fname}.{ext}", dpi=150, bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    FIG_DIR.mkdir(exist_ok=True)
    df = pd.read_csv(DATA_CSV, dtype=str).fillna("")
    df["id_ood_gap"] = pd.to_numeric(df["id_ood_gap"].replace("", pd.NA),
                                     errors="coerce")
    df["gap_se"] = pd.to_numeric(df["gap_se"].replace("", pd.NA), errors="coerce")
    lines = ["# Publication bias assessment — Paper 02 Phase 9 (9.5)",
             "",
             "Egger regression: z = intercept + slope x precision; "
             "intercept != 0 indicates funnel asymmetry (small-study effects). "
             "Caveat: asymmetry may reflect benchmark-family heterogeneity "
             "rather than publication bias.", ""]
    for name, flag, fname in [
            ("S3 peer-reviewed", "S3_peer_reviewed", "funnel-S3"),
            ("S5 seeds>=3", "S5_seeds_ge3", "funnel-S5")]:
        sub = df[df[flag].astype(str) == "True"].dropna(
            subset=["id_ood_gap", "gap_se"])
        if len(sub) < 10:
            lines.append(f"## {name}: k={len(sub)} < 10; not assessed.\n")
            continue
        e = sub["id_ood_gap"].to_numpy(dtype=float)
        s = np.maximum(sub["gap_se"].to_numpy(dtype=float), 1e-8)
        funnel(e, s, name, fname)
        eg = egger(e, s)
        tf = trim_fill(e, s)
        lines.append(f"## {name} (k={len(sub)})\n")
        lines.append(f"- Egger: intercept {eg['intercept']:.3f} "
                     f"(SE {eg['intercept_se']:.3f}, p={eg['intercept_p']:.3f}); "
                     f"slope {eg['slope']:.3f}")
        lines.append(f"- Trim-and-fill: {tf['n_trimmed']} trimmed; adjusted "
                     f"estimate {tf['adjusted_est']:.3f} "
                     f"[{tf['ci_lower']:.3f}, {tf['ci_upper']:.3f}]\n")
    (OUT_MD.parent / OUT_MD.name).write_text("\n".join(lines) + "\n",
                                             encoding="utf-8")
    print(f"pub-bias-results written: {OUT_MD.name}")
    print(f"figures: {sorted(p.name for p in FIG_DIR.glob('funnel-*'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
