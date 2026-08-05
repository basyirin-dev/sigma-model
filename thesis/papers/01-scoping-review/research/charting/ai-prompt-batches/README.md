# External-AI extraction batches — Paper 01 Phase 7

1268 papers split into 5 JSONL batches of ~254 papers each.

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
{"paper_id": "P001",
  "key_contribution": "...", "relevance_justification": "...",
  "relevance_sigma_trap": 4 | null, "open_questions": "...",
  "key_equations_definitions": "...", "datasets_used": "...",
  "sample_size": "...", "effect_sizes": "...",
  "flag": {"field": "corrected value", ...}}
```

- Missing papers in a batch output are logged, not merged (re-run that batch).
- `flag` corrections are applied and recorded in `notes` as `ai-revised:field=old->new`
  for the validation-phase reconciliation log.
- 5 gold-standard examples (pilot papers P002/P034/P040/P073/P1170) are already
  in `charted-data.csv` flagged `pilot=manual-review` — do not overwrite them.
