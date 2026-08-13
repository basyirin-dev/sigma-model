#!/usr/bin/env python3
"""
Paper 01 — Phase 11 revision: signature 'AGI Safety Evidence Landscape' figure.

Bubble plot of the seven named subdomains:
  x = % empirical methods (empirical <-> conceptual axis)
  y = % high-credibility (tiers A+B, credibility axis)
  bubble size = number of studies
  colour = subdomain

Input : research/charting/charted-data.csv + research/quality-scores.csv
Output: manuscript/figures/fig-evidence-landscape.{png,pdf,svg}
        (time-series figure is superseded in the main text and kept as
        supplementary material.)

Usage: python3 evidence_landscape.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/mpl-cfg")

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent
CHARTED = BASE / "research" / "charting" / "charted-data.csv"
QUALITY = BASE / "research" / "quality-scores.csv"
OUT = BASE / "manuscript" / "figures"

SUBS = ["value alignment", "ethics", "robustness", "capabilities",
        "interpretability", "governance", "mesa-optimization"]


def main() -> int:
    df = pd.read_csv(CHARTED, dtype=str).fillna("")
    q = pd.read_csv(QUALITY, dtype=str).fillna("")
    tier_ab = q["tier"].isin(["A", "B"]).astype(int)
    comp = pd.to_numeric(q["composite"], errors="coerce")
    qmap = dict(zip(q["paper_id"], zip(tier_ab, comp)))

    rows = []
    for s in SUBS:
        mask = df["subdomains"].str.split(";").map(
            lambda xs: s in [x.strip() for x in xs])
        sub = df[mask]
        n = len(sub)
        emp = sub["methodology"].isin(
            ["experiment", "simulation", "case study"]).mean() * 100
        ab = sum(qmap.get(pid, (0, 0))[0] for pid in sub["paper_id"]) / n * 100
        rows.append({"sub": s, "n": n, "empirical_pct": emp, "ab_pct": ab})
    d = pd.DataFrame(rows)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    palette = {"value alignment": "#C44E52", "ethics": "#DD8452",
               "robustness": "#55A868", "capabilities": "#4C72B0",
               "interpretability": "#8172B3", "governance": "#937860",
               "mesa-optimization": "#DA8BC3"}
    for _, r in d.iterrows():
        ax.scatter(r["empirical_pct"], r["ab_pct"], s=r["n"] * 0.9,
                   color=palette[r["sub"]], alpha=0.75,
                   edgecolors="white", linewidths=1.2,
                   label=f"{r['sub']} (n={r['n']})")
        ax.annotate(r["sub"], (r["empirical_pct"], r["ab_pct"]),
                    xytext=(6, 6), textcoords="offset points", fontsize=8)
    ax.axhline(25.0, color="#888", lw=0.8, ls="--")
    ax.text(2, 25.6, "corpus baseline (25.0% tier A+B)", fontsize=7, color="#555")
    ax.set_xlabel("% empirical methods (empirical $\\leftrightarrow$ conceptual)")
    ax.set_ylabel("% high-credibility (tier A+B)")
    ax.set_title("The AGI Safety Evidence Landscape")
    ax.set_xlim(-2, 105)
    ax.set_ylim(15, 40)
    ax.legend(fontsize=7, loc="lower right")
    fig.tight_layout()
    OUT.mkdir(exist_ok=True)
    for ext in ("png", "pdf", "svg"):
        fig.savefig(OUT / f"fig-evidence-landscape.{ext}", dpi=150,
                    bbox_inches="tight")
    plt.close(fig)
    print("fig-evidence-landscape written; data:")
    print(d.round(1).to_string(index=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
