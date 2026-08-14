# Paper 02 — Screening Summary Report (Task 5.6)

**Date**: 2026-08-01

## PRISMA 2020 Flow Numbers

| Stage | Records |
|-------|--------:|
| Records identified (databases, pre-dedup) | ~2,807 |
| Records after deduplication (screened) | **1,435** |
| — Excluded at title screening | 842 |
| — Uncertain at title (→ abstract) | 577 |
| — Included at title | 16 |
| Abstract screening (title Include+Uncertain) | 593 |
| — Excluded at abstract screening | 198 (net) |
| — Included after abstract screening | 179 |
| — Uncertain after abstract screening | 216 |
| **Proceeding to full-text assessment (Phase 6)** | **395** |

## Exclusion Reason Breakdown

| Code | Count | Criterion |
|------|------:|-----------|
| E2 | 1007 | Not about OOD / compositional generalization |
| E6 | 17 | Outside date range (2017-2026) |
| E5 | 14 | Not in English |
| E1 | 2 | Not about neural network models |
| **Total excluded** | **1040** | |

## Included Pool

- Included: **179**
- Uncertain (full-text review): **216**
- Total for Phase 6: **395**

## Validation (CC.1.6)

- Dual independent AI screening (S1 + S2) on all 1,435 records
- Title-stage binary κ = 0.738; abstract-stage binary κ = 0.725
- κ < 0.80 → criteria retrained (CG lexicon tightened, non-compositional override); remaining disagreements resolved to full-text review per protocol 5.5.3

## Notes

- 179 Includes + 216 Uncertain = 395 records proceed to Phase 6 full-text retrieval
- The ~953 supplementary records (OpenAlex + citation chaining) remain in the academic-research-mcp review library (server unavailable); documented limitation
