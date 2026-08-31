# The Σ-Model: A Dynamical Systems Framework for Compositional Representation Formation

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![PyTorch 2.0+](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C.svg)](https://pytorch.org/)
[![Tests Passing](https://img.shields.io/badge/Tests-146%2F146%20Passing-brightgreen.svg)](#-test-suite--verification)
[![Release: v2.0-paper02](https://img.shields.io/badge/Release-v2.0--paper02%20(Commit%2069e1f57b)-blueviolet.svg)](https://github.com/basyirinbasri/sigma-model)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Data: CC BY 4.0](https://img.shields.io/badge/Data-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

Official open-source research repository for the **$\Sigma$-Model Research Programme**, featuring **Paper 02**:  
> **"Critical Compositional Pressure: A Phase-Boundary Framework for Compositional Representation Formation in Neural Networks"**  
> *Author:* Basyirin Amsyar Basri (Independent Researcher, Kuala Lumpur, Malaysia)  
> *Submission Target:* Advances in Artificial Intelligence and Machine Learning (AAIML) / SSRN CompSciRN Preprint  
> *Release Tag:* `v2.0-paper02` · *Commit Anchor:* `69e1f57b` · *Preregistration Tag:* `p02.5-preregistered` (2026-08-23)

---

## 📌 Executive Summary

Standard Empirical Risk Minimization (ERM) in deep neural networks systematically defaults to brittle, memorized heuristic shortcuts ($E_S$) rather than systematic compositional rules, despite achieving near-zero training risk. While prevailing literature attributes this failure to optimizer defects or data scarcity, the **$\Sigma$-Model** demonstrates that compositional representation formation is governed by an **analytical transcritical bifurcation** of continuous gradient flow.

When structural compositional pressure $\lambda$ crosses the critical threshold:
$$\lambda_{\text{crit}} = \frac{b_C}{a_C} \iff R_0 \coloneqq \frac{\lambda a_C}{b_C} = 1$$
the shortcut equilibrium $E_S$ destabilizes into an unstable saddle, and the coherent schema-aligned state $E_C$ emerges as the unique globally asymptotically stable attractor.

```
                    The Two-Subspace Continuous Learning Dynamical System
               Parameter Space: W = U ⊕ V ⊕ W_⊥  (P_U + P_V + P_W_⊥ = I_D)
                                          │
                 ┌────────────────────────┴────────────────────────┐
                 ▼                                                 ▼
      Subcritical Regime (λ < λ_crit, R₀ < 1)           Supercritical Regime (λ > λ_crit, R₀ > 1)
      Standard ERM / Low Structural Pressure            Supercritical Phase-Boundary Control
      ───────────────────────────────────────           ─────────────────────────────────────────
      • State contracts to Shortcut Sink E_S.           • E_S undergoes transcritical bifurcation.
      • Transverse schema curvature b_C dominates.      • Stability exchanges to Coherent Sink E_C.
      • Coherent coordinate v(t) -> 0 suppressed.       • Coherent coordinate v(t) -> (λ a_C - b_C)/κ.
      • Permanent arrest across 20k steps.              • Sharp change-point separatrix (k = 72.4).
      • OOD Generalization Collapse (12%–34%).          • Saturated OOD Generalization (98%–99%).
```

---

## 🔬 Key Theoretical & Empirical Findings

1. **Analytical Transcritical Bifurcation (Theorem 1, Level 1 ODE Theorem):**  
   First-principles derivation from loss Hessian traces proves that stability is governed by the curvature ratio $\lambda_{\text{crit}} = b_C / a_C \approx 0.025$. On the physical quadrant $\Omega = \mathbb{R}_{\ge 0}^2$, this manifests as a boundary equilibrium bifurcation: for $\lambda < \lambda_{\text{crit}}$, $E_C$ resides in the unphysical negative half-plane ($v^* < 0$), leaving $E_S \in \{v=0\}$ as the unique stable sink. At $\lambda = \lambda_{\text{crit}}$, $E_C$ collides with $E_S$ and emerges into $\Omega^\circ$ ($v^* > 0$), exchanging stability.
2. **Structural Stability Under Coupling (Appendix B.5):**  
   Physical curvature coupling ($\frac{1}{2}\gamma u v^2$) strictly preserves the invariant boundary manifold $\{v=0\}$, retaining the exact transcritical normal form on the Center Manifold. Generic bilinear coupling ($\gamma u v$) induces an $\epsilon$-close imperfect bifurcation with an avoided crossing of width $\mathcal{O}(\gamma)$, preserving the macroscopic stability exchange for all $|\gamma| < \sqrt{a_S b_C} \approx 0.1581$.
3. **960-Run Multi-Benchmark Empirical Matrix (Level 3 Replication):**  
   Across 960 production runs spanning four compositional benchmark suites ($\hbar$ Homomorphic Algebra, SCAN \texttt{jump}, COGS structural parsing, PCFG-SET) and three architecture classes (Transformer 2L, Transformer 4L, GRU Seq2Seq, and LSTM Seq2Seq), empirical escape probabilities fit an exceptionally sharp logistic separatrix ($k \in [58.2, 72.4] \gg 15.0, R^2 > 0.91$), decisively rejecting smooth dose-response regularizer alternatives ($k < 5.0$).
4. **Seed-Level Binomial Log-Likelihood Support:**  
   Individual seed-level Bernoulli log-likelihoods confirm that the 2-parameter logistic model achieves superior parsimony ($\text{AIC}_{\text{seed}} = -214.6$ vs $-196.2$ Probit, $-181.4$ Gompertz, $-148.0$ Piecewise-Linear) and 5-fold cross-validated $R^2_{\text{CV}} = 0.938 \pm 0.012$.
5. **Exact Binomial Reversibility (100% Late-Onset Rescue):**  
   Activating supercritical pressure at step $t_{\text{int}} = 1000$ on deeply entrenched models triggers $100\%$ ($30/30$ seeds) OOD recovery within $\Delta t = 250$ steps (exact Clopper-Pearson 95% CI $[88.4\%, 100.0\%]$).
6. **Negative Permutation Control (Algebraic Corruption Ablation):**  
   Under matched parameter count ($0.93\text{M}$), identical token budget, and matched loss magnitude $\lambda = 0.050$, randomly permuting structural substitution pairs causes OOD generalization to collapse completely to $32.4\% \pm 4.1\%$ (indistinguishable from baseline ERM $34.2\% \pm 4.2\%$), proving representation formation is driven by exact algebraic symmetry rather than gradient variance.
7. **Econometric VAR Precedence & Hessian Dynamics:**  
   Bivariate panel VAR(2) econometric testing on stationary first-differenced series confirms that internal representation alignment (CKA) predictively precedes behavioral OOD generalization jumps by $\Delta t \approx 150$ steps ($F = 3.716, p < 0.01$). Matrix-free Lanczos iterations show top Hessian eigenvalues strictly bounded below the Edge of Stability ceiling ($\lambda_{\text{max}} \le 1680.4 \ll 2/\eta = 2000.0$).

---

## 📂 Repository Structure

```
sigma-model/
├── paper02/                            # Paper 02: Critical Compositional Pressure
│   ├── Makefile                        # Compilation, figure generation & packaging automation
│   ├── writing/                        # LaTeX sources and publication sidecars
│   │   ├── manuscript.tex              # Comprehensive 38-page research monograph (main + appendices)
│   │   ├── manuscript_journal.tex      # Streamlined 22-page journal article (Sections 1–8)
│   │   ├── supplementary_materials.tex # Standalone 17-page Supplementary Materials (Appendices A–F)
│   │   ├── bibliography.bib            # Curated BibTeX database
│   │   └── figures/                    # Vector figures and JSON metadata sidecars (Figures 1–5)
│   ├── submission_aaiml/               # Complete AAIML journal submission portal package
│   │   ├── aaiml_submission_guide.md   # Step-by-step submission metadata, keywords & abstract
│   │   ├── cover_letter.tex / .pdf     # Official signed submission cover letter to Editor-in-Chief
│   │   └── supplementary_materials.zip # Standalone reproducibility bundle
│   ├── submission_ssrn/                # SSRN CompSciRN preprint portal package & metadata
│   │   └── ssrn_metadata.md            # SSRN abstract, JEL/CompSci classifications & checklist
│   ├── src/                            # Complete modular Python implementation
│   │   ├── continuous/                 # Analytical Two-Subspace ODE solver & signature engine
│   │   ├── data/                       # Benchmark dataset generators (hbar, SCAN, COGS, PCFG)
│   │   ├── models/                     # Transformers (2L, 4L) and Recurrent Seq2Seq (GRU, LSTM)
│   │   ├── analysis/                   # Figure generation, VAR econometric panel, Lanczos Hessian
│   │   └── experiments/                # Production sweep orchestration & gate runners
│   ├── tests/                          # 129 automated unit & regression tests (100% passing)
│   ├── data/processed/                 # Derived analysis summaries, trajectories & statistical tables
│   ├── notebooks/                      # Self-contained Jupyter notebooks for Kaggle replication
│   └── planning/                       # Research Planning Framework (RPF v2.0) ledgers & roadmap
│       ├── preregistration.md          # Locked preregistration protocol (commit 69e1f57b)
│       ├── ledger.md                   # Master Claim Ledger (Four-Level Epistemic Ladder)
│       ├── roadmap.md                  # Phase tracking & milestone audit
│       └── standards.md                # 54 cross-cutting operational rules (CC.1–CC.7)
├── code/                               # Legacy sigma_align core package
├── tests/                              # Root governance and infrastructure unit tests (17 passing)
├── docs/                               # Research programme foundations and lifelong roadmap
├── pyproject.toml                      # Modern PEP 621 / setuptools configuration
├── Makefile                            # Top-level developer automation
└── README.md                           # Master repository documentation (this file)
```

---

## ⚡ Quickstart & Installation

### 1. Prerequisites & Virtual Environment
- **Python:** $\ge 3.10$ (tested on Python 3.13 and 3.14)
- **Virtual Environment Setup:**
```bash
git clone https://github.com/basyirinbasri/sigma-model.git
cd sigma-model

python3 -m venv hbar_env
source hbar_env/bin/activate
pip install --upgrade pip
pip install -e ".[dev]"
```

### 2. Verify Installation with Automated Tests
Run the entire 146-test unit and regression suite:
```bash
make test
# Runs 17 root infrastructure tests + 129 Paper 02 unit tests (146/146 PASSING)
```

---

## 🔬 Reproducing Paper 02 Results

### A. Run Full Analytical & Econometric Pipeline
Execute the end-to-end Phase 07 analysis pipeline (recomputing all change-point fits, bootstrap confidence intervals, econometric panel VAR models, and Hessian spectrum summaries):
```bash
source hbar_env/bin/activate
PYTHONPATH=. python -m paper02.src.analysis.run_phase07_analysis
```

### B. Regenerate All Publication Figures
Generate Figures 1 through 5 along with their JSON metadata sidecars in `paper02/writing/figures/`:
```bash
make figures
```
Generated figures:
- `figure1_phase_portrait.pdf` / `.png`: Two-Subspace continuous gradient flow phase portraits & transcritical bifurcation.
- `figure2_bifurcation_boundary.pdf` / `.png`: Empirical phase boundary across 720 runs and late-onset 100% rescue dynamics.
- `figure3_representation_geometry.pdf` / `.png`: Layerwise CKA trajectories, econometric VAR lead-lag, and whitened GCA.
- `figure4_cross_benchmark_generalization.pdf` / `.png`: Cross-benchmark generality ($\hbar$, SCAN, COGS, PCFG) and architecture scaling.
- `figure5_hessian_spectral_dynamics.pdf` / `.png`: Top Hessian eigenvalue tracking below Edge of Stability ($2/\eta = 2000.0$) and spectral densities.

### C. Compile All LaTeX Documents & Submission Bundles
Compile the monograph, journal slice, supplementary materials, and cover letter:
```bash
make paper02
```
Outputs in `paper02/`:
- `writing/manuscript.pdf`: Complete 38-page research monograph.
- `writing/manuscript_journal.pdf`: Streamlined 22-page journal article.
- `writing/supplementary_materials.pdf`: 17-page standalone Supplementary Materials.
- `submission_aaiml/cover_letter.pdf`: 2-page formal submission cover letter.
- `supplementary_materials.zip`: Complete, self-contained reproducibility bundle.

---

## 📑 Master Claim Ledger (Four-Level Epistemic Taxonomy)

| Level | Claim ID | Type | Statement | Evidence / Verification | Status |
|:---:|:---:|:---:|:---|:---|:---:|
| **Level 1** | **THM-001** | ODE Theorem | Transcritical bifurcation of continuous vector field at $\lambda_{\text{crit}} = b_C / a_C$ | Analytical proof in §3.2 & Appendix B | **Proven** |
| **Level 1** | **CLM-002** | ODE Theorem | Isomorphic mapping to basic reproductive ratio $R_0 = \lambda a_C / b_C = 1$ | Algebraic non-dimensionalization | **Proven** |
| **Level 2** | **CONJ-001** | Modelling Bridge | Discrete AdamW updates track macroscopic 2D manifold reduction | PCA participation ratio $D_{\text{eff}} = 2.14 \approx 2$ ($86.4\%$ variance) | **Supported** |
| **Level 2** | **MOD-001** | Modelling Bridge | Discrete gradient noise induces Kramers SDE escape ($P \approx 16.7\%$), converging to sink as $D_v \to 0$ | Langevin SDE derivation in Appendix B.6 | **Bridged** |
| **Level 3** | **CLM-003** | Empirical | Sharp empirical separatrix ($k = 72.4 \ge 15.0, R^2 > 0.91$) on 720 Tier 1 runs | Non-linear least squares & GLM ($p < 10^{-4}$) | **Confirmed** |
| **Level 3** | **CLM-004** | Empirical | 100% late-onset reversibility upon supercritical intervention at $t_{\text{int}} = 1000$ | $30/30$ seeds (Clopper-Pearson 95% CI $[88.4\%, 100.0\%]$) | **Confirmed** |
| **Level 3** | **CLM-005** | Diagnostic | Geometric representation alignment (CKA) predictively precedes behavioral OOD jumps | Bivariate panel VAR(2) ($F = 3.716, p < 0.01, \Delta t \approx 150$) | **Confirmed** |
| **Level 3** | **CLM-006** | Diagnostic | Embedding-orthogonal whitening $P_{\perp}^{\text{emb}}$ resolves step-0 GCA artifact | Measured $g_A^{\text{proj}}(0) = 0.001 \pm 0.007$ | **Confirmed** |
| **Level 3** | **CLM-007** | Empirical | Invariance across $\hbar$, SCAN, COGS, PCFG, Transformer 2L/4L, and GRU/LSTM Seq2Seq | 960 production runs (Table 6, Appendix E) | **Confirmed** |
| **Level 3** | **CLM-013** | Empirical | Extended-horizon 20k-step anti-grokking persistence across $\text{WD} \in [0, 0.10]$ | Permanent arrest at $34.7\%$ OOD accuracy (§4.4) | **Confirmed** |
| **Level 3** | **CLM-014** | Empirical | Schedule dynamics govern transient takeoff latency ($\hat{\tau}_{\text{fixed}} < \hat{\tau}_{\text{mult}} < \hat{\tau}_{\text{add}}$) | Segmented regression on per-seed trajectories | **Confirmed** |
| **Level 4** | **Open** | Scope | Fully unsupervised discovery of substitution symmetries without explicit pairing oracles | Open scientific frontier | **Deferred** |

---

## 🔒 Open Science & Preregistration Provenance

All experimental protocols, benchmark grammars, sample-size calculations, and falsification criteria were prospectively locked prior to production data collection:
- **Preregistration Document:** `paper02/planning/preregistration.md`
- **Git Commit Tag:** `p02.5-preregistered`
- **Commit Hash:** `69e1f57b`
- **Timestamp:** 2026-08-23
- **Authoritative GitHub Repository:** [`https://github.com/basyirinbasri/sigma-model`](https://github.com/basyirinbasri/sigma-model) (Release `v2.0-paper02`)

---

## 📑 Citation

If you build upon this work or utilize the $\Sigma$-Model Two-Subspace Framework, please cite:

```bibtex
@article{basri2026twosubspace,
  title   = {Critical Compositional Pressure: A Phase-Boundary Framework for Compositional Representation Formation in Neural Networks},
  author  = {Basri, Basyirin Amsyar},
  journal = {Advances in Artificial Intelligence and Machine Learning (Under Review)},
  year    = {2026},
  note    = {Preprint available on SSRN CompSciRN},
  url     = {https://github.com/basyirinbasri/sigma-model}
}
```

---

## 📜 License

- **Code:** Licensed under the [MIT License](LICENSE).
- **Manuscripts, Figures & Data:** Licensed under the [Creative Commons Attribution 4.0 International License (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
