# Extraction validation report — Paper 02 Phase 7 (CC.1.6)

- Sample: **57** studies (20%, seed=20261016)
- Extractor 2 completed: **0** of 57 (missing: S002, S015, S028, S031, S032, S033, S034, S040, S047, S048, S051, S057, S062, S063, S069, S071, S076, S077, S082, S086, S090, S115, S119, S130, S138, S146, S152, S157, S161, S166, S176, S177, S178, S179, S184, S185, S202, S207, S210, S211, S216, S221, S228, S229, S239, S242, S243, S244, S257, S261, S264, S267, S270, S272, S277, S281, S285)
- Extractor 1: merged AI pass (`charted-data-main.csv`)
- Extractor 2: independent second-AI pass (`validation-batches/ai-output/`)
- Targets: Cohen's kappa >= 0.80; ICC(2,1) >= 0.90

## Categorical fields (Cohen's kappa)

| Field | n | Raw agreement | Kappa | Pass (>=0.80) |
|---|---|---|---|---|
| peer_reviewed | 0 | 0.000 | 0.000 | no |
| pub_type | 0 | 0.000 | 0.000 | no |
| pub_venue_type | 0 | 0.000 | 0.000 | no |
| task_primary | 0 | 0.000 | 0.000 | no |
| tasks_secondary | 0 | 0.000 | 0.000 | no |
| ood_split_type | 0 | 0.000 | 0.000 | no |
| ood_difficulty_metric | 0 | 0.000 | 0.000 | no |
| arch_primary | 0 | 0.000 | 0.000 | no |
| arch_family | 0 | 0.000 | 0.000 | no |
| model_scale_category | 0 | 0.000 | 0.000 | no |
| train_regime | 0 | 0.000 | 0.000 | no |
| train_regime_sigma | 0 | 0.000 | 0.000 | no |
| baseline_regime | 0 | 0.000 | 0.000 | no |
| augmentation_used | 0 | 0.000 | 0.000 | no |
| curriculum_used | 0 | 0.000 | 0.000 | no |
| meta_learning_used | 0 | 0.000 | 0.000 | no |
| id_metric_type | 0 | 0.000 | 0.000 | no |
| ood_metric_type | 0 | 0.000 | 0.000 | no |
| effect_size_type | 0 | 0.000 | 0.000 | no |
| effect_size_computed_by_extractor | 0 | 0.000 | 0.000 | no |
| schema_coherence_measured | 0 | 0.000 | 0.000 | no |
| schema_coherence_proxy | 0 | 0.000 | 0.000 | no |
| repr_analysis | 0 | 0.000 | 0.000 | no |
| repr_analysis_secondary | 0 | 0.000 | 0.000 | no |
| ci_reported | 0 | 0.000 | 0.000 | no |
| error_bars_reported | 0 | 0.000 | 0.000 | no |
| n_seeds_reported | 0 | 0.000 | 0.000 | no |
| sig_test_reported | 0 | 0.000 | 0.000 | no |
| sig_test_type | 0 | 0.000 | 0.000 | no |
| multiple_testing_correction | 0 | 0.000 | 0.000 | no |
| data_leakage_check | 0 | 0.000 | 0.000 | no |
| code_available | 0 | 0.000 | 0.000 | no |
| data_available | 0 | 0.000 | 0.000 | no |
| model_weights_available | 0 | 0.000 | 0.000 | no |
| limitations_stated | 0 | 0.000 | 0.000 | no |
| open_questions_stated | 0 | 0.000 | 0.000 | no |

## Continuous fields (ICC(2,1))

| Field | n | ICC | Pass (>=0.90) |
|---|---|---|---|
| param_count | 0 | — | — |
| n_layers | 0 | — | — |
| hidden_dim | 0 | — | — |
| train_n_examples | 0 | — | — |
| train_n_tokens | 0 | — | — |
| id_acc_mean | 0 | — | — |
| id_acc_sd | 0 | — | — |
| id_acc_n_seeds | 0 | — | — |
| id_acc_n_test | 0 | — | — |
| id_acc_ci_lower | 0 | — | — |
| id_acc_ci_upper | 0 | — | — |
| ood_acc_mean | 0 | — | — |
| ood_acc_sd | 0 | — | — |
| ood_acc_n_seeds | 0 | — | — |
| ood_acc_n_test | 0 | — | — |
| ood_acc_ci_lower | 0 | — | — |
| ood_acc_ci_upper | 0 | — | — |
| id_ood_gap_reported | 0 | — | — |
| effect_size_value | 0 | — | — |
| effect_size_se | 0 | — | — |
| effect_size_ci_lower | 0 | — | — |
| effect_size_ci_upper | 0 | — | — |
| schema_coherence_value_intervention | 0 | — | — |
| schema_coherence_value_baseline | 0 | — | — |
| n_seeds_value | 0 | — | — |
| sig_test_pvalue | 0 | — | — |
| relevance_sigma_trap | 0 | — | — |
| relevance_alignment | 0 | — | — |

## Summary

- Categorical fields: 0/36 pass kappa >= 0.80
- Continuous fields: 0/0 pass ICC >= 0.90

**Exit criteria met:** NO — reconcile below and re-run (Task 7.3.4)

## Disagreement examples (first 8 per field, for reconciliation)

- peer_reviewed: no disagreements
- pub_type: no disagreements
- pub_venue_type: no disagreements
- task_primary: no disagreements
- tasks_secondary: no disagreements
- ood_split_type: no disagreements
- ood_difficulty_metric: no disagreements
- arch_primary: no disagreements
- arch_family: no disagreements
- model_scale_category: no disagreements
- train_regime: no disagreements
- train_regime_sigma: no disagreements
- baseline_regime: no disagreements
- augmentation_used: no disagreements
- curriculum_used: no disagreements
- meta_learning_used: no disagreements
- id_metric_type: no disagreements
- ood_metric_type: no disagreements
- effect_size_type: no disagreements
- effect_size_computed_by_extractor: no disagreements
- schema_coherence_measured: no disagreements
- schema_coherence_proxy: no disagreements
- repr_analysis: no disagreements
- repr_analysis_secondary: no disagreements
- ci_reported: no disagreements
- error_bars_reported: no disagreements
- n_seeds_reported: no disagreements
- sig_test_reported: no disagreements
- sig_test_type: no disagreements
- multiple_testing_correction: no disagreements
- data_leakage_check: no disagreements
- code_available: no disagreements
- data_available: no disagreements
- model_weights_available: no disagreements
- limitations_stated: no disagreements
- open_questions_stated: no disagreements
