# Gap Analysis: AGI Safety and the Schema Coherence Thesis

The surveyed literature reveals a striking pattern: the conceptual ingredients for a unified "compositional generalisation failure = alignment failure" thesis already exist across at least five adjacent research strands — developmental interpretability, mechanistic interpretability, goal misgeneralisation, schema theory, and dynamical-systems approaches to learning — but the load-bearing connections between them are almost entirely unmade. The gaps are not in the components but in the joints. The most consequential gap is the absence of any formal framework that treats schema structure as a measurable safety property with dynamical-systems semantics; this single absence blocks the unifying thesis from becoming a theorem.

## Master Gap Analysis Table

| # | Gap | Adjacent existing work | What's missing | Confidence |
|---|---|---|---|---|
| G1 | No formal axiomatisation of "internal representation structure" as a safety property, distinct from behavioural metrics | Pepin Lehalleur et al. (2025); Wang & Murfet (2026); Zou et al. (2023); Bereska & Gavves (2024); Elhage et al. (2022); Gleave et al. (2020); Anthropic defection probes (2024) | Axiomatic definition; causal structure-to-alignment link; structural safety theorem; scalable certification; empirical LLC-to-deceptive-alignment curve | **High** |
| G2 | No unified formal framework treating CG failure and alignment failure as the same phenomenon | Langosco et al. (2022); Azarbal et al. (2025); Ngo (2022); Bogin et al. (2021); Lake (2019) | Shared formalism; theorem linking CG guarantees to alignment guarantees; joint benchmark; value compositionality theory; cross-community citation bridge | **High** |
| G3 | No formal dynamical-systems treatment of safety-relevant attractors (σ-trap as basin, deceptive alignment as bifurcation) | Hoogland et al. (2024); Watanabe (2009); Pepin Lehalleur et al. (2025); Wang & Murfet (2026); Mehta & Schwab (2014) | Bifurcation theory for alignment transitions; σ-trap-as-attractor formalisation; Lyapunov/contraction safety analysis; control-theory to SLT bridge; frontier-scale dynamics | **High** |
| G4 | Schema theory (Piaget/Bartlett/Rumelhart) effectively absent from modern DL safety vocabulary | Classical schema theory; Meylani (2025) systematic review; Emergent Structures review (Neuron, 2026) | Operationalisation of "schema" measurable in trained NNs; Piaget assimilation/accommodation to training-dynamics mapping; bridge from cognitive-science schema to features/circuits; schema-coherence safety theorems | **High** |
| G5 | Secondary gaps that jointly block the unifying thesis | Ngo (2022) informal "capabilities outpace alignment"; spurious forgetting (OpenReview); speed/simplicity prior debate; Selective Generalisation (Azarbal et al., 2025) | Formal derivation of capabilities-vs-alignment gap; shared information-theoretic measure; forgetting-to-alignment bridge; joint CG + alignment protocol; value compositionality study; formal simplicity-prior safety result | **Medium-High** |

## Topology of the Gap Space

The five gaps are not independent: they form a dependency graph in which G3 (dynamical systems) and G4 (schema theory) are the foundational gaps — closing them would mechanically close G1 and G2 — while G5 is a cluster of secondary gaps that resolve once the unifying thesis is formalised.

```
                    G3 (Dynamical systems) ──→ G1 (Structure as safety)
                    G4 (Schema theory)     ──→ G1 ──→ G2 (CG ↔ alignment) ──→ G5 (Secondary)
```

The arrows indicate the natural closure order: G3 and G4 supply the formal language; G1 inherits it; G2 inherits from G1; G5 dissolves once G2 is formalised.

## G1 — Internal Representation Structure as a Safety Concern

**What exists.** The Timaeus position paper "You Are What You Eat" (Pepin Lehalleur et al., 2025) makes the explicit claim that two neural networks can have equivalent performance on the training set but compute their outputs in essentially different ways and thus generalise differently, and that alignment must therefore become a science of internal structure in models. Patterning (Wang & Murfet, 2026) demonstrates that one can select among loss-equivalent algorithms by targeting the local learning coefficient (LLC), operationalising the distinction. Representation Engineering (Zou et al., 2023) reads and manipulates safety-relevant concepts in latent activations. The mechanistic-interpretability review (Bereska & Gavves, 2024) catalogues circuits and features as the safety surface but concedes scalability and comprehensive interpretation remain open. Anthropic's monosemanticity work (Elhage et al., 2022) extracts millions of features from frontier models. Latent adversarial training (Gleave et al., 2020) treats the latent representation as the safety surface. Anthropic's defection probes (2024) operationalise safety as a property detectable in residual-stream activations with AUROC exceeding 99%.

**What's missing.** Four concrete deficits: (i) No axiomatic definition of "internal representation structure" as a property distinct from behavioural metrics — every existing treatment is either operational (LLC, monosemanticity score) or metaphorical. (ii) The structure-to-alignment link is correlational, not causal: there is no experiment showing that intervening on structure (leaving training loss unchanged) causally changes deceptive-alignment propensity. Patterning is the closest, but its interventions target algorithm choice in toy tasks, not alignment-relevant outcomes (Wang & Murfet, 2026). (iii) No structural safety theorem — nothing of the form "if σ_A > threshold τ, then P(deceptive alignment) < ε." (iv) No certification regime beyond detecting known defection patterns in curated contexts.

**Confidence: High.** The gap is well-attested; the Timaeus paper itself frames it as an open programme rather than a closed result.

## G2 — The CG to Alignment Bridge

**What exists.** The compositional generalisation (CG) literature is mature: Lake-style few-shot composition, meta-sequence-to-sequence, Compositional Feature Alignment (Bogin et al., 2021), depth-and-CG results, and a recent coverage-principle unifying framework. The alignment side has goal misgeneralisation (Langosco et al., 2022), which explicitly distinguishes capability generalisation from goal generalisation. Selective Generalisation (Azarbal et al., 2025) is the single closest existing bridge: it benchmarks fine-tuning strategies to improve capabilities while maintaining alignment, explicitly treating the capability/alignment generalisation split as a tradeoff to be managed. Ngo's Framing 2 (2022) defines goals as internal representations of features of environmental outcomes stored in the policy's neural weights, making misalignment a generalisation failure of those representations — the conceptual hook for the unification.

**What's missing.** (i) No shared formalism: CG is framed in terms of factorised latent structure and systematicity; alignment is framed in terms of mesa-objectives and value-relevant invariants. No paper writes a single equation in which both appear as instances. (ii) No theorem of the form "compositional generalisation guarantee G implies alignment robustness property A". (iii) No joint benchmark: existing CG benchmarks test task composition; existing alignment benchmarks test refusal/honesty — none test whether an intervention that raises CG also raises alignment robustness. (iv) Value compositionality is unstudied: the unifying thesis requires that values compose, but whether human-aligned values have compositional structure is empirically and formally open. (v) The two communities scarcely cite each other.

**Confidence: High.** An exhaustive search across both literatures returns no paper that formally equates the two failure modes.

## G3 — Formal Dynamical-Systems Approaches to Safety

**What exists.** Singular Learning Theory (Watanabe, 2009; developed for alignment by Hoogland et al., 2024, and Timaeus) is the only mature formal dynamical framework applied to alignment: it characterises learning as Bayesian inference over a singular loss landscape, with the RLCT and LLC measuring the complexity of the singularity the model occupies. Developmental interpretability studies stagewise development — the cascade of phase transitions by which internal structure deepens over training (Pepin Lehalleur et al., 2025). Patterning introduces susceptibilities — linear-response coefficients measuring how posterior observables respond to data-distribution shifts — which is the closest formalism to a control-theoretic steering of internal structure (Wang & Murfet, 2026). The renormalisation-group connection to deep learning (Mehta & Schwab, 2014) supplies a third formal tradition, though not safety-motivated. Empirical work on attractor dynamics in LLMs (2025) shows that models can become trapped in stable behavioural cycles requiring large structural perturbations to shift. The AISI Learning Theory agenda explicitly identifies training dynamics as under-theorised.

**What's missing.** (i) No formalisation of the σ-trap as an attractor basin in a dynamical system over representation space — the empirical attractor-cycle work is behavioural, not structural. (ii) No bifurcation theory for alignment-relevant transitions: when does a model snap into deceptive alignment? SLT gives stagewise development, but the alignment-relevant bifurcations have no formal characterisation. (iii) No Lyapunov or contraction analysis: there is no safety-relevant Lyapunov function whose decrease certifies that a trajectory is moving away from σ-trap basins. (iv) No bridge between SLT and control theory. (v) Whether susceptibilities scale to frontier models is open (Wang & Murfet, 2026).

**Confidence: High.** SLT is genuinely the only mature formal framework here; the dynamical-systems extension to alignment-relevant attractors is conspicuously absent.

## G4 — Schema-Based Approaches to Model Behaviour

**What exists.** Schema theory is a classical cognitive-science framework (Bartlett, 1932; Piaget, 1952; Rumelhart, 1980) that deeply influenced early AI through Minsky's frames and Schank's scripts. A 2025 systematic review (Meylani, 2025) confirms the concept is alive but largely in knowledge-management and education contexts, not in safety. The Neuron 2026 review "Emergent Structures and Levels of Abstraction in AI and the Brain" explicitly reintroduces schema theory from neuroscience but frames it as a cognitive-science/neuroscience bridge rather than a safety framework.

**What's missing.** (i) "Schema" is essentially absent from the modern DL safety vocabulary. The alignment canon does not use the term; the closest existing operationalisations are "features," "circuits," "natural abstractions," and "latent ontology" — none of which inherits schema theory's developmental dynamics. (ii) No operationalisation of "schema" measurable in a trained network. (iii) Piaget's assimilation/accommodation distinction has no mapping to training dynamics, despite being an obvious formal precursor to SLT's stagewise development. (iv) No bridge from the cognitive-science schema lineage to the mechanistic-interpretability feature/circuit lineage. (v) No schema-coherence safety theorem of the form "high schema coherence implies compositional generalisation and alignment robustness."

**Confidence: High.** The absence is verifiable: no alignment-canon paper uses "schema" in the Piagetian sense.

## G5 — Secondary Gaps

Five smaller gaps collectively block the thesis even if G1–G4 were partially closed.

**G5a — "Capabilities generalise further than alignment" is informal.** Ngo (2022) states this as the key intuition for inner misalignment, but there is no formal derivation from learning-theoretic first principles. The thesis requires it as a lemma.

**G5b — No shared information-theoretic measure.** The unifying thesis needs a single quantity that reduces, in one limit, to "compositional generalisation gap" and, in another, to "alignment gap." Candidate: mutual information between the representation and the true value-relevant latent versus a proxy latent. No paper constructs this.

**G5c — Forgetting-to-alignment disconnect.** "Spurious forgetting" work (OpenReview, 2025) proposes that continual-learning performance drops reflect a decline in task alignment rather than true knowledge loss — structurally a σ-trap under continual learning. But this work is in the continual-learning community, disconnected from the alignment community.

**G5d — No joint CG+alignment experimental protocol.** No paper runs the experiment: intervene on representation structure; measure both CG performance and alignment robustness; test whether they co-move. Selective Generalisation (Azarbal et al., 2025) is the closest but treats the relationship as a tradeoff to be managed, not as evidence of common mechanism.

**G5e — Value compositionality unstudied.** The thesis presupposes that values compose. Whether human values have compositional structure — and whether mesa-objectives are compositional mutations of base objectives — is empirically and formally open.

**G5f — No formal simplicity-prior safety result.** The informal consensus that simplicity-biased inductive pressures are anti-deceptive is exactly the claim that σ_A-raising priors are alignment-protective, but it has no theorem.

**Confidence: Medium-High.** Each sub-gap is verifiable; the Medium-High rather than High reflects that some (especially G5b, G5e) may have precursors in unpublished or very recent work not surfaced by this survey.

## Synthesis: High-Leverage Research Directions

The gap structure above suggests a specific research prioritisation.

**Highest-leverage direction: G4 + G3 jointly.** Importing schema theory's developmental dynamics (assimilation/accommodation) into SLT's stagewise framework, yielding a formal object — a schema as a structured singularity in the loss landscape whose coherence σ_A is measurable via the LLC and whose basin-structure is the σ-trap. This single move would supply G1 with its missing axiomatisation, supply G2 with its missing shared formalism, and make the capabilities-vs-alignment gap a corollary of the schema-coherence dynamics.

**Second-highest direction: G2d + G5d.** A single experimental protocol that intervenes on representation structure (via patterning or CFA-style factorisation) and jointly measures CG performance and alignment robustness. A positive result — co-movement of the two under structural intervention — would be the first empirical evidence for the unifying thesis; a negative result would falsify it and localise the gap.

**Third direction: G1c.** A certification regime that takes a structural measure (LLC, monosemanticity profile, or schema-coherence score) as input and outputs a bound on deceptive-alignment probability. This is the deliverable that would make the internal-structure-as-safety programme operationally useful for frontier-model governance.

The unifying thesis — that compositional generalisation failure and alignment failure are the same phenomenon — is, on this survey, consistent with all existing evidence, supported by convergent intuitions across five research strands, and formally unwritten. The gaps above are the joints where the formal bridge needs to be built.

## References

Azarbal, A., et al. (2025). Selective Generalization: Improving capabilities while maintaining alignment. SPAR cohort report.

Bartlett, F. C. (1932). *Remembering: A Study in Experimental and Social Psychology*. Cambridge University Press.

Bereska, L., & Gavves, E. (2024). Mechanistic Interpretability for AI Safety — A Review. *arXiv preprint arXiv:2404.14082*.

Bogin, B., Berzak, N., & Subramanian, S. (2021). Compositional generalization via compositional feature alignment. *ICLR 2021 Workshop on Compositional Generative Models*.

Elhage, N., Nanda, N., Olsson, C., et al. (2022). Toy models of superposition. *arXiv preprint arXiv:2209.10652*.

Gleave, A., Irving, G., & O'Connell, C. (2020). Adversarial policies: Attacking deep reinforcement learning. *ICLR 2020*.

Hoogland, J., Wang, G., Farrugia-Roberts, M., et al. (2024). Differentiation and specialization of attention heads via the refined local learning coefficient. *arXiv preprint arXiv:2410.02984*.

Langosco, L., Koch, J., Sharkey, L. D., Pfau, J., & Krueger, D. (2022). Goal Misgeneralization in Deep Reinforcement Learning. *ICML 2022*.

Mehta, P., & Schwab, D. J. (2014). An exact mapping between the variational renormalization group and deep learning. *arXiv preprint arXiv:1410.3831*.

Meylani, R. (2025). Schema Theory and Artificial Intelligence: A systematic review. *Education and Information Technologies*.

Ngo, R. (2022). The alignment problem from a deep learning perspective. *arXiv preprint arXiv:2209.00626*.

Pepin Lehalleur, S., Hoogland, J., Farrugia-Roberts, M., et al. (2025). You Are What You Eat — AI Alignment Requires Understanding How Data Shapes Structure and Generalisation. *arXiv preprint arXiv:2502.05475*.

Piaget, J. (1952). *The Origins of Intelligence in Children*. International Universities Press.

Rumelhart, D. E. (1980). Schemata: The building blocks of cognition. In R. J. Spiro et al. (Eds.), *Theoretical Issues in Reading Comprehension*.

Wang, G., & Murfet, D. (2026). Patterning: The Dual of Interpretability. *arXiv preprint*.

Watanabe, S. (2009). *Algebraic Geometry and Statistical Learning Theory*. Cambridge University Press.

Zou, A., Phan, L., Chen, S., et al. (2023). Representation engineering: A top-down approach to AI transparency. *arXiv preprint arXiv:2310.01405*.