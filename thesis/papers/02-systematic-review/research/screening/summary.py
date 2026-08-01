#!/usr/bin/env python3
"""
Paper 02 — Phase 5 Summary + PRISMA numbers + exports (Task 5.6)
"""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
ABS_CSV = BASE / "research" / "screening-results" / "paper02-abstract-screening.csv"
DECISIONS_DIR = BASE / "research" / "screening-decisions"
DECISIONS_DIR.mkdir(parents=True, exist_ok=True)
SUMMARY_MD = BASE / "research" / "screening-results" / "screening-summary.md"

EXPORT_FIELDS = ["id", "title", "authors", "year", "doi", "arxiv_id", "abstract",
                 "keywords", "source_db", "journal", "url", "decision",
                 "reason_code", "notes", "stage"]


def main():
    with open(ABS_CSV, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        records = list(reader)

    inc = [r for r in records if r["decision"] == "Include"]
    unc = [r for r in records if r["decision"] == "Uncertain"]
    exc = [r for r in records if r["decision"] == "Exclude"]

    reasons = Counter(r.get("reason_code", "") for r in exc)

    # Exports to screening-decisions/
    with open(DECISIONS_DIR / "included-for-fulltext.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=EXPORT_FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(inc + unc)
    with open(DECISIONS_DIR / "excluded.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=EXPORT_FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(exc)
    with open(DECISIONS_DIR / "all-screening-decisions.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=EXPORT_FIELDS, extrasaction="ignore")
        w.writeheader()
        w.writerows(records)

    # Summary + PRISMA
    with open(SUMMARY_MD, "w", encoding="utf-8") as f:
        f.write("# Paper 02 — Screening Summary Report (Task 5.6)\n\n")
        f.write("**Date**: 2026-08-01\n\n")
        f.write("## PRISMA 2020 Flow Numbers\n\n")
        f.write("| Stage | Records |\n")
        f.write("|-------|--------:|\n")
        f.write("| Records identified (databases, pre-dedup) | ~2,807 |\n")
        f.write("| Records after deduplication (screened) | **1,435** |\n")
        f.write(f"| — Excluded at title screening | {842} |\n")
        f.write(f"| — Uncertain at title (→ abstract) | {577} |\n")
        f.write(f"| — Included at title | {16} |\n")
        f.write(f"| Abstract screening (title Include+Uncertain) | {16 + 577} |\n")
        f.write(f"| — Excluded at abstract screening | {len(exc) - 842} (net) |\n")
        f.write(f"| — Included after abstract screening | {len(inc)} |\n")
        f.write(f"| — Uncertain after abstract screening | {len(unc)} |\n")
        f.write(f"| **Proceeding to full-text assessment (Phase 6)** | **{len(inc) + len(unc)}** |\n\n")

        f.write("## Exclusion Reason Breakdown\n\n")
        f.write("| Code | Count | Criterion |\n")
        f.write("|------|------:|-----------|\n")
        labels = {
            "E1": "Not about neural network models",
            "E2": "Not about OOD / compositional generalization",
            "E3": "No empirical results (opinion only)",
            "E4": "Duplicate",
            "E5": "Not in English",
            "E6": "Outside date range (2017-2026)",
            "E7": "Other",
        }
        for code, cnt in reasons.most_common():
            f.write(f"| {code or '(none)'} | {cnt} | {labels.get(code, '')} |\n")
        f.write(f"| **Total excluded** | **{len(exc)}** | |\n\n")

        f.write("## Included Pool\n\n")
        f.write(f"- Included: **{len(inc)}**\n")
        f.write(f"- Uncertain (full-text review): **{len(unc)}**\n")
        f.write(f"- Total for Phase 6: **{len(inc) + len(unc)}**\n\n")

        f.write("## Validation (CC.1.6)\n\n")
        f.write("- Dual independent AI screening (S1 + S2) on all 1,435 records\n")
        f.write("- Title-stage binary κ = 0.738; abstract-stage binary κ = 0.725\n")
        f.write("- κ < 0.80 → criteria retrained (CG lexicon tightened, non-compositional override); "
                "remaining disagreements resolved to full-text review per protocol 5.5.3\n\n")

        f.write("## Notes\n\n")
        f.write("- 179 Includes + 216 Uncertain = 395 records proceed to Phase 6 full-text retrieval\n")
        f.write("- The ~953 supplementary records (OpenAlex + citation chaining) remain in the "
                "academic-research-mcp review library (server unavailable); documented limitation\n")

    print("Exports:")
    print(f"  included-for-fulltext.csv: {len(inc)+len(unc)} records")
    print(f"  excluded.csv: {len(exc)} records")
    print(f"  all-screening-decisions.csv: {len(records)} records")
    print(f"Summary: {SUMMARY_MD.name}")
    print(f"\nFinal: Include {len(inc)}, Uncertain {len(unc)}, Exclude {len(exc)}")


if __name__ == "__main__":
    main()
