#!/usr/bin/env python3
"""
Paper 02 — Phase 9 (Task 9.3/9.4): meta-analysis of the ID-OOD gap.

Reads research/analysis/analysis-data.csv, pools the ID-OOD gap with a
DerSimonian-Laird random-effects model (research/analysis/meta_analysis.py)
per the pre-specified strata (S0, S3 peer-reviewed, S4 code, S5 seeds>=3),
with:
  - forest plots per stratum and per subgroup
  - subgroup analyses (benchmark family: custom vs compositional; architecture:
    transformer vs other; scale: small vs medium/large)
  - meta-regression on year (statsmodels WLS) where k >= 10
  - sensitivity excluding the |z|>3 outlier
  - harvest plot for the intervention theme (k = 1)
Output: research/analysis/figures/* + research/analysis/meta-results.md

Usage: python3 run_meta_analysis.py
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
from meta_analysis import meta_random  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent
DATA_CSV = BASE / "research" / "analysis" / "analysis-data.csv"
FIG_DIR = BASE / "research" / "analysis" / "figures"
OUT_MD = BASE / "research" / "analysis" / "meta-results.md"


def gap_pool(df: pd.DataFrame, label: str) -> dict:
    sub = df.dropna(subset=["id_ood_gap", "gap_se"])
    if len(sub) < 2:
        return {"label": label, "k": len(sub), "est": np.nan, "se": np.nan,
                "ci_lower": np.nan, "ci_upper": np.nan, "I2": np.nan,
                "tau2": np.nan, "p": np.nan}
    e = sub["id_ood_gap"].to_numpy(dtype=float)
    v = (sub["gap_se"].to_numpy(dtype=float)) ** 2
    v = np.maximum(v, 1e-8)
    r = meta_random(e, v)
    return {"label": label, "k": len(sub), "est": r["est"], "se": r["se"],
            "ci_lower": r["ci_lower"], "ci_upper": r["ci_upper"],
            "I2": r["I2"], "tau2": r["tau2"], "p": r["p"]}


def forest(results: list[dict], title: str, fname: str) -> None:
    fig, ax = plt.subplots(figsize=(8, max(2.5, 0.5 * len(results) + 1.2)))
    for i, r in enumerate(results):
        y = len(results) - 1 - i
        if np.isnan(r["est"]):
            ax.text(0, y, f"{r['label']}: k={r['k']} (insufficient data)",
                    ha="center", va="center", fontsize=9)
            continue
        ax.plot([r["ci_lower"], r["ci_upper"]], [y, y], color="#333", lw=1.5)
        ax.plot(r["est"], y, "s", color="#C0392B", ms=7)
        ax.text(r["ci_upper"] + 0.01, y,
                f"{r['est']:.3f} [{r['ci_lower']:.3f}, {r['ci_upper']:.3f}] "
                f"k={r['k']} I\u00b2={r['I2']:.0f}%", va="center", fontsize=8)
    ax.axvline(0, color="#888", lw=0.8, ls="--")
    ax.set_yticks(range(len(results)))
    ax.set_yticklabels([r["label"] for r in reversed(results)], fontsize=8)
    ax.set_xlabel("pooled ID-OOD gap (random effects, DL)")
    ax.set_title(title)
    fig.tight_layout()
    for ext in ("png", "pdf", "svg"):
        fig.savefig(FIG_DIR / f"{fname}.{ext}", dpi=150, bbox_inches="tight")
    plt.close(fig)


def harvest(df: pd.DataFrame) -> None:
    """Harvest plot for the intervention theme (k = 1)."""
    fig, ax = plt.subplots(figsize=(7, 3))
    ax.barh([0], [1], color="#B0B0B0")
    ax.text(0.5, 0, "1 study (S046): σ-intervention, no charted effect size",
            ha="center", va="center", fontsize=9)
    ax.set_xlim(0, 1)
    ax.set_yticks([])
    ax.set_title("Intervention effectiveness: harvest plot (k = 1)")
    for ext in ("png", "pdf", "svg"):
        fig.savefig(FIG_DIR / f"harvest-interventions.{ext}", dpi=150,
                    bbox_inches="tight")
    plt.close(fig)


def meta_regression(df: pd.DataFrame, label: str) -> dict | None:
    sub = df.dropna(subset=["id_ood_gap", "gap_se", "year"])
    sub = sub[pd.to_numeric(sub["year"], errors="coerce").notna()]
    if len(sub) < 10:
        return None
    y = sub["id_ood_gap"].to_numpy(dtype=float)
    x = pd.to_numeric(sub["year"], errors="coerce").to_numpy(dtype=float)
    w = 1.0 / np.maximum(sub["gap_se"].to_numpy(dtype=float) ** 2, 1e-8)
    x = sm.add_constant(x)
    model = sm.WLS(y, x, weights=w).fit()
    return {"label": label, "k": len(sub),
            "slope": float(model.params[1]), "slope_se": float(model.bse[1]),
            "slope_p": float(model.pvalues[1])}


def main() -> int:
    FIG_DIR.mkdir(exist_ok=True)
    df = pd.read_csv(DATA_CSV, dtype=str).fillna("")
    for c in ("id_ood_gap", "gap_se", "year"):
        df[c] = pd.to_numeric(df[c].replace("", pd.NA), errors="coerce")

    strata = [("S0 (all)", pd.Series(True, index=df.index)),
              ("S3 (peer-reviewed)", df["S3_peer_reviewed"].astype(str) == "True"),
              ("S4 (code)", df["S4_code"].astype(str) == "True"),
              ("S5 (seeds>=3)", df["S5_seeds_ge3"].astype(str) == "True")]
    pools = [gap_pool(df[mask], name) for name, mask in strata]
    forest(pools, "ID-OOD gap by stratum (random effects)", "forest-strata")

    # sensitivity: exclude outlier
    no_out = df[df["outlier"].astype(str) != "True"]
    pools_no = [gap_pool(no_out[mask], f"{name} (no outlier)")
                for name, mask in strata]
    forest(pools_no, "ID-OOD gap, outlier excluded", "forest-strata-nooutlier")

    # subgroups (S3 primary stratum)
    s3 = df[df["S3_peer_reviewed"].astype(str) == "True"]
    comp = ["CFQ", "SCAN", "COGS", "gSCAN", "GeoQuery", "PCFG_SET"]
    subg = [
        gap_pool(s3[s3["benchmark_family"].isin(comp)], "compositional benchmarks"),
        gap_pool(s3[s3["benchmark_family"] == "custom"], "custom benchmarks"),
        gap_pool(s3[s3["arch_family"] == "transformer"], "transformer"),
        gap_pool(s3[s3["arch_family"] != "transformer"], "non-transformer"),
        gap_pool(s3[s3["model_scale_category"] == "small"], "small scale"),
        gap_pool(s3[s3["model_scale_category"].isin(["medium", "large"])],
                 "medium/large scale"),
    ]
    forest(subg, "Subgroups (S3 stratum)", "forest-subgroups")

    harvest(df)

    mr = meta_regression(df, "year (all gap studies)")
    lines = ["# Meta-analysis results — Paper 02 Phase 9 (9.4)",
             "",
             "Random-effects (DerSimonian-Laird) pooling of the ID-OOD gap. "
             "Variance from charted gap SE or binomial SE.",
             "",
             "## Strata",
             "",
             "| Stratum | k | pooled gap | 95% CI | I² | τ² | p |",
             "|---|---|---|---|---|---|---|"]
    for r in pools:
        lines.append(f"| {r['label']} | {r['k']} | "
                     f"{r['est']:.3f} | [{r['ci_lower']:.3f}, {r['ci_upper']:.3f}] | "
                     f"{r['I2']:.0f}% | {r['tau2']:.4f} | {r['p']:.3f} |")
    lines.append("\n## Sensitivity (outlier excluded)\n")
    for r in pools_no:
        lines.append(f"- {r['label']}: {r['k']} studies, pooled "
                     f"{r['est']:.3f} [{r['ci_lower']:.3f}, {r['ci_upper']:.3f}]")
    lines.append("\n## Subgroups (S3 stratum)\n")
    for r in subg:
        lines.append(f"- {r['label']}: k={r['k']}, pooled {r['est']:.3f} "
                     f"[{r['ci_lower']:.3f}, {r['ci_upper']:.3f}], I²={r['I2']:.0f}%")
    lines.append("\n## Meta-regression (year)\n")
    if mr:
        lines.append(f"- k={mr['k']}, slope {mr['slope']:.4f} per year "
                     f"(SE {mr['slope_se']:.4f}, p={mr['slope_p']:.3f})")
    else:
        lines.append("- k < 10; not estimable.")
    (OUT_MD.parent / OUT_MD.name).write_text("\n".join(lines) + "\n",
                                             encoding="utf-8")
    print(f"meta-results written: {OUT_MD.name}")
    print(f"figures: {sorted(p.name for p in FIG_DIR.glob('forest-*'))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
