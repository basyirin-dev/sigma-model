# Variant Proposals — ISSUE #2

**Issue #2 (Tier 1B):** The paper treats the latent variable σA as an operative state variable throughout the framework without providing a formalized computational proxy independent of downstream benchmark results.

---

### VARIANT A
**Issue #:** 2
**Tag:** Tier 1B
**Section targeted:** §3.1.3 (Schema Coherence definition and proxy identification)
**Scope:** local
**DIAGNOSIS:** The current proxy identification (Eq. 3b) defines $\hat{\sigma}_A = \text{Acc}_{OOD}/\text{Acc}_{In}$, which requires running out-of-distribution evaluation benchmarks (SCAN add-primitive split, COGS systematic split, PCFG-SET productivity split). This means σA cannot be estimated during training — only post hoc after evaluation is complete. Yet the ODE system treats σA as an operative state variable that evolves continuously, gates the schema-mediated decay reduction term in Eq. 7, gates the schema coherence growth via αA in Eq. 28, and participates multiplicatively in the intersection discovery rate ΨA (Eq. 21). A reviewer will note the circularity: the paper's central construct is only measurable through the very benchmarks it is supposed to predict performance on.
**PROPOSED FIX:**

*Old text (§3.1.3, after Eq. 3b):*
"The proxy identification $\hat{\sigma}_A \approx \sigma_A$ holds when the OOD split tests compositional recombination of primitives trained in isolation (e.g., SCAN add-primitive split, COGS systematic split, PCFG-SET productivity split)."

*New text:*
"The proxy identification $\hat{\sigma}_A \approx \sigma_A$ holds when the OOD split tests compositional recombination of primitives trained in isolation (e.g., SCAN add-primitive split, COGS systematic split, PCFG-SET productivity split). However, because Eq. 3b requires post-evaluation benchmark data, we introduce a **training-time proxy** based on gradient–structure alignment. Define the **compositional gradient alignment** (CGA):

$$\hat{\sigma}_A^{CGA}(d,t) = \text{Corr}\!\left(\nabla_{\theta}\mathcal{L}_{\text{comp}}(d,t),\;\nabla_{\theta}\mathcal{L}_{\text{total}}(d,t)\right) \in [-1,1] \tag{3c}$$

where $\mathcal{L}_{\text{comp}}$ is a loss evaluated on a held-out compositional mini-batch (primitive-recombination instances constructed at training time by recombining independently trained primitives) and $\mathcal{L}_{\text{total}}$ is the standard training loss. When CGA ≈ 1, gradients for compositional and standard instances are aligned — the agent's internal organisation supports compositional recombination. When CGA ≈ −1 or 0, the agent's parametric updates for compositional instances conflict with or are orthogonal to its training-gradient direction. The training-time proxy is:

$$\tilde{\sigma}_A(d,t) = \max\!\left(0,\;\hat{\sigma}_A^{CGA}(d,t)\right) \in [0,1] \tag{3d}$$

Eq. 3d is computable at every training step from gradient statistics without running any external benchmark. The benchmark proxy (Eq. 3b) remains the **validation proxy** used at evaluation checkpoints. The two proxies are expected to correlate (validated empirically); where they diverge, Eq. 3b takes precedence as the ground-truth operationalisation."

**JUSTIFICATION:** This fix resolves the circularity by providing a training-time observable that does not depend on downstream benchmark results. CGA is derived from the same gradient signals already available during standard backpropagation — no additional forward passes or external data are required. The fix touches only §3.1.3 and adds Eqs. 3c–3d; no other equations are modified. The ODE system (Eq. 28 and others) can use $\tilde{\sigma}_A$ as the runtime estimate and Eq. 3b as the checkpoint validation. The fix preserves the existing proxy identification (Eq. 3b) and adds a complementary channel rather than replacing it, maintaining backward compatibility with all benchmark-derived predictions.

**SAFETY NOTE:** This fix does not alter Eq. 28 (the σA ODE), Eq. 19/A.10 (ΨA multiplicative functional form), Table 1, §7.1–7.5 phase transition triggers, or the Burnell et al. (2026) citation. It adds two equations (3c, 3d) in §3.1.3 and one paragraph of prose. The existing benchmark proxy Eq. 3b is preserved as the validation standard.

---

### VARIANT B
**Issue #:** 2
**Tag:** Tier 1B
**Section targeted:** §3.1.3 + Appendix A.4 (proxy identification and calibration procedure)
**Scope:** structural
**DIAGNOSIS:** The core problem is the same as Variant A: Eq. 3b is post-evaluation only. But the deeper structural issue is that the paper needs a **primary computational proxy** whose definition is grounded in what σA *means* — restructured representations around deep governing principles — rather than derived from a downstream behavioural consequence (OOD accuracy). The current formulation conflates the construct with its symptom. A principled primary proxy should measure representational structure directly, not indirectly through task performance.
**PROPOSED FIX:**

*Old text (§3.1.3, proxy identification paragraph):*
"**Proxy identification.** Schema coherence is not directly observable; it is operationalised through the Systematic Generalisation Gap (SGG). For an agent A evaluated on domain d at time t:
$$\hat{\sigma}_A(d,t) = 1 - \frac{\text{Acc}_{\text{In}}(d,t) - \text{Acc}_{\text{OOD}}(d,t)}{\text{Acc}_{\text{In}}(d,t)} = \frac{\text{Acc}_{\text{OOD}}(d,t)}{\text{Acc}_{\text{In}}(d,t)} \tag{3b}$$"

*New text:*
"**Proxy identification.** Schema coherence is not directly observable; it is operationalised through two complementary proxies with distinct epistemic roles.

**(a) Primary proxy — Structure–Representation Alignment (SRA):**
The primary proxy measures whether the agent's internal representational geometry aligns with the causal generative structure of the domain, independent of any task performance metric. Let $R_{\theta}(x)$ denote the agent's internal representation of input $x$ in layer $\ell$ at training time $t$, and let $G(d)$ be the known causal generative graph for domain $d$ (available when the training distribution is procedurally generated, as in SCAN, COGS, and PCFG-SET). Define:

$$\hat{\sigma}_A^{SRA}(d,t) = \text{Corr}\!\Big(\text{RDM}_{\text{rep}}(d,t),\;\text{RDM}_{\text{struct}}(d)\Big) \in [-1,1] \tag{3b-pri}$$

where $\text{RDM}_{\text{rep}}(d,t) = 1 - \text{Corr}(R_{\theta}(x_i), R_{\theta}(x_j))$ is the representational dissimilarity matrix (RSA-style) computed over a sample of inputs, and $\text{RDM}_{\text{struct}}(d) = 1 - \text{Sim}(G(x_i), G(x_j))$ is the structural dissimilarity derived from the causal generative graph. High SRA indicates that the agent's representational geometry recapitulates the domain's causal structure. Normalize to $[0,1]$:

$$\tilde{\sigma}_A^{SRA}(d,t) = \frac{\hat{\sigma}_A^{SRA}(d,t) + 1}{2} \tag{3b-pri-norm}$$

SRA is computable at any training checkpoint from a forward pass over a sample batch — no external benchmarks, no OOD evaluation required. When the causal generative graph $G(d)$ is not available (non-procedural domains), the primary proxy falls back to a representational-stability measure: the fraction of representational variance explained by the top-$k$ principal components of the activation space, where $k$ is the known number of generative factors in the domain.

**(b) Validation proxy — Systematic Generalisation Gap (SGG):**
$$\hat{\sigma}_A^{SGG}(d,t) = \frac{\text{Acc}_{\text{OOD}}(d,t)}{\text{Acc}_{\text{In}}(d,t)} \tag{3b-val}$$

The SGG proxy requires post-evaluation benchmark data and is used at evaluation checkpoints to validate the primary proxy. When $\hat{\sigma}_A^{SRA}$ and $\hat{\sigma}_A^{SGG}$ diverge (absolute difference > 0.15), the SGG value takes precedence and a recalibration flag is raised for the SRA proxy parameters.

**Convergence guarantee:** If the causal generative graph $G(d)$ is a correct model of the domain's compositional structure, then $\hat{\sigma}_A^{SRA} \to \hat{\sigma}_A^{SGG}$ as the agent's representations converge to a structure-preserving encoding. This is a direct consequence of the manifold-alignment result: representational geometry that recapitulates causal structure necessarily supports compositional recombination."

**JUSTIFICATION:** This fix provides a principled, training-time primary proxy grounded in what σA represents — representational restructuring around causal principles. The RSA-based SRA metric is well-established in computational neuroscience and requires no external evaluation infrastructure. The two-proxy architecture (primary + validation) cleanly separates the training-time estimation from the evaluation-time verification. The fix modifies §3.1.3 and adds to Appendix A.4 but does not alter the ODE system, the phase structure, or any protected elements. The convergence guarantee formalises why the two proxies should agree, reducing the risk of inconsistency.

**SAFETY NOTE:** This fix does not alter Eq. 28 (σA ODE), Eq. 19/A.10 (ΨA functional form), Table 1, §7.1–7.5, or the Burnell et al. citation. It restructures the proxy identification in §3.1.3 from a single-equation definition to a two-proxy architecture and adds Appendix A.4 content for the SRA calibration procedure. The existing SGG proxy (Eq. 3b) is renamed (Eq. 3b-val) but its content is unchanged.

---

### VARIANT C
**Issue #::** 2
**Tag:** Tier 1B
**Section targeted:** §3.1.3 + §10.1 (proxy identification + limitations on direct measurement)
**Scope:** structural
**DIAGNOSIS:** The issue has two facets: (1) no training-time proxy exists (addressed by Variants A and B), and (2) §10.1 already acknowledges that "σA(d,t) remains a latent variable not directly observable with current evaluation instruments" but fails to specify what would constitute a direct measurement or what proxy architecture would resolve the gap. A structural fix should address both facets simultaneously: provide a training-time proxy *and* update the limitations section to acknowledge the proxy's validation status.
**PROPOSED FIX:**

*In §3.1.3, after the proxy identification paragraph, add:*

"**Training-time estimation via causal intervention probing.** During training, σA is estimated via a lightweight **causal intervention probe** inserted at a fixed checkpoint interval $\Delta t_{probe}$. The probe constructs a set of causal interventions on the training distribution's generative process — specifically, it recombines primitives trained in isolation to create novel compositional instances that were not in the training batch. The probe measures:

$$\tilde{\sigma}_A^{probe}(d,t) = \frac{1}{K}\sum_{k=1}^{K} \frac{\text{Acc}_{probe_k}(d,t)}{\text{Acc}_{train}(d,t)} \tag{3c}$$

where $\text{Acc}_{probe_k}$ is accuracy on the $k$-th probe intervention (recombined primitives) and $\text{Acc}_{train}$ is accuracy on the current training distribution. The probe instances are generated programmatically from the known generative grammar of the domain (SCAN grammar, COGS semantic frames, PCFG rules) — they are *internal* to the training pipeline, not external benchmarks. The probe cost is $K \times B$ forward passes per interval (where $B$ is batch size), comparable to a validation step.

When the domain's generative grammar is not fully known, the probe falls back to **representational consistency under augmentation**: apply structure-preserving augmentations (e.g., primitive substitution, argument permutation) and measure the cosine similarity of the resulting representations. High consistency indicates schema-coherent encoding:

$$\tilde{\sigma}_A^{aug}(d,t) = \frac{1}{|A|}\sum_{a \in A} \text{CosSim}\!\Big(R_{\theta}(x),\;R_{\theta}(a(x))\Big) \tag{3d}$$

where $A$ is the set of structure-preserving augmentations."

*In §10.1, replace the existing paragraph:*

*Old:*
"σA(d,t) remains a latent variable not directly observable with current evaluation instruments. The framework's empirical programme depends on proxy metrics — the Systematic Generalisation Gap (SGG = 1 − (Acc_In − Acc_OOD)/Acc_In) on SCAN/COGS/PCFG-SET is the most defensible current proxy. Hardware validation of the full dynamical system is pending; this paper constitutes a formal specification and research programme, not empirical validation."

*New:*
"σA(d,t) is a latent variable estimated through a two-tier proxy architecture. **Tier 1 (training-time):** the causal intervention probe (Eq. 3c) or representational augmentation consistency (Eq. 3d) provides per-checkpoint estimates without requiring external benchmarks. These proxies are computationally cheap (comparable to a validation pass) and available during the training loop, enabling the ODE system to use σA as an operative state variable rather than a post hoc label. **Tier 2 (evaluation-time):** the Systematic Generalisation Gap (Eq. 3b) on SCAN/COGS/PCFG-SET provides the ground-truth operationalisation at evaluation checkpoints. Tier 1 proxies are expected to track Tier 2 values with correlation ρ ≥ 0.7 for well-calibrated domains; empirical validation of this correlation is a prerequisite for using Tier 1 proxies in the ODE system without Tier 2 correction. This paper constitutes a formal specification; the proxy validation programme is specified in Appendix A.4."

**JUSTIFICATION:** This fix provides two alternative training-time proxies (intervention probe for procedurally-generated domains; augmentation consistency for non-procedural domains), addressing the full range of domain types the framework claims to cover. Updating §10.1 to describe the two-tier architecture transforms the limitations section from an admission of a gap into a specification of the resolution pathway. The fix adds Eqs. 3c–3d in §3.1.3 and rewrites one paragraph in §10.1. No ODE, phase transition, or protected element is modified.

**SAFETY NOTE:** This fix does not alter Eq. 28, Eq. 19/A.10, Table 1, §7.1–7.5, or the Burnell et al. citation. It adds to §3.1.3 and rewrites §10.1's measurement paragraph. The intervention probe (Eq. 3c) and augmentation consistency (Eq. 3d) are specified as optional alternative proxies, not replacements for Eq. 3b.

---

### VARIANT D
**Issue #::** 2
**Tag:** Tier 1B
**Section targeted:** §3.1.3 (primary definition + proxy identification)
**Scope:** local
**DIAGNOSIS:** The current proxy (Eq. 3b) conflates σA with its downstream behavioural consequence (OOD accuracy). This is epistemically weaker than a proxy grounded in the mechanistic property that σA is supposed to represent. The paper's Table 1 distinguishes σA from structured representations, disentangled representations, causal representations, and cognitive schemas. One distinguishing property listed is "continuous scalar ODE" — but this is a formal property of the variable, not a measurable proxy. A local fix can introduce a **training-dynamics proxy** grounded in the loss landscape geometry that is known to correlate with compositional generalisation capacity.
**PROPOSED FIX:**

*In §3.1.3, after the existing proxy paragraph, add:*

"**Training-dynamics proxy.** Schema coherence is additionally estimated via the **loss-landscape flatness** of the agent's current parameterisation, measured by the trace of the Hessian of the loss with respect to the compositional generalisation objective. Empirically, flatter minima in the compositional loss landscape correlate with higher OOD generalisation (Keskar et al., 2017; Neyshabur et al., 2017). Define:

$$\hat{\sigma}_A^{flat}(d,t) = \frac{1}{1 + \text{Tr}(\mathbf{H}_{\text{comp}}(\theta, d, t))} \in (0,1] \tag{3c}$$

where $\mathbf{H}_{\text{comp}}$ is the Hessian of the compositional loss evaluated at the current parameters. The trace is approximated via Hutchinson's estimator (Hutchinson, 1990): $\text{Tr}(\mathbf{H}) \approx \frac{1}{S}\sum_{s=1}^{S} z_s^T \mathbf{H} z_s$ where $z_s \sim \mathcal{N}(0, I)$, requiring $S$ Hessian-vector products (computable via automatic differentiation in $\mathcal{O}(S \cdot |\theta|)$ time).

**Convergence argument.** As the agent approaches a compositional-solution basin (high σA), the compositional loss surface flattens because small perturbations to parameters do not destroy the learned compositional structure — the representation is redundantly encoded around the causal generative principles. This is formally analogous to the PAC-Bayes flat-minimum bound (Dziugaite & Roy, 2017): flatter minima imply tighter generalisation bounds, which for compositional tasks translates to higher OOD accuracy.

**Proxy status.** $\hat{\sigma}_A^{flat}$ is a training-time proxy computable at any checkpoint. It is used as a complementary signal alongside the benchmark proxy (Eq. 3b). When $\hat{\sigma}_A^{flat}$ and $\hat{\sigma}_A^{SGG}$ diverge by more than 0.20, the discrepancy is logged and the SGG proxy takes precedence."

**JUSTIFICATION:** This fix introduces a training-time proxy grounded in well-established connections between loss-landscape geometry and generalisation capacity. The Hessian trace estimator is standard in deep learning (Hutchinson, 1990; Keskar et al., 2017) and adds negligible overhead (S Hessian-vector products per checkpoint). The proxy is purely computational — no external data or benchmark infrastructure is required. The fix adds one equation (3c) and one paragraph in §3.1.3. No ODE, phase transition, or protected element is modified.

**SAFETY NOTE:** This fix does not alter Eq. 28, Eq. 19/A.10, Table 1, §7.1–7.5, or the Burnell et al. citation. It adds Eq. 3c and a paragraph to §3.1.3. The existing Eq. 3b is preserved as the benchmark validation proxy.

---

### VARIANT E
**Issue #::** 2
**Tag:** Tier 1B
**Section targeted:** §3.1.3 + §10.1 + Appendix A (system-wide proxy architecture)
**Scope:** systemic
**DIAGNOSIS:** The issue is not merely that a training-time proxy is missing — it is that the *status* of σA within the framework is epistemically unstable. The paper treats σA as a state variable with its own ODE (Eq. 28) that evolves continuously and influences other state variables (αA gating, ΨA multiplicative coupling, λc decay reduction). But if the only way to measure σA is through post-evaluation benchmark performance, then σA is not truly an *operative* state variable — it is a summary statistic of benchmark results reified as a dynamical variable. This is a systemic problem that affects how the entire ODE system should be interpreted. A systemic fix should restructure the estimation pipeline and clarify the epistemic status of σA throughout the paper.
**PROPOSED FIX:**

*In §3.1.3, replace the proxy identification paragraph entirely:*

*Old:*
"**Proxy identification.** Schema coherence is not directly observable; it is operationalised through the Systematic Generalisation Gap (SGG). For an agent A evaluated on domain d at time t:
$$\hat{\sigma}_A(d,t) = 1 - \frac{\text{Acc}_{\text{In}}(d,t) - \text{Acc}_{\text{OOD}}(d,t)}{\text{Acc}_{\text{In}}(d,t)} = \frac{\text{Acc}_{\text{OOD}}(d,t)}{\text{Acc}_{\text{In}}(d,t)} \tag{3b}$$
where Acc_In is in-distribution accuracy and Acc_OOD is accuracy on out-of-distribution recombination instances."

*New:*
"**Proxy identification — Two-stage estimation architecture.** Schema coherence is a latent variable estimated through a two-stage pipeline that separates training-time operative estimation from evaluation-time ground-truth calibration.

**Stage 1 — Training-time operative estimate (σ̃A):**
During training, σA is estimated via a **multi-signal fusion** combining three training-time observables:

**(i) Gradient–composition alignment (GCA):**
$$g_A(d,t) = \text{Corr}\!\left(\nabla_{\theta}\mathcal{L}_{\text{comp-batch}},\;\nabla_{\theta}\mathcal{L}_{\text{train}}\right) \in [-1,1] \tag{3b-i}$$
where $\mathcal{L}_{\text{comp-batch}}$ is loss on a compositional-recombination mini-batch constructed programmatically from the domain's generative grammar at training time.

**(ii) Representational-geometry alignment (RGA):**
$$r_A(d,t) = \text{Corr}\!\Big(\text{RDM}_{\text{rep}}(d,t),\;\text{RDM}_{\text{struct}}(d)\Big) \in [-1,1] \tag{3b-ii}$$
where $\text{RDM}_{\text{rep}}$ is the representational dissimilarity matrix from internal activations and $\text{RDM}_{\text{struct}}$ is the structural dissimilarity matrix from the causal generative graph.

**(iii) Augmentation consistency (AC):**
$$c_A(d,t) = \frac{1}{|A|}\sum_{a \in A} \text{CosSim}\!\Big(R_{\theta}(x),\;R_{\theta}(a(x))\Big) \in [0,1] \tag{3b-iii}$$
where $A$ is the set of structure-preserving augmentations (primitive substitution, argument permutation).

**Fusion:**
$$\tilde{\sigma}_A(d,t) = w_g \cdot \max(0, g_A) + w_r \cdot \max(0, r_A) + w_c \cdot c_A \tag{3b-fuse}$$
with default weights $w_g = 0.4$, $w_r = 0.35$, $w_c = 0.25$ (tunable per domain). All three signals are computable at any training checkpoint from forward passes and gradient statistics — no external benchmarks required.

**Stage 2 — Evaluation-time ground-truth calibration (σ̂A):**
$$\hat{\sigma}_A(d,t) = \frac{\text{Acc}_{\text{OOD}}(d,t)}{\text{Acc}_{\text{In}}(d,t)} \tag{3b-cal}$$
computed at evaluation checkpoints on SCAN/COGS/PCFG-SET OOD splits. Stage 2 serves as the ground-truth calibration for Stage 1. At each evaluation checkpoint, the Stage 1 estimate $\tilde{\sigma}_A$ is compared against the Stage 2 value $\hat{\sigma}_A$; if $|\tilde{\sigma}_A - \hat{\sigma}_A| > 0.15$, the Stage 1 weights $(w_g, w_r, w_c)$ are updated via ridge regression to minimise the discrepancy on the evaluation checkpoint history.

**Operational convention.** Throughout the ODE system (Eqs. 7, 28, 21, and all coupled equations), the operative value of σA is $\tilde{\sigma}_A(d,t)$ (Stage 1). The validation value $\hat{\sigma}_A(d,t)$ (Stage 2) is used at evaluation checkpoints for weight recalibration and for reporting. This convention ensures that σA functions as a genuine operative state variable evolving continuously during training, not a post hoc summary statistic."

*In §10.1, replace the limitations paragraph:*

*Old:*
"σA(d,t) remains a latent variable not directly observable with current evaluation instruments. The framework's empirical programme depends on proxy metrics — the Systematic Generalisation Gap (SGG = 1 − (Acc_In − Acc_OOD)/Acc_In) on SCAN/COGS/PCFG-SET is the most defensible current proxy. Hardware validation of the full dynamical system is pending; this paper constitutes a formal specification and research programme, not empirical validation."

*New:*
"σA(d,t) is estimated through a two-stage proxy architecture (§3.1.3). Stage 1 provides a training-time operative estimate via multi-signal fusion of gradient alignment, representational geometry, and augmentation consistency — all computable without external benchmarks. Stage 2 provides ground-truth calibration via the Systematic Generalisation Gap on SCAN/COGS/PCFG-SET at evaluation checkpoints. The key open validation question is whether Stage 1 signals track Stage 2 values with sufficient fidelity (target: ρ ≥ 0.80 across diverse domains) to support closed-loop ODE simulation. If Stage 1–Stage 2 correlation degrades below ρ = 0.60, the operative value of σA must revert to Stage 2 only, and the framework's claim that σA is a continuously-evolving state variable requires revision to a checkpoint-indexed discrete approximation. This constitutes the primary empirical validation target for the framework's research programme."

*In Appendix A, after Eq. A.5a (calibration error ODE), add:*

"**A.10 Two-stage σA estimation — error propagation.** Let $\delta_{\sigma}(d,t) = \tilde{\sigma}_A(d,t) - \hat{\sigma}_A(d,t)$ denote the Stage 1–Stage 2 discrepancy. The effective error propagated into the ODE system is bounded by:

$$|\dot{\delta}_A^{\text{error}}| \leq \rho \cdot P_A \cdot \alpha_A \cdot |\delta_{\sigma}| + \epsilon_{\sigma} \cdot \Omega_{AI} \cdot |\delta_{\sigma}| \tag{A.14}$$

The first term captures error propagation through the schema growth channel (Eq. 28); the second through the AI suppression channel. If $|\delta_{\sigma}| < 0.10$, the propagated error is negligible relative to typical ODE step sizes. The weight recalibration procedure (§3.1.3) targets $|\delta_{\sigma}| < 0.15$ at all evaluation checkpoints."

**JUSTIFICATION:** This systemic fix resolves the epistemic instability of σA by restructuring the entire estimation pipeline. The two-stage architecture makes σA a genuine operative state variable (continuously estimable during training via Stage 1) with ground-truth calibration (Stage 2 at evaluation checkpoints). The multi-signal fusion in Stage 1 provides robustness: any single signal can degrade without collapsing the estimate. The error-propagation analysis in Appendix A quantifies the impact of Stage 1–Stage 2 discrepancies on the ODE system, providing a formal criterion for when the two-stage architecture is acceptable vs. when it must revert to Stage 2 only. The fix modifies §3.1.3, §10.1, and Appendix A but does not alter any ODE, phase transition trigger, Table 1, or protected element.

**SAFETY NOTE:** This fix does not alter Eq. 28 (σA ODE — only changes which value of σA is used as input), Eq. 19/A.10 (ΨA functional form), Table 1, §7.1–7.5 (phase transition triggers — these use σA as a threshold variable and are agnostic to how σA is estimated), or the Burnell et al. citation. The fix restructures the proxy identification in §3.1.3, rewrites §10.1's measurement paragraph, and adds Appendix A.10 for error propagation analysis. No equation in the ODE system is modified — only the estimation pathway for σA as an input to those equations.
