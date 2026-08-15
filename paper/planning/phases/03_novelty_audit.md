# Phase 03 — Novelty Audit & Literature Positioning

**Duration**: 5 days (complete)
**Deadline**: 2026-08-16 ✅
**Dependencies**: Phase 00
**Output**: `paper/planning/novelty-audit.md`
**Executor**: Agent (abstracts via arXiv API) + user review of the gate conclusion
**Status**: ✅ Done — commit `5bfeeec`

## Purpose

Gate the §2 novelty claim: verify that no audited competitor already posits an equivalent
low-schema-coherence attractor / bifurcation with a derived threshold for compositional
failure, and produce the positioning note that pre-empts "this is just grokking/SLT/…".

## Tasks & subtasks (as executed)

1. **Assemble the competitor set** — from the manuscript's §7.1 engagement and the
   consultations: Power et al. 2022 (grokking); Kumar/Bordelon/Gershman/Pehlevan 2023
   (lazy→rich, arXiv 2310.06110); Cullen et al. 2026 (SLT basin selection, 2603.01192);
   Wang 2026 (dimensional phase transition, 2604.04655); Montanari & Wang 2026
   (feature-learning phase transitions, 2602.01434); Xu 2026 (early-warning commutator
   defects); sharpness/flatness; lottery-ticket
2. **Fetch abstracts** via arXiv export API; correct the consultations' attribution
   ("Lyu et al." → Kumar et al.)
3. **Per-competitor comparison** — mechanism / order variable / equivalent-bifurcation
   check / distinguishing empirical signature (8-row table)
4. **Positioning note** (§2 content): σ-trap = stable-equilibrium phenomenon vs grokking =
   temporal escape; σ = macroscopic order parameter vs SLT microscopic LLC; σ = representational
   state vs shortcut-learning strategy; vs lazy/rich and dimensional-transition (generic) —
   σ is compositional-specific
5. **Novelty statement** (candidate): "no existing framework combines a latent
   schema-coherence state variable, coupled shortcut-learning pressure, a derived
   bifurcation threshold, and an empirically detectable transition signature"
6. **Decision-point check** — gate PASSED (no equivalent found); residual risks recorded
   (re-scan at P11; "just a logistic-type equation" objection — defence is empirical
   discriminability at P04, not mathematical novelty)

## Expected outputs

- `paper/planning/novelty-audit.md` (§1 comparison table, §2 positioning, §3 novelty
  statement, §4 decision point + residual risks)

## Decisions

- Gate conclusion: proceed with the σ-trap claim, framed as a *mechanism* (not a universal law)
- Leading-indicator discriminability is the empirical burden of proof → carried into P04

## Exit criteria (met)

- novelty-audit.md committed (5bfeeec); no halt condition triggered ✅
