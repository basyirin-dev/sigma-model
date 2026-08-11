#!/usr/bin/env python3
"""
Paper 01 — Phase 8: validate + merge external-AI D2–D8 scores
(Task 8.2.2).

Reads every quality-batches/ai-output/batch-*.jsonl (one JSON object per
line, contract from quality_prompts.py), validates scores (integer 0-4,
null allowed; D4 only for empirical papers), and merges into
research/quality-scores.csv:

  - integer scores replace blanks; audit trail recorded in `notes` as
    `scored:D=value`.
  - null keeps the existing value (blank or prior).
  - D1/D6 columns are untouched (scripted).

Output: updated quality-scores.csv + quality-merge-report.md
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
SCORES_CSV = BASE / "research" / "quality-scores.csv"
OUT_DIR = BASE / "research" / "charting" / "quality-batches"
REPORT_MD = BASE / "research" / "charting" / "quality-merge-report.md"

SCORE_DIMS = ["D2", "D3", "D4", "D5", "D7", "D8"]
EMPIRICAL_ONLY = {"D4"}


def main() -> None:
    rows = list(csv.DictReader(open(SCORES_CSV, newline="", encoding="utf-8")))
    fields = list(rows[0].keys())
    by_pid = {r["paper_id"]: r for r in rows}

    out_files = sorted(OUT_DIR.glob("ai-output/batch-*.jsonl"))
    n_out = 0
    n_merged = 0
    n_scores = 0
    missing: list[tuple[str, str]] = []
    bad_rows: list[tuple[str, str, str]] = []
    duplicates: list[tuple[str, str]] = []
    remerged: list[tuple[str, str, str]] = []
    audit: list[str] = []

    for f in out_files:
        seen_in_file: set[str] = set()
        for lineno, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                bad_rows.append((f.name, f"line {lineno}", "invalid JSON"))
                continue
            pid = obj.get("paper_id")
            if pid not in by_pid:
                missing.append((f.name, str(pid)))
                continue
            n_out += 1
            if pid in seen_in_file:
                duplicates.append((f.name, pid))
            seen_in_file.add(pid)
            row = by_pid[pid]
            pubtype = (row.get("publication_type") or "").strip().lower()
            for dim in SCORE_DIMS:
                if dim not in obj:
                    continue
                v = obj[dim]
                if v is None:
                    continue  # null = keep existing
                if not isinstance(v, int) or isinstance(v, bool) or not (0 <= v <= 4):
                    bad_rows.append((f.name, pid, f"{dim} not int 0-4: {v!r}"))
                    continue
                if dim in EMPIRICAL_ONLY and pubtype != "empirical":
                    bad_rows.append((f.name, pid,
                                     f"{dim} on non-empirical ({pubtype}) paper"))
                    continue
                if row.get(dim, "") != "":
                    # Already scored. Identical value = benign re-processing of
                    # an already-merged batch; different value = a genuine
                    # conflict that must not silently overwrite.
                    if str(row.get(dim, "")) == str(v):
                        remerged.append((f.name, pid, dim))
                        continue
                    bad_rows.append((f.name, pid,
                                     f"{dim} already scored {row.get(dim)}; "
                                     f"refusing overwrite with {v}"))
                    continue
                row[dim] = str(v)
                row["notes"] = (row.get("notes") or "").strip()
                row["notes"] = (row["notes"] + " | " if row["notes"] else "") + f"scored:{dim}={v}"
                audit.append(f"{pid}:{dim}={v}")
                n_scores += 1
            n_merged += 1

    with open(SCORES_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    with open(REPORT_MD, "w", encoding="utf-8") as fh:
        fh.write("# AI quality-score merge report — Paper 01 Phase 8\n\n")
        fh.write(f"- Output files read: **{len(out_files)}**\n")
        fh.write(f"- Paper objects processed: **{n_out}**\n")
        fh.write(f"- Rows merged/updated: **{n_merged}**\n")
        fh.write(f"- Dimension scores applied: **{n_scores}**\n")
        fh.write(f"- Unknown/missing paper_ids: **{len(missing)}**\n")
        fh.write(f"- Invalid rows: **{len(bad_rows)}**\n")
        fh.write(f"- Duplicate paper_ids within a file: **{len(duplicates)}**\n")
        fh.write(f"- Re-processed identical scores (already merged, benign): "
                 f"**{len(remerged)}**\n")
        if audit:
            fh.write("\n## Scores applied\n\n")
            for a in audit:
                fh.write(f"- {a}\n")
        if missing:
            fh.write("\n## Missing / unknown paper_ids\n\n")
            for f_, p in missing:
                fh.write(f"- {f_}: {p}\n")
        if bad_rows:
            fh.write("\n## Invalid rows (not merged)\n\n")
            for f_, p, reason in bad_rows:
                fh.write(f"- {f_}: {p} — {reason}\n")

    print(f"processed {n_out} objects; merged {n_merged}, scores {n_scores}, "
          f"missing {len(missing)}, bad {len(bad_rows)}, "
          f"remerged {len(remerged)}")
    print(f"wrote {SCORES_CSV.name} and {REPORT_MD.name}")


if __name__ == "__main__":
    sys.exit(main())
