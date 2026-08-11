# Paper 02 — Phase 7 Charting Pipeline (run instructions)

Everything needed to complete data extraction & charting, built per
`phases/07_data_extraction.md`. **Task 7.1 (schema + pilot) is DONE.**
Tasks 7.2–7.5 are ready to run — the only thing that needs your hands is
the external-AI extraction pass.

## Status

| Task | State |
|---|---|
| 7.1 Schema finalized + pilot (5 papers) | ✅ done (`pilot-report.md`, `pilot-extractions/pilot-rows.jsonl`) |
| 7.2 Full extraction | ⏳ pipeline ready; **you run the AI pass** (below) |
| 7.3 Validation (20% sample, κ/ICC) | ⏳ sample + extractor2 batch ready; **you run the EX2 AI pass** |
| 7.4 Data quality | ⏳ `quality.py` ready (V01–V20, missingness, ranges) |
| 7.5 Export + summary + figures | ⏳ `export.py` / `summary.py` ready (pilots: 7 figures) |

## Your two AI passes

### Pass 1 — full extraction (Task 7.2)

1. Open `ai-prompt-batches/batch-01.jsonl` … `batch-10.jsonl` (281 studies;
   pilots S038/S046/S061/S089/S109 excluded — already charted as gold).
   If a batch is too large for your tool's context window, split it
   (`split -n l/2 batch-01.jsonl`) — output merges by `study_id`.
2. Ask the model to return **one JSON object per line** for every `study_id`,
   using exactly the `contract` fields in each prompt file (field names must
   match exactly; accuracies as proportions 0–1; leave unverifiable fields
   empty — never guess; `flag` for categorical corrections).
3. Save each response as `ai-prompt-batches/ai-output/batch-NN.jsonl`
   (one JSON object per line).
4. Run `python3 merge_ai.py` → merges into `research/charted-data.csv`
   (long format) + `research/charted-data-main.csv` + `merge-report.md`.

### Pass 2 — validation sample (Task 7.3)

1. Open `validation-batches/batch-01.jsonl` (57 studies = 20% sample,
   seed 20261016). Same contract. **Independent coding**: the model must
   extract from the full-text excerpt alone, not match extractor 1.
2. Save response as `validation-batches/ai-output/batch-01.jsonl`.
3. `python3 validate.py` → Cohen's κ per categorical field + ICC(2,1) per
   continuous field, vs exit targets κ ≥ 0.80 / ICC ≥ 0.90.
4. `python3 reconciliation.py` → `reconciliation-items.md`; resolve
   unresolved items (senior review) and refine schema/template if a field
   is systematically disputed (≥25%).

## After both passes (Tasks 7.4–7.5)

```
python3 quality.py        # missingness, inconsistent coding, ranges, V01–V20
python3 export.py         # research/charted-data.json (nested, CC.4.3)
python3 summary.py        # summary-statistics.md + figures/
```

Then tick the phase-doc checkboxes (7.2.1–7.5.5), satisfy CC.1.5/CC.1.6/
CC.4.3/CC.5.3, and commit with the exit-criteria summary.

## Pipeline files

| File | Role |
|---|---|
| `charted-schema.yaml` | finalized 80+-field schema, vocabularies, V01–V20 (config, ADR 0004) |
| `prefill.py` → `prefill.json` | bibliographic + Phase 6.5.1 hints for S001–S286 |
| `prompts.py` | generates the 10 main AI batches (results-aware excerpts) |
| `merge_ai.py` | validates + merges AI output → long-format CSVs |
| `sample.py` | seeded 20% validation sample (57 studies) |
| `extractor2.py` | generates the independent second-extractor batch |
| `validate.py` | Cohen's κ + ICC(2,1), exit thresholds |
| `reconciliation.py` | itemized disagreements + systematic-flag detection |
| `quality.py` | missingness / normalization / ranges / V01–V20 |
| `export.py` | charted-data.json (nested study → sub_experiments) |
| `summary.py` | summary-statistics.md + figures/ |

Generated/regenerable files (batches, AI output) are gitignored (CC.5.2).
