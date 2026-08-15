# Deep Agent Scoring — Issue #28

**Issue #:** 28
**Tag:** [N]
**Date:** 2026-03-30

---

## Scoring Criteria

| Criterion | Description |
|-----------|-------------|
| C1 | ODE System Coherence (0–10) |
| C2 | Novelty Defence (0–10) |
| C3 | Falsifiability (0–10) |
| C4 | Scope Discipline (0–10) |
| C5 | Hackathon Relevance (0–10) |
| C6 | Version Integration Score (0–10) |
| **Composite** | **mean(C1, C2, C3, C4, C5, C6)** |

---

## Variant A — §2.2 gap statement, local prose fix

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | 8 | Purely additive prose to an existing gap statement. No equations altered, no new variables introduced. No risk of ODE inconsistency. |
| C2 | 8 | Directly engages Patel et al.'s specific mechanism (embedding compositions into training data) and explains why it is δA not σA. Names the "recall vs. inference" distinction implicitly. Does not provide a formal boundary criterion. |
| C3 | 3 | Gap statement prose only. Does not add a prediction, sharpen a falsification condition, or specify a proxy. Indirectly supports falsifiability by clarifying what the paper claims. |
| C4 | 8 | Single-agent boundary maintained. No psychological language. No cross-version contamination. Local scope. |
| C5 | 3 | Tangentially related — connects to Learning track via OOD benchmarks but does not directly improve any hackathon protocol. |
| C6 | 5 | Version-neutral. No integration across version boundaries. |
| **Composite** | **5.83** | |

---

## Variant B — §3.1.3 proxy boundary condition, structural equation fix

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | 8 | Adds a boundary condition to proxy identification prose. Does not alter Eq. 3b, any ODE, or any coupling. No risk of ODE inconsistency. |
| C2 | 9 | Provides the formal criterion c ∉ T_train that distinguishes engineered distributions from σA-valid OOD splits. This is the sharpest possible boundary condition: it precisely defines when a benchmark measures σA vs. δA. Directly pre-empts the Patel et al. objection by naming exactly why their test does not validate σA. |
| C3 | 5 | Sharpens proxy validity, which makes downstream predictions more precise. However, does not itself add a prediction or falsification condition. The boundary condition ensures that future σA measurements are correctly calibrated. |
| C4 | 9 | Purely additive to §3.1.3. Does not affect any other section, any cross-version coupling, or any psychological language boundary. Highly localised. |
| C5 | 4 | The boundary condition directly informs benchmark design for the Learning track — benchmarks must satisfy c ∉ T_train to measure σA. This is a pre-design criterion that improves protocol quality, though not a direct protocol modification. |
| C6 | 5 | Version-neutral. The boundary condition applies to σA (V1.0 variable) but does not create or modify cross-version coupling. |
| **Composite** | **6.67** | **[HIGHEST]** |

---

## Variant C — §2.6 synthesis table, systemic reframe

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | 8 | Extends the §2.6 synthesis table and analysis paragraph. No ODE changes. |
| C2 | 9 | Separating meta-learning from distribution engineering is the most comprehensive novelty defence: it prevents a reviewer from treating the two mechanisms as interchangeable. The "recall vs. inference" framing is concrete and precise. Slightly less formal than Variant B's boundary criterion. |
| C3 | 3 | Systemic reframe provides structural context for future predictions but does not itself add a prediction or sharpen a falsification condition. |
| C4 | 7 | Systemic scope — modifies the §2.6 synthesis table which has cross-section implications. However, purely additive (two new rows, one new paragraph). No boundary violations. |
| C5 | 3 | Tangentially related. Does not directly improve any hackathon protocol. |
| C6 | 5 | Version-neutral. The synthesis table spans all versions conceptually but does not modify any version-specific content. |
| **Composite** | **5.83** | |

---

## Variant D — §9 prediction addition, structural equation fix

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | 8 | Adds one prediction to §9. No ODE changes, no new symbols. Uses existing proxy definitions (Eq. 3b, Appendix A.4). |
| C2 | 8 | Directly tests Patel et al.'s result and shows why it does not validate σA. Explicitly distinguishes from Prediction 6b (meta-learning). Strong engagement with the novelty concern, though the prediction tests the claim rather than formally refuting it. |
| C3 | 10 | This is the strongest falsifiability score. Adds a concrete, executable prediction with specific measurement protocol (three-condition battery), explicit H-Bar claim, and a pre-registered falsification condition. Directly operationalises the Issue #28 concern into a testable experiment. |
| C4 | 8 | Additive to §9. Does not cross single-agent, cognitive bridge, or version boundaries. Local scope within §9. |
| C5 | 8 | Directly operationalises a §9 prediction as a benchmark design for the Learning track. The three-condition battery measurement is directly implementable in a Kaggle evaluation protocol. [HACKATHON PRIORITY] |
| C6 | 5 | Version-neutral. The prediction uses V1.0 (σA) and V3.0+ (three-condition battery) but does not modify cross-version coupling. |
| **Composite** | **7.17** | **[HIGHEST — but C3 inflation risk]** |

---

## Variant E — §10.6 P1 protocol, local prose fix

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | 8 | Adds explanatory paragraph to existing protocol. No ODE changes. |
| C2 | 7 | The "recall vs. inference" distinction directly addresses the novelty concern, but it is embedded within a protocol description rather than a standalone formal argument. Less prominent than Variants A–C. |
| C3 | 5 | Sharpens the training protocol that enables predictions (P1 feeds into Predictions 1, 6, 6b, 6c). However, is not itself a prediction or falsification condition. |
| C4 | 8 | Purely additive to §10.6. Does not cross any scope boundaries. |
| C5 | 6 | §10.6 P1 feeds into hackathon tracks (Learning track implementation). The clarification improves protocol understanding but does not directly modify any track protocol. |
| C6 | 5 | Version-neutral. Protocol P1 is V3.0+ content but the addition does not create cross-version coupling. |
| **Composite** | **6.50** | |

---

## Ranking

| Rank | Variant | Composite | Flags |
|------|---------|-----------|-------|
| 1 | **D** | **7.17** | [HACKATHON PRIORITY] C5 = 8 |
| 2 | **B** | **6.67** | — |
| 3 | E | 6.50 | — |
| 4 | A | 5.83 | — |
| 4 | C | 5.83 | — |

---

## Top 2 Variants — Full Scoring Breakdown

### Variant D (Rank 1) — Composite 7.17 [HACKATHON PRIORITY]

| Criterion | Score | Justification |
|-----------|-------|---------------|
| C1 | 8 | No ODE impact. Prediction uses existing proxy definitions. |
| C2 | 8 | Directly tests Patel et al.'s result. Shows the σA/δA dissociation is falsifiable. |
| C3 | 10 | Concrete experimental design with three-condition battery, explicit H-Bar claim, pre-registered falsification condition. The strongest possible falsifiability contribution. |
| C4 | 8 | Local scope within §9. No boundary violations. |
| C5 | 8 | Directly operationalises a §9 prediction as a Learning track benchmark design. The three-condition battery is implementable as a Kaggle protocol. |
| C6 | 5 | Version-neutral. |

### Variant B (Rank 2) — Composite 6.67

| Criterion | Score | Justification |
|-----------|-------|---------------|
| C1 | 8 | No ODE impact. Boundary condition in prose only. |
| C2 | 9 | The formal criterion c ∉ T_train is the sharpest possible boundary condition. Precisely defines when a benchmark measures σA vs. δA. |
| C3 | 5 | Sharpens proxy validity for downstream predictions. Not itself a prediction. |
| C4 | 9 | Highly localised to §3.1.3. No cross-section implications. |
| C5 | 4 | Informs benchmark pre-design for Learning track. Not a direct protocol modification. |
| C6 | 5 | Version-neutral. |

---

## Suppressed Variants

| Variant | Composite | Reason Suppressed |
|---------|-----------|-------------------|
| E | 6.50 | Below rank 2 threshold. The "recall vs. inference" distinction is valuable but is better expressed through Variants B (formal criterion) and D (testable prediction). |
| A | 5.83 | The gap statement addition is important but is superseded by Variant C's more comprehensive systemic reframe, and both are superseded by B and D's sharper formal/predictive approaches. |
| C | 5.83 | The systemic reframe is comprehensive but does not add a formal criterion (B) or testable prediction (D). Its "recall vs. inference" framing is captured by B and D in more actionable form. |

---

## NEGATIVE LOG

| Variant | Reason Not Recommended |
|---------|----------------------|
| A | Gap statement prose is necessary but insufficient — Patel et al.'s specific mechanism needs a formal boundary criterion (Variant B) or testable prediction (Variant D) to be actionable. |
| C | Systemic reframe is comprehensive but lacks the formal precision of Variant B's c ∉ T_train criterion and the testability of Variant D's prediction. |
| E | Protocol clarification is useful but the "recall vs. inference" distinction is better delivered through B (formal criterion at the proxy definition level) and D (testable prediction). |

---

## HACKATHON UPDATE

**Variant D (top):** Prediction 6c's three-condition battery (ID, OOD-struct, OOD-surf-conflict) should be added to hackathon/track_learning.md as a new benchmark family. The measurement protocol (Acc_OOD-struct / Acc_ID) is directly implementable as a Kaggle evaluation. Specific update: add a "Distribution Engineering Dissociation" benchmark row to the Learning track table.

**Variant B (runner-up):** The c ∉ T_train boundary condition should be noted in hackathon/track_learning.md as a pre-design criterion — any submitted benchmark must satisfy c ∉ T_train to validly measure σA.

## INTEGRATION UPDATE

**Variant D (top):** Add a row to integration_map.md for "Prediction 6c (Issue #28)" with variable σA, interacts with δA, Eq. 3b, Appendix A.4, consistency verified YES (uses existing validated proxy definitions).

**Variant B (runner-up):** No integration_map.md update needed — the boundary condition clarifies existing proxy identification without changing any coupling mechanism or equation.

## CHECKPOINT RECOMMENDATION

Not yet at Checkpoint threshold (this is edit #1 after Checkpoint B; 7 more edits needed before next checkpoint).
