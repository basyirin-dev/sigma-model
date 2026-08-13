# Σ-Align Thesis: Schema Coherence and the σ-Trap in AGI Safety

## Overarching Thesis

**Compositional generalization failure and AI alignment failure are the same phenomenon — a bifurcation in the agent's internal schema coherence (the σ-trap) — and solving one solves the other.**

> **Positioning note (2026-08):** Papers 01–02 are *neutral mapping stages* and do not assert this claim. They use schema-coherence/σ-trap vocabulary strictly as a heuristic search and synthesis lens, state that lens explicitly, and report the evidence-base findings (including the limited explicit intersection between the CG and alignment literatures) without requiring the arc claim to hold. The claim itself is argued from Paper 03 onward. This separation is deliberate: it keeps the reviews submission-ready as standalone contributions and addresses the circular-reasoning concern that the mapping stages presuppose the thesis.

---

## Thesis Arc

| Chapter | Papers | Core Claim |
|:--------|:-------|:------------|
| **Ch 1–2:** Diagnosis | 01. Scoping Review, 02. Systematic Review | "There is an undiagnosed failure mode in deep learning — the σ-trap." |
| **Ch 3:** Framework | 03. Conceptual Paper | "We can measure and intervene on the σ-trap through schema coherence." |
| **Ch 4:** Evidence | 04. Pilot Study, 05. Meta-Analysis, 06. Empirical #1, 07. Empirical #2, 08. Empirical #3 | "The σ-trap is robust (meta), real (Sigma-Model), and safety-relevant (mesa-opt)." |
| **Ch 5:** Implications | 09. Final Scoping Review | "Schema-coherent training is the optimal path to safe, long-term AGI — directly relevant to CEV and Indirect Normativity." |

---

## Dependency Graph

```
YEAR 1 (Months 1-12)          YEAR 2 (Months 13-24)       YEAR 3 (Months 25-36)
──────────────────────────────────────────────────────────────────────────────
TRACK A: Literature & Framework
┌──────────────────────┐      ┌──────────────────────┐
│ 01. Scoping Review   │──────│ 03. Conceptual Paper │
│ (AGI Safety landscape)│     │ (Σ-Align framework)  │
│ Months 1-6           │      │ Months 13-16         │
└──────────────────────┘      └──────────────────────┘
┌──────────────────────┐
│ 02. Systematic Review│
│ (σ-trap evidence)    │
│ Months 1-9           │
└──────────────────────┘

TRACK B: Empirical Core
                              ┌──────────────────────┐      ┌──────────────────────┐
                          │ 04. Pilot Study        │──────│ 07. Empirical #2     │
                          │ (σ-coupling experiments)│      │ (Mesa-opt detection) │
                          │ Months 13-18           │      │ Months 19-25         │
                          └──────────────────────┘      └──────────────────────┘
                                                                                │
┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
│ 06. Empirical #1     │──────│ 05. Meta-Analysis    │      │ 08. Empirical #3    │
│ (Σ-Model — DONE ✓)  │      │ (Quantify σ-trap)    │      │ (TBD)               │
│ Already under review │      │ Months 12-20         │      │ Months 22-30        │
└──────────────────────┘      └──────────────────────┘      └──────────────────────┘
                                                                                │
TRACK C: Synthesis                                                            │
                                                                                ↓
                              ┌──────────────────────────────────────────────────────┐
                              │ 09. Final Scoping Review                             │
                              │ (Implications for Long-Term Agency & CEV)            │
                              │ Months 26-32                                          │
                              └──────────────────────────────────────────────────────┘
```

---

## Minimum Viable Thesis & Contingency (2026-08)

**MVT (graduate-able core): Papers 1, 3, 4, 6** — a Scoping Review, a Conceptual Framework, an Empirical Paper, and a Pilot Study. Papers 2, 5, 7, 9 are stretch goals; 8 is merged into 7.

- **If the Pilot (04) yields null results:** the pre-registered analysis plan governs interpretation — a null result showing schema coherence does *not* bridge the domains is still a publishable finding (falsification of the mechanism claim) and Paper 07 pivots to a mechanism-contrast design. The thesis narrative is written to accommodate both outcomes (see the positioning note above: the mapping stages do not require the arc claim).
- **If JAIR rejects Paper 06 again (or revision stalls):** fallback venues are *TMLR* (fast, certified review) or *ICLR* workshop → main track; the MVT core is unaffected because Paper 06 can be replaced by Paper 04 + Paper 07 as the empirical evidence.
- **If Paper 07 is rejected at a top-tier venue:** the TMLR fallback (guaranteed review) is already the default timeline path; no milestone re-planning needed.
- **Thesis submission decoupling:** confirm with the university that "under review" or preprint status suffices for thesis submission at Month 36; do not wait for final acceptance of Papers 7/9.
- **Universiti Malaya facts (2026-08, from the P8 rules lookup):** UM allows the thesis-by-publication / article-style format **only for Doctoral (PhD by Research) candidates** — not for Master's/undergraduate/foundation theses. The in-candidature route requires papers "published or accepted" in high-impact (WoS-indexed) journals; **under-review and preprint-only papers do NOT count** toward the thesis at submission (FSKTM Guidelines §1.3). The publication-in-fulfilment policy requires candidate first-authorship with supervisor co-authorship and UM affiliation — a solo-authored corpus conflicts with this unless a written faculty exclusion is granted, so **flag supervisor co-authorship early**. Practical consequence: the 9-paper arc is executed during a future PhD-by-Research enrolment at UM (or comparable institution); the current pre-university phase builds the paper pipeline, and the thesis compilation happens within candidature. The conventional monograph format remains the fallback (published papers appear in the "LIST OF PUBLICATIONS" section, not as embedded chapters).

---

## Paper-by-Paper Plan

| # | Paper | Type | Venue Target | Timeline | Status |
|:--|:------|:-----|:-------------|:---------|:-------|
| 1 | **Landscape of AGI Safety** | Scoping Review | *ACM Computing Surveys* or pre-print | M1–6 | 🟡 Pending |
| 2 | **Schema Coherence and the σ-Trap** | Systematic Review | *Artificial Intelligence Review* | M1–9 | 🟡 Pending |
| 3 | **The Σ-Align Framework** | Conceptual Paper | *Journal of AI Research* or *Synthese* | M13–16 | 🟡 Pending |
| 4 | **σ-Coupling Interventions** | Pilot Study | *NeurIPS* workshop → *TMLR* | M13–18 | 🟡 Pending |
| 5 | **Quantifying the σ-Trap** | Evidence Synthesis (meta-analysis of the existing σ-trap-adjacent literature, pooling Paper 02 Phase 9 effect sizes) | *TMLR* or *ACM/IMS TDS* (not psych/methods journals) | M12–20 | 🟡 Pending |
| 6 | **Σ-Model: Compositional Generalisation Failure** | Empirical | *JAIR* (desk-rejected 2026-07-15; revision) | **DONE** | 🟠 Revising |
| 7 | **Mesa-Optimization via Schema Coherence** | Empirical (absorbs the former Paper 08 scope) | *TMLR* or *ICLR/NeurIPS* main track | M19–25 | 🟡 Pending |
| 8 | ~~TBD~~ merged into Paper 07 | — | — | — | ⚪ Merged 2026-08 |
| 9 | **Schema-Coherent Training for Safe AGI** | Final Scoping | *arXiv* → thesis compilation | M26–32 | 🟡 Pending |

---

## Key Milestones

| Milestone | Month | Deliverable |
|:----------|:------|:------------|
| M0 | 0 | Sigma-Model paper under JAIR review ✓ |
| M1 | 6 | Scoping Review #1 submitted |
| M2 | 9 | Systematic Review submitted |
| M3 | 12 | Sigma-Model paper decision (hopefully accepted) |
| M4 | 16 | Conceptual Paper submitted |
| M5 | 18 | Pilot Study submitted |
| M6 | 20 | Meta-Analysis submitted |
| M7 | 25 | Empirical #2 submitted |
| M8 | 30 | Empirical #3 submitted |
| M9 | 32 | Final Scoping Review submitted |
| M10 | 36 | Thesis compiled and published |

---

## Thesis Structure (Document-Level)

```
thesis/
├── narrative.md              ← This file — overarching arc
├── phase-roadmap.md          ← Master roadmap & dependency graph
├── cross-cutting.md          ← Thesis-level cross-cutting standards
├── metadata.yaml             ← Author info, ORCID, degrees, institution
├── compilation.tex           ← LaTeX compilation of all papers
│
├── papers/
│   ├── 01-scoping-review/    ← Scoping Review of AGI Safety landscape
│   │   ├── README.md         ← Paper overview & phase table
│   │   ├── phases/           ← 14 phase documents (Phase 0–99)
│   │   │   ├── 00_cross_cutting.md
│   │   │   ├── 00_repo.md
│   │   │   ├── 00_5_research.md  ← AI-assisted research prompts
│   │   │   ├── 01_*.md → 12_*.md
│   │   │   └── 99_finale.md
│   │   └── research/         ← Phase 0.5 research artifacts
│   ├── 02-systematic-review/ ← Systematic Review of σ-trap evidence
│   ├── 03-conceptual-paper/  ← Σ-Align Framework
│   ├── 04-pilot-study/       ← σ-coupling experiments
│   ├── 05-meta-analysis/     ← Quantifying the σ-trap
│   ├── 06-empirical-1-sigma-model/ ← Sigma-Model (under JAIR review)
│   │   └── manuscript/ → ../../paper/  (symlink)
│   ├── 07-empirical-2/       ← Mesa-optimization detection
│   ├── 08-empirical-3/       ← TBD (placeholder)
│   └── 09-final-scoping-review/ ← Implications & CEV
```

## Phase Convention

Every paper follows this phase structure (see `README.md` for full details):

| Phase | Purpose |
|:------|:--------|
| 00_cross_cutting | Paper-level cross-cutting standards |
| 00_repo | Repository setup, LaTeX template, tooling |
| 00_5_research | AI-assisted research phase (user-led) |
| 01–10+ | Paper-specific phases with exhaustive tasks |
| 99_finale | Unify into thesis compilation |

---

## Repository Layout

```
sigma-model/
├── paper/                    ← Sigma-Model manuscript (Empirical #1)
├── thesis/                   ← Thesis compilation & paper folders
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
