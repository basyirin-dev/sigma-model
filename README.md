# The Σ-Model: A Dynamical Framework for Compositional Generalization

[![OpenReview Submission](https://img.shields.io/badge/OpenReview-TMLR%20Submission-blue)](https://openreview.net/forum?noteId=2ovjgUzk8N)
[![arXiv Preprint](https://img.shields.io/badge/arXiv-Preprint-B31B1B)](https://arxiv.org)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C.svg)](https://pytorch.org/)
[![Tests](https://img.shields.io/badge/Tests-Passing%20(14%2F14)-brightgreen.svg)](#testing)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Official research repository for the **Σ-Model** ("*The $\sigma$-Trap: A Dynamical Model of Schema-Coherence Suppression in Compositional Generalization*").

---

## 📌 Executive Summary

Neural sequence models trained to near-perfect in-distribution (ID) accuracy systematically suffer catastrophic failure on zero-shot out-of-distribution (OOD) compositional recombinations. While prevailing literature treats this failure as an optimization defect requiring adaptive curriculum scheduling, the **Σ-Model** demonstrates that compositional generalization is governed by a **macroscopic dynamical bifurcation**.

```
                ┌──────────────────────────────────────────────────────────┐
                │             The Σ-Model Dynamical State Space            │
                │                                                          │
                │  Parametric Depth (δ_A) ──> Specialized Task Mechanics   │
                │  Schema Coherence (σ_A) ──> Reusable Modular Structure   │
                └──────────────────────────────────────────────────────────┘
                                             │
             ┌───────────────────────────────┴───────────────────────────────┐
             ▼                                                               ▼
  Subcritical Regime (R₀ < 1)                                    Supercritical Regime (R₀ > 1)
  Standard ERM Training                                          Threshold Phase Transition
  ─────────────────────────────────                              ───────────────────────────────────
  • Network enters the σ-Trap (E_S).                              • E_S undergoes transcritical bifurcation.
  • Depth δ_A accumulates rapidly.                               • Stability exchanges to Coherent Basin (E_C).
  • Coherence σ_A is actively suppressed.                        • Coherence σ_A converges asymptotically.
  • Result: 98.7% ID / 34.7% OOD.                                • Result: 98.9% ID / 98.9% OOD.
  • Stable attractor (NO grokking).                              • Static supervision (λ=1.0) suffices!
```

### Key Theoretical & Empirical Findings
1. **The $\sigma$-Trap as a Stable Attractor ($E_S$):** 20,000-step extended-horizon training ($10\times$ standard duration, with and without weight decay) confirms that standard ERM does not spontaneously grok: training loss reaches 0.0186 and ID accuracy reaches 98.7%, while zero-shot OOD accuracy remains permanently arrested at 34.7%.
2. **The Threshold Law and Fixed-Weight Parity:** A static, non-adaptive fixed-weight compositional loss ($\lambda = 1.0$) achieves asymptotic recovery identical to complex adaptive curricula ($98.9 \pm 3.6\%$ vs. $98.9 \pm 2.4\%$, Welch $p = 0.99$, TOST-equivalent within $\pm 2.5\%$). Dynamic curriculum scheduling is unnecessary for asymptotic recovery once the threshold ratio $R_0 > 1$ is crossed.
3. **Dynamical Rate-Ordering:** The bifurcation geometry predicts the exact ordering of transition latencies across intervention regimes ($\hat{\tau}_{\text{fixed}} \approx 148 < \hat{\tau}_{\text{mult}} \approx 340 < \hat{\tau}_{\text{add}} \approx 542$ steps), confirming that scheduling modulates transient efficiency rather than asymptotic destination.
4. **Stage-1 Measurement Diagnostics:** Representational-Geometry Alignment (RGA, via CKA) robustly tracks internal schema emergence during training ($p = 0.005$).

---

## 📂 Repository Structure

```
sigma-model/
├── code/
│   ├── sigma_align/            # Core installable Python package
│   │   ├── ode/                # Dynamical ODE equations, Jacobian, and numerical solvers
│   │   ├── experiments/        # Transformer architectures, benchmark data generators, harnesses
│   │   ├── monitoring/         # Stage-1 online proxy estimation (GCA and RGA algorithms)
│   │   ├── config/             # YAML config loaders
│   │   └── utils/              # Metrics, dataset classes, and vocabulary utilities
│   └── experiments/            # Reproducibility runner scripts and configs
│       ├── configs/            # Experiment YAML configurations (gate, grokking, sweeps)
│       ├── generate_figures.py # One-click reproduction of publication figures
│       ├── analyze_gate.py     # Statistical analysis (Welch t-tests, TOST, regressions)
│       └── run_pilot.py        # Multi-seed experimental sweep harness
├── tests/                      # Automated unit test suite (ODE, grammar, proxies, models)
├── paper/                      # LaTeX source for primary manuscript & companion report
│   ├── manuscript.tex          # Primary TMLR manuscript (TMLR format)
│   ├── bibliography.bib        # Verified bibliography
│   ├── figures/                # Vector TikZ and publication figures
│   ├── companion/              # 24-page companion technical report (extended framework)
│   └── submission/             # Submission snapshot and supplementary ZIP bundles
├── docs/                       # Architecture Decision Records (ADRs) and notes
├── pyproject.toml              # Modern Python packaging configuration
├── Makefile                    # Developer workflow automation
└── README.md                   # Repository overview (this file)
```

---

## ⚡ Quickstart & Installation

### 1. Clone & Setup Environment
```bash
git clone https://github.com/basyirin-dev/sigma-model.git
cd sigma-model

# Create and activate virtual environment
python3 -m venv env
source env/bin/activate

# Install package in editable mode with development dependencies
pip install -e ".[dev]"
```

### 2. Verify Installation with Automated Tests
```bash
make test
# Runs 14 automated unit tests verifying ODE dynamics, grammar splits, proxies, and models
```

---

## 🔬 Reproducing Paper Results

### A. Run Automated Unit & Regression Tests
```bash
pytest -v tests/
```

### B. Regenerate Publication Figures
To regenerate Figures 11, 12, and 13 from the multi-seed raw evaluation data:
```bash
make figures
# Outputs:
# - paper/figures/figure11-gate-ood.png
# - paper/figures/figure12-gate-sigma.png
# - paper/figures/figure13-gate-inflection.png
```

### C. Run Statistical Analysis & Equivalence Tests
To compute the Welch $t$-tests, Two-One-Sided Tests (TOST $\pm 2.5\%$), and segmented regression inflection latencies:
```bash
python code/experiments/analyze_gate.py --results-dir paper/submission/supplementary/data/gate-results
```

### D. Compile Manuscripts & Submissions
```bash
# Build the primary double-blind manuscript PDF
make paper

# Build the companion technical report PDF
make companion

# Package the arXiv submission bundle
make arxiv
```

---

## 📄 Publications & Deliverables

1. **Primary Manuscript (Under Review at TMLR):**  
   *Compositional Generalization as a Threshold Phase Transition: Why Adaptive Curricula are Unnecessary for Asymptotic Recovery*  
   [OpenReview Forum `2ovjgUzk8N`](https://openreview.net/forum?noteId=2ovjgUzk8N) | [`paper/submission/manuscript.pdf`](paper/submission/manuscript.pdf)

2. **Companion Technical Report:**  
   *The Σ-Model: Extended Dynamical Framework for Compositional Generalization*  
   [`paper/companion/companion.pdf`](paper/companion/companion.pdf)

---

## 📑 Citation

If you build upon this work or use the Σ-Model framework in your research, please cite:

```bibtex
@article{basri2026sigmatrap,
  title   = {Compositional Generalization as a Threshold Phase Transition: Why Adaptive Curricula are Unnecessary for Asymptotic Recovery},
  author  = {Basri, Basyirin Amsyar},
  journal = {Transactions on Machine Learning Research (Under Review)},
  year    = {2026},
  url     = {https://openreview.net/forum?noteId=2ovjgUzk8N}
}

@techreport{basri2026sigmamodelcompanion,
  title       = {The {$\Sigma$}-Model: Extended Dynamical Framework for Compositional Generalization},
  author      = {Basri, Basyirin Amsyar},
  institution = {Universiti Malaya},
  year        = {2026},
  note        = {Complementary Companion Technical Report}
}
```

---

## 📜 License

- **Code:** Licensed under the [MIT License](LICENSE).
- **Data & Documentation:** Licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
