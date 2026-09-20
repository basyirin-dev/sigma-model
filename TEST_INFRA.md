# Phase 0 E2E Test Infrastructure & Verification Architecture

## 1. Testing Philosophy

The test suite for Phase 0 manuscript remediation adheres to a strict **requirement-driven, opaque-box testing methodology**. Rather than testing internal code paths or implementation quirks, all tests are derived directly from:
1. **Mathematical derivations and theorems** established in `ORIGINAL_REQUEST.md`.
2. **Exhaustive defect audits** in `.agents/PEER_REVIEW.md` §7.2 (Items 1–17).
3. **Cryptographically frozen ground-truth data**: `paper/experiments/run-log.csv` (960 MECE production runs) and `paper/submission_attachments/dense_grid_330_runs.csv` (330 dense grid runs on $\hbar$).

### Core Testing Invariants
- **Zero-Facade Policy**: No test may pass trivially or assert tautologies. Every assertion exercises empirical data, closed-form mathematical equations, or physical file artifacts.
- **Explicit Authoritative Oracles**:
  - Information criteria: exact $2k - 2\ln\mathcal{L}$ for Bernoulli seed MLE, with ceiling $\log\mathcal{L} \le \log\mathcal{L}_{\text{sat}} = -165.234$.
  - Mixture variance: $s^2_{\text{total}} = s^2_{\text{within}} + s^2_{\text{between}} = [p s_1^2 + (1-p) s_0^2] + p(1-p)(\mu_1 - \mu_0)^2$.
  - Participation ratio: $D_{\text{eff}} = 1/\sum p_i^2 \ge 2.29$ for $p_1=0.582, p_2=0.282, \sum_{i\ge 3} p_i = 0.136$.
  - Welch $t$-test: unpooled variance with Satterthwaite-Welch degrees of freedom.
  - Parameter counts: analytical PyTorch recurrent parameter formulas.
- **State Isolation & Reproducibility**: Tests are completely idempotent, create isolated temp directories when writing outputs, and avoid mutating source code or raw data files.

---

## 2. Test Architecture & Tier Hierarchy

The test suite is organized into four hierarchical verification tiers in `paper/tests/test_phase0_e2e_requirements.py`:

```
paper/tests/test_phase0_e2e_requirements.py
├── Tier 1: Feature Coverage (>= 5 tests per feature requirement)
│   ├── TestR1NumericalAndStatisticalAudit
│   │   ├── test_saturated_log_likelihood_ceiling
│   │   ├── test_bernoulli_mle_information_criteria_ranking
│   │   ├── test_itt_mixture_variance_decomposition
│   │   ├── test_welch_t_test_permutation_control
│   │   ├── test_granger_causality_degrees_of_freedom
│   │   └── test_hbar_baseline_standardization
│   ├── TestR2TheoreticalConsistencyAndKramers
│   │   ├── test_kramers_barrier_excised_from_manuscript
│   │   ├── test_potential_energy_monotonicity_on_physical_domain
│   │   ├── test_transcritical_bifurcation_fixed_point_scaling
│   │   ├── test_deterministic_subcritical_absorption
│   │   └── test_subcritical_escape_reframed_as_finite_sample_fluctuations
│   ├── TestR3TurnkeyTableRegeneration
│   │   ├── test_all_17_processed_csv_tables_exist
│   │   ├── test_raw_run_log_mece_structure
│   │   ├── test_dense_grid_330_runs_structure
│   │   ├── test_table_derivation_idempotence
│   │   └── test_csv_tables_non_empty_and_valid_schemas
│   └── TestR4ManuscriptBibliographyAndBuild
│   │   ├── test_gru_parameter_count_unidirectional
│   │   ├── test_participation_ratio_mathematical_bound
│   │   ├── test_bibliography_citation_keys_and_attributions
│   │   ├── test_repository_urls_canonical
│   │   └── test_latex_compilation_cleanliness
│
├── Tier 2: Boundary & Corner Cases (>= 5 tests per feature domain)
│   ├── test_participation_ratio_single_component_extremum
│   ├── test_participation_ratio_uniform_residual_spread
│   ├── test_piecewise_linear_hard_clipping_penalty
│   ├── test_discrete_grid_saturation_k300
│   ├── test_bimodal_mixture_variance_extreme_splits
│   └── test_clopper_pearson_exact_binomial_confidence_intervals
│
├── Tier 3: Cross-Feature Combinations (Pairwise Consistency)
│   ├── test_raw_log_to_derived_csv_to_latex_consistency
│   ├── test_cross_benchmark_baseline_harmony_table2_table4
│   ├── test_run_accounting_hierarchy_alignment_table7
│   ├── test_granger_causality_panel_to_test_statistic
│   └── test_architecture_c_gru_specs_across_configs_and_manuscript
│
└── Tier 4: Real-World Application Scenarios (>= 5 Realistic Scenarios)
    ├── test_scenario_full_end_to_end_table_regeneration
    ├── test_scenario_turnkey_audit_script_execution
    ├── test_scenario_latex_build_zero_errors_and_zero_undefined_refs
    ├── test_scenario_submission_bundles_synchronization
    └── test_scenario_continuous_ode_vs_empirical_transition
```

---

## 3. Detailed Requirement Mapping & Oracles

| Requirement | Test Class / Method | Authoritative Oracle & Source | Acceptance Threshold |
|:---|:---|:---|:---|
| **R1.1 Info Criteria** | `test_bernoulli_mle_information_criteria_ranking` | Seed Bernoulli MLE on 330 dense grid runs: $\log\mathcal{L} = \sum [S_j \ln p_j + (N-S_j)\ln(1-p_j)]$ | $\log\mathcal{L} \le -165.234$; $\Delta\text{AIC} < 0.3$ among sigmoids |
| **R1.2 ITT Variance** | `test_itt_mixture_variance_decomposition` | Sample variance formula on 30 seeds at $\lambda=0.025$: $s^2_{\text{within}} + s^2_{\text{between}}$ | Sample $s = 22.30\% \pm 0.1\%$; $s_{\text{within}} = 11.62\%$, $s_{\text{between}} = 18.83\%$ |
| **R1.3 Welch $t$-test** | `test_welch_t_test_permutation_control` | Welch $t$-test on Permuted ($32.4 \pm 4.1$) vs ERM ($34.2 \pm 4.2$) with $n=30$ | $t = 1.68 \pm 0.05, p = 0.098 \pm 0.005$ |
| **R1.4 Granger Causality** | `test_granger_causality_degrees_of_freedom` | Bivariate VAR(2) cluster-robust $F(2, 29) = 3.72$ on 30 seed clusters | $p = 0.0366$ ($p < 0.05$); classical $p=0.0084$ rejected |
| **R1.5 $\hbar$ Baseline** | `test_hbar_baseline_standardization` | 30 production seeds at $\lambda=0.000$ in `run-log.csv` | Mean $58.74\% \pm 13.97\%$, SEM $2.55\%$ |
| **R2.1 Kramers Removal** | `test_kramers_barrier_excised_from_manuscript` | String audit in `paper/writing/manuscript.tex` | 0 occurrences of ungrounded potential energy formula $-\frac{1}{2}\mu_\perp v^2 + \frac{1}{3}\kappa v^3$ |
| **R2.2 Potential Monotonicity**| `test_potential_energy_monotonicity_on_physical_domain` | Analytical 1st/2nd derivative of $V(v)$ for $\lambda < \lambda_c$ | $V'(v) > 0$ strictly for all $v > 0$ on $\mathbb{R}_{\ge 0}$ |
| **R2.3 Fixed Point** | `test_transcritical_bifurcation_fixed_point_scaling` | Transcritical ODE normal form $v^* = (\lambda - \lambda_c)/\kappa$ | $v^*(0.025) = 0.0$; $v^*(0.50) = 0.475$ |
| **R3.1 Table Inventory** | `test_all_17_processed_csv_tables_exist` | Filesystem check in `paper/data/processed/` | Exactly 17 required CSV tables present |
| **R3.2 Log Completeness** | `test_raw_run_log_mece_structure` | Line count and cell breakdown of `run-log.csv` | Exactly 961 lines (960 runs), all `PASS` |
| **R4.1 GRU Params** | `test_gru_parameter_count_unidirectional` | PyTorch `nn.GRU(128, 128, num_layers=2)` | Exactly 408,608 parameters (0.41M) |
| **R4.2 Participation Ratio**| `test_participation_ratio_mathematical_bound` | Cauchy-Schwarz lower bound on $1/\sum p_i^2$ | $D_{\text{eff}} \ge 2.2897$ ($\ge 2.29$) |
| **R4.3 Bibliography** | `test_bibliography_citation_keys_and_attributions` | BibTeX parser and text inspection | Kim 2020 (COGS), Hupkes 2020 (diagnostic), Merrill 2024 (ICLR), Nakkiran 2021 (Double Descent) |
| **R4.4 Repository Links** | `test_repository_urls_canonical` | URL regex match in `manuscript.tex` | All point to `https://github.com/basyirin-dev/sigma-model` |

---

## 4. Test Execution & CI Commands

To execute the test suite within the dedicated environment:

```bash
# Run the Phase 0 E2E test suite
PYTHONPATH=.:code:paper/src pytest paper/tests/test_phase0_e2e_requirements.py -v

# Run with coverage report
PYTHONPATH=.:code:paper/src pytest paper/tests/test_phase0_e2e_requirements.py --cov=paper/src

# Run entire paper test suite
PYTHONPATH=.:code:paper/src pytest tests/ paper/tests/

# Verify code style and linting
ruff check paper/tests/test_phase0_e2e_requirements.py
```

---

## 5. Acceptance & Sign-off Criteria

The test suite is officially **READY** when:
1. All test cases in `paper/tests/test_phase0_e2e_requirements.py` execute and pass.
2. Code follows PEP 8 / Ruff style guidelines with 0 lint violations.
3. Every test failure maps cleanly to an unresolved defect in the implementation track, preventing premature sign-off.
4. `TEST_READY.md` is published at the project root with the execution summary and test manifest.
