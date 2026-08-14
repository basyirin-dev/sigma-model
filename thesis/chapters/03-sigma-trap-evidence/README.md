# Chapter 3: Schema Coherence and the σ-Trap

**Source**: Paper 02 — *Schema Coherence and the σ-Trap* (Systematic Review; phases 0–9 done)
**Status**: 🟡 Pending — source phases 0–9 complete; begin chapter adaptation after Ch 2
**Venue manuscript**: `thesis/publications/02-systematic-review/` (submission-format artifact)
**Timeline**: Months 1–9 (2026-07-03 → 2027-03-12)

This chapter adapts the Paper 02 systematic review into monograph prose. It is a *neutral mapping stage*: it reports the σ-trap evidence base (including the limited explicit intersection between the compositional-generalization and alignment literatures) without requiring the arc claim to hold.

## Research Question (PICO)

**Primary**: In neural network models trained via gradient-based optimization, what is the effect of σ-targeting training interventions on compositional out-of-distribution generalization performance compared to standard SGD?

**Secondary 1**: What empirical evidence exists for the σ-trap (stable low-σ_A equilibrium) across benchmarks and architectures?
**Secondary 2**: What proxy measures of schema coherence have been validated, and how do they correlate with OOD performance?
**Secondary 3** [Exploratory — Discussion only]: What is the relationship between σ-trap failure and alignment failure modes (mesa-optimization, deceptive alignment)?

## Phase Overview

| Phase | Name | Deadline | Status |
|:------|:-----|:---------|:-------|
| 00_cross_cutting | Cross-Cutting Concerns | 2027-03-12 | 🟡 Ongoing |
| 00_repo | Repo & LaTeX Setup | 2026-07-10 | ✅ Complete |
| 00_5 | AI-Assisted Research | 2026-07-24 | ✅ Complete |
| 01 | Research Question & Protocol | 2026-07-31 | ✅ Complete |
| 02 | Search Strategy Design | 2026-08-07 | ✅ Complete |
| 03 | Database Search Execution | 2026-08-14 | ✅ Complete |
| 04 | Deduplication & Reference Management | 2026-08-21 | ✅ Complete |
| 05 | Title & Abstract Screening | 2026-09-11 | ✅ Complete |
| 06 | Full-Text Retrieval & Review | 2026-09-25 | ✅ Complete |
| 07 | Data Extraction & Charting | 2026-10-16 | ✅ Complete |
| 08 | Quality Assessment | 2026-11-06 | ✅ Complete |
| 09 | Thematic Synthesis & Meta-Analysis | 2026-12-04 | ✅ Complete |
| 10 | First Draft | 2027-01-08 | 🟡 Pending |
| 11 | Revision & Polishing | 2027-02-05 | 🟡 Pending |
| 12 | Paper Extraction (optional) | 2027-03-05 | 🟡 Pending |
| 99 | Finale — Monograph Unification | 2027-03-12 | 🟡 Pending |

## Chapter Dependencies

- **Depends on**: Ch 2 (Landscape) — specifically Phase 0.5 outputs (landscape boundary, schema coherence mapping, gap analysis)
- **Provides foundation for**: Ch 4 (Σ-Align Framework), Ch 6 (Meta-Analysis), Ch 8 (Safety-relevant optimisation), Ch 9 (Bounded implications)

## Evidence Table (required before Ch 6 relies on this chapter)

Per external assessment (FastTrack F2): the systematic review must produce a complete
**study-level evidence table** — not just narrative summaries — containing at minimum:

| Study | Construct | Operationalisation | Design | N | Outcome | Effect | Variance | Quality | σ relevance |
|-------|-----------|--------------------|--------|---|---------|--------|----------|---------|-------------|

Tracked as a Phase 9/10 task in `phases/`; the effect-size pools for Ch 6 are drawn from this
table, and every effect entering Ch 6 must be auditable back to it.

## Methodology

- **Review type**: Systematic review with meta-analysis (conditional on sufficient comparable studies)
- **Reporting guideline**: PRISMA 2020 (27-item checklist)
- **Protocol registration**: OSF m3asw (2026-07-08); PROSPERO not eligible (non-medical review)
- **Screening**: Dual independent screening (two reviewers) with Cohen's κ ≥ 0.80
- **Risk of bias**: Custom tool adapted from QUADAS-2 / PROBAST (5 domains, 26 signalling questions)
- **Synthesis**: Thematic narrative synthesis + random-effects meta-analysis (if ≥5 comparable studies)
- **Confidence assessment**: GRADE

## Key Differences from Ch 2 (Scoping Review)

| Dimension | Ch 2 (Scoping) | Ch 3 (Systematic) |
|-----------|:------------------:|:---------------------:|
| Review type | Scoping (PRISMA-ScR) | Systematic (PRISMA 2020) |
| Question framework | PCC | PICO |
| Registration | OSF | OSF (PROSPERO ineligible) |
| Screening | AI-assisted acceptable | Dual independent mandatory |
| Risk of bias | Optional | Mandatory (5-domain tool) |
| Meta-analysis | Not applicable | Planned (conditional) |
| Focus | Broad AGI safety landscape | Narrow σ-trap evidence |
| Timeline | 6 months | 9 months |

## Goal-Misgeneralization Reconciliation (assessment B5)

Ch 2's charted records lacked "goal misgeneralization" as an explicit concept. This chapter's
discussion (and Ch 8) must reconcile it with the σ-trap: is goal misgeneralization another
expression of a low-σ regime (objective decoupled from intended semantics), and why did the
keyword mapping miss it? A dedicated theoretical reconciliation is a tracked task.
