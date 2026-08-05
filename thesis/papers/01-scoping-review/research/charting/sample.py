#!/usr/bin/env python3
"""
Paper 01 — Phase 7: draw the 20% validation sample (Task 7.3.1 / CC.1.6).

Simple random 20% sample of included papers (seed fixed for
reproducibility), composition reported by evidence_basis. Output:
research/charting/validation-sample.csv (paper_id, seed position).
"""

from __future__ import annotations

import csv
import random
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
OUT_CSV = BASE / "research" / "charting" / "validation-sample.csv"

SEED = 20260901
FRACTION = 0.20


def main() -> None:
    rows = list(csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")))
    rng = random.Random(SEED)
    sample = rng.sample(rows, round(FRACTION * len(rows)))
    by_basis: dict[str, int] = {}
    for r in sample:
        by_basis[r["evidence_basis"]] = by_basis.get(r["evidence_basis"], 0) + 1

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["paper_id", "title", "evidence_basis", "publication_type"])
        for r in sorted(sample, key=lambda x: x["paper_id"]):
            w.writerow([r["paper_id"], r["title"], r["evidence_basis"], r["publication_type"]])

    print(f"sample size: {len(sample)} ({FRACTION:.0%} of {len(rows)}) seed={SEED}")
    print(f"by evidence_basis: {by_basis}")


if __name__ == "__main__":
    sys.exit(main())
