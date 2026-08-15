# Phase 0.5 — AI-Assisted Research: σ-Trap Evidence Landscape

**Duration**: 2 weeks (Month 1)
**Deadline**: 2026-07-24
**Dependencies**: Phase 00 (paper directory exists), Paper 01 Phase 0.5 outputs (especially `research/landscape-boundary.md`, `research/schema-coherence-mapping.md`, `research/gap-analysis.md`)
**Output**: Research artifacts in `research/` forming the evidence base for the systematic review protocol
**Executor**: **User-led** — executed using Consensus AI, AI Deep Research, and general top AI models. The agent does not perform these research tasks.

---

This phase prepares the technical and conceptual grounding for the σ-Trap systematic review. Unlike Paper 01 (broad landscape mapping), this phase is narrowly focused on locating and characterizing evidence for schema coherence failure — the σ-trap — as a formal phenomenon in neural network training.

Each research area includes:
1. **Research question** — what needs to be known
2. **Tool recommendation** — which tool to use
3. **Prompt** — copy-paste ready prompt
4. **Expected output** — what artifact the research should produce
5. **Decision** — how the output feeds into subsequent phases

---

## Research Area A: σ-Trap Boundary Definition

**Tool**: AI Deep Research (comprehensive, multi-source investigation)

### A.1: Define the σ-trap as a research construct

- **Prompt**: "Define the σ-trap as a formal research construct in machine learning. The σ-trap is a hypothesized stable low-schema-coherence equilibrium produced by standard SGD training. Schema coherence (σ_A) is the degree to which an agent's internal representations are restructured around deep governing principles rather than surface-statistical regularities. (1) What existing terms in the literature describe similar or overlapping phenomena? Consider: 'shortcut learning', 'Clever Hans effect', 'specification gaming', 'reward hacking', 'goal misgeneralization', 'distributional shift failure', 'robust overfitting', 'memorization vs generalization'. (2) For each related term, provide: definition, first-known usage (paper + year), how it differs from the σ-trap. (3) Which benchmarks are known to elicit σ-trap-like behavior (high ID, low OOD)? (4) Which papers explicitly discuss 'internal representation structure' failure as distinct from data-level or architecture-level failure? (5) Create a boundary definition table: phenomenon — shares mechanism with σ-trap? — shares symptoms? — shares intervention? Cite specific papers for each row."

- **Expected output**: Reference document `research/sigma-trap-boundary.md`
- **Decision**: Informs inclusion/exclusion criteria in Phase 1 — defines what counts as evidence of the σ-trap

### A.2: Identify landmark papers and inflection points

- **Prompt**: "Identify the landmark papers in the study of compositional generalization failure and out-of-distribution failure in neural networks. For each paper provide: (1) full citation, (2) year, (3) task/benchmark used, (4) model type tested, (5) key finding related to OOD failure, (6) whether internal representations were analyzed (and how), (7) whether any intervention was proposed, (8) citation count. Include: SCAN (Lake et al. 2018), COGS (Kim & Linzen 2020), CFQ (Keysers et al. 2020), PCFG-SET (Hupkes et al. 2020), gSCAN (Ruis et al. 2020), COFE (Li et al. 2021), COGS-γ (Qiu et al. 2022), and any others that demonstrate systematic OOD failure. Also include papers that found positive results (successful OOD generalization) and their methods. Total: aim for 20-30 papers."

- **Expected output**: Reference document `research/landmark-papers.md`
- **Decision**: Informs search calibration in Phase 2 (these papers must be captured by search strings)

### A.3: Schema coherence proxies in the literature

- **Prompt**: "Search for papers that measure or approximate internal representation structure in neural networks during training. I am looking for proxies for 'schema coherence' — measures that capture the degree to which a model's internal representations are organized around rules rather than statistics. Search for: (1) representational similarity analysis (RSA) applied during training, (2) probing classifiers for rule vs memorization distinction, (3) clustering quality of hidden representations, (4) mutual information between representations and task structure, (5) disentanglement metrics (β-VAE, DCI, MIG), (6) measures of compositional representation (tree-structured, recursive, or factorized), (7) measures of shortcut learning detection. For each, provide: paper citation, measure name, what it claims to capture, validation approach, and computational cost. Specifically highlight any measure that has been correlated with OOD generalization performance."

- **Expected output**: Reference document `research/coherence-proxies.md`
- **Decision**: Informs data extraction template in Phase 7 (which proxy measures to extract), and informs meta-analysis coding in Phase 9

---

## Research Area B: Empirical Evidence Mapping

**Tool**: Consensus AI (research-specific, citation-grounded)

### B.1: Evidence for σ-trap existence

- **Prompt**: "Find all empirical papers that demonstrate the following pattern: neural networks trained with standard gradient-based optimization achieve high in-distribution accuracy but fail catastrophically on out-of-distribution test sets that require recombination of learned primitives. For each paper: (1) provide full citation, (2) describe the task and OOD split, (3) report ID accuracy, (4) report OOD accuracy, (5) report the ID-OOD gap, (6) note the model architecture, (7) note training hyperparameters, (8) whether any representation analysis was done, (9) whether any intervention improved OOD performance. Cover benchmarks: SCAN, COGS, CFQ, PCFG-SET, gSCAN, COFE, MathQA, QED, NACS, SQUAD compositional splits, and any synthetic reasoning benchmarks. Aim for 20+ papers with extractable numerical results."

- **Expected output**: Reference document `research/empirical-evidence.md`
- **Decision**: Provides the core evidence base for the review; feeds directly into extraction template design

### B.2: Interventions that escape the σ-trap

- **Prompt**: "Find all papers that propose and evaluate interventions aimed at improving compositional generalization or OOD performance in neural networks. For each intervention: (1) provide full citation, (2) describe the intervention (curriculum learning, data augmentation, architectural modification, regularization, representation learning objective, multi-task learning, meta-learning, etc.), (3) report the effect size (improvement in OOD accuracy, Cohen's d if available), (4) note whether the intervention directly targets internal representations or indirectly affects them, (5) compare effect across benchmarks, (6) note computational cost, (7) note whether the intervention is compatible with standard SGD training. Focus on interventions that explicitly or implicitly increase schema coherence. Include negative results (interventions that did NOT improve OOD performance)."

- **Expected output**: Reference document `research/interventions.md`
- **Decision**: Provides the evidence base for comparative effectiveness analysis in Phase 9 (meta-analysis)

### B.3: Theoretical frameworks for σ-trap

- **Prompt**: "Find theoretical or conceptual papers that propose frameworks for understanding why neural networks fail on OOD generalization despite succeeding in-distribution. Cover: (1) the lottery ticket hypothesis — does it explain or relate to OOD failure? (2) The simplicity bias of neural networks — are OOD tasks systematically more complex? (3) The spectral bias / frequency principle — do networks learn low-frequency first, and does this cause OOD failure? (4) Information bottleneck theory — do networks discard task-relevant information? (5) The neural tangent kernel — does NTK theory predict OOD failure? (6) Capacity and generalization bounds — do existing bounds predict the OOD gap? (7) Any other formal frameworks. For each, provide: a summary of the framework, whether it makes testable predictions about OOD failure, whether it suggests specific interventions, and how it relates to the σ-trap concept (schema coherence as a dynamical variable)."

- **Expected output**: Reference document `research/theoretical-frameworks.md`
- **Decision**: Informs the Background section and the theoretical synthesis in Phase 9

---

## Research Area C: Systematic Review Methodology

**Tool**: General top AI model + manual review

### C.1: Identify existing reviews on OOD generalization

- **Prompt**: "Search for existing systematic reviews, scoping reviews, or meta-analyses on compositional generalization, OOD generalization, or shortcut learning in neural networks. For each review found: (1) full citation, (2) review type, (3) number of papers reviewed, (4) databases searched, (5) date range, (6) key findings, (7) gaps identified, (8) whether a meta-analysis was performed. Specifically check whether any existing review has attempted to quantify the ID-OOD gap across benchmarks, or has systematically compared interventions. If no such review exists, state this explicitly as justification for our review. If such reviews exist, explain how our review differs (narrower focus on σ-trap mechanism, different inclusion criteria, more recent date range, meta-analysis component)."

- **Expected output**: Reference document `research/existing-reviews.md`
- **Decision**: Informs Phase 1 protocol justification — explains why a new systematic review is needed

### C.2: Review methodology for ML experiments

- **Prompt**: "Review methodological guidance for conducting systematic reviews of machine learning experimental papers. (1) What are the unique challenges of reviewing ML papers compared to medical trials? (2) How to handle papers that do not report effect sizes or confidence intervals? (3) How to assess risk of bias in ML experiments — what are known sources of bias? (4) How to handle the rapid pace of arXiv preprints — do we include non-peer-reviewed papers, and if so, how to weight them? (5) What meta-analytic methods are appropriate for ML performance metrics (accuracy, F1, AUC)? (6) Are there existing guidelines (e.g., PRISMA-AI or similar)? (7) How to handle studies that compare multiple interventions on different benchmarks? Cite methodological papers or guidelines."

- **Expected output**: Reference document `research/review-methodology.md`
- **Decision**: Informs Phase 2 search strategy, Phase 8 risk of bias tool design, and Phase 9 meta-analysis methods

### C.3: Meta-analysis feasibility assessment

- **Prompt**: "Given the research question: 'What is the effect of σ-targeting interventions on OOD generalization performance compared to standard SGD?', assess the feasibility of a meta-analysis. (1) What effect size measure is most appropriate for accuracy data (Cohen's d, Hedges' g, log odds ratio)? (2) How to handle studies that report accuracy on different benchmarks with different difficulty levels? (3) Is a random-effects model appropriate given expected heterogeneity? (4) What subgroup analyses would be informative (by architecture, by benchmark, by intervention type, by model scale)? (5) How many studies are typically needed for each subgroup? (6) How to handle studies that report multiple OOD splits? (7) What publication bias tests are appropriate for ML meta-analysis? (8) Provide a statistical analysis plan template."

- **Expected output**: Reference document `research/meta-analysis-feasibility.md`
- **Decision**: Informs Phase 9 — the synthesis plan (meta-analysis vs narrative only)

---

## Research Area D: σ-Trap → Safety Bridge

**Tool**: General top AI model (synthesis in context of our specific formalism)

### D.1: Map σ-trap to alignment failure modes

- **Prompt**: "Given the σ-trap concept — a stable low-schema-coherence equilibrium in neural network training — and the formal Σ-Model framework that describes it: (1) Map this concept onto the AI safety literature on mesa-optimization, deceptive alignment, and inner alignment failure. Specifically, identify papers that argue or demonstrate that models which rely on surface statistics (shortcuts, spurious correlations) rather than deep understanding are more likely to exhibit: specification gaming, reward hacking, goal misgeneralization, or deceptive behavior under distribution shift. (2) Find papers that argue that internal representation quality is relevant to safety. (3) Find papers that propose representation-level interventions for safety. (4) Is there any existing literature that explicitly connects compositional generalization failure to alignment failure? (5) Provide a mapping table: failure mode — σ-trap manifestation — safety consequence — evidence level."

- **Expected output**: Reference document `research/safety-connection.md`
- **Decision**: Informs the Discussion section of the systematic review and establishes the bridge to Papers 03 and 07

### D.2: Gap analysis for the systematic review

- **Prompt**: "Based on all research above, synthesize a structured gap analysis that motivates this systematic review. Address: (1) What is known — what can we confidently say about the σ-trap from existing evidence? (2) What is unknown — what aspects of the σ-trap have not been systematically investigated? (3) What is contested — where do studies disagree about the existence, causes, or remedies of σ-trap? (4) What is the evidence gap — are there sufficient comparable studies for meta-analysis? (5) What is the methodological gap — do existing studies use appropriate measures, controls, and reporting standards? (6) Why is filling these gaps important for the broader thesis (that σ-trap = alignment failure)? Provide confidence levels for each claim."

- **Expected output**: Reference document `research/gap-analysis.md`
- **Decision**: Directly informs the Introduction and Discussion of the systematic review

---

## Research Area E: Methodological Calibration

**Tool**: General top AI model + manual review

### E.1: Search term generation

- **Prompt**: "Based on the σ-trap concept and related phenomena, generate comprehensive search terms for a systematic review. Produce: (1) A list of core concepts with synonyms/acronyms/variations: 'compositional generalization', 'systematic generalization', 'out-of-distribution generalization', 'OOD generalization', 'shortcut learning', 'robust overfitting', 'memorization vs generalization', 'schema coherence', 'representational structure', 'internal representation quality', 'compositional failure', 'generalization failure', 'rule learning', 'statistical learning', 'surface statistics'. (2) For each concept, list 3-5 alternative phrasings used in ML/NLP literature. (3) Boolean search strings for each major database (Scopus, Web of Science, ACM DL, IEEE Xplore, arXiv). Use PICO structure: Population (neural networks, deep learning, transformers), Intervention (curriculum, augmentation, regularization, representation learning), Comparison (standard SGD, baseline), Outcome (OOD accuracy, compositional accuracy, generalization gap). (4) Estimate expected yield for each search string. (5) Note which combinations are likely to be too broad or too narrow."

- **Expected output**: Reference document `research/search-terms.md`
- **Decision**: Directly feeds into Phase 2 (Search Strategy Design)

### E.2: Data extraction template design

- **Prompt**: "Design a data extraction template for a systematic review on the σ-trap. The template must capture: (1) Paper ID (P001–PXXX). (2) Bibliographic info (title, authors, year, venue, DOI). (3) Publication type (empirical, theoretical, review, position). (4) Task/benchmark (SCAN, COGS, CFQ, PCFG-SET, gSCAN, custom, etc.). (5) Model architecture (RNN, LSTM, GRU, Transformer, CNN, MLP, ODE, etc.). (6) Model scale (parameters, layers, hidden dimension). (7) Training dataset size. (8) Training regime (standard SGD, curriculum, augmentation, multi-task, meta-learning, σ-coupled, other). (9) ID accuracy reported (mean, SD, n). (10) OOD accuracy reported (mean, SD, n). (11) ID-OOD gap (calculated or extractable). (12) Effect size of intervention vs baseline (Cohen's d, Hedges' g, or raw Δ with CI). (13) Schema coherence proxy measured (yes — name of proxy / no). (14) Internal representation analysis (probing, RSA, clustering, PCA, none). (15) Statistical rigor (confidence intervals reported? error bars? number of seeds? significance tests?). (16) Code availability. (17) Relevance to σ-trap (1-5 scale with justification). (18) Relevance to alignment/safety (1-5 scale with justification). (19) Key limitations stated. (20) Open questions raised. Provide as structured template with field types, controlled vocabularies, and validation rules."

- **Expected output**: Reference document `research/extraction-template.md`
- **Decision**: Directly feeds into Phase 7 (Data Extraction & Charting)

### E.3: Risk of bias criteria

- **Prompt**: "Given a systematic review on the σ-trap in neural network experiments, design a risk of bias assessment tool. This should be adapted from established tools (QUADAS-2, ROBINS-I, PROBAST) for the ML context. Cover domains: (1) Reproducibility — are random seeds reported? Is code available? Are exact training hyperparameters reported? (2) Benchmark validity — is the OOD split appropriate? Is the metric appropriate for the task? (3) Confounding — are comparisons fair (same architecture, same compute, same data)? (4) Reporting completeness — are negative results reported? Are failed OOD splits reported? (5) Statistical rigor — are confidence intervals or error bars reported? Are multiple seeds used? Is statistical significance tested appropriately? (6) External validity — does the finding generalize beyond the specific benchmark? Provide a scoring rubric (Low / Unclear / High risk of bias) with specific criteria for each level. Provide a structured extraction form for each domain."

- **Expected output**: Reference document `research/quality-criteria.md`
- **Decision**: Directly feeds into Phase 8 (Quality Assessment)

---

## Research Execution Plan

| Week | Activities | Tools | Outputs |
|:-----|:-----------|:------|:--------|
| 1 | Areas A (boundary + landmarks + proxies) + C (existing reviews + methodology) | Deep Research, Consensus AI | `sigma-trap-boundary.md`, `landmark-papers.md`, `coherence-proxies.md`, `existing-reviews.md`, `review-methodology.md` |
| 2 | Areas B (empirical evidence + interventions + theoretical frameworks) + D (safety bridge + gap analysis) + E (search terms + extraction template + quality criteria) | Consensus AI, Top model | `empirical-evidence.md`, `interventions.md`, `theoretical-frameworks.md`, `safety-connection.md`, `gap-analysis.md`, `search-terms.md`, `extraction-template.md`, `quality-criteria.md` |
| 2 (end) | Synthesis: compile findings into master research summary | Manual | `research/master-summary.md` — consolidated 3-5 page summary with key decisions for Phase 1 protocol |

---

**Phase 0.5 Exit Criteria**:
- [ ] All research areas A–E completed with artifacts in `research/`
- [ ] `research/master-summary.md` compiled with key decisions
- [ ] Search terms draft ready for Phase 2 refinement
- [ ] Data extraction template draft ready for Phase 7 pilot
- [ ] Risk of bias criteria draft ready for Phase 8
- [ ] Gap analysis identifies clear focus for the systematic review and establishes bridge to Papers 03, 07
- [ ] CC.5.3 satisfied — all research artifacts committed
