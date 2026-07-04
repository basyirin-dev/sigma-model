# Landmark Papers: Compositional Generalization and OOD Failure in Deep Neural Networks

**Document type:** Reference — search calibration for systematic review Phase 2
**Purpose:** These papers must be captured by search strings in Phase 2
**Status:** Draft

---

## Part I: Seminal Diagnostic Benchmarks of Compositional Generalization Failure

### 1. Lake & Baroni (2018) — SCAN

- **Citation:** Lake, B. M., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *Proceedings of ICML*.
- **Year:** 2018
- **Task / Benchmark:** SCAN — maps structured natural language commands (e.g., "turn left twice and jump around right") into discrete agent action sequences (e.g., LTURN LTURN RTURN JUMP RTURN JUMP RTURN JUMP RTURN JUMP).
- **Model type tested:** Sequence-to-sequence RNNs (vanilla RNN, GRU, LSTM).
- **Key OOD finding:** Near-perfect accuracy (99.8%) on random train-test splits, but catastrophic failure on systematic splits. On the primitive addition split (trained on "jump" in isolation, all other verbs in complex structures), achieved 0–1.2% zero-shot generalization on commands like "jump twice" or "jump around right."
- **Internal representation analysis:** Projected word embeddings and discovered that the network failed to align the representation of the newly introduced primitive ("jump") with established verb embeddings. The embedding was geometrically isolated, preventing the recurrent decoder from leveraging similarity-driven structural composition.
- **Intervention proposed:** None. Designed as a diagnostic benchmark to establish the systematicity gap.
- **Citation count:** ~916

---

### 2. Kim & Linzen (2020) — COGS

- **Citation:** Kim, J., & Linzen, T. (2020). COGS: A Compositional Generalization Challenge Based on Semantic Interpretation. *Proceedings of EMNLP*.
- **Year:** 2020
- **Task / Benchmark:** COGS — semantic parsing benchmark mapping English sentences (e.g., "A hedgehog ate the cake") into formal lambda-calculus logical forms. Contains systemic gaps isolating structural recursion and lexical shifts.
- **Model type tested:** Transformer, Sequence-to-Sequence LSTM.
- **Key OOD finding:** Near-perfect ID accuracy (96–99%), but OOD generalization accuracy drops to 16–35%. Failures were highly seed-sensitive (std dev 6–8%). Models performed reasonably on lexical generalization but failed completely on structural generalization (e.g., prepositional phrase modifiers on subjects when only objects were seen in training).
- **Internal representation analysis:** Probed behavioral error trajectories and structural dependencies, demonstrating that standard sequence decoders overfit to absolute position coordinates of nominal variables.
- **Intervention proposed:** None. Diagnostic benchmark.
- **Citation count:** Highly Influential (widespread adoption in NLP evaluation)

---

### 3. Keysers et al. (2020) — CFQ

- **Citation:** Keysers, D., Schärli, N., Aksu, S., Tarber, D., Buisson, H., Saadatpanah, P., Driessens, K., & Weber, L. (2020). Measuring Compositional Generalization: A Comprehensive Method on Realistic Data. *Proceedings of ICLR*.
- **Year:** 2020
- **Task / Benchmark:** CFQ (Compositional Freebase Questions) — semantic parsing from natural language questions (e.g., "Did the male actor of Lohengrin marry Margarete Joswig?") to SPARQL queries on Freebase.
- **Model type tested:** LSTMs with attention, Transformers, Evolved Transformers, Universal Transformers.
- **Key OOD finding:** Under Maximum Compound Divergence (MCD) splits — which maximize train/test divergence over larger structures while keeping individual rule distributions similar — all models collapsed to 5–37%.
- **Internal representation analysis:** Studied output serialization patterns; demonstrated that standard models learn strong linear ordering biases rather than capturing permutation-invariant properties of logical semantic conjuncts.
- **Intervention proposed:** Automated MCD split generation algorithm to systematically measure and control dataset compositionality.
- **Citation count:** ~300+

---

### 4. Hupkes et al. (2020) — PCFG-SET

- **Citation:** Hupkes, D., Veldhoen, S., & Zuidema, W. (2020). Compositional Generalization and Natural Language Processing: Explaining Category-Level Multi-Task Generalization. *arXiv:2006.15951*.
- **Year:** 2020
- **Task / Benchmark:** PCFG-SET — a highly compositional string transduction dataset used to instantiate five structurally grounded tests.
- **Model type tested:** LSTM, Convolutional Seq2Seq, Transformer.
- **Key OOD finding:** All models exhibited severe multi-dimensional systematicity deficits: significant drops in productivity (length generalization) and substitutivity (synonym behavior in varying contexts) under low-exposure conditions.
- **Internal representation analysis:** Five structurally grounded tests: systematicity (recombining known parts), productivity (length extrapolation), substitutivity (synonym behavior), localism (sub-expression invariance in nested compounds), and overgeneralization (misapplication of structured rules to irregular exceptions).
- **Intervention proposed:** None. Theoretical framework for evaluating compositionality.
- **Citation count:** ~150+

---

### 5. Ruis et al. (2020) — gSCAN

- **Citation:** Ruis, L., Andreas, J., Baroni, M., & Lake, B. M. (2020). A Benchmark for Systematic Generalization in Grounded Language Understanding. *Proceedings of NeurIPS*.
- **Year:** 2020
- **Task / Benchmark:** gSCAN (Grounded SCAN) — extends SCAN into a situated multimodal setting with 2D grid world navigation, distinct object shapes, sizes, and colors.
- **Model type tested:** Multimodal CNN-LSTM seq2seq, compositional architectures.
- **Key OOD finding:** Standard models failed catastrophically on Split D (novel spatial directions) and Split H (adverb-verb generalization, e.g., "cautiously" + "spin" when held out). Exact match trajectory accuracies dropped to near 0%.
- **Internal representation analysis:** Visualized cross-modal attention maps and tracked visual coordinate alignments. Models failed to decouple adjectival and adverbial modifiers from the visual context in which they were originally trained.
- **Intervention proposed:** None. Positioned as open visual-linguistic reasoning challenges.
- **Citation count:** 156

---

### 6. An et al. (2023) — CoFe

- **Citation:** An, S., et al. (2023). How Do In-Context Examples Affect Compositional Generalization? *Proceedings of ACL*.
- **Year:** 2023
- **Task / Benchmark:** CoFe (Compositional Few-shot Evaluation) — built on COGS grammar; evaluates in-context learning compositional generalization.
- **Model type tested:** GPT series LLMs (davinci, code-cushman-001/002, text-davinci-002, text-chat-davinci-002, code-davinci-002).
- **Key OOD finding:** In-context compositional generalization is highly fragile and prompt-sensitive. When prompts cover only basic primitives, davinci (175B) lags fine-tuned GPT-2 Large by 24.2% in parsing accuracy. LLMs showed severe limitations generalizing over fictional/novel words, indicating pretraining weights heavily dominate in-context structural mappings.
- **Internal representation analysis:** Systematically replaced standard English words with fictional tokens (e.g., "dax", "lug") to analyze pretraining weight interference with abstract, rule-based syntactic patterns.
- **Intervention proposed:** CoFe prompt selection framework optimizing exemplars along three dimensions: high structural similarity to test case, high diversity among examples, low individual complexity.
- **Citation count:** Emerging

---

### 7. Qiu et al. (2022) — COGS-γ / COGS-vf

- **Citation:** Qiu, L., et al. (2022). Evaluating the Impact of Model Scale for Compositional Generalization in Semantic Parsing. *Proceedings of EMNLP*.
- **Year:** 2022
- **Task / Benchmark:** COGS, GeoQuery — investigated whether parameter scaling resolves systematic OOD failures in semantic parsing.
- **Model type tested:** T5 (Base through 3B), BART.
- **Key OOD finding:** Scaling parameter volume leads to massive improvements on lexical OOD splits, but leaves structural generalization splits (nested subject modifiers) largely unresolved, with accuracies remaining near 0% even for multi-billion parameter models.
- **Internal representation analysis:** Evaluated model checkpoint trajectories and pretraining losses, demonstrating that deeper models attain lower pretraining perplexity but still fail to develop the representational geometry required for structural recursion OOD.
- **Intervention proposed:** Variable-Free COGS (COGS-vf) — removing numbered index variables from target lambda-calculus representations reduces output space complexity, dramatically improving structural generalization.
- **Citation count:** ~80+

---

### 8. Bahdanau et al. (2019) — SQOOP

- **Citation:** Bahdanau, D., et al. (2019). Systematic Generalization: What Is Required and Can It Be Learned? *Proceedings of ICLR*.
- **Year:** 2019
- **Task / Benchmark:** SQOOP (Spatial Queries on Object Pairs) — visual relational reasoning over images containing randomly scattered letters and digits (e.g., "Is A left of 3?").
- **Model type tested:** Relation Networks, FiLM, Neural Module Networks (NMNs).
- **Key OOD finding:** Standard unconstrained models fail to generalize to unseen object pairs even when all individual objects and spatial relations were seen during training.
- **Internal representation analysis:** Probed sharpness and modularity of intermediate representations within NMN routing layers. When trained end-to-end, individual modules "collapsed," failing to maintain functional boundaries and learning entangled representations of both object identity and spatial position.
- **Intervention proposed:** Vector-NMN — constrains module interfaces to pass compact, vector-valued messages rather than large spatial tensors, forcing decoupling of object categorization from spatial localization.
- **Citation count:** 245

---

### 9. Bahdanau et al. (2020) — CLOSURE

- **Citation:** Bahdanau, D., et al. (2020). CLOSURE: Assessing Systematic Generalization of CLEVR Models. *Proceedings of NeurIPS*.
- **Year:** 2020
- **Task / Benchmark:** CLOSURE — extends CLEVR-VQA to test understanding of referring expressions based on matching object properties in novel, nested contexts (e.g., "the object that has the same size as the red ball").
- **Model type tested:** MAC, FiLM, standard NMNs.
- **Key OOD finding:** Despite 97–99% accuracy on standard CLEVR, models fail zero-shot when evaluating identical reference rules in nested configurations.
- **Internal representation analysis:** Evaluated visual-attentional map projections and tracked coordinate variable flow across nested syntax paths. Models overfit to dominant training pathways, failing to route semantic information along novel syntactic tree branches.
- **Intervention proposed:** Vector-NMN — restricting interfaces to low-dimensional vector representations forces dynamic signal routing using discrete syntactic trees.
- **Citation count:** ~100+

---

### 10. Li et al. (2023) — SLOG

- **Citation:** Li, Y., Wang, Z., & Li, Y. (2023). SLOG: A Structural Generalization Benchmark for Semantic Parsing. *arXiv*.
- **Year:** 2023
- **Task / Benchmark:** SLOG — extends COGS with 17 challenging structural generalization cases.
- **Model type tested:** Standard Transformers, pretrained LMs, specialized structure-aware parsers.
- **Key OOD finding:** Pretrained models achieving near-perfect COGS performance drop to 40.6% on SLOG structural OOD splits. Even specialized parsers fail to cross 70.8%.
- **Internal representation analysis:** Probed self-attention patterns at varying recursive parsing depths. Standard Transformers fail to maintain structural coherence when prepositional phrase modifiers modify noun phrases in novel positions — internal representations collapse during deep syntactic nesting.
- **Intervention proposed:** None. Diagnostic benchmark.
- **Citation count:** Emerging

---

## Part II: Probing and Analytical Studies of Compositional Breakdown

### 11. Loula, Baroni & Lake (2018) — SCAN Rearranged

- **Citation:** Loula, J., Baroni, M., & Lake, B. M. (2018). Rearranging the Familiar: Testing Compositional Generalization in Recurrent Networks. *EMNLP Workshop*.
- **Year:** 2018
- **Task / Benchmark:** Repurposed SCAN splits requiring combination of familiar primitives with familiar modifiers in novel contexts (e.g., "jump around right" when meanings of "jump", "right", "around" were all seen in other combinations).
- **Model type tested:** LSTM seq2seq with 50% dropout.
- **Key OOD finding:** Recurrent networks fail to combine familiar primitive verbs with familiar modifiers in novel contexts.
- **Internal representation analysis:** Demonstrated that the LSTM's hidden state representations for functional adverbs (e.g., "around", "opposite") are heavily entangled with specific verb templates seen during training. Second-order modifiers cannot execute compositionally when combined with verbs not seen with those modifiers.
- **Intervention proposed:** None.
- **Citation count:** 118

---

### 12. Goodwin et al. (2022) — CFQ Dependency Parsing

- **Citation:** Goodwin, E., et al. (2022). Compositional Generalization in Dependency Parsing on CFQ. *arXiv*.
- **Year:** 2022
- **Task / Benchmark:** CFQ MCD splits applied to dependency parsing.
- **Model type tested:** Transition-based and graph-based dependency parsers.
- **Key OOD finding:** Non-uniform degradation in parsing performance; specific structures (nested relative clauses, conjunctions) drive OOD inaccuracy.
- **Internal representation analysis:** Mapped self-attention weights and encoder states to formal syntactic trees. Internal representations highly sensitive to linear token sequence rather than abstract grammatical dependencies. Internal tree constructions collapse when compound structures diverge from training.
- **Intervention proposed:** Structure-masking intervention to improve structural systematicity.
- **Citation count:** Highly Cited

---

### 13. Petty et al. (2024) — Transformer Depth

- **Citation:** Petty, J., et al. (2024). The Impact of Depth on Compositional Generalization in Transformer Language Models. *arXiv*.
- **Year:** 2024
- **Task / Benchmark:** COGS, COGS-vf, GeoQuery, English Passivization.
- **Model type tested:** Three classes of Transformers trading off depth for width under fixed parameter budgets (41M, 134M, 374M).
- **Key OOD finding:** Increasing depth significantly improves lexical generalization but does not resolve structural generalization failures. Performance saturates at ~6 layers.
- **Internal representation analysis:** Matched checkpoints by pretraining validation perplexity and controlled for ID fine-tuning loss, proving depth benefits on lexical generalization are direct but Transformers remain fundamentally constrained for recursive structural modifications.
- **Intervention proposed:** None. Recommended Transformers can be shallower without sacrificing performance under fixed parameter budgets.
- **Citation count:** ~10

---

### 14. Dziri et al. (2023) — Faith and Fate

- **Citation:** Dziri, N., et al. (2023). Faith and Fate: Limits of Transformers on Compositionality. *Proceedings of NeurIPS*.
- **Year:** 2023
- **Task / Benchmark:** Multi-digit multiplication, logic grid puzzles, dynamic programming.
- **Model type tested:** GPT-3, GPT-4, LLaMA (autoregressive LMs).
- **Key OOD finding:** Catastrophic decline to near-zero as task complexity increases (number of digits in multiplication, sequence length in dynamic programming). Transformer LLMs do not execute underlying algorithmic rules but reduce multi-step calculations into linearized subgraph matching.
- **Internal representation analysis:** Modeled problem-solving as computation graphs. Proved that autoregressive generation (greedy next-token prediction) causes error propagation scaling exponentially with computation graph depth and width.
- **Intervention proposed:** Discussed explicit step-by-step scratchpads and external symbolic solvers.
- **Citation count:** 185

---

### 15. Press et al. (2023) — Compositionality Gap

- **Citation:** Press, O., Zhang, M., Min, S., Schmidt, L., Smith, N. A., & Lewis, M. (2023). Measuring and Narrowing the Compositionality Gap in Language Models. *EMNLP Findings*.
- **Year:** 2023
- **Task / Benchmark:** Compositional Celebrities, Bamboogle — two-hop factual query benchmarks.
- **Model type tested:** GPT-3 family.
- **Key OOD finding:** Single-hop factual recall accuracy improves much faster than multi-hop compositionality with scale. The compositionality gap does not decrease with scale.
- **Internal representation analysis:** Computed factual correlation scores and analyzed intermediate activation paths during implicit retrieval. LLMs struggle with sequential synthesis of facts not observed together during pretraining.
- **Intervention proposed:** Self-Ask prompting — instructs the model to explicitly ask itself and answer follow-up sub-questions before outputting the final response.
- **Citation count:** ~500+

---

## Part III: Architectural, Meta-Learning, and Prompting Successes

### 16. Dessì & Baroni (2019) — CNN on SCAN

- **Citation:** Dessì, R., & Baroni, M. (2019). CNNs found to jump around more skillfully than RNNs: Compositional Generalization in Seq2seq Convolutional Networks. *Proceedings of EMNLP*.
- **Year:** 2019
- **Task / Benchmark:** SCAN.
- **Model type tested:** Convolutional seq2seq model vs. LSTM baselines.
- **Key OOD finding:** CNN successfully generalizes on primitive addition splits that completely block LSTMs.
- **Internal representation analysis:** Probed self-attention weight profiles. Sliding window of 1D convolutions constrains representations locally, preventing sequential state drift that plagues RNNs. However, CNNs still do not learn explicit systematic rules — they generalize by utilizing strong local context patterns.
- **Intervention proposed:** Convolutional seq2seq architecture as a more robust, bounded alternative to recurrent networks.
- **Citation count:** ~80

---

### 17. Lake (2019) — Meta-Seq2Seq

- **Citation:** Lake, B. M. (2019). Compositional Generalization through Meta-Sequence-to-Sequence Learning. *Proceedings of NeurIPS*.
- **Year:** 2019
- **Task / Benchmark:** SCAN.
- **Model type tested:** Memory-augmented seq2seq architecture with episodic meta-learning.
- **Key OOD finding:** Successfully solved SCAN primitive splits under dynamic episode training.
- **Internal representation analysis:** Analyzed external memory slot contents during training, confirming the network learns to dynamically assign variables to memory locations and execute abstract slot-filling operations mimicking symbolic rules.
- **Intervention proposed:** Meta-sequence-to-sequence learning episode framework as an alternative to standard maximum-likelihood fine-tuning.
- **Citation count:** ~120

---

### 18. Lake & Baroni (2023) — MLC

- **Citation:** Lake, B. M., & Baroni, M. (2023). Human-like systematic generalization through a meta-learning neural network. *Nature*, 623, 115–121.
- **Year:** 2023
- **Task / Benchmark:** Human instruction learning task, SCAN, COGS.
- **Model type tested:** Standard Transformer encoder-decoder (5.7M parameters) trained via Meta-learning for Compositionality (MLC).
- **Key OOD finding:** Achieved 100% exact match on human-designed systematicity task, outperforming GPT-4o, Gemini 2.0 Flash, o3-mini.
- **Internal representation analysis:** Stochastically paired query inputs with algebraic outputs or common human heuristic errors, comparing model's output distribution directly with human empirical error patterns. Proved MLC successfully aligns continuous neural activations with abstract symbolic composition rules.
- **Intervention proposed:** MLC dynamic episodic training paradigm for systematicity in standard architectures.
- **Citation count:** Highly Influential (focal point of modern cognitive AI)

---

### 19. Andreas (2020) — GECA

- **Citation:** Andreas, J. (2020). Good-Enough Compositional Data Augmentation. *Proceedings of ACL*.
- **Year:** 2020
- **Task / Benchmark:** SCAN, GeoQuery.
- **Model type tested:** Standard LSTMs with attention.
- **Key OOD finding:** GECA reduced error rate by up to 87% on SCAN diagnostic splits and 16% on semantic parsing.
- **Internal representation analysis:** Probed how GECA affected alignment paths, demonstrating that training on the augmented distribution prevents the network from learning absolute coordinate boundaries for specific words, instead enforcing category-level substitution invariance.
- **Intervention proposed:** GECA — constructs synthetic training examples by replacing fragments with other fragments appearing in similar environments.
- **Citation count:** 313

---

### 20. Liu et al. (2020) — LANE

- **Citation:** Liu, Q., et al. (2020). Compositional Generalization by Learning Analytical Expressions. *Proceedings of NeurIPS*.
- **Year:** 2020
- **Task / Benchmark:** SCAN (all challenging splits).
- **Model type tested:** LANE — memory-augmented architecture with Composer and Solver modules, trained via hierarchical reinforcement learning.
- **Key OOD finding:** LANE solved all challenging SCAN splits with 100% exact match accuracy.
- **Internal representation analysis:** Analyzed continuous memory trajectories, proving the model explicitly separates variable slots from specific symbol values.
- **Intervention proposed:** LANE Composer-Solver architecture and hierarchical optimization algorithm.
- **Citation count:** 78

---

### 21. Liu et al. (2021) — LeAR

- **Citation:** Liu, J., et al. (2021). Learning Algebraic Recombination for Compositional Generalization. *Proceedings of ACL*.
- **Year:** 2021
- **Task / Benchmark:** COGS, CFQ.
- **Model type tested:** LeAR — Tree-LSTM Composer + neural Interpreter, modeling parsing as formal homomorphism between latent syntactic and semantic algebras.
- **Key OOD finding:** Boosted COGS OOD accuracy from 35.0% to 97.7% and CFQ from 67.3% to 90.9%.
- **Internal representation analysis:** Parsed hidden activations of the Tree-LSTM, verifying that hidden states successfully preserve mathematical syntactic-semantic homomorphisms.
- **Intervention proposed:** LeAR framework and end-to-end RL training objective.
- **Citation count:** Highly Cited

---

### 22. Zhou et al. (2023) — Least-to-Most Prompting

- **Citation:** Zhou, D., et al. (2023). Least-to-Most Prompting Enables Complex Reasoning in Large Language Models. *Proceedings of ICLR*.
- **Year:** 2023
- **Task / Benchmark:** SCAN length split, symbolic manipulation (Last-Letter Concatenation), math word problems.
- **Model type tested:** GPT-3 code-davinci-002.
- **Key OOD finding:** Standard chain-of-thought prompting achieved only 16% on SCAN length split; least-to-most prompting solved it with >99% accuracy using only 14 exemplars.
- **Internal representation analysis:** Tracked generation trajectories in the forward pass, confirming that physical decomposition prevents exponential accumulation of autoregressive translation errors.
- **Intervention proposed:** Least-to-Most prompting methodology — decomposes difficult queries into sequences of simpler subproblems.
- **Citation count:** ~1,769

---

### 23. Csordás et al. (2021) — Transformer Tricks

- **Citation:** Csordás, R., et al. (2021). The Devil is in the Detail: Simple Tricks Improve Systematic Generalization of Transformers. *Proceedings of EMNLP*.
- **Year:** 2021
- **Task / Benchmark:** SCAN, COGS.
- **Model type tested:** Vanilla Transformer encoder-decoder.
- **Key OOD finding:** Carefully tuned relative positional encodings and scaled attention weights allow vanilla Transformers to achieve near-perfect performance on both structural and length OOD splits.
- **Internal representation analysis:** Probed cross-attention alignment maps under different positional schemes. Standard absolute positional encodings cause self-attention to overfit to absolute sequence coordinates, preventing generalization to novel recursive nesting. Relative positional encodings preserve abstract relative offsets required for systematicity.
- **Intervention proposed:** Suite of optimization recommendations for vanilla Transformers (relative positional encodings, attention weight scaling).
- **Citation count:** Highly Cited

---

### 24. Gordon et al. (2020) — Permutation Equivariant Models

- **Citation:** Gordon, J., et al. (2020). Permutation Equivariant Models for Compositional Generalization in Language. *Proceedings of ICLR*.
- **Year:** 2020
- **Task / Benchmark:** SCAN primitive splits.
- **Model type tested:** Sequence-to-sequence models modified with permutation-equivariant layers.
- **Key OOD finding:** Enforcing strict mathematical group symmetries over the lexicon guarantees treatment of newly introduced verbs identically to known verbs; achieved 100% exact match on OOD splits.
- **Internal representation analysis:** Demonstrated that syntactic frame representations are completely decoupled from individual lexical tokens.
- **Intervention proposed:** Permutation equivariant layers for sequence learning.
- **Citation count:** 112

---

### 25. Herzig & Berant (2021) — SpanBasedSP

- **Citation:** Herzig, J., & Berant, J. (2021). Span-Based Semantic Parsing for Compositional Generalization. *Proceedings of ACL*.
- **Year:** 2021
- **Task / Benchmark:** COGS, GeoQuery.
- **Model type tested:** SpanBasedSP — predicts span tree over input sentence, mapping logical programs to non-overlapping input text spans.
- **Key OOD finding:** Near-perfect structural OOD generalization.
- **Internal representation analysis:** Traced boundaries of output logical conjuncts, demonstrating span constraints prevent semantic leakage across distinct sentence constituents.
- **Intervention proposed:** SpanBasedSP parser.
- **Citation count:** Highly Cited (semantic parsing literature)

---

### 26. Yao & Koller (2024) — MR Grammar Augmentation

- **Citation:** Yao, Y., & Koller, A. (2024). Simple and effective data augmentation for compositional generalization. *arXiv*.
- **Year:** 2024
- **Task / Benchmark:** COGS, CFQ, GeoQuery, SCAN.
- **Model type tested:** T5, BART.
- **Key OOD finding:** Uniform grammar-based augmentation matched or outperformed test-distribution augmentations, yielding massive OOD gains.
- **Internal representation analysis:** Computed target output perplexity and tracked local syntactic structure coverage. Uniform grammar breaks skewed joint probability of structure-lexicon pairs, forcing context-independent semantic mappings.
- **Intervention proposed:** Uniform MR grammar backtranslation framework — target logical meaning representations sampled from uniform grammar, backtranslated into natural language, and added to training.
- **Citation count:** Emerging

---

### 27. Anonymous (2025/2026) — Scale Leads to Comp Gen

- **Citation:** Anonymous. (2025/2026). Scale leads to compositional generalization. *Under review*.
- **Year:** 2025/2026
- **Task / Benchmark:** $K$-out-of-$M$ compositional task families (synthetic).
- **Model type tested:** Multilayer perceptrons (MLPs).
- **Key OOD finding:** Simply scaling model size and dataset volume leads to robust compositional generalization to held-out tasks, provided training distribution sufficiently covers the module space. MLPs can approximate general compositional families using a linear number of neurons with respect to task module count.
- **Internal representation analysis:** Probed hidden activations across deep layers; demonstrated that when a network successfully generalizes, individual task constituents can be linearly decoded from hidden activations with high $R^2$ accuracy. Linear decodability of continuous features directly correlates with emergent systematicity.
- **Intervention proposed:** Scaling (parameters + data).
- **Citation count:** Emerging

---

## Comparative Matrix: Diagnostic Failure Studies

| Study | Year | Benchmark | Model | Key OOD Failure | Representation Probing | Intervention | Citations |
|---|---|---|---|---|---|---|---|
| Lake & Baroni | 2018 | SCAN | RNN/LSTM/GRU | 0–1% on primitive splits | Word embedding projection | None | ~916 |
| Kim & Linzen | 2020 | COGS | Transformer, LSTM | Structural OOD: 16–35% | Error trajectory tracing | None | Highly Influential |
| Keysers et al. | 2020 | CFQ | LSTM, Transformer, Universal Transformer | 5–37% on MCD splits | Serialization bias analysis | MCD split generation | ~300+ |
| Hupkes et al. | 2020 | PCFG-SET | LSTM, Conv Seq2Seq, Transformer | Productivity/substitutivity failure | 5 metric diagnostic suite | None | ~150+ |
| Ruis et al. | 2020 | gSCAN | CNN-LSTM | Split D/H: near 0% | Attention map visualization | None | 156 |
| An et al. | 2023 | CoFe | GPT series | Fragile ICL comp gen | Fictional vocab substitution | CoFe prompt selection | Emerging |
| Qiu et al. | 2022 | COGS-γ | T5, BART | Structural: near 0% even at 3B | Checkpoint tracing | COGS-vf format | ~80+ |
| Bahdanau et al. | 2019 | SQOOP | Relation Nets, FiLM, NMN | Module collapse on unseen pairs | NMN module probing | Vector-NMN | 245 |
| Bahdanau et al. | 2020 | CLOSURE | MAC, FiLM, NMN | Nested reference failure | Attention map + parameter collapse | Vector-NMN | ~100+ |
| Li et al. | 2023 | SLOG | Transformer, specialized parsers | COGS models: 40.6% on SLOG | Self-attention at recursive depths | None | Emerging |

---

## Comparative Matrix: Successful Interventions

| Study | Year | Benchmark | Model | Intervention | Mechanism of Success | Representational Impact | Citations |
|---|---|---|---|---|---|---|---|
| Dessì & Baroni | 2019 | SCAN | Conv Seq2Seq | Architectural | 1D conv constraints local state transitions | Limits sequential state drift | ~80 |
| Lake | 2019 | SCAN | Memory-Augmented Seq2Seq | Meta-Learning | Dynamic episodic training | Variable-to-memory-slot assignment | ~120 |
| Lake & Baroni | 2023 | SCAN, COGS | Transformer Seq2Seq | Meta-Learning | MLC episodic training over changing grammars | Activations align with algebraic rules | Highly Influential |
| Andreas | 2020 | SCAN, GeoQuery | LSTM | Data Augmentation | GECA fragment swapping | Substitution invariance | 313 |
| Liu et al. | 2020 | SCAN | Memory-Augmented LANE | Architectural + RL | Composer-Solver + hierarchical RL | Variable-slot separation | 78 |
| Liu et al. | 2021 | COGS, CFQ | LeAR (Tree-LSTM) | Architectural + RL | Syntactic-semantic homomorphism | Algebraic structure preservation | Highly Cited |
| Zhou et al. | 2023 | SCAN length | GPT-3 | Prompting | Least-to-Most decomposition | Prevents error accumulation | ~1,769 |
| Csordás et al. | 2021 | SCAN, COGS | Transformer | Optimization tuning | Relative positional encodings | Translation-invariant features | Highly Cited |
| Gordon et al. | 2020 | SCAN | Perm-Equiv RNN | Architectural | Permutation equivariance | Decouples frames from lexical tokens | 112 |
| Herzig & Berant | 2021 | COGS, GeoQuery | SpanBasedSP | Architectural | Span-tree constraints | Prevents semantic leakage | Highly Cited |
| Yao & Koller | 2024 | COGS, CFQ | BART, T5 | Data Augmentation | Uniform MR grammar backtranslation | Breaks context skew | Emerging |
| Anonymous | 2025/26 | K-of-M families | MLPs | Model + Data Scaling | Module space coverage | Linearly decodable task constituents | Emerging |

---

## Synthesis: Mechanistic Principles

### Representational Alignment and Isomorphism

For a neural network to systematically generalize, its internal activation space must develop a homomorphic or isomorphic relationship with the underlying symbolic operations of the task domain. When optimized with standard maximum likelihood on heavily skewed training data, unconstrained networks collapse because their internal representations do not preserve this algebraic structure. Rather than developing invariant vector transformations, hidden states become highly entangled with specific training templates. Models that systematically generalize — whether constrained through architectural scaffolding (LeAR, Vector-NMN) or meta-learned (MLC) — actively preserve this algebraic structure: their intermediate representations can be mapped directly to symbolic rules, and individual task constituents can be linearly decoded from hidden activations.

### Positional Overfitting as Root Cause of Transformer Failures

Standard positional encodings are a primary driver of structural generalization failure in Transformers. Because standard architectures use absolute coordinates to represent token positions, self-attention mechanisms frequently overfit to absolute positional indexing. A model trained on subject-modifier prepositional phrases in object positions associates modifier terms with specific 0-indexed sentence coordinates (e.g., $x_4, x_5$). When the same modifier structure appears in subject positions ($x_1, x_2$) at test time, self-attention maps fail to align. This explains why scaling parameter size fails to improve structural generalization — billion-parameter models attain lower perplexity by memorizing complex surface patterns but remain constrained by coordinate-based positional representations. Interventions using relative positional encodings (Csordás et al.) or eliminating positional variables (COGS-vf) successfully mitigate this.

### Dual-Process Theory of Deep Generalization

Analytical findings of Dziri et al. (2023) and Press et al. (2023) support a dual-process theory: under standard autoregressive generation, a Transformer operates as an implicit, single-step pattern matcher translating inputs to outputs in greedy next-token fashion — highly prone to error propagation. Interventions like Least-to-Most and Self-Ask prompting act as an explicit cognitive workspace by physically decomposing complex queries into isolated, sequential subproblems. This procedural decomposition prevents exponential accumulation of errors, allowing scaled language models to systematically execute complex OOD reasoning chains.

---

## References

- Andreas, J. (2020). Good-Enough Compositional Data Augmentation. *ACL*.
- An, S., et al. (2023). How Do In-Context Examples Affect Compositional Generalization? *ACL*.
- Bahdanau, D., et al. (2019). Systematic Generalization: What Is Required and Can It Be Learned? *ICLR*.
- Bahdanau, D., et al. (2020). CLOSURE: Assessing Systematic Generalization of CLEVR Models. *NeurIPS*.
- Csordás, R., et al. (2021). The Devil is in the Detail: Simple Tricks Improve Systematic Generalization of Transformers. *EMNLP*.
- Dessì, R., & Baroni, M. (2019). CNNs found to jump around more skillfully than RNNs. *EMNLP*.
- Dziri, N., et al. (2023). Faith and Fate: Limits of Transformers on Compositionality. *NeurIPS*.
- Goodwin, E., et al. (2022). Compositional Generalization in Dependency Parsing on CFQ. *arXiv*.
- Gordon, J., et al. (2020). Permutation Equivariant Models for Compositional Generalization in Language. *ICLR*.
- Herzig, J., & Berant, J. (2021). Span-Based Semantic Parsing for Compositional Generalization. *ACL*.
- Hupkes, D., et al. (2020). Compositional Generalization and Natural Language Processing. *arXiv*.
- Keysers, D., et al. (2020). Measuring Compositional Generalization: A Comprehensive Method on Realistic Data. *ICLR*.
- Kim, J., & Linzen, T. (2020). COGS: A Compositional Generalization Challenge Based on Semantic Interpretation. *EMNLP*.
- Lake, B. M. (2019). Compositional Generalization through Meta-Sequence-to-Sequence Learning. *NeurIPS*.
- Lake, B. M., & Baroni, M. (2018). Generalization without systematicity. *ICML*.
- Lake, B. M., & Baroni, M. (2023). Human-like systematic generalization through a meta-learning neural network. *Nature*.
- Li, Y., et al. (2023). SLOG: A Structural Generalization Benchmark for Semantic Parsing. *arXiv*.
- Liu, J., et al. (2021). Learning Algebraic Recombination for Compositional Generalization. *ACL*.
- Liu, Q., et al. (2020). Compositional Generalization by Learning Analytical Expressions. *NeurIPS*.
- Loula, J., et al. (2018). Rearranging the Familiar. *EMNLP Workshop*.
- Petty, J., et al. (2024). The Impact of Depth on Compositional Generalization in Transformers. *arXiv*.
- Press, O., et al. (2023). Measuring and Narrowing the Compositionality Gap in Language Models. *EMNLP Findings*.
- Qiu, L., et al. (2022). Evaluating the Impact of Model Scale for Compositional Generalization. *EMNLP*.
- Ruis, L., et al. (2020). A Benchmark for Systematic Generalization in Grounded Language Understanding. *NeurIPS*.
- Yao, Y., & Koller, A. (2024). Simple and effective data augmentation for compositional generalization. *arXiv*.
- Zhou, D., et al. (2023). Least-to-Most Prompting Enables Complex Reasoning in Large Language Models. *ICLR*.
