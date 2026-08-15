# Existing Compositional Generalisation Benchmarks for Protein Domain Architectures

> **Source**: Literature review using DeepSearch AI (Jun 2026)
> **Purpose**: Establish novelty of PfamCG-1.0; inform design choices in Phase 07
> **Target paper**: `paper-neurips/main.tex` ("The Σ-Model in Protein Domain Architectures")

---

## Overview

A compositional generalisation benchmark for protein domain architectures must satisfy three criteria:

1. **Systematic ID/OOD partitioning by recombination distance** — splits are based on novelty of domain adjacencies, not sequence identity or fold class
2. **ΔCG reporting** — compositional gap = Acc_ID − Acc_OOD is measured and reported
3. **Standardised evaluation protocol** — the benchmark is reusable, the OOD splits are pre-defined, and the evaluation procedure is documented

**Finding**: No existing benchmark identified in the reviewed literature satisfies all three criteria simultaneously. This establishes the novelty basis for PfamCG-1.0.

---

## 1. Explicit Recombination Distance Benchmarks

### 1.1 PAGNN (Protein Adjacency Graph Neural Network)

| Property | Detail |
|----------|--------|
| Task | Predict whether two protein domains are adjacent within a multi-domain structure |
| Recombination distance | Yes — predicts domain adjacency, the fundamental unit of recombination |
| Reference | GitHub: `ostrokach/protein-adjacency-net` |

**Assessment**: PAGNN formalises domain adjacency prediction, which is a necessary building block for recombination distance. However, it does not:
- Construct ID/OOD splits based on recombination distance
- Report ΔCG
- Provide a standardised evaluation protocol for full architecture prediction

PAGNN is a methodological contribution toward the problem, not a benchmark for it.

### 1.2 Genomics-Inspired Recombination Metrics

Recombination distance metrics are well-established in genomics for analysing structural variants (NAIBR, Hi-C-based methods) and genome evolution. These principles could theoretically be adapted to domain architectures, but **no existing protein benchmark has done so**.

---

## 2. Implicit / Proxy-Based Benchmarks

These benchmarks create OOD scenarios involving unseen domain combinations but do not formalise recombination distance as a continuous variable.

### 2.1 Antibody DomainBed

| Property | Detail |
|----------|--------|
| Task | Stability classification of antibody–antigen interactions across 5 domains |
| OOD axis | Explicitly includes "domain adjacency" as one of the 5 distribution-shift domains |
| Reference | [arXiv:2407.21028] |

**Assessment**: The most relevant existing benchmark. It probes OOD generalisation across domain adjacency shifts, which directly tests compositional reasoning. Limitations: restricted to antibody domains; does not report ΔCG; does not formalise recombination distance as a continuous variable.

### 2.2 Large-Scale Multi-Task Benchmarks

| Benchmark | Task Coverage | Why Not a CompGen Benchmark |
|-----------|--------------|----------------------------|
| **PEER** | 17 tasks (function, localisation, structure, PPI) | No OOD split based on domain recombination; PPI tasks could proxy for it but are not designed for it |
| **PFMBench** | 38 tasks across 8 areas of protein science | Same limitation — OOD splits are sequence- or structure-based, not adjacency-based |
| **SPURS** | Stability prediction, claims "generalisation to unseen proteins" | "Unseen" criteria undocumented; cannot verify if based on domain recombination |

These benchmarks are valuable for general protein understanding but do not isolate compositional reasoning as a distinct capability.

### 2.3 Recombinant Data Tools

| Tool | Purpose | Reference |
|------|---------|-----------|
| **Protlego** | Generate all possible chimeras between parent proteins for domain shuffling analysis | [bioRxiv 2020] |
| **Domainator** | Search, extract, and cluster proteins by domain-based gene neighbourhoods | GitHub: nebiolabs/domainator |

These are infrastructure tools, not benchmarks. They enable custom OOD dataset construction but provide no standardised evaluation protocol or pre-defined splits.

---

## 3. Generative / Reconstruction Benchmarks

These test domain compatibility from a generative (can the model *create* a valid architecture?) rather than predictive (can the model *classify* an OOD architecture?) perspective.

### 3.1 DOMINO

| Property | Detail |
|----------|--------|
| Task | Generate novel multi-domain protein architectures |
| Approach | Contrastive retrieval model learns domain compatibility space; retrieves partner domains even for unseen pairs |
| Scale | 5 million novel multi-domain proteins generated; diverse CATH annotations recovered |
| Reference | [bioRxiv 2026.05.01.721929] |

**Assessment**: DOMINO directly demonstrates generative understanding of domain compatibility. However, it is a generative framework, not a predictive benchmark. It does not:
- Define ID/OOD splits
- Report ΔCG
- Provide a standardised protocol for model comparison

DOMINO is the strongest piece of related work and should be cited as closest prior art. Its existence strengthens PfamCG-1.0's novelty: if even the most sophisticated generative model of domain compatibility does not provide a standardised predictive benchmark, one is clearly needed.

### 3.2 Inverse Folding Benchmarks

Inverse folding (predicting sequence from backbone structure) tests domain-level understanding implicitly. The **ProteinInvBench** benchmark evaluates inverse folding models on diverse backbones. However, OOD splits are based on structural folds, not domain adjacencies. These benchmarks do not report ΔCG for novel domain combinations.

---

## 4. Cross-Domain Templates

### 4.1 COGS (NLP — Semantic Parsing)

| Property | Detail |
|----------|--------|
| Task | Map natural language sentences to logical forms |
| OOD design | Test contains grammatical constructions composed of known words arranged in novel ways |
| Reference | [arXiv:2109.15101] |

COGS is the gold standard for what a rigorous compositional generalisation benchmark looks like: a formal procedure for generating OOD data based on structural novelty, and a clear metric (accuracy drop) to measure failure. No protein benchmark currently matches this level of formalisation.

---

## 5. Gap Analysis

| Benchmark | Criterion 1 (Recombination distance split) | Criterion 2 (ΔCG reported) | Criterion 3 (Standardised protocol) | Verdict |
|-----------|-------------------------------------------|---------------------------|-------------------------------------|---------|
| PAGNN | Partial (adjacency prediction) | ❌ | ❌ | Fails 2/3 |
| Antibody DomainBed | Partial (domain adjacency axis) | ❌ | ✅ (the benchmark is reusable) | Fails 1/3 |
| DOMINO | ❌ (generative, no OOD split) | ❌ | ❌ | Fails 3/3 |
| PEER | ❌ | ❌ | ✅ | Fails 2/3 |
| PFMBench | ❌ | ❌ | ✅ | Fails 2/3 |
| Protlego | ❌ (tool, not benchmark) | ❌ | ❌ | Fails 3/3 |
| COGS (NLP) | ✅ (structural novelty) | ✅ | ✅ | Not a protein benchmark |
| **PfamCG-1.0 (proposed)** | **✅** | **✅** | **✅** | **Satisfies all 3** |

**Novelty claim**: PfamCG-1.0 is the first benchmark to simultaneously formalise recombination distance as a split criterion (via HMMER bit scores, Types A/B/C), report ΔCG as the primary metric, and provide a standardised community-usable evaluation protocol for domain recombination generalisation.

---

## 6. Implications for Phase 07

| PfamCG-1.0 Design Choice | Literature Gap That Motivates It |
|--------------------------|----------------------------------|
| **Split A (seen-family recombination)** | No existing benchmark tests generalisation to novel combinations of familiar families; Antibody DomainBed comes closest but is antibody-specific |
| **Split B (new family recombinations)** | No benchmark holds out specific families while preserving fold-level familiarity |
| **Split C (cross-clan recombination)** | No benchmark tests generalisation to entirely novel fold contexts at the domain architecture level |
| **ΔCG as primary metric** | No existing benchmark reports a paired ID/OOD accuracy difference as the measure of compositional generalisation |
| **HMMER bit score as recombination distance** | Genomics recombination metrics exist but have never been adapted to protein domain architectures |

### Novelty framing for the paper

The paper should cite the following as closest prior art and explain why each falls short:

1. **Antibody DomainBed**: Only benchmark with a domain-adjacency OOD axis, but restricted to antibodies; no ΔCG; no continuous distance metric.
2. **DOMINO**: Strongest generative model of domain compatibility, but generative paradigm, not predictive; no standardised evaluation protocol.
3. **PEER / PFMBench**: Broad multi-task benchmarks that could proxy for compositional reasoning (via PPI tasks) but lack the specific split design.

### Bibliography status

| Reference | Status in `paper-neurips/bibliography.bib` |
|-----------|------------------------------------------|
| COGS (Kim 2021) | ❌ New |
| DOMINO (2026) | ❌ New |
| Antibody DomainBed (2024) | ❌ New |
| PAGNN (Ostrokach) | ❌ New |
| PEER (Xu 2022) | ❌ New |
| PFMBench (2025) | ❌ New |
| Protlego (2020) | ❌ New |
| SPURS (2025) | ❌ New |
| ProteinGym (Notin 2024) | ✅ Already exists |

---

## References

*Note: Full bibliographic details for each reference are available in the DeepSearch AI research output (40 papers screened, 20 included in synthesis). Key sources listed below.*

Antibody DomainBed. (2024). OOD generalization in therapeutic protein design. *arXiv:2407.21028*.

COGS benchmark. (2021). Compositionality in Grammar and Semantics. *arXiv:2109.15101*.

DOMINO framework. (2026). Multi-domain protein design via contrastive retrieval. *bioRxiv 2026.05.01.721929*.

Ostrokach, A. Protein Adjacency Graph Neural Network (PAGNN). GitHub: ostrokach/protein-adjacency-net.

Protlego. (2020). Software suite for analysis and design of chimeric proteins. *bioRxiv 2020.10.04.325555*.

Xu, M., et al. (2022). PEER: A Comprehensive and Multi-Task Benchmark for Protein Sequence Understanding. *arXiv:2206.02096*.

PFMBench. (2025). Protein Foundation Model Benchmark across 38 tasks. *arXiv:2506.14796*.

SPURS. (2025). Stability prediction with generalisation to unseen proteins. *Nature Communications*.
