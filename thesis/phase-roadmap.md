# Σ-Align Monograph: Chapter Roadmap

> **Format (2026-08):** The thesis is a **monograph**. This roadmap tracks *chapters*, not papers. Each chapter has a `phases/` directory; completed publications are adapted into chapters and their manuscripts live under `thesis/publications/`. Journal submission is an optional byproduct extracted from a completed chapter (Phase 12 — paper extraction).

## Chapter Pipeline

```
YEAR 1 (Months 1-12)          YEAR 2 (Months 13-24)       YEAR 3 (Months 25-36)
──────────────────────────────────────────────────────────────────────────────
TRACK A: Literature & Framework
┌──────────────────────┐      ┌──────────────────────┐
│ Ch 2. Landscape      │──────│ Ch 4. Σ-Align        │
│ 🟡 Adaptation (src ✓)│      │ ⚪ Pending           │
└──────────────────────┘      └──────────────────────┘
┌──────────────────────┐
│ Ch 3. σ-Trap evidence│
│ 🟡 Adaptation (src ✓)│
└──────────────────────┘

TRACK B: Empirical Core
                              ┌──────────────────────┐      ┌──────────────────────┐
                          │ Ch 5. Pilot Study      │──────│ Ch 8. Mesa-Opt.      │
                          │ ⚪ Pending             │      │ ⚪ Pending           │
                          └──────────────────────┘      └──────────────────────┘
                                                                                │
┌──────────────────────┐      ┌──────────────────────┐      ┌──────────────────────┐
│ Ch 7. Σ-Model        │──────│ Ch 6. Meta-Analysis  │      │ Ch 9. Implications   │
│ 🟢 Source complete   │      │ ⚪ Pending           │      │ ⚪ Pending           │
└──────────────────────┘      └──────────────────────┘      └──────────────────────┘
                                                                                │
TRACK C: Synthesis                                                            │
                                                                                ↓
                              ┌──────────────────────────────────────────────────────┐
                              │ Ch 1 Introduction 🟢 drafted · Ch 10 Conclusion ⚪    │
                              └──────────────────────────────────────────────────────┘
```

## Chapter Status Overview

| Ch | Chapter | Source | Phases Status | Phase Docs | Next Action |
|:--:|:--------|:-------|:--------------|:-----------|:------------|
| 1 | Introduction | original | 🟢 Phases 00–10 done | ✅ `phases/` created | Adapt Ch 2 |
| 2 | Landscape of AGI Safety | Paper 01 (Scoping Review) | 🟡 Adapting — source phases 0–11 done (revised draft) | ✅ carried over from Paper 01 | Adapt manuscript to monograph prose |
| 3 | Schema Coherence and the σ-Trap | Paper 02 (Systematic Review) | 🟡 Pending — source phases 0–9 done | ✅ carried over from Paper 02 | Begin chapter adaptation after Ch 2 |
| 4 | The Σ-Align Framework | Paper 03 (Conceptual) | ⚪ Not started | — | Wait for Ch 2–3 adaptation |
| 5 | σ-Coupling Interventions | Paper 04 (Pilot Study) | ⚪ Not started | — | Wait for Ch 4 |
| 6 | Quantifying the σ-Trap | Paper 05 (Meta-Analysis) | ⚪ Not started | — | Build on Ch 3 Phase 9 effect-size pools (k≈27–31) |
| 7 | The Σ-Model | Paper 06 (Empirical #1) | 🟢 Source complete | — | Adapt; extracted Paper 06 desk-rejected by JAIR 2026-07-15 → pivot to TMLR (`Σ-Align/10-jair-desk-rejection-response.md`) |
| 8 | Mesa-Optimization via Schema Coherence | Paper 07 (Empirical #2, incl. former Paper 08 scope) | ⚪ Not started | — | Wait for Ch 5 results; extracted paper venue TMLR or ICLR/NeurIPS main track |
| 9 | Schema-Coherent Training for Safe AGI | Paper 09 (Final Scoping) | ⚪ Not started | — | Wait for Ch 6–8 results |
| 10 | Conclusion | original | ⚪ Not started | — | Months 33–36 |

## Phase Document Status

| Chapter | Phases |
|:--------|:-------|
| 01-introduction | `00_cross_cutting` ✅ `00_repo` ✅ `00_5_research` ✅ `10_draft` ✅ (phases 01–09 N/A) — chapter drafted |
| 02-agi-safety-landscape | `00_cross_cutting` ✅ `00_repo` ✅ `00_5_research` ✅ `01`–`11` ✅ (carried over from Paper 01) `12_paper_extraction` ⬜ `99_finale` ⬜ |
| 03-sigma-trap-evidence | `00_cross_cutting` ✅ `00_repo` ✅ `00_5_research` ✅ `01`–`09` ✅ (carried over from Paper 02) `10`+ ⬜ |
| 04, 05, 06, 08, 09, 10 | ⚪ Phase documents not yet created |
| 07-sigma-model | ⚪ Empirical track — no phase docs (source manuscript complete; adaptation pending) |

## Key Milestones

| Milestone | Target | Chapter |
|:----------|:-------|:--------|
| M1 | Month 6 | Ch 2 adapted (Landscape) |
| M2 | Month 9 | Ch 3 adapted (σ-Trap evidence) |
| M3 | Month 12 | Ch 7 adapted (Σ-Model); TMLR decision on extracted Paper 06 |
| M4 | Month 16 | Ch 4 drafted (Σ-Align Framework) |
| M5 | Month 18 | Ch 5 drafted (Pilot Study) |
| M6 | Month 20 | Ch 6 drafted (Meta-Analysis) |
| M7 | Month 25 | Ch 8 drafted (Mesa-Optimization) |
| M8 | Month 30 | Ch 9 drafted (Implications) |
| M9 | Month 32 | First full monograph draft compiled (Ch 1–10) |
| M10 | Month 36 | Monograph submitted per institution format |

See [`narrative.md`](narrative.md) for the full monograph arc.
See [`cross-cutting.md`](cross-cutting.md) for monograph-level standards.
