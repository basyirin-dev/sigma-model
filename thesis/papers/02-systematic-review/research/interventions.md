# Interventions That Escape the σ-Trap

**Document type:** Reference — evidence base for comparative effectiveness analysis (Phase 9 meta-analysis)
**Purpose:** Catalogues interventions for compositional / OOD generalization; which escape the σ-trap, effect sizes, and transfer limitations
**Status:** Draft

---

## Intervention Type Taxonomy

| Family | Definition | Schema Coherence Link | Representative Papers |
|---|---|---|---|
| **Meta-learning** | Training over dynamic task streams forcing the model to learn learning algorithms that support recombination | Indirect — reshapes optimization trajectory to discover compositional structure | MLC (Lake & Baroni, 2023), Lake (2019), Conklin et al. (2021) |
| **Data augmentation** | Synthetic expansion of the training distribution to include unseen recombination of primitives | Indirect — forces context-independent mappings by breaking skewed joint probabilities | GECA (Andreas, 2020), Akyürek et al. (2020), Yao & Koller (2024), Li et al. (2025) |
| **Architectural modification** | Inductive biases baked into the model that enforce compositional structure (modularity, symmetry, span constraints) | Direct — architecture constrains representational geometry | CNN (Dessì & Baroni, 2019), LANE (Liu et al., 2020), LeAR (Liu et al., 2021), Vector-NMN (Bahdanau et al., 2019, 2020), SpanBasedSP (Herzig & Berant, 2021), Perm-Equiv (Gordon et al., 2020) |
| **Optimization tuning** | Changes to training hyperparameters, regularization, or loss landscape traversal without architectural changes | Indirect — modifies gradient flow or convergence behavior | Csordás et al. (2021), early stopping, Group DRO (Sagawa et al., 2019) |
| **Representation regularization** | Explicit penalties or constraints applied directly to latent representations during training | Direct — reshapes latent geometry toward invariant or algebraic structure | Spectral regularization (Yang et al., 2024), Homomorphism error (An & Du, 2026), StableGNN causal regularizer (Fan et al., 2021) |
| **Prompting / decomposition** | Inference-time structured reasoning that decomposes complex queries into composable subproblems | Indirect — prevents error accumulation in autoregressive generation | Least-to-Most (Zhou et al., 2023), Self-Ask (Press et al., 2023), CoFe (An et al., 2023) |
| **Representation simplification** | Modifying the target output format to reduce structural complexity of the mapping | Direct — reduces output space complexity, enabling alignment | COGS-vf (Qiu et al., 2022) |

---

## Part I: Meta-Learning Interventions

### 1. MLC — Meta-Learning for Compositionality

- **Citation:** Lake, B. M., & Baroni, M. (2023). Human-like systematic generalization through a meta-learning neural network. *Nature*, 623, 115–121.
- **Intervention type:** Meta-learning
- **Description:** Trains a standard Transformer encoder-decoder (5.7M params) on a dynamic stream of few-shot compositional tasks defined by randomly generated latent grammars. Each training episode provides support mappings and queries, forcing the model to acquire generalizable variable-binding skills. Training is distributed across small dynamic datasets ("episodes") rather than a single static split.
- **Effect size:** 100% exact match on human-designed systematicity task; outperforms GPT-4o, Gemini 2.0 Flash, o3-mini. No single numeric OOD improvement over baseline reported (baseline not MLC-compatible).
- **Representation target:** Indirect — training pressure forces activations to align with algebraic composition rules (verified by comparing model output distributions to human error patterns).
- **Cross-benchmark:** Human task, SCAN, COGS. Strong across all three. No results reported on CFQ, gSCAN.
- **Computational cost:** High — dynamic episode stream requires outer-loop task generation; significant training overhead vs. standard fine-tuning.
- **SGD compatible:** Yes — trains standard Transformer via gradient descent on episodic objectives.
- **Citation count:** Highly Influential

---

### 2. Meta-Seq2Seq (Lake, 2019)

- **Citation:** Lake, B. M. (2019). Compositional Generalization through Meta-Sequence-to-Sequence Learning. *Proceedings of NeurIPS*.
- **Intervention type:** Meta-learning
- **Description:** Memory-augmented seq2seq architecture trained under dynamic episodes over non-overlapping support sets. Each episode provides a small compositional task; the model must learn to dynamically assign variables to memory slots and execute abstract slot-filling operations.
- **Effect size:** Solved SCAN primitive splits (0% → ~100%) that completely block standard LSTM seq2seq.
- **Representation target:** Indirect — external memory contents learn variable-to-slot assignment mimicking symbolic rules.
- **Cross-benchmark:** SCAN only. Transfer to COGS, CFQ not demonstrated.
- **Computational cost:** Medium — memory augmentation adds moderate overhead; episode generation adds some cost.
- **SGD compatible:** Yes — gradient-based training on episodic objectives.
- **Citation count:** ~120

---

### 3. Similarity-Driven Meta-Learning (Conklin et al., 2021)

- **Citation:** Conklin, H., Wang, B., Smith, K., & Titov, I. (2021). Meta-Learning to Compositionally Generalize. *Proceedings of ACL*.
- **Intervention type:** Meta-learning
- **Description:** Similarity-driven meta-learning over subsampled task pairs; discourages memorization by forcing the model to generalize from few examples with compositional structure.
- **Effect size:** Improves COGS and SCAN; exact numeric gains not extractable from current data.
- **Representation target:** Indirect — discourages memorization of training-specific patterns.
- **Cross-benchmark:** COGS, SCAN. No CFQ, GeoQuery results reported.
- **Computational cost:** Medium — subsampled task pairs add overhead but less than full episode streaming.
- **SGD compatible:** Yes.
- **Citation count:** N/A

---

## Part II: Data Augmentation Interventions

### 4. GECA — Good-Enough Compositional Augmentation (Andreas, 2020)

- **Citation:** Andreas, J. (2020). Good-Enough Compositional Data Augmentation. *Proceedings of ACL*.
- **Intervention type:** Data augmentation
- **Description:** Constructs synthetic training examples by taking real sentences and replacing fragments with other fragments that appear in similar environments. Enforces category-level substitution invariance rather than token-level augmentation.
- **Effect size:** Reduced error rate by up to 87% on SCAN diagnostic splits and 16% on GeoQuery semantic parsing.
- **Representation target:** Indirect — prevents the network from learning absolute coordinate boundaries for specific words; enforces category-level substitution invariance.
- **Cross-benchmark:** SCAN, GeoQuery. No COGS, CFQ results reported.
- **Computational cost:** Low — offline augmentation, no training overhead change.
- **SGD compatible:** Yes — standard fine-tuning on augmented data.
- **Citation count:** 313

---

### 5. Learned Recombination + Resampling (Akyürek et al., 2020)

- **Citation:** Akyürek, E., Akyürek, A. F., & Andreas, J. (2020). Learning to Recombine and Resample Data for Compositional Generalization. *arXiv*.
- **Intervention type:** Data augmentation
- **Description:** Learned recombination and resampling of synthetic examples; the model learns a policy for which compositional augmentations to generate, rather than using a fixed grammar.
- **Effect size:** Significant gains on SCAN and Sigmorphon; learns from as few as 8 examples. Exact numeric OOD improvement not extractable from current data.
- **Representation target:** Indirect — changes the training distribution to include compositional recombination.
- **Cross-benchmark:** SCAN, Sigmorphon. No COGS, CFQ results reported.
- **Computational cost:** Medium — requires learning an augmentation policy (additional model).
- **SGD compatible:** Yes — augmentation policy trained via gradient-based methods.
- **Citation count:** N/A

---

### 6. Uniform MR Grammar Backtranslation (Yao & Koller, 2024)

- **Citation:** Yao, Y., & Koller, A. (2024). Simple and effective data augmentation for compositional generalization. *arXiv*.
- **Intervention type:** Data augmentation
- **Description:** Target logical meaning representations are sampled from a uniform grammar, backtranslated into natural language, and added to the training set. Breaks the skewed joint probability of structure-lexicon pairs in the original training data.
- **Effect size:** Matched or outperformed test-distribution augmentations on COGS, CFQ, GeoQuery, SCAN. Massive OOD gains (exact numbers not extractable from current data).
- **Representation target:** Indirect — forces context-independent semantic mappings by breaking structure-lexicon co-occurrence bias.
- **Cross-benchmark:** COGS, CFQ, GeoQuery, SCAN — strong breadth. Best breadth of any augmentation method.
- **Computational cost:** Low — offline augmentation using existing grammar; no training overhead change.
- **SGD compatible:** Yes.
- **Citation count:** Emerging

---

### 7. CompSub — Component Substitution (Li et al., 2025)

- **Citation:** Li, Z., Jiang, G., Wu, C., Wei, Y., Lian, D., & Chen, E. (2025). Learning to Substitute Components for Compositional Generalization. *arXiv*.
- **Intervention type:** Data augmentation + difficulty-aware learning
- **Description:** CompSub, LCS, and LCS-ICL methods that learn to substitute compositional components in training examples, with difficulty-aware curriculum weighting.
- **Effect size:** Up to 66.5% (CompSub), 10.3% (LCS), 1.4% (LCS-ICL), 8.8% across SCAN, COGS, GeoQuery, COGS-QL. Gains vary substantially by benchmark.
- **Representation target:** Indirect — regularization-like invariance pressure through component substitution.
- **Cross-benchmark:** SCAN, COGS, GeoQuery, COGS-QL. Moderate breadth.
- **Computational cost:** Medium — requires learning substitution policy and curriculum weighting.
- **SGD compatible:** Yes.
- **Citation count:** Emerging

---

## Part III: Architectural Modification Interventions

### 8. CNN Seq2Seq (Dessì & Baroni, 2019)

- **Citation:** Dessì, R., & Baroni, M. (2019). CNNs found to jump around more skillfully than RNNs. *Proceedings of EMNLP*.
- **Intervention type:** Architectural
- **Description:** Convolutional seq2seq architecture replaces recurrent state transitions with 1D sliding window convolutions, constraining representations locally and preventing sequential state drift.
- **Effect size:** Successfully generalizes on SCAN primitive addition splits that completely block LSTMs.
- **Representation target:** Direct — local convolution constraints reshape representational geometry; prevents sequential drift.
- **Cross-benchmark:** SCAN only. No COGS, CFQ results reported.
- **Computational cost:** Low — standard convolution training; no additional overhead.
- **SGD compatible:** Yes.
- **Citation count:** ~80

---

### 9. LANE — Learning Analytical Expressions (Liu et al., 2020)

- **Citation:** Liu, Q., et al. (2020). Compositional Generalization by Learning Analytical Expressions. *Proceedings of NeurIPS*.
- **Intervention type:** Architectural + RL
- **Description:** Memory-augmented architecture with two cooperative modules: a Composer that finds structured analytical expressions from unstructured sentences, and a Solver that executes these expressions by accessing continuous memory. Trained end-to-end via hierarchical reinforcement learning.
- **Effect size:** 100% exact match accuracy on all challenging SCAN splits (0% → 100%).
- **Representation target:** Direct — explicitly separates variable slots from specific symbol values in continuous memory.
- **Cross-benchmark:** SCAN only. No COGS, CFQ results reported.
- **Computational cost:** High — hierarchical RL training, memory augmentation, two-module architecture.
- **SGD compatible:** Yes (RL variant).
- **Citation count:** 78

---

### 10. LeAR — Learning Algebraic Recombination (Liu et al., 2021)

- **Citation:** Liu, J., et al. (2021). Learning Algebraic Recombination for Compositional Generalization. *Proceedings of ACL*.
- **Intervention type:** Architectural + RL
- **Description:** Models semantic parsing as a formal homomorphism between a latent syntactic algebra and a semantic algebra. Tree-LSTM Composer generates a latent syntactic tree in a bottom-up manner; neural Interpreter assigns semantic operations to tree nodes. End-to-end RL training.
- **Effect size:** COGS OOD: 35.0% → 97.7% (+62.7pts); CFQ OOD: 67.3% → 90.9% (+23.6pts).
- **Representation target:** Direct — hidden states preserve mathematical syntactic-semantic homomorphisms (verified by parsing hidden activations).
- **Cross-benchmark:** COGS, CFQ — two of the most challenging semantic parsing benchmarks. Strong transfer.
- **Computational cost:** High — Tree-LSTM + neural Interpreter, RL training.
- **SGD compatible:** Yes (RL variant).
- **Citation count:** Highly Cited

---

### 11. Vector-NMN (Bahdanau et al., 2019, 2020)

- **Citation:** Bahdanau, D., et al. (2019). Systematic Generalization: What Is Required and Can It Be Learned? *ICLR*. Bahdanau, D., et al. (2020). CLOSURE. *NeurIPS*.
- **Intervention type:** Architectural
- **Description:** Constrains Neural Module Network interfaces to pass compact, vector-valued messages rather than large spatial tensors, forcing modules to decouple object categorization from spatial localization.
- **Effect size:** Qualitative — addresses catastrophic failure on SQOOP and CLOSURE; prevents module collapse.
- **Representation target:** Direct — forces modular, decoupled representations through low-dimensional message-passing constraints.
- **Cross-benchmark:** SQOOP, CLOSURE. Vision-language benchmarks. No SCAN, COGS results.
- **Computational cost:** Medium — architectural constraint adds minimal overhead; standard end-to-end training.
- **SGD compatible:** Yes.
- **Citation count:** 245 (2019 paper), ~100+ (2020 paper)

---

### 12. SpanBasedSP (Herzig & Berant, 2021)

- **Citation:** Herzig, J., & Berant, J. (2021). Span-Based Semantic Parsing for Compositional Generalization. *Proceedings of ACL*.
- **Intervention type:** Architectural
- **Description:** Semantic parser that predicts a span tree over the input sentence, explicitly mapping logical programs to non-overlapping spans of the input text. Constrains the parsing search space to prevent semantic leakage.
- **Effect size:** Near-perfect structural OOD generalization on COGS and GeoQuery.
- **Representation target:** Direct — span constraints prevent semantic constituent leakage during decoding.
- **Cross-benchmark:** COGS, GeoQuery. No CFQ results reported.
- **Computational cost:** Medium — span-based decoding adds moderate overhead.
- **SGD compatible:** Yes.
- **Citation count:** Highly Cited (semantic parsing literature)

---

### 13. Permutation Equivariant Models (Gordon et al., 2020)

- **Citation:** Gordon, J., et al. (2020). Permutation Equivariant Models for Compositional Generalization in Language. *Proceedings of ICLR*.
- **Intervention type:** Architectural
- **Description:** Enforces strict mathematical group symmetries over the lexicon via permutation-equivariant layers, guaranteeing that newly introduced verbs are treated identically to known verbs.
- **Effect size:** 100% exact match on SCAN OOD splits.
- **Representation target:** Direct — syntactic frame representations completely decoupled from individual lexical tokens.
- **Cross-benchmark:** SCAN only. No COGS, CFQ results reported.
- **Computational cost:** Low — permutation equivariance adds minimal architectural overhead.
- **SGD compatible:** Yes.
- **Citation count:** 112

---

## Part IV: Optimization Tuning Interventions

### 14. Transformer Tricks (Csordás et al., 2021)

- **Citation:** Csordás, R., Irie, K., & Schmidhuber, J. (2021). The Devil is in the Detail: Simple Tricks Improve Systematic Generalization of Transformers. *Proceedings of EMNLP*.
- **Intervention type:** Optimization tuning
- **Description:** Suite of recommendations: relative positional encodings, embedding scaling, early stopping, attention weight scaling. No architectural changes.
- **Effect size:** PCFG: 50% → 85% (+35pts); COGS: 35% → 81% (+46pts); SCAN length: 100% (baseline ≤10%). Effects invisible on IID validation.
- **Representation target:** Indirect — relative positional encodings preserve abstract relative offsets; prevents overfitting to absolute positional indexing.
- **Cross-benchmark:** SCAN, COGS, PCFG-SET, CFQ, Mathematics. Broadest benchmark coverage of any optimization tuning.
- **Computational cost:** Low — no additional training overhead; early stopping reduces training time.
- **SGD compatible:** Yes.
- **Citation count:** Highly Cited

---

### 15. Group DRO (Sagawa et al., 2019)

- **Citation:** Sagawa, S., Koh, P. W., Hashimoto, T. B., & Liang, P. (2019). Distributionally Robust Neural Networks for Group Shifts. *arXiv*.
- **Intervention type:** Regularization
- **Description:** Group Distributionally Robust Optimization with stronger L2 regularization or early stopping; optimizes worst-case group accuracy rather than average accuracy.
- **Effect size:** 10–40 point worst-group accuracy gains under distribution shifts.
- **Representation target:** Indirect — reshapes optimization to prevent spurious correlation reliance.
- **Cross-benchmark:** Group shift benchmarks; not tested on standard compositional benchmarks (SCAN, COGS).
- **Computational cost:** Medium — requires group annotations; stochastic optimization.
- **SGD compatible:** Yes.
- **Citation count:** N/A

---

### 16. COGS-vf — Variable-Free Format (Qiu et al., 2022)

- **Citation:** Qiu, L., et al. (2022). Evaluating the Impact of Model Scale for Compositional Generalization in Semantic Parsing. *Proceedings of EMNLP*.
- **Intervention type:** Representation simplification
- **Description:** Removes numbered index variables from target lambda-calculus representations, reducing the complexity of the output space and improving alignment between input and output structures.
- **Effect size:** Structural generalization splits that remain at ~0% for T5-3B become competitive (exact improvement not extractable from current data; qualitative dramatic improvement).
- **Representation target:** Direct — reduces output space complexity, enabling alignment between input syntax and output structure.
- **Cross-benchmark:** COGS only. GeoQuery structural splits not reported.
- **Computational cost:** Low — no architectural change; just target format modification.
- **SGD compatible:** Yes.
- **Citation count:** ~80+

---

## Part V: Representation Regularization Interventions

### 17. Spectral Regularization (Yang et al., 2024)

- **Citation:** Yang, S., Zavatone-Veth, J. A., & Pehlevan, C. (2024). Spectral regularization for adversarially-robust representation learning. *Asilomar Conference*.
- **Intervention type:** Representation regularization
- **Description:** Spectral regularizer applied up to the feature space to constrain the representational geometry; more effective than all-layer regularization for test accuracy and robustness.
- **Effect size:** More effective than all-layer regularization; exact OOD accuracy numbers not extractable from current data.
- **Representation target:** Direct — regularizes the spectral properties of feature representations.
- **Cross-benchmark:** Not tested on standard compositional benchmarks (SCAN, COGS). Tested on robustness benchmarks.
- **Computational cost:** Medium — requires computing spectral norms during training.
- **SGD compatible:** Yes.
- **Citation count:** N/A

---

### 18. Homomorphism Error Regularization (An & Du, 2026)

- **Citation:** An, Z., & Du, W. (2026). Representational Homomorphism Predicts and Improves Compositional Generalization in Transformer Language Model. *arXiv*.
- **Intervention type:** Representation regularization
- **Description:** Homomorphism error (HE) metric measures the degree to which the model's internal representations preserve algebraic structure. HE regularization adds a training-time penalty that encourages homomorphism between input and output algebras.
- **Effect size:** Significant OOD improvement; HE predicted OOD performance better than baseline metrics. Exact numeric improvement not extractable from current data.
- **Representation target:** Direct — explicitly targets the algebraic homomorphism structure of internal representations.
- **Cross-benchmark:** Adapted SCAN with controlled noise. No COGS, CFQ results reported.
- **Computational cost:** Medium — requires computing homomorphism error during training.
- **SGD compatible:** Yes.
- **Citation count:** Emerging

---

### 19. StableGNN — Causal Representation Learning (Fan et al., 2021)

- **Citation:** Fan, S., Wang, X., Shi, C., Cui, P., & Wang, B. (2021). Generalizing Graph Neural Networks on Out-of-Distribution Graphs. *IEEE TPAMI*.
- **Intervention type:** Causal representation learning
- **Description:** StableGNN with differentiable pooling and causal regularizer; explicitly extracts subgraph-level representations and regularizes them to suppress spurious correlations.
- **Effect size:** Outperforms prior methods on 8 real-world OOD graph datasets; exact numeric gains not extractable from current data.
- **Representation target:** Direct — subgraph-level representations regularized to suppress spurious correlations.
- **Cross-benchmark:** 8 OOD graph datasets. Not tested on standard compositional NLP benchmarks.
- **Computational cost:** Medium — differentiable pooling adds moderate overhead; end-to-end training.
- **SGD compatible:** Yes, end-to-end.
- **Citation count:** N/A

---

### 20. Domain Generalization Survey — Negative Results (Shen et al., 2021)

- **Citation:** Shen, Z., et al. (2021). Towards Out-Of-Distribution Generalization: A Survey. *arXiv*.
- **Intervention type:** Survey / negative results
- **Description:** Comprehensive survey of domain generalization methods; notes that many methods show weak effects on real-world images compared to synthetic benchmarks.
- **Effect size:** Negative — domain generalization effects can be weak on real-world images.
- **Representation target:** N/A — survey
- **Cross-benchmark:** Multiple real-world vision benchmarks. Weak effects.
- **Computational cost:** N/A.
- **SGD compatible:** N/A.
- **Citation count:** N/A

---

### 21. Pretraining vs. Specialized Architectures — Negative Results (Furrer et al., 2020)

- **Citation:** Furrer, D., Van Zee, M., Scales, N., & Scharli, N. (2020). Compositional Generalization in Semantic Parsing: Pre-training vs. Specialized Architectures. *arXiv*.
- **Intervention type:** Negative results
- **Description:** Compared pretraining-based approaches against specialized compositional architectures. Pretraining helps but does not solve compositional generalization. Some specialized architectures show no significant CFQ improvement.
- **Effect size:** Negative — pretraining helps but does not solve compositionality; some architectures show no CFQ improvement.
- **Representation target:** N/A — baseline comparison
- **Cross-benchmark:** CFQ. No SCAN, COGS results.
- **Computational cost:** N/A.
- **SGD compatible:** N/A.
- **Citation count:** N/A

---

## Part VI: Prompting / Decomposition Interventions

### 22. Least-to-Most Prompting (Zhou et al., 2023)

- **Citation:** Zhou, D., et al. (2023). Least-to-Most Prompting Enables Complex Reasoning in Large Language Models. *Proceedings of ICLR*.
- **Intervention type:** Prompting / decomposition
- **Description:** Decomposes difficult queries into sequences of simpler subproblems and solves them in order, using solutions of previous subproblems to solve the next. Physical decomposition prevents exponential error accumulation.
- **Effect size:** SCAN length: 16% (chain-of-thought) → >99% (least-to-most) using only 14 exemplars (+83pts).
- **Representation target:** Indirect — prevents exponential accumulation of autoregressive decoding errors.
- **Cross-benchmark:** SCAN length, symbolic manipulation (Last-Letter Concatenation), math word problems. Strong breadth.
- **Computational cost:** Low — prompt engineering only; no additional training.
- **SGD compatible:** Yes — inference-time only; compatible with any pre-trained model.
- **Citation count:** ~1,769

---

### 23. Self-Ask Prompting (Press et al., 2023)

- **Citation:** Press, O., et al. (2023). Measuring and Narrowing the Compositionality Gap in Language Models. *EMNLP Findings*.
- **Intervention type:** Prompting / decomposition
- **Description:** Instructs the model to explicitly ask itself and answer follow-up sub-questions before outputting the final response. Decomposes multi-hop queries into sequential single-hop retrievals.
- **Effect size:** Narrows compositionality gap; exact OOD accuracy improvement not extractable from current data.
- **Representation target:** Indirect — sequential synthesis of facts not observed together during pretraining.
- **Cross-benchmark:** Compositional Celebrities, Bamboogle — two-hop factual queries. Not tested on SCAN, COGS.
- **Computational cost:** Low — prompt engineering only.
- **SGD compatible:** Yes — inference-time only.
- **Citation count:** ~500+

---

### 24. CoFe Prompt Selection (An et al., 2023)

- **Citation:** An, S., et al. (2023). How Do In-Context Examples Affect Compositional Generalization? *Proceedings of ACL*.
- **Intervention type:** Prompting / decomposition
- **Description:** CoFe framework optimizes in-context exemplars along three dimensions: high structural similarity to test case, high diversity among examples, low individual complexity.
- **Effect size:** davinci (175B) improved from 24.2% lag to competitive with fine-tuned GPT-2 Large. Exact OOD improvement not extractable.
- **Representation target:** Indirect — reduces pretraining weight interference with in-context structural mappings.
- **Cross-benchmark:** CoFe (COGS-based). Not tested on SCAN, CFQ.
- **Computational cost:** Low — prompt selection only.
- **SGD compatible:** Yes — inference-time only.
- **Citation count:** Emerging

---

## Cost Comparison

| Cost Tier | Interventions | Rationale |
|---|---|---|
| **Low** | Early stopping, embedding scaling, relative positional encodings (Csordás et al.), GECA, MR grammar augmentation (Yao & Koller), COGS-vf, Least-to-Most, Self-Ask, CoFe, Perm-Equiv | No additional training overhead; offline augmentation or inference-time only |
| **Medium** | Group DRO, spectral regularization, HE regularization, StableGNN, CompSub, learned recombination (Akyürek), similarity-driven meta-learning (Conklin) | Requires additional loss terms, auxiliary models, or group annotations |
| **High** | MLC, meta-seq2seq, LANE, LeAR, NAS with curriculum (Yao et al.) | Outer-loop task generation, hierarchical RL, tree-structured architectures, architecture search |

---

## Negative Results Summary

| Intervention | Benchmark | Result | Implication |
|---|---|---|---|
| Pretraining only (Furrer et al., 2020) | CFQ | No significant improvement | Pretraining alone does not solve compositional generalization |
| Specialized architectures (Furrer et al., 2020) | CFQ | Some architectures show no improvement | Architecture-specific gains do not transfer across benchmarks |
| Domain generalization (Shen et al., 2021) | Real-world images | Weak effects | Synthetic benchmark gains do not reliably transfer to real-world OOD |
| Parameter scaling (Qiu et al., 2022) | COGS structural | Near 0% even at T5-3B | Scale alone does not resolve structural generalization |
| Depth scaling (Petty et al., 2024) | COGS structural | Saturates at ~6 layers | Depth alone does not resolve structural generalization |
| Chain-of-thought (Zhou et al., 2023) | SCAN length | 16% | CoT alone is insufficient; least-to-most required |

---

## Synthesis: Which Interventions Most Consistently Escape the σ-Trap?

### Consistency across benchmarks

| Intervention | # Benchmarks Tested | Consistent OOD Improvement |
|---|---|---|
| Csordás et al. (optimization tuning) | 5 (SCAN, COGS, PCFG, CFQ, Math) | **Yes** — +35–90pts across all |
| Yao & Koller (MR augmentation) | 4 (COGS, CFQ, GeoQuery, SCAN) | **Yes** — matched/test-distribution augmentations |
| Least-to-Most (prompting) | 3 (SCAN, symbolic, math) | **Yes** — 16% → >99% on SCAN |
| LeAR (architectural) | 2 (COGS, CFQ) | **Yes** — +62.7pts (COGS), +23.6pts (CFQ) |
| MLC (meta-learning) | 3 (human, SCAN, COGS) | **Yes** — 100% on all three |
| GECA (augmentation) | 2 (SCAN, GeoQuery) | **Yes** — up to 87% error reduction |

### Most promising schema-coherence-targeting interventions

1. **Representation regularization** (HE, spectral) — directly targets algebraic structure of internal representations; nascent but theoretically grounded
2. **Architectural inductive biases** (LeAR, Vector-NMN, SpanBasedSP) — forces representational homomorphism through architectural constraints; strong effect sizes but limited transfer across benchmarks
3. **Optimization tuning** (Csordás et al.) — cheapest, broadest benchmark coverage; proves that small training changes can have large effects when they address the right representational bottleneck (positional overfitting)

### Central caveat

Benchmark sensitivity remains the key limitation. Strong gains on one benchmark (especially SCAN) do not reliably transfer to harder benchmarks (CFQ, SLOG). The interventions with the broadest benchmark coverage (Csordás et al., Yao & Koller, Least-to-Most) are those that target fundamental representational or optimization bottlenecks rather than benchmark-specific structure.

---

## References

- Akyürek, E., et al. (2020). Learning to Recombine and Resample Data for Compositional Generalization. *arXiv*.
- Andreas, J. (2020). Good-Enough Compositional Data Augmentation. *ACL*.
- An, S., et al. (2023). How Do In-Context Examples Affect Compositional Generalization? *ACL*.
- An, Z., & Du, W. (2026). Representational Homomorphism Predicts and Improves Compositional Generalization. *arXiv*.
- Bahdanau, D., et al. (2019). Systematic Generalization: What Is Required and Can It Be Learned? *ICLR*.
- Bahdanau, D., et al. (2020). CLOSURE: Assessing Systematic Generalization of CLEVR Models. *NeurIPS*.
- Conklin, H., et al. (2021). Meta-Learning to Compositionally Generalize. *ACL*.
- Csordás, R., et al. (2021). The Devil is in the Detail. *EMNLP*.
- Dessì, R., & Baroni, M. (2019). CNNs found to jump around more skillfully than RNNs. *EMNLP*.
- Fan, S., et al. (2021). Generalizing Graph Neural Networks on Out-of-Distribution Graphs. *IEEE TPAMI*.
- Furrer, D., et al. (2020). Compositional Generalization in Semantic Parsing: Pre-training vs. Specialized Architectures. *arXiv*.
- Gordon, J., et al. (2020). Permutation Equivariant Models for Compositional Generalization. *ICLR*.
- Herzig, J., & Berant, J. (2021). Span-Based Semantic Parsing for Compositional Generalization. *ACL*.
- Lake, B. M. (2019). Compositional Generalization through Meta-Sequence-to-Sequence Learning. *NeurIPS*.
- Lake, B. M., & Baroni, M. (2023). Human-like systematic generalization through a meta-learning neural network. *Nature*.
- Li, Z., et al. (2025). Learning to Substitute Components for Compositional Generalization. *arXiv*.
- Liu, J., et al. (2021). Learning Algebraic Recombination for Compositional Generalization. *ACL*.
- Liu, Q., et al. (2020). Compositional Generalization by Learning Analytical Expressions. *NeurIPS*.
- Press, O., et al. (2023). Measuring and Narrowing the Compositionality Gap in Language Models. *EMNLP Findings*.
- Qiu, L., et al. (2022). Evaluating the Impact of Model Scale for Compositional Generalization. *EMNLP*.
- Sagawa, S., et al. (2019). Distributionally Robust Neural Networks for Group Shifts. *arXiv*.
- Shen, Z., et al. (2021). Towards Out-Of-Distribution Generalization: A Survey. *arXiv*.
- Yao, Y., & Koller, A. (2024). Simple and effective data augmentation for compositional generalization. *arXiv*.
- Yang, S., et al. (2024). Spectral regularization for adversarially-robust representation learning. *Asilomar*.
- Zhou, D., et al. (2023). Least-to-Most Prompting Enables Complex Reasoning in Large Language Models. *ICLR*.
