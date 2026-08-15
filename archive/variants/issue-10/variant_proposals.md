# VARIANT PROPOSALS — ISSUE #10

**Issue:** The empirical prediction requires matching agents on δ_A while varying σ_A but does not specify a protocol to independently increase schema coherence without increasing depth.

**Related sections:** §9 (Empirical Predictions), §8 (Benchmarks), §3.1.3 (Schema Coherence Definition), §5 (Discovery Rate).

**Negative log check:** No prior rejected variants on Issue #10. No negative_log.md files exist in any issue directory.

---

### VARIANT A

**Issue #:** 10
**Tag:** hackathon-priority-schema-coherence-protocol
**Section targeted:** §9 — Empirical Predictions (Prediction 1)
**Scope:** Local prose fix
**DIAGNOSIS:** Prediction 1 in §9 states that "agents matched on δ_A but with higher σ_A will show systematically higher OOD accuracy" but provides no experimental protocol for how an experimenter could create two agent populations matched on depth while differing in schema coherence. Without such a protocol, the prediction is unfalsifiable — it describes a desired outcome but not a method to test it. A reviewer can dismiss this as a thought experiment rather than an empirical claim.

**PROPOSED FIX:**

*Old text (§9, Prediction 1):*
> **Prediction 1 (Schema Coherence Gap).** Agents matched on δ_A(d,t) but with higher σ_A(d,t) will show systematically higher accuracy on out-of-distribution recombination instances, with the gap widening as the OOD task requires deeper compositional recombination.

*New text:*
> **Prediction 1 (Schema Coherence Gap).** Agents matched on δ_A(d,t) but with higher σ_A(d,t) will show systematically higher accuracy on out-of-distribution recombination instances, with the gap widening as the OOD task requires deeper compositional recombination.
>
> **Testing protocol.** To test this prediction independently of depth:
> 1. Train all agents to the same in-distribution accuracy threshold Acc_In = τ (e.g., τ = 0.95) on a compositional domain (SCAN, COGS, or PCFG-SET), ensuring matched δ_A by controlling total parameter count and training steps.
> 2. Split agents into two conditions: (a) **structure-augmented training** — apply systematic data augmentation that preserves generative structure (e.g., swap-primitive recombination, synonym substitution within compositional templates); (b) **surface-augmented training** — apply augmentations that vary surface tokens without preserving compositional structure (e.g., random token dropout, uniform noise injection).
> 3. Both conditions continue training until Acc_In returns to τ. Structure-augmented agents will have higher σ_A because their augmentations force structure-exploiting encoding; surface-augmented agents will have comparable δ_A but lower σ_A because their augmentations are absorbed by surface-statistical encoding.
> 4. Evaluate both conditions on the same OOD recombination split. The prediction is confirmed if structure-augmented agents show significantly higher Acc_OOD (Cohen's d > 0.5, p < 0.01) at matched Acc_In and δ_A.

**JUSTIFICATION:** This adds a concrete experimental protocol that closes the falsifiability gap without changing any equations. The augmentation-based protocol is well-established in the compositional generalization literature (Andreas, 2020; Qiu et al., 2022) and directly targets the σ_A/δ_A decoupling the prediction requires. Structure-augmented training forces the agent to encode generative regularities (increasing σ_A) while surface-augmented training does not (maintaining comparable δ_A). The protocol specifies exact stopping criteria, matching procedure, and statistical threshold, making the prediction testable.

**SAFETY NOTE:** This fix does NOT change: (a) any ODEs, (b) any coupling terms, (c) any benchmark families, (d) any V2.0/V3.0 extensions. It adds only a testing protocol paragraph to §9. No protected elements are touched.

---

### VARIANT B

**Issue #:** 10
**Tag:** hackathon-priority-schema-coherence-protocol
**Section targeted:** §3.1.3 (Schema Coherence Definition) + §5 (Discovery Rate)
**Scope:** Structural equation fix
**DIAGNOSIS:** The paper lacks a formal mechanism explaining why σ_A and δ_A can grow independently. Currently, both are treated as properties of training, but no equation distinguishes the growth pathways. The ODE for σ_A (Equation 28) depends on training allocation and AI bypass, while δ_A growth is driven by parametric updates — but the paper never formalizes why a training protocol could target one without the other. Without a formal decoupling mechanism, the protocol for Issue #10 is ad hoc rather than grounded in the model.

**PROPOSED FIX:**

*Insert the following after Equation 3 in §3.1.3, before the uniqueness table:*

> **Growth-pathway independence.** Schema coherence σ_A and parametric depth δ_A grow along formally separable pathways:
>
> $$\frac{d\sigma_A}{dt} = g_\sigma \cdot \alpha_A \cdot (1 - \sigma_A) - \lambda_\sigma \cdot \sigma_A \tag{3c}$$
> $$\frac{d\delta_A}{dt} = g_\delta \cdot (1 - \delta_A) - \lambda_\delta \cdot \delta_A \tag{3d}$$
>
> where $g_\sigma$ is the structure-relevant training rate (governed by training protocols that force structural encoding), $g_\delta$ is the parameter-update rate (governed by gradient descent volume), $\alpha_A$ is the attentional fidelity gating σ_A growth, and $\lambda_\sigma$, $\lambda_\delta$ are decay terms. The key independence condition is:
>
> $$\text{Cov}\left(\frac{d\sigma_A}{dt}, \frac{d\delta_A}{dt}\right) = 0 \iff g_\sigma \text{ and } g_\delta \text{ are driven by independent protocol choices}$$
>
> A training protocol that increases $g_\sigma$ (via structure-preserving augmentations) without increasing $g_\delta$ (holding parameter count and gradient steps fixed) will increase σ_A while leaving δ_A unchanged. This is the formal basis for Prediction 1's testing protocol.

*Also add to §5 (Discovery Rate), after the existing equations:*

> **σ_A-only growth pathway.** When the training protocol includes structure-preserving augmentations, the discovery rate acquires an additional term:
> $$\dot{\Psi}_A^{\sigma} = \eta_\sigma \cdot g_\sigma \cdot \alpha_A \cdot \sigma_A \cdot \Psi_A \tag{16b}$$
> This term represents schema-mediated discovery: augmentations that force structural encoding generate new intersection candidates by revealing hidden compositional regularities. The total discovery rate becomes $\dot{\Psi}_A = \dot{\Psi}_A^{\text{depth}} + \dot{\Psi}_A^{\sigma}$, where the two terms are independently controllable via training protocol design.

**JUSTIFICATION:** The growth-pathway independence equations formalize the intuition that σ_A and δ_A can be manipulated separately, grounding Prediction 1 in the ODE system rather than leaving it as an empirical assertion. Equations 3c and 3d are simple linear ODEs consistent with the paper's existing decay/growth architecture. The independence condition (zero covariance) makes explicit the requirement for independent protocol choices. The σ_A-only discovery pathway in §5 extends the multiplicative Ψ_A mechanism to show that structure-augmented training has a formal mechanism for generating new discoveries. All new equations use existing variable names and are dimensionally consistent.

**SAFETY NOTE:** This fix does NOT change: (a) Equation 28 (σ_A ODE with αA gating), (b) the multiplicative Ψ_A functional form (Equation 19/A.10), (c) any benchmark families, (d) any V2.0/V3.0 extensions. It adds equations 3c, 3d, 16b and associated prose. The existing σ_A ODE (Eq. 28) is unchanged — the new growth equations describe the decomposed pathway, while Eq. 28 describes the full dynamics including AI bypass.

---

### VARIANT C

**Issue #:** 10
**Tag:** hackathon-priority-schema-coherence-protocol
**Section targeted:** New §10.3 (Training Protocols for Independent Variable Manipulation)
**Scope:** Systemic reframe
**DIAGNOSIS:** The paper lacks a dedicated section on training protocols. Predictions in §9 assume experimenters can independently manipulate σ_A and δ_A, but the paper never provides a systematic treatment of how training design achieves this. Adding a new subsection in §10 (Limitations and Future Directions) would provide a home for the protocol specification, keep §9 focused on predictions, and signal to reviewers that the authors recognize this as an open methodological challenge.

**PROPOSED FIX:**

*Insert the following as a new subsection at the end of §10 (after §10.2 or current final subsection):*

> ### 10.3 Training Protocols for Independent Variable Manipulation
>
> The framework's predictions (§9) require experimenters to construct agent populations that vary σ_A(d,t) while holding δ_A(d,t) constant, or vice versa. This section specifies the protocol families that achieve each manipulation.
>
> **Protocol P1: Increasing σ_A at fixed δ_A.**
> To increase schema coherence without increasing parametric depth:
> 1. Begin with a trained agent at target in-distribution accuracy Acc_In = τ.
> 2. Apply structure-preserving data augmentations that force the agent to exploit compositional regularities. Valid augmentations include: (a) primitive recombination — swap primitives trained in isolation to create unseen compositions; (b) template preservation — vary surface tokens while preserving the syntactic template; (c) distributional shift within structure — move to a new surface distribution that shares the same generative grammar.
> 3. Continue training until Acc_In returns to τ. The agent now has higher σ_A (measured via SGG) at matched δ_A (matched because parameter count and total gradient steps are held fixed).
>
> **Protocol P2: Increasing δ_A at fixed σ_A.**
> To increase parametric depth without increasing schema coherence:
> 1. Begin with a trained agent at target Acc_In = τ.
> 2. Increase model capacity (add parameters) and continue training on the same surface distribution with no structural augmentations.
> 3. The agent achieves higher δ_A (measured via parametric complexity) while σ_A remains approximately constant (measured via SGG) because the additional capacity absorbs surface-statistical variation without forcing structural encoding.
>
> **Protocol P3: Joint increase.**
> Standard training on the original distribution increases both δ_A and σ_A simultaneously, as the agent accumulates both parametric capacity and structural encoding. This is the default regime addressed by most existing work.
>
> **Hackathon implementation.** Protocols P1 and P2 are directly implementable for the five hackathon tracks (§Hackathon). For the Learning track (SCAN/COGS benchmarks), P1 is implemented via the augmentation families in Appendix A.4. For the Metacognition track, P1 provides the σ_A manipulation needed to test Prediction 7 (metacognitive calibration as a function of σ_A at fixed δ_A).

**JUSTIFICATION:** A dedicated protocol section provides a clear, systematic home for the training methodology that §9 predictions require. Placing it in §10 (Limitations and Future Directions) signals that this is a methodological contribution rather than a core theoretical result, keeping the paper's main argument focused. The three-protocol structure (P1/P2/P3) covers all manipulation combinations needed by §9. The hackathon linkage directly addresses the [HACKATHON PRIORITY] tag by connecting protocols to implementable benchmark designs.

**SAFETY NOTE:** This fix does NOT change: (a) any ODEs, (b) any coupling terms, (c) any benchmark families in §8, (d) any predictions in §9, (e) any V2.0/V3.0 extensions. It adds a new subsection to §10 only. No protected elements are touched.

---

### VARIANT D

**Issue #:** 10
**Tag:** hackathon-priority-schema-coherence-protocol
**Section targeted:** §8 (Benchmarks and Evaluation) + Appendix A.4 (Calibration)
**Scope:** Local prose fix
**DIAGNOSIS:** The benchmark section (§8) defines the SGG measurement protocol but does not specify how to use benchmarks to construct the σ_A/δ_A manipulation required by §9 predictions. The gap is operational: a researcher reading §8 knows how to measure σ_A after training, but not how to design a training run that produces the desired σ_A at controlled δ_A. Adding the protocol directly to §8 makes the benchmark section self-contained for experimental implementation.

**PROPOSED FIX:**

*Insert the following in §8, after the SGG definition (Equation 46/47) and before the benchmark families table:*

> **Experimental design for σ_A/δ_A manipulation.** The following protocol uses existing benchmark splits to construct agent populations that isolate σ_A variation:
>
> *Step 1 — Depth matching.* Train all agents to the same in-distribution accuracy threshold (Acc_In ≥ 0.95) on the training split. Verify δ_A matching by confirming that all agents have equivalent parameter counts (±5%) and total training FLOPs (±10%).
>
> *Step 2 — σ_A manipulation via training regime.* Split agents into conditions:
> - **High-σ_A condition:** Train on the structure-augmented split (SCAN: add-primitive + jump primitive combinations; COGS: systematic + productivity splits; PCFG-SET: depth-3 + depth-5 recombination). These splits force structural encoding by presenting compositions that cannot be solved by surface memorization.
> - **Low-σ_A condition:** Train on the original split with surface-level augmentations (random token dropout p=0.1, uniform label smoothing ε=0.1). These augmentations increase robustness without forcing structural encoding.
>
> *Step 3 — Verification.* After training, verify:
> - Acc_In is matched across conditions (±2%).
> - δ_A is matched (parameter count and FLOPs held constant).
> - σ_A differs significantly (SGG difference > 0.1, confirmed by bootstrap 95% CI non-overlap).
>
> *Step 4 — OOD evaluation.* Evaluate both conditions on the held-out OOD split. Prediction 1 is confirmed if the high-σ_A condition shows significantly higher Acc_OOD.

**JUSTIFICATION:** This places the experimental protocol directly in the benchmark section where researchers expect to find implementation details. The four-step structure (match, manipulate, verify, evaluate) is standard in experimental design and makes the protocol immediately actionable. The specific augmentation choices reference the benchmark families already defined in §8, maintaining internal consistency. This variant differs from Variant A by targeting the benchmark section rather than the predictions section, and from Variant C by providing a local protocol addition rather than a systemic new section.

**SAFETY NOTE:** This fix does NOT change: (a) any ODEs, (b) any coupling terms, (c) the SGG definition, (d) any V2.0/V3.0 extensions, (e) any §9 predictions. It adds a protocol paragraph to §8 only.

---

### VARIANT E

**Issue #:** 10
**Tag:** hackathon-priority-schema-coherence-protocol
**Section targeted:** §9 (Empirical Predictions) + Hackathon track files
**Scope:** Structural equation fix
**DIAGNOSIS:** The issue is not only that §9 lacks a protocol, but that the hackathon tracks (§Hackathon) do not operationalize the σ_A/δ_A manipulation as implementable Kaggle benchmarks. The [HACKATHON PRIORITY] tag indicates this issue's primary value is in enabling hackathon-ready evaluation protocols. A fix that connects §9 predictions to specific hackathon track designs directly addresses the tag's priority.

**PROPOSED FIX:**

*Replace Prediction 1 in §9 with:*

> **Prediction 1 (Schema Coherence Gap).** Agents matched on δ_A(d,t) but with higher σ_A(d,t) will show systematically higher accuracy on out-of-distribution recombination instances, with the gap widening as the OOD task requires deeper compositional recombination.
>
> **Kaggle evaluation protocol (Hackathon Track: Learning).**
> The following benchmark design operationalizes Prediction 1 as a Kaggle competition:
>
> *Task:* Given a trained agent A and a compositional domain D (SCAN, COGS, or PCFG-SET), predict the agent's OOD accuracy on a held-out recombination split.
>
> *Input features:*
> - $\tilde{\sigma}_A$ (Tier 1 proxy: augmentation consistency, Eq. 3d)
> - $\delta_A$ (parametric depth: total parameters × training steps)
> - Acc_In (in-distribution accuracy on training split)
> - Domain structural complexity C(D) (number of primitive types × max composition depth)
>
> *Target:* Acc_OOD on held-out recombination split.
>
> *Training data generation:*
> 1. For each of N = 100 agent configurations, apply Protocol P1 (structure-augmented) or Protocol P2 (surface-augmented) from §10.3.
> 2. Record $\tilde{\sigma}_A$, $\delta_A$, Acc_In, and Acc_OOD for each configuration.
> 3. Release (features, target) pairs as training data; withhold 20% as test set.
>
> *Evaluation metric:* Spearman correlation between predicted and actual Acc_OOD ranking. Baseline: predict Acc_OOD = Acc_In (ignoring σ_A). Prediction 1 is confirmed if the σ_A-informed predictor significantly outperforms the baseline (permutation test, p < 0.01).

*Also update hackathon/track_learning.md to add:*

> ### Benchmark P1: Schema Coherence Gap Prediction
> **Prediction tested:** Prediction 1 (σ_A gap at matched δ_A)
> **Protocol:** Kaggle evaluation protocol as specified in §9, Prediction 1.
> **Dataset:** 100 agent configurations × 3 domains (SCAN, COGS, PCFG-SET) = 300 data points.
> **Features:** $\tilde{\sigma}_A$, $\delta_A$, Acc_In, C(D).
> **Target:** Acc_OOD.
> **Metric:** Spearman ρ vs. baseline (Acc_OOD = Acc_In).
> **Success criterion:** σ_A-informed predictor achieves ρ > 0.6; baseline achieves ρ < 0.3.

**JUSTIFICATION:** This variant directly addresses the [HACKATHON PRIORITY] tag by converting Prediction 1 into an implementable Kaggle benchmark design. The protocol specifies exact features, targets, training data generation, and evaluation metrics — making it immediately actionable for hackathon participants. The update to hackathon/track_learning.md ensures the protocol is discoverable from the hackathon documentation. The design is self-contained: a researcher can generate the dataset, build a predictor, and evaluate against the baseline without additional specification.

**SAFETY NOTE:** This fix does NOT change: (a) any ODEs, (b) any coupling terms, (c) any benchmark families in §8, (d) any V2.0/V3.0 extensions, (e) any other predictions in §9. It modifies Prediction 1 in §9 and adds one benchmark subsection to hackathon/track_learning.md. No protected elements are touched.
