#!/usr/bin/env python3
"""
Paper 01 — Phase 7: validate + merge external-AI extraction output
(Task 7.2.4/7.2.5).

Reads every ai-prompt-batches/ai-output/batch-*.jsonl (one JSON object per
line, contract from prompts.py), validates against the finalized schema,
and merges into charted-data.csv:

  - AI free-text fields are written verbatim.
  - relevance_sigma_trap: int 1-5 replaces the seed; null keeps the seed.
  - flag corrections are applied to categorical fields and recorded in
    `notes` as `ai-revised:field=old->new`.
  - pilot gold-standard rows (notes ~ pilot=manual-review) are never
    overwritten (logged).

Output: updated charted-data.csv + merge-report.md
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
OUT_DIR = BASE / "research" / "charting" / "ai-prompt-batches"
SCHEMA_YAML = BASE / "research" / "charting" / "charted-schema.yaml"
REPORT_MD = BASE / "research" / "charting" / "merge-report.md"

AI_TEXT_FIELDS = ["key_contribution", "relevance_justification", "open_questions",
                  "key_equations_definitions", "datasets_used", "sample_size",
                  "effect_sizes"]
CAT_FIELDS = ["publication_type", "subdomains", "formal_framework",
              "mathematical_formalism", "methodology",
              "discusses_internal_representations", "discusses_schema_coherence",
              "limitations_stated"]
# Flag-field name -> controlled-vocabulary key in charted-schema.yaml
# (the trinary fields live under trinary/schema_coherence/limitations).
FIELD_VOCAB = {
    "discusses_internal_representations": "trinary",
    "discusses_schema_coherence": "schema_coherence",
    "limitations_stated": "limitations",
}

BOOL_TO_STR = {True: "yes", False: "no"}


def load_vocabularies() -> dict[str, set[str]]:
    cfg = yaml.safe_load(SCHEMA_YAML.read_text(encoding="utf-8"))
    v = cfg["controlled_vocabularies"]
    return {k: {BOOL_TO_STR.get(x, x) for x in vals} for k, vals in v.items()}


def main() -> None:
    vocab = load_vocabularies()
    rows = list(csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")))
    by_pid = {r["paper_id"]: r for r in rows}
    fields = list(rows[0].keys())

    out_files = sorted(OUT_DIR.glob("ai-output/batch-*.jsonl"))
    n_out = 0
    n_merged = 0
    n_flags = 0
    n_skipped_pilot = 0
    n_revisions = 0
    missing: list[tuple[str, str]] = []   # (file, paper_id)
    bad_rows: list[tuple[str, str, str]] = []  # (file, paper_id, reason)
    revisions: list[str] = []

    for f in out_files:
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
            row = by_pid[pid]
            if "pilot=manual-review" in (row.get("notes") or ""):
                n_skipped_pilot += 1
                continue
            # free-text AI fields
            for k in AI_TEXT_FIELDS:
                v = obj.get(k)
                if isinstance(v, str):
                    row[k] = v
            # relevance revision
            rel = obj.get("relevance_sigma_trap")
            if isinstance(rel, int) and 1 <= rel <= 5 and str(rel) != row["relevance_sigma_trap"]:
                old = row["relevance_sigma_trap"]
                row["relevance_sigma_trap"] = str(rel)
                row["relevance_justification"] = row["relevance_justification"] or \
                    f"(revised {old}->{rel} by AI)"
                revisions.append(f"{pid}:relevance_sigma_trap:{old}->{rel}")
                n_revisions += 1
            # flag corrections
            flags = obj.get("flag") or {}
            if not isinstance(flags, dict):
                bad_rows.append((f.name, pid, "flag not an object"))
                continue
            for field, val in flags.items():
                if field not in CAT_FIELDS:
                    bad_rows.append((f.name, pid, f"unknown flag field {field}"))
                    continue
                vkey = FIELD_VOCAB.get(field, field)
                if not (isinstance(val, str) and val in vocab[vkey]):
                    bad_rows.append((f.name, pid, f"flag {field} value not in vocabulary: {val!r}"))
                    continue
                old = row[field]
                if old == val:
                    continue
                row[field] = val
                row["notes"] = (row.get("notes") or "") + f" | ai-revised:{field}={old}->{val}"
                revisions.append(f"{pid}:{field}:{old}->{val}")
                n_flags += 1
            n_merged += 1

    with open(CHARTED_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    with open(REPORT_MD, "w", encoding="utf-8") as fh:
        fh.write("# AI merge report — Paper 01 Phase 7\n\n")
        fh.write(f"- Output files read: **{len(out_files)}**\n")
        fh.write(f"- Paper objects processed: **{n_out}**\n")
        fh.write(f"- Rows merged/updated: **{n_merged}**\n")
        fh.write(f"- Pilot gold rows skipped (protected): **{n_skipped_pilot}**\n")
        fh.write(f"- flag corrections applied: **{n_flags}**\n")
        fh.write(f"- relevance revisions: **{n_revisions}**\n")
        fh.write(f"- Unknown/missing paper_ids: **{len(missing)}**\n")
        fh.write(f"- Invalid rows: **{len(bad_rows)}**\n")
        if revisions:
            fh.write("\n## Revisions applied\n\n")
            for r in revisions:
                fh.write(f"- {r}\n")
        if missing:
            fh.write("\n## Missing / unknown paper_ids\n\n")
            for f_, p in missing:
                fh.write(f"- {f_}: {p}\n")
        if bad_rows:
            fh.write("\n## Invalid rows (not merged)\n\n")
            for f_, p, reason in bad_rows:
                fh.write(f"- {f_}: {p} — {reason}\n")

    print(f"processed {n_out} objects from {len(out_files)} files; "
          f"merged {n_merged}, flags {n_flags}, revisions {n_revisions}, "
          f"pilot skipped {n_skipped_pilot}, missing {len(missing)}, bad {len(bad_rows)}")
    print(f"wrote {CHARTED_CSV.name} and {REPORT_MD.name}")


if __name__ == "__main__":
    sys.exit(main())
