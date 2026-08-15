# Quantifying Schema Coherence: Proxies for Rule-Governed Internal Representations

**Document type:** Reference — data extraction template (Phase 7) and meta-analysis coding (Phase 9)
**Purpose:** Catalogues known proxy measures for schema coherence; which proxies to extract from papers
**Status:** Draft

---

## Part I: Representational Similarity Analysis (RSA)

### 1.1 RDM Consistency — Mehrer & Kietzmann (2020)

- **Citation:** Mehrer, J., & Kietzmann, T. C. (2020). Representational Stability of Deep Neural Networks. *arXiv:2009.01898*.
- **Measure name:** RDM Consistency — Spearman correlation of Representational Dissimilarity Matrix lower triangles
- **Construct captured:** Pairwise geometric alignment of activation spaces across initialization seeds, network layers, or architectures. Tracks how consistently different network instances organize the same stimuli in their internal representation space.
- **Validation approach:** Computed pairwise RDMs from 1,000 CIFAR-10 test images across ResNet and VGG architectures; demonstrated that changing only the random seed of weights prior to training leads to significant representational divergence in deeper layers while maintaining identical classification performance.
- **Computational cost:** $O(N^2 \cdot D)$ forward passes and distance matrix calculations for $N$ samples, where $D$ is the activation dimensionality. Spearman correlation over $N(N-1)/2$ unique lower-triangle entries scales as $O(N^2 \log N)$.
- **OOD correlation:** Moderate. High representational alignment between seeds is a marker of stable optimization, but global geometric similarity does not guarantee robust generalization. CKA is insensitive to fine-grained parameter shifts causing catastrophic forgetting. In multi-task pre-training, representational convergence partially predicts downstream OOD fine-tuning performance on unseen entities.

---

### 1.2 Centered Kernel Alignment (CKA) — Kornblith et al. (2019)

- **Citation:** Kornblith, S., Norouzi, M., Lee, H., & Hinton, G. (2019). Similarity of Neural Network Representations Revisited. *Proceedings of ICML*.
- **Measure name:** Centered Kernel Alignment (CKA) — normalized inner product between two kernel matrices computed from layer activations
- **Construct captured:** Similarity of learned representations across layers, architectures, or training checkpoints. More rotation- and sign-invariant than representational similarity; captures structural alignment regardless of axis permutation.
- **Validation approach:** Compared layer-wise representations of vision models trained on ImageNet; demonstrated that early and late layers are often more similar across architectures than middle layers.
- **Computational cost:** $O(N^2 \cdot D)$ for computing Gram matrices; lower constant factor than RDM due to inner product vs. distance calculation.
- **OOD correlation:** Moderate. Tracks global geometry but can be insensitive to localized rule-level changes. In sequential learning, CKA does not detect catastrophic forgetting caused by fine-grained interference.

---

## Part II: Probing Classifiers

### 2.1 Control Task Selectivity — Hewitt & Liang (2019)

- **Citation:** Hewitt, J., & Liang, P. (2019). Designing and Interpreting Probes with Control Tasks. *Proceedings of EMNLP*.
- **Measure name:** Selectivity = $\text{Accuracy}_{\text{Linguistic}} - \text{Accuracy}_{\text{Control}}$
- **Construct captured:** Separation of true rule encoding from probe-level memorization. A control task assigns each word type to a randomly sampled label while preserving the overall token distribution, so only memorization (not structure) can explain control accuracy. Selectivity isolates the structural signal.
- **Validation approach:** Trained linear and bilinear probes on ELMo and BERT hidden states for POS and dependency edge prediction; showed that linear probes achieve higher selectivity (26.0%) than MLP probes (4.5%), confirming that lower-capacity probes are more reliable indicators of representational structure. Demonstrated that second-layer ELMo representations are substantially more selective than first-layer.
- **Computational cost:** Low — single forward pass to extract hidden states, then training a linear or bilinear classifier scales as $O(N \cdot D)$.
- **OOD correlation:** Strong. High selectivity indicates that the underlying model has internalized abstract, contextual rules rather than type-level lexical features, directly impacting performance on OOD grammar and syntax structures. However, recent evaluations across 32 Transformer models indicate that while selectivity is necessary to identify true syntactic encoding, high probing scores do not always translate to downstream task outcomes — combining structural probes with behavioral testing is recommended.

---

### 2.2 Probe Capacity Taxonomy — Belinkov (2021)

- **Citation:** Belinkov, Y. (2021). Probing Classifiers: Promises, Shortcomings, and Advances. *Computational Linguistics*.
- **Measure name:** Probe accuracy vs. probe capacity trade-off — comparative analysis of linear, bilinear, and MLP probes
- **Construct captured:** The degree to which target linguistic features are linearly separable in the representation space versus requiring non-linear readout. More linearly decodable features indicate stronger structural organization.
- **Validation approach:** Survey of probing studies across POS tagging, dependency parsing, semantic role labeling; recommended controlling probe capacity and reporting selectivity rather than raw accuracy.
- **Computational cost:** Low — same linear/bilinear classifiers as selectivity.
- **OOD correlation:** Indirect. Linear separability of linguistic features correlates with structural robustness but does not guarantee systematic generalization.

---

## Part III: Intraclass Clustering Quality

### 3.1 Neuron & Layer Subclass Selectivity ($c_1$–$c_4$) — Carbonnelle & De Vleeschouwer (2021)

- **Citation:** Carbonnelle, S., & De Vleeschouwer, C. (2021). Neuron and Layer Subclass Selectivity Measures for Identifying Feature Learning Regimes. *arXiv:2110.14521*.
- **Measure name:** $c_1$ (neuron subclass selectivity), $c_2$ (neuron unsupervised clustering), $c_3$ (layer-level subclass variance ratio), $c_4$ (layer-level unsupervised clustering via silhouette score)
- **Construct captured:** Spontaneous, unsupervised semantic subclass grouping within a supervised superclass. A model with strong subclass clustering organizes its representation space around meaningful categories even when not explicitly trained to do so.
- **Validation approach:** Trained >500 VGG and ResNet models on CIFAR-100 superclasses and BREEDS hierarchy; varied learning rate, batch size, optimizer, weight decay, dropout, data augmentation, and network depth/width. Used granulated Kendall rank-correlation coefficient to demonstrate that intraclass clustering quality increases with layer depth, peaks in intermediate layers, and compresses in the penultimate layer. Differences between high- and low-generalizing models emerge in early epochs.
- **Computational cost:** Moderate — $O(I \cdot N_s^2 \cdot D)$ for variance ratio computation or $O(I \cdot N_s \cdot K \cdot D)$ for K-Means, where $I$ is class count, $N_s$ is samples per class, $K$ is subclass count. Can be approximated using randomized mini-batches.
- **OOD correlation:** Exceptionally strong. Intraclass clustering serves as an implicit regularizer directly tied to OOD performance. Models displaying robust subclass organization exhibit significantly superior OOD generalization under covariate shifts (BREEDS hierarchy evaluation). Spontaneous subclass clustering is an empirical marker of learning structural rules rather than memorizing individual exemplars.

---

## Part IV: Information-Theoretic Tracking

### 4.1 Information Plane Trajectories — Shwartz-Ziv & Tishby (2017), Adnan et al. (2022)

- **Citation (primary):** Shwartz-Ziv, R., & Tishby, N. (2017). Opening the Black Box of Deep Neural Networks via Information. *arXiv:1703.00810*.
- **Citation (shortcut application):** Adnan, M., et al. (2022). Understanding Deep Learning via Information Plane Trajectories. *arXiv*.
- **Measure name:** Mutual Information $I(X; Z)$ and $I(Z; Y)$, where $Z$ is a hidden layer representation; Information Plane trajectory
- **Construct captured:** Compression of input-irrelevant details and tracking of fitting vs compression phases. The Fitting Phase increases $I(Z; Y)$ as the representation encodes target-relevant features; the Compression Phase decreases $I(X; Z)$ as the network discards input variability irrelevant to $Y$. Shortcut learning is detected by sharp decrease and low convergence of $I(X; Z)$, indicating compression without structural encoding.
- **Validation approach:** Tracked on synthetic and natural shortcut datasets (MNIST with white patches, CelebA gender/hair attributes). Showed that networks latching onto shortcuts learn highly compressed representations, captured by $\text{Shortcut Signal} \propto -\Delta I(X; Z)$.
- **Computational cost:** Extremely high — standard bounds require MINE (Mutual Information Neural Estimation), which trains an auxiliary discriminator neural network in an inner loop. Scales as $O(E_{\text{aux}} \cdot N \cdot D)$. NTK framework provides tractable analytical bounds but is limited to infinite-width models.
- **OOD correlation:** Strong. Hyper-compression of $I(X; Z)$ maps shortcut latching and predicts OOD failure. Optimizing representations to compress task-irrelevant details (low $I(X; Z)$ conditional on high $I(Z; Y)$) forces the network to learn invariant, low-dimensional structures, directly enhancing robustness to covariate shifts.

---

### 4.2 Conditional Information Flow Maximization (CIFM)

- **Citation:** Referenced in Adnan et al. (2022) framework.
- **Measure name:** $\max I(X; Z) + \beta I(Y; Z)$ subject to Conditional Information Minimization (CIM)
- **Construct captured:** Balances sufficiency (preserving task-relevant information) and robustness (filtering task-irrelevant features). Prevents over-compression where critical predictive features are lost.
- **Validation approach:** Applied to domain generalization tasks; demonstrated that maximizing both $I(X; Z)$ and $I(Y; Z)$ while minimizing redundancy prevents shortcut learning.
- **Computational cost:** Same as variational MI estimators — $O(E_{\text{aux}} \cdot N \cdot D)$.
- **OOD correlation:** Strong. Balances information preservation and compression to optimize OOD robustness.

---

### 4.3 f-DIME Density Ratio Estimation

- **Citation:** Referenced in Adnan et al. (2022) as Type 3 estimator.
- **Measure name:** $f$-DIME — direct estimation of density ratio $p(x, y) / (p(x) p(y))$
- **Construct captured:** Decouples density ratio learning from specific variational bounds, enabling more accurate MI estimation in deterministic networks where standard methods fail.
- **Validation approach:** Tested on deterministic networks with known generative processes; shown to outperform Type 1 (single variational bound) and Type 2 (surrogate training) methods.
- **Computational cost:** High — requires training a specialized density ratio estimator.
- **OOD correlation:** Theoretical improvement over standard MI estimation; practical OOD correlation requires further validation.

---

## Part V: Disentanglement Metrics

### 5.1 β-VAE Metric — Higgins et al. (2017), Burgess et al. (2018)

- **Citation:** Higgins, I., et al. (2017). β-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework. *Proceedings of ICLR*.
- **Measure name:** β-VAE metric — classification accuracy of a linear classifier predicting which ground-truth factor was held constant, given absolute differences in latent representations
- **Construct captured:** Alignment of individual latent dimensions with independent physical factors of variation (FoV). Measures whether the model has factored the data-generating process into modular components.
- **Validation approach:** Trained on synthetic datasets (dSprites, Shapes3D, MPI3D) with ground-truth factors; demonstrated that β-VAE with KL-divergence constraint learns disentangled representations.
- **Computational cost:** High — requires dedicated evaluation dataset with systematically intervened factors and multi-class classifier training.
- **OOD correlation:** Strong. High disentanglement predicts downstream sample efficiency and OOD transfer, including sim-to-real robotic manipulation tasks.

---

### 5.2 Mutual Information Gap (MIG) — Chen et al. (2018)

- **Citation:** Chen, T. Q., et al. (2018). Isolating Sources of Disentanglement in Variational Autoencoders. *Proceedings of NeurIPS*.
- **Measure name:** $\text{MIG}(v_k) = \frac{I(z_{j^{(1)}}; v_k) - I(z_{j^{(2)}}; v_k)}{H(v_k)}$ — normalized gap between highest and second-highest mutual information between any latent coordinate and a target ground-truth factor
- **Construct captured:** Measures whether a single latent coordinate uniquely captures a single factor of variation, penalizing representations where information about one factor is split across multiple latents.
- **Validation approach:** Evaluated across synthetic datasets (dSprites, Shapes3D); validated on 4,260 models with systematic hyperparameter sweeps. Demonstrated that disentanglement is theoretically impossible without inductive biases but emerges in practice due to geometry of optimization paths.
- **Computational cost:** High — requires estimating mutual information matrix across all latent dimensions and factors, scaling as $O(|Z| \cdot |V| \cdot N \log N)$.
- **OOD correlation:** Exceptionally strong. High MIG predicts OOD robustness in sim-to-real transfer and novel target position generalization in robotic manipulation.

---

### 5.3 DCI (Disentanglement, Completeness, Explicitness) — Eastwood & Williams (2018)

- **Citation:** Eastwood, C., & Williams, C. K. I. (2018). A Framework for the Quantitative Evaluation of Disentangled Representations. *Proceedings of ICLR*.
- **Measure name:** Disentanglement ($D$), Completeness ($C$), Explicitness ($E$) — three independent metrics
- **Construct captured:**
  - *Disentanglement*: Degree to which each latent variable $z_i$ is informative about at most one ground-truth factor $v_j$ (computed via entropy of regressor importances)
  - *Completeness*: Extent to which each ground-truth factor $v_j$ is captured by a single latent variable $z_i$
  - *Explicitness*: How easily ground-truth factors can be recovered from $Z$ using simple linear or shallow predictors
- **Validation approach:** Validated on robotic manipulation setups with weak supervision; demonstrated that disentanglement metrics break down when real-world factors are correlated, requiring weak supervision during training or post-hoc corrections.
- **Computational cost:** High — requires training multi-class regressors or computing feature importance tables.
- **OOD correlation:** Exceptionally strong. High DCI predicts downstream sample efficiency and robust OOD transfer under distribution shifts (sim-to-real transfer, novel target positions). Prevents optimization pathways from interfering, allowing downstream decoders to generalize feature-by-feature to unseen coordinate combinations.

---

### 5.4 Dimensionwise Mutual Information — Ridgeway & Mozer (2015)

- **Citation:** Ridgeway, K., & Mozer, M. C. (2015). Learning Deep Disentangled Embeddings with the F-Statistic Loss. *Proceedings of NeurIPS*.
- **Measure name:** Dimensionwise mutual information — per-latent-dimension MI with each ground-truth factor
- **Construct captured:** Quantifies information sharing between individual latent dimensions and generative factors; basis for MIG and related metrics.
- **Validation approach:** Evaluated on synthetic factor-varying datasets; shown to be consistent but high-variance in high-dimensional settings.
- **Computational cost:** High — same as MIG.
- **OOD correlation:** Indirect — feeds into MIG and DCI, which have strong OOD correlation.

---

## Part VI: Compositional Representation Measures

### 6.1 Systematicity, Productivity, Substitutivity, Localism, Overgeneralisation — Hupkes et al. (2020)

- **Citation:** Hupkes, D., Veldhoen, S., & Zuidema, W. (2020). Compositional Generalization and Natural Language Processing: Explaining Category-Level Multi-Task Generalization. *arXiv:2006.15951*.
- **Measure name:** Five behavioral metrics: Systematicity, Productivity, Substitutivity, Localism, Overgeneralisation
- **Construct captured:** Rule-governed symbolic composition vs template-matching and memorization:
  - *Systematicity*: Recombining known rules into novel, unseen combinations
  - *Productivity*: Unboundedness — generalizing to sequence lengths / recursion depths greater than training
  - *Substitutivity*: Robustness to synonym substitution
  - *Localism*: Whether nested constituents are resolved locally before integration
  - *Overgeneralisation*: Balance between rule extraction and exception memorization
- **Validation approach:** Evaluated using PCFG-SET dataset across LSTM, CNN, and Transformer models. All models achieved near-perfect accuracy on standard test sets but performance dropped by 22–34% under Systematicity and Productivity tests. Standard evaluations fail to capture compositional generalization failures.
- **Computational cost:** Low to moderate — behavioral evaluations across targeted distribution splits. Topographic Similarity scales as $O(N^2)$ where $N$ is evaluation vocabulary size.
- **OOD correlation:** Exceptionally strong. Directly measures the network's capacity to extrapolate to unbounded lengths and novel factor configurations. Designing models that maximize systematicity and productivity metrics guarantees structured, robust OOD generalization.

---

### 6.2 Topographic Similarity (Topsim) — Resnik et al. (2016)

- **Citation:** Resnik, P., et al. (2016). Measuring Compositionality in Sign Language. *ICLR Workshop*.
- **Measure name:** Topographic Similarity — Spearman correlation between pairwise distances in meaning space and pairwise distances in representational space
- **Construct captured:** Whether the structure of the meaning space is preserved in the model's representational space; a necessary condition for compositional encoding.
- **Validation approach:** Applied to emergent language studies; validated on compositional communication protocols.
- **Computational cost:** $O(N^2)$ where $N$ is the evaluation vocabulary size.
- **OOD correlation:** Moderate — topographic similarity is a necessary but not sufficient condition for systematic generalization.

---

### 6.3 Iterated Learning Bottleneck Pressure — Kirby et al. (2014), Ren et al. (2020)

- **Citation:** Kirby, S., et al. (2014). Compression and communication in the cultural evolution of linguistic structure. *Cognition*.
- **Measure name:** Iterated Learning convergence rate — speed at which compositional structure emerges across generations
- **Construct captured:** Pressure toward compositionality when models learn from the outputs of previous generations (iterated bottleneck), forcing compression of the meaning-to-signal mapping.
- **Validation approach:** Theoretical and empirical demonstration that iterated bottleneck pressures outperform single-generation models optimized with standard early stopping. Analyzed in emergent language protocols.
- **Computational cost:** Moderate — requires sequential training across multiple generations.
- **OOD correlation:** Strong — iterated learning produces more systematic representations, directly linked to OOD compositional generalization.

---

## Part VII: Shortcut Learning Detection

### 7.1 Information Plane MI Trajectory ($I(X; Z)$) — Adnan et al. (2022)

- **Citation:** Adnan, M., et al. (2022). Understanding Deep Learning via Information Plane Trajectories. *arXiv*.
- **Measure name:** $I(X; Z)$ trajectory — mutual information between raw inputs and hidden representations over training
- **Construct captured:** Shortcut learning detection: shortcuts are visually or statistically simpler than semantic rules, causing highly compressed representations captured by a sharp decrease and low convergence value of $I(X; Z)$. Formally: $\text{Shortcut Signal} \propto -\Delta I(X; Z)$.
- **Validation approach:** Tracked on MNIST with synthetic white patches and CelebA with highly correlated facial attributes; correlated with performance on de-biased OOD test sets.
- **Computational cost:** Extremely high — requires variational MI estimation (MINE or $f$-DIME).
- **OOD correlation:** Exceptionally strong negative predictor. High shortcut reliance (sharp $I(X; Z)$ drop) predicts catastrophic OOD performance degradation.

---

### 7.2 ShorT (Shortcut Testing) — Brown et al. (2023)

- **Citation:** Brown, S., et al. (2023). ShorT: A Fairness Metric for Shortcut Learning Detection. *Proceedings*.
- **Measure name:** ShorT correlation coefficient — correlation between fairness deterioration and level of spurious attribute encoding
- **Construct captured:** Systematic quantification and control of spurious attribute encoding via three steps: (1) define a fairness metric (e.g., separation — difference in error rates given true labels), (2) quantify spurious encoding via transfer head MAE on spurious attribute, (3) control via multi-task gradient scaling factor $\lambda$.
- **Validation approach:** Validated on ISIC skin lesion diagnostics and chest radiographs; demonstrated that high correlation coefficient between fairness deterioration and spurious encoding confirms shortcut reliance.
- **Computational cost:** Moderate to high — requires training families of models with varying gradient scaling factors $\lambda$.
- **OOD correlation:** Exceptionally strong. Directly diagnoses the model's performance collapse when spurious correlations break.

---

### 7.3 Unsupervised Prototype Activation Matching

- **Citation:** Referenced in unsupervised concept activation literature (various).
- **Measure name:** Prototype activation matching — identification of image patches or tokens that activate decision heads via prototype learning and MLLM-based concept detection
- **Construct captured:** Whether highly active patches correspond to spurious features (e.g., clinical markers) rather than target pathology, indicating shortcut reliance.
- **Validation approach:** Applied to medical imaging datasets; demonstrated on chest radiographs where clinical markers correlate with diagnostic labels.
- **Computational cost:** Low to moderate — runs on consumer hardware in minutes using pretrained MLLMs.
- **OOD correlation:** Moderate to strong. Unsupervised detection of spurious activation patterns without requiring ground-truth factor labels.

---

## Summary Matrix

| Proxy Family | Representative Measure | Construct Captured | OOD Correlation | Computational Cost |
|---|---|---|---|---|
| RSA | RDM Consistency (Mehrer & Kietzmann, 2020) | Geometric alignment across seeds/layers | Moderate | High ($O(N^2 \cdot D)$) |
| Probing | Control Task Selectivity (Hewitt & Liang, 2019) | Rule encoding vs. memorization | Strong | Low ($O(N \cdot D)$) |
| Intraclass Clustering | Layer Subclass Selectivity $c_3$ (Carbonnelle & De Vleeschouwer, 2021) | Unsupervised semantic subclass grouping | Exceptionally Strong | Moderate ($O(I \cdot N_s^2 \cdot D)$) |
| Information-Theoretic | $I(X; Z)$ trajectory (Adnan et al., 2022) | Fitting vs. compression, shortcut detection | Strong | Extremely High (MINE) |
| Disentanglement | MIG / DCI (Chen et al., 2018; Eastwood & Williams, 2018) | Latent factor alignment with FoV | Exceptionally Strong | High ($O(|Z| \cdot |V| \cdot N \log N)$) |
| Compositional | Systematicity + Productivity (Hupkes et al., 2020) | Rule-governed composition vs. template matching | Exceptionally Strong | Low–Moderate (behavioral) |
| Shortcut Detection | ShorT coefficient (Brown et al., 2023) | Spurious correlation reliance | Exceptionally Strong (negative) | Moderate–High |

---

## Synthesis: Navigating the Representational Landscape

Characterizing internal representation structure during training requires a multi-faceted approach. As networks transition from statistical memorization to rule-based schema coherence, their latent spaces undergo transformations tracked through geometric, information-theoretic, and behavioral lenses.

**Strongest OOD predictors:**
- *Intraclass clustering quality* — acts as an implicit regularizer directly predicting generalization accuracy
- *Disentanglement metrics (DCI, MIG)* — predict downstream sample efficiency and OOD robustness
- *Compositionality tests (Systematicity, Productivity)* — directly measure unbounded OOD extrapolation capacity

**Strongest negative predictors (shortcut detection):**
- *Information Plane $I(X; Z)$ trajectory* — sharp compression signals shortcut latching
- *ShorT correlation coefficient* — directly diagnoses performance collapse when spurious correlations break

**Lowest cost, highest diagnostic value:**
- *Control Task Selectivity* — $O(N \cdot D)$, captures rule encoding vs. memorization
- *Systematicity/Productivity behavioral tests* — behavioral evaluation, no probe training required

**Recommended combination:** Deploy structural probes (selectivity) + behavioral compositionality tests + intraclass clustering metrics in tandem. This triangulation approach provides: (1) whether the model encodes rules, (2) whether those rules generalize to novel compositions, and (3) whether the representation space spontaneously organizes around meaningful categories.

---

## References

- Adnan, M., et al. (2022). Understanding Deep Learning via Information Plane Trajectories. *arXiv*.
- Belinkov, Y. (2021). Probing Classifiers: Promises, Shortcomings, and Advances. *Computational Linguistics*.
- Brown, S., et al. (2023). ShorT: A Fairness Metric for Shortcut Learning Detection. *Proceedings*.
- Burgess, C. P., et al. (2018). Understanding Disentangling in β-VAE. *arXiv:1804.03599*.
- Carbonnelle, S., & De Vleeschouwer, C. (2021). Neuron and Layer Subclass Selectivity Measures. *arXiv:2110.14521*.
- Chen, T. Q., et al. (2018). Isolating Sources of Disentanglement in VAEs. *NeurIPS*.
- Eastwood, C., & Williams, C. K. I. (2018). A Framework for Quantitative Evaluation of Disentangled Representations. *ICLR*.
- Hewitt, J., & Liang, P. (2019). Designing and Interpreting Probes with Control Tasks. *EMNLP*.
- Higgins, I., et al. (2017). β-VAE: Learning Basic Visual Concepts with a Constrained Variational Framework. *ICLR*.
- Hupkes, D., et al. (2020). Compositional Generalization and NLP: Explaining Category-Level Multi-Task Generalization. *arXiv*.
- Kirby, S., et al. (2014). Compression and communication in the cultural evolution of linguistic structure. *Cognition*.
- Kornblith, S., et al. (2019). Similarity of Neural Network Representations Revisited. *ICML*.
- Mehrer, J., & Kietzmann, T. C. (2020). Representational Stability of Deep Neural Networks. *arXiv*.
- Ren, Y., et al. (2020). Iterated Learning for Emergent Systematicity in VQA. *ICLR*.
- Resnik, P., et al. (2016). Measuring Compositionality in Sign Language. *ICLR Workshop*.
- Ridgeway, K., & Mozer, M. C. (2015). Learning Deep Disentangled Embeddings with the F-Statistic Loss. *NeurIPS*.
- Shwartz-Ziv, R., & Tishby, N. (2017). Opening the Black Box of Deep Neural Networks via Information. *arXiv*.
