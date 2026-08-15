#!/usr/bin/env python3
"""
Paper 01 — Phase 7: generate external-AI prompt batches (Task 7.2.4/7.2.5).

Produces self-contained JSONL tasks for the user's external AI tool. Each
task carries the paper's evidence (abstract + full-text excerpt when a
verified PDF exists) plus the scripted heuristic values, so the AI can:

  - write the free-text fields (key_contribution, relevance_justification,
    open_questions, key_equations_definitions, datasets_used, sample_size,
    effect_sizes) from the evidence, and
  - flag categorical disagreements for reconciliation (validation, Task 7.3).

Output contract (one JSON object per line, keys = exact field names):
  {
    "paper_id": "P001",
    "key_contribution": "2-3 sentence summary",
    "relevance_justification": "why relevant to sigma-trap thesis",
    "relevance_sigma_trap": 4,                 // revised 1-5 or null to keep seed
    "open_questions": "numbered list or empty string",
    "key_equations_definitions": "or empty string",
    "datasets_used": "or empty string",
    "sample_size": "or empty string",
    "effect_sizes": "or empty string",
    "flag": { "field": "corrected value", ... }  // optional categorical disagreements
  }

The user saves the model's responses as ai-prompt-batches/ai-output/batch-NN.jsonl
for merge_ai.py.
"""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
PDF_MAP_CSV = BASE / "research" / "charting" / "pdf-map.csv"
PDF_DIR = BASE / "research" / "pdfs"
OUT_DIR = BASE / "research" / "charting" / "ai-prompt-batches"

N_BATCHES = 5
ABS_CAP = 1000     # chars of abstract per task
FT_CAP = 1200       # chars of full-text excerpt per task
FT_PAGES = 3

AI_FIELDS = ["key_contribution", "relevance_justification", "open_questions",
             "key_equations_definitions", "datasets_used", "sample_size",
             "effect_sizes"]
CTX_FIELDS = ["publication_type", "subdomains", "formal_framework",
              "mathematical_formalism", "methodology",
              "discusses_internal_representations", "discusses_schema_coherence",
              "limitations_stated"]


def pdf_excerpt(pdf_file: str) -> str:
    path = PDF_DIR / pdf_file
    try:
        out = subprocess.run(
            ["pdftotext", "-f", "1", "-l", str(FT_PAGES), str(path), "-"],
            capture_output=True, text=True, timeout=45)
    except Exception:
        return ""
    return (out.stdout or "")[:FT_CAP]


def main() -> None:
    global N_BATCHES
    if len(sys.argv) > 1:
        N_BATCHES = max(1, int(sys.argv[1]))
    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "ai-output").mkdir(exist_ok=True)

    inc = {r["study_id"]: r for r in
           csv.DictReader(open(INCLUDED_CSV, newline="", encoding="utf-8"))}
    pmap = {r["study_id"]: r["pdf_file"] for r in
            csv.DictReader(open(PDF_MAP_CSV, newline="", encoding="utf-8"))}
    rows = list(csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")))

    tasks = []
    for r in rows:
        pid = r["paper_id"]
        abstract = (inc.get(pid, {}).get("abstract") or "")[:ABS_CAP]
        pdf = pmap.get(pid, "")
        excerpt = pdf_excerpt(pdf) if pdf else ""
        task = {
            "paper_id": pid,
            "title": r["title"],
            "year": r["year"],
            "venue": r["venue"],
            "evidence_basis": r["evidence_basis"],
            "abstract": abstract,
            "fulltext_excerpt": excerpt,
            "heuristic_values": {f: r[f] for f in CTX_FIELDS},
            "relevance_seed": r["relevance_sigma_trap"],
            "instructions": (
                "Write the free-text extraction fields from the evidence. "
                "If the evidence is only an abstract, base judgments on it "
                "and mark confidence low. relevance_sigma_trap: revise from "
                "the seed if the evidence clearly justifies a different 1-5; "
                "else null. key_equations_definitions only if the paper uses "
                "a formal framework; datasets_used/sample_size/effect_sizes "
                "only if empirical. In 'flag', list any categorical "
                "heuristic_values you disagree with and your corrected value."),
        }
        tasks.append(task)

    n_total = len(tasks)
    # round-robin split into N_BATCHES (keeps evidence balance across batches)
    batches = [[] for _ in range(N_BATCHES)]
    for i, t in enumerate(tasks):
        batches[i % N_BATCHES].append(t)

    for i, batch in enumerate(batches, start=1):
        out = OUT_DIR / f"batch-{i:02d}.jsonl"
        with open(out, "w", encoding="utf-8") as fh:
            for t in batch:
                fh.write(json.dumps(t, ensure_ascii=False) + "\n")
        chars = sum(len(json.dumps(t, ensure_ascii=False)) for t in batch)
        print(f"{out.name}: {len(batch)} papers, {chars/1000:.0f}k chars (~{chars//2200}k tokens)")

    with open(OUT_DIR / "README.md", "w", encoding="utf-8") as fh:
        fh.write(f"""# External-AI extraction batches — Paper 01 Phase 7

{n_total} papers split into {N_BATCHES} JSONL batches of ~{len(batches[0])} papers each.

## How to run (user)

1. Open each `batch-NN.jsonl` in your AI tool (paste the file content as one
   prompt). If the tool's context window is limited, split a batch in half
   (`split -n l/2 batch-NN.jsonl`) — outputs are merged by paper_id.
2. Ask the model to return **one JSON object per line** for every paper_id in
   the batch, using exactly the output contract in the prompt file header.
3. Save the response as `ai-output/batch-NN.jsonl` (one JSON object per line).
4. Run `python3 merge_ai.py` to validate and merge into `charted-data.csv`.

## Output contract (field names must match exactly)

```
{{"paper_id": "P001",
  "key_contribution": "...", "relevance_justification": "...",
  "relevance_sigma_trap": 4 | null, "open_questions": "...",
  "key_equations_definitions": "...", "datasets_used": "...",
  "sample_size": "...", "effect_sizes": "...",
  "flag": {{"field": "corrected value", ...}}}}
```

- Missing papers in a batch output are logged, not merged (re-run that batch).
- `flag` corrections are applied and recorded in `notes` as `ai-revised:field=old->new`
  for the validation-phase reconciliation log.
- 5 gold-standard examples (pilot papers P002/P034/P040/P073/P1170) are already
  in `charted-data.csv` flagged `pilot=manual-review` — do not overwrite them.
""")

    print(f"wrote {N_BATCHES} batches + README to {OUT_DIR}")


if __name__ == "__main__":
    sys.exit(main())
