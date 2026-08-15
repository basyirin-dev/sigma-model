# Issue #5 — Variant Proposals (MODE 1: FAST AGENT)

## Issue Summary

**Issue #:** 5
**Tag:** Tier 1A [HACKATHON PRIORITY]
**Description:** The attentional fidelity ODE (Equation 29) relies on surface-reward pressure $R_A^{\text{surface}}(d,t)$ which currently lacks a formal definition or measurement procedure in paper.md.

**Core problem:** Equation 29 defines:
$$\dot{\alpha}_A(d,t) = \gamma \cdot C_A(d,t) \cdot (1 - \alpha_A(d,t)) - \zeta_{\alpha} \cdot \alpha_A(d,t) \cdot R_A^{\text{surface}}(d,t) \tag{29}$$

But the table entry for $R_A^{\text{surface}}(d,t)$ reads only: "Surface-reward pressure — training signal rewarding surface accuracy." No mathematical definition, no measurement procedure, no connection to observables. The hackathon file (track_attention.md §1) proposes a relative entropy definition, but this has not been propagated to the paper.

---

### VARIANT A
**Issue #:** 5
**Tag:** Tier 1A
**Section targeted:** §4.1.3 (table after Equation 29, prose clarification)
**Scope:** local

**DIAGNOSIS:** The table entry for $R_A^{\text{surface}}(d,t)$ is a gloss — it names the quantity but provides no formal content. A reader of §4.1.3 cannot derive what $R_A^{\text{surface}}$ means, how to compute it, or how it connects to the benchmark protocol. This makes the entire attentional fidelity ODE non-simulatable: every other term in Equation 29 is defined, but the erosion term is opaque.

**PROPOSED FIX:**

*Old table entry:*
| $R_A^{surface}(d,t)$ | Surface-reward pressure — training signal rewarding surface accuracy |

*New table entry:*
| $R_A^{surface}(d,t)$ | Surface-reward pressure — the degree to which the training signal rewards correct outputs derivable from surface-feature co-occurrence rather than from compositional rule application. Formally: the conditional probability that a training update reinforces surface-feature associations when both surface and structural cues predict the correct output. Measurable via the surface-conflict drop $\Delta_{\text{surf}} = \text{Acc}_{ID} - \text{Acc}_{OOD\text{-surf-conflict}}$ in the H-AFB protocol (§8.2, Attention track). High $R_A^{\text{surface}}$ means the training regime preferentially rewards surface accuracy; low $R_A^{\text{surface}}$ means the training signal is agnostic or structurally weighted. |

*Add prose after Equation 29:* "Surface-reward pressure $R_A^{\text{surface}}(d,t)$ quantifies the degree to which the training signal reinforces surface-feature associations over compositional-structure application. In training regimes where surface tokens (e.g., lexical items, formatting patterns, salient features) co-occur with correct outputs at high base rates, $R_A^{\text{surface}}$ is elevated; in regimes requiring compositional discrimination for reward, $R_A^{\text{surface}}$ is reduced. The H-AFB benchmark (§8.2) operationalises this via confound strength $s$, which controls the entropy ratio between surface and structural features."

**JUSTIFICATION:** This fix provides a qualitative definition and a measurement reference without changing any equation. The ODE remains Equation 29 as written; the reader now understands what $R_A^{\text{surface}}$ represents and where to find its operationalisation. The connection to the H-AFB benchmark (already designed in track_attention.md) is made explicit. No downstream equation is affected.

**SAFETY NOTE:** This fix deliberately does NOT change Equation 29, Equation 28, Equation 19/A.10, Table 1, §7.1–7.5 phase triggers, or the Burnell et al. citation. It modifies only the gloss table entry and adds prose clarification in §4.1.3.

---

### VARIANT B
**Issue #:** 5
**Tag:** Tier 1A
**Section targeted:** §4.1.3 (Equation 29 + new equation definition)
**Scope:** structural

**DIAGNOSIS:** The gloss table entry cannot substitute for a formal equation. To make the ODE simulatable, $R_A^{\text{surface}}(d,t)$ requires a mathematical expression in terms of quantities that are either directly measurable or derivable from training statistics. The hackathon file (track_attention.md §1) proposes a relative entropy definition: $R_A^{\text{surface}} = 1 - \frac{H(Y|S)}{H(Y)}$. This should be propagated to the main text.

**PROPOSED FIX:**

*Update table entry:*
| $R_A^{surface}(d,t)$ | Surface-reward pressure — the information-theoretic advantage of surface features for predicting the target label. Defined as: $R_A^{\text{surface}} = 1 - \frac{H(Y \mid S)}{H(Y)}$ where $Y$ is the target label distribution and $S$ is the set of surface features. $R_A^{\text{surface}} = 0$ when surface features carry no predictive information; $R_A^{\text{surface}} = 1$ when surface features perfectly predict the label. |

*Add equation after Equation 29:*
$$R_A^{\text{surface}}(d,t) = 1 - \frac{H(Y \mid S, d, t)}{H(Y \mid d, t)} \tag{29a}$$

*Add prose:* "The entropy ratio $H(Y|S)/H(Y)$ measures the fraction of label uncertainty resolved by surface features alone. When surface features are highly predictive (low $H(Y|S)$ relative to $H(Y)$), $R_A^{\text{surface}}$ approaches 1, and the erosion term in Equation 29 dominates — attentional fidelity decays. When surface features carry little predictive information, $R_A^{\text{surface}}$ approaches 0 and the erosion term vanishes, leaving only the contrastive formation term $\gamma \cdot C_A \cdot (1 - \alpha_A)$."

**JUSTIFICATION:** This provides the formal mathematical definition that the ODE requires for simulation. The relative entropy form is information-theoretically standard and computable from training data statistics (surface-feature frequencies and label frequencies). It connects directly to the H-AFB confound strength parameter $s$, which controls the correlation between $S$ and $Y$. The parameter groups (Appendix A.2) are unaffected because $R_A^{\text{surface}}$ is a state-dependent quantity, not a constant parameter. The boundedness argument for $\alpha_A$ (Nagumo) holds because $R_A^{\text{surface}} \in [0,1]$ ensures the erosion term cannot flip sign.

**SAFETY NOTE:** This fix does NOT change Equation 28, Equation 19/A.10, Table 1, §7.1–7.5, or the Burnell citation. It adds Equation 29a and revises the gloss table. Equation 29 itself is unchanged — the new equation defines one of its existing terms.

---

### VARIANT C
**Issue #:** 5
**Tag:** Tier 1A
**Section targeted:** §4.1.3 (Equation 29) — redefine via observable proxy
**Scope:** structural

**DIAGNOSIS:** The relative entropy definition (Variant B) is formally correct but requires access to the joint distribution of surface features and labels during training — information not always available post-hoc. An alternative approach defines $R_A^{\text{surface}}$ via a directly measurable behavioural proxy: the fraction of correct outputs attributable to surface-cue tracking rather than structural rule application, as measured by the surface-conflict condition.

**PROPOSED FIX:**

*Update table entry:*
| $R_A^{surface}(d,t)$ | Surface-reward pressure — the empirically measured fraction of in-distribution performance attributable to surface-cue tracking. Operationally: $R_A^{\text{surface}}(d,t) = 1 - \hat{\alpha}_A(d,t)$ where $\hat{\alpha}_A = \text{Acc}_{OOD\text{-struct}} / \text{Acc}_{ID}$ is the attentional fidelity proxy from the H-AFB benchmark. When $\hat{\alpha}_A$ is low (agent tracks surface cues), $R_A^{\text{surface}}$ is high, and the erosion term in Eq. 29 is large. |

*Add after Equation 29:*
$$R_A^{\text{surface}}(d,t) \approx 1 - \hat{\alpha}_A(d,t) = 1 - \frac{\text{Acc}_{OOD\text{-struct}}(d,t)}{\text{Acc}_{ID}(d,t)} \tag{29b}$$

*Add prose:* "This proxy identification equates surface-reward pressure with the complement of attentional fidelity: the fraction of in-distribution accuracy that collapses under OOD evaluation. An agent with $\hat{\alpha}_A = 0.3$ (70% OOD accuracy loss) has $R_A^{\text{surface}} \approx 0.7$, meaning the training regime's surface-reward pressure is high. This operationalisation converts $R_A^{\text{surface}}$ from an unobservable latent quantity to a directly measurable benchmark score."

**JUSTIFICATION:** This definition makes $R_A^{\text{surface}}$ directly computable from benchmark scores — no training-distribution access required. It creates a clean closed loop: the H-AFB measures $\hat{\alpha}_A$, which identifies $R_A^{\text{surface}}$, which feeds back into the ODE predicting $\dot{\alpha}_A$. The proxy form preserves the $[0,1]$ boundedness required for Nagumo's theorem. The identification $R_A^{\text{surface}} \approx 1 - \hat{\alpha}_A$ is an approximation valid when the H-AFB surface confound strength $s$ is calibrated to match the training distribution's actual surface-reward pressure — a calibration requirement that should be noted as a measurement assumption.

**SAFETY NOTE:** This fix does NOT change Equation 28, Equation 19/A.10, Table 1, §7.1–7.5, or the Burnell citation. It adds Equation 29b and revises the gloss table. It introduces a measurement assumption (calibration of $s$ to training distribution) that should be documented.

---

### VARIANT D
**Issue #:** 5
**Tag:** Tier 1A
**Section targeted:** §4.1.3 (Equation 29) — decompose into two measurable sub-components
**Scope:** structural

**DIAGNOSIS:** Both the relative entropy definition (Variant B) and the proxy definition (Variant C) treat $R_A^{\text{surface}}$ as a single scalar. An alternative that preserves both theoretical grounding and empirical measurability is to decompose it into two named sub-components: (1) the cross-entropy reward from surface features, and (2) the structural reward deficit — the gap between surface-rewarded and structure-rewarded gradient updates.

**PROPOSED FIX:**

*Update table entry:*
| $R_A^{surface}(d,t)$ | Surface-reward pressure — composite of two sub-components: (a) $R_S(d,t)$: the rate at which training updates reinforce surface-feature associations; (b) $R_\Delta(d,t)$: the structural reward deficit, measuring the gap between surface-reward and structure-reward gradient magnitudes. $R_A^{\text{surface}} = R_S + \lambda_\Delta \cdot R_\Delta$. |

*Add equations after Equation 29:*

**Surface reward rate:**
$$R_S(d,t) = \frac{1}{N_{\text{batch}}} \sum_{i=1}^{N_{\text{batch}}} \mathbb{1}[\text{correct}(i) \text{ via surface cue}] \cdot \ell'(i) \tag{29c}$$

The batch-normalised sum of loss gradients for items where the correct output is attributable to surface-cue tracking.

**Structural reward deficit:**
$$R_\Delta(d,t) = \max\left(0, \; R_S(d,t) - \frac{1}{N_{\text{batch}}} \sum_{i=1}^{N_{\text{batch}}} \mathbb{1}[\text{correct}(i) \text{ via structure}] \cdot \ell'(i)\right) \tag{29d}$$

The positive part of the difference between surface-rewarded and structure-rewarded gradient contributions. When surface-rewarded gradients dominate, $R_\Delta > 0$ and adds to erosion. When structure-rewarded gradients dominate or are equal, $R_\Delta = 0$.

**Composite:**
$$R_A^{\text{surface}}(d,t) = R_S(d,t) + \lambda_\Delta \cdot R_\Delta(d,t) \tag{29e}$$

Where $\lambda_\Delta \geq 0$ weights the structural deficit. Bounded: $R_A^{\text{surface}} \in [0, 1 + \lambda_\Delta]$.

*Add prose:* "The two-component decomposition separates the direct effect of surface-rewarded gradient updates ($R_S$) from the additional erosion caused by the *imbalance* between surface and structure rewards ($R_\Delta$). An agent in a balanced training regime — where surface and structure receive equal gradient magnitude — has $R_\Delta = 0$ and erosion depends only on $R_S$. An agent in a surface-dominated regime has $R_\Delta > 0$, adding a second erosion channel."

**JUSTIFICATION:** The decomposition provides two distinct intervention points: (1) reduce $R_S$ by decreasing the base rate of surface-cue-rewarded items; (2) reduce $R_\Delta$ by increasing structure-rewarded gradient magnitudes to match surface-rewarded magnitudes. This has direct curriculum design implications: contrastive training (increasing $C_A$) addresses the formation term, while structural reward balancing addresses the erosion term. The decomposition is consistent with the H-AFB design, where confound strength $s$ manipulates $R_S$ and the three-condition battery measures both components.

**SAFETY NOTE:** This fix does NOT change Equation 28, Equation 19/A.10, Table 1, §7.1–7.5, or the Burnell citation. It adds Equations 29c–29e and revises the gloss table. The composite $R_A^{\text{surface}}$ plugs into Equation 29 unchanged.

---

### VARIANT E
**Issue #:** 5
**Tag:** Tier 1A
**Section targeted:** §4.1.3 + §4.1.5 + §12 (Appendix A.4) — systemic theory-measurement closure
**Scope:** systemic

**DIAGNOSIS:** The problem is not merely that $R_A^{\text{surface}}$ lacks a definition — it is that §4.1.3 (the ODE), §4.1.5 (the benchmark table), and the H-AFB protocol (track_attention.md) form an incomplete loop. The ODE uses a term the benchmarks measure; the benchmarks measure a proxy the ODE does not define. A systemic fix closes this loop by: (1) formally defining $R_A^{\text{surface}}$ in §4.1.3, (2) updating §4.1.5 to reference the formal definition, and (3) adding a measurement theory subsection to Appendix A that specifies the proxy identification and its calibration requirements.

**PROPOSED FIX:**

**Part 1 — §4.1.3 (after Equation 29):**

Add formal definition:
$$R_A^{\text{surface}}(d,t) = 1 - \frac{H(Y \mid S, d, t)}{H(Y \mid d, t)} \tag{29a}$$

Add measurement proxy identification:
$$R_A^{\text{surface}}(d,t) \approx 1 - \frac{\text{Acc}_{OOD\text{-struct}}(d,t)}{\text{Acc}_{ID}(d,t)} = 1 - \hat{\alpha}_A(d,t) \tag{29b}$$

Add calibration note: "The proxy identification (29b) is valid when the H-AFB surface confound strength $s$ is calibrated to match the training distribution's surface-feature/label correlation structure. The required calibration procedure is specified in Appendix A.4."

**Part 2 — §4.1.5 (update Attention track benchmark table):**

*Old row:*
| **Dual-Regularity Competition** | Tasks with superimposed surface regularity (high correlation, zero OOD validity) and compositional regularity (lower correlation, full OOD validity) | $α_A$ | High-$α_A$: tracks compositional; Low-$α_A$: tracks surface |

*New row:*
| **Dual-Regularity Competition (H-AFB)** | Tasks with superimposed surface regularity (high correlation, zero OOD validity) and compositional regularity (lower correlation, full OOD validity). Surface confound strength $s$ controls $R_A^{\text{surface}}$ via entropy ratio (Eq. 29a). Three-condition battery (ID, OOD-struct, OOD-surf-conflict) yields $\hat{\alpha}_A$, $\Delta_{\text{surf}}$, and SRI. | $α_A$, $R_A^{\text{surface}}$ | High-$α_A$: $\hat{\alpha}_A > 0.65$, small $\Delta_{\text{surf}}$, SRI ≈ 0. Low-$α_A$: $\hat{\alpha}_A < 0.45$, large $\Delta_{\text{surf}}$, SRI > 0. |

**Part 3 — Appendix A.4 (new subsection):**

```
### A.4 Surface-Reward Pressure: Formal Definition and Measurement

**Definition (information-theoretic):**
$$R_A^{\text{surface}}(d,t) = 1 - \frac{H(Y \mid S, d, t)}{H(Y \mid d, t)} \tag{A.14}$$

where $Y$ is the target label distribution and $S$ is the set of surface features.
$R_A^{\text{surface}} = 0$ when surface features carry no predictive information.
$R_A^{\text{surface}} = 1$ when surface features perfectly predict labels.

**Proxy identification:**
$$\hat{\alpha}_A(d,t) = \frac{\text{Acc}_{OOD\text{-struct}}(d,t)}{\text{Acc}_{ID}(d,t)} \implies R_A^{\text{surface}}(d,t) \approx 1 - \hat{\alpha}_A(d,t) \tag{A.15}$$

**Calibration requirement:** The proxy identification holds when the H-AFB
surface confound strength $s$ satisfies:
$$s \approx \frac{P(Y=1 \mid S=1)}{P(Y=1)} \quad \text{(training distribution)}$$

i.e., the confound-induced correlation matches the training distribution's
actual surface-feature/label correlation. Calibration proceeds by estimating
$P(Y=1|S=1)/P(Y=1)$ from training data and setting $s$ accordingly.

**Boundedness:** $R_A^{\text{surface}} \in [0,1]$ by construction (entropy ratio).
The erosion term $-\zeta_\alpha \cdot \alpha_A \cdot R_A^{\text{surface}}$ in Eq. 29
is non-positive, ensuring $\dot{\alpha}_A \leq \gamma \cdot C_A \cdot (1-\alpha_A)$.
Nagumo's theorem applies: $[0,1]$ is forward-invariant for $\alpha_A$.
```

**JUSTIFICATION:** This systemic fix closes the theory-measurement loop. The ODE (§4.1.3) now formally defines its erosion term. The benchmark table (§4.1.5) now references the formal definition. The Appendix (A.4) specifies the measurement theory, including the calibration requirement that connects the benchmark's confound strength to the training distribution's actual surface-feature statistics. The proxy identification (29b) creates a computable link between the ODE and the H-AFB output. This fix addresses not just the missing definition but the missing integration between theory and measurement.

**SAFETY NOTE:** This fix does NOT change Equation 28, Equation 19/A.10, Table 1, §7.1–7.5, or the Burnell citation. It adds Equations 29a–29b to §4.1.3, adds Appendix A.4, and updates one row in §4.1.5. All additions are to existing sections; no sections are restructured.
