# AI Interpretability and AGI Safety

AI interpretability relates to AGI safety through three main facets: methods for understanding models, evidence that understanding helps safety, and gaps about when it is enough (Shah et al., 2025; Lee et al., 2025). The field is broad, but the strongest current safety-relevant work clusters around mechanistic interpretability, post hoc analysis tools, and causal frameworks for testing whether explanations are faithful (Bereska & Gavves, 2024; Geiger et al., 2023).

## Mechanistic Interpretability

Mechanistic interpretability aims to reverse-engineer a network into human-understandable algorithms, features, and computations — rather than only explaining outputs (Bereska & Gavves, 2024; Gantla, 2025). It treats neural networks as physical systems to be reverse-engineered into human-understandable code, providing the necessary tools to audit a model's internal cognitive processes for signatures of deception, manipulation, or situational awareness.

### Circuit Discovery

A major result is **circuit discovery**: automated methods can recover sparse subgraphs linked to specific behaviors. The ACDC (Automatic Circuit DisCovery) algorithm rediscovered all five component types in a GPT-2 Greater-Than circuit while selecting 68 of 32,000 edges (Conmy et al., 2023). This builds on foundational circuit analysis by Wang et al. (2022), who reverse-engineered the Indirect Object Identification (IOI) circuit in GPT-2 Small, mapping distinct attention heads to specific algorithmic subtasks (duplicate token detection, name mover, and induction heads).

Olah et al. (2020) established the "circuits" paradigm in **Zoom In: An Introduction to Circuits**, proposing that neural network representations could be rigorously decomposed into universal computational units. This transitioned the field from speculative black-box probing to rigorous inner interpretability.

### Features, Superposition, and Polysemanticity

**Features** are treated as the basic carriers of knowledge in activations, and current work increasingly studies modular features rather than isolated neurons (Bereska & Gavves, 2024; Geiger et al., 2023). Neuron-level interpretations are often limited by **polysemanticity** — individual neurons respond to multiple unrelated concepts — and **superposition**, where models represent more features than they have dimensions by encoding features in overlapping, sparse ways (Elhage et al., 2022; Gantla, 2025).

Elhage et al. (2022) introduced "Toy Models of Superposition," demonstrating mathematically that models exploit superposition to represent $O(d^2)$ features in $d$ dimensions when features are sparse. This explains why single-neuron interpretability is fundamentally limited and motivates feature-level rather than neuron-level analysis.

### Benchmarking Methods

Attribution and mask optimization currently perform best on circuit localization benchmarks, while supervised DAS (Distributed Alignment Search) performs best for causal variable localization. Notably, SAE features were not better than neurons on the MIB (Mechanistic Interpretability Benchmark) (Mueller et al., 2025).

## Probes and Diagnostic Classifiers

Probes — classifiers trained on hidden representations to predict specific properties — serve as a primary tool for determining what information a model's internal states encode. Linear probes have been used extensively to detect concepts such as truthfulness, sentiment, and factual knowledge in LLM activations.

However, probe evidence has a crucial limitation: a probe can detect information in representations that the model does not actually use causally in its computations. This is the distinction between **correlational** and **causal** interpretability. The field has increasingly moved toward causal methods (activation patching, causal abstraction) over pure probing.

The evidence coverage for probes in safety-relevant contexts remains limited compared to mechanistic interpretability (see coverage table).

## Concept-Based Explanations

Concept-based methods extend beyond local saliency by linking semantic concepts to internal representations globally, which can expose bias, concept entanglement, and latent information flow (Chorna et al., 2025).

Rather than explaining individual predictions, concept-based approaches identify high-level human-interpretable concepts (e.g., "honesty," "deception," "harm") that are encoded across distributed activations. These methods are particularly relevant for safety because they can potentially detect dangerous concepts (like power-seeking or deception) that may not manifest in any single output but are present in the model's internal geometry.

## Causal Abstraction

Causal abstraction provides a theoretical foundation for mechanistic interpretability (Geiger et al., 2023, *JMLR*). It formalizes the notion of an "interpretable model" as a causal model that faithfully represents the computation performed by the neural network.

The framework defines **interchange intervention accuracy**: if swapping representations at a given level of abstraction changes the model's output in the way the causal model predicts, then the abstraction is faithful. This provides a rigorous test for whether an interpretation genuinely captures the model's computation rather than being a post-hoc rationalization.

Causal abstraction distinguishes between:
- **Causal variable localization**: identifying the right level of analysis (features, circuits, subroutines)
- **Circuit localization**: identifying the specific edges and nodes involved in a computation

## Influence Functions and Attribution

Attribution methods assign credit for a model's output to specific input features, neurons, or layers. Standard techniques include saliency maps, gradient-based attribution, and layer-wise relevance propagation.

In the context of mechanistic interpretability, attribution methods (such as attribution patching) have been shown to outperform more complex automated circuit discovery methods on several benchmarks (Syed et al., 2024). However, post-hoc attribution methods face fundamental challenges:

- **Instability**: small input perturbations can produce dramatically different attributions
- **Unfaithfulness**: attributions may highlight features that are correlated with the output but not causally implicated
- **Misleading confidence**: attribution maps can encourage over-trust in model decisions (Singh et al., 2025)

## The Safety Connection — Does Understanding Make Models Safer?

Interpretability appears to help safety when it increases the ability to **audit, localize, and intervene** on unsafe internal processes (Shah et al., 2025; Shi et al., 2024). Safety arguments in AGI work explicitly treat interpretability as an enabler of control, monitoring, and future safety cases, including the possibility of detecting internal circuits that precede deception or other undesirable actions (Shah et al., 2025).

### Specific Safety Contributions

**LLM safety**: Interpretability is used for understanding capabilities, auditing unsafe factors, and locating or editing unsafe content representations (Shi et al., 2024). Representation engineering (Zou et al., 2023) and circuit-breaker approaches (Zou et al., 2024) directly manipulate internal activations to improve safety, building on interpretability findings.

**Applied safety-critical systems**: Interpretable intermediate features and attention outputs have improved debugging and sometimes operational safety, as shown in autonomous driving studies (Shao et al., 2022; Nan et al., 2025).

**Quantitative safety arguments**: Model structure can simplify safety assessment, such as computing or bounding maximum deviation from a safe reference (Wei et al., 2022).

### The Double-Edged Sword

But the evidence also shows that explanation methods can mislead users, encourage over-trust, or even improve capabilities — transparency is not automatically safety-improving (Singh et al., 2025; Bereska & Gavves, 2024). For example, an interpretability method that reveals how a model performs a dangerous capability (e.g., chemical synthesis planning) could accelerate misuse. Interpretability also reveals information about model internals that could be used to construct more sophisticated adversarial attacks.

## Evidence Coverage

| Sub-Topic | Peer-Reviewed Evidence | Mechanistic Faithfulness | Direct Safety Link | Long-Term AGI Relevance |
|-----------|----------------------|------------------------|-------------------|------------------------|
| Mechanistic interpretability | Strong | Strong | Moderate | Strong |
| Probes and diagnostic tools | Moderate | Limited | Moderate | Limited |
| Concept-based explanations | Moderate | Moderate | Moderate | Limited |
| Attribution and influence methods | Strong | Moderate | Moderate | Limited |
| Built-in safety-by-design | Moderate | Limited | Moderate | Moderate |

The most striking gap is **direct evidence** that better interpretability yields safer frontier models under realistic AGI threat models. Reviews argue that understanding internals should make safety easier, but they also stress that substantial progress is still needed before interpretability can support strong safety cases or verification-style guarantees (Shah et al., 2025).

Another persistent gap is **faithfulness**: post hoc methods can be unstable or misleading, which is why several papers argue for built-in transparency or causal testing rather than relying on explanations alone (Singh et al., 2025; Wei et al., 2022).

## Known Gaps and Debates

### Is Interpretability Necessary for AGI Safety?

Interpretability is **probably not necessary in one fixed form**, since some safety gains can come from behavioral evaluation, verification, or inherently safer architectures without deep post hoc explanation (Shah et al., 2025; Wen, 2025). A model could be safe without being interpretable if it is provably constrained, verifiably aligned, or deployed with sufficient control measures.

### Is Interpretability Sufficient for AGI Safety?

Interpretability is **not sufficient** for AGI safety because safety also needs monitoring, access control, robustness, governance, and possibly formal verification (Shah et al., 2025; Tegmark & Omohundro, 2023). Understanding a model's internals does not guarantee that it will not cause harm — it only provides the visibility to detect and diagnose problems.

### Neuron-Level vs Circuit-Level

Current evidence favors circuits and causal pathways over single neurons because distributed representations, polysemanticity, and superposition make isolated neuron stories fragile (Geiger et al., 2023; Mueller et al., 2025). The field has largely moved from "neuron-atlas" approaches (mapping single neurons to concepts) toward circuit-level analysis that captures distributed computation.

### Post-Hoc vs Built-In Interpretability

Post hoc tools remain widely used, but evidence from medical imaging and safety theory warns that they can create misleading confidence unless paired with uncertainty estimates or structurally interpretable designs (Singh et al., 2025). Several research programs advocate for "built-in" interpretability — architectures that are transparent by design rather than requiring post-hoc explanation.

### Local vs Global Explanations

Local explanations help inspect single decisions, while global concept-based approaches better reveal recurring bias, entanglement, and system-level failure modes (Chorna et al., 2025). For safety auditing, global methods are arguably more important, as they can detect systematic unsafe patterns that local explanations would miss.

## Synthesis

The field increasingly treats interpretability as a **supporting layer** for auditing and control, not a standalone guarantee of alignment or harmlessness (Shah et al., 2025; Wei et al., 2022). Its primary safety value lies in enabling:

1. **Detection of hidden capabilities** — mechanistic interpretability can discover whether a model has dangerous capabilities (e.g., situational awareness, strategic reasoning) that are not apparent from behavioral testing alone.
2. **Diagnosis of failure modes** — when a model behaves unsafely, interpretability can help determine why and guide targeted fixes.
3. **Verification of safety properties** — causal abstraction can test whether a model implements a specified safe algorithm.
4. **Editing of unsafe representations** — representation engineering and circuit editing can directly modify internal states to remove unsafe patterns.

Overall, AI interpretability is relevant to AGI safety because it can expose internal mechanisms, support auditing, and sharpen safety cases, but current evidence does not show that interpretability alone is necessary or sufficient for safe AGI.

## References

Bereska, L., & Gavves, E. (2024). Mechanistic interpretability for AI safety — a review. *arXiv:2404.14082*.

Chorna, S., Tarelkina, K., Berthier, E., & Franchi, G. (2025). Concept-based mechanistic interpretability using structured knowledge graphs. *arXiv:2507.05810*.

Conmy, A., Mavor-Parker, A. N., Lynch, A., Heimersheim, S., & Garriga-Alonso, A. (2023). Towards automated circuit discovery for mechanistic interpretability. *arXiv:2304.14997*.

Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S., ... & Olah, C. (2022). Toy models of superposition. *Transformer Circuits*.

Gantla, S. R. (2025). Exploring mechanistic interpretability in large language models: Challenges, approaches, and insights. *ICDSAAI 2025*, 1–8. https://doi.org/10.1109/icdsaai65575.2025.11011640

Geiger, A., Ibeling, D., Zur, A., Chaudhary, M., Chauhan, S., Huang, J., ... & Icard, T. F. (2023). Causal abstraction: A theoretical foundation for mechanistic interpretability. *Journal of Machine Learning Research*, 26, 83:1–83:64.

Lee, S., Cho, A., Kim, G. C., Peng, S.-H., Phute, M., & Chau, D. H. (2025). Interpretation meets safety: A survey on interpretation methods and tools for improving LLM safety. *arXiv:2506.05451*.

Mueller, A., Geiger, A., Wiegreffe, S., Arad, D., Arcuschin, I., Belfki, A., ... & Belinkov, Y. (2025). MIB: A mechanistic interpretability benchmark. *arXiv:2504.13151*.

Nan, J., Zhang, R., Yin, G., Zhuang, W., Zhang, Y., & Deng, W. (2025). Safe and interpretable human-like planning with transformer-based deep inverse reinforcement learning for autonomous driving. *IEEE Transactions on Automation Science and Engineering*, 22, 12134–12146. https://doi.org/10.1109/tase.2025.3539340

Olah, C., Cammarata, N., Schubert, L., Goh, G., Petrov, M., & Carter, S. (2020). Zoom in: An introduction to circuits. *Distill*. https://distill.pub/2020/circuits/zoom-in/

Shah, R., Irpan, A., Turner, A. M., Wang, A., Conmy, A., Lindner, D., ... & Dragan, A. (2025). An approach to technical AGI safety and security. *arXiv:2504.01849*.

Shao, H., Wang, L., Chen, R., Li, H., & Liu, Y. (2022). Safety-enhanced autonomous driving using interpretable sensor fusion transformer. *arXiv:2207.14024*.

Shi, D., Shen, T., Huang, Y., Li, Z., Leng, Y., Jin, R., ... & Xiong, D. (2024). Large language model safety: A holistic survey. *arXiv:2412.17686*.

Singh, Y., Hathaway, Q. A., Keishing, V., Salehi, S., Wei, Y., Horvat, N., ... & Andersen, J. (2025). Beyond post hoc explanations: A comprehensive framework for accountable AI in medical imaging. *Bioengineering*, 12(8). https://doi.org/10.3390/bioengineering12080879

Syed, A., Rager, C., & Conmy, A. (2024). Attribution patching outperforms automated circuit discovery. *BlackboxNLP Workshop at ACL 2024*. https://doi.org/10.18653/v1/2024.blackboxnlp-1.25

Tegmark, M., & Omohundro, S. (2023). Provably safe systems: The only path to controllable AGI. *arXiv:2309.01933*.

Wang, K., Variengien, A., Conmy, A., Shlegeris, B., & Steinhardt, J. (2022). Interpretability in the wild: A circuit for indirect object identification in GPT-2 small. *arXiv:2211.00593*.

Wei, D., Nair, R., Dhurandhar, A., Varshney, K. R., Daly, E. M., & Singh, M. (2022). On the safety of interpretable machine learning: A maximum deviation approach. *arXiv:2211.01498*.

Wen, B. (2025). A framework for inherently safer AGI through language-mediated active inference. *arXiv:2508.05766*.

Zou, A., Phan, L., Wang, J., Carlini, N., Hendrycks, D., & Kolter, J. Z. (2024). Improving alignment and robustness with circuit breakers. *arXiv:2406.04313*.
