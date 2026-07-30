#!/usr/bin/env python3
"""
Paper 01 — Phase 4: Field check, screening CSV, dedup enhancements.

Quick operations (no O(n²) fuzzy matching):
1. Field completeness check (4.4.1)
2. Same-DOI-different-source duplicates report (4.3.2)
3. Screening CSV with decision columns (4.5.1-4.5.2)
4. Update dedup stats
"""

import csv, re, logging
from collections import defaultdict
from pathlib import Path
from datetime import date

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

BASE = Path(__file__).resolve().parent.parent  # .../01-scoping-review/research/
LIB_DIR = BASE / "clean-library"
CSV_PATH = LIB_DIR / "paper01-library.csv"
SCREENING_CSV = LIB_DIR / "paper01-library-screening.csv"
REPORT_PATH = LIB_DIR / "deduplication-report.md"

CHECK_FIELDS = ["title", "authors", "year", "doi", "url", "abstract", "keywords", "source_db", "journal"]


def load(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# ── 1. Field completeness (4.4.1) ─────────────────────────────────────

def check_fields(records: list[dict]) -> dict:
    stats = {}
    for field in CHECK_FIELDS:
        present = sum(1 for r in records if r.get(field, "").strip())
        pct = round(present / len(records) * 100, 1)
        stats[field] = {"present": present, "pct": pct}
    return stats


# ── 2. Same-DOI multi-source detection (4.3.2) ───────────────────────

def find_multi_source(records: list[dict]) -> list[dict]:
    """Find DOIs that appear in multiple source databases."""
    doi_groups = defaultdict(list)
    for r in records:
        doi = r.get("doi", "").strip().lower()
        if doi:
            doi_groups[doi].append(r)

    multi = []
    for doi, group in doi_groups.items():
        sources = set(r["source_db"] for r in group)
        if len(sources) > 1:
            multi.append({
                "doi": doi,
                "sources": sources,
                "count": len(group),
                "records": group,
            })
    multi.sort(key=lambda x: -x["count"])
    return multi


# ── 3. Screening CSV (4.5.1-4.5.2) ───────────────────────────────────

def create_screening_csv(records: list[dict], path: Path):
    fields = [
        "id", "title", "authors", "year", "doi", "arxiv_id", "abstract",
        "keywords", "source_db", "journal", "url",
        "decision", "reason_code", "notes",
    ]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for r in records:
            row = {k: r.get(k, "") for k in fields[:11]}
            row["decision"] = ""      # Include / Exclude / Unsure
            row["reason_code"] = ""   # E1-E7 or blank
            row["notes"] = ""
            w.writerow(row)


# ── 4. Report append ─────────────────────────────────────────────────

def append_report(path: Path, stats: dict, multi: list):
    with open(path, "a", encoding="utf-8") as f:
        # Field completeness
        f.write(f"\n## Field Completeness (n={sum(s['present'] for s in stats.values()):,} total fields)\n\n")
        f.write("| Field | Present | Coverage |\n")
        f.write("|-------|--------:|--------:|\n")
        for field in CHECK_FIELDS:
            s = stats[field]
            flag = " ⚠️" if s["pct"] < 50 else ""
            f.write(f"| {field} | {s['present']:,} | {s['pct']}%{flag} |\n")

        # Multi-source summary
        f.write(f"\n## Multi-Source Duplicates (same DOI, different databases)\n\n")
        f.write(f"**Records with multiple source tags**: {len(multi)} DOIs appear in ≥2 databases\n\n")

        # Screening columns guide
        f.write(f"\n## Screening Column Guide\n\n")
        f.write(f"Screening CSV columns for Phase 5:\n")
        f.write(f"- `decision`: Include / Exclude / Unsure\n")
        f.write(f"- `reason_code`: E1=Not neural network, E2=Not CG, E3=No empirical,\n")
        f.write(f"  E4=Duplicate, E5=Not English, E6=Outside date, E7=Other\n")
        f.write(f"- `notes`: Free-text rationale\n")


def main():
    records = load(CSV_PATH)
    log.info("Loaded %s records", len(records))

    # 1. Field completeness
    log.info("Checking field completeness...")
    stats = check_fields(records)
    for f, s in sorted(stats.items(), key=lambda x: x[1]["pct"]):
        flag = " ⚠️" if s["pct"] < 50 else ""
        log.info("  %-12s %5.1f%% present%s", f, s["pct"], flag)

    # 2. Multi-source detection
    log.info("Finding multi-DB duplicates...")
    multi = find_multi_source(records)
    log.info("  %s DOIs appear in ≥2 databases", len(multi))

    # 3. Screening CSV
    create_screening_csv(records, SCREENING_CSV)
    log.info("Screening CSV: %s records → %s", len(records), SCREENING_CSV.name)

    # 4. Append report
    append_report(REPORT_PATH, stats, multi)
    log.info("Report updated: %s", REPORT_PATH.name)

    print(f"\n{'='*60}")
    print(f"  Phase 4 Enhancements — Complete")
    print(f"{'='*60}")
    print(f"  Field completeness:     appended to dedup report")
    print(f"  Multi-source DOIs:      {len(multi)} flagged")
    print(f"  Screening CSV:          {SCREENING_CSV.name}")
    print(f"    2,867 records with decision/reason/notes columns")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
