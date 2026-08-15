# External-AI extraction batches — Paper 02 Phase 7 (Task 7.2)

281 studies (286 included minus 5 gold-standard pilots) split into
10 JSONL batches of ~29 studies each.

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
{"study_id": "S001",
  <all contract.study_fields, "" when not determinable>,
  "sub_experiments": [{"sub_exp_id": "S001_E001", ...}],
  "flag": {"field": "corrected value", ...}}
```

- Missing studies in a batch output are logged, not merged (re-run that batch).
- `flag` corrections are applied and recorded in `notes` as
  `ai-revised:field=old->new` for the validation-phase reconciliation log.
- Leave fields empty rather than guessing; numeric accuracies as 0-1.
- 5 gold-standard pilots (S061, S089, S109, S046, S038) are already charted in
  `pilot-extractions/pilot-rows.jsonl` — do not re-extract them.
