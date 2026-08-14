#!/usr/bin/env python3
"""
Paper 02 — Phase 7 (Task 7.3.1): generate the second-extractor prompt batch.

Independent second extraction of the 20% validation sample (CC.1.6). Uses the
same output contract as the main AI pass but instructs the extractor to code
INDEPENDENTLY — i.e., from the full-text excerpt alone, without access to the
first extractor's values (the prefilled hints are still provided; corrections
are flagged as usual, and any value matching the hint is still independent
coding).

Output: research/charting/validation-batches/batch-01.jsonl
        (user saves responses as validation-batches/ai-output/batch-01.jsonl)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
CHARTING = BASE / "research" / "charting"
PREFILL_JSON = CHARTING / "prefill.json"
SCHEMA_YAML = CHARTING / "charted-schema.yaml"
SAMPLE_CSV = CHARTING / "validation-sample.csv"
FULLTEXT_DIR = BASE / "research" / "full-text-txt"
OUT_DIR = CHARTING / "validation-batches"

sys.path.insert(0, str(CHARTING))
from prompts import fulltext_excerpt  # noqa: E402  (shared excerpt logic)


def main() -> None:
    cfg = yaml.safe_load(SCHEMA_YAML.read_text(encoding="utf-8"))
    prefill = json.loads(PREFILL_JSON.read_text(encoding="utf-8"))
    import csv
    sample = [r["study_id"] for r in
              csv.DictReader(open(SAMPLE_CSV, newline="", encoding="utf-8"))]

    ai_fields = [f["name"] for f in cfg["study_fields"] if f.get("source") == "ai"]
    hint_fields = ["task_primary", "arch_primary", "n_seeds_value"]
    subexp_fields = [f["name"] for f in cfg["subexp_fields"]]
    vocab = cfg.get("vocabularies", {})

    tasks = []
    for sid in sample:
        rec = prefill[sid]
        hints = rec.pop("_hints", {})
        task = {
            "study_id": sid,
            "title": rec["title"],
            "year": rec["year"],
            "venue": rec["venue"],
            "extractor": "EX2",
            "prefill_hints": {
                "architectures": hints.get("architectures", ""),
                "benchmarks": hints.get("benchmarks", ""),
                "seeds_runs": hints.get("seeds_runs", ""),
            },
            "fulltext_excerpt": fulltext_excerpt(sid),
            "contract": {
                "study_fields": ai_fields + hint_fields,
                "subexp_fields": subexp_fields,
                "vocabularies": vocab,
            },
            "instructions": (
                "SECOND-EXTRACTOR PASS (independent validation). Code this study "
                "from the full-text excerpt alone, as if you had never seen it "
                "before. Do not try to match or guess any other extractor's "
                "answers — your values are compared against extractor 1 for "
                "inter-rater agreement (kappa/ICC). Fill fields ONLY when the "
                "evidence supports them; leave unverifiable fields EMPTY — do "
                "not guess. Same output contract as extractor 1: study fields + "
                "sub_experiments + flag. Accuracies as proportions 0-1."),
        }
        tasks.append(task)

    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "ai-output").mkdir(exist_ok=True)
    out = OUT_DIR / "batch-01.jsonl"
    with open(out, "w", encoding="utf-8") as fh:
        for t in tasks:
            fh.write(json.dumps(t, ensure_ascii=False) + "\n")
    chars = sum(len(json.dumps(t, ensure_ascii=False)) for t in tasks)
    print(f"{out.name}: {len(tasks)} studies, {chars/1000:.0f}k chars "
          f"(~{chars//2600}k tokens)")

    (OUT_DIR / "README.md").write_text(
        f"""# Second-extractor validation batch — Paper 02 Phase 7 (Task 7.3)

{len(tasks)} sample studies for independent second extraction (CC.1.6).

1. Open `batch-01.jsonl` in your AI tool (split in half if the context window
   is limited — outputs are merged by study_id).
2. Ask the model to return one JSON object per line for every study_id, using
   exactly the `contract` fields. The model must code INDEPENDENTLY (it should
   not see extractor-1 answers — they are not in the batch file).
3. Save the response as `ai-output/batch-01.jsonl`.
4. Run `python3 validate.py` to compute Cohen's kappa / ICC(2,1).
5. Run `python3 reconciliation.py` to log and resolve disagreements.

Contract: identical to the main extraction pass (see `ai-prompt-batches/README.md`).
""", encoding="utf-8")
    print(f"wrote {OUT_DIR.name}/README.md")


if __name__ == "__main__":
    sys.exit(main())
