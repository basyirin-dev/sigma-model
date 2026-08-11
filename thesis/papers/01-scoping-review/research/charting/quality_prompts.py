#!/usr/bin/env python3
"""
Paper 01 — Phase 8: generate external-AI scoring batches for D2–D8
(Task 8.2.2; pilot uses --pilot).

Reuses the Phase 7 pattern (prompts.py): self-contained JSONL tasks that
carry the paper's evidence (abstract + full-text excerpt when a verified
PDF exists) plus the charted-data assists relevant to each dimension, so
the external AI can score the rater-scored credibility dimensions:

  D2  author authority
  D3  formal methods rigor        (applicability-gated: neutral 2 when the
                                   contribution type does not admit formal
                                   methods)
  D4  empirical reproducibility   (empirical papers only; null otherwise)
  D5  argumentative rigor
  D7  transparency
  D8  prior-lit engagement

D1 (venue) and D6 (citation/uptake) are scripted by quality_score.py and
are NOT emitted here; raters refine them separately if needed.

Output contract (one JSON object per line):
  {
    "paper_id": "P002",
    "D2": 0-4 | null, "D3": 0-4 | null, "D4": 0-4 | null (empirical only),
    "D5": 0-4 | null, "D7": 0-4 | null, "D8": 0-4 | null,
    "justifications": { "D2": "short rationale", ... }  // optional
  }

The user saves model responses as ai-prompt-batches/ai-output/batch-NN.jsonl
for merge_quality_ai.py.
"""

from __future__ import annotations

import csv
import json
import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
CHARTED_CSV = BASE / "research" / "charting" / "charted-data.csv"
SCORES_CSV = BASE / "research" / "quality-scores.csv"
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
PDF_MAP_CSV = BASE / "research" / "charting" / "pdf-map.csv"
PDF_DIR = BASE / "research" / "pdfs"
OUT_DIR = BASE / "research" / "charting" / "quality-batches"

N_BATCHES = 5
ABS_CAP = 1000
FT_CAP = 1200
FT_PAGES = 3

# rater-scored dimensions: field -> (charted assist fields, applicability)
DIMENSIONS = {
    "D2": ["authors"],
    "D3": ["formal_framework", "mathematical_formalism", "key_equations_definitions"],
    "D4": ["datasets_used", "sample_size", "effect_sizes"],
    "D5": ["key_contribution"],
    "D7": ["limitations_stated"],
    "D8": ["key_contribution"],
}
# D4 empirical-only; null otherwise.
EMPIRICAL_ONLY = {"D4"}

ANCHORS = """Scoring anchors (quality-criteria.md §6, each dimension 0-4):
D2 Author authority: 0=anonymous/first-time;
   2=recognized safety researcher (2-5 prior contributions);
   4=field leader (10+ cited, institutional grounding).
   Base on safety-specific track record, not generic h-index.
D3 Formal methods rigor: 0=no formal apparatus;
   2=semi-formal (definitions, structured argument);
   4=machine-checked proof / SLT-grade analysis.
   APPLICABILITY GATE: if the contribution type does not admit formal
   methods (policy, conceptual opinion), score neutral 2 — do not penalize
   for absence of formal apparatus where none is expected; reward 3-4 only
   when formal methods add genuine rigor.
D4 Empirical reproducibility (EMPIRICAL PAPERS ONLY, else null):
   0=no code/data/seeds; 2=partial code or documented setup;
   4=full code + data + preregistration + replication.
D5 Argumentative rigor: 0=undefined terms, no counterarguments;
   2=explicit definitions, some counterarguments;
   4=all premises identified, counterarguments fully addressed.
D7 Transparency: 0=no limitations, no threat model;
   2=limitations stated but vague;
   4=explicit limitations + threat model + disclosed funding.
D8 Prior-lit engagement: 0=reinvents known concepts; 2=cites some prior work;
   4=positioned relative to canonical references (Hubinger, Christiano, Ngo,
   Carlsmith, Wentworth, etc.).
Return an integer 0-4 per dimension, or null when the evidence genuinely
cannot support a judgment. Never guess venue prestige (D1) or citation
uptake (D6) — those are scripted."""


def pdf_excerpt(pdf_file: str) -> str:
    path = PDF_DIR / pdf_file
    try:
        out = subprocess.run(
            ["pdftotext", "-f", "1", "-l", str(FT_PAGES), str(path), "-"],
            capture_output=True, text=True, timeout=45)
    except Exception:
        return ""
    return (out.stdout or "")[:FT_CAP]


def build_tasks(rows: list[dict], inc: dict, pmap: dict, only: set[str] | None) -> list[dict]:
    tasks = []
    for r in rows:
        pid = r["paper_id"]
        if only is not None and pid not in only:
            continue
        abstract = (inc.get(pid, {}).get("abstract") or "")[:ABS_CAP]
        pdf = pmap.get(pid, "")
        excerpt = pdf_excerpt(pdf) if pdf else ""
        assists = {}
        for dim, fields in DIMENSIONS.items():
            vals = [r.get(f, "") for f in fields if (r.get(f, "") or "").strip()]
            if vals:
                assists[dim] = " | ".join(vals)[:900]
        pubtype = (r.get("publication_type") or "").strip().lower()
        dim_list = [d for d in DIMENSIONS if not (d in EMPIRICAL_ONLY and pubtype != "empirical")]
        task = {
            "paper_id": pid,
            "title": r.get("title", ""),
            "year": r.get("year", ""),
            "venue": r.get("venue", ""),
            "publication_type": pubtype,
            "evidence_basis": r.get("evidence_basis", ""),
            "abstract": abstract,
            "fulltext_excerpt": excerpt,
            "charted_assists": assists,
            "dimensions_to_score": dim_list,
            "instructions": (
                "Score ONLY the rater-scored credibility dimensions listed in "
                "dimensions_to_score using the anchors below. Base judgments on "
                "the abstract/fulltext evidence and charted_assists; if evidence "
                "is only an abstract, mark confidence low but still score. "
                "D4 is only for empirical papers. "
                "Return one JSON object per line exactly matching the contract "
                "in the header."),
            "anchors": ANCHORS,
        }
        tasks.append(task)
    return tasks


def main() -> None:
    n_batches = N_BATCHES
    only: set[str] | None = None
    pilot_csv = BASE / "research" / "charting" / "quality-pilot.csv"
    args = [a for a in sys.argv[1:]]
    if "--pilot" in args:
        with open(pilot_csv, newline="", encoding="utf-8") as pfh:
            only = {r["paper_id"] for r in csv.DictReader(pfh)}
        n_batches = 1
        args.remove("--pilot")
    if args:
        n_batches = max(1, int(args[0]))

    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "ai-output").mkdir(exist_ok=True)

    inc = {r["study_id"]: r for r in
           csv.DictReader(open(INCLUDED_CSV, newline="", encoding="utf-8"))}
    pmap = {r["study_id"]: r["pdf_file"] for r in
            csv.DictReader(open(PDF_MAP_CSV, newline="", encoding="utf-8"))}
    rows = list(csv.DictReader(open(CHARTED_CSV, newline="", encoding="utf-8")))

    tasks = build_tasks(rows, inc, pmap, only)
    batches = [[] for _ in range(n_batches)]
    for i, t in enumerate(tasks):
        batches[i % n_batches].append(t)

    for i, batch in enumerate(batches, start=1):
        out = OUT_DIR / f"batch-{i:02d}.jsonl"
        with open(out, "w", encoding="utf-8") as fh:
            for t in batch:
                fh.write(json.dumps(t, ensure_ascii=False) + "\n")
        chars = sum(len(json.dumps(t, ensure_ascii=False)) for t in batch)
        print(f"{out.name}: {len(batch)} papers, {chars/1000:.0f}k chars")

    with open(OUT_DIR / "README.md", "w", encoding="utf-8") as fh:
        fh.write(f"""# External-AI quality-scoring batches — Paper 01 Phase 8

{len(tasks)} papers split into {n_batches} JSONL batches
(full run: {len(rows)} papers across 5 batches; --pilot: the 10 pilot papers in 1 batch).

## How to run (user)

1. Open each `batch-NN.jsonl` in your AI tool (paste file content as one prompt).
2. Ask the model to return **one JSON object per line** for every paper_id,
   using exactly the output contract in the prompt file header.
3. Save responses as `ai-output/batch-NN.jsonl`.
4. Run `python3 merge_quality_ai.py` to validate + merge into `quality-scores.csv`.

## Output contract (field names must match exactly)

```
{{"paper_id": "P002",
  "D2": 0-4|null, "D3": 0-4|null, "D4": 0-4|null (empirical only),
  "D5": 0-4|null, "D7": 0-4|null, "D8": 0-4|null,
  "justifications": {{"D2": "...", ...}}}}
```

- Scores are integers 0-4; null = evidence insufficient (keeps existing/blank).
- D1 (venue) and D6 (citations) are scripted — do NOT return them.
- Pilot papers are scored identically; their scores feed 8.1.5 dual-scorer IRR.
""")

    print(f"wrote {n_batches} batch(es) + README to {OUT_DIR}")


if __name__ == "__main__":
    sys.exit(main())
