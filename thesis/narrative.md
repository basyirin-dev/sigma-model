# Σ-Align Monograph: Schema Coherence and the σ-Trap in AGI Safety

## Overarching Thesis

**Compositional generalization failure and AI alignment failure are the same phenomenon — a bifurcation in the agent's internal schema coherence (the σ-trap) — and solving one solves the other.**

> **Positioning note (2026-08):** Chapters 2–3 are *neutral mapping stages* and do not assert this claim. They use schema-coherence/σ-trap vocabulary strictly as a heuristic search and synthesis lens, state that lens explicitly, and report the evidence-base findings (including the limited explicit intersection between the CG and alignment literatures) without requiring the arc claim to hold. The claim itself is argued from Chapter 4 onward. This separation is deliberate: it keeps the review chapters honest as scholarship and addresses the circular-reasoning concern that the mapping stages presuppose the thesis.

> **Format note (2026-08):** The thesis is written as a **monograph** (continuous, chapter-based prose), not a thesis-by-publication. Completed publications (Papers 01, 02, 06) are *adapted* into chapters, and their venue-formatted manuscripts are archived under `thesis/publications/` (they appear in the LIST OF PUBLICATIONS front matter). Pending publications are developed *as chapters first*; journal submission is an optional byproduct extracted from a completed chapter (see `phase-roadmap.md`).

---

## Monograph Arc

| Chapter | Source | Core Claim |
|:--------|:-------|:------------|
| **Ch 1:** Introduction | original | "There is an undiagnosed failure mode in deep learning — the σ-trap — and this thesis shows it is the same phenomenon as alignment failure." |
| **Ch 2:** The Landscape of AGI Safety | Paper 01 (Scoping Review) | "The AGI safety literature is fragmented; no existing framework treats internal schema coherence as the central failure mode." |
| **Ch 3:** Schema Coherence and the σ-Trap | Paper 02 (Systematic Review) | "The evidence base supports σ-trap as a measurable construct with real consequences." |
| **Ch 4:** The Σ-Align Framework | Paper 03 (Conceptual) | "We can measure and intervene on the σ-trap through schema coherence." |
| **Ch 5:** σ-Coupling Interventions | Paper 04 (Pilot Study) | "Schema-coherence interventions are feasible and their effects are estimable." |
| **Ch 6:** Quantifying the σ-Trap | Paper 05 (Meta-Analysis) | "The σ-trap is robust across the literature." |
| **Ch 7:** The Σ-Model: Compositional Generalisation Failure | Paper 06 (Empirical #1) | "Compositional generalisation failure is a bifurcation in schema coherence — the σ-trap is real in a minimal mechanistic model." |
| **Ch 8:** Mesa-Optimization via Schema Coherence | Paper 07 (Empirical #2, absorbs Paper 08) | "The σ-trap is safety-relevant: mesa-optimization arises as a schema-coherence phenomenon." |
| **Ch 9:** Implications: Schema-Coherent Training for Safe AGI | Paper 09 (Final Scoping) | "Schema-coherent training is the optimal path to safe, long-term AGI — directly relevant to CEV and Indirect Normativity." |
| **Ch 10:** Conclusion | original | Synthesis, limitations, and the research programme forward. |

---

## Dependency Graph

```
YEAR 1 (Months 1-12)          YEAR 2 (Months 13-24)       YEAR 3 (Months 25-36)
──────────────────────────────────────────────────────────────────────────────
TRACK A: Literature & Framework
┌──────────────────────┐      ┌──────────────────────┐
│ Ch 2. Landscape      │──────│ Ch 4. Σ-Align        │
│ (Paper 01 — draft ✓) │      │ (Paper 03)           │
│ Months 1-6           │      │ Months 13-16         │
└──────────────────────┘      └──────────────────────┘
┌──────────────────────┐
│ Ch 3. σ-Trap evidence│
│ (Paper 02)           │
│ Months 1-9           │
└──────────────────────┘

TRACK B: Empirical Core
                              ┌──────────────────────┐      ┌──────────────────────┐
                          │ Ch 5. Pilot Study      │──────│ Ch 8. Mesa-Opt.      │
                          │ (Paper 04)             │      │ (Paper 07)           │
                          │ Months 13-18           │      │ Months 19-25         │
                          └──────────────────────┘      └──────────────────────┘
                                                                                │
┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
│ Ch 7. Σ-Model        │──────│ Ch 6. Meta-Analysis  │      │ Ch 9. Implications   │
│ (Paper 06 — done ✓)  │      │ (Paper 05)           │      │ (Paper 09)           │
│ Already written      │      │ Months 12-20         │      │ Months 26-32         │
└──────────────────────┘      └──────────────────────┘      └──────────────────────┘
                                                                                │
TRACK C: Synthesis                                                            │
                                                                                ↓
                              ┌──────────────────────────────────────────────────────┐
                              │ Ch 1 + Ch 10: Introduction & Conclusion              │
                              │ Ch 1 drafted 2026-08; Ch 10 at Months 33-36          │
                              └──────────────────────────────────────────────────────┘
```

---

## Minimum Viable Thesis & Contingency (2026-08)

**MVT (graduate-able core): Chapters 2, 4, 5, 7** — Landscape, Framework, Pilot, Σ-Model. Chapters 3, 6, 8, 9 are stretch goals; former Paper 08 scope is folded into Chapter 8.

- **If the Pilot (Ch 5 / Paper 04) yields null results:** the pre-registered analysis plan governs interpretation — a null result showing schema coherence does *not* bridge the domains is still a publishable finding (falsification of the mechanism claim) and Ch 8 pivots to a mechanism-contrast design. The monograph narrative is written to accommodate both outcomes (see the positioning note above: the mapping stages do not require the arc claim).
- **If JAIR/TMLR rejects Paper 06 again (or revision stalls):** the monograph is unaffected — Ch 7 is *adapted from* the manuscript but does not depend on its acceptance. Fallback venues for the extracted publication remain *TMLR* (fast, certified review) or *ICLR* workshop → main track.
- **If Paper 07 is rejected at a top-tier venue:** the TMLR fallback (guaranteed review) is already the default timeline path; Ch 8 stands regardless.
- **Monograph decoupling from publication status:** because the thesis is a monograph, no chapter's completion waits on journal acceptance. Under-review/preprint status of extracted papers never blocks thesis submission.
- **Universiti Malaya facts (2026-08, from the P8 rules lookup):** UM allows the thesis-by-publication / article-style format **only for Doctoral (PhD by Research) candidates** — not for Master's/undergraduate/foundation theses. The in-candidature route requires papers "published or accepted" in high-impact (WoS-indexed) journals; **under-review and preprint-only papers do NOT count** toward the thesis at submission (FSKTM Guidelines §1.3). The publication-in-fulfilment policy requires candidate first-authorship with supervisor co-authorship and UM affiliation — a solo-authored corpus conflicts with this unless a written faculty exclusion is granted, so **flag supervisor co-authorship early**. Practical consequence: the **monograph is the primary format** for the current pre-university phase; the 9-paper corpus becomes the underlying research programme executed during a future PhD-by-Research enrolment at UM (or comparable institution), with published papers appearing in the "LIST OF PUBLICATIONS" section, not as embedded chapters. The thesis compilation happens within candidature.

---

## Chapter-by-Chapter Plan

| Ch | Chapter | Source | Status | Phase Status |
|:--:|:--------|:-------|:-------|:-------------|
| 1 | **Introduction** | original | 🟡 Drafted (2026-08) | 🟢 phases 00–10 done |
| 2 | **The Landscape of AGI Safety** | Paper 01 (Scoping Review, revised draft) | 🟡 Adapting | 🟢 phases 00–11 done (as Paper 01) |
| 3 | **Schema Coherence and the σ-Trap** | Paper 02 (Systematic Review) | 🟡 Pending | 🟢 phases 00–09 done (as Paper 02) |
| 4 | **The Σ-Align Framework** | Paper 03 (Conceptual) | ⚪ Not started | ⚪ Pending Ch 2–3 adaptation |
| 5 | **σ-Coupling Interventions** | Paper 04 (Pilot Study) | ⚪ Not started | ⚪ Pending Ch 4 |
| 6 | **Quantifying the σ-Trap** | Paper 05 (Meta-Analysis) | ⚪ Not started | ⚪ Builds on Ch 3 effect-size pools (k≈27–31) |
| 7 | **The Σ-Model** | Paper 06 (Empirical #1) | 🟢 Source complete | 🟢 manuscript done; JAIR desk-rejected 2026-07-15, pivoting to TMLR |
| 8 | **Mesa-Optimization via Schema Coherence** | Paper 07 (Empirical #2, absorbs Paper 08 scope) | ⚪ Not started | ⚪ Pending Ch 5 results |
| 9 | **Implications: Schema-Coherent Training for Safe AGI** | Paper 09 (Final Scoping) | ⚪ Not started | ⚪ Pending Ch 6–8 results |
| 10 | **Conclusion** | original | ⚪ Not started | ⚪ Months 33–36 |

---

## Key Milestones

| Milestone | Month | Deliverable |
|:----------|:------|:------------|
| M0 | 0 | Σ-Model manuscript complete (under JAIR review at the time; now pivoting to TMLR) ✓ |
| M1 | 6 | Ch 2 (Landscape) adapted from Scoping Review draft |
| M2 | 9 | Ch 3 (σ-Trap evidence) adapted from Systematic Review |
| M3 | 12 | Ch 7 (Σ-Model) adapted; TMLR decision on extracted Paper 06 |
| M4 | 16 | Ch 4 (Σ-Align Framework) drafted |
| M5 | 18 | Ch 5 (Pilot Study) drafted |
| M6 | 20 | Ch 6 (Meta-Analysis) drafted |
| M7 | 25 | Ch 8 (Mesa-Optimization) drafted |
| M8 | 30 | Ch 9 (Implications) drafted |
| M9 | 32 | First full monograph draft compiled (Ch 1–10) |
| M10 | 36 | Monograph submitted per institution format |

---

## Monograph Structure (Document-Level)

```
thesis/
├── narrative.md              ← This file — overarching arc
├── phase-roadmap.md          ← Master roadmap & dependency graph (chapters)
├── cross-cutting.md          ← Monograph-level cross-cutting standards
├── metadata.yaml             ← Author info, ORCID, degrees, institution
├── monograph.tex             ← Main LaTeX compilation (report, 12pt)
├── bibliography.bib          ← Shared bibliography
├── Makefile                  ← latexmk build (`make pdf`)
│
├── chapters/                 ← The monograph itself
│   ├── 01-introduction/      ← Ch 1 (drafted 2026-08)
│   │   ├── README.md         ← Chapter overview & phase table
│   │   ├── phases/           ← Chapter phase roadmaps
│   │   ├── manuscript/       ← Chapter .tex source
│   │   └── figures/
│   ├── 02-agi-safety-landscape/   ← Ch 2 (adapts Paper 01)
│   ├── 03-sigma-trap-evidence/    ← Ch 3 (adapts Paper 02)
│   ├── 04-sigma-align-framework/  ← Ch 4 (Paper 03)
│   ├── 05-pilot-study/            ← Ch 5 (Paper 04)
│   ├── 06-meta-analysis/          ← Ch 6 (Paper 05)
│   ├── 07-sigma-model/            ← Ch 7 (Paper 06)
│   ├── 08-mesa-optimization/      ← Ch 8 (Paper 07)
│   ├── 09-implications/           ← Ch 9 (Paper 09)
│   └── 10-conclusion/             ← Ch 10
│
├── front-matter/             ← Title, abstract, acknowledgements, LIST OF PUBLICATIONS
├── back-matter/              ← Glossary, notation registry, appendices
└── publications/             ← Venue-formatted manuscripts (standalone artifacts)
    ├── 01-scoping-review/    ← Paper 01 manuscript (ACM Computing Surveys format)
    ├── 02-systematic-review/ ← Paper 02 manuscript (Springer sn-jnl format)
    └── 06-sigma-model/       ← Paper 06 → symlink to ../../paper/ (JAIR/TMLR)
```

## Chapter Phase Convention

Every chapter follows this phase structure (see `README.md` for full details):

| Phase | Purpose |
|:------|:--------|
| 00_cross_cutting | Chapter-level cross-cutting standards |
| 00_repo | Repository setup, LaTeX template, tooling |
| 00_5_research | AI-assisted research phase (user-led) |
| 01–11 | Chapter-specific phases (research, drafting, revision) |
| 12_paper_extraction | Optional: extract a submission-ready paper from the chapter |
| 99_finale | Unify into monograph compilation |

For chapters adapted from completed papers (Ch 2, 3, 7), phases 01–11 carry over from the paper's phase docs nearly unchanged, since they document the research behind the chapter; phase 12 is re-framed from "submission" to "paper extraction".

---

## Repository Layout

```
sigma-model/
├── paper/                    ← Σ-Model manuscript (Paper 06, JAIR → TMLR)
├── thesis/                   ← Monograph compilation & chapter folders
├── code/sigma_align/         ← Reusable ODE + config framework
├── Σ-Align/                  ← Decision documentation (MCDAs, audit trails)
├── docs/adrs/                ← Architecture Decision Records
├── archive/                  ← Protein-domain artifacts (read-only)
├── hbar_env/                 ← Python virtual environment
├── AGENTS.md                 ← Agent instructions
├── opencode.json             ← Opencode configuration
├── pyproject.toml            ← Package config
├── requirements*.txt         ← Dependencies
├── README.md                 ← Project overview
├── LICENSE                   ← MIT
└── .gitignore
```
