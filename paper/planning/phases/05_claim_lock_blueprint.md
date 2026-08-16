# Phase 05 — Claim-Level Lock & Paper Blueprint

**Duration**: 2–3 days
**Deadline**: after P04 gate verdict
**Dependencies**: P04 (gate result), P00 (claim ledger), P03 (novelty audit)
**Output**: `paper/planning/paper-blueprint.md` — user-approved
**Executor**: Agent (drafts) + user (approval)
**Status**: 🔶 Drafted — `paper/planning/paper-blueprint.md` complete (taxonomy mapping, gate-number refresh, decide resolutions, relabeling plan + Conjecture 1, title decision, section blueprint, claim-status skeleton, circularity decision, page budget); **awaiting user approval** before P06

## Draft result (2026-08-16)

- Verdict lock encoded throughout: phenomenological/descriptive; no mechanistic or leading-indicator wording in any kept section.
- Title: **A recommended** ("The σ-Trap: A Dynamical Model of Schema-Coherence Suppression in Compositional Generalisation"), C fallback, B rejected.
- Page budget ≈ 14 pp (main ≈ 12.75 + appendix ≈ 1.25), within TMLR norms; §12 claim-status skeleton includes "σ is a unique construct — open" and the negative leading result.
- Circularity: σ̂_A post-hoc only, stated plainly; Stage-1 proxies one-sentence-referenced to the companion.
- Approval marker: see `paper/planning/paper-blueprint.md` §11 (to be ticked by the user).

## Purpose

Convert the gate verdict and the claim ledger into a precise blueprint: the three-layer
claim taxonomy applied to every result, the relabeling plan, the title, per-section
keep/cut/compress/move-to-companion decisions with page targets, and the circularity
decision. This is the contract P06–P09 execute against.

## Tasks & subtasks

1. **Apply the three-layer claim taxonomy to every ledger entry**
   - *Model theorem* — what follows from the posited ODEs (assertive)
   - *Empirical observation* — what the pilot/gate data show (hedged to the measured scope)
   - *Scientific interpretation* — what we argue it means (conditional, discussion-level)
   - Produce a mapping table: ledger item → layer → wording responsibility (§)
2. **Relabeling plan** (per consultations)
   - Theorem 4.1 → model-conditional Proposition ("under the proposed dynamics, standard
     training conditions yield a stable low-σ equilibrium") — no "SGD-induced" claim
   - Propositions 3.1–3.2 → Lemmas (standard applications; proofs to appendix)
   - Add explicit **Conjecture 1: SGD↔ODE mapping** (the modelling assumption)
   - Decide Prop 3.3 (Fenichel), Prediction 6, SDE/IMEX appendices (ledger `decide` items)
     — default: Fenichel → companion unless the two-variable analysis needs it; Pred 6 →
     companion; SDE → companion; IMEX → keep-compressed (numerical-rigour defence)
3. **Title selection** — 3 mechanism-level candidates (drop "as the Origin of…"):
   - A) "The σ-Trap: A Dynamical Model of Schema-Coherence Suppression in Compositional Generalisation"
   - B) "The σ-Trap: A Dynamical Mechanism for Compositional Generalisation Failure"
   - C) "A Dynamical Model of Schema-Coherence Traps in Compositional Generalisation"
   - Pick one with a documented fallback; revisit wording after the gate verdict
4. **Section blueprint** (~12–14 pp main + appendices), derived from the ledger:
   - §1 Intro ≈1.5 pp (SCAN/COGS motivation, δ-vs-σ tension, one research question,
     3 contributions; no cognitive faculties, no scaling-law qualifiers)
   - §2 Related Work ≈2 pp (4 literatures + P03 novelty statement; competing-variable design)
   - §3 Core ≈5–6 pp (two-variable core: δ_A, σ_A ODEs, R₀=1 transcritical bifurcation,
     σ_critical, existence/invariance/equilibria; β_A/Ψ_A/D*/proxy → companion)
   - §7 Phase structure ≈1.5 pp (Phases 0–2 + transition + bifurcation relation)
   - §9 Predictions ≈0.75 pp (Prediction 9 flagship; wording per gate verdict)
   - §§10–13 rebuilt (P07); appendices pruned (P09)
5. **Circularity decision** — σ̂_A = Acc_OOD/Acc_ID used *post-hoc* only, stated plainly;
   Stage-1 proxies (GCA/RGA) referenced with one sentence to the companion; the claim-status
   table (§12) lists "σ is a unique construct — open"
6. **Commit** blueprint; **user approval required** before P06

## Expected outputs

- `paper/planning/paper-blueprint.md` (taxonomy table, relabeling plan, title, section plan,
  circularity decision, page budget)
- Approved-by-user marker

## Decisions (forks)

- Claim level (from P04) fixes abstract/intro wording; the blueprint must not contradict it
- Whether Fenichel/Pred-6/SDE/IMEX stay in the narrow paper — resolved here, final

## Exit criteria

- Blueprint committed and explicitly approved by the user; page budget within TMLR norms
