# Thesis Format Pivot: Thesis-by-Publication → Monograph

**Date**: 2026-08-14
**Scope**: Thesis compilation format — 9-paper pipeline → 10-chapter monograph
**Status**: Decided and implemented

---

## Decision

The thesis compilation switches from **thesis-by-publication** (9 papers under
`thesis/papers/`, compiled as embedded papers) to a **monograph** (continuous
chapter-based prose, 10 chapters under `thesis/chapters/`).

## Rationale

1. **Institutional constraint (Universiti Malaya).** Per the P8 rules lookup
   (recorded in `thesis/chapters/02-agi-safety-landscape/research/submission/p8-um-thesis-rules.md`
   and `narrative.md`): the article-style / thesis-by-publication format is allowed
   only for Doctoral candidates and requires papers *published or accepted* in
   WoS-indexed journals at submission. Under-review and preprint-only papers do not
   count (FSKTM Guidelines §1.3). A monograph is the conventional fallback the
   project already identified, and it decouples thesis completion from journal
   acceptance entirely.
2. **Coherence.** A monograph is continuous prose: definitions serve both the
   compositional-generalisation and AI-safety communities, notation is shared, and
   the arc claim is argued once rather than repeated per paper. This directly
   addresses the fragmentation the scoping review itself documents.
3. **Publication independence.** No chapter's completion waits on journal acceptance;
   the JAIR desk-rejection of Paper 06 no longer threatens the thesis structure
   (see `10-jair-desk-rejection-response.md`).

## Strategy: monograph-first, papers as byproducts

| Decision | Choice |
|----------|--------|
| Primary artifact | The monograph (10 chapters) |
| Completed papers (01, 02, 06) | **Adapted** into chapters (Ch 2, 3, 7); venue manuscripts archived in `thesis/publications/` and listed in the front-matter LIST OF PUBLICATIONS |
| Pending papers (03–09) | Developed **as chapters first**; journal submission is an optional byproduct extracted at chapter Phase 12 (`12_paper_extraction.md`) |
| Phase docs | Repurposed per chapter (carried over from Papers 01/02 nearly unchanged; phase 12 re-framed from "submission" to "paper extraction") |

## Paper → Chapter Mapping

| Paper | Chapter | Status |
|:------|:--------|:-------|
| 01 Scoping Review | Ch 2 The Landscape of AGI Safety | 🟡 Adapted draft (2026-08-14) |
| 02 Systematic Review | Ch 3 Schema Coherence and the σ-Trap | 🟡 Pending adaptation (phases 0–9 done) |
| 03 Conceptual | Ch 4 The Σ-Align Framework | ⚪ Pending |
| 04 Pilot Study | Ch 5 σ-Coupling Interventions | ⚪ Pending |
| 05 Meta-Analysis | Ch 6 Quantifying the σ-Trap | ⚪ Pending |
| 06 Σ-Model | Ch 7 The Σ-Model | 🟢 Source complete; adaptation pending |
| 07 Empirical #2 | Ch 8 Mesa-Optimization (absorbs former Paper 08 scope) | ⚪ Pending |
| 08 (merged) | → Ch 8 | — |
| 09 Final Scoping | Ch 9 Implications | ⚪ Pending |
| — | Ch 1 Introduction, Ch 10 Conclusion | 🟢 Ch 1 drafted |

## Repository Changes

- `thesis/papers/` (9 folders) → removed
- `thesis/chapters/01-introduction/ … 10-conclusion/` (each: `README.md`, `phases/`, `manuscript/`, `figures/`)
- `thesis/publications/` — venue manuscripts (01, 02; 06 symlinked to root `paper/`)
- `thesis/monograph.tex` — main document (report, 12pt); build via `make monograph`
- `thesis/front-matter/`, `thesis/back-matter/` — title/abstract/acknowledgements/list-of-publications; glossary/notation/appendices
- Planning docs rewritten: `narrative.md`, `phase-roadmap.md`, `README.md`, `cross-cutting.md`, `metadata.yaml`
- `.gitignore` patterns updated (`thesis/papers/*` → `thesis/chapters/*`, `thesis/publications/*`)

## Reversibility

The pivot is reversible at low cost: `git mv` restores any chapter to a paper folder,
and the venue manuscripts were preserved verbatim in `thesis/publications/` (no source
content was deleted — all 479 previously tracked files are accounted for as renames).
The monograph does not preclude a later thesis-by-publication submission if the
candidature requirements change.
