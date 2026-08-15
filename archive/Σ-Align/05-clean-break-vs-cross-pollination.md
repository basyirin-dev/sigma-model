# 5. Clean Break vs. Cross-Pollination Analysis

## 5.1 The Question

The pivot from the original Σ-Model (protein domain architecture recombination) to AGI Safety raises the question: should the new direction be positioned as continuous with or separate from the original work?

Two levels of separation were considered:
1. **Scientific content:** Protein work vs. AGI safety
2. **Repository structure:** Single repo vs. separate repos

## 5.2 Clean Break (Decision)

**Decision: Clean break from the protein application, retain the formalism.**

| Factor | Clean Break | Cross-Pollination | Verdict |
|--------|:-----------|:------------------|:--------|
| **Scientific honesty** | Protein architectures and AGI safety are different domains. No natural bridge. | Risk of appearing to force an intellectual thread. Reviewers will see through it. | **Clean break** |
| **Paper identity** | Σ-Model paper lives or dies independently. | Tethering future papers creates dependency on the protein paper's fate. | **Clean break** |
| **Research brand** | Pivot signals deliberate redirection. | Claiming continuity creates confusion — biology lab or AI lab? | **Clean break** |
| **Publication strategy** | AGI safety papers target *Quantum*, *NeurIPS*, *JAIR*. Protein work targets computational biology. No overlap. | Forced explanation of protein work in every AGI paper wastes space. | **Clean break** |
| **Nobel trajectory** | CEV/alignment recognition comes from fundamental theorems. | Dilutes contribution purity. | **Clean break** |

## 5.3 What Is Retained

The **formal apparatus** of the Σ-Model is retained, not the application:

| Retained | Rationale |
|:---------|:----------|
| ODE framework ($\delta_A, \beta_A, \sigma_A, \alpha_A, \hat{M}_A, \Xi_A$) | General mathematical model of training dynamics |
| $\sigma$-trap discovery | Formally describes how SGD produces brittle, OOD-unreliable agents |
| Bifurcation analysis at $R_0 = 1$ | Threshold theorem structure applicable to alignment phase transitions |
| Five-phase training arc | Describes capability generalization vs. safety generalization |
| Cognitive faculty benchmarks | Directly maps to AGI evaluation and safety case frameworks |

## 5.4 Lineage Maintenance

The Σ-Model paper (under review, JAIR) is retained as **Paper 1** in the intellectual lineage. Every Σ-Align publication will cite it as the foundational formalism. This maintains scholarly provenance without requiring the protein application to be carried forward.

## 5.5 Repository Decision

A **new repository** will host Σ-Align work, with explicit documentation:

> "This project extends the Σ-Model formalism (DOI: 10.5281/zenodo.20714248) from its original application in protein domain architectures to AGI safety and alignment."

This provides:
- Clean narrative coherence for new readers
- Complete scholarly traceability via citation
- No dead code or unrelated artifacts
