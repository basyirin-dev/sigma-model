# Deep Agent Scoring — Issue #8

**Issue #:** 8
**Tag:** [P] (Phase transition)
**Description:** The paper lacks a mathematical criterion such as sensitivity analysis to demonstrate which growth-limiting variable is dominant at any given threshold.

---

## Scoring Breakdown

### VARIANT A — §7 Phase Structure, dominance criterion with prescription table

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **C1 — ODE System Coherence** | 8 | Adds dominance index D_v derived from partial sensitivities of Eq. A.1. Does not modify existing equations. Closes the gap of determining which variable is growth-limiting. The index is a diagnostic quantity, not a new state variable — no unclosed variables introduced. |
| **C2 — Novelty Defence** | 8 | The dominance index is a novel contribution that sharpens the phase structure. Adds a formally derived differentiation argument (sensitivity-based dominance) not present in any comparator framework. |
| **C3 — Falsifiability** | 7 | The dominance index is computable from existing equations. Phase prescriptions become testable by checking if targeting the dominant variable accelerates growth. Does not require direct observation of unobservable variables. But lacks a standalone falsifiable prediction. |
| **C4 — Scope Discipline** | 10 | Stays within single-agent boundary. No psychological language. No version boundary violation. All three boundaries clean. |
| **C5 — Hackathon Relevance** | 7 | The dominance criterion directly improves the Executive Functions track by enabling targeted training interventions based on which variable is binding. |
| **C6 — Version Integration** | 8 | Connects V1.0 depth dynamics (Eq. A.1) with V2.0 attentional (α_A) and schema (σ_A) variables through the dominance index. Integrates across version boundaries without violating them. |
| **COMPOSITE** | **8.0** | |

---

### VARIANT B — §9 Predictions, Prediction 9b for dominance ranking

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **C1 — ODE System Coherence** | 5 | References dominance index D_v but assumes it is defined elsewhere (Variant A or C). Adds a prediction without adding the underlying mathematical framework. Does not close the ODE gap independently. |
| **C2 — Novelty Defence** | 7 | Adds a new falsifiable prediction that sharpens the framework's empirical testability. Distinguishes from δ-only accounts by making phase variable dominance empirically measurable. |
| **C3 — Falsifiability** | 10 | Directly adds a falsifiable prediction with clear measurement protocol (targeted intervention experiment), concrete threshold (80% accuracy target), and falsification condition (below 60%). Most falsifiable variant. |
| **C4 — Scope Discipline** | 10 | Clean on all three boundaries. No psychological language, single-agent, version-neutral. |
| **C5 — Hackathon Relevance** | 5 | Prediction 9b could improve benchmark design for the Learning track by identifying which variable to manipulate. Tangentially related. |
| **C6 — Version Integration** | 5 | Version-neutral. Does not integrate across version boundaries. |
| **COMPOSITE** | **7.0** | |

---

### VARIANT C — Appendix A.3, Jacobian-based dominance criterion

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **C1 — ODE System Coherence** | 10 | Derives dominance criterion rigorously from the Jacobian of the coupled ODE system. Computes partial derivatives from Eqs. A.1, A.3, A.4. Adds formal proposition about Phase 1 dominance. Formally closes an existing gap and propagates consistently to every affected equation. |
| **C2 — Novelty Defence** | 9 | The Jacobian-based dominance criterion is a novel formal contribution. The column norm approach captures both direct and indirect coupling effects, sharpening the bifurcation analysis. Formally derived differentiation argument. |
| **C3 — Falsifiability** | 7 | The Jacobian is computable from existing equations. The proposition about Phase 1 dominance (α_A is binding when σ_A ≈ 0) is testable via targeted interventions. Makes the framework more testable but doesn't add a standalone prediction. |
| **C4 — Scope Discipline** | 10 | Clean on all three boundaries. No psychological language, single-agent, version-neutral. |
| **C5 — Hackathon Relevance** | 5 | The Jacobian analysis could tangentially improve the Executive Functions track protocol by formalising which variable to target. |
| **C6 — Version Integration** | 9 | The Jacobian connects V1.0 depth ODE (Eq. A.1) with V2.0 attentional ODE (Eq. A.4) and schema ODE (Eq. A.3) through the partial derivative matrix. Actively integrates across version boundaries. |
| **COMPOSITE** | **8.33** | |

---

### VARIANT D — §7 systemic reframe, phases as dominance landscape

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **C1 — ODE System Coherence** | 8 | Reframes the phase architecture but preserves all existing equations and trigger conditions. Adds dominance index D_v embedded in the phase structure. Improves coherence without introducing inconsistencies. |
| **C2 — Novelty Defence** | 8 | The dominance landscape framing is a novel systemic contribution. Phases as overlapping regions of a sensitivity landscape is not present in any comparator framework. |
| **C3 — Falsifiability** | 7 | The dominance landscape is testable through intervention experiments. Makes the phase structure more actionable but doesn't add a standalone prediction. |
| **C4 — Scope Discipline** | 10 | Clean on all three boundaries. |
| **C5 — Hackathon Relevance** | 7 | The dominance landscape could improve all five hackathon tracks by making phase prescriptions actionable — each phase targets the dominant variable. |
| **C6 — Version Integration** | 9 | The dominance landscape integrates V1.0 (δ_A) and V2.0 (α_A, σ_A) variables into a unified framework. Reframed diagram shows how all variables interact across phases. |
| **COMPOSITE** | **8.17** | |

---

### VARIANT E — §10.2, limitation acknowledgement

| Criterion | Score | Justification |
|-----------|-------|---------------|
| **C1 — ODE System Coherence** | 4 | Acknowledges the limitation but does not close it. Introduces dominance index notation as future work. Identifies the gap but leaves it open. |
| **C2 — Novelty Defence** | 4 | Proposes a method but does not implement it. Does not actively sharpen any boundary. |
| **C3 — Falsifiability** | 5 | Proposes a validation protocol but does not add a specific falsifiable prediction. Tangentially related. |
| **C4 — Scope Discipline** | 10 | Clean on all three boundaries. |
| **C5 — Hackathon Relevance** | 0 | No relevance to hackathon tracks. Pure limitation acknowledgement. |
| **C6 — Version Integration** | 5 | Version-neutral. |
| **COMPOSITE** | **4.67** | **[SUPPRESSED]** |

---

## Summary Table

| Variant | C1 | C2 | C3 | C4 | C5 | C6 | Composite | Status |
|---------|----|----|----|----|----|----|-----------|--------|
| C | 10 | 9 | 7 | 10 | 5 | 9 | **8.33** | **TOP 1** |
| D | 8 | 8 | 7 | 10 | 7 | 9 | **8.17** | **TOP 2** |
| A | 8 | 8 | 7 | 10 | 7 | 8 | **8.00** | — |
| B | 5 | 7 | 10 | 10 | 5 | 5 | **7.00** | — |
| E | 4 | 4 | 5 | 10 | 0 | 5 | **4.67** | [SUPPRESSED] |

---

## TOP 2 VARIANTS — Full Scoring Breakdown

### #1: VARIANT C [INTEGRATION PRIORITY]

**Section targeted:** Appendix A.3 (σcritical bifurcation derivation)
**Scope:** structural
**Composite:** 8.33

**Why it wins:** Variant C provides the most rigorous mathematical foundation for the dominance criterion by deriving it from the Jacobian of the coupled ODE system. It scores highest on C1 (ODE System Coherence, 10) because it formally closes the gap through partial derivatives of existing equations, and highest on C6 (Version Integration, 9) because the Jacobian matrix connects V1.0 depth dynamics with V2.0 attentional and schema dynamics. The formal proposition about Phase 1 dominance (α_A is binding when σ_A ≈ 0) provides the most prescriptively important result.

**C6 ≥ 9 → [INTEGRATION PRIORITY]**

### #2: VARIANT D

**Section targeted:** §7 Phase Structure (systemic reframe)
**Scope:** systemic
**Composite:** 8.17

**Why it's #2:** Variant D provides the best integration of the dominance criterion into the existing phase architecture. It scores highest on C5 (Hackathon Relevance, 7) alongside Variant A, because the dominance landscape framing makes phase prescriptions actionable for all five hackathon tracks. The systemic reframe is more theoretically coherent than Variant A's add-on approach.

---

## HACKATHON UPDATE

**For Variant C:** The Jacobian-based dominance criterion formalises which variable to target in each phase. This should be noted in hackathon tracks:
- track_executive.md: Add reference to the dominance criterion (Eq. A.16–A.17) for designing inhibitory conflict tasks that test whether the agent correctly identifies the binding constraint.
- track_learning.md: The Phase 1 dominance proposition (α_A binding when σ_A ≈ 0) provides a testable prediction for the Compositional Dissociation Battery.

**For Variant D:** The dominance landscape reframe makes phase prescriptions directly actionable:
- All five track files should reference the dominance index (Eq. 53) for designing interventions that target the growth-limiting variable.

---

## INTEGRATION UPDATE

**For Variant C:**
- integration_map.md: Add row for the Jacobian dominance criterion:
  ```
  | J (Jacobian dominance) | V3.0+ | δ_A, σ_A, α_A | Column norm of linearised coupled system; identifies growth-limiting variable | A.16, A.17 | NO |
  ```

**For Variant D:**
- integration_map.md: Same row as Variant C (the dominance index is the same mathematical object, presented differently).

---

## NEGATIVE LOG

- **Variant E:** Suppressed (composite 4.67 < 6.0). Pure limitation acknowledgement with no implementation — does not close the gap, does not improve falsifiability, has zero hackathon relevance.

---

## CHECKPOINT RECOMMENDATION

Not yet at Checkpoint threshold. Current edit count: 9 (Checkpoint A already passed). Next checkpoint after 8 more approved edits.
