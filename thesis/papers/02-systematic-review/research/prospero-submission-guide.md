# PROSPERO Submission Guide — Paper 02 Systematic Review Protocol

**URL:** https://www.crd.york.ac.uk/prospero/
**Estimated time:** 20 minutes
**Protocol PDF:** `manuscript/protocol.pdf` (compiled, 14 pages)

---

## Before You Start

1. Create an account at https://www.crd.york.ac.uk/prospero/ if you don't have one
2. Have `protocol.pdf` open for copy-pasting
3. The form autosaves every 30 seconds

---

## Form Field Mapping

### Section 1: Review Title
> **From `protocol.tex` line 5:**
> *Schema Coherence and the $\sigma$-Trap in Neural Network Compositional Generalisation: A Systematic Review Protocol*

**Copy:** `Schema Coherence and the sigma-Trap in Neural Network Compositional Generalisation: A Systematic Review Protocol`

### Section 2: Original Language Title
> Same as above

### Section 3: Review Question(s)
> **From `protocol.tex` lines 76–82:**

**Copy:**
```
Primary: In neural network models trained via gradient-based optimization, what is the effect of sigma-targeting training interventions on compositional out-of-distribution generalization performance compared to standard SGD?

Secondary 1: What empirical evidence exists for the sigma-trap (stable low-sigma_A equilibrium) across benchmarks and architectures?

Secondary 2: What proxy measures of schema coherence have been validated, and how do they correlate with OOD performance?

Secondary 3 (exploratory): What is the relationship between sigma-trap failure and alignment failure modes (mesa-optimization, deceptive alignment)?
```

### Section 4: Searches
> **From `protocol.tex` lines 209–222:**
**Copy:**
```
Databases: Scopus (Elsevier), Web of Science Core Collection (Clarivate), ACM Digital Library, IEEE Xplore, arXiv (cs.AI, cs.LG, cs.CL), PsycINFO (APA PsycNet). Date range: 2017-2026. Grey literature: OpenAlex, Semantic Scholar, Alignment Forum, LessWrong. Supplementary: forward and backward citation tracking from seed papers (Lake 2018, Hupkes 2020, Keysers 2020, Kim & Linzen 2020).
```

### Section 5: URL to Search Strategy
**Enter:** `https://osf.io/` [link to be added after OSF registration]

### Section 6: Condition or Domain Being Studied
**Copy:**
```
Compositional out-of-distribution (OOD) generalisation failure in neural networks, specifically the sigma-trap (schema-coherence trap): a failure mode where models with low internal schema coherence achieve high in-distribution accuracy but catastrophically fail on OOD compositional tasks requiring recombination of learned primitives.
```

### Section 7: Participants/Population
> **From `protocol.tex` lines 147–149:**
**Copy:**
```
Neural network models of any architecture (CNN, RNN, LSTM, GRU, Transformer, ViT, MLP, GNN, neurosymbolic hybrid, differentiable tree machine, state-space model) trained via gradient-based optimisation on supervised compositional generalisation or OOD tasks.
```

### Section 8: Intervention(s), Exposure(s)
> **From `protocol.tex` lines 153–155:**
**Copy:**
```
Any training or architectural modification intended to improve compositional, systematic, or zero-shot generalisation performance, including: sharpness-aware minimisation (SAM, ASAM, GSAM, F-SAM); stochastic weight averaging (SWAD, SWA); entropy-SGD; meta-learning for OOD generalisation; data augmentation targeting compositionality; architectural modifications (e.g., attention, relative positional encodings); regularisation (coherence penalties, information bottleneck, variational dropout); and in-context learning strategies for compositional tasks.
```

### Section 9: Comparator(s)/Control
> **From `protocol.tex` lines 159–161:**
**Copy:**
```
Standard empirical risk minimisation (ERM) or standard stochastic gradient descent (SGD) training on the same architecture, dataset, and split. Baseline must be trained on the same in-distribution data as the intervention.
```

### Section 10: Context
**Copy:**
```
Neural network generalisation to out-of-distribution compositional inputs, measured on established benchmarks (SCAN, COGS, CFQ, gSCAN, PCFG-SET, CoFe, CLEVR, SQOOP, CLOSURE) and domain generalisation datasets.
```

### Section 11: Primary Outcome(s)
> **From `protocol.tex` lines 165–167:**
**Copy:**
```
Accuracy (top-1, exact match, or per-example accuracy) reported separately for ID and OOD splits. The primary effect size is the log odds ratio (LOR) of correct classification computed from ID and OOD accuracy.
```

### Section 12: Secondary Outcome(s)
**Copy:**
```
F1-score, AUC-ROC, per-split accuracy (where multiple OOD splits exist), schema coherence proxy measures (probing classifier accuracy, CKA similarity, effective rank, representational similarity, clustering metrics), and any reported measures of representation geometry.
```

### Section 13: Data Extraction (Selection and Coding)
> **From `protocol.tex` lines 271–279:**
**Copy:**
```
Two independent reviewers using a standardised extraction form (80 fields with controlled vocabularies). Pilot extraction on 5 papers with inter-reviewer agreement assessment. Extraction performed study-level; multiple experiments per paper coded via linked sub-forms. Missing data extracted from figures using PlotDigitizer; authors contacted if critical data missing.
```

### Section 14: Risk of Bias (Quality) Assessment
> **From `protocol.tex` lines 313-end:**
**Copy:**
```
Custom sigma-ROB tool covering 6 domains: Population Representativeness, Outcome Measurement, Confounding/Selection Bias, Intervention Fidelity, Reporting Bias, and Reproducibility. Adapted from QUADAS-2, ROBINS-I, and PROBAST+AI. Two independent assessors; conflicts resolved by discussion or third reviewer.
```

### Section 15: Strategy for Data Synthesis
> **From `protocol.tex` lines relevant to meta-analysis:**
**Copy:**
```
Primary synthesis: three-level random-effects meta-analysis with robust variance estimation (REML tau-squared, HKSJ confidence intervals) if k >= 10 studies. Effect size: log odds ratio (LOR). Heterogeneity: I-squared, tau-squared, prediction intervals. Subgroup analyses by intervention family, architecture type, benchmark family. Sensitivity analyses: influence diagnostics, leave-one-out, small-study bias (Egger's test, Doi plot). Publication bias: funnel plot, Egger's regression, trim-and-fill. If k < 10: structured narrative synthesis with per-study effect-size catalogue and Albatross plot.
```

### Section 16: Analysis of Subgroups or Subsets
**Copy:**
```
Subgroup 1: By intervention family (SAM-family, data augmentation, architectural, meta-learning, regularisation). Subgroup 2: By architecture (Transformer vs. RNN vs. CNN). Subgroup 3: By benchmark (SCAN-family vs. COGS-family vs. CFQ vs. gSCAN). Subgroup 4: By model scale (small <1B vs. large >=1B parameters).
```

### Section 17: Type and Method of Review
- **Type:** Systematic review
- **Method:** Meta-analysis (conditional on k >= 10)
- **Health area:** Not applicable (computer science / AI)

### Section 18: Language
**Select:** English

### Section 19: Country
**Select:** Malaysia

### Section 20: Other Registration Details
- **PROSPERO submission date:** [today's date]
- **Current review status:** Not yet started (protocol stage)

### Section 21: Reference and URL of Published Protocol
**Enter:** OSF URL (to be obtained)

### Section 22: Dissemination Plans
**Copy:**
```
Results will be submitted to a peer-reviewed journal (target: Artificial Intelligence Review or JAIR). Protocol, data, extraction forms, and analysis scripts will be deposited on OSF. The review forms part of a PhD-by-publication thesis.
```

### Section 23: Keywords
**Enter:** `systematic review, meta-analysis, schema coherence, compositional generalization, out-of-distribution generalization, sigma-trap, shortcut learning, neural networks, deep learning, PRISMA-P`

### Section 24: Details of Existing Review
**Copy:**
```
No existing systematic review with meta-analysis covers this specific question. Related narrative surveys: Geirhos et al. 2020 (shortcut learning — narrative, no meta-analysis), Hupkes et al. 2023 (taxonomy of 700+ experiments — NLP only, no meta-analysis), Sinha et al. 2024 (compositional learning — no quantitative synthesis).
```

### Section 25: Review Team Details
| Field | Value |
|-------|-------|
| **Lead reviewer name** | Basyirin Amsyar Basri |
| **Email** | amsyar.basy@gmail.com |
| **Country** | Malaysia |
| **Organisation** | Independent Researcher |
| **Other reviewers** | None |

---

## After Submission

1. PROSPERO will assign an ID (format: `CRD4202XXXXXX`)
2. Email this ID to me
3. I will:
   - Update `protocol.tex` with the ID
   - Update `README.md`
   - Update phase tracking documents
   - Recompile `protocol.pdf`
   - Upload updated PDF to OSF
