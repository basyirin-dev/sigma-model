# Search Terms: Comprehensive Term Library for Systematic Review

**Document type:** Reference — directly feeds Phase 2 (Search Strategy) and Phase 3 (Database Search)
**Purpose:** Converts 350+ extracted concepts into structured, database-ready Boolean strings organized by PICO framework
**Status:** Draft

---

## 1. PICO Framework — Concept Blocks

### Block P: Population (neural network models)

```
"neural network" OR "deep learning" OR "deep net" OR "deep neural network"
OR "transformer" OR "seq2seq" OR "sequence-to-sequence"
OR "LSTM" OR "long short-term memory"
OR "GRU" OR "gated recurrent unit"
OR "RNN" OR "recurrent neural network"
OR "CNN" OR "convolutional neural network"
OR "MLP" OR "multilayer perceptron"
OR "BERT" OR "GPT" OR "LLaMA" OR "T5" OR "BART"
OR "gradient descent" OR "SGD" OR "stochastic gradient descent"
OR "Adam" OR "AdamW"
OR "encoder-decoder" OR "decoder-only"
OR "attention mechanism" OR "self-attention"
OR "graph neural network" OR "GNN"
OR "neural module network" OR "NMN"
OR "MAC" OR "memory attention composition"
OR "FiLM" OR "feature-wise linear modulation"
OR "relation network"
OR "tree-LSTM" OR "tree-structured LSTM"
OR "perceptron"
OR "Fourier neural operator" OR "DeepONet"
```

### Block I/C: Phenomena and Interventions (OOD evaluation / generalization failure / σ-targeting)

```
"compositional generalization" OR "compositional generalisation"
OR "systematic generalization" OR "systematic generalisation"
OR "structural generalization" OR "combinatorial generalization"
OR "out-of-distribution" OR "OOD" OR "OOD generalization"
OR "distribution shift" OR "covariate shift" OR "dataset shift"
OR "generalization gap" OR "generalisation gap"
OR "shortcut learning" OR "spurious correlation" OR "spurious feature"
OR "simplicity bias"
OR "memorization" OR "memorisation" OR "memorization-generalization spectrum"
OR "flat minima" OR "sharp minima" OR "sharpness-aware minimization"
OR "SAM" OR "ASAM" OR "SWAD" OR "MESA" OR "entropy-SGD" OR "entropy SGD"
OR "Friendly-SAM" OR "Tilted-SAM"
OR "loss landscape curvature" OR "perturbation radius"
OR "regularization" OR "weight decay" OR "dropout"
OR "data augmentation" OR "compositional augmentation"
OR "curriculum learning" OR "curriculum"
OR "meta-learning" OR "meta-learning compositionality"
OR "MLC" OR "meta-learning for compositionality"
OR "invariant risk minimization" OR "IRM"
OR "group distributionally robust optimization" OR "group DRO" OR "DRO"
OR "domain generalization" OR "domain adaptation"
OR "information bottleneck" OR "IB objective"
OR "spectral regularization"
OR "homomorphism error" OR "HE regularization"
OR "representation regularization"
OR "feature disentanglement" OR "disentangled representations"
OR "invariant feature" OR "invariant representation"
OR "loss landscape topology" OR "loss landscape geometry"
```

### Block O: Outcome / measurement (failure metric, ID-OOD gap, representation quality)

```
"generalization failure" OR "generalisation failure"
OR "generalization error" OR "generalisation error"
OR "ID-OOD gap" OR "ID OOD gap" OR "ID-OOD performance"
OR "in-distribution" OR "ID performance" OR "ID accuracy"
OR "out-of-distribution accuracy" OR "OOD accuracy"
OR "OOD performance" OR "distribution shift performance"
OR "representational similarity" OR "representation similarity"
OR "CKA" OR "centered kernel alignment"
OR "RSA" OR "representational similarity analysis" OR "representational dissimilarity matrix" OR "RDM"
OR "probing classifier" OR "linear probe" OR "probing task" OR "control task selectivity"
OR "information plane" OR "mutual information" OR "information bottleneck"
OR "MINE" OR "mutual information neural estimation"
OR "disentanglement metric" OR "DCI" OR "MIG" OR "mutual information gap"
OR "shortcut detection" OR "shortcut signal" OR "ShorT"
OR "schema coherence" OR "schema coherence metric"
OR "representational alignment" OR "representational structure"
OR "internal representation quality" OR "representation quality"
OR "representation geometry" OR "representational geometry"
OR "algebraic structure" OR "algebraic representation"
OR "homomorphism" OR "representational homomorphism"
OR "topographic similarity" OR "topsim"
OR "systematicity" OR "productivity" OR "substitutivity"
OR "compositionality gap" OR "compositionality metric"
OR "Jacobian alignment" OR "Jacobian representation"
OR "tangent spaces" OR "gradient alignment"
OR "representation disentanglement"
OR "feature representation" OR "feature geometry"
OR "representation stagnation" OR "representation bottleneck"
OR "loss landscape" OR "loss surface" OR "minima flatness"
OR "sharpness" OR "loss sharpness" OR "eigenvalue Hessian"
```

### Block S: Safety connection (supplementary)

```
"alignment" OR "AI alignment" OR "value alignment"
OR "mesa-optimization" OR "mesa-optimiser" OR "meso-optimization"
OR "inner alignment" OR "inner misalignment" OR "outer alignment"
OR "deceptive alignment" OR "deceptive misalignment"
OR "specification gaming" OR "specification overoptimization"
OR "reward hacking" OR "reward overoptimization"
OR "goal misgeneralization" OR "goal misgeneralisation"
OR "goal misalignment" OR "proxy goal"
OR "sleeper agent" OR "backdoor alignment"
OR "alignment faking" OR "alignment evasion"
```

### Block B: Benchmarks (compositional generalization diagnostics)

```
"SCAN" OR "SCAN benchmark" OR "SCAN command"
OR "COGS" OR "COGS benchmark" OR "COGS semantic parsing" OR "ReCOGS"
OR "CFQ" OR "compositional freebase questions" OR "CFQ benchmark" OR "CFQ MCD"
OR "PCFG-SET" OR "PCFG" OR "string transduction"
OR "gSCAN" OR "grounded SCAN" OR "gSCAN grounded"
OR "SQOOP" OR "spatial queries on object pairs"
OR "CLOSURE" OR "CLEVR-VQA" OR "CLEVR" OR "CLEVR nested reference"
OR "SLOG" OR "structural generalization SLOG"
OR "CoFe" OR "compositional few-shot"
OR "GeoQuery" OR "GeoQuery semantic parsing"
OR "WILDS" OR "WILDS benchmark"
OR "PACS" OR "Office-Home" OR "OfficeHome" OR "DomainNet" OR "TerraIncognita" OR "VLCS"
OR "ImageNet-C" OR "ImageNet-R" OR "ImageNet-Sketch" OR "ImageNet-V2"
OR "domain generalization benchmark"
OR "COFE" OR "MathQA" OR "QED" OR "NACS"
OR "SQuAD compositional" OR "SQuAD generalization"
OR "multi-digit multiplication" OR "last letter concatenation"
OR "logic grid puzzle" OR "math word problem"
OR "compositional celebrities" OR "bamboogle"
OR "Cars3D" OR "dSprites" OR "Shapes3D" OR "MPI3D"
OR "dynamic programming" OR "dynamic-programming"
OR "k-out-of-M" OR "k out of m"
```

---

## 2. Concept–Synonym–Variation Tables

### Core Constructs

| Concept | Synonyms / Variations | Notes |
|---|---|---|
| Compositional generalization | compositional generalisation, systematic generalization, systematic generalisation, structural generalization, combinatorial generalization, algebraic generalization, compositional skills, systematicity | British + American spelling variants essential |
| Out-of-distribution | OOD, distribution shift, dataset shift, covariate shift, domain shift, distributional robustness, domain generalization | OOD may be ambiguous (also "object of desire" in older lit) |
| Shortcut learning | spurious correlation, non-causal feature, simple decision rules, surface statistics, Clever Hans predictor, dataset bias exploitation, background shortcut | Clever Hans is a well-established keyword |
| Schema coherence | representational alignment, representational structure, representation quality, internal representation geometry, algebraic structure preservation, Jacobian alignment | **Novel term** — will have zero hits initially; depends on your own paper being indexed |
| Sharpness / flat minima | sharpness-aware minimization, SAM, ASAM, SWAD, MESA, entropy-SGD, flat minima, sharp minima, loss landscape curvature, perturbation radius, radius of loss ball | SAM is ambiguous (Subject Access Module, etc.) |
| Representation disentanglement | feature disentanglement, disentangled representations, latent disentanglement, latent factors, factors of variation, latent code | "Factor" is overloaded in statistics |

### Benchmarks

| Benchmark | Full name / description | Also called |
|---|---|---|
| SCAN | Command-to-action sequence learning (Lake & Baroni, 2018) | SCAN benchmark, SCAN primitive, SCAN novel |
| COGS | Compositional Generalization on Semantic parsing (Kim & Linzen, 2020) | COGS benchmark, COGS structural, COGS lexical, ReCOGS |
| CFQ | Compositional Freebase Questions (Keysers et al., 2020) | CFQ MCD, MCD splits, CFQ benchmark |
| PCFG-SET | String transduction with 5 behavioral tests (Hupkes et al., 2020) | PCFG benchmark, systematicity test, productivity test |
| gSCAN | Grounded SCAN (Ruis et al., 2020) | gSCAN Split D, gSCAN Split H, grounded SCAN |
| SQOOP | Spatial Queries on Object Pairs (Bahdanau et al., 2019) | SQOOP visual relational reasoning |
| CLOSURE | CLEVR-VQA nested referring expressions (Bahdanau et al., 2020) | CLOSURE CLEVR, CLOSURE benchmark |
| SLOG | Structural generalization for semantic parsing (Li et al., 2023) | SLOG benchmark |
| CoFe | Compositional Few-shot Evaluation (An et al., 2023) | CoFe benchmark, CoFe ICL |

### Interventions

| Intervention | Also called | Mechanism category |
|---|---|---|
| SAM | Sharpness-Aware Minimization | Optimization (sharpness-seeking) |
| ASAM | Adaptive SAM | Optimization (adaptive radius) |
| SWAD | Stochastic Weight Averaging Densely | Optimization (weight averaging) |
| Friendly-SAM | Friendly Sharpness-Aware Minimization | Optimization (regularized sharpness) |
| Tilted-SAM | Tilted Loss SAM | Optimization (tilted objective) |
| MESA | Max-Entropy SGD (not the software) | Optimization (entropy-seeking) |
| Entropy-SGD | Entropy SGD | Optimization (entropy-seeking) |
| MLC | Meta-Learning for Compositionality (Lake & Baroni, 2023) | Meta-learning |
| LeAR | Learning Algebraic Recombination (Liu et al., 2021) | Architectural |
| Vector-NMN | Vector Neural Module Networks (Bahdanau et al., 2019) | Architectural |
| GECA | Good-Enough Compositional Augmentation (Andreas, 2020) | Data augmentation |
| SpanBasedSP | Span-Based Semantic Parsing (Herzig & Berant, 2021) | Architectural |
| LANE | Learning Analytical Expressions (Liu et al., 2020) | Architectural |
| Group DRO | Distributionally Robust Optimization (Sagawa et al., 2019) | Optimization (robust) |
| IRM | Invariant Risk Minimization (Arjovsky et al., 2019) | Optimization (invariant) |
| HE regularization | Homomorphism Error Regularization (An & Du, 2026) | Representation regularization |
| Spectral Regularization | Constrains spectral properties (Yang et al., 2024) | Representation regularization |
| Least-to-Most Prompting | Decomposition prompting (Zhou et al., 2023) | Prompting |
| Self-Ask Prompting | Decomposition prompting (Press et al., 2023) | Prompting |
| Chain-of-Thought | CoT reasoning prompting | Prompting |
| PRISM | Preference-based Reward Invariance for Shortcut Mitigation | Reward model debiasing |

---

## 3. Boolean Search Strings per Database

### Primary Search (P AND I/C AND O)

| Database | Syntax | Search string |
|---|---|---|
| **Scopus** | TITLE-ABS-KEY(...) | `TITLE-ABS-KEY(("neural network" OR "deep learning" OR "transformer" OR "LSTM" OR "RNN" OR "CNN" OR "gradient descent" OR "SGD") AND ("compositional generalization" OR "compositional generalisation" OR "systematic generalization" OR "systematic generalisation" OR "out-of-distribution" OR "OOD" OR "distribution shift" OR "shortcut learning" OR "spurious correlation" OR "schema coherence" OR "representational structure" OR "flat minima" OR "sharpness-aware minimization") AND ("generalization failure" OR "generalisation failure" OR "ID-OOD gap" OR "OOD accuracy" OR "compositional accuracy" OR "representation similarity" OR "CKA" OR "probing classifier" OR "schema coherence" OR "representational alignment" OR "loss landscape" OR "sharpness" OR "flat minima"))` |
| **Web of Science** | TS=(...) | `TS=(("neural network" OR "deep learning" OR "transformer" OR "LSTM" OR "RNN" OR "CNN" OR "gradient descent" OR "SGD") AND ("compositional generalization" OR "compositional generalisation" OR "systematic generalization" OR "systematic generalisation" OR "out-of-distribution" OR "OOD" OR "distribution shift" OR "shortcut learning" OR "spurious correlation" OR "schema coherence" OR "representational structure" OR "flat minima" OR "sharpness-aware minimization") AND ("generalization failure" OR "generalisation failure" OR "ID-OOD gap" OR "OOD accuracy" OR "compositional accuracy" OR "representation similarity" OR "CKA" OR "probing classifier" OR "schema coherence" OR "representational alignment" OR "loss landscape" OR "sharpness" OR "flat minima"))` |
| **ACM DL** | ACM search | Same as WoS, using ACM field tags (Abstract, Title, Keywords) |
| **IEEE Xplore** | "Full Text & Metadata" | Same as WoS, using IEEE field tags |
| **arXiv** | Advanced search (ti: / abs: / and / or) | `abs:"neural network" OR abs:"deep learning" OR abs:"transformer" AND abs:"compositional generalization" OR abs:"OOD generalization" OR abs:"shortcut learning" AND abs:"generalization failure" OR abs:"ID-OOD gap" OR abs:"representation similarity"` |
| **PsycINFO** | APA PsycNet | `AB,DE("neural network" OR "deep learning") AND AB("compositional generalization" OR "systematic generalization") AND AB("generalization failure" OR "shortcut learning")` |

### Secondary Search — Safety Bridge (P AND I/C AND S)

| Database | Search string |
|---|---|
| **Scopus** | `TITLE-ABS-KEY(("neural network" OR "deep learning" OR "transformer") AND ("compositional generalization" OR "compositional generalisation" OR "out-of-distribution" OR "OOD" OR "shortcut learning") AND ("alignment" OR "mesa-optimization" OR "deceptive alignment" OR "goal misgeneralization" OR "specification gaming" OR "reward hacking"))` |
| **WoS** | `TS=(("neural network" OR "deep learning" OR "transformer") AND ("compositional generalization" OR "compositional generalisation" OR "out-of-distribution" OR "OOD" OR "shortcut learning") AND ("alignment" OR "mesa-optimization" OR "deceptive alignment" OR "goal misgeneralization" OR "specification gaming" OR "reward hacking"))` |

### Benchmark-Specific Search (P AND B AND O)

| Database | Search string |
|---|---|
| **All databases** | `(P) AND ("SCAN" OR "COGS" OR "CFQ" OR "PCFG-SET" OR "gSCAN" OR "SQOOP" OR "CLOSURE" OR "SLOG" OR "CoFe" OR "GeoQuery") AND ("generalization failure" OR "compositional accuracy" OR "OOD accuracy" OR "generalization gap")` |

### Broad Search (I/C AND O) — for theoretical/position papers

| Database | Search string |
|---|---|
| **Scopus, arXiv** | `("compositional generalization" OR "systematic generalization" OR "out-of-distribution" OR "OOD" OR "shortcut learning" OR "spurious correlation") AND ("generalization failure" OR "schema coherence" OR "representational structure" OR "loss landscape" OR "sharpness" OR "flat minima")` |

---

## 4. Yield Estimates

### Primary Search (P AND I/C AND O)

| Database | Expected yield | Precision estimate | Notes |
|---|---|---|---|
| Scopus | ~400–600 | ~15–20% | Broadest coverage; may capture domain adaptation papers |
| Web of Science | ~300–450 | ~18–25% | Stronger in formal methods; slightly higher precision |
| ACM DL | ~150–250 | ~20–30% | CS/ML core; fewer false positives |
| IEEE Xplore | ~100–180 | ~20–30% | Formal methods, robustness; good precision |
| arXiv | ~500–800 | ~10–15% | Preprints; very broad; highest recall, lowest precision |
| PsycINFO | ~30–80 | ~25–35% | Cognitive science; high precision for compositional lit |
| **Total (pre-dedup)** | **~1500–2400** | | |

### Secondary Search (P AND I/C AND S)

| Database | Expected yield | Precision estimate | Notes |
|---|---|---|---|
| Scopus | ~80–150 | ~25–35% | Safety-connection papers |
| Web of Science | ~60–120 | ~28–40% | Higher precision |
| ACM DL | ~40–80 | ~30–40% | Good for RL safety papers |
| IEEE Xplore | ~30–60 | ~30–40% | Formal verification angle |
| arXiv | ~150–250 | ~15–20% | Alignment Forum cross-references |
| PsycINFO | ~10–30 | ~20–30% | Cognitive alignment papers |
| **Total (pre-dedup)** | **~370–690** | | |

### Benchmark-Specific Search (P AND B AND O)

| Database | Expected yield | Precision estimate | Notes |
|---|---|---|---|
| Scopus | ~200–300 | ~35–50% | Very targeted |
| Web of Science | ~150–250 | ~40–55% | Highest precision |
| ACM DL | ~80–150 | ~40–55% | Core ML venues |
| IEEE Xplore | ~50–100 | ~40–55% | Formal methods angle |
| arXiv | ~300–500 | ~25–40% | Preprints on benchmarks |
| PsycINFO | ~10–30 | ~40–55% | Cognitive benchmarks |
| **Total (pre-dedup)** | **~790–1330** | | |

### Broad Search (I/C AND O)

| Database | Expected yield | Precision estimate | Notes |
|---|---|---|---|
| Scopus | ~3000–5000 | ~5–8% | Too broad; captures cognitive science, domain adaptation, few-shot |
| arXiv | ~5000–8000 | ~3–6% | Very broad; many false positives |

---

## 5. Too Broad / Too Narrow Diagnostics

| Combination | Problem | Recommendation |
|---|---|---|
| **I/C alone** (compositional generalization OR OOD OR shortcut learning) | Captures cognitive science papers on human morphosyntax, animal cognition, board games, cryptography, mobile UX | Restrict with P (neural network OR deep learning OR transformer) |
| **O alone** (shortcut learning) | Captures board games, cryptography, UX design, learning shortcuts in games | Restrict with neural network terms |
| **P AND I/C with no O** | Captures infinite-width NTK theory papers that don't study generalization failure | Acceptable as secondary search for theoretical papers; exclude from primary |
| **P AND B AND O AND S** | Too narrow: only ~10–20 papers | Use as separate "gold standard" search; keep primary without S block |
| **arXiv with no date filter** | Captures pre-2014 CNNs that don't study compositionality | Add date >= 2014; for compositionality specifically >= 2017 |
| **P AND "SAM" with no disambiguation** | SAM ambiguous (Subject Access Module, S-Adenosyl Methionine) | Always pair SAM with "sharpness-aware" or "loss landscape" |
| **P AND "MESA" with no context** | MESA ambiguous (software package, geographic acronym) | Always pair with "sharpness" or "entropy" or context |
| **P AND "generalization" alone** | Captures all generalization theory papers (VC dimension, PAC learning, etc.) | Too broad; always pair with OOD or compositional |

### Recall risk: known papers that may be missed

| Landmark paper | Risk of missing | Mitigation |
|---|---|---|
| Geirhos et al. 2020 ("Shortcut Learning in Deep Neural Networks") | Low — "shortcut learning" is well-established | Primary search captures this |
| Dziri et al. 2023 ("Faith and Fate") | Low — "compositional" + "transformer" in title | Primary captures; benchmark search catches CLEVR |
| Hubinger et al. 2019 ("Risks from Learned Optimization") | Medium — "mesa-optimization" not in I/C block | Secondary search (P AND I/C AND S) captures this |
| Langosco et al. 2022 ("Goal Misgeneralization") | Medium — RL-focused; may not use "neural network" | Secondary search captures; add "deep reinforcement learning" to P |
| Anthropic 2024/2025 safety papers | High — technical reports, not in databases | Grey literature strategy required (Phase 2 Task 2.3) |

---

## 6. Landmark Paper Recall Validation

Target: **≥95% recall** — any missed paper triggers synonym/alternative addition.

| # | Landmark paper | Benchmark | Primary search? | Benchmark search? | Safety search? | Notes |
|---|---|---|---|---|---|---|
| 1 | Lake & Baroni 2018 (SCAN) | SCAN | Yes | Yes (B=SCAN) | No | Primary captures |
| 2 | Kim & Linzen 2020 (COGS) | COGS | Yes | Yes (B=COGS) | No | Primary captures |
| 3 | Keysers et al. 2020 (CFQ) | CFQ | Yes | Yes (B=CFQ) | No | Primary captures |
| 4 | Hupkes et al. 2020 (PCFG-SET) | PCFG-SET | Yes | Yes (B=PCFG-SET) | No | Primary captures |
| 5 | Ruis et al. 2020 (gSCAN) | gSCAN | Yes | Yes (B=gSCAN) | No | Primary captures |
| 6 | Bahdanau et al. 2019 (SQOOP) | SQOOP | Yes | Yes (B=SQOOP) | No | Primary captures |
| 7 | Bahdanau et al. 2020 (CLOSURE) | CLOSURE | Yes | Yes (B=CLOSURE) | No | Primary captures |
| 8 | Li et al. 2023 (SLOG) | SLOG | Yes | Yes (B=SLOG) | No | Primary captures |
| 9 | Csordas et al. 2021 (Transformer Tricks) | PCFG-SET, COGS | Yes | Yes (B=PCFG-SET, COGS) | No | Primary captures |
| 10 | Qiu et al. 2022 (COGS-vf) | COGS | Yes | Yes (B=COGS) | No | Primary captures |
| 11 | Jiang & Bansal 2021 (Aux Seq Pred) | SCAN | Yes | Yes (B=SCAN) | No | Primary captures |
| 12 | Liu et al. 2021 (LeAR) | COGS, CFQ | Yes | Yes (B=COGS, CFQ) | No | Primary captures |
| 13 | An & Du 2026 (HE Regularization) | COGS, CFQ | Yes | Yes (B=COGS, CFQ) | No | Primary captures |
| 14 | Yang et al. 2024 (Spectral Reg) | generalization | Yes | Partial | No | Primary captures |
| 15 | Teney et al. 2021 (Simplicity Bias) | shortcuts | Yes | Partial | No | Primary captures |
| 16 | Rahaman et al. 2018 (Spectral Bias) | theory | Yes | No | No | Primary captures |
| 17 | Frankle & Carbin 2018 (LTH) | theory | Yes | No | No | Primary captures |
| 18 | Zhang et al. 2021 (Functional LTH) | OOD | Yes | Partial | No | Primary captures |
| 19 | Press et al. 2023 (Compositionality Gap) | LLMs | Yes | No | No | Primary captures |
| 20 | Zhou et al. 2023 (Least-to-Most) | SCAN | Yes | Yes (B=SCAN) | No | Primary captures |
| 21 | Dziri et al. 2023 (Faith and Fate) | CLEVR | Yes | Yes (B=CLEVR) | No | Primary captures |
| 22 | Geirhos et al. 2020 (Shortcut Learning) | shortcuts | Yes | Partial | No | Primary captures |
| 23 | Hubinger et al. 2019 (Risks from LO) | safety | **Maybe** | No | **Yes** | **May miss in primary** — add "learning" context or rely on secondary search |
| 24 | Langosco et al. 2022 (Goal Misgeneralization) | RL | **Maybe** | No | **Yes** | **May miss in primary** — add "deep reinforcement learning" to P for safety search |
| 25 | Anthropic 2024 (Sleeper Agents) | safety | No | No | **Yes** | Grey literature only |
| 26 | Anthropic 2025 (Emergent Misalignment) | safety | No | No | **Yes** | Grey literature only |
| 27 | Lake et al. 2023 (Human-like Systematic Gen) | MLC | Yes | Partial | No | Primary captures |

**Current recall estimate:** 22/27 captured by primary (81.5%); 25/27 captured by primary + secondary (92.6%); 27/27 captured by primary + secondary + grey (100%).

**Action items:**
1. Add "deep reinforcement learning" to Block P to capture Langosco et al. 2022
2. Ensure secondary search covers Hubinger et al. 2019 (already included via "mesa-optimization" in Block S)
3. Grey literature strategy (Phase 2 Task 2.3) required for Anthropic safety papers

---

## 7. Database-Specific Syntax Notes

| Database | Field tags | Date filter | Notes |
|---|---|---|---|
| **Scopus** | TITLE-ABS-KEY(), TITLE-ABS-KEY-OLD() | PUBYEAR > 2017 | Use exact phrase with quotes |
| **Web of Science** | TS=(), TI=(), AB=() | 2017–2026 | Use parentheses for OR groups |
| **ACM DL** | Abstract:, Title:, Keywords: | 2017–2026 | ACM uses "+" for OR in some interfaces |
| **IEEE Xplore** | "Abstract":"...", "Title":"...", "Full Text & Metadata":"..." | 2017–2026 | Use double quotes for exact phrases |
| **arXiv** | ti:, abs:, cat: | 2017–2026 | cat:cs.AI OR cat:cs.LG OR cat:cs.CL |
| **PsycINFO** | AB,DE(), TI(), KW() | 2017–2026 | DE=Thesaurus descriptor |

**Date range:** 2017–2026 (captures the rise of compositional generalization research post-SCAN)
