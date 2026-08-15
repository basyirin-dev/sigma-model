# Checkpoint B Review — Fresh Mathematical Appendix Review
**Date:** 2026-03-30
**Trigger:** All `[O]`-tagged issues resolved (#4); integration map Tier 1A rows confirmed YES
**Approach:** Fresh agent perspective — no prior fix-cycle context assumed

---

## Review Scope

Complete Mathematical Appendix (§12): Equations A.1–A.13
Also cross-referenced against §3, §4, §6, §7, §10 for consistency.

---

## Q1: Is the system of ODEs closed? Are all variables formally defined?

### State Variables in the ODE System

| Variable | Appears in | Formally Defined | Location |
|----------|-----------|-----------------|----------|
| δA(d,t) | A.1 | YES | §3.1.1, Eq. 1 |
| βA(d,t) | A.2 | YES | §3.1.2, Eq. 5 |
| σA(d,t) | A.1, A.3, A.5, A.5a | YES | §3.1.3, Eq. 3 |
| αA(d,t) | A.3, A.4, A.5a | YES | §4.1.1, Eq. 27 |
| M̂A(d,t) | A.5, A.5a | YES | §4.4.1, Eq. 37 |
| ζA(d,t) | A.5a | YES | §4.4.1, Eq. 38 (derived: ζA = M̂A - σA) |
| ΞA^P(t), ΞA^I(t), ΞA^F(t) | A.6 | YES | §4.3.1, Eq. 35 |

### Functions Used in ODEs

| Function | Appears in | Formally Defined | Location |
|----------|-----------|-----------------|----------|
| η(δrel) | A.1 | YES | §3.4.1, Eq. 13 |
| TA(d,t) | A.1 | YES | §3.4.1, Eq. 14 |
| rA(d,t) | A.1 | YES | §3.3.1, Eq. 8 |
| flearn(d,t) | A.1, A.3 | **DEFINED IN BODY ONLY** | §3.4.1 (prose: "training signal intensity") — no explicit functional form given |
| gexplore(d,t) | A.2 | **DEFINED IN BODY ONLY** | §3.4.2 (prose: "exploration drive") — no explicit functional form given |
| χA(d,t) | A.3 | **DEFINED IN BODY ONLY** | §3.4.3 (prose: "principled-practice fraction") — described as ∈ [0,1] |
| PA(d,t) | A.3 | YES | §3.4.3, Eq. 18 |
| CA(d,t) | A.4 | YES (conceptual) | §4.1.3 ("contrastive training rate") |
| RA^surface(d,t) | A.4 | YES | §4.1.3, Eq. 29a |
| P*(t), I*(t), F*(t) | A.6 | YES | §4.3.2, Eqs. 36a–c |
| ΘA(d,m',m,t) | A.3 | YES | §5.1.3, Eq. 42 |
| ΩAI(d,t) | A.3, A.4, A.5, A.5a | YES (conceptual) | §3.6 ("AI bypass risk") |

### Closure Verdict

**VERDICT: FUNCTIONALLY CLOSED — MINOR ISSUE**

The ODE system is functionally closed: every variable that appears in any ODE is either a state variable (defined in §3–§5) or a function of state variables and constants. The system does not contain undefined variables.

**Minor issue:** Three forcing functions — `f_learn(d,t)`, `g_explore(d,t)`, and `χ_A(d,t)` — are used in the ODE system (A.1, A.2, A.3) but are described only in prose in the main body, not given explicit functional forms in the Mathematical Appendix. They are:
- `f_learn(d,t)`: described as "training signal intensity" in §3.4.1
- `g_explore(d,t)`: described as "exploration drive" in §3.4.2
- `χ_A(d,t)`: described as "principled-practice fraction ∈ [0,1]" in §3.4.3

These are exogenous inputs (training-design choices), not internal dynamics — so their absence from the appendix is defensible. However, for the ODE system to be simulatable, they need explicit forms. This is a sub-issue of Issue #17 (parameter non-simulatability), not a new issue.

**No new `[O]` issues created.**

---

## Q2: Are threshold conditions consistent and never contradictory?

### Threshold Inventory

| Threshold | Definition | Location | Used In |
|-----------|-----------|----------|---------|
| σcritical | (1/γσ)·(1 - R₀⁻¹) | Eq. 51 / A.15 | §7 Phase 2 trigger, Eq. 36b (I* step) |
| θI | εmin/(Ψ0·σcritical²·ϕ(d1,d2)) | Eq. 52 / A.15 | §3.5 activation condition |
| θδ | ~0.7 (reference) | §3.2 | Eq. 4 (mastery set) |
| θσ | operationalised via SCAN/COGS | §3.2 | Eq. 4 (mastery set) |
| θβ | (reference) | §3.2 | Eq. 5 (breadth set) |
| δrel > 0.65 | Phase 2→3 trigger | §7 | Eq. 36a (P* step) |
| |M_A| < 2 AND Ψ=0 | Phase 3 characterization | §7 | Eq. 36c (F* step) |

### Consistency Check

1. **σcritical in Eq. 51 vs. A.15:** Identical formula. ✓
2. **σcritical in Eq. 36b (I* step):** Step function checks σA < σcritical vs. ≥ σcritical. Matches Phase 2 trigger. ✓
3. **θI in Eq. 52 vs. A.15:** A.15 states σcritical formula but labels it A.15; Eq. 52 gives θI. Cross-referencing: θI depends on σcritical (via Ψ₀·σcritical²). No contradiction. ✓
4. **Phase triggers in §7 vs. ODE system:** Phase 0→1 (depth investment) — no threshold in ODEs (correct, it's a training-design decision). Phase 1→2 (σA > σcritical) — matches I* step. Phase 2→3 (δrel > 0.65) — matches P* step. Phase 3→4 (ΨA > 0 measurably) — follows from A.6 bifurcation. ✓
5. **θI derivation (A.5):** States "θI scales inversely with ϕ(d1,d2)." Consistent with Eq. 52 where θI = εmin/(Ψ₀·σcritical²·ϕ). ✓

### Contradiction Check

No contradictory threshold conditions found. All thresholds are consistent across §3, §4, §7, and the Appendix.

**VERDICT: CONSISTENT — PASS**

---

## Q3: Does rA σA-coupling appear formally in the correct equations?

### rA Usage Audit

| Equation | rA Appears | σA Appears | Coupling |
|----------|-----------|-----------|----------|
| Eq. 8 (rA definition) | YES (defined) | NO | rA = rmax·exp(-μr·τA) — purely temporal ✓ |
| Eq. 7 (depth decay) | YES: (1-rA) | YES: (1-γσ·σA) | **Separated:** rA is engagement modulation; σA is schema modulation. Product: λc·(1-γσ·σA)·δA·(1-rA). ✓ |
| A.1 (depth ODE) | YES: (1-rA) | YES: (1-γσ·σA) | Same as Eq. 7. ✓ |
| A.3 (σA ODE) | NO | YES | rA does not appear in σA dynamics. ✓ |
| A.4 (αA ODE) | NO | NO | rA and σA absent from attentional fidelity. ✓ |
| A.5 (M̂A ODE) | NO | YES | rA does not distort self-model. ✓ |
| A.6 (ΞA ODE) | NO | NO (indirect via I*) | rA absent; σA enters only via I*(σA) step function. ✓ |

### Verification

- rA appears only in Eq. 7, 8, and A.1. ✓
- rA has no hidden σA dependence: Eq. 8 uses only rmax, μr, τA. ✓
- σA couples to depth decay through λc^eff, not through rA. ✓
- Three-factor product in Eq. 7 cleanly separates: schema coupling × engagement coupling. ✓

**VERDICT: rA σA-coupling is formally correct — PASS**

Issue #4 fix is confirmed clean. The "three-mechanism architecture" (engagement/schema/frontier) stated in the integration map is faithfully represented in the equations.

---

## Q4: Are all constants listed as calibration parameters in §10?

### Complete Constant Inventory

| Constant | Symbol | Defined In | In §10? | In Appendix? |
|----------|--------|-----------|---------|-------------|
| Parametric decay rate | λc | §3.3.1 | NO | A.1 ✓ |
| Breadth decay rate | λb | §3.4.2 | NO | A.2 ✓ |
| Schema formation rate | ρ | §3.4.3 | NO | A.3 ✓ |
| AI bypass erosion | ϵσ | §3.4.3 | NO | A.3 ✓ |
| Attention formation rate | γ | §4.1.3 | NO | A.4 ✓ |
| Attention erosion rate | ζα | §4.1.3 | NO | A.4 ✓ |
| Metacognitive update rate | νM | §4.4.2 | NO | A.5 ✓ |
| Metacognitive distortion | ξM | §4.4.2 | NO | A.5 ✓ |
| Planning relaxation rate | κP | §4.3.2 | NO | A.6 ✓ |
| Inhibition relaxation rate | κI | §4.3.2 | NO | A.6 ✓ |
| Flexibility relaxation rate | κF | §4.3.2 | NO | A.6 ✓ |
| Discovery rate scale | Ψ0 | §3.5 | NO | A.6 ✓ |
| Max engagement rate | rmax | §3.3.1 | NO | Eq. 8 ✓ |
| Engagement decay rate | μr | §3.3.1 | NO | Eq. 8 ✓ |
| Max learning efficiency | ηmax | §3.4.1 | NO | Eq. 13 ✓ |
| Gompertz shape | a | §3.4.1 | NO | Eq. 13 ✓ |
| Gompertz rate | b | §3.4.1 | NO | Eq. 13 ✓ |
| Max transfer coefficient | Tmax | §3.4.1 | NO | Eq. 14 ✓ |
| Half-saturation constant | KT | §3.4.1 | NO | Eq. 14 ✓ |
| Schema-decay coupling | γσ | §3.3.2 | NO | A.2, A.10 ✓ |
| AI augmentation rate | λAI | §3.4.2, Eq. 16 | NO | — |
| Cross-modal coupling | ρθ | §5.1.4 | NO | A.3 ✓ |
| Minimum intersection | εmin | §7 | NO | A.5 ✓ |

### Verdict

**VERDICT: FAIL — No consolidated calibration parameter table in §10**

None of the 22+ constants have a dedicated calibration table in §10. They are scattered across §3, §4, §5, §6, §7, and the Appendix. The user's task requirement — "Are all constants (λc, λb, ρ, ϵσ, γ, ζα, νM, ξM, κP, κI, κF, Ψ0, rmax, μr, ηmax, a, b, Tmax, KT) listed as calibration parameters in §10?" — receives a definitive **NO**.

This is not a new issue. It validates Issue #17 ("Multiple rate constants and parameters... non-simulatable") as a persistent, unresolved concern.

**No new `[O]` issues created. Issue #17 confirmed as actionable.**

---

## Additional Findings

### A.8 Reliability Threshold — Minor Inconsistency

The formula in A.8:
$$R_A^{\min} = 1 - \left(\frac{d}{4}\right)^2 \cdot \frac{k}{k-1}$$

For d=0.3 (small effect), k=5: R_A^min = 1 - (0.075)²·1.25 = 1 - 0.00703 = **0.993**

Wait — rechecking: (0.3/4)² = (0.075)² = 0.005625. × 1.25 = 0.00703. So R_A^min = 0.993.

This does NOT match the table in A.8 which shows 0.72 for d=0.3, k=5. The formula and table are inconsistent.

**Correcting my arithmetic:**
Actually: (d/4)² = (0.3/4)² = 0.005625. k/(k-1) = 5/4 = 1.25. Product = 0.00703. R_A^min = 1 - 0.00703 = 0.993.

The table says 0.72. There is a **discrepancy between the formula and the table values**. Either:
- The formula is wrong, or
- The table was computed with a different formula

Checking d=0.8, k=5: (0.8/4)² = 0.04. × 1.25 = 0.05. R_A^min = 0.95. Table says 0.44.

The table values are dramatically lower than the formula produces. This suggests the table may have been computed with a different formula entirely, or the formula in the appendix is incorrect.

**VERDICT: Formula/table inconsistency in A.8 — potential issue**

However, this is in §6 (V3.0+ reliability) and was not directly touched by any of the 9 resolved issues. It is a pre-existing discrepancy that should be flagged but is not a regression from the fixes.

---

## Checkpoint B Summary

| Question | Verdict |
|----------|---------|
| Q1: ODE system closure | FUNCTIONALLY CLOSED — minor issue with f_learn, g_explore, χ_A forms |
| Q2: Threshold consistency | CONSISTENT — PASS |
| Q3: rA σA-coupling | CORRECT — PASS |
| Q4: Constants in §10 | FAIL — no consolidated table (validates Issue #17) |

**New `[O]`-tagged issues: NONE**

**Pre-existing discrepancy found:** A.8 formula vs. table values inconsistent (not a regression from the 9 fixes).

**Confirmed persistent issue:** Issue #17 (parameter calibration table missing from §10).

---

## Recommendation

Both Checkpoints A and B find **no new issues introduced by the 9 resolved fixes**. The framework is mathematically sound after the Tier 1A resolution cycle. Two pre-existing concerns persist:

1. **Issue #17** (Tier 3): No consolidated calibration parameter table — confirmed as actionable.
2. **A.8 formula/table mismatch**: Pre-existing discrepancy in reliability threshold derivation — should be verified and corrected but is not an `[O]`-tagged issue.

Proceeding to Tier 2 is safe. No blockers from the checkpoint reviews.
