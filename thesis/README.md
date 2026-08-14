# Σ-Align Monograph

**Overarching thesis**: *Compositional generalization failure and AI alignment failure are the same phenomenon — a bifurcation in the agent's internal schema coherence (the σ-trap) — and solving one solves the other.*

This thesis is written as a **monograph**: continuous, chapter-based prose. Completed publications are adapted into chapters (their venue-formatted manuscripts live in `thesis/publications/`), and pending publications are developed as chapters first, with journal submission as an optional extracted byproduct.

## Chapters

| Ch | Chapter | Source | Status |
|:--:|:--------|:-------|:-------|
| 1 | Introduction | original | 🟢 Drafted (2026-08) |
| 2 | The Landscape of AGI Safety | Paper 01 (Scoping Review) | 🟡 Adapting |
| 3 | Schema Coherence and the σ-Trap | Paper 02 (Systematic Review) | 🟡 Pending |
| 4 | The Σ-Align Framework | Paper 03 (Conceptual) | ⚪ Pending |
| 5 | σ-Coupling Interventions | Paper 04 (Pilot Study) | ⚪ Pending |
| 6 | Quantifying the σ-Trap | Paper 05 (Meta-Analysis) | ⚪ Pending |
| 7 | The Σ-Model | Paper 06 (Empirical #1) | 🟢 Source complete |
| 8 | Mesa-Optimization via Schema Coherence | Paper 07 (Empirical #2, absorbs Paper 08) | ⚪ Pending |
| 9 | Implications: Schema-Coherent Training for Safe AGI | Paper 09 (Final Scoping) | ⚪ Pending |
| 10 | Conclusion | original | ⚪ Pending |

## Structure

```
thesis/
├── README.md              ← This file
├── narrative.md           ← Overarching monograph arc
├── phase-roadmap.md       ← Master roadmap & dependency graph (chapters)
├── cross-cutting.md       ← Monograph-level cross-cutting standards
├── metadata.yaml          ← Author info, ORCID
├── monograph.tex          ← Main LaTeX compilation (report, 12pt)
├── bibliography.bib       ← Shared bibliography
├── Makefile               ← latexmk build (`make pdf`)
├── chapters/              ← 10 chapter folders (README, phases/, manuscript/, figures/)
├── front-matter/          ← Title, abstract, acknowledgements, LIST OF PUBLICATIONS
├── back-matter/           ← Glossary, notation registry, appendices
└── publications/          ← Venue-formatted manuscripts (Papers 01, 02, 06)
```

## Chapter Phase Convention

Every chapter has a `phases/` directory following this convention:

| File | Phase | Purpose |
|:-----|:------|:--------|
| `00_cross_cutting.md` | Cross-cutting | Standards applied across all phases of this chapter |
| `00_repo.md` | 0 | Repository setup, tooling, LaTeX template |
| `00_5_research.md` | 0.5 | AI-assisted research phase (user-led) |
| `01_*.md` … `11_*.md` | 1–11 | Chapter-specific phases with exhaustive tasks |
| `12_paper_extraction.md` | 12 | Optional: extract a submission-ready paper from the chapter |
| `99_finale.md` | 99 | Unify chapter into monograph compilation |

Chapters adapted from completed papers (Ch 2, 3, 7) inherit the paper's phase docs — they document the research behind the chapter.

## Task Numbering

- **Phase**: `N` (e.g., Phase 3)
- **Task**: `N.M` (e.g., `3.2` = Phase 3, Task 2)
- **Subtask**: `N.M.P` (e.g., `3.2.1`)
- Checkbox convention: `[x]` = done, `[ ]` = pending

See [`narrative.md`](narrative.md) for the full monograph arc.
See [`phase-roadmap.md`](phase-roadmap.md) for the chapter pipeline and milestones.
See [`cross-cutting.md`](cross-cutting.md) for monograph-level standards.
