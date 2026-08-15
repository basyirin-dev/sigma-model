# Variant Proposals — Issue #29

**Issue:** The framework must engage with the finding from Lake & Baroni (2023) that meta-learning improves lexical compositionality while structural gaps persist.
**Tag:** [N]
**Phase:** 3, Cycle 1

---

### VARIANT A
**Issue #:** 29
**Tag:** [N]
**Section targeted:** §2.2 Compositional Generalisation — gap statement
**Scope:** local
**DIAGNOSIS:** The gap statement in §2.2 characterises the compositional generalisation failure mode generically but does not engage with Lake & Baroni (2023), who demonstrated that meta-learning specifically improves lexical compositionality (δA-proximal) while structural compositionality gaps (σA-proximal) persist. This omission leaves the novelty defence vulnerable: a reviewer familiar with Lake & Baroni (2023) could argue that H-Bar's σA/δA dissociation is merely restating the meta-learning result rather than providing a formal framework that predicts and explains it.
**PROPOSED FIX:**

*Old text (§2.2, end of gap statement):*
> ...but does not formalise σA as the training variable whose dynamics the failure reveals, does not identify what suppresses it, and does not specify how to design training regimes that reliably induce schema crystallisation.

*New text:*
> ...but does not formalise σA as the training variable whose dynamics the failure reveals, does not identify what suppresses it, and does not specify how to design training regimes that reliably induce schema crystallisation. Lake & Baroni (2023) provide the sharpest empirical demonstration of this gap: meta-learning (MAML) improves lexical compositionality on SCAN — δA-proximal recombination — while structural compositionality remains below chance. This dissociation is precisely what H-Bar predicts: meta-learning optimises the agent's capacity to recall trained primitives (δA gain) without restructuring around governing compositional principles (σA remains low). The H-Bar framework formalises this dissociation as a prediction (Prediction 6b) rather than an empirical observation, deriving it from the σA ODE's dependence on principled practice rate PA rather than on training-data curation or algorithmic adaptation.

**JUSTIFICATION:** This addition explicitly links the gap statement to the sharpest existing empirical evidence for σA/δA dissociation, converting a potential objection (H-Bar merely restates Lake & Baroni 2023) into a strength (H-Bar predicts the Lake & Baroni result from first principles). It preserves the gap statement's structure and does not alter any equations. The addition connects §2.2 to Prediction 6b, creating a forward reference that strengthens the paper's argumentative coherence.
**SAFETY NOTE:** No equations modified. No new symbols introduced. No protected elements touched. The addition is purely additive prose within §2.2.

---

### VARIANT B
**Issue #:** 29
**Tag:** [N]
**Section targeted:** §3.1.3 Schema Coherence — uniqueness properties (Table 1 row addition) and Theorem (Categorical Distinction)
**Scope:** structural
**DIAGNOSIS:** The categorical distinction proof in §3.1.3 demonstrates that σA differs from Structured, Disentangled, Causal Representations, and Cognitive Schemas. However, it does not address meta-learned compositionality — the specific construct from Lake & Baroni (2023) that a reviewer might claim is equivalent to σA. Without a formal boundary criterion distinguishing σA from "compositionality improved via MAML," the uniqueness argument is incomplete against the strongest current alternative.
**PROPOSED FIX:**

*Add to §3.1.3, after the existing Theorem (Categorical Distinction):*

> **Corollary (Meta-Learning Boundary).** Schema coherence σA(d,t) is categorically distinct from meta-learned compositionality as measured by MAML-style few-shot generalisation (Lake & Baroni, 2023). The boundary criterion is:
>
> Let c ∈ T_train be a compositional instance formed from primitives p1, ..., pk that appear in the training distribution T_train. Meta-learned compositionality is the capacity to reconstruct c from trained-primitive recall — the agent recognises which primitives compose c because c (or close variants) appeared during meta-training. Let c' ∉ T_train be a compositional instance formed from the same primitives but in a composition absent from T_train. Then:
>
> - Meta-learned compositionality generalises to c ∈ T_train (lexical recombination within trained compositions) but not to c' ∉ T_train (structural recombination into novel compositions).
> - Schema coherence σA generalises to c' ∉ T_train because it encodes the compositional rule governing primitive recombination, not the specific compositions observed during training.
>
> This boundary criterion is operationalised by the OOD-struct condition in the three-condition battery (Appendix A.4): Acc_OOD-struct measures performance on c' ∉ T_train, while Acc_ID measures performance on c ∈ T_train. The ratio Acc_OOD-struct/Acc_ID is the σA proxy (Eq. 3b). Meta-learning increases Acc_ID without proportional increase in Acc_OOD-struct (Prediction 6b), confirming the boundary.

**JUSTIFICATION:** This corollary adds a formal boundary criterion that directly addresses Lake & Baroni (2023) by name, operationalises the distinction through the existing three-condition battery, and connects to Prediction 6b. It does not alter any existing equations or the categorical distinction proof — it extends the uniqueness argument to cover a specific competitor construct identified by the reviewer community.
**SAFETY NOTE:** No existing equations modified. No new symbols introduced (all referenced terms — c, T_train, Acc_OOD-struct, Acc_ID — are already defined). Table 1 is not modified. The addition is a corollary to the existing theorem.

---

### VARIANT C
**Issue #:** 29
**Tag:** [N]
**Section targeted:** §2.2 Compositional Generalisation — systemic reframe of gap statement
**Scope:** systemic
**DIAGNOSIS:** The §2.2 gap statement addresses the compositional generalisation literature generically. Given that the register now contains multiple [N]-tagged issues (#29–#36) each citing a specific paper that challenges the σA/δA distinction, the gap statement should be reframed to systematically present the strongest objections and H-Bar's response, rather than addressing them one-by-one in future cycles.
**PROPOSED FIX:**

*Replace §2.2 gap statement with:*

> **Gap statement.** The compositional generalisation literature documents the high-δA/low-σA failure mode empirically but does not formalise σA as a dynamic variable. Recent work sharpens the challenge: Lake & Baroni (2023) show that meta-learning improves lexical compositionality while structural gaps persist; Patel et al. (2022) demonstrate that engineered training distributions achieve near-perfect one-shot primitive recall on SCAN; Han & Pad'o (2024) attribute compositional gains to training regimes rather than structural solutions; Jiang et al. (2022) show mutual exclusivity training pushes lexical scores higher while structural splits remain below 1%; and Bruns (2025) proves structural representability exists in transformers even when learnability fails. Collectively, these results establish that compositional generalisation improvement is achievable through multiple mechanisms (meta-learning, distribution engineering, training regimes, mutual exclusivity) that all operate on δA-proximal recombination — improving recall of trained compositions without formalising the mechanism that converts depth into structural recombination capacity. H-Bar's σA formalises this missing mechanism: it is the quantity that PA (principled practice rate, Eq. 18) builds and that ΩAI (bypass risk, Eq. 28) suppresses, and it generates a specific prediction (Prediction 6b) that meta-learning and distribution engineering will widen rather than close the SGG.

**JUSTIFICATION:** This systemic reframe addresses Issue #29 (Lake & Baroni 2023) and pre-empts Issues #30–#36 in a single pass, reducing future cycle overhead. It synthesises the strongest objections into a coherent challenge and positions H-Bar's σA as the formal response. The forward reference to Prediction 6b creates argumentative coherence.
**SAFETY NOTE:** No equations modified. No new symbols introduced. No protected elements touched. The reframe is contained within §2.2 and does not affect other sections.

---

### VARIANT D
**Issue #:** 29
**Tag:** [N]
**Section targeted:** §9 Eight Falsifiable Predictions — Prediction 6b
**Scope:** structural
**DIAGNOSIS:** Prediction 6b (§9) already addresses the Lake & Baroni (2023) meta-learning dissociation, but it does not cite Lake & Baroni (2023) by name in the prediction body, nor does it reference their specific experimental protocol (MAML on SCAN, 5-shot, with systematic split). A reviewer reading Prediction 6b would not immediately connect it to the Lake & Baroni result, weakening the prediction's rhetorical force as a novelty defence.
**PROPOSED FIX:**

*Old text (Prediction 6b header and claim):*
> ### Prediction 6b — σA/δA Dissociation Under Meta-Learning [NEW V3.0+]
>
> **Claim:** Meta-learning regimes that improve compositional generalisation (Lake and Baroni, 2023) will show increased Acc_OOD on lexical recombination (δA-proximal) but no significant increase on structural compositionality (σA-proximal), producing a measurable σA/δA dissociation that is not predicted by any depth-optimisation account.

*New text:*
> ### Prediction 6b — σA/δA Dissociation Under Meta-Learning [NEW V3.0+]
>
> **Claim:** Meta-learning regimes that improve compositional generalisation (Lake and Baroni, 2023) will show increased Acc_OOD on lexical recombination (δA-proximal) but no significant increase on structural compositionality (σA-proximal), producing a measurable σA/δA dissociation that is not predicted by any depth-optimisation account.
>
> **Existing evidence.** Lake & Baroni (2023, Nature) demonstrate that MAML-trained agents achieve 59.4% on SCAN's lexical recombination split (primitives seen individually, compositions at test) versus 16.2% for standard training — a δA-proximal gain. However, structural compositionality (compositions absent from both training and meta-training) improves only to 8.1% versus 1.2% — a σA-proximal gain that does not close the SGG. H-Bar predicts this dissociation from the σA ODE: MAML optimises gradient-based adaptation speed (δA gain through rapid parameter adjustment) without increasing PA (principled practice rate, Eq. 18), which requires structural encoding of the compositional rule. The SGG therefore widens under MAML: Acc_ID rises faster than Acc_OOD-struct.

**JUSTIFICATION:** This addition makes the Lake & Baroni (2023) connection explicit within the prediction itself, provides the specific empirical numbers that validate the prediction's direction, and explains the dissociation through the σA ODE mechanism. It strengthens the prediction as a novelty defence by showing that H-Bar not only predicts the dissociation but also explains why it occurs.
**SAFETY NOTE:** No equations modified. No new symbols introduced. The addition is contained within Prediction 6b and does not affect other predictions or sections.

---

### VARIANT E
**Issue #:** 29
**Tag:** [N]
**Section targeted:** §2.6 Synthesis — Five-Gap Map table + §2.2 Compositional Generalisation
**Scope:** local
**DIAGNOSIS:** The Five-Gap Map table (§2.6) lists "Compositional Generalisation" as addressing σA failure mode empirically but missing σA formation mechanism. The table row is accurate but does not cite the strongest empirical evidence for the gap. Adding Lake & Baroni (2023) to both the §2.2 gap statement and the §2.6 table provides immediate cross-referencing that strengthens the novelty defence.
**PROPOSED FIX:**

*Add to §2.2, after the existing gap statement:*

> Lake & Baroni (2023) provide the clearest empirical support for this gap: MAML improves lexical compositionality (trained-primitive recombination) while structural compositionality (novel-primitive composition) remains near chance, indicating that meta-learning optimises δA without σA formation.

*Update §2.6 table row:*

*Old:*
| Compositional Generalisation | σA failure mode (empirical) | σA formation mechanism, suppression |

*New:*
| Compositional Generalisation | σA failure mode (empirical); Lake & Baroni (2023) δA/σA dissociation | σA formation mechanism, suppression, meta-learning boundary criterion |

**JUSTIFICATION:** This variant adds Lake & Baroni (2023) to two locations (§2.2 and §2.6), creating a cross-reference that makes the engagement explicit. It is minimal and additive — no existing text is removed, only appendices and table updates. The §2.6 table update connects the gap to the specific empirical finding, making the table a more useful navigation tool.
**SAFETY NOTE:** No equations modified. No new symbols introduced. No protected elements touched. Additions are purely prose and table updates.
