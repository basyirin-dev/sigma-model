# Paper 01 — Screening Calibration Report (Task 5.1)

**Date**: 2026-08-01
**Sample**: seeded random 50 of 2867 records (seed=20260801)
**Screeners**: deterministic classifier (machine) vs PI manual review (human)

## Agreement

- Exact agreement (3-way): **31/50 (62%)**
- Cohen's kappa (3-way): **0.41**
- Hard-decision agreement (Include vs Exclude, Uncertain deferred): **27/27 (100%)**

## Disagreement Analysis

| Type | Count | Examples | Resolution |
|------|------:|----------|------------|
| Include vs Exclude (true FP) | 0 | — | Rule refinements below |
| Exclude vs Include (true FN) | 0 | — | — |
| Include/Exclude vs Uncertain (deferred) | 19 | value-alignment papers → abstract screening | Abstract stage (5.3) decides |

## Criteria Refinements Applied During Calibration

1. **Precision gate**: added CORE_INDICATORS — records need ≥1 high-precision AGI-safety indicator (not just a subdomain vocabulary hit) to be Included.
2. **Word-boundary anchoring**: 'corrigib' no longer matches 'incorrigibility' (juvenile-law term); added explicit 'incorrigib' pattern.
3. **Ambiguous-vs-unambiguous split**: 'value alignment', 'ai alignment', 'misalignment', 'corrigib', 'interpretability', 'reward model', 'rlhf' treated as ambiguous — require AI context; ambiguous-only evidence → Uncertain (abstract screening), not Include.
4. **Narrow-domain exclusion**: business/HR/psych/medical/legal markers ('employee', 'leadership', 'CSR', 'juvenile', 'court', …) with only ambiguous evidence → Exclude.
5. **AI context word-boundary**: bare 'ai'/'ml'/'gpt' now word-boundary matched ('sustainability' no longer triggers AI context).
6. **Proceedings-volume exclusion**: records that are collections ('proceedings contain') without an individual-study abstract → Exclude.
7. **'AI safety' synonym**: added 'ai safety'/'long-term ai safety' to the AGI Safety subdomain vocabulary (recall fix).

## Remaining Known Limitations

- **Polysemy**: 'corrigibility' appears in linguistics (hypothesis correction) and juvenile law; such records are now routed to Uncertain/Exclude via context rules.
- **HCI boundary**: 'human-AI alignment' / 'XAI' papers (Editable XAI, transparency studies) are routed to Uncertain; abstract stage determines structural-AGI-safety relevance.
- **Abstract-less records**: 746 records lack abstracts; title-only decisions fall back to title+keywords evidence.

## Next Step

Title screening complete: Include 631, Uncertain 919, Exclude 1317. Include+Uncertain (1550 records) proceed to abstract screening (Task 5.3).
