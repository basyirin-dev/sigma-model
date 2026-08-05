# Screening Decision Framework

**Task:** 1.8 Study Selection (PRISMA 2020 Items 8-9)
**Date:** 2026-07-08
**Stage:** Framework ready; awaiting full search results from all databases

---

## 1. Stage 1: Title and Abstract Screening

### Decision Options
| Code | Decision | Meaning |
|------|----------|---------|
| **INC** | Include | Clearly meets all inclusion criteria |
| **EXC** | Exclude | Clearly fails ≥1 inclusion criterion |
| **UNC** | Uncertain | Cannot decide from title/abstract alone; proceed to full-text |

### Exclusion Reasons (for EXC)
| Code | Reason | Criterion violated |
|------|--------|--------------------|
| **E1** | No empirical evaluation | Study design (theoretical only, no experiments) |
| **E2** | No neural network model | Population (symbolic/statistical only) |
| **E3** | No OOD/compositional split | Outcome (no ID-OOD comparison) |
| **E4** | OOD detection (not OOD gen.) | Study design (detecting novelty per input, not measuring compositional gen.) |
| **E5** | Pre-2017 | Timing |
| **E6** | Non-English | Timing/setting |
| **E7** | Unsupervised/RL only | Population (secondary stream only) |
| **E8** | Non-compositional OOD | Study design (simple covariate shift without compositional structure) |
| **E9** | Survey/review/position paper | Study design (excluded; used as contextual reference) |
| **E10** | Neural closure model (PDE) | Study design ("compositional" ≠ linguistic compositionality) |

### Screening Protocol
- Two independent reviewers (simulated by single reviewer with re-screen after 24h)
- Pilot calibration: 50 titles to ensure ≥80% agreement
- Conflicts: discuss → third reviewer if unresolved
- Blinding: reviewers NOT blinded to authors/institutions/journals

### Order of Record Processing
1. Remove duplicates (Zotero dedup)
2. Sort by database source (to track per-database yield)
3. Randomize order within each database batch

---

## 2. Stage 2: Full-Text Screening

### Decision Options
| Code | Decision | Meaning |
|------|----------|---------|
| **FINC** | Final include | All criteria met |
| **FEXC** | Final exclude | ≥1 criterion fails after full-text review |

### Exclusion Reasons (full-text)
Codes per `phases/06_full_text.md` Task 6.2.4 (authoritative for Phase 6):
| Code | Reason | Details |
|------|--------|---------|
| **FT1** | No OOD/compositional split reported | Intervention/Comparison: benchmark lacks held-out OOD/compositional split |
| **FT2** | Only ID results reported | Outcome: no OOD condition at all |
| **FT3** | Insufficient quantitative detail | Outcome: no accuracy numbers, no extractable data |
| **FT4** | Not actually about neural network models | Population: screening error |
| **FT5** | Full text unavailable | Practical: not retrievable after 3 attempts (task 6.1.4) |
| **FT6** | Duplicate content | Superseded by later publication |
| **FT7** | Review or opinion paper without original results | Study design |
| **FT8** | Other (specify) | — |

### Full-Text Retrieval Priority
1. DOI → CrossRef/Unpaywall/OpenAlex OA
2. arXiv PDF
3. Author's institutional repository
4. Email corresponding author (one attempt) / ResearchGate request
   → 3 distinct attempts (task 6.1.4), then code `Unavailable` + reason

---

## 3. Pilot Screening (arXiv Results Only)

Since full database results are pending, a pilot screening of arXiv results is planned:

| Batch | Source | Records | Current status |
|-------|--------|---------|----------------|
| A | arXiv primary | 50 | Raw results saved; screening pending |
| B | arXiv secondary | 50 | Raw results saved; screening pending |
| C | arXiv benchmark | 50 | Raw results saved; screening pending |
| D | arXiv safety | 50 | Raw results saved; screening pending |
| E | OpenAlex | 20 | Raw results saved; screening pending |

### Pilot Screening Protocol
1. Review 20 records from Batch A (simulated)
2. Calculate inter-reviewer agreement
3. If <80%, clarify ambiguous criteria and repeat
4. Screen remaining batches
5. Document screening decisions in `screening-log.md`

---

## 4. Pre-Registration of Extraction

All studies that pass full-text screening will be registered in an extraction database before extraction begins (to prevent selective reporting). Registration fields:

- Unique study ID
- Full bibliographic reference
- DOI / arXiv ID
- Screening decision (by whom, date)
- Screening notes
