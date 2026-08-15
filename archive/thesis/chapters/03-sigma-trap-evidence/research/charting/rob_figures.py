#!/usr/bin/env python3
"""
Paper 02 — Phase 8 (Task 8.4): RoB visualizations.

Reads research/risk-of-bias.csv -> figures/rob-*.{png,pdf,svg}:
  rob-traffic-light   studies x domains traffic-light matrix (Low/Unclear/High/N-A)
  rob-weighted-bar    proportion of Low/Unclear/High per domain (weighted bar chart)
  rob-overall         overall judgment distribution

Usage: python3 rob_figures.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/mpl-cfg")

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Patch  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent
ROB_CSV = BASE / "research" / "risk-of-bias.csv"
FIG_DIR = BASE / "research" / "charting" / "figures"

COLORS = {"LOW": "#2E8B57", "UNCLEAR": "#E6B800", "HIGH": "#C0392B", "N/A": "#B0B0B0"}
DOMAINS = ["D1", "D2", "D3", "D4", "D5", "D6"]


def save(fig, stem: str) -> None:
    for ext in ("png", "pdf", "svg"):
        fig.savefig(FIG_DIR / f"{stem}.{ext}", dpi=150, bbox_inches="tight")


def main() -> int:
    import csv
    FIG_DIR.mkdir(exist_ok=True)
    rows = list(csv.DictReader(open(ROB_CSV, newline="", encoding="utf-8")))

    # ---- traffic-light matrix -------------------------------------------------
    n = len(rows)
    fig, ax = plt.subplots(figsize=(9, max(4, n * 0.055 + 1.5)))
    data = [[rows[i][d] for d in DOMAINS] for i in range(n)]
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            ax.add_patch(plt.Rectangle((j, n - 1 - i), 1, 1,
                                       facecolor=COLORS.get(v, "#FFFFFF"),
                                       edgecolor="white", linewidth=0.3))
    ax.set_xlim(0, len(DOMAINS))
    ax.set_ylim(0, n)
    ax.set_xticks([j + 0.5 for j in range(len(DOMAINS))])
    ax.set_xticklabels(DOMAINS, fontsize=9)
    ax.set_yticks([])
    ax.set_xlabel("σ-ROB domain")
    ax.set_ylabel(f"studies (n={n})")
    ax.set_title("Risk of bias by domain — traffic-light matrix")
    ax.legend(handles=[Patch(facecolor=COLORS[k], label=k) for k in COLORS],
              loc="upper right", fontsize=8)
    fig.tight_layout()
    save(fig, "rob-traffic-light")
    plt.close(fig)

    # ---- weighted bar chart ----------------------------------------------------
    fig, ax = plt.subplots(figsize=(9, 4.5))
    dist = {d: {"LOW": 0, "UNCLEAR": 0, "HIGH": 0, "N/A": 0} for d in DOMAINS}
    for r in rows:
        for d in DOMAINS:
            dist[d][r[d]] = dist[d].get(r[d], 0) + 1
    bottom = [0] * len(DOMAINS)
    for level in ("LOW", "UNCLEAR", "HIGH", "N/A"):
        vals = [dist[d][level] / n * 100 for d in DOMAINS]
        ax.bar(DOMAINS, vals, bottom=bottom, color=COLORS[level],
               label=level, width=0.6)
        bottom = [b + v for b, v in zip(bottom, vals)]
    ax.set_ylabel("% of studies")
    ax.set_title("Risk of bias by domain (weighted proportions)")
    ax.legend(fontsize=8)
    fig.tight_layout()
    save(fig, "rob-weighted-bar")
    plt.close(fig)

    # ---- overall ---------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(7, 4.5))
    from collections import Counter
    overall = Counter(r["overall"] for r in rows)
    levels = ["LOW", "UNCLEAR", "HIGH"]
    vals = [overall.get(lv, 0) for lv in levels]
    ax.bar(levels, vals, color=[COLORS[lv] for lv in levels], width=0.55)
    for i, v in enumerate(vals):
        ax.text(i, v + 1, f"{v} ({v / n * 100:.1f}%)", ha="center", fontsize=9)
    ax.set_ylabel("studies")
    ax.set_title("Overall risk of bias (§7.1 algorithm)")
    fig.tight_layout()
    save(fig, "rob-overall")
    plt.close(fig)

    print("figures written:", sorted(p.name for p in FIG_DIR.glob("rob-*")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
