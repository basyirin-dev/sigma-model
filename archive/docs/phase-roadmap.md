# Σ-Model on Natural Data: Protein Domain Compositional Generalisation — Phase Roadmap

**Target**: NeurIPS 2027 (primary) / ICML 2027 (stretch)
**Paper**: "The Sigma Model on Natural Data: Compositional Generalisation Failure in Protein Domain Architectures"
**Repo**: Single monorepo at `code/sigma/proteins/` — protein work is an application of the Σ-Model framework, not a separate project.
**License**: MIT (inherited from sigma-model)
**Status**: Planning — Jun 2026

---

## High-Level Phase Map

| Phase | Name | Deadline | Dependencies | Critical Path |
|-------|------|----------|--------------|---------------|
| **00** | Cross-Cutting Concerns | Ongoing | None | Yes |
| **00_repo** | Repo & Tooling Infrastructure | 5 Jul 2026 | None | Yes |
| **00_5** | Research Preparation | 12 Jul 2026 | None | Yes (user-led) |
| **01** | Pfam Data Pipeline | 2 Aug 2026 | 00_repo, 00_5 | Yes |
| **02** | Custom Protein Language Model | 23 Aug 2026 | 01 | Yes |
| **03** | Brittle Domain N=500 Experiment | 13 Dec 2026 | 02 | Yes |
| **04** | Statistical Analysis & H1 Testing | 10 Jan 2027 | 03 | Yes (ICML deadline) |
| **05** | Grammar Induction Probe Tasks | 10 Jan 2027 | 02 (parallel with 03) | Yes (ICML deadline) |
| **06** | ESM-2 Scale-Up Validation | 7 Mar 2027 | 04, 05 | No (NeurIPS only) |
| **07** | PfamCG-1.0 Benchmark | 25 Jul 2027 | 01, 04 | No (NeurIPS only) |
| **08** | Paper Writing & Figure Generation | 2 May 2027 | 04, 05, 06 | Yes |
| **09** | Submission, Rebuttal & Release | 1 Aug 2027 | 08 | Yes |

---

## Dependency Graph

```
00 (cross-cutting) ─────────────────────────────────────────────────► all phases
00_repo ──────────────────────────► 01 ──► 02 ──► 03 ──► 04 ──┐
                                                        │       │
00_5 (user-led research) ───► 01                        │       │
                                     02 ──► 05 ──────────┤       │
                                                              │       │
                                                              └───► 08 ──► 09
                                                                        │
                                                                  06 ───┘
                                                                        │
                                                                  07 ───┘
```

**Key dependencies:**
- ICML 2027 (Jan 2027 deadline): Phases 00–05 must complete by Jan 2027
- NeurIPS 2027 (May 2027 deadline): Phases 00–09 must complete by May 2027
- ICML is a stretch goal; if Phase 04/05 analysis is not solid by Jan, let it pass and go all-in on NeurIPS

---

## Phase Status

| Phase | Status |
|-------|--------|
| 00 | Pending |
| 00_repo | Pending |
| 00_5 | Pending (user-led) |
| 01 | Pending |
| 02 | Pending |
| 03 | Pending |
| 04 | Pending |
| 05 | Pending |
| 06 | Pending |
| 07 | Pending |
| 08 | Pending |
| 09 | Pending |

---

## Key Milestones

| Date | Milestone | Phase Dependency |
|------|-----------|-----------------|
| 28 Jun 2026 | Phase roadmap approved | — |
| 5 Jul 2026 | Repo infrastructure ready | 00_repo |
| 12 Jul 2026 | Research prep complete (user-led) | 00_5 |
| 2 Aug 2026 | Pfam data pipeline complete | 01 |
| 23 Aug 2026 | Custom PLM implemented and tested | 02 |
| 13 Dec 2026 | N=500 Brittle Domain complete | 03 |
| 10 Jan 2027 | Statistical analysis (H1) complete; ICML go/no-go | 04, 05 |
| 7 Mar 2027 | ESM-2 validation complete | 06 |
| 2 May 2027 | First paper draft | 08 |
| May 2027 | NeurIPS submission | 09 |
| 25 Jul 2027 | PfamCG-1.0 benchmark release | 07 |
| 1 Aug 2027 | Rebuttal & release | 09 |

---

## Cross-References

- [Cross-Cutting Concerns](phases/00_cross_cutting.md)
- [Repo Infrastructure](phases/00_repo.md)
- [Research Preparation](phases/00_5_research_prep.md)
- [Data Pipeline](phases/01_data_pipeline.md)
- [Protein Language Model](phases/02_protein_lm.md)
- [Brittle Domain Experiment](phases/03_brittle_domain.md)
- [Statistical Analysis](phases/04_statistical_analysis.md)
- [Grammar Induction](phases/05_grammar_induction.md)
- [ESM-2 Validation](phases/06_esm2_validation.md)
- [PfamCG-1.0 Benchmark](phases/07_pfamcg_benchmark.md)
- [Paper Writing](phases/08_paper_writing.md)
- [Submission & Release](phases/09_submission.md)

---

## Risks

See [docs/risks/](risks/) for full risk register.
