#!/usr/bin/env python3
"""
Paper 01 — Phase 7: summary statistics + initial visualizations
(Task 7.5.3/7.5.4).

Summary: total charted; distributions by publication type, subdomain,
year, formal framework, methodology, evidence basis, relevance.
Visualizations (research/charting/figures/):
  - bar charts: publication_type, subdomains, formal_framework, methodology
  - time series: papers per year (all + by top subdomain)
  - treemap: subdomains x publication_type (squarify-lite implemented here)
Output: research/charting/summary-statistics.md + figures/
"""

from __future__ import annotations

import csv
import os
import sys
from collections import Counter
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
os.environ.setdefault("MPLCONFIGDIR", "/tmp/mpl-cfg")
import matplotlib.pyplot as plt  # noqa: E402
import matplotlib.patches as mpatches  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
OUT_MD = BASE / "research" / "charting" / "summary-statistics.md"
FIG_DIR = BASE / "research" / "charting" / "figures"


def bar(dist: Counter, title: str, fname: str, top: int = 14) -> None:
    items = dist.most_common(top)
    fig, ax = plt.subplots(figsize=(9, 4.5))
    labels = [k for k, _ in items]
    vals = [v for _, v in items]
    ax.bar(range(len(vals)), vals, color="#4C72B0")
    ax.set_xticks(range(len(vals)))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=8)
    ax.set_ylabel("papers")
    ax.set_title(title)
    fig.tight_layout()
    fig.savefig(FIG_DIR / fname, dpi=150)
    plt.close(fig)


def timeseries(year_dist: Counter) -> None:
    years = sorted(y for y in year_dist if isinstance(y, int))
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.plot(years, [year_dist[y] for y in years], marker="o", ms=3)
    ax.set_xlabel("year")
    ax.set_ylabel("papers")
    ax.set_title("Included papers by year")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "timeseries-year.png", dpi=150)
    plt.close(fig)


def treemap(pairs: list[tuple[str, int]], title: str, fname: str) -> None:
    """Minimal squarify-lite treemap (sorted alternating strips)."""
    total = sum(v for _, v in pairs)
    fig, ax = plt.subplots(figsize=(9, 6))
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    colors = plt.cm.viridis([i / max(len(pairs), 1) for i in range(len(pairs))])
    x, y, w, h = 0.0, 0.0, 1.0, 1.0
    horizontal = True
    for (label, v), c in zip(pairs, colors):
        frac = v / total
        if horizontal:
            cw = w * frac
            ax.add_patch(mpatches.Rectangle((x, y), cw, h, facecolor=c, edgecolor="white"))
            if v / total > 0.03:
                ax.text(x + cw / 2, y + h / 2, f"{label}\n{v}", ha="center", va="center",
                        fontsize=7, color="white")
            x += cw
            if abs(x - 1.0) < 1e-9:
                x, y = 0.0, y + h
                w, h = 1.0, 1.0 - h
                horizontal = False
        else:
            ch = h * frac
            ax.add_patch(mpatches.Rectangle((x, y), w, ch, facecolor=c, edgecolor="white"))
            if v / total > 0.03:
                ax.text(x + w / 2, y + ch / 2, f"{label}\n{v}", ha="center", va="center",
                        fontsize=7, color="white")
            y += ch
    ax.set_title(title)
    fig.tight_layout()
    fig.savefig(FIG_DIR / fname, dpi=150)
    plt.close(fig)


def main() -> None:
    FIG_DIR.mkdir(exist_ok=True)
    rows = list(csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")))
    n = len(rows)

    pub = Counter((r["publication_type"] or "missing") for r in rows)
    year = Counter()
    for r in rows:
        try:
            year[int(float(r["year"]))] += 1
        except (ValueError, TypeError):
            year["unknown"] += 1
    ff = Counter((r["formal_framework"] or "missing") for r in rows)
    mf = Counter((r["mathematical_formalism"] or "missing") for r in rows)
    meth = Counter((r["methodology"] or "missing") for r in rows)
    eb = Counter((r["evidence_basis"] or "missing") for r in rows)
    rel = Counter((r["relevance_sigma_trap"] or "missing") for r in rows)
    sub = Counter()
    for r in rows:
        for s in (r["subdomains"] or "").split(";"):
            s = s.strip()
            if s:
                sub[s] += 1
    sub_pub = Counter()
    for r in rows:
        for s in (r["subdomains"] or "").split(";"):
            s = s.strip()
            if s:
                sub_pub[(s, r["publication_type"])] += 1

    bar(pub, "Publication type", "bar-publication-type.png")
    bar(sub, "AGI safety subdomain (multi-select)", "bar-subdomains.png", top=10)
    bar(ff, "Formal framework", "bar-formal-framework.png", top=10)
    bar(meth, "Methodology (empirical)", "bar-methodology.png")
    timeseries(year)
    treemap(sub.most_common(), "Subdomains x publication type (treemap)", "treemap-subdomains.png")

    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write(f"# Summary statistics — Paper 01 Phase 7 (Task 7.5.3)\n\n")
        fh.write(f"- **Total papers charted: {n}**\n\n")
        fh.write("## By publication type\n\n| Type | n |\n|---|---|\n")
        for k, v in pub.most_common():
            fh.write(f"| {k} | {v} |\n")
        fh.write("\n## By AGI safety subdomain (multi-select)\n\n| Subdomain | n |\n|---|---|\n")
        for k, v in sub.most_common():
            fh.write(f"| {k} | {v} |\n")
        fh.write("\n## By year\n\n| Year | n |\n|---|---|\n")
        for k in sorted(year, key=lambda x: (isinstance(x, str), x)):
            fh.write(f"| {k} | {year[k]} |\n")
        fh.write("\n## By formal framework\n\n| Framework | n |\n|---|---|\n")
        for k, v in ff.most_common():
            fh.write(f"| {k} | {v} |\n")
        fh.write("\n## By mathematical formalism\n\n| Formalism | n |\n|---|---|\n")
        for k, v in mf.most_common():
            fh.write(f"| {k} | {v} |\n")
        fh.write("\n## By methodology\n\n| Methodology | n |\n|---|---|\n")
        for k, v in meth.most_common():
            fh.write(f"| {k} | {v} |\n")
        fh.write("\n## By evidence basis\n\n| Basis | n |\n|---|---|\n")
        for k, v in eb.most_common():
            fh.write(f"| {k} | {v} |\n")
        fh.write("\n## By sigma-trap relevance (seed)\n\n| Score | n |\n|---|---|\n")
        for k in sorted(rel, key=lambda x: (isinstance(x, str), x)):
            fh.write(f"| {k} | {rel[k]} |\n")
        fh.write("\nFigures: `figures/` (bar charts, timeseries-year.png, treemap-subdomains.png)\n")

    print(f"summary written: {OUT_MD.name}; figures in {FIG_DIR.name}: "
          f"{sorted(p.name for p in FIG_DIR.glob('*.png'))}")


if __name__ == "__main__":
    sys.exit(main())
