# VARIANT PROPOSALS — ISSUE #1

**Issue:** The primary definition of schema coherence relies on rhetorical cognitive psychology vocabulary rather than rigorous mathematical grounding.

**Related sections:** §3.1.3 (Schema Coherence σ_A(d,t)), Abstract, §1.1 Central Claim, uniqueness table.

**Negative log check:** No prior rejected variants on Issue #1 or related schema-coherence definition issues. (Negative logs from issues #22 and #23 contain no entries on this topic.)

---

### VARIANT A

**Issue #:** 1
**Tag:** schema-coherence-definition
**Section targeted:** §3.1.3 — prose definition of σ_A(d,t)
**Scope:** Local prose fix
**DIAGNOSIS:** The prose definition "the degree to which the agent's representation of domain d has been restructured around deep governing principles" uses rhetorical cognitive psychology vocabulary ("restructured," "deep governing principles") without formal grounding. This language invites reviewers to interpret σ_A through a psychological lens, which violates the language rules in §3.8 (psychological vocabulary confined to §3.8 and bridge appendix). The definition needs a mathematical anchor that makes σ_A computationally interpretable independent of cognitive metaphor.

**PROPOSED FIX:**

*Old text (§3.1.3, Equation 3 and its prose definition):*
> #### 3.1.3 Schema Coherence σ_A(d,t)
>
> The degree to which the agent's representation of domain d has been restructured around deep governing principles.
> $$\sigma_A(d,t) \in [0, 1] \tag {3}$$

*New text:*
> #### 3.1.3 Schema Coherence σ_A(d,t)
>
> Schema coherence σ_A(d,t) measures the compression gain the agent achieves when moving from surface-feature encoding to structure-exploiting encoding of domain d. Formally, σ_A is the normalised ratio of the agent's representation length under a structure-invariant encoding to its representation length under the best available structure-exploiting encoding:
> $$\sigma_A(d,t) = 1 - \frac{L_{\text{struct}}(d,t)}{L_{\text{surface}}(d,t)} \in [0, 1] \tag {3}$$
> where $L_{\text{surface}}(d,t)$ is the minimum description length of the agent's representation using only surface-statistical regularities, and $L_{\text{struct}}(d,t)$ is the minimum description length using structure-exploiting codes that leverage the domain's generative rule. At σ_A = 0, the agent's representation gains no compression from exploiting domain structure (all structure is absorbed into surface patterns). At σ_A = 1, the agent's representation is maximally compressed by exploiting structure.

**JUSTIFICATION:** This replaces vague psychological language ("restructured around deep governing principles") with a precise information-theoretic quantity grounded in minimum description length (MDL). The ratio is bounded in [0,1] by construction (the structure-exploiting encoding cannot be longer than the surface-only encoding when the domain has exploitable structure). This is compatible with the existing ODE (Equation 28) because the MDL ratio is a property of the agent's representation at time t — it does not require rewriting the dynamics. The uniqueness table in §3.1.3 remains consistent: each row now refers to whether the competitor construct has this MDL-based property. The abstract and §1.1 still use "restructured around deep governing principles" as motivating prose, but the formal definition in §3.1.3 now provides the mathematical anchor.

**SAFETY NOTE:** This fix does NOT change: (a) the ODE for σ_A (Equation 28), (b) the multiplicative Ψ_A coupling (Equation 21), (c) the uniqueness table entries for rows other than the prose definition row, (d) any V2.0/V3.0 extensions. It only replaces the prose definition and adds Equation 3 as an MDL ratio.

---

### VARIANT B

**Issue #:** 1
**Tag:** schema-coherence-definition
**Section targeted:** §3.1.3 — uniqueness table, "Cognitive Schema" row
**Scope:** Local prose fix
**DIAGNOSIS:** The uniqueness table in §3.1.3 compares σ_A to "Cognitive Schema" — a psychological construct — in the final column. This imports cognitive psychology vocabulary directly into the formal variable architecture and invites reviewers to argue that σ_A is merely a repackaged cognitive schema concept. The table is the primary source of conflation: it is where the cognitive vocabulary enters the formal framework.

**PROPOSED FIX:**

*Old text (§3.1.3 uniqueness table, final column):*
> | Property                                 | σ_A | Structured Repr. | Disentangled Repr. | Causal Repr. | Cognitive Schema |
> | ---------------------------------------- | --- | ---------------- | ------------------ | ------------ | ---------------- |
> | Continuous scalar ODE                    | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | Frontier-relative normalisation          | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | Evaluative function (AI error detection) | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | Multiplicative Ψ_A coupling              | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | Decay coupling (slows λ_c)               | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | AI bypass risk Ω_AI suppression          | ✓   | ✗                | ✗                  | ✗            | ✗                |
> | Cross-modal transfer Θ_A                 | ✓   | ✗                | ✗                  | ✗            | ✗                |

*New text:*
> | Property                                 | σ_A | Structured Repr. | Disentangled Repr. | Causal Repr. | Compressed Residual Code |
> | ---------------------------------------- | --- | ---------------- | ------------------ | ------------ | ------------------------ |
> | Continuous scalar ODE                    | ✓   | ✗                | ✗                  | ✗            | ✗                        |
> | Frontier-relative normalisation          | ✓   | ✗                | ✗                  | ✗            | ✗                        |
> | Evaluative function (AI error detection) | ✓   | ✗                | ✗                  | ✗            | ✗                        |
> | Multiplicative Ψ_A coupling              | ✓   | ✗                | ✗                  | ✗            | ✗                        |
> | Decay coupling (slows λ_c)               | ✓   | ✗                | ✗                  | ✗            | ✗                        |
> | AI bypass risk Ω_AI suppression          | ✓   | ✗                | ✗                  | ✗            | ✗                        |
> | Cross-modal transfer Θ_A                 | ✓   | ✗                | ✗                  | ✗            | ✗                        |

Also add the following prose immediately before the table:

> **Formal definition:** σ_A(d,t) is the compression ratio of the agent's domain-d representation relative to a structure-agnostic baseline. An agent with σ_A = 1 has a representation that achieves maximal compression by exploiting the domain's generative regularities. An agent with σ_A = 0 has a representation that is no more compressible than surface-feature encoding.

**JUSTIFICATION:** Replacing "Cognitive Schema" with "Compressed Residual Code" removes the final cognitive psychology reference in the formal variable architecture while preserving the table's function of distinguishing σ_A from adjacent computational constructs. "Compressed Residual Code" is a term from the MDL literature (Grünwald, 2007) referring to the portion of the representation that remains after removing redundant surface structure — directly analogous to what σ_A measures. The added prose definition provides an anchor without psychological vocabulary. No ODEs, coupling terms, or benchmark designs are affected.

**SAFETY NOTE:** This fix does NOT change: (a) any ODEs, (b) the Ψ_A mechanism, (c) any benchmark families, (d) any V2.0/V3.0 extensions. It only modifies the uniqueness table column header and adds a brief prose definition. The word "Cognitive Schema" appears only in this table; removing it eliminates the sole entry point of this psychological term into the formal framework.

---

### VARIANT C

**Issue #:** 1
**Tag:** schema-coherence-definition
**Section targeted:** Abstract + §1.1 + §3.1.3
**Scope:** Systemic reframe
**DIAGNOSIS:** The cognitive psychology vocabulary is not confined to §3.1.3 — it pervades the abstract ("restructured around deep governing principles") and the central claim in §1.1. A local fix in §3.1.3 alone will not prevent reviewers from encountering the rhetorical framing first and interpreting the entire framework through a cognitive lens. A systemic reframe is needed to establish the information-theoretic grounding from the paper's opening.

**PROPOSED FIX:**

*Old text (Abstract, first paragraph):*
> Current training pipelines optimise parametric depth δ_A(d,t) without formally targeting schema coherence σ_A(d,t) — the degree to which an agent's representations are restructured around deep governing principles rather than surface-statistical regularities.

*New text:*
> Current training pipelines optimise parametric depth δ_A(d,t) without formally targeting schema coherence σ_A(d,t) — the degree to which an agent's internal representation of domain d achieves compression by exploiting the domain's generative regularities rather than encoding surface-statistical features.

*Old text (§1.1 Central Claim):*
> Training pipelines that optimise δ_A(d,t) without formally targeting σ_A(d,t) will systematically produce agents that pass in-distribution evaluation while failing out-of-distribution recombination — not because they lack depth, but because their training regimes suppress the schema crystallisation that converts parametric depth into principled generalisation capacity.

*New text:*
> Training pipelines that optimise δ_A(d,t) without formally targeting σ_A(d,t) will systematically produce agents that pass in-distribution evaluation while failing out-of-distribution recombination — not because they lack depth, but because their training regimes suppress the structural compression that converts parametric depth into generalisable encoding.

*Old text (§3.1.3 prose definition):*
> The degree to which the agent's representation of domain d has been restructured around deep governing principles.

*New text:*
> The degree to which the agent's representation of domain d achieves compression by exploiting the domain's generative structure. Formally: the normalised difference between the agent's representation cost under structure-agnostic encoding and under structure-exploiting encoding, bounded in [0,1].

**JUSTIFICATION:** This systemic reframe replaces all instances of cognitive psychology vocabulary ("restructured around deep governing principles," "schema crystallisation," "principled generalisation") with information-theoretic language ("compression," "generative structure," "structure-exploiting encoding") across the three primary locations where the reader first encounters σ_A. The ODEs, coupling terms, and benchmark designs are untouched because the mathematical machinery was already information-theoretic — only the prose framing was rhetorical. The word "principled" is removed from §1.1 to avoid the cognitive loading it carries. "Generative structure" is preferred over "governing principles" because it is a formal property (the generating distribution of the domain) rather than a metaphor.

**SAFETY NOTE:** This fix deliberately does NOT change: (a) any equations, (b) any coupling terms, (c) any benchmark families, (d) any V2.0/V3.0 extensions. It replaces only prose text in the abstract, §1.1, and §3.1.3. The mathematical content is identical.

---

### VARIANT D

**Issue #:** 1
**Tag:** schema-coherence-definition
**Section targeted:** §3.1.3 + §3.4.3 (schema coherence ODE)
**Scope:** Structural equation fix
**DIAGNOSIS:** The current definition of σ_A is purely prose and lacks a formal axiomatic foundation. The ODE (Equation 17/28) specifies how σ_A changes over time, but never specifies what σ_A *is* at a point in time. This means σ_A is operationally defined only by its dynamics — a circular situation that invites reviewers to question whether σ_A is a coherent quantity or merely a label on a free parameter. Fixing this requires grounding σ_A in representation fidelity from first principles.

**PROPOSED FIX:**

*Insert the following axiomatization immediately before Equation 3 in §3.1.3:*

> **Axiom 1 (Representation Fidelity).** Let F(d,t) denote the set of all encodings of domain d available to agent A at time t. For each encoding f ∈ F, let L(f) denote its description length and let OOD(f) denote the agent's accuracy on out-of-distribution instances of domain d when using encoding f. Define:
> $$\sigma_A(d,t) = \frac{\max_{f \in F} \text{OOD}(f) - \text{OOD}(f_{\text{surface}})}{1 - \text{OOD}(f_{\text{surface}})} \in [0, 1] \tag{3a}$$
> where $f_{\text{surface}}$ is the encoding that minimises description length using only surface-statistical features (the default encoding under standard training).
>
> **Axiom 2 (Monotonicity).** σ_A(d,t) is non-decreasing in the agent's OOD performance at fixed surface baseline: $\partial \sigma_A / \partial \text{OOD}_{\max} \geq 0$.
>
> **Axiom 3 (Boundary).** σ_A = 0 when the agent's best encoding achieves no better OOD accuracy than the surface baseline. σ_A = 1 when the agent's encoding achieves perfect OOD accuracy.

*Old Equation 3:*
> $$\sigma_A(d,t) \in [0, 1] \tag{3}$$

*Replace with:*
> $$\sigma_A(d,t) \in [0, 1] \tag{3}$$
> (Characterised by Axioms 1–3 above.)

**JUSTIFICATION:** The three axioms provide a complete, non-circular definition of σ_A grounded in measurable quantities (OOD accuracy relative to surface baseline). Axiom 1 gives the explicit formula; Axiom 2 guarantees the quantity behaves as expected; Axiom 3 pins the boundaries. This is consistent with the existing proxy identification (SGG) already used throughout the paper — in fact, Axiom 1 is a normalised version of the SGG proxy, making the definition self-referentially consistent with the measurement protocol. The ODE (Equation 28) remains unchanged because the axioms define σ_A at a point in time and the ODE specifies its temporal evolution — these are complementary, not redundant. The uniqueness table can now reference "Axiom 1 formula" as the distinguishing property rather than a vague prose description.

**SAFETY NOTE:** This fix does NOT change: (a) the ODE for σ_A (Equation 28), (b) any coupling terms, (c) any benchmark families, (d) any V2.0/V3.0 extensions. It adds axiomatic grounding before Equation 3 and labels Equation 3 as axiomatically characterised. The uniqueness table gains a new row referencing the axiomatic definition, but existing rows are unchanged.

---

### VARIANT E

**Issue #:** 1
**Tag:** schema-coherence-definition
**Section targeted:** §3.1.3
**Scope:** Structural equation fix
**DIAGNOSIS:** The existing paper already defines a measurement proxy for σ_A — the Systematic Generalisation Gap (SGG) in §8 and Appendix A.4 — but the primary definition in §3.1.3 does not reference this proxy. This creates a disconnect: the formal definition is rhetorical while the measurement protocol is operational. Reviewers can argue σ_A is unmeasurable because the primary definition provides no anchor to observable quantities. Closing this gap requires making the proxy identification explicit in §3.1.3 itself, so the definition and the measurement are formally linked.

**PROPOSED FIX:**

*Old text (§3.1.3, after Equation 3 and before the uniqueness table):*

> **Unique properties distinguishing σ_A from adjacent constructs:**

*New text (insert immediately after Equation 3, before the uniqueness table):*

> **Proxy identification.** Schema coherence is not directly observable; it is operationalised through the Systematic Generalisation Gap (SGG). For an agent A evaluated on domain d at time t:
> $$\hat{\sigma}_A(d,t) = 1 - \frac{\text{Acc}_{\text{In}}(d,t) - \text{Acc}_{\text{OOD}}(d,t)}{\text{Acc}_{\text{In}}(d,t)} = \frac{\text{Acc}_{\text{OOD}}(d,t)}{\text{Acc}_{\text{In}}(d,t)} \tag{3b}$$
> where Acc_In is in-distribution accuracy and Acc_OOD is accuracy on out-of-distribution recombination instances. This proxy is valid when the OOD split tests compositional recombination of primitives trained in isolation (e.g., SCAN add-primitive split, COGS systematic split, PCFG-SET productivity split). The proxy identification $\hat{\sigma}_A \approx \sigma_A$ holds when the OOD difficulty is calibrated to span the $\sigma_{\text{critical}}$ threshold (see Appendix A.4).
>
> **Unique properties distinguishing σ_A from adjacent constructs:**

*Also update the prose definition in §3.1.3 to reference the proxy:*

*Old:*
> The degree to which the agent's representation of domain d has been restructured around deep governing principles.

*New:*
> The degree to which the agent's representation of domain d has been restructured around deep governing principles. Operationally: the normalised ratio of OOD compositional generalisation accuracy to in-distribution accuracy (Equation 3b), measurable via SCAN/COGS/PCFG-SET benchmark splits.

**JUSTIFICATION:** This variant makes the proxy identification a formal part of the definition in §3.1.3, rather than leaving it implicit in §8 and Appendix A.4. The result is that σ_A is defined by its observable consequences (OOD accuracy relative to ID accuracy at matched depth), not by a vague prose description alone. The phrase "restructured around deep governing principles" is retained as motivating language but is now explicitly anchored to the proxy equation. This preserves the paper's rhetorical framing while providing the mathematical grounding the issue demands. The proxy equation (3b) is a direct normalisation of the SGG already defined in the paper, so no new measurement protocol is introduced — only the existing one is integrated into the primary definition.

**SAFETY NOTE:** This fix does NOT change: (a) the ODE for σ_A (Equation 28), (b) any coupling terms, (c) any benchmark families, (d) any V2.0/V3.0 extensions. It adds one equation (3b) and one paragraph of prose to §3.1.3, and updates the prose definition to reference the proxy. The SGG definition in §8 and Appendix A.4 remains unchanged.
