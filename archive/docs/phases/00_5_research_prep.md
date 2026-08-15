# Phase 00_5 — Research Preparation

**Deadline**: 12 Jul 2026
**Dependencies**: None
**Output**: Completed research artefacts forming the evidence base for all subsequent phases
**Executor**: **User-led** — this phase is executed by the user using Consensus AI, AI Deep Research, and general top AI models. The agent does not perform any of these research tasks.

---

This phase prepares the biological and methodological grounding for the protein domain experiments. The user executes all research tasks using their chosen tools. Each research area below includes:

1. **Research question** — what needs to be known
2. **Tool recommendation** — which tool to use for this specific question
3. **Prompt** — copy-paste ready prompt for the recommended tool
4. **Expected output** — what artefact the research should produce
5. **Decision** — how the output feeds into subsequent phases

---

## Research Area A: Pfam Database Deep-Dive

**Tool**: Consensus AI (paper-focused literature review)

### A.1: Pfam content and structure
- **Prompt**: "What is the internal structure of the Pfam database (version 38.2)? Describe Pfam-A vs Pfam-B, clans, seed alignments vs full alignments, Stockholm format annotations, domain architecture representation, and the relationship between Pfam families, PDB structures, and SCOP/CATH classifications. Include the number of families, clans, and typical domain architecture lengths in 38.2."
- **Expected output**: Reference document `docs/research/pfam-structure-notes.md`
- **Decision**: Informs data pipeline design in Phase 01 (what data to download, how to parse, what filters to apply)

### A.2: Domain architecture compositionality in nature
- **Prompt**: "What does the scientific literature say about the recombinatorial grammar of protein domain architectures? How do existing domain combinations constrain new combinations? What is known about fold compatibility, domain neighbour preferences, and the evolutionary processes (gene fusion, shuffling, duplication) that produce domain architectures? Cite key papers with sample sizes and methods."
- **Expected output**: Reference document `docs/research/domain-grammar-literature.md`
- **Decision**: Informs hypothesis framing for H1/H2 and split construction in Phase 01/07

### A.3: Pfam in machine learning
- **Prompt**: "How has the Pfam database been used in machine learning for proteins? Describe every benchmark, dataset split strategy, and evaluation methodology that uses Pfam data. Cover TAPE, PEER, DeepProtein, and any domain-architecture-specific benchmarks. What train/validation/test split strategies exist (family-level, sequence-identity, fold-level)? What are known failure modes of ML models on Pfam data?"
- **Expected output**: Reference document `docs/research/pfam-ml-literature.md`
- **Decision**: Informs baseline selection and novelty claim in paper

---

## Research Area B: ESM Model Family Audit

**Tool**: AI Deep Research (comprehensive, multi-source investigation)

### B.1: ESM-2 training data and architecture
- **Prompt**: "Provide a comprehensive audit of ESM-2 training data, architecture, and known limitations. Include: (1) exact UniRef version and date used for pretraining each ESM-2 model size (8M, 35M, 150M, 650M, 3B, 15B); (2) tokenization scheme and vocabulary; (3) number of layers, hidden dimensions, attention heads per model size; (4) training compute budget (GPU-hours, hardware); (5) known data leakage risks — which protein sequence databases overlap between ESM-2 training data and Pfam 38.2; (6) known biases — sequence length distribution, taxonomic bias, under-representation of certain fold classes; (7) published evaluations of ESM-2 representation quality on domain-level tasks. The ESM-2 paper is Lin et al. 2023, Science."
- **Expected output**: Reference document `docs/research/esm2-audit.md`
- **Decision**: Informs Phase 6 ESM-2 validation design, data leakage documentation in paper

### B.2: Comparison of protein language models for domain tasks
- **Prompt**: "Compare ESM-2, ProtT5, ProstT5, ESM-1b, and any other protein language models on domain-level downstream tasks. Which models use domain-aware training objectives? Which models have been evaluated on domain architecture prediction, domain boundary detection, or domain combination prediction? What are the state-of-the-art results on these tasks? Include per-model parameter counts, training data, and availability (open-source API, HuggingFace, license)."
- **Expected output**: Reference document `docs/research/plm-comparison.md`
- **Decision**: Informs Phase 6 model selection (ESM-2 650M was chosen; this confirms or suggests alternatives)

---

## Research Area C: Pre-registration Protocol Design

**Tool**: General top AI model (unbiased, optimal confirmation of statistical design)

### C.1: Statistical power analysis for N=500
- **Prompt**: "I am designing a pre-registered experiment with N=500 runs (split across 3 conditions). The primary hypothesis test is a Welch's t-test comparing two groups (high σ_A vs low σ_A) on OOD accuracy, with Bonferroni correction for 8 comparisons (α = 0.00625). The expected effect size is Cohen's d ≥ 0.5. (1) Verify that N=500 is sufficient for 80% power at α = 0.00625 with d = 0.5. (2) Recommend the optimal allocation ratio between high/low σ_A groups. (3) Identify any statistical assumptions that could be violated (normality, homoscedasticity) and recommend robustness checks. (4) Design a secondary analysis plan using Bayesian estimation. (5) Should we use a median split or a quantile-based split for the σ_A threshold θ_σ? Justify. (6) Is there a better approach than dichotomisation (e.g., regression with σ_A as continuous predictor)? Compare approaches."
- **Expected output**: Reference document `docs/research/power-analysis.md`
- **Decision**: Fixes the OSF pre-registration protocol before any data collection

### C.2: Pre-registration document template
- **Prompt**: "Draft a complete OSF pre-registration for the following experiment. Study design: N=500 runs of a transformer language model trained on Pfam domain architecture sequences, with 3 conditions (familiar combinations, new combinations of familiar families, cross-fold combinations). Primary outcome: OOD accuracy on domain architecture prediction. Primary test: Welch's t-test comparing high-σ_A vs low-σ_A groups on OOD accuracy, Bonferroni-corrected α = 0.00625. Secondary outcomes: ΔCG (compositional gap), σ_A trajectories, phase transition detection. Exclusion criteria: NaN loss during training, final accuracy < 10%, failed training. Data provenance: Pfam 38.2, seed formula: run_id * 42 + 7. The output should be a ready-to-copy-paste pre-registration in OSF format with all sections (Study Information, Design Plan, Sampling Plan, Variables, Analysis Plan, Other)."
- **Expected output**: Draft ready for OSF registration at `docs/research/osf-preregistration-draft.md`
- **Decision**: Registered on OSF before Phase 3 execution

### C.3: Pilot experiment design confirmation
- **Prompt**: "Given the planned N=500 brittle domain similarity experiment on Pfam domain architectures, what pilot experiment should we run first to validate the experimental setup before committing to the full N=500? Propose a pilot with N=15 runs (matching the existing sigma-model experiment pattern) that tests: (1) that the model can train to convergence on Pfam data; (2) that the σ_A proxy measurements show variance across runs; (3) that the OOD splits are neither too easy (ceiling effects) nor too hard (floor effects). What go/no-go criteria should the pilot meet before proceeding to N=500? What sample size is needed for the pilot to detect whether the experimental pipeline is working?"
- **Expected output**: Reference document `docs/research/pilot-design.md`
- **Decision**: Pilot run design used in Phase 3 before full N=500 launch

---

## Research Area D: Benchmark Design Research

**Tool**: AI Deep Research (for comprehensive domain landscape mapping)

### D.1: Existing protein compositional generalisation benchmarks
- **Prompt**: "Search the entire literature for existing benchmarks of compositional generalisation on protein data. A compositional generalisation benchmark tests whether a model can generalise to unseen combinations of known components. This is distinct from standard protein benchmarks (remote homology detection, fold classification, function prediction). Do any existing benchmarks: (1) systematically partition protein domain architectures into ID/OOD splits by recombination distance; (2) measure compositional gap (ΔCG = Acc_ID - Acc_OOD); (3) provide standardised evaluation protocols for domain recombination generalisation? Search for: domain architecture benchmarks, domain combination prediction, protein module recombination, and any benchmark that uses the term 'compositional generalisation' with proteins. Cite all relevant benchmarks."
- **Expected output**: Reference document `docs/research/existing-benchmarks.md`
- **Decision**: Establishes novelty of PfamCG-1.0; informs design choices in Phase 7

### D.2: Biological validation criteria for benchmark splits
- **Prompt**: "For a benchmark that partitions Pfam domain architectures into training and test splits by recombination distance, what biological validation criteria should the splits satisfy? Consider: (1) fold compatibility — domains that physically interact should appear more often together; (2) domain neighbour statistics — certain domain pairs (e.g., kinase + SH2) are evolutionarily conserved; (3) phylogenetic conservation — architectures conserved across deep evolutionary time should not be artificially separated; (4) HMMER bit score distributions — what threshold separates plausible from implausible domain combinations? (5) Known protein interaction databases (STRING, BioGRID, iPfam) — can they validate whether OOD combinations are biologically plausible? Provide specific, actionable validation tests."
- **Expected output**: Reference document `docs/research/benchmark-validation-criteria.md`
- **Decision**: Informs PfamCG-1.0 validation pipeline in Phase 7

---

## Research Area E: Kaggle Environment Validation

**Tool**: General top AI model (practical, tool-oriented)

### E.1: Kaggle GPU experiment architecture
- **Prompt**: "Design the execution architecture for running N=500 neural language model training runs on Kaggle GPUs (Tesla T4, 16GB VRAM). Each run trains a transformer with d_model=256, nhead=8, num_layers=4, vocab_size=22000 on domain architecture sequences. Constraints: Kaggle has 30-hour session limits, 30GB disk, and inference-only GPU for free tier (or usage quotas for GPU-enabled notebooks). Address: (1) how to distribute N=500 runs across sessions; (2) checkpointing strategy to resume interrupted runs; (3) result aggregation across sessions; (4) dataset caching to avoid re-downloading; (5) parallel execution strategy (multiple notebooks in parallel); (6) Kaggle API or Kaggle Notebooks interface; (7) how to monitor progress across 500 runs; (8) estimated total cost (if using paid GPU quotas)."
- **Expected output**: Reference document `docs/research/kaggle-experiment-architecture.md`
- **Decision**: Feasibility check; informs Phase 3 execution plan

### E.2: Google Colab alternative assessment
- **Prompt**: "Compare Kaggle (T4, 16GB, 30hr session) vs Google Colab (T4/V100/A100, usage quotas, 12–24hr session) vs a local GPU setup for running N=500 transformer training runs. Consider: cost, session limits, disk space, upload/download bandwidth, GPU availability, reproducibility (fixed environments), ability to run many parallel experiments, and ease of result collection. Which platform is optimal for this specific experiment? What hybrid strategy (e.g., use both platforms) would be most robust?"
- **Expected output**: Recommendation in `docs/research/kaggle-experiment-architecture.md`
- **Decision**: Platform selection confirmed for Phase 3

---

## Research Outcome Summary

| Research Area | Output File | Feeds Into | Status |
|---------------|-------------|------------|--------|
| A.1 Pfam structure | `docs/research/pfam-structure-notes.md` | Phase 01 data pipeline | [x] |
| A.2 Domain grammar literature | `docs/research/domain-grammar-literature.md` | Paper §2 background, H1/H2 framing | [x] |
| A.3 Pfam ML literature | `docs/research/pfam-ml-literature.md` | Paper §7 related work, baseline selection | [x] |
| B.1 ESM-2 audit | `docs/research/esm2-audit.md` | Phase 06, Paper §2.3 | [x] |
| B.2 PLM comparison | `docs/research/plm-comparison.md` | Phase 06 model selection | [x] |
| C.1 Power analysis | `docs/research/power-analysis.md` | OSF pre-registration | [x] |
| C.2 Pre-registration draft | `docs/research/osf-preregistration-draft.md` | OSF registration | [x] |
| C.3 Pilot design | `docs/research/pilot-design.md` | Phase 03 pilot | [x] |
| D.1 Existing benchmarks | `docs/research/existing-benchmarks.md` | Paper §7, PfamCG-1.0 novelty | [x] |
| D.2 Validation criteria | `docs/research/benchmark-validation-criteria.md` | Phase 07 | [x] |
| E.1/E.2 Kaggle/Colab architecture | `docs/research/kaggle-experiment-architecture.md` | Phase 03 execution | [x] |

---

**Phase 00_5 Exit Criteria**:
- [x] All 11 research output documents saved to `docs/research/`
- [ ] Pre-registration uploaded to OSF with all sections populated — *Phase 03 Task 3.1*
- [ ] Kaggle environment confirmed and tested with a single training run — *Phase 03 Task 3.3–3.4*
- [ ] Go/no-go decision documented: is the protein domain σ-trap experiment feasible and well-motivated? — *Phase 03 Task 3.4 pilot*
