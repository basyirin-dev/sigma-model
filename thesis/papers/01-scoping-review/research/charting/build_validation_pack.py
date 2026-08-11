#!/usr/bin/env python3
"""
Paper 01 — Phase 8: build the 8.2.5 validation-scoring pack (Task 8.2.5).

Extracts the validation-sample papers (research/charting/validation-sample.csv,
254 papers, fixed seed) from the full-run scoring batches
(quality-batches/batch-*.jsonl) into a single self-contained JSONL pack for
independent rater-2 scoring:

  - the two 8.1.5 pilot overlaps (P003, P1036) are excluded — they are
    already dual-scored under the pilot IRR and have no full-run rater-1
    scores to pair against; effective sample = 252 papers.
  - tasks keep the exact batch format (title, venue, year, abstract,
    fulltext_excerpt, charted_assists, dimensions_to_score, §6 anchors) so
    the rater scores them identically to the batches/pilot.
  - D4 remains gated to empirical papers only.

Validates: 252 unique ids, all present, no pilot ids, D4 gating, and prints
an evidence-basis breakdown for the rater.

Output: research/charting/quality-batches/validation/validation-01.jsonl
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
VALIDATION_CSV = BASE / "research" / "charting" / "validation-sample.csv"
BATCHES_DIR = BASE / "research" / "charting" / "quality-batches"
OUT_DIR = BATCHES_DIR / "validation"
OUT_FILE = OUT_DIR / "validation-01.jsonl"

PILOT_IDS = {"P002", "P003", "P032", "P034", "P040",
             "P073", "P1030", "P1036", "P1170", "P635"}
EMPIRICAL_ONLY = {"D4"}


def main() -> int:
    sample = list(csv.DictReader(open(VALIDATION_CSV, newline="", encoding="utf-8")))
    wanted = [r["paper_id"] for r in sample if r["paper_id"] not in PILOT_IDS]
    wanted_set = set(wanted)
    if len(wanted) != len(wanted_set):
        print(f"error: {len(wanted) - len(wanted_set)} duplicate ids in sample",
              file=sys.stderr)
        return 1

    by_pid: dict[str, dict] = {}
    batch_files = sorted(BATCHES_DIR.glob("batch-*.jsonl"))
    for bf in batch_files:
        for line in bf.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line:
                continue
            task = json.loads(line)
            pid = task["paper_id"]
            if pid in wanted_set:
                if pid in by_pid:
                    print(f"error: {pid} present in multiple batches", file=sys.stderr)
                    return 1
                by_pid[pid] = task

    missing = wanted_set - set(by_pid)
    if missing:
        print(f"error: {len(missing)} ids missing from batches: "
              f"{sorted(missing)[:10]}", file=sys.stderr)
        return 1

    # Preserve sample order (matches validation-sample.csv ordering).
    ordered = [by_pid[pid] for pid in wanted]

    # Validate evidence + D4 gating, recompute dimensions_to_score from the
    # sample's publication_type (source of truth for the validation sample).
    pubtype = {r["paper_id"]: (r.get("publication_type") or "").strip().lower()
               for r in sample}
    for task in ordered:
        pid = task["paper_id"]
        pt = pubtype.get(pid, "")
        task["publication_type"] = pt
        dims = [d for d in ("D2", "D3", "D4", "D5", "D7", "D8")
                if not (d in EMPIRICAL_ONLY and pt != "empirical")]
        task["dimensions_to_score"] = dims

    OUT_DIR.mkdir(exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as fh:
        for task in ordered:
            fh.write(json.dumps(task, ensure_ascii=False) + "\n")

    from collections import Counter
    ev = Counter(r["evidence_basis"] for r in sample)
    chars = sum(len(json.dumps(t, ensure_ascii=False)) for t in ordered)
    print(f"wrote {len(ordered)} papers -> {OUT_FILE.relative_to(BASE)}")
    print(f"evidence: {dict(ev)}")
    print(f"pilot excluded: {sorted(set(r['paper_id'] for r in sample) & PILOT_IDS)}")
    print(f"batch sources: {len(batch_files)} files")
    print(f"size: {len(ordered)} tasks, {chars/1000:.0f}k chars")
    return 0


if __name__ == "__main__":
    sys.exit(main())
