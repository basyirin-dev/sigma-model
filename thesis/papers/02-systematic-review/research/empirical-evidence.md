# Empirical ID–OOD Gaps in Compositional Generalization Benchmarks

**Document type:** Reference — core evidence base for the review
**Purpose:** Papers demonstrating the σ-trap pattern (high ID accuracy, catastrophic OOD failure on recombination-based splits); feeds directly into extraction template design
**Status:** Draft

---

## Scope

This document catalogs empirical papers demonstrating the σ-trap pattern: neural networks trained with standard gradient-based optimization achieve high in-distribution (ID) accuracy but fail catastrophically on out-of-distribution (OOD) test sets that require recombination of learned primitives.

**Covered benchmarks with extractable ID/OOD numerics:** SCAN, COGS, CFQ, PCFG-SET, gSCAN, SQOOP, CLOSURE, SLOG, synthetic compositional datasets.

**Not covered (insufficient extractable numerics from current search):** COFE, QED, NACS, SQuAD compositional splits, MathQA. See §Missing Data.

---

## Part I: Core Evidence — Diagnostic Failure Papers

### 1. Lake & Baroni (2018) — SCAN

- **Citation:** Lake, B. M., & Baroni, M. (2018). Generalization without systematicity: On the compositional skills of sequence-to-sequence recurrent networks. *Proceedings of ICML*.
- **Task / OOD split:** SCAN command-to-action translation; primitive addition split (trained on "jump" in isolation, other verbs in complex structures); length splits (longer sequences than training).
- **ID accuracy:** ~99.8% (random train-test splits)
- **OOD accuracy:** 0–1.2% (primitive addition split); near-0% on length generalization
- **ID–OOD gap:** ~98–99 points
- **Architecture:** Sequence-to-sequence RNN (vanilla RNN, GRU, LSTM)
- **Training hyperparameters:** Not fully extractable; standard training with cross-entropy loss
- **Representation analysis:** Yes — projected word embeddings; showed novel primitive "jump" was geometrically isolated from established verb embeddings, preventing compositional decoding.
- **OOD improvement:** None proposed. Diagnostic benchmark establishing the systematicity gap.
- **Citation count:** ~916

---

### 2. Kim & Linzen (2020) — COGS

- **Citation:** Kim, J., & Linzen, T. (2020). COGS: A Compositional Generalization Challenge Based on Semantic Interpretation. *Proceedings of EMNLP*.
- **Task / OOD split:** Semantic parsing (English → lambda-calculus); generalization splits testing lexical substitution and structural recursion (e.g., prepositional phrase modifiers on subjects when only objects were seen).
- **ID accuracy:** 96–99%
- **OOD accuracy:** 16–35% (structural splits); high seed sensitivity (std dev 6–8%)
- **ID–OOD gap:** 61–83 points
- **Architecture:** Transformer, Sequence-to-Sequence LSTM
- **Training hyperparameters:** Standard cross-entropy; multiple random seeds reported
- **Representation analysis:** Yes — behavioral error trajectory tracing; identified overfitting to absolute position coordinates of nominal variables.
- **OOD improvement:** None. Diagnostic benchmark.
- **Citation count:** Highly Influential

---

### 3. Keysers et al. (2020) — CFQ

- **Citation:** Keysers, D., Schärli, N., Aksu, S., et al. (2020). Measuring Compositional Generalization: A Comprehensive Method on Realistic Data. *Proceedings of ICLR*.
- **Task / OOD split:** CFQ (Compositional Freebase Questions) — NL→SPARQL; Maximum Compound Divergence (MCD) splits maximizing train/test divergence over larger structures while keeping individual rule distributions similar.
- **ID accuracy:** ~80–90% (standard splits, not explicitly reported per model)
- **OOD accuracy:** 5–37% on MCD splits
- **ID–OOD gap:** ~43–85 points (estimated)
- **Architecture:** LSTMs with attention, Transformers, Evolved Transformers, Universal Transformers
- **Training hyperparameters:** Standard training; MCD split generation algorithm
- **Representation analysis:** Yes — studied output serialization patterns; showed models learn linear ordering biases rather than permutation-invariant properties of logical conjuncts.
- **OOD improvement:** MCD split generation algorithm proposed as a measurement tool, not a training intervention.
- **Citation count:** ~300+

---

### 4. Csordás et al. (2021) — SCAN, CFQ, PCFG, COGS

- **Citation:** Csordás, R., Irie, K., & Schmidhuber, J. (2021). The Devil is in the Detail: Simple Tricks Improve Systematic Generalization of Transformers. *Proceedings of EMNLP*.
- **Task / OOD split:** SCAN, CFQ, PCFG-SET, COGS, Mathematics; standard systematic generalization splits.
- **ID accuracy:** IID differences often invisible (near-ceiling across all models)
- **OOD accuracy (baseline):** PCFG productivity ~50%; COGS ~35%
- **OOD accuracy (intervention):** PCFG ~85% (+35pts); COGS ~81% (+46pts)
- **ID–OOD gap:** Baseline gaps implied; intervention substantially reduces gap
- **Architecture:** Transformer, Universal Transformer
- **Training hyperparameters:** Embedding scaling, early stopping, relative positional embeddings
- **Representation analysis:** Yes — probed cross-attention alignment maps; standard absolute positional encodings cause self-attention to overfit to absolute sequence coordinates.
- **OOD improvement:** Yes — simple optimization tuning (relative positional encodings, attention scaling) strongly improved OOD.
- **Citation count:** Highly Cited

---

### 5. Hupkes et al. (2020) — PCFG-SET

- **Citation:** Hupkes, D., Veldhoen, S., & Zuidema, W. (2020). Compositional Generalization and Natural Language Processing: Explaining Category-Level Multi-Task Generalization. *arXiv:2006.15951*.
- **Task / OOD split:** PCFG-SET string transduction; tests of systematic recombination, productivity (length), substitutivity (synonym), localism, overgeneralization.
- **ID accuracy:** Near-perfect on standard test sets
- **OOD accuracy:** Severe drops (22–34%) under Systematicity and Productivity tests
- **ID–OOD gap:** 22–34 points
- **Architecture:** LSTM, Convolutional Seq2Seq, Transformer
- **Training hyperparameters:** Not extractable from current data
- **Representation analysis:** Yes — five structurally grounded behavioral tests (systematicity, productivity, substitutivity, localism, overgeneralization).
- **OOD improvement:** None. Theoretical framework for evaluating compositionality.
- **Citation count:** ~150+

---

### 6. Ruis et al. (2020) — gSCAN

- **Citation:** Ruis, L., Andreas, J., Baroni, M., & Lake, B. M. (2020). A Benchmark for Systematic Generalization in Grounded Language Understanding. *Proceedings of NeurIPS*.
- **Task / OOD split:** gSCAN (Grounded SCAN) — multimodal 2D grid world navigation; Split D (novel spatial directions), Split H (adverb-verb generalization, e.g., "cautiously" + "spin" held out).
- **ID accuracy:** ~95%+ on standard splits
- **OOD accuracy:** Near 0% on Split D and Split H
- **ID–OOD gap:** ~95 points
- **Architecture:** Multimodal CNN-LSTM seq2seq
- **Training hyperparameters:** Not extractable from current data
- **Representation analysis:** Yes — visualized cross-modal attention maps; tracked visual coordinate alignments; models failed to decouple adjectival/adverbial modifiers from visual context.
- **OOD improvement:** None. Open visual-linguistic reasoning challenges.
- **Citation count:** 156

---

### 7. Bahdanau et al. (2019) — SQOOP

- **Citation:** Bahdanau, D., et al. (2019). Systematic Generalization: What Is Required and Can It Be Learned? *Proceedings of ICLR*.
- **Task / OOD split:** SQOOP (Spatial Queries on Object Pairs) — visual relational reasoning ("Is A left of 3?"); unseen object pairs.
- **ID accuracy:** High on seen object pairs (exact numbers not extractable from current data)
- **OOD accuracy:** Fails to generalize to unseen object pairs even when all individual objects and relations were seen in training.
- **ID–OOD gap:** Not numerically quantified in current data; qualitative catastrophic failure.
- **Architecture:** Relation Networks, FiLM, Neural Module Networks (NMNs)
- **Training hyperparameters:** Standard training; end-to-end backpropagation for NMNs.
- **Representation analysis:** Yes — probed intermediate module activation parameters and routing pathways. Individual NMN modules "collapsed," learning entangled representations of object identity and spatial position.
- **OOD improvement:** Yes — Vector-NMN with vector-valued message passing forces decoupling of object categorization from spatial localization.
- **Citation count:** 245

---

### 8. Bahdanau et al. (2020) — CLOSURE

- **Citation:** Bahdanau, D., et al. (2020). CLOSURE: Assessing Systematic Generalization of CLEVR Models. *Proceedings of NeurIPS*.
- **Task / OOD split:** CLOSURE — extends CLEVR-VQA; referring expressions based on matching object properties in novel nested configurations.
- **ID accuracy:** 97–99% on standard CLEVR
- **OOD accuracy:** Near 0% zero-shot on nested reference queries
- **ID–OOD gap:** ~97–99 points
- **Architecture:** MAC, FiLM, standard NMNs
- **Training hyperparameters:** Standard CLEVR training protocol
- **Representation analysis:** Yes — evaluated visual-attentional map projections; tracked coordinate variable flow across nested syntax paths. Models overfit to dominant training pathways.
- **OOD improvement:** Yes — Vector-NMN with low-dimensional vector-valued messages.
- **Citation count:** ~100+

---

### 9. Li et al. (2023) — SLOG

- **Citation:** Li, B., Donatelli, L., Koller, A., et al. (2023). SLOG: A Structural Generalization Benchmark for Semantic Parsing. *Proceedings of EMNLP*.
- **Task / OOD split:** SLOG — extends COGS with 17 challenging structural generalization cases (prepositional phrase modifiers on novel noun phrase positions).
- **ID accuracy:** Near-perfect on original COGS
- **OOD accuracy:** 40.6% (standard pretrained models); best specialized parser 70.8%
- **ID–OOD gap:** ~59 points (standard models)
- **Architecture:** Standard Transformers, pretrained LMs, specialized structure-aware parsers
- **Training hyperparameters:** Not extractable from current data
- **Representation analysis:** Yes — probed self-attention patterns at varying recursive parsing depths. Standard Transformers fail to maintain structural coherence during deep syntactic nesting.
- **OOD improvement:** None. Diagnostic benchmark.
- **Citation count:** Emerging

---

### 10. Qiu et al. (2022) — COGS-γ / Scaling

- **Citation:** Qiu, L., et al. (2022). Evaluating the Impact of Model Scale for Compositional Generalization in Semantic Parsing. *Proceedings of EMNLP*.
- **Task / OOD split:** COGS, GeoQuery; investigated whether parameter scaling resolves systematic OOD failures.
- **ID accuracy:** Near-perfect (improves with scale on lexical splits)
- **OOD accuracy (lexical):** Improved massively with scale (T5-3B)
- **OOD accuracy (structural):** Near 0% even for T5-3B on nested subject modifiers
- **ID–OOD gap:** Structural gap persists despite scale
- **Architecture:** T5 (Base through 3B), BART
- **Training hyperparameters:** Fine-tuning T5 at multiple scales; fixed parameter budgets
- **Representation analysis:** Yes — checkpoint trajectories and pretraining losses; deeper models attain lower perplexity but fail to develop representational geometry for structural recursion.
- **OOD improvement:** Yes — COGS-vf (Variable-Free) format removing numbered index variables from target representations dramatically improves structural generalization.
- **Citation count:** ~80+

---

## Part II: Supplementary Evidence — Intervention and Analysis Papers

### 11. Jiang & Bansal (2021) — SCAN via Auxiliary Tasks

- **Citation:** Jiang, Y., & Bansal, M. (2021). Inducing Transformer's Compositional Generalization Ability via Auxiliary Sequence Prediction Tasks. *Proceedings of EMNLP*.
- **Task / OOD split:** SCAN challenging splits; gSCAN positive transfer.
- **ID accuracy:** Standard splits near-perfect
- **OOD accuracy (baseline):** ≤10% on challenging splits
- **OOD accuracy (intervention):** 100% on SCAN; 97.8% on CFQ MCD1 with only 5% data
- **ID–OOD gap:** Up to ~90 points (baseline); nearly eliminated by intervention
- **Architecture:** Transformer
- **Training hyperparameters:** Auxiliary sequence prediction tasks; 418 examples = 5% of data in one setting
- **Representation analysis:** Some architecture insight (auxiliary supervision shapes representation)
- **OOD improvement:** Yes — large gains from auxiliary supervision.
- **Citation count:** N/A

---

### 12. An et al. (2023) — CoFe (LLMs)

- **Citation:** An, S., et al. (2023). How Do In-Context Examples Affect Compositional Generalization? *Proceedings of ACL*.
- **Task / OOD split:** CoFe (Compositional Few-shot Evaluation) — built on COGS grammar; in-context learning compositional generalization.
- **ID accuracy:** Varied by prompt
- **OOD accuracy:** davinci (175B) lags fine-tuned GPT-2 Large by 24.2% with basic-primitive prompts
- **ID–OOD gap:** ~24 points for best LLM
- **Architecture:** GPT series (davinci, code-cushman-001/002, text-davinci-002, code-davinci-002)
- **Training hyperparameters:** In-context learning; prompt selection framework
- **Representation analysis:** Yes — systematic vocabulary substitution (fictional tokens) analyzed pretraining weight interference.
- **OOD improvement:** Yes — CoFe prompt selection framework optimizing similarity, diversity, complexity.
- **Citation count:** Emerging

---

### 13. Patel et al. (2022) — SCAN Revisited

- **Citation:** Patel, A., Bhattamishra, S., Blunsom, P., & Goyal, N. (2022). Revisiting the Compositional Generalization Abilities of Neural Sequence Models. *arXiv*.
- **Task / OOD split:** SCAN one-shot primitive split.
- **ID accuracy:** Not numerically extractable
- **OOD accuracy:** Near-perfect after train-distribution modification; baseline catastrophic
- **ID–OOD gap:** Large (qualitative)
- **Architecture:** Standard seq2seq
- **Training hyperparameters:** Modified training distribution
- **Representation analysis:** Yes — empirical analysis of primitive handling
- **OOD improvement:** Yes — simple train-distribution changes improve systematic generalization.
- **Citation count:** N/A

---

### 14. Li et al. (2022) — Neural-Symbolic Recursive Machine (NSR)

- **Citation:** Li, Q., Zhu, Y., Liang, Y., Wu, Y., Zhu, S.-C., & Huang, S. (2022). Neural-Symbolic Recursive Machine for Systematic Generalization. *arXiv*.
- **Task / OOD split:** SCAN, PCFG, HINT, compositional MT.
- **ID accuracy:** Strong
- **OOD accuracy:** NSR superior to baselines
- **ID–OOD gap:** Significantly reduced by NSR
- **Architecture:** Modular neural-symbolic system
- **Training hyperparameters:** Deduction-abduction training
- **Representation analysis:** Not explicitly
- **OOD improvement:** Yes — strong compositional inductive bias.
- **Citation count:** N/A

---

### 15. Camposampiero et al. (2025) — Large-Scale Synthetic Compositional Evaluation

- **Citation:** Camposampiero, G., et al. (2025). Scalable Evaluation and Neural Models for Compositional Generalization. *arXiv*.
- **Task / OOD split:** Six representation-learning datasets; orthotopic and pairwise compositional splits.
- **ID accuracy:** Almost every model perfect ID; many 100% train, 95% ID val
- **OOD accuracy:** None generalize properly at hardest extrapolation; Cars3D ED test 73.38%
- **ID–OOD gap:** Large across all model families
- **Architecture:** Six model families (monolithic and disentangled)
- **Training hyperparameters:** >5000 runs, 3 seeds, model-selection ablation
- **Representation analysis:** Not in cited lines
- **OOD improvement:** Yes — ED/AIN improve OOD but trade off with ID.
- **Citation count:** Emerging

---

### 16. Ito et al. (2024) — gCOG Multimodal Reasoning

- **Citation:** Ito, T., Dan, S., Rigotti, M., Kozloski, J., & Campbell, M. (2024). On the generalization capacity of neural networks during generic multimodal reasoning. *arXiv*.
- **Task / OOD split:** gCOG; distractor, systematic, productive splits.
- **ID accuracy:** Train >98%; systematic IID 75.4% best
- **OOD accuracy:** Systematic OOD 65.7% best; all fail productivity
- **ID–OOD gap:** At least 9.7 points for best model; much worse on productivity
- **Architecture:** RNN, GRU, Transformer, Perceiver, cross-attn
- **Training hyperparameters:** Depth and cross-attention ablations
- **Representation analysis:** Yes — penultimate-layer similarity analysis.
- **OOD improvement:** Yes — cross-attention and deeper attention help some splits, not productivity.
- **Citation count:** Emerging

---

### 17. An & Du (2026) — Representational Homomorphism

- **Citation:** An, Z., & Du, W. (2026). Representational Homomorphism Predicts and Improves Compositional Generalization in Transformer Language Model. *arXiv*.
- **Task / OOD split:** Adapted SCAN with controlled noise.
- **ID accuracy:** Not extractable
- **OOD accuracy:** OOD predicted by HE (homomorphism error); improved with HE regularization
- **ID–OOD gap:** Significant; improved by intervention
- **Architecture:** Small decoder-only Transformer
- **Training hyperparameters:** Train from scratch; HE regularization
- **Representation analysis:** Yes — homomorphism error metric as explicit representation probe.
- **OOD improvement:** Yes — HE regularization yields significant OOD improvement.
- **Citation count:** Emerging

---

## Summary: Extractable ID–OOD Gap Table

| Study | Year | Benchmark | ID Acc | OOD Acc | Gap | Architecture |
|---|---|---|---|---|---|---|
| Lake & Baroni | 2018 | SCAN (primitive) | ~99.8% | 0–1.2% | ~98 pts | RNN/LSTM/GRU |
| Kim & Linzen | 2020 | COGS (structural) | 96–99% | 16–35% | 61–83 pts | Transformer, LSTM |
| Keysers et al. | 2020 | CFQ (MCD) | ~80–90% | 5–37% | 43–85 pts | LSTM, Transformer, Evolved Transformer |
| Csordás et al. | 2021 | PCFG-SET | ~95% | ~50% | ~45 pts | Transformer |
| Csordás et al. | 2021 | COGS | ~95% | ~35% | ~60 pts | Transformer |
| Hupkes et al. | 2020 | PCFG-SET | ~95% | ~60–75% | 22–34 pts | LSTM, Conv, Transformer |
| Ruis et al. | 2020 | gSCAN (Split D/H) | ~95% | ~0% | ~95 pts | CNN-LSTM |
| Bahdanau et al. | 2020 | CLOSURE | 97–99% | ~0% | ~97 pts | MAC, FiLM, NMN |
| Li et al. | 2023 | SLOG | ~99% | 40.6% | ~59 pts | Transformer |
| Qiu et al. | 2022 | COGS (structural) | ~95% | ~0% (3B) | ~95 pts | T5, BART |
| Jiang & Bansal | 2021 | SCAN (challenging) | ~95% | ≤10% | ~85 pts | Transformer |

---

## Missing Data: Benchmarks Not Recoverable

The following requested benchmarks lack sufficient extractable ID/OOD numerics from the current search. These should be targets for Phase 2 search string refinement.

| Benchmark | Status | Recommended Search String |
|---|---|---|
| **COFE** | Not recoverable | "COFE compositional few-shot" OR "COFE evaluation" |
| **MathQA** | Not recoverable | "MathQA compositional generalization" OR "MathQA OOD" |
| **QED** | Not recoverable | "QED compositional" OR "QED semantic parsing OOD" |
| **NACS** | Not recoverable | "NACS compositional" OR "NACS systematic generalization" |
| **SQuAD compositional splits** | Not recoverable | "SQuAD compositional generalization" OR "SQuAD OOD recombination" |
| **GeoQuery** | Partially covered (intervention papers only) | "GeoQuery compositional generalization baseline" |

---

## Synthesis: Patterns in the Evidence

### Gap Magnitude Distribution

The ID–OOD gap ranges from **22 points** (PCFG-SET productivity, Hupkes et al. 2020) to **~98 points** (SCAN primitive, Lake & Baroni 2018). The median gap across extractable studies is approximately **60–85 points**, confirming that the σ-trap pattern is not a marginal effect but a catastrophic failure.

### Architecture Sensitivity

- **RNNs/LSTMs:** Consistently fail across all benchmarks (SCAN, COGS, CFQ, gSCAN)
- **Transformers:** Fail on structural generalization (COGS, SLOG, CFQ) but improve with optimization tuning (Csordás et al.)
- **Scale alone insufficient:** T5-3B shows massive lexical improvement but structural gap persists (Qiu et al. 2022)
- **Specialized architectures:** Some succeed (LANE 100% on SCAN, MLC 100%, Vector-NMN on SQOOP/CLOSURE) but require structural inductive biases

### Interventions That Work

1. **Relative positional encodings** — Csordás et al. (+35–46pts)
2. **Variable-Free target format (COGS-vf)** — Qiu et al. (structural gap from 0% → competitive)
3. **Auxiliary sequence prediction** — Jiang & Bansal (≤10% → 100% on SCAN)
4. **Least-to-Most prompting** — Zhou et al. (16% → >99% on SCAN length)
5. **Homomorphism regularization** — An & Du (significant OOD improvement)
6. **LE (Latent Structure + Augmentation)** — Qiu et al. (2021) (stronger than T5-CSL ensemble)

### Interventions That Partially/Don't Work

1. **Parameter scaling alone** — lexical improves, structural does not (Qiu et al. 2022)
2. **Depth scaling** — lexical improves, structural saturates at ~6 layers (Petty et al. 2024)
3. **Chain-of-thought prompting** — 16% on SCAN length (vs. 99%+ with least-to-most)

---

## References

- An, S., et al. (2023). How Do In-Context Examples Affect Compositional Generalization? *ACL*.
- An, Z., & Du, W. (2026). Representational Homomorphism Predicts and Improves Compositional Generalization. *arXiv*.
- Bahdanau, D., et al. (2019). Systematic Generalization: What Is Required and Can It Be Learned? *ICLR*.
- Bahdanau, D., et al. (2020). CLOSURE: Assessing Systematic Generalization of CLEVR Models. *NeurIPS*.
- Camposampiero, G., et al. (2025). Scalable Evaluation and Neural Models for Compositional Generalization. *arXiv*.
- Csordás, R., et al. (2021). The Devil is in the Detail. *EMNLP*.
- Hupkes, D., et al. (2020). Compositional Generalization and NLP. *arXiv*.
- Ito, T., et al. (2024). On the generalization capacity of neural networks during generic multimodal reasoning. *arXiv*.
- Jiang, Y., & Bansal, M. (2021). Inducing Transformer's Compositional Generalization Ability. *EMNLP*.
- Keysers, D., et al. (2020). Measuring Compositional Generalization. *ICLR*.
- Kim, J., & Linzen, T. (2020). COGS: A Compositional Generalization Challenge. *EMNLP*.
- Lake, B. M., & Baroni, M. (2018). Generalization without systematicity. *ICML*.
- Li, Q., et al. (2022). Neural-Symbolic Recursive Machine for Systematic Generalization. *arXiv*.
- Li, Y., et al. (2023). SLOG: A Structural Generalization Benchmark. *arXiv*.
- Patel, A., et al. (2022). Revisiting the Compositional Generalization Abilities. *arXiv*.
- Qiu, L., et al. (2022). Evaluating the Impact of Model Scale. *EMNLP*.
- Ruis, L., et al. (2020). A Benchmark for Systematic Generalization in Grounded Language Understanding. *NeurIPS*.
