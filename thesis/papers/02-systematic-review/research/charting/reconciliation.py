#!/usr/bin/env python3
"""
Paper 02 — Phase 7 (Task 7.3.4): reconcile extractor-1 vs extractor-2
disagreements on the validation sample.

Produces `reconciliation-items.md` listing every field-level disagreement
with the two extracted values. For each disagreement a default resolution
rule is applied and logged:

  R1  gold-standard pilot values beat both extractors (pilots are not in the
      sample, so this applies to charted data generally)
  R2  where extractor 1 has evidence already merged (post-AI) and extractor 2
      left the field empty, keep extractor 1 (missing value is not a dispute)
  R3  otherwise the disagreement is resolved by the senior reviewer (user):
      the item is marked `unresolved` with the suggested action

Systematic disagreements (>= 25% of the sample differing on a field) trigger
a schema/template refinement note (7.3.4).

Output: research/charting/reconciliation-items.md
"""

from __future__ import annotations

import csv
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
CHARTING = BASE / "research" / "charting"
MAIN_CSV = BASE / "research" / "charted-data-main.csv"
SAMPLE_CSV = CHARTING / "validation-sample.csv"
EX2_JSONL = CHARTING / "validation-batches" / "ai-output" / "batch-01.jsonl"
SCHEMA_YAML = CHARTING / "charted-schema.yaml"
OUT_MD = CHARTING / "reconciliation-items.md"

SYSTEMATIC_THRESHOLD = 0.25


def main() -> None:
    cfg = yaml.safe_load(SCHEMA_YAML.read_text(encoding="utf-8"))
    sample = [r["study_id"] for r in
              csv.DictReader(open(SAMPLE_CSV, newline="", encoding="utf-8"))]
    ex1 = {r["study_id"]: r for r in
           csv.DictReader(open(MAIN_CSV, newline="", encoding="utf-8"))}
    ex2: dict[str, dict] = {}
    if EX2_JSONL.exists():
        for line in EX2_JSONL.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line:
                obj = json.loads(line)
                ex2[obj["study_id"]] = obj

    fields = [f["name"] for f in cfg["study_fields"] if f.get("dual", False)]
    meta = {f["name"]: f for f in cfg["study_fields"]}
    items: list[tuple[str, str, str, str]] = []
    field_diff: Counter[str] = Counter()
    n_compared = 0

    for s in sample:
        if s not in ex2:
            continue
        n_compared += 1
        r2 = ex2[s]
        for f in fields:
            v1, v2 = ex1[s].get(f, ""), r2.get(f, "")
            if v1 == v2:
                continue
            field_diff[f] += 1
            if v1 == "" and v2 != "":
                resolution = ("KEEP ex2 (extractor 1 missing; "
                              "adopt extractor-2 value after spot-check)")
            elif v2 == "" and v1 != "":
                resolution = "KEEP ex1 (extractor 2 missing value; no dispute on substance)"
            else:
                resolution = "UNRESOLVED — senior reviewer decides; see action"
            items.append((s, f, v1, v2, resolution))

    # systematic trigger: structured fields only (free-text fields differ by
    # construction — wording, not coding; excluded per validation-report note 3)
    systematic = {f: c for f, c in field_diff.items()
                  if c >= SYSTEMATIC_THRESHOLD * n_compared
                  and meta.get(f, {}).get("data_type") not in ("text", "long_text")}

    lines = [
        "# Reconciliation items — Paper 02 Phase 7 (Task 7.3.4)",
        "",
        f"- Sample compared: **{n_compared}** studies "
        f"({len(items)} field-level disagreements)",
        "- Resolution rules: R1 pilots are gold; R2 missing value is not a",
        "  dispute (keep the non-empty value); R3 otherwise senior review.",
        "",
        f"## Systematic disagreements (>= {SYSTEMATIC_THRESHOLD:.0%} of sample)",
        "",
    ]
    if systematic:
        for f, c in sorted(systematic.items(), key=lambda kv: -kv[1]):
            lines.append(
                f"- `{f}`: {c}/{n_compared} differ — "
                "**refine template/codebook and re-extract** (7.3.4)")
        lines.append("")
        lines.append("## Template refinement notes")
        lines.append("")
        lines.append("Review the fields above; if the disagreement is a codebook")
        lines.append("ambiguity, update `research/extraction-template.md` and")
        lines.append("`charting/charted-schema.yaml` (bump minor version), then")
        lines.append("re-run the affected extraction.")
        lines.append("")
    else:
        lines.append("- none — no field exceeds the systematic-disagreement threshold")
        lines.append("")

    lines += ["", "## Itemized disagreements", ""]
    if items:
        lines.append("| Study | Field | Extractor 1 | Extractor 2 | Resolution |")
        lines.append("|---|---|---|---|---|")
        for s, f, v1, v2, res in sorted(items, key=lambda t: (t[0], t[1])):
            v1 = str(v1)
            v2 = str(v2)
            v1s = (v1[:60] + "…") if len(v1) > 60 else (v1 or "—")
            v2s = (v2[:60] + "…") if len(v2) > 60 else (v2 or "—")
            lines.append(f"| {s} | {f} | {v1s} | {v2s} | {res} |")
    else:
        lines.append("- no disagreements (extractor 2 matched extractor 1 everywhere)")

    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"wrote {OUT_MD.name}: {len(items)} items, "
          f"{len(systematic)} systematic fields")


if __name__ == "__main__":
    sys.exit(main())
