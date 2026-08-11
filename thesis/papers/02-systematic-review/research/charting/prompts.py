#!/usr/bin/env python3
"""
Paper 02 — Phase 7 (Task 7.2.2): generate external-AI prompt batches.

Produces self-contained JSONL tasks for the user's external AI tool. Each
task carries the study's bibliographic prefill, Phase 6.5.1 hints, a
full-text excerpt from research/full-text-txt/, and the complete output
contract (every ai-source study field + the sub-experiment array), so the
AI can:

  - fill every extraction field from the full-text evidence,
  - confirm or correct the prefilled hints (task_primary, arch_primary,
    n_seeds_value) — recording corrections in `flag`,
  - emit one sub-experiment record per unique configuration
    (template section 3; Tasks 7.2.4-7.2.6), and
  - leave fields it cannot verify EMPTY (never guess).

Pilot studies (S061, S089, S109, S046, S038) are excluded — their
gold-standard extractions already live in pilot-extractions/pilot-rows.jsonl.

Output contract (one JSON object per line, keys = exact schema field names):
  {
    "study_id": "S001",
    "<all ai/hint study fields>": <value or "">,
    "sub_experiments": [
      {"sub_exp_id": "S001_E001", "experiment_label": "...",
       "task": "...", "arch": "...", "train_regime": "...",
       "id_acc_mean": 0.0, "id_acc_sd": ..., "id_acc_n_seeds": ...,
       "ood_acc_mean": ..., "ood_acc_sd": ..., "ood_acc_n_seeds": ...,
       "id_ood_gap": ..., "effect_size_type": "...",
       "effect_size_value": ..., "effect_size_se": ...,
       "schema_coherence_value": ..., "notes": "..."},
      ...
    ],
    "flag": {"field": "corrected value", ...}   // optional categorical disagreements
  }

The user saves the model's responses as ai-output/batch-NN.jsonl for merge_ai.py.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
PREFILL_JSON = BASE / "research" / "charting" / "prefill.json"
SCHEMA_YAML = BASE / "research" / "charting" / "charted-schema.yaml"
FULLTEXT_DIR = BASE / "research" / "full-text-txt"
OUT_DIR = BASE / "research" / "charting" / "ai-prompt-batches"

PREF: dict | None = None  # prefill cache, lazily loaded by fulltext_excerpt()

N_BATCHES = 10
LEAD_CAP = 4000     # chars from the start of the text (title/abstract/intro)
RESULTS_CAP = 9000  # chars from the results-dense window
RESULTS_WIN = 4000  # chars around the detected results window

# keywords suggesting where quantitative results live
RESULTS_RE = re.compile(
    r"\b(table|accuracy|precision|recall|F1|AUC|BLEU|perplexity|seed|"
    r"±|\+/-|generaliz|experiment|result)\b", re.I)


def fulltext_excerpt(study_id: str, prefill: dict | None = None) -> str:
    """Return (lead + results-window) excerpt from the study's full text."""
    if prefill is None:
        global PREF
        if PREF is None:
            PREF = json.loads(PREFILL_JSON.read_text(encoding="utf-8"))
        prefill = PREF
    f = FULLTEXT_DIR / f"{prefill[study_id]['id']}.txt"
    try:
        text = f.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""
    lead = text[:LEAD_CAP]
    # results-dense window: max density of results keywords over sliding window
    if len(text) > LEAD_CAP + RESULTS_WIN:
        best_pos, best_score = LEAD_CAP, 0
        for m in RESULTS_RE.finditer(text):
            pos = m.start()
            if pos < LEAD_CAP:
                continue
            win = text[pos:pos + RESULTS_WIN]
            score = len(RESULTS_RE.findall(win))
            if score > best_score:
                best_pos, best_score = pos, score
        tail = text[best_pos:best_pos + RESULTS_CAP]
        return f"{lead}\n\n[...results section excerpt...]\n{tail}"
    return lead


def field_contract(cfg: dict) -> tuple[list[str], list[str], dict[str, str]]:
    """(ai_fields, hint_fields, field->vocab) from the schema."""
    ai_fields, hint_fields, vocab = [], [], {}
    for f in cfg["study_fields"]:
        src = f.get("source", "")
        if src == "ai":
            ai_fields.append(f["name"])
        if f.get("source") == "hint" or f["name"] in (
                "task_primary", "arch_primary", "n_seeds_value"):
            hint_fields.append(f["name"])
        if "vocabulary" in f:
            vocab[f["name"]] = f["vocabulary"]
    return ai_fields, hint_fields, vocab


def main() -> None:
    global N_BATCHES
    if len(sys.argv) > 1:
        N_BATCHES = max(1, int(sys.argv[1]))

    cfg = yaml.safe_load(SCHEMA_YAML.read_text(encoding="utf-8"))
    ai_fields, hint_fields, _ = field_contract(cfg)
    vocab = {v["name"]: v for v in cfg["vocabularies"]} if isinstance(
        cfg.get("vocabularies"), list) else cfg.get("vocabularies", {})

    global PREF
    PREF = json.loads(PREFILL_JSON.read_text(encoding="utf-8"))
    pilot_ids = {r["study_id"] for r in
                 json.loads("[" + ",".join(
                     (BASE / "research/charting/pilot-extractions/pilot-rows.jsonl")
                     .read_text(encoding="utf-8").splitlines()) + "]")}

    tasks = []
    for sid, rec in sorted(PREF.items(), key=lambda kv: int(kv[0][1:])):
        if sid in pilot_ids:
            continue
        hints = rec.pop("_hints", {})
        task = {
            "study_id": sid,
            "title": rec["title"],
            "year": rec["year"],
            "venue": rec["venue"],
            "prefill_hints": {
                "architectures": hints.get("architectures", ""),
                "benchmarks": hints.get("benchmarks", ""),
                "seeds_runs": hints.get("seeds_runs", ""),
            },
            "fulltext_excerpt": fulltext_excerpt(sid),
            "contract": {
                "study_fields": ai_fields + hint_fields,
                "subexp_fields": [f["name"] for f in cfg["subexp_fields"]],
                "vocabularies": vocab,
            },
            "instructions": (
                "Extract the study-level fields and sub-experiment rows from the "
                "full-text excerpt. Use the controlled vocabularies exactly "
                "(see contract.vocabularies). Fill fields ONLY when the evidence "
                "supports them; leave unverifiable fields EMPTY string / empty "
                "array — do not guess. task_primary / arch_primary / n_seeds_value "
                "are seeded in prefill_hints: confirm them, or if the full text "
                "contradicts a hint, put the corrected value in the field and "
                "record it in 'flag'. Sub-experiment rows (contract.subexp_fields): "
                "one per unique (split x architecture x intervention) configuration; "
                "sub_exp_id = {study_id}_E{NN}; use 'default' in split_id/arch_id/"
                "intervention_id when a study has a single configuration. Report "
                "accuracies as proportions 0-1. effect_size_type = 'none' when no "
                "effect size is reported. If the excerpt lacks results numbers, "
                "leave numeric fields empty and note it."),
        }
        tasks.append(task)

    n_total = len(tasks)
    batches = [[] for _ in range(N_BATCHES)]
    for i, t in enumerate(tasks):
        batches[i % N_BATCHES].append(t)

    OUT_DIR.mkdir(exist_ok=True)
    (OUT_DIR / "ai-output").mkdir(exist_ok=True)
    for i, batch in enumerate(batches, start=1):
        out = OUT_DIR / f"batch-{i:02d}.jsonl"
        with open(out, "w", encoding="utf-8") as fh:
            for t in batch:
                fh.write(json.dumps(t, ensure_ascii=False) + "\n")
        chars = sum(len(json.dumps(t, ensure_ascii=False)) for t in batch)
        print(f"{out.name}: {len(batch)} studies, {chars/1000:.0f}k chars "
              f"(~{chars//2600}k tokens)")

    with open(OUT_DIR / "README.md", "w", encoding="utf-8") as fh:
        fh.write(f"""# External-AI extraction batches — Paper 02 Phase 7 (Task 7.2)

{n_total} studies (286 included minus 5 gold-standard pilots) split into
{N_BATCHES} JSONL batches of ~{len(batches[0])} studies each.

## How to run (user)

1. Open each `batch-NN.jsonl` in your AI tool (paste the file content as one
   prompt). If the tool's context window is limited, split a batch in half
   (`split -n l/2 batch-NN.jsonl`) — outputs are merged by study_id.
2. Ask the model to return **one JSON object per line** for every study_id in
   the batch, using exactly the `contract` fields in the prompt file.
3. Save the response as `ai-output/batch-NN.jsonl` (one JSON object per line).
4. Run `python3 merge_ai.py` to validate and merge into `charted-data.csv`.

## Output contract (field names must match exactly)

One JSON object per line:
```
{{"study_id": "S001",
  <all contract.study_fields, "" when not determinable>,
  "sub_experiments": [{{"sub_exp_id": "S001_E001", ...}}],
  "flag": {{"field": "corrected value", ...}}}}
```

- Missing studies in a batch output are logged, not merged (re-run that batch).
- `flag` corrections are applied and recorded in `notes` as
  `ai-revised:field=old->new` for the validation-phase reconciliation log.
- Leave fields empty rather than guessing; numeric accuracies as 0-1.
- 5 gold-standard pilots (S061, S089, S109, S046, S038) are already charted in
  `pilot-extractions/pilot-rows.jsonl` — do not re-extract them.
""")

    print(f"wrote {N_BATCHES} batches + README to {OUT_DIR} (pilots excluded)")


if __name__ == "__main__":
    sys.exit(main())
