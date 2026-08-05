#!/usr/bin/env python3
"""
Paper 02 — Phase 6 finalize eligibility with human adjudication (Task 6.3)

Applies the human (third-reviewer) adjudication log to the reconciled
eligibility decisions and rewrites the final files.

Human adjudications: research/retrieval/human-adjudication.csv
  columns: id, decision (Include|Exclude|Uncertain), reason (FT code), note

Usage:
  python ft_finalize.py

Outputs (final):
  research/retrieval/eligibility-decisions.csv   (all 395, adjudicated)
  research/retrieval/fulltext-exclusions.md      (FT counts + lists)
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent
RETR = BASE / "research" / "retrieval"
OUT_CSV = RETR / "eligibility-decisions.csv"
EXCL_MD = RETR / "fulltext-exclusions.md"
ADJ_CSV = RETR / "human-adjudication.csv"

FT_LABELS = {
    "FT1": "No OOD/compositional split reported",
    "FT2": "Only ID results reported",
    "FT3": "Insufficient quantitative detail (no accuracy numbers, no extractable data)",
    "FT4": "Not actually about neural network models",
    "FT5": "Full text unavailable (after 3 attempts)",
    "FT6": "Duplicate content (superseded by later publication)",
    "FT7": "Review or opinion paper without original results",
    "FT8": "Other (specify)",
}


def main() -> None:
    with open(OUT_CSV, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    with open(ADJ_CSV, "r", encoding="utf-8") as f:
        adj = {r["id"]: r for r in csv.DictReader(f)}

    applied = 0
    for row in rows:
        if row["id"] in adj:
            a = adj[row["id"]]
            row["decision"] = a["decision"]
            row["reason"] = a.get("reason", "")
            row["note"] = (row.get("note", "") + " | adj: " + a.get("note", "")).strip(" |")
            applied += 1

    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    stats = Counter(r["decision"] for r in rows)
    reasons = Counter(r["reason"] for r in rows if r["decision"] == "Exclude")
    excl = [r for r in rows if r["decision"] == "Exclude"]

    with open(EXCL_MD, "w", encoding="utf-8") as f:
        f.write("# Paper 02 — Full-Text Exclusions (Task 6.2/6.4) — FINAL\n\n")
        f.write(f"**Total excluded at full-text stage**: {len(excl)}\n\n")
        f.write("| Code | Reason | Count |\n")
        f.write("|------|--------|------:|\n")
        for code, label in FT_LABELS.items():
            f.write(f"| {code} | {label} | {reasons[code]} |\n")
        f.write("\n## Excluded Records (by code)\n\n")
        for code in FT_LABELS:
            items = [r for r in excl if r["reason"] == code]
            if not items:
                continue
            f.write(f"### {code}: {FT_LABELS[code]} ({len(items)})\n\n")
            f.write("| ID | Title |\n")
            f.write("|----|-------|\n")
            for r in items:
                f.write(f"| {r['id']} | {r['title'][:70]} |\n")
            f.write("\n")

    print(f"Applied {applied} human adjudications")
    for d, c in stats.most_common():
        print(f"  {d:10s} {c}")
    print("Exclusion reasons:", dict(reasons.most_common()))
    print(f"Final outputs: {OUT_CSV.name}, {EXCL_MD.name}")


if __name__ == "__main__":
    main()
