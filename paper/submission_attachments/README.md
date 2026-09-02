# Paper 02 Submission Attachments & Turnkey Replication Guide

**Title:** Critical Compositional Pressure: A Phase-Boundary Framework for Compositional Representation Formation in Neural Networks  
**Author:** Basyirin Amsyar Basri  
**Repository Anchor:** `v2.0-paper02` (`f9ba574`)

---

## 1. Directory Manifest & Cryptographic SHA-256 Checksums (Submission Deliverables & Artifacts)

This directory contains the primary submission deliverables and self-contained artifacts for the defining paper, including the comprehensive master monograph PDF, journal main body PDF, supplementary materials annex PDF, submission archives, primary configuration and pre-registration manifests, reproducibility dossiers, and master processed data tables.

| File Name | SHA-256 Checksum | Size | Description |
|---|---|---|---|
| `manuscript.pdf` | `4852667fb33721430698c4b145798875a423ca27c55c913a2c66ebf97cd3584a` | 1076.8 KB | **Comprehensive Master Monograph**: Full TMLR-formatted master deliverable (Main Body + Appendices A–F, proofs, and figures). |
| `manuscript_journal.pdf` | `e36457c30fb7579d872a886a3486ed9a580d9f07a7106448810c0cfd34a3b3b0` | 844.0 KB | **Journal Main Manuscript**: Streamlined 27-page AAIML journal format covering core theoretical foundations and empirical validation. |
| `supplementary_materials.pdf` | `dab8ca4b1c5c20538dc11da473ca44d5372a101db4720fa797ee5b1b466decb1` | 718.2 KB | **Supplementary Materials Annex**: Self-contained 19-page annex containing full mathematical proofs, dataset formalizations, and econometric tables. |
| `arxiv_bundle.tar.gz` | `2966fd1b22fbfbf37ad0d1664592e0766f515bfd5f57ac67da05fb5418d3f3ad` | 243.7 KB | **arXiv Submission Package**: Complete turnkey source bundle (LaTeX source, flattened bibliography `.bbl`, style files, and vector figures). |
| `supplementary_materials.zip` | `a5cca5923ad527c255a5d08acba5f22a6ad9293b549acf43786f8a3c28faa636` | 3977.4 KB | **Standalone Reproducibility Archive**: Complete standalone package containing all source code (`src/`), unit/leakage tests (`tests/`), all 17 processed CSV tables (`data/processed/`), and vector figures. |
| `run-log.csv` | `cefd63bb945b23675d2c57baade225fb22f2cec49bc0ab858e58ead40f76faf8` | 190.3 KB | **Master Run Log**: Complete 960-run production execution log across 4 benchmarks and 3 architectures, including explicit `split` metadata and baseline GCA. |
| `ood_summary_table.csv` | `838e5ee9c9dea69f0c3c4f19dd56bc59ff2a1dbaf54dca58c1e8da4579831769` | 9.2 KB | **Canonical OOD Summary Table**: Summary metrics and 95% confidence intervals across all benchmark $\times$ architecture $\times$ $\lambda$ conditions. |
| `dense_grid_330_runs.csv` | `77e2159c234a305f544980786713fe9c1ee1a105d44d398f7d7c0635f86b44c2` | 52.7 KB | **Dense Grid Dataset**: Complete 330 evaluations on $\hbar$ across 11 dense levels integrating primary runs and calibrated boundary refinements. |
| `inflection_breakpoints.csv` | `fe1ef4f502bfe2cc0ea39451a6c58cc1e0e2e75738cb6647bba9eb21bdd1100d` | 0.9 KB | **Inflection Breakpoints**: Fitted non-linear logistic separatrix parameters, steepness $k \ge 15.0$, and $R^2$ goodness-of-fit scores. |
| `matrix_p04.yaml` | `be06bc8c1c870592d34fefeedc61ac430bf66d36593cfd980a1aa2224f19ce80` | 4.7 KB | **Experimental Matrix Configuration**: Full factorial specification of architecture parameters, benchmark splits, training schedules, and evaluation grids. |
| `preregistration.md` | `de78319639fb85f412572666068effd2bb8706e3dd5004fb3b94cb8ca2548140` | 10.6 KB | **Preregistration Protocol**: Prospective evaluation protocol locked prior to Phase 06 production runs (RPF v2.0). |
| `TIER0_AUDIT_REPRODUCIBILITY_DOSSIER.md` | `078d6dfb34fac36fe43c5201acd32b287a4016f8a35fb82f38b1623122df1170` | 38.0 KB | **Audit & Reproducibility Dossier**: Epistemic claim hierarchy, oracle boundary disclosures, and mathematical/econometric toolchain mapping. |
| `README.md` | `*` | 7.5 KB | **Manifest & Guide**: Directory index, cryptographic checksums, schema definitions, and turnkey replication guide. |
*(Note: Additional granular CSV trajectory and falsification tables—including `cka_trajectories.csv`, `pairwise_welch_tost.csv`, `granger_causality_results.csv`, `hessian_spectral_summary.csv`, `late_onset_recovery_trajectories.csv`, `anti_grokking_extended_runs.csv`, `threshold_sensitivity_grid.csv`, `model_selection_comparison.csv`, `data_augmentation_baseline.csv`, `permutation_control_runs.csv`, `pairing_noise_robustness.csv`, `falsification_controls_summary.csv`, `theoretical_separatrix.csv`, `escaped_subcohort_tost.csv`, and `dimensionality_concentration.csv`—as well as `seeds.yaml` are packaged within `supplementary_materials.zip` and versioned in `paper/data/processed/`.)*

---

## 2. Master Run Log Column Definitions (`run-log.csv`)

The master run log contains 960 rows formatted according to the unified schema:

1. `run_id`: Unique 1-indexed execution identifier ($1 \dots 960$).
2. `cell_seed_idx`: Zero-indexed seed index within the specific experimental condition cell ($0 \dots 29$ for Tier 1, $0 \dots 9$ for Tier 2).
3. `tier`: Experimental tier identifier (`tier_1_primary_change_point` or `tier_2_exploratory_scaling`).
4. `evidence_class`: Methodological evidence category (`primary` or `exploratory`).
5. `benchmark`: Compositional benchmark suite (`hbar`, `scan_jump`, `cogs`, `pcfg_set`).
6. `split`: Exact benchmark evaluation split:
   - `hbar`: `split_b_recursion_depth` (hierarchical depth $d \in \{4, 5\}$ extrapolation)
   - `scan_jump`: `add_primitive_jump` (Lake & Baroni primitive zero-shot extrapolation)
   - `cogs`: `structural_recursion` (Kim & Linzen structural syntactic recursion)
   - `pcfg_set`: `systematicity` (Hupkes et al. Cartesian systematic substitution)
7. `arch`: Neural architecture:
   - `transformer_2l`: Canonical baseline ($0.93\text{M}$ parameters, $d_{\text{model}}=128, d_{\text{ff}}=512, n_{\text{heads}}=4, 2 \text{ enc} + 2 \text{ dec layers}$).
   - `transformer_4l_scaled`: Deep capacity scaling ($3.80\text{M}$ parameters, $d_{\text{model}}=256, d_{\text{ff}}=1024, n_{\text{heads}}=8, 2 \text{ enc} + 2 \text{ dec layers}$).
   - `gru_baseline`: Recurrent Seq2Seq ($0.41\text{M}$ parameters, $d_{\text{model}}=128, d_{\text{hidden}}=128, 2 \text{ layers}$).
8. `lambda`: Compositional regularizer weight ($\lambda \in [0.000, 0.500]$).
9. `lambda_regime`: Theoretical regime classification (`subcritical`, `boundary`, `supercritical`).
10. `seed`: Global random seed (`seed = cell_seed_idx * 42 + 7`).
11. `final_id_acc`: In-distribution validation accuracy percentage ($\%$).
12. `final_ood_acc`: Out-of-distribution evaluation accuracy percentage ($\%$).
13. `mean_whitened_gca`: Mean Whitened Gradient Cosine Alignment diagnostic across training ($g_A^{\text{proj}}(t)$), with baseline orthogonal probe alignment $0.001$ at $\lambda = 0.0$ (eliminating the unwhitened $1.0$ artifact).
14. `top_hessian_eig`: Top Hessian eigenvalue $\lambda_{\text{max}}(H_t)$ computed via matrix-free Lanczos iterations.
15. `wall_clock_sec`: Total training execution wall-clock time in seconds.
16. `status`: Execution completion and convergence status (`PASS`).

---

## 3. Turnkey Replication & Environment Setup

### Prerequisites
- Python $\ge 3.10$ (validated on Python 3.13.9)
- PyTorch $\ge 2.0.0$ (validated on PyTorch 2.12.0)
- CUDA $\ge 12.0$ (optional; CPU execution fully supported)

### Quick Start
```bash
# 1. Clone repository and enter directory
git clone https://github.com/basyirin-dev/sigma-model.git
cd sigma-model

# 2. Activate virtual environment
source hbar_env/bin/activate

# 3. Verify test suite (147 tests)
PYTHONPATH=.:code:paper02/src pytest -q paper02/tests/ tests/

# 4. Re-derive all processed tables from raw production records
python -m paper02.src.data.derive_processed_tables

# 5. Compile full PDF manuscript suite
make paper02
```
