# Phase 10 — arXiv Companion Technical Report

**Duration**: 3–4 days
**Deadline**: parallel to P09 (can start once the cut-list is final)
**Dependencies**: P06–P09 (cut content), P04 (proxy implementation)
**Output**: standalone companion report (`paper/companion/`)
**Executor**: Agent
**Status**: ✅ Complete — companion.tex builds clean (0 undefined refs/citations, 24 pp); dependency cross-check passes both directions

## Result (2026-08-16)

- **companion.tex** (v1.0): plain-article technical-report style with the shared macro/figure set; own title/abstract; Introduction positioning the report as a framework document with the foundational hypothesis as a labelled quote; self-citation of the narrow paper.
- **Content assembled** from `removed-sections-draft.tex` + P04 data: proxy architecture (GCA/RGA/AC, fusion, two-stage calibration, Props 3.6–3.7, implementation), cognitive extensions (α_A, Ξ_A, M̂_A, collective field), multimodal (product space, Θ_A, V_A, R_A), reliability + benchmark protocol, phases 3–5 + faculty–validity, predictions 1–8/H6/M1, five-gap map + assumption ledger + SDE extension, and the full mechanism-gate data (four-arm table, Welch, proxy diagnostics, Prediction-9 τ).
- **Dependency cross-check**: all 21 "companion" refs in the narrow paper verified supplementary (no load-bearing claim); the companion cites the narrow paper only (no circular dependency).
- **Build**: `paper/companion/Makefile` (BIBINPUTS to the shared bibliography); `make pdf` → 0 errors / 0 undefined; 24 pp. 15 framework-citation entries restored into `companion.bib` (pruned from the main bib in P09); a Core-Equations appendix restates the narrow paper's equations for self-containment.

## Purpose

Preserve the full Σ-Model framework — the proxy architecture, cognitive extensions,
multimodal coverage, benchmark protocol, and the extended predictions — as a standalone
arXiv technical report. This is where the "fundamental to AI understanding" ambition
lives, explicitly as a framework document, not a claim. The narrow paper must be fully
self-contained; the companion is referenced only as "complementary material".

## Tasks & subtasks

1. **Assemble companion content** (from the ledger's `companion` tags and the removed
   §§4–6, 8 content):
   - §3.1.4 proxy architecture: GCA/RGA/AC signals, fusion estimator, two-stage
     calibration, Propositions 3.6–3.7, Stage-1 implementation (P04's proxy.py)
   - Cognitive-dimension extensions: attentional fidelity α_A, executive control Ξ_A,
     metacognitive self-model, collective schema field
   - Multimodal: domain × modality product space, cross-modal transfer Θ_A,
     benchmark-validity V_A, reliability R_A
   - Phase structure Phases 3–5, faculty–validity correspondence, benchmark protocol
   - Predictions 1–8 + hypotheses 6.1–6.3 + Meta-Prediction M1
   - Five-gap map, assumption-boundary ledger, SDE extension, (IMEX if moved out at P09)
2. **Write the companion's own intro/abstract** — positioning it as the extended Σ-Model
   framework; the foundational hypothesis stated as the framework's motivation
3. **Self-containment cross-check**
   - Narrow paper: no load-bearing claim depends on the companion (grep-verify every
     "see companion" reference is supplementary)
   - Companion: cites the narrow paper for the core results; no circular dependency
4. **Build** — companion compiles with the same `paper/` toolchain (own Makefile);
   commit sources
5. **Versioning** — companion carries its own title/abstract/version; distinct from the
   narrow manuscript

## Expected outputs

- `paper/companion/companion.tex` (+ Makefile, bibliography, figures) → PDF

## Decisions

- The companion is a technical report, NOT submitted for peer review (P04/user decision:
   arXiv-only until the proxy circularity is broken)
- If a reviewer might see the companion: the narrow paper's self-containment is the
   mitigation (non-negotiable)

## Exit criteria

- Companion builds cleanly; dependency cross-check passes both directions
