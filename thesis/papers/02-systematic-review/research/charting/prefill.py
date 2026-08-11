#!/usr/bin/env python3
"""
Paper 02 — Phase 7 (Task 7.2.1): build the per-study prefill skeleton.

Reads Phase 6 artifacts and the finalized schema, and emits a per-study
prefill JSON consumed by prompts.py and merge_ai.py:

  - bibliographic fields from research/included-studies.csv
  - arch/task hints from research/study-characteristics.csv (Phase 6.5.1)
  - seeds hint from study-characteristics.csv seeds_runs
  - peer_reviewed + pub_venue_type derived heuristically from venue/journal

Prefill values are seeds: the external AI pass confirms or corrects every
field against the full text (flagging changes). merge_ai.py keeps prefilled
bibliographic fields verbatim.

Output: research/charting/prefill.json
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
CHARACTERISTICS_CSV = BASE / "research" / "study-characteristics.csv"
SCHEMA_YAML = BASE / "research" / "charting" / "charted-schema.yaml"
OUT_JSON = BASE / "research" / "charting" / "prefill.json"

# venue/journal keyword -> pub_venue_type
VENUE_RULES = [
    (re.compile(r"arxiv|preprint", re.I), "preprint"),
    (re.compile(r"workshop", re.I), "workshop"),
    (re.compile(r"thesis|dissertation", re.I), "thesis"),
    (re.compile(r"technical report|tech\.? report", re.I), "tech_report"),
    (re.compile(r"proceedings|conference|ICLR|NeurIPS|CVPR|ICCV|ECCV|AAAI|IJCAI|"
               r"ACL|EMNLP|NAACL|WWW|KDD|ICML|ICASSP|INTERSPEECH", re.I), "conference"),
]
# journals identified by name pattern (journal titles)
JOURNAL_MARKERS = re.compile(
    r"Journal|Transactions|Letters|Review|Nature|Science|IEEE|ACM Transactions|"
    r"PLOS|Frontiers|MDPI|Elsevier|Springer", re.I)


def derive_venue_type(journal: str, venue: str) -> str:
    """Best-effort pub_venue_type from bibliographic venue/journal."""
    blob = f"{journal} {venue}"
    if not blob.strip() or "arxiv" in blob.lower():
        return "preprint"
    for rx, vtype in VENUE_RULES:
        if rx.search(blob):
            return vtype
    if JOURNAL_MARKERS.search(blob):
        return "journal"
    return "other"


def derive_peer_reviewed(journal: str, source_db: str) -> str:
    """TRUE unless the record is arXiv-only with no journal."""
    if journal.strip():
        return "TRUE"
    src = source_db.lower()
    if "arxiv" in src and ":" in src and src.startswith("arxiv"):
        # arXiv:benchmark / arXiv:primary / arXiv:safety — check for journal column
        return "FALSE" if not journal.strip() else "TRUE"
    return "TRUE"


def main() -> None:
    cfg = yaml.safe_load(SCHEMA_YAML.read_text(encoding="utf-8"))
    study_fields = [f["name"] for f in cfg["study_fields"]]

    inc = {r["study_id"]: r for r in
           csv.DictReader(open(INCLUDED_CSV, newline="", encoding="utf-8"))}
    chars = {r["study_id"]: r for r in
             csv.DictReader(open(CHARACTERISTICS_CSV, newline="", encoding="utf-8"))}

    prefill: dict[str, dict] = {}
    for sid in sorted(inc, key=lambda s: int(s[1:])):
        row = inc[sid]
        ch = chars.get(sid, {})
        record = {
            "study_id": sid,
            "id": row["id"],
            "title": row["title"],
            "authors": row["authors"],
            "year": int(row["year"]) if row["year"].strip().isdigit() else "",
            "venue": row["journal"] or row["url"],
            "doi": row["doi"],
            "arxiv_id": row["arxiv_id"],
            "peer_reviewed": derive_peer_reviewed(row["journal"], row["source_db"]),
            "pub_venue_type": derive_venue_type(row["journal"], row["url"]),
            "extractor_id": "EX1",
            # hints (Phase 6.5.1) — AI pass confirms/corrects
            "_hints": {
                "architectures": ch.get("architectures", ""),
                "benchmarks": ch.get("benchmarks", ""),
                "seeds_runs": ch.get("seeds_runs", ""),
            },
        }
        # keep only fields defined in the schema (plus hints block)
        record = {k: v for k, v in record.items() if k in study_fields or k == "_hints"}
        prefill[sid] = record

    OUT_JSON.parent.mkdir(exist_ok=True)
    OUT_JSON.write_text(
        json.dumps(prefill, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    n_arxiv = sum(1 for r in prefill.values() if r.get("peer_reviewed") == "FALSE")
    n_preprint = sum(1 for r in prefill.values() if r.get("pub_venue_type") == "preprint")
    print(f"prefilled {len(prefill)} studies -> {OUT_JSON}")
    print(f"  peer_reviewed=FALSE: {n_arxiv} | pub_venue_type=preprint: {n_preprint}")
    print("  (peer_reviewed is a heuristic seed — AI pass confirms from full text)")


if __name__ == "__main__":
    sys.exit(main())
