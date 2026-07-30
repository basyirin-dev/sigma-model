# Citation Chaining Log — Paper 01 (Scoping Review)

## Method

- **Tool**: Semantic Scholar API via snowball_search (academic research MCP)
- **Direction**: Both forward and backward simultaneously
- **Date executed**: 2026-07-30
- **Review ID**: 041e97f2-702e-45db-8c0d-bc69e0e4801a

## Seeds Used

### Run 1: 7 seeds (arXiv IDs)
| # | Paper | arXiv ID | Year |
|:--|:------|:----------|:-----|
| 1 | Hubinger et al. — Risks from Learned Optimization | 1906.01820 | 2019 |
| 2 | Amodei et al. — Concrete Problems in AI Safety | 1606.06565 | 2016 |
| 3 | Elhage et al. — Toy Models of Superposition | 2209.10652 | 2022 |
| 4 | Ngo et al. — Alignment Problem from DL Perspective | 2209.00626 | 2022 |
| 5 | Langosco et al. — Goal Misgeneralization in DRL | 2105.14111 | 2022 |
| 6 | Christiano et al. — Deep RL from Human Preferences | 1706.03741 | 2017 |
| 7 | Hubinger et al. — Sleeper Agents | 2401.05566 | 2024 |
| **Total harvested**: 1,056 (944 new, 107 within-snowball duplicates, 5 against-review duplicates) |

### Run 2: 3 seeds (arXiv IDs)
| # | Paper | arXiv ID | Year |
|:--|:------|:----------|:-----|
| 1 | Greenblatt et al. — Alignment Faking in LLMs | 2412.14093 | 2024 |
| 2 | Ji et al. — AI Alignment: A Comprehensive Survey | 2310.19852 | 2023 |
| 3 | Hadshar — Review of Evidence for Existential Risk | 2310.18244 | 2023 |
| **Total harvested**: 275 (194 new, 6 within-snowball duplicates, 75 against-review duplicates) |

## Seeds Not Accessible via API

These papers exist on non-API sources (LessWrong, MIRI, etc.) and need manual citation extraction:

| Paper | Reason | Recommended Manual Action |
|:------|:-------|:------------------------|
| Yudkowsky (2004) — CEV | LessWrong post, no DOI/arXiv ID | Manually extract references from the online post |
| Soares et al. (2015) — Corrigibility | MIRI technical report | Check Semantic Scholar via browser for citation graph |
| Hadfield-Menell et al. (2016) — CIRL | Published in PMLR; not found via API | Manually check references |
| Carlsmith (2023) — Existential Risk | Online essay | Manually extract references |
| Pepin Lehalleur et al. (2025) — Schemas | In-progress thesis preprint | Manually check when published |
| Wang & Murfet (2026) — SLT | In-progress thesis preprint | Manually check when published |

## Combined Results

| Metric | Value |
|:-------|:------|
| **Total seeds with API access** | 10 (of 15) |
| **Total new candidates from chaining** | 1,138 |
| **Total unique papers in review pool** | 1,353 |
| **DOIs exported** | 642 |
| **Non-DOI papers** | ~558 (arXiv-only + grey literature) |
