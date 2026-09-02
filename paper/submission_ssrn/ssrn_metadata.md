# SSRN CompSciRN Submission Package & Metadata

## Paper Details

- **Title:** Critical Compositional Pressure: A Phase-Boundary Framework for Compositional Representation Formation in Neural Networks
- **Author:** Basyirin Amsyar Basri
- **Email:** basyirinbasri@gmail.com
- **Affiliation:** Independent Researcher, Kuala Lumpur, Malaysia
- **Date:** August 2026
- **Manuscript File:** `manuscript.pdf` (20 pages, LaTeX/TMLR preprint format)
- **Primary Classification:** Computer Science Research Network (CompSciRN)
  - Topic: Artificial Intelligence (CompSciRN: AI)
  - Topic: Machine Learning (CompSciRN: ML)
  - Topic: Neural & Evolutionary Computing
- **Secondary Classifications:**
  - Mathematics: Dynamical Systems & Bifurcation Theory
  - Cognitive Science: Computational Linguistics & Representation Learning

## Keywords

`compositional generalization`, `continuous gradient flow`, `phase transition`, `shortcut learning`, `transcritical bifurcation`

---

## SSRN Abstract (Extended Web Abstract)

Standard empirical risk minimization (ERM) in deep neural networks consistently defaults to brittle, memorized shortcuts ($E_S$) rather than systematic compositional rules, despite achieving near-zero training risk. We formulate the Two-Subspace Phase-Boundary Framework, establishing that the transition between shortcut entrapment and systematic compositional generalization is governed by an analytical transcritical bifurcation of continuous gradient flow. 

When structural compositional pressure $\lambda$ crosses the critical threshold:
$$\lambda_{\text{crit}} = \frac{b_C}{a_C} \iff R_0 = 1,$$
(formalized via the non-dimensional threshold ratio $R_0 = \lambda a_C / b_C = 1$), the shortcut equilibrium loses stability to a coherent representation attractor $E_C$. 

Across 960 multi-seed production runs (720 primary change-point runs and 240 architecture scaling runs) spanning four compositional benchmark suites ($\hbar$ Homomorphic Algebra, SCAN \texttt{jump}, COGS structural parsing, and PCFG-SET) and three architecture families (Transformer 2L, Transformer 4L, and recurrent GRU Seq2Seq), we empirically validate the theoretical law:

1. **Sharp Empirical Separatrix:** Non-linear change-point fitting reveals an exceptionally sharp empirical separatrix ($k \ge 79.5 \gg 15.0, R^2 \in [0.765, 0.887]$), providing strong evidence against smooth dose-response regularizers ($k < 5.0$).
2. **Primary Intent-to-Treat (ITT) Reporting:** At $\lambda = 0.025$, unconditional population OOD accuracy is $72.1\% \pm 10.1\%$ ($17/30 = 56.7\%$ escape fraction), while the conditional escaped sub-cohort saturates at $98.1\% \pm 0.4\%$, statistically equivalent to $\lambda = 0.500$ ($98.4\% \pm 0.3\%$, $\Delta \mu = 0.35\%$, TOST $p < 0.001$, margin $\delta = \pm 2.5\%$).
3. **Late-Onset Destabilization:** Supercritical pressure achieves $100\%$ ($30/30$) zero-shot recovery of deeply entrenched shortcut models at $t_{\text{int}} = 1000$ (exact Clopper-Pearson 95\% CI $[88.4\%, 100.0\%]$).
4. **Anti-Grokking Finite-Horizon Scoping:** Extended-horizon training for $20{,}000$ steps across weight decay regimes $\text{WD} \in \{0.0, 0.01, 0.10\}$ confirms that subcritical models remain stably arrested without spontaneous grokking within the evaluated finite horizon.
5. **Econometric VAR Precedence:** Augmented Dickey-Fuller stationarity confirmation and panel VAR econometric testing prove that internal representation alignment systematically leads behavioral out-of-distribution accuracy jumps ($\Delta t \approx 150$ steps, $F = 3.716, p < 0.01, \Delta R^2 = 0.184$).
6. **Cross-Benchmark & Architecture Universality:** The critical boundary $\hat{\lambda}_{\text{crit}} \in [0.0189, 0.0238]$ is invariant across synthetic algebraic grammars, natural language semantic parsing, capacity scaling, and recurrent inductive biases.
7. **Hessian Spectral Bounds:** Matrix-free Lanczos iterations show top Hessian eigenvalues strictly bounded deep below the Edge of Stability ceiling ($\lambda_{\text{max}} \le 0.002 \ll 2/\eta = 2000.0$), confirming stable continuous manifold reorganization.
---

## AI Disclosure

Large language models (Claude, Anthropic) were used as assistive grammar, style, and \LaTeX{} formatting tools under direct human author supervision. All scientific conceptions, mathematical theorems, experimental workflows, and interpretations were verified and authored by the human author.

---

## Submission Checklist for SSRN

1. [x] PDF rendered cleanly without undefined references or author placeholders (`manuscript.pdf`).
2. [x] Supplementary materials bundle (`supplementary_materials.zip`) generated with code, test suite, and processed results.
3. [x] SSRN CompSciRN subject areas selected.
4. [x] LLM writing assistance disclosed in paper footnote (`\thanks`) and abstract metadata.
5. [x] Open-source repository: \url{https://github.com/basyirin-dev/sigma-model} (Release \texttt{v2.0-paper02}, Commit \texttt{f9ba574}) and reproducibility bundle (\texttt{supplementary\_materials.zip}). A permanent Zenodo DOI will be minted concurrent with or prior to SSRN posting.
