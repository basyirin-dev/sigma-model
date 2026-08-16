# Paper 06 v2 — Paper Blueprint (Claim-Level Lock)

**Date**: 2026-08-16
**Phase**: P05
**Status**: 🔶 drafted — awaiting user approval
**Inputs**: P04 gate verdict (`paper/planning/gate-result.md`), claim ledger (P00), novelty audit (P03), cross-cutting standards (CC.2/CC.3)
**Contract for**: P06–P09 (manuscript restructure, empirical rebuild, epistemology, format/build)

---

## 1. Claim-level lock (from P04 — binding)

**Verdict: phenomenological/descriptive** — "a dynamical model of σ-trap behaviour", *not* "a dynamical mechanism".

| What the lock permits | What the lock forbids |
|---|---|
| σ-trap as a descriptive dynamical model of a reproduced behaviour | "σ drives/explains the failure" (mechanistic causation) |
| Empirical statements hedged to the gate's measured scope (H-Bar, n=15, T4) | "σ̃_A precedes/leads OOD" (leading-indicator claims) |
| σ-scheduling as *one* sufficient intervention among equals (fixed-weight equivalence) | "the σ-modulated curriculum is necessary" |
| Conjecture 1 (SGD↔ODE) as an explicitly labeled modelling assumption | Any unqualified "SGD-induced" / "origin" wording |
| RGA-as-consequence finding (geometry tracks comp exposure, incl. in the no-σ arm) | "representational organisation causes compositional OOD success" |

**Evidence base (P04, 60 runs):** baseline OOD 45.9±4.8 (trap reproduced, gap 44.3 pp vs ID 90.2);
fixed_weight 98.9±3.6 = additive 98.9±2.4 (p=0.99); multiplicative 94.0±8.9; measured σ̃_A
partial corr → OOD_{t+1} ≈ 0 (pooled ODE +0.018, one-sided t p=0.24); RGA-only +0.125 (p≈0.005)
but also in fixed_weight; scheduled knob leads-fraction 0.00 in all arms (archived finding reproduced).

---

## 2. Three-layer claim taxonomy applied to every ledger entry

**Layer definitions** (CC.3.2):

- **MT — model theorem**: what follows from the posited ODEs (assertive, "within the model" scope).
  Never asserted about real SGD/training beyond Conjecture 1.
- **EO — empirical observation**: what the pilot/gate data show (hedged to the measured scope:
  H-Bar benchmark, n=15/arm, this architecture, T4 run). Always with raw distributions + CIs.
- **SI — scientific interpretation**: what we argue it means (conditional; discussion-level;
  may appear as labeled research programme only).
- **MA — modelling assumption**: explicit, labeled (Conjecture 1; operational definitions).
- **(companion) / (cut)**: not in the narrow paper.

### 2.1 Mapping table — mathematical results (ledger §A)

| Ledger item | Tag (ledger) | Layer | Wording responsibility (§) |
|:------------|:-------------|:------|:---------------------------|
| Prop 3.1 Local Existence → **Lemma 1** | keep | MT | §3.4; proof → App A |
| Prop 3.2 Forward Invariance → **Lemma 2** | keep | MT | §3.4; proof → App A |
| Prop 3.3 Fast–Slow Decomposition (Fenichel) | decide → companion | MT | companion (§R3) |
| Prop 3.4 Single-Domain Equilibria | keep | MT | §3.4 (equilibria of the two-variable core) |
| Prop 3.5 Numerical Stability | cut | — | — (one-line footnote in App A at most) |
| Prop 3.6 Estimator Consistency | companion | MT | companion (§R2, measurement) |
| Prop 3.7 Error Propagation (ODE system) | companion | MT | companion (§R2) |
| Thm 4.1 "SGD-induced σ-suppression" → **Prop 1 (model-conditional)** | keep (relabel) | MT, explicitly scoped: "under the proposed dynamics, standard *training conditions* (as defined in §3) yield a stable low-σ equilibrium" | §3.5 — no "SGD-induced" wording anywhere |
| Prop 4.1 σ_critical derivation (R₀=1 transcritical bifurcation) | keep | MT | §3.4/§7 — main theorem of the narrow paper |
| Prop 4.2 Depth Threshold (phase 2→3) | companion | MT | companion |
| Prop 4.3 Hysteresis / reverse transitions | decide → companion | MT | companion (§R4, conjecture-level note) |
| Prop 4.4 Noise Sensitivity (SDE) | companion | MT | companion (§R5) |
| Thm 4.2 Faculty–Validity Correspondence | companion | SI | companion |
| Lemma 4.2 Faculty Omission Penalty | companion | — | companion |
| Prop 4.5 Compensation Analysis | companion | MT | companion |
| **Conjecture 1 — SGD↔ODE mapping** (new) | keep (new) | **MA** — the modelling assumption connecting real training trajectories to the posited ODEs | §3 opening; restated once in §13 (research programme) |

### 2.2 Mapping table — predictions (ledger §B)

| Ledger item | Tag (ledger) | Layer | Wording responsibility (§) |
|:------------|:-------------|:------|:---------------------------|
| Prediction 1 — Schema quality at intersections | companion | SI | companion |
| Prediction 2 — AI augmentation / schema suppression | companion | SI | companion |
| Prediction 3 — Relative mastery as resilience | companion | SI | companion |
| Prediction 4 — Shortcut threshold expansion | companion | SI | companion |
| Prediction 5 — Phase-3 compression | companion | SI | companion |
| Prediction 6 — Multiplicative vs additive σ_A | decide → companion | SI | companion |
| Hypotheses 6.1–6.3 | companion | SI | companion |
| Prediction 7 — Benchmark validity cross-model | companion | SI | companion |
| Prediction 8 — Cross-modal schema transfer | companion | SI | companion |
| **Prediction 9 — Phase-2 entry inflection** | keep (flagship) | MT (the bifurcation predicts the inflection) **+ EO** (transitions observed in the ODE arms of the gate) | §9 — reworded descriptively: "the model predicts an inflection in phase-2 entry under σ-modulated training; observed at step ≈ 200–400 in the gate" — no mechanistic reading |
| Meta-Prediction M1 — Incidental σ_A elevation | companion | SI | companion (future programme) |

### 2.3 Mapping table — framework components (ledger §C)

| Ledger item | Tag (ledger) | Layer | Wording responsibility (§) |
|:------------|:-------------|:------|:---------------------------|
| Depth δ_A (dimension + ODE) | keep | MT | §3.1–§3.3 |
| Schema coherence σ_A (dimension + ODE) | keep | MT | §3.1–§3.3 |
| Breadth β_A | companion | MT | companion |
| Online estimation protocol (two-tier proxy: GCA/RGA/AC fusion + Stage-2 calibration) | companion | SI (measurement) | companion; **one-sentence reference** in §3 (see §9 circularity decision) |
| Mastery set | keep | **MA** (operational definition) | §3.1 (needed to define δ_A) |
| Decay architecture (schema-mediated decay, combined depth decay) | keep (minimal) | MT | §3.2 (only what the two-variable ODEs need) |
| Growth dynamics (depth + σ ODEs) | keep | MT | §3.3 (core equations) |
| Intersection activation Ψ_A | companion | MT | companion |
| Shortcut threshold D* | companion | MT | companion (≤1 paragraph mention) |
| Math foundations: state space & vector field | keep | MT | §3.4 |
| Math foundations: timescale separation | decide → companion | MT | companion |
| Math foundations: equilibrium analysis | keep | MT | §3.4 |
| Math foundations: numerical integration protocol | keep (compressed) | MT + EO (reproducibility) | App A |
| Implementation: required network features | companion | — | companion |
| Implementation: GCA/RGA/AC signal extraction | companion | SI | companion (with §2.3 protocol row) |
| Implementation: ODE-state-modulated training | keep (compressed) | EO/SI | §11 methods (essence only; algorithm box → companion) |
| Implementation: complete training algorithm | companion | — | companion |
| Implementation: computational overhead | companion | — | companion |
| Extension 1 — Attentional fidelity α_A | companion | MT | companion |
| Extensions 2–8 (collective schema field, executive control Ξ_A, self-model, domain × modality product space, cross-modal transfer Θ_A, benchmark validity V_A, benchmark reliability R_A) | companion | MT/SI | companion |
| Phase structure Phases 0–2 + bifurcation | keep | MT (bifurcation) + **EO** (transitions observed in gate) | §7 |
| Phase structure Phases 3–5 | companion | MT | companion |
| Faculty–validity correspondence | companion | SI | companion |
| Five-step benchmark protocol | companion | SI | companion |
| Empirical grounding §10 | keep (rebuilt) | EO | §10 (proof-of-concept framing) |
| Empirical validation §11 | keep (rebuilt) | EO | §11 — rebuilt on gate results (see §3 below) |
| Scope/Open Questions + claim-status table §12 (replaces/augments the assumption-boundary ledger) | keep (rebuilt) | meta | §12 (see §8 below) |
| Conclusion §13 | keep (rewritten) | SI | §13 — no "origin" language; Conjecture 1 restated as research programme |
| Appendix: Notation reference | keep (pruned) | — | App A (only symbols used) |
| Appendix: SDE extension | decide → companion | MT | companion |
| Appendix: IMEX-RK stability | decide → keep (compressed) | MT (numerical-rigour defence) | App A |

**Accounting check**: every ledger `keep` entry has a layer and a target §; every ledger
`companion`/`cut`/`decide` entry is resolved (decide resolutions in §4). No `keep` item in the
narrow paper asserts the mechanistic or leading readings (enforced at P11 re-check).

---

## 3. Empirical numbers — ledger §D refresh (P04 gate, 60 runs)

Replaces the "verify at Phase 04" placeholders in the ledger. Raw per-seed distributions,
95% CIs, and Welch details live in `paper/planning/gate-result.md` §3–§6 (single source);
this table carries the headline values and the wording obligations.

| Quantity (ledger §D) | Old value (paper) | Gate value (n=15/arm, T4) | Status |
|:---------------------|:------------------|:--------------------------|:-------|
| Baseline OOD accuracy | 44.5 ± 4.7% | **45.9 ± 4.8%** [43.2, 48.5] | confirmed (EO) |
| σ-coupled OOD accuracy | ~94–97% | additive **98.9 ± 2.4%**, multiplicative **94.0 ± 8.9%** | confirmed (EO) |
| fixed_weight OOD (new arm) | — | **98.9 ± 3.6%** [97.0, 100.9] | new (EO) |
| Compositional gap (baseline) | — | **44.3 pp** (ID 90.2 − OOD 45.9) | confirmed (EO) |
| Effect sizes | d = 9.08 / 7.57, p < 0.0001 | fixed_weight vs additive Δ=−0.01 pp, **p=0.99**, d=−0.005; vs multiplicative Δ=−4.98, p=0.059, d=−0.76 | **superseded** — report per-pair Welch + per-seed, no pooled d alone (CC.3.6) |
| Phase-2 entry inflection τ | segmented-regression breakpoint | transitions observed in ODE arms; OOD median rise additive 325 / multiplicative 175; additive OOD jumps 42→84→99 between steps 200–400 | confirmed; **τ estimated in P07** from `trajectories.csv` |
| Leading indicator (σ̃_A → OOD) | (assumed in §11 draft) | pooled ODE partial corr **+0.018, one-sided p=0.24** → does not lead | **negative** — wording per §1 lock |
| RGA component (diagnostic) | — | RGA-only partial corr **+0.125, p≈0.005** in comp-exposure arms, incl. fixed_weight | new (EO; consequence-of-exposure reading) |
| Scheduled σ knob leads-fraction | 0.00 (archived finding) | 0.00 in all four arms | reproduced (EO) |

**Wording obligations for §§10–11 (P07):** every number above is reported with its raw
distribution and CI; the fixed-weight equivalence (p=0.99 vs additive) is stated as the
headline finding; the leading-indicator result is reported as a **negative result**, not
omitted; RGA appears only with the consequence-of-exposure interpretation.

---

## 4. Decide-item resolutions (ledger `decide` tags — final)

| Item | Resolution | Rationale |
|:-----|:-----------|:----------|
| Prop 3.3 Fast–Slow / Fenichel | **companion** | Two-variable core needs no timescale separation; cited once in §3.4 as context |
| Prediction 6 (multiplicative vs additive σ_A, Ψ_A) | **companion** | Ψ_A removed; gate shows both arms behave alike on final OOD (p=0.053, d=−0.79) — no narrow-paper content |
| Appendix B — SDE extension | **companion** | Noise sensitivity (Prop 4.4) is deferred with the SDE machinery |
| Appendix C — IMEX-RK stability | **keep (compressed)** | Numerical-rigour defence for the two-variable integration (App A) |

---

## 5. Relabeling plan + Conjecture 1 (per consultations)

**Guiding rule (CC.3.1/CC.3.2):** nothing labelled *Theorem* in the narrow paper; the model is
posited (phenomenological), so results are *Lemmas* (standard mathematics), *Propositions*
(within-the-model claims), and one explicit *Conjecture* (the modelling assumption).

| Old label (ledger) | New label | Exact reworded claim | § |
|:-------------------|:----------|:---------------------|:--|
| Prop 3.1 — Local Existence and Uniqueness | **Lemma 1** | "The two-variable system (Eqs. 1–2) with Lipschitz right-hand side on the invariant box has a unique local solution (Picard–Lindelöf)." Proof → App A | §3.4 |
| Prop 3.2 — Forward Invariance and Boundedness | **Lemma 2** | "Solutions starting in [0,1]² remain in [0,1]² for all t ≥ 0." Proof → App A | §3.4 |
| Prop 3.4 — Single-Domain Equilibria | **Proposition 2** | "The system has the equilibria E₀ (low-σ) and E₁ (high-σ); E₀ is locally stable when R₀ < 1." (unchanged mathematics, relabelled) | §3.4 |
| Theorem 4.1 — "SGD-induced σ-suppression" | **Proposition 3 (model-conditional)** | "Under the proposed dynamics with the training conditions specified in §3.3 (optimiser, loss, σ-modulation schedule), standard training conditions yield a locally stable low-σ equilibrium reachable from generic initial states. **This is a statement about the model, not about real SGD (see Conjecture 1).**" | §3.5 |
| Prop 4.1 — σ_critical derivation | **Proposition 4** | "Crossing σ_critical corresponds to a transcritical bifurcation of the σ-dynamics at R₀ = 1." (main theorem of the narrow paper; relabelled) | §3.4/§7 |
| — (new) | **Conjecture 1 — SGD↔ODE mapping** | Exact wording in §5.1 below | §3 opening |
| Prop 3.3 / 4.2 / 4.3 / 4.4 / Thm 4.2 / Lemma 4.2 / Prop 4.5 | — (companion) | Numbers re-issued in the companion, not referenced by narrow-paper labels | — |

### 5.1 Conjecture 1 — exact wording (draft for §3 opening)

> **Conjecture 1 (SGD↔ODE mapping, modelling assumption).** For the architecture and
> training protocol of §11, there exist empirical diagnostics (depth δ_A and schema
> coherence σ_A measured by the Stage-1 proxies; see companion, §R2) whose evolution along
> SGD trajectories is well approximated, in the scaling regime of the gate experiments, by
> the posited two-variable ODE system (Eqs. 1–2). The conjecture licenses transferring the
> qualitative predictions of the ODE analysis — existence of a stable low-σ equilibrium, the
> σ_critical crossing, and the phase-2 inflection — to trained networks.
>
> *Status:* assumption, not derived. Nothing in this paper asserts that SGD itself instantiates
> the ODEs; the ODEs are a phenomenological description. The gate results (P04) support the
> descriptive use of the model (the trap behaviour is reproduced and the phase transitions
> occur in the σ-modulated arms) but provide **no evidence** that measured σ̃_A precedes OOD
> improvement (partial corr ≈ 0), so no leading-indicator role may be attached to this
> conjecture.

**Wording obligation:** the *status* paragraph accompanies Conjecture 1 wherever it appears
(§3 opening; restated once in §13 as the labeled research programme).

---

## 6. Title decision

| # | Candidate | Verdict |
|:--|:----------|:--------|
| **A** | "The σ-Trap: A Dynamical Model of Schema-Coherence Suppression in Compositional Generalisation" | **✅ recommended** — mechanism-level without "mechanism"; keeps the σ-Trap brand; "suppression" is descriptive (a stable low-σ state), not causal |
| B | "The σ-Trap: A Dynamical Mechanism for Compositional Generalisation Failure" | **❌ rejected** — "Mechanism" asserts causation the P04 gate ruled out; contradicts the locked claim level |
| C | "A Dynamical Model of Schema-Coherence Traps in Compositional Generalisation" | **fallback** — same claim level as A, drops the σ-Trap brand; use if reviewers dislike the brand |

**Decision:** A, with C documented as fallback. Wording constraint: the title never contains
"Origin", "Mechanism", "leads to", or any causal-necessity phrasing; "Dynamical Model" is
mandatory in the chosen title. (Final pick is a user approval point at the end of this phase.)

---

## 7. Section blueprint (~12–14 pp main + appendices)

| § | Section | Disposition | Page target | Content obligations |
|:--|:--------|:------------|:------------|:--------------------|
| §1 | Introduction | rebuild | 1.25 | SCAN/COGS motivation; δ-vs-σ tension; **one** research question; 3 contributions: (1) two-variable dynamical model of σ-trap behaviour with derived σ_critical; (2) gate experiment: trap reproduced + **fixed-weight equivalence** (plain comp loss matches σ-modulation, p=0.99); (3) negative leading-indicator result + RGA-as-consequence diagnostic. No cognitive faculties, no scaling-law qualifiers, no "origin" language |
| §2 | Related Work | rebuild | 1.75 | 4 literature clusters (grokking, SLT, shortcut learning, curriculum/comp-gen; condensed from novelty-audit table of 8) + P03 novelty statement **re-anchored**: descriptive-equilibrium account; distinguishing signature = compositional-specific failure conditional on matched ID; leading-indicator defence **retired**; competing-variable design noted (fixed-weight control + partial-corr controls ran in the gate) |
| §3 | Core (two-variable model) | restructure | 5.0 | Conjecture 1 at opening (§5.1 wording); δ_A + σ_A ODEs (Eqs. 1–2); R₀=1 transcritical bifurcation + σ_critical (Prop 4); Lemmas 1–2, Props 2–3 (§5 relabels); one-sentence Stage-1-proxy reference + circularity statement (see §9); β_A/Ψ_A/D*/full proxy protocol → companion |
| §7 | Phase structure | compress | 1.25 | Phases 0–2 + transition + bifurcation relation (Prop 4); empirical: phase-2 entries observed in gate ODE arms (EO, per §3); phases 3–5 → companion |
| §9 | Predictions | compress | 0.5 | Prediction 9 flagship, descriptive wording ("the model predicts a phase-2-entry inflection; observed in the gate"); remaining predictions → companion |
| §10 | Empirical grounding | rebuild (P07) | 0.5 | Proof-of-concept framing; experimental setup (H-Bar, n=15, T4); per-seed + CI reporting (CC.3.5/3.6) |
| §11 | Empirical validation | rebuild (P07) | 1.75 | Gate results per blueprint §3: four-arm table, Welch pairs, leading tests **including the negative result**, RGA diagnostic; fixed-weight design note (maximal comp exposure, deliberately strong baseline) |
| §12 | Scope / claim status | rebuild (P07) | 0.5 | Claim-status table (§8 skeleton); open questions; "σ is a unique construct — open" |
| §13 | Conclusion | rewrite | 0.5 | Interpretation (SI); Conjecture 1 restated as labeled research program; no "origin"/grand-theory language (CC.3.9) |
| App A | Proofs + notation + integration | prune | 1.25 | Lemma/Prop proofs; notation (only symbols used); numerical integration protocol + compressed IMEX note |
| — | Total | | **~14** | within TMLR norms |

**Section inventory to remove at P06:** the current §3 subsections on Ψ_A, D*, β_A, extensions,
§4 (cognitive extensions), §5 (multimodal), §6 (reliability protocol), §8 (five-step
benchmark protocol), §9's predictions 1–8/H6/M1, phases 3–5, faculty–validity correspondence
— all move to the companion per the ledger, *without deletion* (content preserved).

---

## 8. §12 claim-status table — skeleton

| Claim | Status tag | Evidence (gate) |
|:------|:-----------|:----------------|
| Two-variable ODE system has a stable low-σ equilibrium (E₀) | **proven in model** | Prop 3 (model-conditional) |
| σ_critical = transcritical bifurcation at R₀ = 1 | **proven in model** | Prop 4 |
| Standard training reproduces the trap (high ID / low OOD) | **empirically supported** | baseline ID 90.2 / OOD 45.9, gap 44.3 pp |
| σ-modulated curriculum improves OOD vs baseline | **empirically supported** | additive 98.9, multiplicative 94.0 vs 45.9 |
| σ-modulation is *necessary* for OOD improvement | **not established** | fixed_weight = additive (p=0.99) |
| Measured σ̃_A precedes OOD improvement | **not established (negative)** | pooled ODE partial corr +0.018, one-sided p=0.24 |
| RGA component tracks compositional-loss exposure | **empirically supported** | +0.125 (p≈0.005), incl. fixed_weight (no σ dynamics) |
| σ_A is a unique construct vs grokking/SLT/shortcut variables | **open** | competing variables (sharpness/LLC) not yet measured in the gate; the fixed-weight + partial-corr controls are the first such checks |
| SGD↔ODE mapping holds | **assumption** | Conjecture 1, explicitly unproven |
| Phase-2 entry inflection under σ-modulated training | **proven in model + empirically supported** | bifurcation (Prop 4) + transitions observed at steps ≈ 200–400 |

---

## 9. Circularity decision (CC.3.4)

1. **Stage-2 diagnostic (σ̂_A = Acc_OOD / Acc_ID)** is used **post-hoc only** — as a
   descriptive summary of the measured gap, never as a training signal and never as evidence
   for a leading/causal relationship. Wherever σ̂_A appears (§11 results, §12 table), a
   one-sentence circularity statement accompanies it ("σ̂_A is defined from the same
   accuracies it describes; it is reported as a descriptive diagnostic, not a measurement of
   an independent construct").
2. **Stage-1 proxies (GCA/RGA/AC)** are referenced in the narrow paper with **one sentence**
   in §3 (definition of the measured σ̃_A used in §11) and a pointer to the companion
   (§R2) for the full protocol, Props 3.6–3.7, and the two-stage calibration. The gate's
   measured σ̃_A (fused GCA+RGA) is reported with its negative leading result; the RGA
   component result is reported with the consequence-of-exposure interpretation.
3. **Claim-status row**: "σ is a unique construct — **open**" (competing variables such as
   sharpness/LLC were not measured in the gate; the fixed-weight control and partial-
   correlation controls are the first competing-variable checks and are reported as such).

---

## 10. Page budget summary (TMLR norms)

| Component | Pages |
|:----------|:------|
| Main text §§1–13 (targets in §7) | ≈ 12.75 |
| Appendix A (proofs, notation, integration + IMEX note) | ≈ 1.25 |
| **Total** | **≈ 14** — within TMLR length norms; trim target if reviewers push back: §2 → 1.5 pp, §3 → 4.5 pp |
| Figures (planned) | 3: gate four-arm OOD summary; σ̃_A/phase trajectories; claim-status table (§12) |
| Tables | 2–3: per-arm results (raw + CI), Welch pairs, leading-test summary |

**Assembly checklist (used at P06–P09 and re-checked at P11):**
- [ ] every ledger `keep` entry appears in the blueprint mapping with a §
- [ ] no "Theorem"/"SGD-induced"/"origin"/"mechanism (causal)" wording in any kept section
- [ ] Conjecture 1 present at §3 opening with its status paragraph
- [ ] circularity statement present at every σ̂_A use
- [ ] negative leading-indicator result reported, not omitted (§11)
- [ ] per-seed distributions + CIs for every gate number (CC.3.5)
- [ ] page budget ≤ 14 pp incl. appendix

---

## 11. Approval

**Status: ✅ approved by user (2026-08-16)** — P05 exit criterion met.

- [x] **User approval** — this blueprint is the contract P06–P09 execute against. Title pick
      confirmed by the user: **A** ("The σ-Trap: A Dynamical Model of Schema-Coherence
      Suppression in Compositional Generalisation"); C retained as documented fallback; B
      rejected by the locked claim level and will not be used.
- [x] Approved blueprint committed (this file); P06 may start.





