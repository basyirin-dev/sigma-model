# Paper 02: Schema Coherence and the σ-Trap — A Systematic Review

**Status**: 🟡 Phase 00 complete — ready for Phase 0.5 (AI-Assisted Research)
**Type**: Systematic Review with Meta-Analysis (conditional)
**Target Venue**: *Artificial Intelligence Review* (Springer) or *JAIR*
**PROSPERO ID**: [Pending registration — Phase 1]
**OSF Project**: [Pending registration — Phase 1]
**Timeline**: Months 1–9 (2026-07-03 → 2027-03-12)

## Research Question (PICO)

**Primary**: In neural network models trained via gradient-based optimization, what is the effect of σ-targeting training interventions on OOD generalization performance compared to standard SGD?

**Secondary 1**: What empirical evidence exists for the σ-trap (stable low-σ_A equilibrium) across benchmarks and architectures?
**Secondary 2**: What proxy measures of schema coherence have been validated, and how do they correlate with OOD performance?
**Secondary 3**: What is the relationship between σ-trap failure and alignment failure modes (mesa-optimization, deceptive alignment)?

## Phase Overview

| Phase | Name | Deadline | Status |
|:------|:-----|:---------|:-------|
| 00_cross_cutting | Cross-Cutting Concerns | 2027-03-12 | 🟡 Ongoing |
| 00_repo | Repo & LaTeX Setup | 2026-07-10 | 🟡 Pending |
| 00_5 | AI-Assisted Research | 2026-07-24 | 🟡 Pending |
| 01 | Research Question & Protocol | 2026-07-31 | 🟡 Pending |
| 02 | Search Strategy Design | 2026-08-07 | 🟡 Pending |
| 03 | Database Search Execution | 2026-08-14 | 🟡 Pending |
| 04 | Deduplication & Reference Management | 2026-08-21 | 🟡 Pending |
| 05 | Title & Abstract Screening | 2026-09-11 | 🟡 Pending |
| 06 | Full-Text Retrieval & Review | 2026-09-25 | 🟡 Pending |
| 07 | Data Extraction & Charting | 2026-10-16 | 🟡 Pending |
| 08 | Quality Assessment | 2026-11-06 | 🟡 Pending |
| 09 | Thematic Synthesis & Meta-Analysis | 2026-12-04 | 🟡 Pending |
| 10 | First Draft | 2027-01-08 | 🟡 Pending |
| 11 | Revision & Polishing | 2027-02-05 | 🟡 Pending |
| 12 | Submission Preparation | 2027-03-05 | 🟡 Pending |
| 99 | Finale — Thesis Unification | 2027-03-12 | 🟡 Pending |

## Paper Dependencies

- **Depends on**: Paper 01 (Scoping Review) — specifically Phase 0.5 outputs (landscape boundary, schema coherence mapping, gap analysis)
- **Provides foundation for**: Paper 03 (Conceptual Paper — Σ-Align framework), Paper 07 (Empirical #2 — Mesa-optimization), Paper 09 (Final Scoping Review)

## Methodology

- **Review type**: Systematic review with meta-analysis (conditional on sufficient comparable studies)
- **Reporting guideline**: PRISMA 2020 (27-item checklist)
- **Protocol registration**: PROSPERO and OSF
- **Screening**: Dual independent screening (two reviewers) with Cohen's κ ≥ 0.80
- **Risk of bias**: Custom tool adapted from QUADAS-2 / PROBAST (5 domains, 26 signalling questions)
- **Synthesis**: Thematic narrative synthesis + random-effects meta-analysis (if ≥5 comparable studies)
- **Confidence assessment**: GRADE

## Key Differences from Paper 01 (Scoping Review)

| Dimension | Paper 01 (Scoping) | Paper 02 (Systematic) |
|-----------|:------------------:|:---------------------:|
| Review type | Scoping (PRISMA-ScR) | Systematic (PRISMA 2020) |
| Question framework | PCC | PICO |
| Registration | OSF | PROSPERO + OSF |
| Screening | AI-assisted acceptable | Dual independent mandatory |
| Risk of bias | Optional | Mandatory (5-domain tool) |
| Meta-analysis | Not applicable | Planned (conditional) |
| Focus | Broad AGI safety landscape | Narrow σ-trap evidence |
| Timeline | 6 months | 9 months |

See `phases/` for detailed phase-by-phase task breakdowns.
See `research/` for Phase 0.5 AI-assisted research artifacts (to be created).
