#!/usr/bin/env python3
"""
Paper 01 — Phase 8: compute composite credibility scores + tiers
(Task 8.2.3).

Reads research/quality-scores.csv (D1–D8 columns) and
research/charting/rubric-config.yaml, computes:

  composite = Σ(dimension score × paper-type weight)
  tier      = A–E from config cutoffs
  +0.4 replication bonus where `notes` carries `replication:yes`, capped.

Weight handling:
  - Missing dimension scores (blank cells) do NOT sink a paper: the
    remaining non-missing weights are renormalized to sum to 1.00.
  - D4 is empirical-only: weight 0.00 for non-empirical weight_sets
    (already in config); a blank D4 on an empirical paper is renormalized
    out like any other missing dimension.
  - When D6 is blank (no citation data) and config `renormalize_missing_d6`
    is true, D6's weight is redistributed across the scored dimensions.

Writes composite + tier back into quality-scores.csv. Idempotent.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
SCORES_CSV = BASE / "research" / "quality-scores.csv"
CONFIG_YAML = Path(__file__).resolve().parent / "rubric-config.yaml"

DIMS = ["D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8"]


def parse_score(value: str) -> int | None:
    v = (value or "").strip()
    if not v:
        return None
    try:
        return int(v)
    except ValueError:
        return None


def renormalize(weights: dict[str, float], present: list[str]) -> dict[str, float]:
    """Scale the weights of present dims to sum to 1.00."""
    w = {d: weights[d] for d in present}
    total = sum(w.values())
    if total <= 0:
        return {}
    return {d: v / total for d, v in w.items()}


def main() -> None:
    parser = argparse.ArgumentParser(description="Phase 8 composite computation (Task 8.2.3)")
    parser.add_argument("--summary", action="store_true", help="print distribution summary")
    args = parser.parse_args()

    cfg = yaml.safe_load(CONFIG_YAML.read_text(encoding="utf-8"))
    weight_sets = cfg["weight_sets"]
    tiers = cfg["tiers"]  # {"A": 3.2, "B": 2.4, "C": 1.6, "D": 0.8}
    bonus = float(cfg.get("replication_bonus", 0.0))
    max_composite = float(cfg.get("max_composite", 4.0))
    renormalize_d6 = bool(cfg.get("renormalize_missing_d6", False))

    rows = list(csv.DictReader(open(SCORES_CSV, newline="", encoding="utf-8")))
    fields = list(rows[0].keys())

    def tier_for(score: float) -> str:
        for name in ("A", "B", "C", "D"):
            if score >= float(tiers[name]):
                return name
        return "E"

    n_composite = 0
    n_renorm = 0
    from collections import Counter
    tier_counts: Counter = Counter()

    for r in rows:
        ws = weight_sets.get(r.get("weight_set", ""), weight_sets["pos_review"])
        scores = {d: parse_score(r.get(d, "")) for d in DIMS}
        present = [d for d in DIMS if scores[d] is not None]

        # If D6 missing and renormalization requested, drop it from scoring.
        if renormalize_d6 and scores.get("D6") is None and "D6" in present:
            present = [d for d in present if d != "D6"]
        if renormalize_d6 and scores.get("D6") is None:
            n_renorm += 1

        if not present:
            r["composite"] = ""
            r["tier"] = ""
            continue

        weights = renormalize(ws, present)
        composite = sum(scores[d] * weights[d] for d in present)

        # +0.4 replication bonus where rater-documented.
        if "replication:yes" in (r.get("notes") or ""):
            composite += bonus
        composite = min(composite, max_composite)
        composite = round(composite, 2)

        r["composite"] = f"{composite:.2f}"
        r["tier"] = tier_for(composite)
        n_composite += 1
        tier_counts[r["tier"]] += 1

    with open(SCORES_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f"computed composite for {n_composite}/{len(rows)} rows "
          f"(D6-renormalized: {n_renorm})")
    if args.summary:
        print(f"tiers: {dict(sorted(tier_counts.items()))}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
