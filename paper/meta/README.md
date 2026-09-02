# Paper 02 — Project Overview & Metadata

**Title:** Critical Compositional Pressure: A Phase-Boundary Law for Neural Representation Formation  
**Working Package:** `paper`  
**Parent Framework:** $\Sigma$-Model Programme  
**Methodology:** The Research Planning Framework (RPF v1.0.0)  

---

## 1. Executive Summary
Paper 02 establishes the **Two-Subspace Law of Critical Compositional Pressure**, deriving the exact threshold $\lambda_{\text{crit}} = b_C / a_C \iff R_0 = 1$ from continuous gradient flow and experimentally validating the existence of a sharp supercritical separatrix in deep Transformer architectures.

---

## 2. Canonical Directory Map

```
paper/
├── planning/                   # RPF Roadmap, standards, claims ledger, and phase documents
│   ├── roadmap.md              # Temporal spine & non-negotiables
│   ├── standards.md            # Cross-cutting CC.N.M rules & compliance matrix
│   ├── ledger.md               # Scope inventory & claim tracking
│   └── phases/                 # P00 through P12 phase execution briefs
├── decisions/                  # Architecture Decision Records (ADRs)
│   ├── ADR-template.md         # Template for all architectural records
│   └── ADR-001_...             # Two-subspace continuous gradient flow record
├── src/                        # Modular package implementations
│   ├── continuous/             # Differentiable ODE / gradient flow integration
│   ├── models/                 # Neural architectures & subspace bottlenecks
│   ├── data/                   # Synthetic compositionality dataset splits
│   └── analysis/               # Subspace CKA, principal angles, Hessian spectrum
├── experiments/                # Orchestration configurations & literature sweeps
│   ├── configs/                # YAML sweep parameter files
│   └── literature/             # Baseline comparisons (grokking, standard SGD)
├── notebooks/                  # Interactive exploratory notebooks & diagnostic visualizers
├── data/                       # Experimental data tiers
│   ├── raw/                    # Immutable raw tensor outputs (ignored by git)
│   └── processed/              # Tidy benchmark parquet/csv files
├── writing/                    # LaTeX manuscript, figures, and supplementary materials
│   ├── figures/                # Vector PDF/SVG and TikZ diagrams
│   └── supplementary/          # Proof reconstructions and ablation tables
├── tests/                      # Automated smoke tests and numerical kernel unit tests
└── meta/                       # Agent operating manual & environment pinning
```

---

## 3. Quick Commands

```bash
# Activate virtual environment
source hbar_env/bin/activate

# Run Paper 02 Automated Unit & Smoke Tests
make -C paper test

# Build Paper 02 Manuscript PDF (Phase 08+)
make -C paper pdf

# Package arXiv Submission Bundle (Phase 11+)
make -C paper arxiv

# Run Ruff Linter across Paper 02
ruff check paper/src/ paper/tests/
```

