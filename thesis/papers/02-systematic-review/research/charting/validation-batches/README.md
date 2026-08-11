# Second-extractor validation batch — Paper 02 Phase 7 (Task 7.3)

57 sample studies for independent second extraction (CC.1.6).

1. Open `batch-01.jsonl` in your AI tool (split in half if the context window
   is limited — outputs are merged by study_id).
2. Ask the model to return one JSON object per line for every study_id, using
   exactly the `contract` fields. The model must code INDEPENDENTLY (it should
   not see extractor-1 answers — they are not in the batch file).
3. Save the response as `ai-output/batch-01.jsonl`.
4. Run `python3 validate.py` to compute Cohen's kappa / ICC(2,1).
5. Run `python3 reconciliation.py` to log and resolve disagreements.

Contract: identical to the main extraction pass (see `ai-prompt-batches/README.md`).
