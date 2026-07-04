# Theoretical Frameworks for OOD Failure and the σ-Trap

**Document type:** Reference — theoretical synthesis for Background section and Phase 9 meta-analysis
**Purpose:** Why neural networks succeed ID but fail OOD; how each framework maps to the σ-trap concept
**Status:** Draft

---

## Framework Comparison Table

| Framework | Core Claim | OOD Prediction Strength | Suggested Interventions | Relation to σ-Trap |
|---|---|---|---|---|
| **Lottery Ticket + Functional LTH** | Sparse trainable subnetworks exist within dense networks; functional LTH proposes invariant subnetworks survive distribution shift | Yes — if invariant subnetworks exist | Pruning, Modular Risk Minimization, subnetwork search | σ as structure selection — finding high-σ subnetworks |
| **Simplicity Bias** | SGD prefers simpler predictive features, which often coincide with spurious correlations rather than task mechanisms | **Strongest** — directly predicts shortcut collapse when task complexity exceeds shortcut complexity | Diverse-model training with gradient-alignment penalties, SPARE (early spurious detection), GAN-generated unbiased augmentations | Low σ = coherent shortcut schema built from simple features |
| **Spectral Bias / Frequency Principle** | Networks learn low-frequency components before high-frequency ones; stronger on low-frequency than high-frequency functions | Sometimes — if invariant cues are spectrally harder than shortcuts | Frequency-aware regularization | σ tracks global-vs-local feature coherence |
| **Information Bottleneck** | Good representations compress task-irrelevant input information while preserving label-relevant structure | Weak to moderate, **contested** — compression phase not always observed, not evidently causal for generalization | Redundancy filtering, IB objectives, invariant-feature extraction | σ as selective retention of coherent invariants |
| **NTK Theory** | Infinite-width networks behave like kernel methods with frequency-dependent convergence rates | Partial only — NTK assumes lazy linearized dynamics that may underperform real networks | Kernel/frequency shaping, density-aware sampling | σ mostly absent in linearized theory |
| **Capacity / Generalization Bounds** | Norm-based complexity measures bound generalization error | **Too weak** to predict OOD gap — complexity measures can negatively correlate with generalization under stochastic optimization | None specific | N/A |
| **Invariant-Feature / Graph OOD** | Redundant spurious topology drives shift failure; compression isolates invariant structure | Strong (graph-specific) | Structural-entropy IB, subgraph disagreement (DIVE), invariant graph learning | σ as invariant structure extraction from noisy topology |

---

## Part I: Structural and Simplicity Frameworks

### 1.1 Lottery Ticket Hypothesis (Frankle & Carbin, 2018)

- **Citation:** Frankle, J., & Carbin, M. (2018). The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks. *arXiv: Learning*.
- **Summary:** Dense neural networks contain sparse subnetworks ("winning tickets") that, when trained in isolation from the same initialization, can match or exceed the full network's IID test accuracy. Pruning iteratively removes weights with lowest magnitude, identifying a sparse mask that preserves training dynamics.
- **Testable OOD prediction:** The original LTH is about IID generalization, not distribution shift. Does not directly predict OOD failure.
- **Interventions suggested:** Pruning to find sparse, trainable subnetworks.
- **σ-Trap relation:** Conceptual only — σ denotes the degree to which a subnetwork's internal structure is organized around deep principles. A high-σ subnetwork would be one whose sparse connectivity preserves compositional structure rather than surface shortcuts. Original LTH does not address this.

### 1.2 Functional Lottery Ticket Hypothesis (Zhang et al., 2021)

- **Citation:** Zhang, D., Ahuja, K., Xu, Y., Wang, Y., & Courville, A. C. (2021). Can Subnetwork Structure be the Key to Out-of-Distribution Generalization? *Proceedings of NeurIPS*.
- **Summary:** Extends LTH to OOD settings. Proposes that dense networks contain subnetworks whose predictions are more invariant under distribution shift and can outperform the full model OOD when trained in isolation. Subnetwork structure (not just sparsity) determines OOD robustness.
- **Testable OOD prediction:** Yes — biased full networks should still contain less shortcut-prone subnetworks, and structure search should recover them. Testable by pruning + OOD evaluation.
- **Interventions suggested:** Modular Risk Minimization (MRM) — searches for subnetworks with better OOD inductive bias; can combine with other OOD methods.
- **σ-Trap relation:** Strong conceptual link. A high-σ subnetwork would be one whose structure preserves compositional or invariant features across environments. The σ-trap would correspond to the full network converging to a low-σ equilibrium while high-σ subnetworks remain dormant but discoverable via pruning.

### 1.3 Simplicity Bias (Teney et al., 2021; Yang et al., 2023)

- **Citation (primary):** Teney, D., Abbasnejad, E., Lucey, S., & Van Den Hengel, A. (2021). Evading the Simplicity Bias: Training a Diverse Set of Models Discovers Solutions with Superior OOD Generalization. *CVPR*.
- **Citation (early detection):** Yang, Y., Gan, E., Dziugaite, G., & Mirzasoleiman, B. (2023). Identifying Spurious Biases Early in Training through the Lens of Simplicity Bias. *arXiv*.
- **Summary:** SGD-trained networks preferentially fit simpler predictive features first. When spurious correlations are simpler than the true task mechanism, models latch onto shortcuts, achieving high ID accuracy but catastrophic OOD failure. The space of simpler spurious rules grows with task complexity, making OOD failure more likely as tasks become harder.
- **Testable OOD prediction:** **Strongest** — OOD failures rise when the true task mechanism is more complex than available shortcuts. Predicts an early-training signature: examples with spurious features become separable early; if the spurious feature has favorable signal-to-noise, model outputs are dominated by it, hurting worst-group accuracy.
- **Interventions suggested:**
  - Diverse-model training with gradient-alignment penalties (Teney et al., 2021) — forces discovery of more complex predictive patterns
  - SPARE — early spurious-feature detection via training trajectory analysis (Yang et al., 2023)
  - GAN-generated unbiased augmentations to diminish simplicity bias (Verma & Khan, 2024)
- **σ-Trap relation:** **Best conceptual match.** A low-σ regime corresponds to optimization settling on internally coherent but shallow schemas built from simple or spuriously stable cues. The σ-trap is the stable local minimum where simplicity bias has locked the model into a low-complexity, low-schema-coherence equilibrium. Escaping requires forcing the model to discover higher-complexity, higher-σ features.

---

## Part II: Spectral, IB, and NTK Frameworks

### 2.1 Spectral Bias / Frequency Principle (Rahaman et al., 2018; Xu et al., 2022)

- **Citation (primary):** Rahaman, N., Baratin, A., Arpit, D., et al. (2018). On the Spectral Bias of Neural Networks. *Proceedings of ICML*.
- **Citation (survey):** Xu, Z., Zhang, Y., & Luo, T. (2022). Overview Frequency Principle/Spectral Bias in Deep Learning. *Communications on Applied Mathematics and Computation*, 7, 827–864.
- **Citation (practice):** Fridovich-Keil, S., Lopes, R. G., & Roelofs, R. (2021). Spectral Bias in Practice: The Role of Function Frequency in Generalization. *arXiv*.
- **Summary:** Neural networks exhibit a frequency-dependent learning bias: low-frequency components of the target function are learned before high-frequency components. Fourier analysis of ReLU networks confirms that high-frequency functions require finer parameter tuning and more training data. Under non-uniform data density, convergence for a frequency component depends on both its frequency and local sample density (Basri et al., 2020).
- **Testable OOD prediction:** Only under an extra assumption: OOD robustness depends on features that are spectrally "harder" (higher-frequency) than the ID shortcuts. Evidence supports this possibility but does not establish a universal claim that OOD tasks are always higher-frequency.
- **Interventions suggested:** Frequency-aware regularization; density-aware sampling in sparse data regions.
- **σ-Trap relation:** Spectral bias is a **training-dynamics lens** on why some schemas are easier to form than others, not a complete theory of schema coherence itself. In the σ-trap framework, spectral bias explains why low-σ (simple, low-frequency) equilibria are preferentially reached: the optimization trajectory naturally flows toward the easiest-to-learn frequency components first, and without intervention, remains trapped there.

### 2.2 Information Bottleneck (Saxe et al., 2018; Tishby et al., 2000)

- **Citation (critique):** Saxe, A. M., Bansal, Y., Dapello, J., et al. (2018). On the information bottleneck theory of deep learning. *Journal of Statistical Mechanics: Theory and Experiment*, 2019.
- **Summary:** Classical IB theory claims a dual-phase trajectory: (1) a fitting phase where $I(Z; Y)$ increases as the representation encodes target-relevant features, followed by (2) a compression phase where $I(X; Z)$ decreases as the network discards input variability irrelevant to $Y$. Compression is claimed to be causally tied to generalization and induced by SGD noise.
- **Testable OOD prediction:** Weak to moderate. The major critique (Saxe et al., 2018) finds that compression phase claims do not hold in general: ReLU networks often do not show the claimed compression, and compression is not evidently causal for generalization. However, one OOD-relevant idea is preserved: when inputs mix task-relevant and irrelevant information, hidden representations can compress the task-irrelevant part during fitting.
- **Interventions suggested:** Redundancy filtering; IB-style objectives that explicitly maximize $I(Z; Y)$ while minimizing $I(X; Z)$; Conditional Information Flow Maximization (CIFM).
- **σ-Trap relation:** σ maps to **selective retention of coherent invariants**. In the σ-trap, the model fails to compress task-irrelevant information while preserving task-relevant structure — instead, it retains spurious correlations (high $I(X; Z)$ for spurious features) while failing to encode deep structural rules (low $I(Z; Y)$ for compositional features). The σ-trap is an IB failure mode where compression and fitting are misaligned.

### 2.3 Neural Tangent Kernel (Basri et al., 2020; Jacot et al., 2018)

- **Citation:** Basri, R., Galun, M., Geifman, A., et al. (2020). Frequency Bias in Neural Networks for Input of Non-Uniform Density. *Proceedings of ICML*.
- **Summary:** NTK theory shows that infinite-width networks behave like kernel methods with a fixed kernel determined at initialization. Learning follows kernel eigendynamics: components aligned with large eigenvalues of the NTK converge faster. Under non-uniform data density, convergence for a frequency component depends on both its frequency and local sample density, implying slower learning in sparse regions.
- **Testable OOD prediction:** Partial only. NTK provides frequency-dependent convergence predictions but relies on unrealistically wide networks and lazy linearized dynamics. These may underperform real nonlinear networks, so NTK does not cleanly predict real-world OOD gaps.
- **Interventions suggested:** Kernel/frequency shaping; density-aware sampling to address sparse-region convergence.
- **σ-Trap relation:** σ is **mostly absent in linearized theory.** NTK describes the linearized regime around initialization, which is precisely the regime where schema coherence (σ) has not yet emerged. The σ-trap is a phenomenon of the nonlinear training regime where representations reorganize — outside NTK's scope.

---

## Part III: Capacity Bounds and Graph OOD Frameworks

### 3.1 Capacity and Generalization Bounds (Xu et al., 2022; Liu et al., 2024)

- **Citation (bounds critique):** Xu, Z., Zhang, Y., & Luo, T. (2022). Overview Frequency Principle/Spectral Bias in Deep Learning. *Communications on Applied Mathematics and Computation*.
- **Citation (LTH survey):** Liu, B., Zhang, Z., He, P., et al. (2024). A Survey of Lottery Ticket Hypothesis. *arXiv*.
- **Summary:** Norm-based complexity measures (e.g., margin bounds, Rademacher complexity) appear too weak to predict the OOD gap directly. Many complexity measures perform poorly and can even negatively correlate with generalization under stochastic optimization. Lottery-ticket work connects compression to tighter generalization bounds but concerns IID-style generalization rather than which learned rule will survive a shift.
- **Testable OOD prediction:** **Negative** — existing bounds are insufficient. No specific bound predicts the ID-OOD gap reliably.
- **Interventions suggested:** None specific to OOD from bounds theory.
- **σ-Trap relation:** Bounds theory does not address schema coherence directly. The σ-trap is a phenomenon of the optimization landscape's local structure, not captured by global capacity measures.

### 3.2 Invariant-Feature and Graph OOD Frameworks (Di et al., 2025; Sun et al., 2024; Mao et al., 2024)

- **Citation:** Di, Z., Zheng, P., Lu, B., et al. (2025). Graph Out-of-Distribution Generalization Based on Structural-Entropy-Guided Information Bottleneck. *ACM TKDD*.
- **Citation:** Sun, X., Wang, L., Liu, Q., et al. (2024). DIVE: Subgraph Disagreement for Graph Out-of-Distribution Generalization. *KDD*.
- **Citation:** Mao, W., Wu, J., Liu, H., et al. (2024). Invariant graph learning meets information bottleneck for out-of-distribution generalization. *Frontiers of Computer Science*.
- **Summary:** In graph-structured data, redundant or spurious topology is treated as the driver of shift failure. Compression (via information bottleneck) is used to isolate concise, label-relevant invariant structure. Related methods argue that simplicity bias can cause models to lock onto simple structural patterns, so disagreement across models or redundancy filtering can recover broader invariant evidence.
- **Testable OOD prediction:** Strong (within graph domain). Structural-entropy-guided IB predicts that suppressing spurious topology improves OOD generalization. Subgraph disagreement (DIVE) predicts that model disagreement on subgraph importance identifies invariant features.
- **Interventions suggested:**
  - Structural-entropy information bottleneck for graph OOD (Di et al., 2025)
  - Subgraph disagreement (DIVE) for invariant feature identification (Sun et al., 2024)
  - Invariant graph learning with IB constraints (Mao et al., 2024)
- **σ-Trap relation:** **Strongest formal link.** These frameworks treat OOD failure as collapse onto coherent-but-wrong internal structure: simplicity bias explains why the collapse happens, invariant-learning methods explain how to suppress environmentally contingent information while preserving label-relevant structure. The σ-trap corresponds to a stable local minimum where the model's internal graph structure is coherent (locally self-consistent) but wrong (not aligned with the true generative process). Structural-entropy IB and subgraph disagreement are methods to increase σ by filtering spurious structure and preserving invariant structure.

---

## Synthesis: Three Recurring Explanations

### 1. Networks preferentially fit easy or spurious structure

**Simplicity bias** is the clearest mechanism: SGD converges to the simplest predictive features first, and when spurious correlations are simpler than the true task mechanism, models lock into shortcut schemas. This is the **direct explanation** for the σ-trap — a low-σ equilibrium where the model has found a internally coherent but shallow solution.

### 2. Standard IID objectives do not identify invariant mechanisms

Cross-entropy loss on IID data provides no signal to distinguish invariant features from spurious features. The model has no incentive to learn deep structural rules when surface statistics suffice. This is a **structural explanation** for why the σ-trap is stable: the loss landscape has no gradient pointing toward higher σ when the spurious solution already achieves near-zero training error.

### 3. Classical theories explain optimization better than OOD gaps

Spectral bias, NTK, and capacity bounds describe optimization dynamics and IID generalization, but do not cleanly predict which features will survive distribution shift. These are **contributing factors** (spectral bias explains why simple features are learned first; NTK describes the linearized regime where σ has not yet emerged) but not complete theories of OOD failure.

---

## Mapping Frameworks to the σ-Trap

| Framework | σ-Trap Mapping | Which variable? | Intervention Implication |
|---|---|---|---|
| Simplicity Bias | Low σ = coherent shortcut schema | σ as complexity of learned schema | Force discovery of higher-complexity features |
| Functional LTH | High-σ subnetworks exist but are dormant | σ as structural selection | Prune to find high-σ subnetworks |
| Spectral Bias | σ tracks frequency of learned features | σ as frequency content | Frequency-aware training to reach higher-σ features |
| Information Bottleneck | σ = selective retention of coherent invariants | σ as mutual information structure | Compress spurious, preserve invariant |
| Graph OOD | σ = invariant structure extraction | σ as structural entropy filtering | Structural-entropy IB, subgraph disagreement |
| Capacity Bounds | σ not captured by global capacity measures | N/A | N/A |
| NTK | σ absent in linearized regime | N/A (out of scope) | N/A |

### The σ-trap as a dynamical variable

The σ-trap concept synthesizes the strongest elements of existing frameworks:

1. **From simplicity bias:** The σ-trap is a stable local minimum where the model has converged on a simple, internally coherent schema. Escaping requires increasing the complexity of the learned schema (increasing σ).

2. **From functional LTH:** High-σ subnetworks may already exist within the trained model but are not selected by standard training. Structural search (pruning, MRM) can find them.

3. **From spectral bias:** The σ-trap is preferentially reached because low-frequency (low-σ) features are learned first. Without intervention, the model remains in the low-σ basin.

4. **From IB / graph OOD:** The σ-trap is a failure mode of information compression — the model retains spurious structure while failing to encode invariant structure. Increasing σ requires filtering spurious information and preserving coherent invariants.

The σ-trap is **not** predicted by NTK or capacity bounds, which operate outside the regime where schema coherence emerges. It is **most strongly predicted** by simplicity bias, which explains both why the trap exists and why it is stable.

---

## References

- Basri, R., et al. (2020). Frequency Bias in Neural Networks for Input of Non-Uniform Density. *ICML*.
- Di, Z., et al. (2025). Graph OOD Generalization Based on Structural-Entropy-Guided Information Bottleneck. *ACM TKDD*.
- Frankle, J., & Carbin, M. (2018). The Lottery Ticket Hypothesis. *arXiv*.
- Fridovich-Keil, S., et al. (2021). Spectral Bias in Practice. *arXiv*.
- Liu, B., et al. (2024). A Survey of Lottery Ticket Hypothesis. *arXiv*.
- Mao, W., et al. (2024). Invariant graph learning meets information bottleneck. *Frontiers of Computer Science*.
- Rahaman, N., et al. (2018). On the Spectral Bias of Neural Networks. *ICML*.
- Saxe, A. M., et al. (2018). On the information bottleneck theory of deep learning. *JSTAT*.
- Sun, X., et al. (2024). DIVE: Subgraph Disagreement for Graph OOD Generalization. *KDD*.
- Teney, D., et al. (2021). Evading the Simplicity Bias. *CVPR*.
- Verma, A., & Khan, S. S. (2024). Diminishing Simplicity Bias using GAN Generated Unbiased Augmentations. *Canadian AI*.
- Xu, Z., et al. (2022). Overview Frequency Principle/Spectral Bias in Deep Learning. *Comm. Appl. Math. Comput.*.
- Yang, Y., et al. (2023). Identifying Spurious Biases Early in Training. *arXiv*.
- Zhang, D., et al. (2021). Can Subnetwork Structure be the Key to OOD Generalization? *NeurIPS*.
