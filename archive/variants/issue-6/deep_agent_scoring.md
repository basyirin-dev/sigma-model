# DEEP AGENT Scoring — Issue #6

**Date:** 2026-03-30
**Issue:** Optimal sub-state values for the executive control ODE are not formally defined for each of the five training phases.

---

## Scoring Matrix

| Variant | C1 | C2 | C3 | C4 | C5 | C6 | **Composite** |
|---------|:--:|:--:|:--:|:--:|:--:|:--:|:---:|
| A (Lookup table §4.3.2) | 8 | 7 | 7 | 10 | 8 | 5 | **7.50** |
| B (Embedded in §7) | 7 | 7 | 7 | 10 | 8 | 6 | **7.50** |
| C (Monotonic formulas) | 9 | 6 | 8 | 10 | 8 | 8 | **8.17** |
| D (Bifurcation step functions) | 8 | 7 | 9 | 10 | 9 | 8 | **8.50** |
| E (ODE replacement) | 9 | 8 | 8 | 9 | 8 | 8 | **8.33** |

**Suppression threshold:** 6.0 — No variants suppressed.

---

## Detailed Scoring

### VARIANT A — Lookup Table in §4.3.2
| Criterion | Score | Rationale |
|-----------|:-----:|-----------|
| C1 ODE Coherence | 8 | Explicitly defines P*, I*, F* → closes Eq. 36 gap. No new equations or variables. Table is external to the ODE system (not derived), reducing tightness. |
| C2 Novelty Defence | 7 | P*, I*, F* remain distinct sub-components. No conflation introduced. Neutral — maintains existing boundaries without strengthening them. |
| C3 Falsifiability | 7 | Enables §4.3.3 executive control benchmarks by providing concrete targets. Supports Prediction 5 (Phase 3 compression) testing. |
| C4 Scope Discipline | 10 | All three boundaries clean: single-agent, no psychological language, no V1.0 equation modification. |
| C5 Hackathon Relevance | 8 | Directly enables Executive Functions track — "Multi-Step Training Plan Tasks" and "Inhibitory Conflict Tasks" now have formal targets. |
| C6 Version Integration | 5 | Version-neutral — doesn't connect V1.0 and V2.0 variables. Standalone table with no cross-version coupling. |
| **Composite** | **7.50** | |

### VARIANT B — Embedded in §7 Phase Descriptions
| Criterion | Score | Rationale |
|-----------|:-----:|-----------|
| C1 ODE Coherence | 7 | Same values as A but distributed across 5 locations. Cross-reference burden slightly reduces system coherence. |
| C2 Novelty Defence | 7 | Identical values to A. Same boundary maintenance. |
| C3 Falsifiability | 7 | Same benchmark enablement as A. |
| C4 Scope Discipline | 10 | All three boundaries clean. Appending to existing phase descriptions preserves existing structure. |
| C5 Hackathon Relevance | 8 | Same benchmark enablement as A. |
| C6 Version Integration | 6 | Slight improvement over A — embedding in §7 (which spans all versions) creates implicit cross-version reference. |
| **Composite** | **7.50** | |

### VARIANT C — Monotonic Derivation Formulas
| Criterion | Score | Rationale |
|-----------|:-----:|-----------|
| C1 ODE Coherence | 9 | Formally closed — Eqs. 36a–36c use only existing variables. Self-contained derivation. Smooth phase transitions. |
| C2 Novelty Defence | 6 | P* = 1 − δ_A^rel creates a direct dependency on depth, risking partial conflation of planning with depth tracking. I* = max(0, 1 − σ_A/σ_critical) links inhibition to schema coherence — expected coupling but tight. |
| C3 Falsifiability | 8 | Continuous formulas enable finer-grained predictions. Can test whether P*, I*, F* follow monotonic patterns empirically. |
| C4 Scope Discipline | 10 | All three boundaries clean. Uses only V1.0/V2.0 variables already in the system. |
| C5 Hackathon Relevance | 8 | Continuous formulas could generate parameterised difficulty curves for executive control benchmarks. |
| C6 Version Integration | 8 | Uses V1.0 variables (δ_A^rel, σ_A) to derive V2.0 executive control targets — strengthens V1.0→V2.0 coupling. |
| **Composite** | **8.17** | |

### VARIANT D — Bifurcation-Aware Step Functions **[HACKATHON PRIORITY]**
| Criterion | Score | Rationale |
|-----------|:-----:|-----------|
| C1 ODE Coherence | 8 | Formally closed with Eqs. 36a–36c. Step discontinuity in I* at σ_critical is smoothed by ODE relaxation — architecturally sound but adds discontinuity to forcing terms. |
| C2 Novelty Defence | 7 | Step functions reinforce the σ_A/Ξ_A^I boundary through the σ_critical threshold. F* uses |M_A| and Ψ_A — maintains distinctness. |
| C3 Falsifiability | 9 | The step function at σ_critical is directly testable: "Does inhibitory behaviour change sharply at schema crystallisation?" This operationalises the "Latent Threshold Detection" benchmark (§4.3.3) with a formal prediction. |
| C4 Scope Discipline | 10 | All three boundaries clean. Bifurcation at σ_critical is already derived in Appendix A.3 (Eq. A.15). |
| C5 Hackathon Relevance | 9 | **Directly operationalises the "Latent Threshold Detection" benchmark.** The step function at σ_critical is a falsifiable benchmark design: test whether agents adapt inhibitory behaviour at the schema crystallisation threshold without explicit signal. |
| C6 Version Integration | 8 | Connects σ_critical (V1.0 bifurcation from Eq. A.15) to Ξ_A^I (V2.0 executive control) — explicit cross-version coupling. |
| **Composite** | **8.50** | |

### VARIANT E — ODE Replacement (Systemic)
| Criterion | Score | Rationale |
|-----------|:-----:|-----------|
| C1 ODE Coherence | 9 | Fully self-contained — no undefined quantities. Coupling-driven ODE is architecturally consistent with all other ODEs in the system (δ_A, σ_A, α_A, M̂_A). |
| C2 Novelty Defence | 8 | Unique architecture (domain-averaged coupling) makes Ξ_A fundamentally different from other variables. Strengthens distinctness. |
| C3 Falsifiability | 8 | Domain-averaged dynamics are testable. Self-contained ODE is simulatable for benchmark generation. |
| C4 Scope Discipline | 9 | Minor concern: domain-averaging $\barδ_A^{rel}$ introduces implicit multi-domain coupling not present in the original single-domain Ξ_A specification. Otherwise clean on all three boundaries. |
| C5 Hackathon Relevance | 8 | Self-contained ODE generates synthetic training data for executive control benchmarks. Simulatable without external lookup. |
| C6 Version Integration | 8 | Domain-averaged variables span all domains — strengthens cross-domain integration. Modifies Eq. 36 (V2.0) substantially but consistently. |
| **Composite** | **8.33** | |

---

## Top 2 Variants

### 🥇 Variant D — Bifurcation-Aware Step Functions [HACKATHON PRIORITY]
**Composite: 8.50** | C5 = 9

**Why it wins:** Best falsifiability score (C3 = 9) — the step function at σ_critical is directly testable as a benchmark prediction. Highest hackathon relevance (C5 = 9) — directly operationalises the "Latent Threshold Detection" benchmark from §4.3.3. Clean scope discipline (C4 = 10). Strong version integration (C6 = 8) by connecting V1.0's σ_critical bifurcation to V2.0's executive control.

**Scoring breakdown:** C1=8, C2=7, C3=9, C4=10, C5=9, C6=8

---

### 🥈 Variant E — ODE Replacement (Systemic)
**Composite: 8.33** | C6 = 8

**Why it's second:** Strongest ODE coherence (C1 = 9) — eliminates the undefined quantity at the architectural level. Strongest novelty defence (C2 = 8) — unique domain-averaging architecture. Minor scope discipline concern (C4 = 9) due to implicit multi-domain coupling.

**Scoring breakdown:** C1=9, C2=8, C3=8, C4=9, C5=8, C6=8

---

## HACKATHON UPDATE:
**Variant D:** The "Latent Threshold Detection" benchmark in `hackathon/track_executive.md` should be updated with a formal prediction: "H-Bar predicts that executive inhibition $Ξ_A^I$ will transition from 0.9 to 0.4 when σ_A crosses σ_critical, without explicit signal. Testable via inhibitory conflict tasks with hidden threshold." This directly operationalises Eq. 36b (step function).

**Variant E:** No direct hackathon update — the ODE replacement improves internal consistency but does not generate new benchmark designs beyond what existing §4.3.3 benchmarks already specify.

## INTEGRATION UPDATE:
**Variant D:** Update `integration_map.md` — row for Executive Functions track should note: "Eq. 36b links Ξ_A^I to σ_critical bifurcation (Appendix A.3, Eq. A.15). Cross-version coupling established: V1.0 σ_critical → V2.0 Ξ_A^I."

**Variant E:** Update `integration_map.md` — row for Executive Functions track should note: "Eq. 36 rewritten as self-contained coupling-driven ODE. Domain-averaged δ_A^rel and σ_A replace external P*, I*, F* specification."

## NEGATIVE LOG:
**Variant A:** Static lookup table provides values but does not derive them from the model's state — external specification remains, limiting integration depth.
**Variant B:** Same values as A distributed across §7; reduced cross-reference locality without compensating integration gain.
**Variant C:** Monotonic formulas risk conflating P* with depth tracking (P* = 1 − δ_A^rel) — C2 penalty relative to D and E.

## CHECKPOINT RECOMMENDATION:
Not yet at Checkpoint threshold (edit count: 0).
