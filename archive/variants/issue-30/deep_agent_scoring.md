# Deep Agent Scoring — Issue #30

**Issue #:** 30
**Tag:** [N] — Novelty Defence
**Date:** 2026-03-30
**Cycles scored:** 5 variants

---

## Scoring Criteria

| Criterion | Description |
|---|---|
| **C1** | ODE System Coherence (0–10) |
| **C2** | Novelty Defence (0–10) |
| **C3** | Falsifiability (0–10) |
| **C4** | Scope Discipline (0–10) |
| **C5** | Hackathon Relevance (0–10) |
| **C6** | Version Integration Score (0–10) |
| **Composite** | Mean(C1–C6) |

---

## VARIANT A — §2.2 gap statement, local prose fix

| Criterion | Score | Rationale |
|---|---|---|
| C1 | 10 | Purely additive prose; no equations altered; no new variables introduced |
| C2 | 7 | Names Han & Pad'o explicitly and classifies training regime as δA intervention; but prose-only approach is weaker than formal boundary (B) or testable prediction (D) |
| C3 | 5 | No new prediction or testable claim added; engagement is descriptive only |
| C4 | 10 | Single-agent boundary maintained; no cognitive language; version-neutral |
| C5 | 3 | Tangentially related; no direct hackathon protocol improvement |
| C6 | 5 | Version-neutral; no cross-version integration |
| **Composite** | **6.67** | |

---

## VARIANT B — §3.1.3 Categorical Distinction Theorem corollary, structural

| Criterion | Score | Rationale |
|---|---|---|
| C1 | 10 | Corollary to existing theorem; no equation changes; no new symbols |
| C2 | 9 | Formal PC1–PC3 boundary shows training regime optimisation fails all three criteria; directly addresses Han & Pad'o by name; sharpens σA/δA distinction with structural property vs. procedural property framing |
| C3 | 7 | Formal boundary criterion (c' ∉ T_train vs. c ∈ T_train) is testable through the three-condition battery; not a dedicated prediction but provides falsifiable structure |
| C4 | 10 | Single-agent boundary; no cognitive language; version-neutral |
| C5 | 3 | Tangentially related; no direct hackathon protocol improvement |
| C6 | 5 | Version-neutral; no cross-version integration |
| **Composite** | **7.33** | |

---

## VARIANT C — §2.6 Five-Gap Map table, systemic reframe

| Criterion | Score | Rationale |
|---|---|---|
| C1 | 10 | Table row addition and analysis paragraph; no equation changes |
| C2 | 8 | Adds dedicated row separating training regime from meta-learning and distribution engineering; analysis paragraph connects to σA ODE (Eq. 28) and PA (Eq. 18) |
| C3 | 5 | No new prediction; analysis is descriptive; less actionable than B or D |
| C4 | 10 | Single-agent; no cognitive language; version-neutral |
| C5 | 3 | Tangentially related; no direct hackathon protocol improvement |
| C6 | 5 | Version-neutral; no cross-version integration |
| **Composite** | **6.83** | |

---

## VARIANT D — §9 Predictions, add Prediction 6d, structural

| Criterion | Score | Rationale |
|---|---|---|
| C1 | 10 | Prediction addition; uses existing three-condition battery (Eq. 3b, Appendix A.4); no equation changes |
| C2 | 9 | Testable prediction with concrete empirical numbers (78.3%, 62.1%, 12.4%, 15.7%); explicit distinction from Predictions 6b and 6c; formalises the challenge as a falsifiable claim |
| C3 | 9 | Dedicated prediction with falsification condition; uses existing three-condition battery; directly testable on COGS; experimental numbers provide grounding |
| C4 | 10 | Single-agent; no cognitive language; version-neutral |
| C5 | 3 | Tangentially related to hackathon tracks; no direct protocol improvement |
| C6 | 5 | Version-neutral; no cross-version integration |
| **Composite** | **7.67** | |

**Flags:** None (C5 < 8, C6 < 9)

---

## VARIANT E — §10.6 P1 + §2.2 gap statement, local prose fix

| Criterion | Score | Rationale |
|---|---|---|
| C1 | 10 | Prose additions to two sections; no equation changes |
| C2 | 7 | Dual-location coverage is thorough but prose-only; formal criterion (ΔAcc_ID > ΔAcc_OOD-struct vs. ΔAcc_OOD-struct > 0) is useful but less sharp than B's PC1–PC3 or D's prediction |
| C3 | 5 | No new prediction; engagement is descriptive; less actionable than D |
| C4 | 10 | Single-agent; no cognitive language; version-neutral |
| C5 | 3 | Tangentially related; no direct hackathon protocol improvement |
| C6 | 5 | Version-neutral; no cross-version integration |
| **Composite** | **6.17** | |

---

## Ranking

| Rank | Variant | Composite | Key Strength | Key Weakness |
|---|---|---|---|---|
| 1 | **D** | **7.67** | Testable prediction with empirical numbers; highest C3 (9) | No hackathon relevance (C5: 3) |
| 2 | **B** | **7.33** | Formal PC1–PC3 boundary; highest C2 (9) | No dedicated prediction (C3: 7) |
| 3 | C | 6.83 | Systemic table row; clear separation of mechanisms | No falsifiable claim (C3: 5) |
| 4 | A | 6.67 | Minimal, safe addition | Prose-only; no formal criterion (C3: 5) |
| 5 | E | 6.17 | Dual-location consistency | Prose-only; weakest C2 (7) and C3 (5) |

---

## Suppression Check

All variants have composite ≥ 6.0. No variants suppressed.

---

## Top 2 Variants

### 🥇 VARIANT D — Composite: 7.67

**Full scoring:**
| C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|
| 10 | 9 | 9 | 10 | 3 | 5 |

**Recommendation:** APPROVED. Prediction 6d provides the strongest novelty defence against Han & Pad'o (2024) by creating a directly falsifiable test with concrete empirical grounding. The three-condition battery measurement and explicit distinction from Predictions 6b/6c maximise argumentative rigour.

### 🥈 VARIANT B — Composite: 7.33

**Full scoring:**
| C1 | C2 | C3 | C4 | C5 | C6 |
|---|---|---|---|---|---|
| 10 | 9 | 7 | 10 | 3 | 5 |

**Recommendation:** Strong alternative. The PC1–PC3 corollary provides the strongest formal boundary criterion. Best suited as complementary to Variant D — the corollary in §3.1.3 provides definitional grounding while Prediction 6d in §9 provides testability.

---

## HACKATHON UPDATE:
None for both variants. Neither Variant D nor Variant B directly improves any hackathon track protocol. The predictions and boundary criteria are novelty-defence mechanisms, not benchmark designs.

## INTEGRATION UPDATE:
If Variant D is approved:
- Add row to integration_map.md: `Prediction 6d (Issue #30) | V3.0+ | σA, δA, Eq. 3b, Appendix A.4 | Training regime optimisation dissociation test; uses three-condition battery for falsification of Han & Pad'o (2024) claim | 3b, A.4 | YES`

If Variant B is approved:
- Add row to integration_map.md: `Training Regime Boundary Corollary (Issue #30) | V3.0+ | σA, PC1–PC3, Categorical Distinction Theorem | Formal boundary showing training regime optimisation fails PC1–PC3 criteria | 3, 3b | YES`

## NEGATIVE LOG:
- **Variant A:** Prose-only gap statement addition is necessary but weaker than Variant D's Prediction 6d enhancement (C3: 5 vs. 9) and Variant B's formal boundary criterion (C2: 7 vs. 9).
- **Variant C:** Systemic reframe with table row is clear but lacks falsifiable claims (C3: 5); weaker than Variant D's testable prediction and Variant B's formal criterion.
- **Variant E:** Dual-location prose addition is thorough but provides the weakest novelty defence (C2: 7) and no falsifiability improvement (C3: 5) compared to D and B.

## CHECKPOINT RECOMMENDATION:
Not yet at Checkpoint threshold. Current approved edit count: 12 (Issues #1–#6, #10, #22, #23, #28, #29, #11). Next checkpoint after 16 approved edits.
