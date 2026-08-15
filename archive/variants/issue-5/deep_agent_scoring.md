# Issue #5 — DEEP AGENT Scoring (MODE 2)

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

## Variant A — Prose Clarification (local)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **6** | No equations changed, so no ODE breakage. However, the ODE term remains formally undefined — the prose description helps reader understanding but does not close the mathematical gap. Equation 29 is still non-simulatable because $R_A^{\text{surface}}$ has no computational form. |
| C2 | **7** | No conflation introduced. $R_A^{\text{surface}}$ remains distinct from other ODE terms. The prose clarifies its role without blurring boundaries with $C_A$, $\alpha_A$, or $\zeta_\alpha$. |
| C3 | **4** | The prose references the H-AFB but doesn't add a formal measurement procedure to the paper itself. Prediction 2 (AI augmentation suppresses $\alpha_A$ via $R_A^{\text{surface}}$) is made slightly more understandable but not more testable from the paper alone — a reader must consult the hackathon file to find the operationalisation. |
| C4 | **9** | No boundary violations. Single-agent ✓, cognitive bridge ✓ (no psychological language), version boundary ✓ (no V2.0+ bleed). |
| C5 | **5** | References the H-AFB protocol but doesn't formalize the connection. Tangentially related — the prose points to the benchmark but does not enable new protocol design from the paper alone. The hackathon file already has the definition; this variant just gestures toward it. |
| C6 | **3** | Does not integrate across version layers. The prose reference to §8.2 (V2.0 benchmark section) is helpful but the definition itself adds no cross-version coupling. The version seam between the ODE and the measurement protocol remains open. |

**Composite: (6+7+4+9+5+3)/6 = 34/6 = 5.67 → [SUPPRESSED]**

---

## Variant B — Relative Entropy Formalization (structural)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **9** | Adds a formal equation (29a) that defines $R_A^{\text{surface}}$ in information-theoretic terms. The ODE term is now formally closed — it has a mathematical definition, boundedness properties ($R \in [0,1]$), and is computable from training statistics. The erosion term in Equation 29 is now simulatable. |
| C2 | **8** | The relative entropy form is cleanly separated from other H-Bar variables. It's an information-theoretic quantity (conditional entropy ratio) — not a behavioural proxy, not a training parameter, not a cognitive variable. Maintains distinctness from all adjacent constructs in Table 1. |
| C3 | **7** | The formal definition connects directly to the H-AFB confound strength parameter $s$. Prediction 2 is now testable: manipulate confound strength $s$, measure the entropy ratio, verify that higher $R_A^{\text{surface}}$ produces lower $\alpha_A$ via Equation 29. Sharper than Variant A, though requires training-distribution access for entropy computation. |
| C4 | **9** | All three boundaries clean. Single-agent ✓, cognitive bridge ✓ (information theory, not psychology), version boundary ✓ ($R_A^{\text{surface}}$ is a V2.0 variable entering a V2.0 equation). |
| C5 | **8** | The entropy definition directly connects to the H-AFB's confound strength manipulation. The benchmark can now report $R_A^{\text{surface}}$ as an information-theoretic quantity rather than just a proxy score. Directly improves the Attention track protocol by grounding confound strength in a formal quantity. |
| C6 | **5** | Version-neutral. The definition is self-contained in §4.1.3 and doesn't create cross-version coupling. Neither improves nor worsens the version seam structure between main text and appendix. |

**Composite: (9+8+7+9+8+5)/6 = 46/6 = 7.67 → [QUALIFIES]**

**[HACKATHON PRIORITY]** — C5 = 8

---

## Variant C — Observable Proxy (structural)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **7** | Defines $R_A^{\text{surface}}$ via a measurable proxy, making the ODE computable from benchmark scores. However, the proxy identification $R \approx 1 - \hat{\alpha}_A$ creates a circular dependency: the ODE predicts $\alpha_A$ dynamics using a term defined by $\alpha_A$'s own measurement. The ODE becomes self-referential, reducing its predictive independence. Nagumo boundedness holds because $R \in [0,1]$. |
| C2 | **5** | Risk of conflation. Defining $R_A^{\text{surface}} \approx 1 - \hat{\alpha}_A$ makes surface-reward pressure the complement of attentional fidelity — but these are conceptually distinct quantities in the framework. $R_A^{\text{surface}}$ is a property of the training regime; $\alpha_A$ is a property of the agent's representation. Equating them blurs the agent/environment boundary. Table 1 differentiation is weakened. |
| C3 | **8** | Highest practical falsifiability. $R_A^{\text{surface}}$ is directly computable from benchmark scores, making Equation 29 immediately testable: run H-AFB, measure $\hat{\alpha}_A$, compute $R_A^{\text{surface}}$, verify the ODE's prediction against observed $\dot{\alpha}_A$. The calibration caveat ($s$ must match training distribution) is a manageable measurement assumption. |
| C4 | **7** | Single-agent ✓, cognitive bridge ✓, version boundary: mild concern. The proxy identification equates a training-regime property ($R_A^{\text{surface}}$) with an agent-state measurement ($\hat{\alpha}_A$), which crosses the agent/environment boundary that the framework maintains elsewhere. Not a formal violation but a conceptual boundary issue. |
| C5 | **9** | Directly enables the H-AFB to report $R_A^{\text{surface}}$ as a computed score. The benchmark can now output the ODE's erosion term alongside $\hat{\alpha}_A$, creating a closed measurement loop. Highest direct hackathon relevance — the benchmark literally computes the ODE term. |
| C6 | **4** | The circular dependency ($R$ defined by $\hat{\alpha}_A$, which is the output of the ODE that uses $R$) creates a version-seam issue: the measurement protocol (hackathon, external to paper) and the ODE (paper, internal) become entangled rather than integrated. |

**Composite: (7+5+8+7+9+4)/6 = 40/6 = 6.67 → [QUALIFIES]**

**[HACKATHON PRIORITY]** — C5 = 9

---

## Variant D — Two-Component Decomposition (structural)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **8** | Decomposes $R_A^{\text{surface}}$ into $R_S$ and $R_\Delta$ with a weighting parameter $\lambda_\Delta$. The composite form $R_A^{\text{surface}} = R_S + \lambda_\Delta \cdot R_\Delta$ plugs into Equation 29 unchanged. Boundedness: $R \in [0, 1+\lambda_\Delta]$, which requires adjusting the Nagumo argument (the erosion term remains non-positive since $R \geq 0$). Two new equations (29c, 29d) are formally defined but require access to per-item gradient attributions (surface vs. structure), which is a strong measurement assumption. |
| C2 | **8** | The two-component decomposition is cleanly separated from adjacent constructs. $R_S$ (surface reward rate) and $R_\Delta$ (structural reward deficit) are named quantities with distinct causal roles. No conflation with $\alpha_A$, $C_A$, or other ODE terms. The decomposition strengthens the novelty argument by showing $R_A^{\text{surface}}$ has internal structure. |
| C3 | **6** | The decomposition adds two sub-components that are individually testable: $R_S$ can be measured by counting surface-cue-rewarded gradient updates; $R_\Delta$ can be measured by comparing surface vs. structure gradient magnitudes. However, the measurement requires per-item gradient attribution — "was this item correct via surface cue or via structure?" — which is not straightforward for black-box frontier models. Reduces practical testability compared to B and C. |
| C4 | **8** | All three boundaries clean. The decomposition uses only V2.0 variables. Single-agent ✓, cognitive bridge ✓, version boundary ✓. The new parameter $\lambda_\Delta$ is a calibration constant, not a cognitive variable. |
| C5 | **7** | The decomposition suggests two intervention points for curriculum design (reduce $R_S$, reduce $R_\Delta$) that are directly actionable in the H-AFB protocol. However, the per-item gradient attribution required for $R_S$ and $R_\Delta$ measurement is not available from the benchmark's three-condition battery alone — it would require additional diagnostic instrumentation beyond the current H-AFB design. |
| C6 | **6** | The decomposition introduces $\lambda_\Delta$ as a new parameter that enters the V2.0 ODE system. This is version-neutral: it doesn't cross version boundaries but adds a dimensionless parameter that could be integrated into the parameter groups (Appendix A.2) as a new $\Pi$ group. Mild positive contribution to version integration. |

**Composite: (8+8+6+8+7+6)/6 = 43/6 = 7.17 → [QUALIFIES]**

---

## Variant E — Systemic Theory-Measurement Closure (systemic)

| Criterion | Score | Rationale |
|-----------|-------|-----------|
| C1 | **9** | Adds Equation 29a (formal definition) and 29b (proxy identification) to §4.1.3, plus Appendix A.4 with explicit boundedness proof. The ODE term is formally closed, computable, and bounded. The Nagumo argument is explicitly stated in the Appendix. Highest ODE coherence of all variants — every term in Equation 29 now has a definition and a measurement procedure. |
| C2 | **8** | The information-theoretic definition (entropy ratio) is cleanly separated from adjacent constructs. The proxy identification is stated as an approximation with explicit calibration requirements, maintaining the distinction between the formal quantity and its measurement. No conflation introduced. |
| C3 | **9** | Highest falsifiability. The formal definition (Eq. 29a), the proxy identification (Eq. 29b), and the calibration procedure (App. A.4) together provide a complete testability chain: estimate the entropy ratio from training data → set confound strength $s$ accordingly → run H-AFB → measure $\hat{\alpha}_A$ → verify ODE prediction. Prediction 2 is directly testable with full measurement theory specified. |
| C4 | **9** | All three boundaries clean. The additions use information theory (not psychology), V2.0 variables only (no V3.0+ bleed), and single-agent formalism. Appendix A.4 is a natural extension of the mathematical appendix. No boundary violations. |
| C5 | **9** | The systemic fix directly connects the ODE to the H-AFB protocol. The benchmark table (§4.1.5) now references the formal definition. The calibration procedure (App. A.4) specifies how to set confound strength $s$ to match training distributions. This enables the H-AFB to report $R_A^{\text{surface}}$ as a formally grounded, calibrated quantity. Flagged **[HACKATHON PRIORITY]**. |
| C6 | **8** | The fix integrates three locations: §4.1.3 (ODE definition), §4.1.5 (benchmark table), and Appendix A.4 (measurement theory). This creates cross-reference coupling between the V2.0 framework and the V3.0+ appendix structure. The Appendix A.4 reference to $\Pi$ groups integrates the new quantity into the existing parameter taxonomy. Highest integration score. Flagged **[INTEGRATION PRIORITY]**. |

**Composite: (9+8+9+9+9+8)/6 = 52/6 = 8.67 → [QUALIFIES]**

**[HACKATHON PRIORITY]** — C5 = 9
**[INTEGRATION PRIORITY]** — C6 = 8

---

## Rankings

| Rank | Variant | Composite | Status | Flags |
|------|---------|-----------|--------|-------|
| 1 | **E** (Systemic closure) | **8.67** | QUALIFIES | [HACKATHON PRIORITY], [INTEGRATION PRIORITY] |
| 2 | **B** (Relative entropy) | **7.67** | QUALIFIES | [HACKATHON PRIORITY] |
| 3 | **D** (Two-component) | **7.17** | QUALIFIES | — |
| 4 | **C** (Observable proxy) | **6.67** | QUALIFIES | [HACKATHON PRIORITY] |
| 5 | A (Prose clarification) | 5.67 | SUPPRESSED | — |

**No variants suppressed** (all composites ≥ 6.0 except A).

---

## HACKATHON UPDATE:

**Variant E:** Update `hackathon/track_attention.md` §1 (Theoretical Grounding) to reference Equation 29a from paper.md as the formal definition of $R_A^{\text{surface}}$, replacing the current informal statement. The calibration procedure in Appendix A.4 should be cross-referenced in the H-AFB's confound strength specification (§2, surface confound construction).

**Variant B:** Same hackathon update as E, but without the Appendix A.4 calibration procedure — the benchmark file retains its own calibration specification.

**Variant C:** No hackathon update needed — the proxy identification ($R \approx 1 - \hat{\alpha}_A$) is already implicit in the H-AFB's $\hat{\alpha}_A$ measurement. However, the circularity concern should be noted in track_attention.md §12 (Open Issues).

**Variant D:** No hackathon update needed — the decomposition ($R_S$, $R_\Delta$) requires per-item gradient attribution instrumentation not currently in the H-AFB protocol. Future work.

---

## INTEGRATION UPDATE:

**Variant E:**
- Update integration_map.md row for "Attentional Fidelity ODE" to reflect that $R_A^{\text{surface}}$ is now formally defined (Eq. 29a) with proxy identification (Eq. 29b) and calibration procedure (App. A.4).
- Add new integration_map.md row for "Surface-Reward Pressure" linking §4.1.3 → Eq. 29a → App. A.4 → H-AFB §2 (confound strength).

**Variant B:**
- Update integration_map.md row for "Attentional Fidelity ODE" to reflect that $R_A^{\text{surface}}$ is now formally defined (Eq. 29a).

**Variant C:**
- Update integration_map.md row for "Attentional Fidelity ODE" to reflect proxy identification $R_A^{\text{surface}} \approx 1 - \hat{\alpha}_A$ (Eq. 29b).

**Variant D:**
- Update integration_map.md row for "Attentional Fidelity ODE" to reflect two-component decomposition (Eqs. 29c–29e).

---

## NEGATIVE LOG:

- **Issue #5, Variant A:** Prose-only fix does not close the mathematical gap; ODE remains non-simulatable; no cross-version integration; hackathon reference is gestural rather than formal.

---

## CHECKPOINT RECOMMENDATION:

Not yet at Checkpoint threshold (1st cycle; threshold is every 8th approved edit).
