#!/usr/bin/env python3
"""
Paper 02 — Phase 7 (Task 7.3.1): draw the 20% validation sample.

Fixed-seed random sample of the 286 included studies. Seed documented for
reproducibility (20261016 = Phase 7 deadline); 20% of 286 = 57 studies
(round-half-up).

Output: research/charting/validation-sample.csv
"""

from __future__ import annotations

import csv
import json
import random
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
PREFILL_JSON = BASE / "research" / "charting" / "prefill.json"
OUT_CSV = BASE / "research" / "charting" / "validation-sample.csv"

SEED = 20261016
FRACTION = 0.20


def main() -> None:
    prefill = json.loads(PREFILL_JSON.read_text(encoding="utf-8"))
    studies = sorted(prefill, key=lambda s: int(s[1:]))
    rng = random.Random(SEED)
    sample = rng.sample(studies, k=round(FRACTION * len(studies)))
    sample.sort(key=lambda s: int(s[1:]))

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["study_id", "id", "title"])
        for sid in sample:
            rec = prefill[sid]
            w.writerow([sid, rec["id"], rec["title"]])

    print(f"sample: {len(sample)} of {len(studies)} studies "
          f"({FRACTION:.0%}, seed={SEED}) -> {OUT_CSV}")
    print("studies:", ", ".join(sample))


if __name__ == "__main__":
    sys.exit(main())
