# Σ-Align Monograph: Schema Coherence and the σ-Trap in AGI Safety

## Overarching Thesis

The thesis is structured as a **cumulative claim hierarchy** (three tiers), not a single
all-or-nothing identity claim. See `claim-evidence-ledger.md` for the C1–C10 claim matrix and
`Σ-Align/13-external-assessment-response.md` for the decisions behind this structure.

### Primary thesis

> **Schema coherence is a measurable property of learned representation structure whose deterioration can produce a stable low-coherence regime (the σ-trap) associated with systematic generalisation failure.**

### Secondary thesis (extension)

> **The same mechanism provides a testable account of some safety-relevant forms of objective divergence** — in particular where internal optimisation develops around representations that have become decoupled from the intended semantic structure.

### Long-term implication (bounded)

> **If these relationships persist in more capable systems, schema-coherent training may constitute a candidate component of alignment strategy.**

(Formerly stated as "compositional generalisation failure and AI alignment failure are the same
phenomenon — and solving one solves the other." That **identity** formulation is documented but
rejected as the working claim; the thesis claims the **unified-framework hypothesis** (σ as a
common structural variable) with the **mechanistic hypothesis** as the demonstrated core.
Every arrow in the CG → mesa-optimisation → alignment bridge carries an explicit evidential
status: literature-supported / observed / modelled / experimentally manipulated / inferred /
speculative.)

### Falsifiability criterion

The mechanism claim is falsified if σ is measured, interventions demonstrably raise σ, and the
predicted outcome (compositional generalisation, or safety-relevant divergence in the secondary
thesis) does **not** change — e.g. a low-σ regime with intact systematic generalisation, or a
mediation analysis in which raising σ leaves CG unchanged. The secondary thesis explicitly
allows some alignment failures to lie outside the framework.

> **Positioning note (2026-08):** Chapters 2–3 are *neutral mapping stages* and do not assert any
> tier of the claim. They use schema-coherence/σ-trap vocabulary strictly as a heuristic search
> and synthesis lens, state that lens explicitly, and report the evidence-base findings (including
> the limited explicit intersection between the CG and alignment literatures) without requiring
> the arc claims to hold. The claims are argued cumulatively from Chapter 4 onward. This
> separation is deliberate: it keeps the review chapters honest as scholarship, addresses the
> circular-reasoning concern that the mapping stages presuppose the thesis, and honours the
> discipline that a literature gap establishes *novelty, not truth*.

> **Format note (2026-08):** The thesis is written as a **monograph** (continuous, chapter-based prose), not a thesis-by-publication. Completed publications (Papers 01, 02, 06) are *adapted* into chapters, and their venue-formatted manuscripts are archived under `thesis/publications/` (they appear in the LIST OF PUBLICATIONS front matter). Pending publications are developed *as chapters first*; journal submission is an optional byproduct extracted from a completed chapter (see `phase-roadmap.md`).

---

## Monograph Arc

| Chapter | Source | Core Claim |
|:--------|:-------|:------------|
| **Ch 1:** Introduction | original | "There is an undiagnosed, potentially unifying failure mode in deep learning — the σ-trap — and this thesis makes it measurable, tests it, and examines its safety relevance." |
| **Ch 2:** The Landscape of AGI Safety | Paper 01 (Scoping Review) | "The AGI safety literature is fragmented; internal representation structure is treated operationally (15.5% of studies) rather than as an explicit safety property." |
| **Ch 3:** Schema Coherence and the σ-Trap | Paper 02 (Systematic Review) | "The evidence base is charted study-by-study (evidence table); it supports σ-trap as a researchable construct with testable consequences." |
| **Ch 4:** The Σ-Align Framework | Paper 03 (Conceptual) | "σ is operationally defined (construct, unit, metric, range, invariance) and passes construct-validity tests — the conceptual centre of the thesis." |
| **Ch 5:** σ-Coupling Interventions | Paper 04 (Pilot Study) | "Interventions raise σ, and raising σ changes compositional generalisation (mediation: intervention → σ → CG)." |
| **Ch 6:** Quantifying the σ-Trap | Paper 05 (Meta-Analysis) | "Within predefined effect families (A–E), the σ-adjacent evidence is consistent; construct heterogeneity is handled by design, not pooled away." |
| **Ch 7:** The Σ-Model | Paper 06 (Empirical #1) | "A minimal learning system can exhibit a transition from compositional to non-compositional learning predicted by an independently measurable σ — the flagship empirical chapter." |
| **Ch 8:** Schema Coherence and Safety-Relevant Optimisation | Paper 07 (Empirical #2, absorbs Paper 08) | "Low σ is linked, by explicit diagnostic criteria, to safety-relevant optimisation phenomena (proxy behaviour distinguished from mesa-optimisation)." |
| **Ch 9:** What Schema Coherence Can and Cannot Tell Us About Alignment | Paper 09 (Final Scoping) | "The evidence justifies a bounded, candidate-component role for schema-coherent training — limitations precede implications." |
| **Ch 10:** Conclusion | original | Synthesis, limitations, and the research programme forward. |

---

## Scope Convergence (2026-08, from external assessment)

The PhD's experimentally demonstrated core is **σ → compositional generalisation** (Ch 4–7).
**σ → safety-relevant optimisation** is the major extension (Ch 8). **σ → safe AGI** is a
carefully bounded implication, not a claim the thesis must establish (Ch 9). Claims C1–C10 are
tracked in `claim-evidence-ledger.md`; no claim may be cited as established before its
establishing chapter has produced the evidence.

---

## Dependency Graph

```
YEAR 1 (Months 1-12)          YEAR 2 (Months 13-24)       YEAR 3 (Months 25-36)
──────────────────────────────────────────────────────────────────────────────
TRACK A: Literature & Framework
┌──────────────────────┐      ┌──────────────────────┐
│ Ch 2. Landscape      │──────│ Ch 4. Σ-Align (σ    │
│ (Paper 01 — draft ✓) │      │  operationalisation) │
│ Months 1-6           │      │ Months 13-16         │
└──────────────────────┘      └──────────────────────┘
┌──────────────────────┐
│ Ch 3. σ-Trap evidence│
│ (Paper 02 + evidence │
│  table) Months 1-9   │
└──────────────────────┘

TRACK B: Empirical Core
                              ┌──────────────────────┐      ┌──────────────────────┐
                          │ Ch 5. Pilot Study      │──────│ Ch 8. Safety-relevant │
                          │ (mediation:            │      │ optimisation (mesa-opt │
                          │  interv → σ → CG)      │      │  criteria)             │
                          │ Months 13-18           │      │ Months 19-25         │
                          └──────────────────────┘      └──────────────────────┘
                                                                                │
┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
│ Ch 7. Σ-Model        │──────│ Ch 6. Meta-Analysis  │      │ Ch 9. What σ can/can't│
│ (flagship: transition│      │ (effect families     │      │ tell us about alignmt │
│  predicted by σ)     │      │  A–E sensitivities)  │      │ Months 26-32         │
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

**MVT (graduate-able core, per external assessment §18):**
*Must establish* — (1) σ operationalised; (2) σ construct validity; (3) low-σ regime
identifiable; (4) regime predicts CG failure; (5) intervention alters σ; (6) changing σ changes
the predicted outcome; (7) robustness to alternative explanations.
*Bonus* — (8) meta-analytic support; (9) replication across architectures/tasks; (10) low-σ →
safety-relevant optimisation.
*Long-term programme (not PhD-defining)* — corrigibility, CEV, indirect normativity, safe AGI,
optimality of schema-coherent training.

Chapter-wise: **core = Ch 2, 4, 5, 7**; **extension = Ch 3, 6, 8**; **synthesis = Ch 1, 9, 10**
(former Paper 08 scope folded into Ch 8).

- **If the Pilot (Ch 5 / Paper 04) yields null results:** the pre-registered analysis plan
  governs interpretation — a null result showing σ does *not* bridge to CG is still a publishable
  finding (falsification of the mechanism claim, per the falsifiability criterion) and Ch 8 pivots
  to a mechanism-contrast design. The monograph narrative is written to accommodate both outcomes.
- **If JAIR/TMLR rejects Paper 06 again (or revision stalls):** the monograph is unaffected — Ch 7
  is *adapted from* the manuscript but does not depend on its acceptance. The TMLR revision must
  address the desk-rejection grounds (exposition, overbroad claims, scope) and add non-toy
  validation evidence. Fallback venues: TMLR or ICLR workshop → main track.
- **If Paper 07 is rejected at a top-tier venue:** the TMLR fallback (guaranteed review) is
  already the default timeline path; Ch 8 stands regardless.
- **Monograph decoupling from publication status:** because the thesis is a monograph, no
  chapter's completion waits on journal acceptance. Under-review/preprint status of extracted
  papers never blocks thesis submission.
- **Universiti Malaya facts (2026-08, from the P8 rules lookup):** UM allows the
  thesis-by-publication / article-style format **only for Doctoral (PhD by Research) candidates**
  — not for Master's/undergraduate/foundation theses. The in-candidature route requires papers
  "published or accepted" in high-impact (WoS-indexed) journals; **under-review and preprint-only
  papers do NOT count** toward the thesis at submission (FSKTM Guidelines §1.3). The
  publication-in-fulfilment policy requires candidate first-authorship with supervisor
  co-authorship and UM affiliation — a solo-authored corpus conflicts with this unless a written
  faculty exclusion is granted, so **flag supervisor co-authorship early**. Practical consequence:
  the **monograph is the primary format** for the current pre-university phase; the 9-paper corpus
  becomes the underlying research programme executed during a future PhD-by-Research enrolment at
  UM (or comparable institution), with published papers appearing in the "LIST OF PUBLICATIONS"
  section, not as embedded chapters. The thesis compilation happens within candidature.

---

## Chapter-by-Chapter Plan

| Ch | Chapter | Source | Status | Phase Status |
|:--:|:--------|:-------|:-------|:-------------|
| 1 | **Introduction** | original | 🟡 Drafted (2026-08) | 🟢 phases 00–10 done |
| 2 | **The Landscape of AGI Safety** | Paper 01 (Scoping Review, revised draft) | 🟡 Adapting | 🟢 phases 00–11 done (as Paper 01) |
| 3 | **Schema Coherence and the σ-Trap** | Paper 02 (Systematic Review) | 🟡 Pending | 🟢 phases 00–09 done (as Paper 02); **evidence table pending** |
| 4 | **The Σ-Align Framework** | Paper 03 (Conceptual) | ⚪ Not started | ⚪ Pending Ch 2–3 adaptation; operational definition + validity tests |
| 5 | **σ-Coupling Interventions** | Paper 04 (Pilot Study) | ⚪ Not started | ⚪ Pending Ch 4; mediation design |
| 6 | **Quantifying the σ-Trap** | Paper 05 (Meta-Analysis) | ⚪ Not started | ⚪ Builds on Ch 3 evidence table; effect families A–E |
| 7 | **The Σ-Model** | Paper 06 (Empirical #1) | 🟢 Source complete | 🟢 manuscript done; JAIR desk-rejected 2026-07-15 → TMLR (add non-toy validation) |
| 8 | **Schema Coherence and Safety-Relevant Optimisation** | Paper 07 (Empirical #2, absorbs Paper 08 scope) | ⚪ Not started | ⚪ Pending Ch 5 results; mesa-opt diagnostic criteria |
| 9 | **What Schema Coherence Can and Cannot Tell Us About Alignment** | Paper 09 (Final Scoping) | ⚪ Not started | ⚪ Pending Ch 6–8 results; limitations-first |
| 10 | **Conclusion** | original | ⚪ Not started | ⚪ Months 33–36 |

---

## Key Milestones

| Milestone | Month | Deliverable |
|:----------|:------|:------------|
| M0 | 0 | Σ-Model manuscript complete (under JAIR review at the time; now pivoting to TMLR) ✓ |
| M1 | 6 | Ch 2 (Landscape) adapted from Scoping Review draft |
| M2 | 9 | Ch 3 (σ-Trap evidence) adapted + evidence table complete |
| M3 | 12 | Ch 7 (Σ-Model) adapted; TMLR decision on extracted Paper 06 |
| M4 | 16 | Ch 4 (σ operationalisation + validity tests) drafted |
| M5 | 18 | Ch 5 (Pilot, mediation design) drafted |
| M6 | 20 | Ch 6 (Meta-Analysis, effect families) drafted |
| M7 | 25 | Ch 8 (Safety-relevant optimisation) drafted |
| M8 | 30 | Ch 9 (Bounded implications) drafted |
| M9 | 32 | First full monograph draft compiled (Ch 1–10) |
| M10 | 36 | Monograph submitted per institution format |

---

## Monograph Structure (Document-Level)

```
thesis/
├── narrative.md              ← This file — overarching arc (three-tier claims)
├── claim-evidence-ledger.md  ← C1–C10 claim–evidence matrix (living document)
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

For chapters adapted from completed papers (Ch 2, 3, 7), phases 01–11 carry over from the
paper's phase docs nearly unchanged, since they document the research behind the chapter;
phase 12 is re-framed from "submission" to "paper extraction".

---

## Repository Layout

```
sigma-model/
├── paper/                    ← Σ-Model manuscript (Paper 06, JAIR → TMLR)
├── thesis/                   ← Monograph compilation & chapter folders
├── code/sigma_align/         ← Reusable ODE + config framework
├── Σ-Align/                  ← Decision documentation (MCDAs, audit trails, assessment responses)
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
