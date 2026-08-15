# Issue #23 — DEEP AGENT Scoring (MODE 2)

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

## Scoring Matrix

| Variant | C1 | C2 | C3 | C4 | C5 | C6 | **Composite** |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|:---:|
| A (Nagumo proof only) | 8 | 7 | 5 | 10 | 3 | 5 | **6.33** |
| B (Calibration error ODE) | 9 | 8 | 7 | 10 | 5 | 6 | **7.50** |
| C (Saturating nonlinearity) | 7 | 7 | 6 | 9 | 3 | 4 | **6.00** |
| D (Stability analysis) | 10 | 8 | 9 | 10 | 7 | 8 | **8.67** |
| E (Systemic integration) | 10 | 9 | 9 | 10 | 8 | 9 | **9.17** |

**Suppression threshold:** 6.0 — No variants suppressed (all composites ≥ 6.0).

---

## Detailed Scoring

### VARIANT A — Prose-Only Nagumo Proof (local)
| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **8** | No equations changed; Nagumo proof directly closes the boundedness gap for M̂_A. The ODE was already bounded by construction — the proof makes it explicit. However, no calibration error ODE or steady-state analysis; the mechanistic account of why boundedness holds under AI bypass is limited to "because the math works out." |
| C2 | **7** | No conflation introduced. The proof maintains M̂_A's distinctness from σ_A independently. Same Nagumo structure as σ_A and α_A — matches existing practice without strengthening boundary differentiation. Neutral. |
| C3 | **5** | The boundedness proof confirms M̂_A ∈ [0,1] but does not sharpen any §9 predictions or add observable proxies. Supports existing calibration error predictions without generating new testable claims. |
| C4 | **10** | All three boundaries clean. Single-agent ✓, no psychological language (formal Nagumo theorem), no V2.0+ bleed. |
| C5 | **3** | Tangentially related. The proof improves theoretical rigour for the Metacognition track but does not directly improve or enable any benchmark protocol. |
| C6 | **5** | Version-neutral. The proof makes §4.4.2 internally consistent but creates no cross-version coupling or integration across V1.0/V2.0/V3.0 boundaries. |

**Composite: (8+7+5+10+3+5)/6 = 38/6 = 6.33 → [QUALIFIES]**

---

### VARIANT B — Calibration Error ODE + Dual Boundedness (structural)
| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **9** | Adds a derived equation (38a) that closes the calibration error dynamics. Two independent boundedness arguments (direct Nagumo + calibration error relationship) provide redundant verification. The calibration error ODE is derived from existing equations (38, 28, 39) — a mathematical consequence, not an assumption. Highest coherence among structural variants. |
| C2 | **8** | The calibration error ODE (38a) has a distinct structure: restoring term (−ν_M ζ_A) and AI bypass term (−ξ_M Ω_AI (ζ_A + σ_A)) are clearly separated. No conflation with σ_A or α_A. Makes the "distortion" mechanism formally precise — AI bypass enters with a sign that increases ζ_A (overconfidence). Strengthens differentiation. |
| C3 | **7** | The calibration error ODE makes the transient overconfidence mechanism testable: agents with sudden Ω_AI onset should show ζ_A > 0 transiently before correction. However, no new observable proxy or experimental design is added — testability depends on existing Two-Stage Calibration Protocol. |
| C4 | **10** | All three boundaries clean. Derived ODE uses only V2.0 variables. No psychological language. Single-agent formalism. |
| C5 | **5** | The calibration error ODE supports the Metacognition track's "Two-Stage Calibration Protocol" by formalising the transient overconfidence prediction. Tangentially improves benchmark grounding but doesn't directly produce a new protocol design. |
| C6 | **6** | The calibration error ODE connects §4.4.1 (calibration error definition) to §4.4.2 (self-model ODE) and implicitly to §4.1.2 (schema coherence ODE via σ_A terms). Creates internal integration within §4.4 but doesn't cross version boundaries. |

**Composite: (9+8+7+10+5+6)/6 = 45/6 = 7.50 → [QUALIFIES]**

---

### VARIANT C — Saturating Nonlinearity (structural)
| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **7** | Modifies Equation 39's functional form. The new form is bounded (Nagumo holds) and the distortion term vanishes at both boundaries, providing structural robustness. However, the modification changes the ODE's linear structure — affects the steady-state analysis (Variant D's key insight) and the dimensionless parameter group Π_7 interpretation. Linear eigenvalue analysis no longer applies. Partial coherence gain offset by structural change cost. |
| C2 | **7** | The (1 − M̂_A) factor creates a natural interpretation: AI bypass distortion is strongest at intermediate self-model values and weakest at extremes. Distinct from other ODE terms; no conflation introduced. However, modifies existing ODE rather than adding to it, which changes the boundary behavior of the distortion term. |
| C3 | **6** | The nonlinear form predicts that overconfidence dynamics are strongest at intermediate M̂_A values (matching Dunning-Kruger). Testable but requires more complex experimental design than the linear form's predictions. |
| C4 | **9** | Single-agent ✓, no psychological language ✓, version boundary: mild concern. Modifies Equation 39 (V2.0) but uses only V2.0 variables. Clean on all three counts, but modifying an existing ODE is more invasive than adding prose. |
| C5 | **3** | Tangentially related. The nonlinear form could improve benchmark predictions but doesn't directly enable new protocol design. |
| C6 | **4** | Negative impact. Modifying Equation 39 changes the linear structure that Π_7 = ν_M/ξ_M was derived for. The steady-state analysis (39a) from Variant D no longer applies in the same form. Deepens version seam by creating a nonlinear ODE whose properties differ from the linear form documented elsewhere. |

**Composite: (7+7+6+9+3+4)/6 = 36/6 = 6.00 → [QUALIFIES] (borderline)**

---

### VARIANT D — Stability Analysis via Dimensionless Groups (structural)
| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **10** | Nagumo proof + steady-state analysis (39a) + convergence rate characterisation. The steady-state result M̂_A* ≤ σ_A is stronger than M̂_A* ≤ 1 — the self-model never exceeds true schema coherence at equilibrium. Convergence rate (eigenvalue −(ν_M + ξ_M Ω_AI)) confirms exponential convergence. Dimensionless group Π_7 = ν_M/ξ_M is now analysed, completing its theoretical account. Highest coherence. |
| C2 | **8** | The steady-state result M̂_A* ≤ σ_A provides a sharp differentiation: at equilibrium, the self-model is strictly ≤ schema coherence. Sustained AI bypass produces underconfidence, not overconfidence — counterintuitive but mathematically precise. Strengthens the boundary between M̂_A and σ_A. |
| C3 | **9** | The steady-state prediction M̂_A* < σ_A under sustained Ω_AI exposure is directly testable: expose agents to sustained AI-assisted evaluation, wait for equilibration, measure M̂_A calibration. H-Bar predicts underconfidence at steady state. Novel, falsifiable prediction not derivable from δ-only accounts. |
| C4 | **10** | All three boundaries clean. Uses only existing variables and the already-declared dimensionless group Π_7. No new parameters. No psychological language. |
| C5 | **7** | The steady-state prediction M̂_A* < σ_A under sustained Ω_AI directly improves the Metacognition track's "Two-Stage Calibration Protocol" benchmark: the protocol can now test for equilibration behavior, not just transient overconfidence. Directly improves an existing benchmark protocol. |
| C6 | **8** | The steady-state analysis connects Π_7 (Appendix A.2, V3.0+) to the self-model ODE (§4.4.2, V2.0). Creates cross-version coupling between the dimensionless parameter taxonomy and metacognitive dynamics. The convergence rate analysis also connects to the timescale separation hierarchy (§10.3, Category A issue). |

**Composite: (10+8+9+10+7+8)/6 = 52/6 = 8.67 → [QUALIFIES]**

---

### VARIANT E — Systemic Boundedness Integration (systemic)
| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **10** | All three components: Nagumo proof + steady-state analysis + calibration error ODE. The coupled system is fully closed. Calibration error ODE (38a) derived from existing equations. Steady-state result M̂_A* ≤ σ_A proven. Appendix A.1 updated with new ODE. Highest coherence. |
| C2 | **9** | The calibration error ODE (38a) has a unique structure: restoring term (−ν_M ζ_A) opposes overconfidence; AI bypass terms inflate it. The steady-state result M̂_A* ≤ σ_A is a strong differentiation: self-model bounded by schema coherence, not just by 1. The mechanistic account of "distortion" is formally precise. Strongest differentiation. |
| C3 | **9** | The steady-state prediction M̂_A* < σ_A under sustained Ω_AI is directly testable. The calibration error ODE predicts transient overconfidence followed by equilibration to underconfidence. The hackathon benchmark update operationalises this as a new protocol design. Sharpest falsifiability. |
| C4 | **10** | All three boundaries clean. Uses only existing variables. No psychological language. Single-agent formalism. Appendix update is a natural extension. |
| C5 | **8** | The hackathon benchmark update directly operationalises the steady-state prediction as a new testable protocol in track_metacognition.md. The "sustained AI bypass → underconfidence at equilibrium" prediction is a novel benchmark design that improves the Metacognition track. |
| C6 | **9** | Integrates four locations: §4.4.1 (calibration error ODE), §4.4.2 (Nagumo + steady-state), Appendix A.1 (system listing), and hackathon/track_metacognition.md (benchmark update). Creates cross-reference coupling between V2.0 metacognitive variables and V3.0+ appendix structure. Calibration error ODE (38a) connects to schema coherence ODE (28) via shared σ_A and Ω_AI terms. Highest integration. |

**Composite: (10+9+9+10+8+9)/6 = 55/6 = 9.17 → [QUALIFIES]**

**[HACKATHON PRIORITY]** — C5 = 8
**[INTEGRATION PRIORITY]** — C6 = 9

---

## Top 2 Variants

### 🥇 Variant E — Systemic Boundedness Integration
**Composite: 9.17** | C5 = 8 | C6 = 9

**Why it wins:** Highest overall composite (9.17). The only variant flagged both [HACKATHON PRIORITY] and [INTEGRATION PRIORITY]. Provides the complete boundedness account: Nagumo proof + steady-state analysis (M̂_A* ≤ σ_A) + calibration error ODE (38a) + Appendix A.1 integration + hackathon benchmark update. The steady-state result — that sustained AI bypass produces underconfidence, not overconfidence — is the key theoretical insight that drives both the falsifiability score (C3 = 9) and the hackathon relevance (C5 = 8). The calibration error ODE connects V2.0 metacognitive dynamics to the V3.0+ appendix structure.

**Scoring breakdown:** C1=10, C2=9, C3=9, C4=10, C5=8, C6=9

---

### 🥈 Variant D — Stability Analysis via Dimensionless Groups
**Composite: 8.67** | C5 = 7 | C6 = 8

**Why it's second:** Second-highest composite (8.67). Provides the steady-state analysis and Nagumo proof without the calibration error ODE or hackathon update — a more focused structural fix. The M̂_A* ≤ σ_A result is the same as Variant E's key insight, making this a strong alternative if the systemic scope of E is too invasive. The dimensionless group Π_7 analysis completes the theoretical account declared in Appendix A.2.

**Scoring breakdown:** C1=10, C2=8, C3=9, C4=10, C5=7, C6=8

---

## HACKATHON UPDATE:

**Variant E:** Update `hackathon/track_metacognition.md` §2 (Benchmark Designs) — add a new sub-prediction to the "Two-Stage Calibration Protocol":

> **Equilibration Prediction:** H-Bar predicts that agents with sustained AI bypass exposure (Ω_AI > 0 maintained over multiple evaluation cycles) will converge to M̂_A* = σ_A/(1 + Ω_AI/Π_7) < σ_A — i.e., underconfidence at steady state. This is the opposite of the transient overconfidence (ζ_A > 0) predicted immediately after AI bypass onset. The Two-Stage Calibration Protocol should include a third stage: after Stage 2 (complete OOD items), administer a second Stage 1 prediction. H-Bar predicts the second prediction will show ζ_A < 0 (underconfidence) if Ω_AI exposure was sustained between stages.

**Variant D:** No direct hackathon update — the stability analysis improves theoretical grounding but doesn't generate a new benchmark protocol design beyond what existing §4.4.3 benchmarks already specify.

**Variant B:** No hackathon update needed.

**Variant A:** No hackathon update needed.

**Variant C:** No hackathon update needed.

---

## INTEGRATION UPDATE:

**Variant E:**
- Update `integration_map.md` row for "Metacognitive Self-Model ODE" to reflect: (a) Nagumo boundedness proof now present, (b) calibration error ODE (Eq. 38a) added, (c) steady-state analysis (Eq. 39a) showing M̂_A* ≤ σ_A.
- Update `integration_map.md` row for "Dimensionless Parameter Groups" to reflect: Π_7 = ν_M/ξ_M now analysed with steady-state interpretation.
- Add new `integration_map.md` row: "Calibration Error ODE" linking §4.4.1 → Eq. 38a → App. A.1 → Hackathon Metacognition track.

**Variant D:**
- Update `integration_map.md` row for "Metacognitive Self-Model ODE" to reflect: (a) Nagumo boundedness proof, (b) steady-state analysis (Eq. 39a) showing M̂_A* ≤ σ_A, (c) convergence rate analysis.
- Update `integration_map.md` row for "Dimensionless Parameter Groups" to reflect: Π_7 now analysed with steady-state interpretation.

**Variant B:**
- Update `integration_map.md` row for "Metacognitive Self-Model ODE" to reflect: calibration error ODE (Eq. 38a) added with dual boundedness argument.

**Variant A:**
- Update `integration_map.md` row for "Metacognitive Self-Model ODE" to reflect: Nagumo boundedness proof now present.

**Variant C:**
- Update `integration_map.md` row for "Metacognitive Self-Model ODE" to reflect: Equation 39 modified with saturating nonlinearity. Note: affects Π_7 interpretation.

---

## NEGATIVE LOG:

**Issue #23, Variant C:** Modifies Equation 39's linear structure, affecting the steady-state analysis (Eq. 39a) and dimensionless group Π_7 interpretation; reduces version integration (C6 = 4). Boundedness is achieved structurally but at the cost of ODE system coherence. Borderline composite (6.00).

---

## CHECKPOINT RECOMMENDATION:

Not yet at Checkpoint threshold (1st cycle; threshold is every 8th approved edit).
