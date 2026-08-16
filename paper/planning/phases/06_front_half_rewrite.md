# Phase 06 — Narrow Manuscript Restructure (Front Half)

**Duration**: 4–6 days
**Deadline**: after P05 approval
**Dependencies**: P05 blueprint
**Output**: manuscript §§1–3, 7, 9 restructured
**Executor**: Agent (LaTeX edits) + user review at the §3 checkpoint
**Status**: ✅ Complete — §§1–3, 7, 9 rewritten per the blueprint; §§4–6 and §8 removed (content preserved in `paper/companion/removed-sections-draft.tex`); §3 checkpoint passed (3 reviews, PROCEED); build clean

## Result (2026-08-16)

- **§1** rewritten (title A applied, one research question, three verdict-consistent contributions, companion pointer); **§2** rewritten (four literatures + re-anchored positioning + competing-variable sentence; 3 competitor citations added to the bib).
- **§3** = two-variable core: phenomenological statement + Conjecture 1 (SGD↔ODE) with status paragraph; δ_A/σ_A definitions; mastery/decay; depth + σ ODEs; Lemmas 1–2, Props 2–4 (σ_critical transcritical bifurcation); numerical-integration note. Review fixes applied: σ*_C corrected to (1/γ)(1−R₀⁻¹) (removed inherited internal contradiction), Prop 3 strengthened to global stability, Prop 4 transversality corrected, moving-threshold note added.
- **§7** = Phases 0–2 + bifurcation relation + empirical inflection signature; **§9** = Prediction 9 flagship (descriptive wording).
- **§§4–6, §8** deleted; all dangling refs fixed; label audit: exactly one `??` (abstract → `eq:lr-modulation`, deferred to P08). `make pdf` builds (30 pp, pre-P07 length).

## Purpose

Execute the blueprint's front half: compress §1–2, reduce §3 to the two-variable core,
trim §7 to Phases 0–2 + bifurcation, cut §9 to Prediction 9, and remove §§4–6, 8 from the
submitted manuscript (content preserved for the P10 companion).

## Tasks & subtasks

1. **§1 Introduction (≈1.5 pp)**
   - Keep: SCAN/COGS failure-mode motivation, high-ID/low-OOD dissociation, the
     δ_A-vs-σ_A tension, one central research question, three contributions
   - Cut: cognitive-faculty alignment table, four-version history, scope-qualification vs
     scaling laws; drop "origin" phrasing
   - Insert: one-sentence pointer to the companion ("complementary material") if referenced
2. **§2 Related Work (≈2 pp)**
   - Keep four literatures: compositional generalisation (SCAN/COGS/PCFG-SET), grokking /
     delayed generalisation, representation/feature-learning dynamics, curriculum
     interventions
   - Integrate the P03 positioning note as a dedicated paragraph; add the
     competing-variable design sentence (σ predicts OOD conditional on ID, loss, norm,
     landscape metrics)
   - Cut: continual learning, causal representation learning, cognitive evaluation,
     five-gap map (companion)
3. **§3 Core Framework (≈5–6 pp)** — the heart
   - Keep: δ_A and σ_A definitions + ODEs, state space & vector field, local existence
     (Lemma), forward invariance (Lemma), single-domain equilibria (Prop), the R₀ = 1
     transcritical bifurcation, σ_critical derivation
   - Move/cut per ledger: β_A, Ψ_A, D*, proxy architecture, implementation architecture
     → companion; Fenichel per P05 decision
   - Add: Conjecture 1 (SGD↔ODE mapping); "phenomenological model" statement
4. **§7 Phase Structure (≈1.5 pp)** — Phases 0–2, the Phase 1→2 transition condition, its
   relation to the bifurcation, and the empirically testable inflection signature;
   Phases 3–5 + faculty–validity correspondence → companion
5. **§9 Predictions (≈0.75 pp)** — Prediction 9 (Phase-2 entry inflection) as the single
   flagship; Predictions 1–8, hypotheses 6.1–6.3, M1 → companion (per ledger + P05)
6. **Remove §§4–6 and §8** from `paper/manuscript.tex`; verify their content is preserved
   in the companion working copy (P10 will format it)
7. **Checkpoint**: user review of the §3 core before proceeding to P07

## Expected outputs

- Restructured §§1–3, 7, 9 in `paper/manuscript.tex`
- A companion working copy holding the removed sections (unformatted draft)

## Decisions

- Any deviation from the blueprint (e.g., a result that cannot be cleanly separated) is
  flagged to the user rather than silently kept

## Exit criteria

- Front half matches the blueprint's keep/cut list; user checkpoint passed;
  sections compile in a working build
