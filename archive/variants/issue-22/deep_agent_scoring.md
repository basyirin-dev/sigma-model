# Issue #22 — DEEP AGENT Scoring (MODE 2)

## Scoring Criteria Reference

| Code | Criterion | Scale |
|------|-----------|-------|
| C1 | ODE System Coherence | 0–10 |
| C2 | Novelty Defence | 0–10 |
| C3 | Falsifiability | 0–10 |
| C4 | Scope Discipline | 0–10 |
| C5 | Hackathon Relevance | 0–10 |
| C6 | Version Integration | 0–10 |

**Composite = mean(C1, C2, C3, C4, C5, C6)**
**Suppression threshold: composite < 6.0**

---

## Variant A — Clamp to [0,1] (local)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **8** | Adds a `max(0, ·)` floor to Equation 48, ensuring $R_A \geq 0$. The ODE system is not directly affected (Eq. 48 is a measurement function, not a dynamical equation), but the validity function (Eq. 49) now has a guaranteed non-negative factor. No new unclosed variables introduced. The fix is minimal and self-contained — it patches the boundedness violation without altering the functional form. However, the `max` operator introduces a non-smooth point at $CV = 1$, which could complicate sensitivity analysis of $V_A$ near the boundary. |
| C2 | **7** | No conflation introduced. $R_A$ remains a distinct quantity measuring benchmark reliability, separate from $CI$, $FD$, $DG$. The coefficient-of-variance-based definition is preserved, maintaining its distinction from the psychometric reliability constructs (test-retest correlation, internal consistency). The floor operation does not blur any variable boundaries. |
| C3 | **5** | The fix makes the reliability threshold $R_A > 0.75$ more interpretable (it now has a guaranteed domain) but does not sharpen any of the eight §9 predictions. Prediction 7 (benchmark validity predicts cross-model stability) uses $V_A$, which is now better-defined, but the prediction itself is not made more testable. The boundedness fix is a measurement-theory correction, not an empirical sharpening. |
| C4 | **9** | All three boundaries clean. Single-agent ✓ (measurement function, not agent state), cognitive bridge ✓ (no psychological language), version boundary ✓ ($R_A$ is a V3.0+ variable in a V3.0+ equation; no V1.0 bleed). |
| C5 | **6** | The fix ensures the reliability component of the H-Bar Benchmark Protocol is formally valid, which is necessary for hackathon submission. However, it does not improve the benchmark design itself or enable new protocol capabilities. It is a correctness fix, not an enhancement. Tangentially related — the hackathon tracks benefit from valid reliability measurement, but no specific track protocol is improved. |
| C6 | **3** | The `max(0, ·)` operation is a local patch that does not create cross-version coupling. It does not integrate language, notation, or structure across version boundaries. Version-neutral at best; the non-smooth boundary could create subtle version-seam issues if sensitivity analysis near $CV = 1$ is needed in future V3.0+ extensions. |

**Composite: (8+7+5+9+6+3)/6 = 38/6 = 6.33 → [QUALIFIES]**

---

## Variant B — Bounded Functional Form (structural)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **9** | Replaces Equation 48 with $R_A = 1/(1 + CV^2)$, which is bounded in $(0,1]$ by construction. The validity function (Eq. 49) now has a formally guaranteed non-negative factor. No new unclosed variables; no new parameters. The form is smooth (infinitely differentiable), which preserves any future sensitivity analysis. The ODE system is unaffected (Eq. 48 is a measurement function). Highest ODE coherence — the boundedness is structural, not patched. |
| C2 | **8** | The inverse form $1/(1 + CV^2)$ is cleanly separated from adjacent constructs. It is an information-theoretic quantity (signal-to-noise ratio) — distinct from test-retest correlation (Variant C), absolute reliability (original form), or internal consistency (Cronbach's α). The form actively sharpens the boundary: $R_A = 0.5$ at $CV = 1$ provides a natural midpoint interpretation that the original form lacked. |
| C3 | **6** | The bounded form makes the minimum threshold $R_A > 0.75$ more interpretable ($CV < 0.577$), which marginally improves the testability of Prediction 7. However, the prediction itself is not sharpened — the reliability-validity relationship is better-defined but not more empirically discriminating. |
| C4 | **9** | All three boundaries clean. Single-agent ✓, cognitive bridge ✓ (signal-to-noise ratio is engineering/mathematical, not psychological), version boundary ✓ (V3.0+ variable in V3.0+ equation). |
| C5 | **7** | The bounded form ensures the H-Bar Benchmark Protocol produces valid reliability scores for all benchmarks, including high-variance ones. The signal-to-noise interpretation ($R_A = \mu^2/(\mu^2 + \sigma^2)$) is directly actionable for benchmark designers: it quantifies how much of the observed score is "signal" vs. "noise." This improves the hackathon protocol's reliability assessment without changing the protocol structure. |
| C6 | **6** | The new form introduces a clean mathematical structure ($1/(1 + CV^2)$) that could be integrated into the parameter groups (Appendix A.2) as a dimensionless quantity. The signal-to-noise interpretation connects to existing information-theoretic constructs in the framework. Mild positive integration — the form is self-contained but has natural connections to the entropy-based definitions elsewhere in the paper. |

**Composite: (9+8+6+9+7+6)/6 = 45/6 = 7.50 → [QUALIFIES]**

---

## Variant C — Test-Retest Correlation (structural)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **7** | Replaces Equation 48 with Pearson test-retest correlation, which is bounded in $[-1,1]$ and, for valid benchmarks, in $[0,1]$. The validity function (Eq. 49) is unaffected. However, the correlation-based definition changes the *type* of reliability being measured: from absolute reliability (consistency of raw scores) to relative reliability (rank-order consistency). This is a semantic shift that propagates to the threshold interpretation in §6.2 — $R_A > 0.75$ now means "acceptable-to-good rank-order consistency" rather than "low coefficient of variation." The ODE system is unaffected, but the measurement semantics change. |
| C2 | **9** | Highest novelty defence. Test-retest correlation is a formally distinct quantity from the CV-based reliability, internal consistency (Cronbach's α), and split-half reliability. The psychometric grounding (Nunnally & Bernstein, 1994) provides a formal differentiation argument: this measures rank-order consistency, not score-level consistency. The boundary between $R_A$ (reliability) and $CI$ (construct isolation) is sharpened — $CI$ measures cross-variable discrimination, $R_A$ measures within-variable temporal consistency. |
| C3 | **7** | Test-retest correlation has established interpretive benchmarks in psychometrics ($R > 0.7$ = acceptable, $R > 0.8$ = good, $R > 0.9$ = excellent), which sharpens the interpretability of the $R_A > 0.75$ threshold. Prediction 7 (benchmark validity predicts cross-model stability) becomes more testable: test-retest reliability is a standard predictor of cross-sample stability in psychometrics, providing a direct theoretical link. |
| C4 | **8** | Single-agent ✓, cognitive bridge ✓ (psychometric methodology, not psychological language about agents), version boundary: mild concern. The psychometric framing introduces measurement-theory language from outside the H-Bar formalism, but this is appropriate for a V3.0+ measurement function. No formal boundary violation. |
| C5 | **8** | Test-retest correlation is the field-standard reliability measure for benchmark validation. Adopting it directly aligns the H-Bar Benchmark Protocol with established psychometric practice, making the protocol more credible and interpretable to reviewers familiar with measurement theory. The hackathon tracks benefit from a reliability measure that is immediately recognisable as valid by the evaluation community. **[HACKATHON PRIORITY]** |
| C6 | **5** | Version-neutral. The psychometric definition is self-contained in §6.1.1 and does not create cross-version coupling. Neither improves nor worsens the version seam structure. The external psychometric grounding (Nunnally & Bernstein) is cited but does not integrate with H-Bar-specific constructs. |

**Composite: (7+9+7+8+8+5)/6 = 44/6 = 7.33 → [QUALIFIES]**

**[HACKATHON PRIORITY]** — C5 = 8

---

## Variant D — Systemic Boundedness + Edge Cases (systemic)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **10** | Highest ODE coherence. Replaces Eq. 48 with the precision-weighted form $1/(1 + CV^2)$ (bounded by construction), adds explicit edge-case handling ($E[\text{score}] = 0 \implies R_A = 0$), and adds a prose guarantee that $V_A \in [0,1]$ from the boundedness of all four factors. The validity function (Eq. 49) now has a formal boundedness proof chain: $CI, FD, DG \in [0,1]$ by definition; $R_A \in [0,1]$ by Eq. 48; therefore $V_A \in [0,1]$. No unclosed variables; no new parameters; all edge cases handled. |
| C2 | **8** | The precision-weighted form ($R_A = \mu^2/(\mu^2 + \sigma^2)$) is cleanly separated from adjacent constructs. It is a signal-to-noise ratio — distinct from test-retest correlation (Variant C), the original CV form, and internal consistency. The edge-case handling ($E[\text{score}] = 0 \implies R_A = 0$) sharpens the boundary: zero-mean benchmarks are explicitly classified as unreliable, which was ambiguous in the original. |
| C3 | **7** | The explicit $CV$ interpretation of the $R_A > 0.75$ threshold ($CV < 0.577$) makes the reliability criterion more concrete and testable. Prediction 7 is marginally sharpened: the validity function's boundedness guarantee means cross-model stability regressions on $V_A$ are well-defined for all possible benchmark scores. The edge-case handling prevents undefined behaviour in empirical tests. |
| C4 | **9** | All three boundaries clean. Single-agent ✓, cognitive bridge ✓ (signal-to-noise ratio is mathematical), version boundary ✓ (V3.0+ variables in V3.0+ equations). The prose addition to Eq. 49 is a definitional clarification, not a structural change. |
| C5 | **8** | The systemic fix directly improves the H-Bar Benchmark Protocol: (1) reliability is guaranteed valid for all benchmarks; (2) the $CV$ interpretation makes the threshold actionable for benchmark designers; (3) edge-case handling prevents protocol failures on degenerate benchmarks. The hackathon tracks can now submit benchmarks with confidence that the reliability component is formally robust. **[HACKATHON PRIORITY]** |
| C6 | **9** | Highest integration score. The fix integrates three locations: §6.1.1 (Eq. 48), §6.1.2 (Eq. 49 prose), and §6.2 (threshold table). The precision-weighted form connects to information-theoretic constructs elsewhere in the paper (entropy-based definitions in §4.1.3, Eq. 29a). The $CV$ interpretation integrates with the parameter groups (Appendix A.2) — $CV$ is a dimensionless ratio analogous to the $\Pi$ groups. The boundedness guarantee propagates to the validity function, creating a closed formal chain. **[INTEGRATION PRIORITY]** |

**Composite: (10+8+7+9+8+9)/6 = 51/6 = 8.50 → [QUALIFIES]**

**[HACKATHON PRIORITY]** — C5 = 8
**[INTEGRATION PRIORITY]** — C6 = 9

---

## Variant E — Conditional Definition + Boundedness Proof (local)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **8** | Adds a domain condition ($CV \leq 1$) to Equation 48 and a boundedness proof to the Appendix. The original functional form ($R_A = 1 - CV^2$) is preserved for valid cases. Benchmarks with $CV > 1$ are assigned $R_A = 0$ by convention. The validity function (Eq. 49) is unaffected for valid benchmarks. The proof in the Appendix formally establishes $R_A \in [0,1]$ for $CV \leq 1$. However, the convention assignment ($R_A = 0$ for $CV > 1$) is ad hoc — it patches the edge case without changing the underlying form, leaving the theoretical gap (why $1 - CV^2$ rather than a bounded form?) unaddressed. |
| C2 | **7** | No conflation introduced. The domain condition ($CV \leq 1$) clarifies the scope of the reliability measure without blurring boundaries with adjacent constructs. The boundedness proof sharpens the distinction between $R_A$ (bounded reliability) and unbounded variance quantities. |
| C3 | **5** | The boundedness proof adds formal rigour but does not sharpen any empirical predictions. The domain condition ($CV \leq 1$) makes the reliability threshold more interpretable but does not make Prediction 7 more testable. The fix is a mathematical correction, not an empirical enhancement. |
| C4 | **9** | All three boundaries clean. Single-agent ✓, cognitive bridge ✓, version boundary ✓. The Appendix addition is a natural extension of the mathematical appendix structure. |
| C5 | **5** | The boundedness proof and domain condition ensure the reliability component is formally valid, which is necessary for hackathon submission. However, the convention assignment ($R_A = 0$ for $CV > 1$) is less elegant than the bounded functional forms (Variants B, D) and does not improve the benchmark protocol's design capabilities. Tangentially related. |
| C6 | **4** | The domain condition and Appendix proof are self-contained additions that do not create cross-version coupling. The proof references the minimum threshold (§6.2) but does not integrate with other framework constructs. Mild version-seam concern: the convention assignment ($R_A = 0$ for $CV > 1$) is an ad hoc boundary that could complicate future extensions. |

**Composite: (8+7+5+9+5+4)/6 = 38/6 = 6.33 → [QUALIFIES]**

---

## Rankings

| Rank | Variant | Composite | Status | Flags |
|------|---------|-----------|--------|-------|
| 1 | **D** (Systemic boundedness + edge cases) | **8.50** | QUALIFIES | [HACKATHON PRIORITY], [INTEGRATION PRIORITY] |
| 2 | **B** (Bounded functional form) | **7.50** | QUALIFIES | — |
| 3 | **C** (Test-retest correlation) | **7.33** | QUALIFIES | [HACKATHON PRIORITY] |
| 4 | **A** (Clamp to [0,1]) | **6.33** | QUALIFIES | — |
| 5 | **E** (Conditional definition + proof) | **6.33** | QUALIFIES | — |

**No variants suppressed** (all composites ≥ 6.0).

---

## TOP 2 VARIANTS — Full Scoring Breakdown

### #1: Variant D — Systemic Boundedness + Edge Cases

| Criterion | Score | Key Rationale |
|-----------|-------|---------------|
| C1 | 10 | Bounded by construction + edge-case handling + formal guarantee chain |
| C2 | 8 | Signal-to-noise ratio cleanly separated; zero-mean edge case sharpened |
| C3 | 7 | $CV$ interpretation makes threshold concrete; prevents undefined behaviour |
| C4 | 9 | All three boundaries clean |
| C5 | 8 | Directly improves benchmark protocol robustness |
| C6 | 9 | Integrates §6.1.1 + §6.1.2 + §6.2; connects to information-theoretic constructs |
| **Composite** | **8.50** | |

### #2: Variant B — Bounded Functional Form

| Criterion | Score | Key Rationale |
|-----------|-------|---------------|
| C1 | 9 | Bounded in $(0,1]$ by construction; smooth; no new parameters |
| C2 | 8 | Signal-to-noise ratio distinct from adjacent constructs; natural midpoint at $CV=1$ |
| C3 | 6 | Marginally improves threshold interpretability |
| C4 | 9 | All three boundaries clean |
| C5 | 7 | Signal-to-noise interpretation actionable for benchmark designers |
| C6 | 6 | Self-contained; mild connections to information-theoretic constructs |
| **Composite** | **7.50** | |

---

## HACKATHON UPDATE:

**Variant D:** Update `hackathon/track_metacognition.md` and other track files to reference the precision-weighted reliability form ($R_A = 1/(1 + CV^2)$) in their benchmark validity specifications. The $CV$ interpretation ($CV < 0.577$ for $R_A > 0.75$) should be noted in the reliability threshold documentation. Edge-case handling ($E[\text{score}] = 0 \implies R_A = 0$) should be documented in the benchmark submission checklist.

**Variant B:** Same hackathon update as D, but without the edge-case handling and threshold reinterpretation — the bounded form alone is sufficient for the protocol.

**Variant C:** Update hackathon track files to note that test-retest correlation is an alternative reliability measure compatible with the H-Bar protocol. The psychometric interpretive benchmarks ($R > 0.7$ = acceptable) should be referenced.

---

## INTEGRATION UPDATE:

**Variant D:**
- Update integration_map.md row for "Benchmark Reliability" to reflect the precision-weighted form (Eq. 48) and the $CV$ interpretation of the minimum threshold.
- Add edge-case handling note to the integration_map.md validity function entry.
- Update integration_map.md to reference the boundedness guarantee chain: $R_A \in [0,1] \implies V_A \in [0,1]$.

**Variant B:**
- Update integration_map.md row for "Benchmark Reliability" to reflect the precision-weighted form (Eq. 48).

**Variant C:**
- Update integration_map.md row for "Benchmark Reliability" to reflect the test-retest correlation form (Eq. 48).

**Variant A:**
- Update integration_map.md row for "Benchmark Reliability" to reflect the clamped form (Eq. 48).

**Variant E:**
- Update integration_map.md row for "Benchmark Reliability" to reflect the domain condition ($CV \leq 1$) and the Appendix boundedness proof.

---

## NEGATIVE LOG:

- **Issue #22, Variant A:** Non-smooth `max(0, ·)` operation creates a boundary discontinuity at $CV = 1$; no cross-version integration; minimal hackathon relevance; patch rather than principled fix.
- **Issue #22, Variant E:** Ad hoc convention assignment ($R_A = 0$ for $CV > 1$) leaves the underlying unbounded form unchanged; no cross-version integration; lower hackathon relevance than Variants B/C/D.

---

## CHECKPOINT RECOMMENDATION:

Not yet at Checkpoint threshold (1st cycle; threshold is every 8th approved edit).
