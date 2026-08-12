#!/usr/bin/env python3
"""
Paper 01 — Phase 10 revision: consolidate manuscript exhibits.

Combines existing Phase 7/8/9 figures into the journal-ready exhibit set
(<= 5 exhibits: PRISMA flow + 3 multi-panel figures + 2 tables):

  fig-corpus-overview  [publication type | subdomains | venue distribution]
  fig-time-series      [subdomains x year | formal-vs-conceptual by year]

Reads research/charting/figures/*.png|pdf and writes manuscript/figures/.
Usage: python3 consolidate_exhibits.py
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

os.environ.setdefault("MPLCONFIGDIR", "/tmp/mpl-cfg")

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.image as mpimg  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
SRC = BASE / "research" / "charting" / "figures"
OUT = BASE / "manuscript" / "figures"


def load(name: str):
    for ext in (".png", ".pdf"):
        p = SRC / (name + ext)
        if p.exists():
            if ext == ".png":
                return mpimg.imread(p)
            # pdf: fall back to png sibling
            q = SRC / (name + ".png")
            if q.exists():
                return mpimg.imread(q)
    raise FileNotFoundError(name)


def panel(ax, img, title: str) -> None:
    ax.imshow(img)
    ax.axis("off")
    ax.set_title(title, fontsize=9)


def main() -> int:
    OUT.mkdir(exist_ok=True)

    # ---- corpus overview: pubtype | subdomains | venue ---------------------
    fig, axes = plt.subplots(1, 3, figsize=(11, 3.2))
    panel(axes[0], load("bar-publication-type"), "(a) Publication type")
    panel(axes[1], load("bar-subdomains"), "(b) Subdomains (multi-select)")
    panel(axes[2], load("phase9-venue-distribution"), "(c) Venue distribution")
    fig.tight_layout()
    for ext in ("png", "pdf", "svg"):
        fig.savefig(OUT / f"fig-corpus-overview.{ext}", dpi=150, bbox_inches="tight")
    plt.close(fig)

    # ---- time series: subdomains x year | formal vs conceptual -------------
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.4))
    panel(axes[0], load("phase9-subdomains-year"), "(a) Subdomain focus over time")
    panel(axes[1], load("phase9-formal-conceptual-year"),
          "(b) Formal vs conceptual by year")
    fig.tight_layout()
    for ext in ("png", "pdf", "svg"):
        fig.savefig(OUT / f"fig-time-series.{ext}", dpi=150, bbox_inches="tight")
    plt.close(fig)

    print("consolidated exhibits written:",
          sorted(p.name for p in OUT.glob("fig-*")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
