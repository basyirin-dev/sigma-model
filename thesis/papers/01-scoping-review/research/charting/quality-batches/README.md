# External-AI quality-scoring batches — Paper 01 Phase 8

1258 papers split into 10 JSONL batches
(default full run: 1268 papers across 5 batches;
--pilot: the pilot papers in 1 batch; --exclude-pilot: drop the already-scored
pilot papers from the full run).

## How to run (user)

1. Open each `batch-NN.jsonl` in your AI tool (paste file content as one prompt).
2. Ask the model to return **one JSON object per line** for every paper_id,
   using exactly the output contract in the prompt file header.
3. Save responses as `ai-output/batch-NN.jsonl`.
4. Run `python3 merge_quality_ai.py` to validate + merge into `quality-scores.csv`.

## Output contract (field names must match exactly)

```
{"paper_id": "P002",
  "D2": 0-4|null, "D3": 0-4|null, "D4": 0-4|null (empirical only),
  "D5": 0-4|null, "D7": 0-4|null, "D8": 0-4|null,
  "justifications": {"D2": "...", ...}}
```

- Scores are integers 0-4; null = evidence insufficient (keeps existing/blank).
- D1 (venue) and D6 (citations) are scripted — do NOT return them.
- Pilot papers are scored identically; their scores feed 8.1.5 dual-scorer IRR.
