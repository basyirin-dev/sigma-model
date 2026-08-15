# Deep Agent Scoring — Issue #9

**Issue #:** 9
**Tag:** [N] — Novelty Defence
**Date:** 2026-03-30
**Scoring criteria:** C1–C6 as defined in program.md
**Suppression threshold:** composite < 6.0

---

## Scoring Matrix

| Criterion | Variant A | Variant B | Variant C | Variant D | Variant E |
|---|---|---|---|---|---|
| **C1** — ODE System Coherence | 8 | 8 | 8 | 8 | 8 |
| **C2** — Novelty Defence | 9 | 10 | 8 | 9 | 10 |
| **C3** — Falsifiability | 5 | 6 | 5 | 5 | 10 |
| **C4** — Scope Discipline | 9 | 9 | 9 | 9 | 9 |
| **C5** — Hackathon Relevance | 3 | 5 | 3 | 5 | 7 |
| **C6** — Version Integration | 7 | 8 | 8 | 7 | 8 |
| **Composite** | **6.83** | **7.67** | **6.83** | **7.17** | **8.67** |

---

## Detailed Scoring

### Variant A — §2.2 Gap Statement (local prose)

| Criterion | Score | Rationale |
|---|---|---|
| C1 | 8 | No ODE changes. Prose-only. Does not harm equation closure. |
| C2 | 9 | Directly addresses Lake & Baroni (2023), Patel et al. (2022), Han & Pad'o (2024). Shows each is δA gain without σA gain. Strong pre-emption. |
| C3 | 5 | No new predictions added. Gap statement is assertive but not falsifiable. |
| C4 | 9 | All changes within §2.2 gap statement. No boundary violations. |
| C5 | 3 | No direct hackathon benchmark relevance. Tangential at best. |
| C6 | 7 | References δA (V1.0) and σA (V1.0). Moderate integration. |
| **Composite** | **6.83** | |

### Variant B — §3.1.3 Theorem Corollary (structural)

| Criterion | Score | Rationale |
|---|---|---|
| C1 | 8 | No ODE changes. Corollary uses existing Eq. 3b and Eq. 21. |
| C2 | 10 | Formal proof that σA ≠ optimised δA. Proof-by-contradiction using the OOD/in-distribution ratio. Strongest possible theoretical grounding. |
| C3 | 6 | References Prediction 6 indirectly. Does not add a new falsifiable prediction itself. |
| C4 | 9 | Within existing theorem block in §3.1.3. Clean scope. |
| C5 | 5 | References Protocol P1 (§10.6) which connects to hackathon tracks. Indirect. |
| C6 | 8 | Uses Eq. 3b (V1.0) and Protocol P1 (V3.0+). Good cross-version integration. |
| **Composite** | **7.67** | |

### Variant C — §2.6 Synthesis Table (systemic)

| Criterion | Score | Rationale |
|---|---|---|
| C1 | 8 | No ODE changes. Table extension only. |
| C2 | 8 | Integrates competing accounts into framework rather than opposing them. Shows each is δA-only. Good but less direct than A/B/E. |
| C3 | 5 | No new predictions. Analytical framing only. |
| C4 | 9 | Changes confined to §2.6 table and one paragraph. |
| C5 | 3 | No direct hackathon benchmark relevance. |
| C6 | 8 | Reframes synthesis across all version layers. Good systemic integration. |
| **Composite** | **6.83** | |

### Variant D — §2.5 Cognitive Evaluation (local prose)

| Criterion | Score | Rationale |
|---|---|---|
| C1 | 8 | No ODE changes. Prose-only. |
| C2 | 9 | Directly addresses the benchmark-measures-δA-not-σA distinction. Key insight: meta-learning benchmarks measure in-distribution, not OOD. |
| C3 | 5 | No new predictions. Argues existing benchmarks are insufficient but doesn't add a new test. |
| C4 | 9 | Changes within §2.5 gap statement only. |
| C5 | 5 | References §8 benchmark protocol. Indirect hackathon relevance. |
| C6 | 7 | Integrates with §8 protocol. Moderate cross-version coherence. |
| **Composite** | **7.17** | |

### Variant E — §9 Prediction 6b (structural)

| Criterion | Score | Rationale |
|---|---|---|
| C1 | 8 | No ODE changes. Uses existing Eq. 3b and Appendix A.4 three-condition battery. |
| C2 | 10 | Creates a direct falsifiable test of "σA = optimised δA" using MAML + SCAN. If meta-learning increases Acc_ID and Acc_OOD proportionally, H-Bar is falsified. |
| C3 | 10 | Prediction 6b is fully falsifiable with explicit experimental design: MAML on SCAN, three-condition battery, statistical test on ΔAcc_ID vs. ΔAcc_OOD-struct. |
| C4 | 9 | Changes confined to §9 prediction list. No boundary violations. |
| C5 | 7 | Directly applicable to Learning track (SCAN benchmarks). Prediction 6b generates a concrete Kaggle-evaluable experiment. |
| C6 | 8 | Uses Appendix A.4 (V3.0) three-condition battery. Good integration across version layers. |
| **Composite** | **8.67** | |

---

## Flags

| Variant | Flag |
|---|---|
| E | [INTEGRATION PRIORITY] — C6 = 8 (close to 9, not quite) |
| E | [HACKATHON PRIORITY] — C5 = 7 (approaching 8 threshold) |

---

## Top 2 Variants

### 1. Variant E — §9 Prediction 6b (composite: 8.67)

**Strengths:** Highest falsifiability (C3 = 10), strongest novelty defence (C2 = 10), direct hackathon relevance (C5 = 7). Creates a concrete experimental test that a reviewer can evaluate: does MAML increase Acc_ID and Acc_OOD-struct proportionally or not? If yes, H-Bar's σA is redundant with δA. If no, σA is independently necessary.

**Weaknesses:** Adds a new prediction to §9 (minor structural change). Requires Appendix A.4 to be cited.

### 2. Variant B — §3.1.3 Theorem Corollary (composite: 7.67)

**Strengths:** Formal proof that σA ≠ optimised δA (C2 = 10). The proof is elegant: if a δA-only regime could increase σA, then Acc_OOD would increase without a mechanism forcing representational restructuring — but by construction OOD tests are outside the training distribution. This is the theoretical foundation that Variant E operationalises.

**Weaknesses:** Lower falsifiability (C3 = 6) — the corollary is a proof, not a prediction. Less direct hackathon relevance.

---

## Suppressed Variants

None. All variants score above the 6.0 threshold.

---

## Negative Log (for future cycles)

| Variant | Reason not recommended (if not in top 2) |
|---|---|
| A | Strong novelty defence (C2 = 9) but low falsifiability (C3 = 5) and low hackathon relevance (C5 = 3). Prose-only fix without testable consequences. |
| C | Good systemic framing but lowest novelty defence (C2 = 8) among top variants. Analytical only — no proof or prediction added. |
| D | Good benchmark-measures-δA-not-σA argument but no new prediction. Superseded by E which operationalises the same insight as a falsifiable test. |

---

## HACKATHON UPDATE

**Variant E:** The Prediction 6b experiment (MAML on SCAN + three-condition battery) should be documented in hackathon/track_learning.md as a concrete evaluation protocol for the Learning track. The protocol: train with MAML on SCAN, apply the three-condition battery (ID, OOD-struct, OOD-surf-conflict), measure ΔAcc_ID vs. ΔAcc_OOD-struct.

**Variant B:** Reference Protocol P1 (§10.6) in track_learning.md as the σA-manipulation protocol needed for Prediction 6 tests.

**Recommendation:** If Variant E is approved, update hackathon/track_learning.md with the Prediction 6b experimental protocol.

---

## INTEGRATION UPDATE

**Variant E:** Update integration_map.md:
- Add row: `Prediction 6b (Issue #9)` → interacts with σA, δA, Eq. 3b, Appendix A.4 → "σA/δA dissociation test under meta-learning; uses three-condition battery for falsification" → Equations 3b, A.4 → Consistency Verified: YES (pending paper.md update)

**Variant B:** No integration_map.md update needed (corollary references existing equations already tracked).

---

## CHECKPOINT RECOMMENDATION

Not yet at Checkpoint threshold. Current approved edits: 9 (Issues #1–#6, #10, #22, #23). Issue #9 would be edit #10. Checkpoint A was after edit #9. Recommendation: after approving this edit, perform a brief check on §2.2, §2.5, §2.6, §3.1.3, and §9 to verify no regressions.
