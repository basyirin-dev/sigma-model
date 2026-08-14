# Paper 02 — Phase 7.1 Pilot Extraction Report

**Status:** Complete (2026)
**Extractor:** Pilot pass (read from `research/full-text-txt/` directly)
**Task:** 7.1.3 — pilot extraction on 5 papers to verify template coverage; 7.1.4 — refine template based on pilot
**CC:** CC.1.5 (data extraction form developed, piloted, iterated)

---

## 1. Pilot Selection (stratified)

| Study | ID | Paper | Stratum |
|---|---|---|---|
| S089 | P02_0622 | Keysers et al. 2019/2020 — CFQ (ICLR 2020) | SCAN/CFQ-class compositional |
| S109 | P02_0643 | Ruis et al. 2020 — gSCAN (NeurIPS 2020) | SCAN/CFQ-class compositional (grounded/multimodal) |
| S061 | P02_0594 | Kim & Linzen 2020 — COGS (EMNLP 2020) | Compositional benchmark (semantic parsing) |
| S046 | P02_0386 | Qiu et al. 2026 — E2A/SAM (WWW 2026) | σ-coupled intervention (sharpness-aware) |
| S038 | P02_0151 | Addepalli et al. 2024 — VL2V-ADiP (CVPR 2024) | Vision OOD / domain generalization |

Selection covers: 3 compositional benchmarks, 1 vision domain-shift empirical paper, 1 σ-coupled
intervention paper. Also spans 3 `pub_type` values (dataset_benchmark ×3, empirical ×2), multiple
architectures (LSTM/Transformer/ViT/GNN), and 4 `ood_split_type` values.

Pilot rows are stored at `pilot-extractions/pilot-rows.jsonl` in the exact AI-output contract format
(one record per study; `sub_experiments[]` per template §3), so the pilot doubles as the contract
exemplar for the AI pass and as 5 of the 286 final records.

## 2. Coverage Findings

The 80-field template (sections 1A–1Q + §3 sub-experiment form) **covered all information present**
in the 5 pilot papers. No missing fields required adding a new code to the schema. Findings:

1. **`peer_reviewed` prefill needs full-text confirmation.** S061 (COGS, EMNLP 2020), S089 (CFQ,
   ICLR 2020), S109 (gSCAN, NeurIPS 2020) are coded arXiv-only in `included-studies.csv`
   (source_db = arXiv:benchmark), but all three are peer-reviewed conference papers per their
   full texts. The extraction rule: `peer_reviewed` = TRUE if full text shows a published venue,
   regardless of the library record's source_db. This is an **extraction guidance** note, not a
   schema change (the field and its vocabulary suffice).
2. **`id_acc_n_seeds` vs `n_seeds_value`**: both are needed. `n_seeds_value` (15d) records the
   stated number of runs; `id_acc_n_seeds`/`ood_acc_n_seeds` (9c/10c) record seeds actually
   reported for the metric. Papers sometimes report one without the other (e.g., S038 fixed-seed
   results with 3 re-runs only for a subset). Guidance: record both when distinct.
3. **CI vs SD reporting**: papers differ (S089 reports 95% CI ±; S109/S061 report SD ±). Schema
   has both CI fields (9e/9f) and SD fields (9b/10b); guidance: fill what the paper reports, put
   the other in `notes` with the ± interpretation. No schema change needed.
4. **σ-coupled detection (S046)**: E2A is SAM-inspired (sharpness/flatness via loss landscape)
   but is not a listed SAM-family subtype. `train_regime = sigma_coupled`,
   `train_regime_sigma = other_sigma` with `train_data_note`/`notes` describing the mechanism —
   template handles it via the existing vocabulary (V07 satisfied).
5. **Non-accuracy metrics (S046 ROC-AUC, S109 exact match)**: `metric_type = accuracy` with
   `metric_other`/`ood_metric_other` capturing the specific metric; S109 uses "accuracy" with
   `id_metric_other = "exact match accuracy"`. The metric-type vocabulary needs no extension.
6. **Long-format viability**: multi-split (S109: 9 rows), multi-arch (S089: 3 archs × 2 tasks),
   multi-intervention-vs-baseline (S046: E2A intervention) all map cleanly onto
   `sub_exp_id` + `split_id`/`arch_id`/`intervention_id` (Tasks 7.2.4–7.2.6). Phase 9's
   meta-analysis will consume the per-sub-experiment ID/OOD means, SDs, and n.

## 3. Schema/Template Changes from Pilot (7.1.4)

Schema already final per `charted-schema.yaml` v1.0; pilot found **no missing fields**, so no field
additions were required. Two clarifications were folded into the schema's field descriptions
(no version bump needed — descriptions only):

- `peer_reviewed`: "TRUE if venue is peer-reviewed (derived from venue/source_db)" → guidance
  documented here: confirm from full text when source_db is arXiv.
- `id_metric_type`/`ood_metric_type`: vocabulary unchanged; `metric_other` captures exact-match,
  ROC-AUC, etc.

`research/extraction-template.md` status updated Draft → **Finalized** with this changelog entry
(see template §0 header).

## 4. Phase Doc Checkboxes (Task 7.1)

- [x] 7.1.1: template reviewed and iterated based on full-text experience (5 pilot papers)
- [x] 7.1.2: extraction fields finalized (schema YAML + this report)
- [x] 7.1.3: pilot extraction on 5 papers completed
- [x] 7.1.4: template refined (no new fields needed; clarifications recorded)
- [x] 7.1.5: CC.1.5 satisfied (form developed, piloted, iterated)
