# Validation-sample IRR report — Paper 01 Phase 8 (Task 8.2.5)

- Sample: **254** papers (fixed seed, Counter({'full-text': 129, 'abstract': 80, 'metadata': 45})); pilot overlaps excluded (P003, P1036) -> **252** scored.
- Rater 1: external-AI raw scores (ai-output/batch-*.jsonl).
- Rater 2: rater2-validation.jsonl.
- Kappa: Cohen's unweighted, per dimension, null-pairs excluded.
- ICC(2,1): two-way random, single measures, absolute agreement, on the D6-renormalized composite.

## Per-dimension inter-rater agreement

| Dim | n pairs | exact match | kappa | >=1pt gaps |
|-----|--------:|------------:|------:|-----------:|
| D2 | 250 | 96% | 0.924 | 11 |
| D3 | 252 | 87% | 0.627 | 33 |
| D4 | 80 | 90% | 0.649 | 8 |
| D5 | 207 | 100% | 0.954 | 1 |
| D7 | 252 | 100% | 1.000 | 0 |
| D8 | 208 | 98% | 0.967 | 4 |

## Composite ICC

- Composite ICC(2,1) over 252 papers (D6-renormalized): **0.947**

## Reconciliation queue (57 gaps >= 1pt)

| paper_id | dim | rater1 | rater2 |
|----------|-----|-------:|-------:|
| P007 | D3 | 3 | 2 |
| P044 | D4 | 1 | 2 |
| P1001 | D2 | 1 | 2 |
| P1001 | D3 | 1 | 2 |
| P1014 | D2 | 2 | 3 |
| P1014 | D3 | 1 | 2 |
| P1039 | D3 | 1 | 2 |
| P1047 | D3 | 1 | 2 |
| P105 | D4 | 2 | 1 |
| P1055 | D3 | 1 | 2 |
| P1061 | D3 | 1 | 2 |
| P1067 | D2 | 3 | 4 |
| P1067 | D3 | 1 | 2 |
| P1068 | D3 | 1 | 2 |
| P1070 | D3 | 1 | 2 |
| P1089 | D3 | 1 | 2 |
| P1091 | D3 | 1 | 2 |
| P1092 | D3 | 1 | 2 |
| P1103 | D3 | 1 | 2 |
| P1112 | D3 | 1 | 2 |
| P1122 | D3 | 1 | 2 |
| P1134 | D3 | 1 | 2 |
| P1144 | D3 | 1 | 2 |
| P1154 | D3 | 1 | 2 |
| P1165 | D3 | 1 | 2 |
| P1195 | D3 | 1 | 2 |
| P1203 | D3 | 3 | 2 |
| P1243 | D2 | 1 | 2 |
| P220 | D4 | 2 | 1 |
| P264 | D4 | 2 | 1 |
| P275 | D2 | 1 | 3 |
| P300 | D4 | 2 | 1 |
| P366 | D2 | 2 | 4 |
| P439 | D4 | 1 | 2 |
| P509 | D3 | 3 | 1 |
| P509 | D8 | 3 | 1 |
| P516 | D2 | 1 | 3 |
| P547 | D8 | 3 | 4 |
| P626 | D3 | 1 | 2 |
| P630 | D5 | 3 | 2 |
| P630 | D8 | 4 | 1 |
| P649 | D3 | 3 | 2 |
| P702 | D4 | 2 | 3 |
| P726 | D4 | 2 | 1 |
| P799 | D3 | 3 | 2 |
| P846 | D2 | 1 | 3 |
| P856 | D2 | 3 | 4 |
| P882 | D8 | 1 | 2 |
| P883 | D2 | 2 | 3 |
| P977 | D3 | 1 | 2 |
| P978 | D3 | 1 | 2 |
| P983 | D3 | 1 | 2 |
| P985 | D2 | 1 | 2 |
| P985 | D3 | 1 | 2 |
| P986 | D3 | 1 | 2 |
| P991 | D3 | 1 | 2 |
| P994 | D3 | 1 | 2 |
