# Data quality report — Paper 02 Phase 7 (Task 7.4)

- Rows (long format): **33**
- Missing threshold: **10%**

## 7.4.1 Missing data (fields >10% missing)

| Field | Missing | Rate | |
|---|---|---|---|
| pub_type_other | 33 | 100.0% | flag-optional/conditional |
| train_n_tokens | 33 | 100.0% | flag-optional/conditional |
| id_acc_n_test | 33 | 100.0% | flag-optional/conditional |
| ood_acc_n_test | 33 | 100.0% | flag-optional/conditional |
| id_ood_gap_reported | 33 | 100.0% | flag-optional/conditional |
| effect_size_value | 33 | 100.0% | flag-optional/conditional |
| effect_size_se | 33 | 100.0% | flag-optional/conditional |
| effect_size_ci_lower | 33 | 100.0% | flag-optional/conditional |
| effect_size_ci_upper | 33 | 100.0% | flag-optional/conditional |
| schema_coherence_proxy | 33 | 100.0% | flag-optional/conditional |
| schema_coherence_proxy_other | 33 | 100.0% | flag-optional/conditional |
| schema_coherence_value_intervention | 33 | 100.0% | flag-optional/conditional |
| schema_coherence_value_baseline | 33 | 100.0% | flag-optional/conditional |
| repr_analysis_secondary | 33 | 100.0% | flag-optional/conditional |
| repr_analysis_layer | 33 | 100.0% | flag-optional/conditional |
| sig_test_type | 33 | 100.0% | flag-optional/conditional |
| sig_test_pvalue | 33 | 100.0% | flag-optional/conditional |
| limitations_extractor | 33 | 100.0% | flag-optional/conditional |
| open_questions_extractor | 33 | 100.0% | flag-optional/conditional |
| other_metrics_reported | 33 | 100.0% | flag-optional/conditional |
| schema_coherence_value | 33 | 100.0% | flag-optional/conditional |
| param_count | 30 | 90.9% | flag-optional/conditional |
| n_layers | 30 | 90.9% | flag-optional/conditional |
| hidden_dim | 30 | 90.9% | flag-optional/conditional |
| train_regime_other | 30 | 90.9% | flag-optional/conditional |
| ood_difficulty_metric_name | 27 | 81.8% | flag-optional/conditional |
| train_n_examples | 27 | 81.8% | flag-optional/conditional |
| id_acc_ci_lower | 27 | 81.8% | flag-optional/conditional |
| id_acc_ci_upper | 27 | 81.8% | flag-optional/conditional |
| ood_acc_ci_lower | 27 | 81.8% | flag-optional/conditional |
| ood_acc_ci_upper | 27 | 81.8% | flag-optional/conditional |
| tasks_secondary | 24 | 72.7% | flag-optional/conditional |
| id_acc_sd | 24 | 72.7% | flag-optional/conditional |
| id_ood_gap_se | 24 | 72.7% | flag-optional/conditional |
| repr_analysis_finding | 24 | 72.7% | flag-optional/conditional |
| task_custom_name | 21 | 63.6% | flag-optional/conditional |
| augmentation_type | 21 | 63.6% | flag-optional/conditional |
| doi | 18 | 54.5% | flag-optional/conditional |
| id_ood_gap_raw | 15 | 45.5% | flag-optional/conditional |
| open_questions_text | 15 | 45.5% | flag-optional/conditional |
| id_ood_gap | 15 | 45.5% | flag-optional/conditional |
| id_acc_mean | 14 | 42.4% | flag-optional/conditional |
| id_metric_other | 12 | 36.4% | flag-optional/conditional |
| data_url | 12 | 36.4% | flag-optional/conditional |
| ood_acc_sd | 10 | 30.3% | flag-optional/conditional |
| ood_metric_other | 9 | 27.3% | flag-optional/conditional |

## 7.4.2 / 7.4.3 Inconsistent coding & vocabulary normalization

- `tasks_secondary`: **'OfficeHome; VLCS; TerraIncognita; DomainNet' x3 not in vocabulary (task)** — review manually

## 7.4.4 Numeric range checks

- no out-of-range values

## 7.4.5 Cross-field validation (V01-V20)

| Rule | Severity | Violations |
|---|---|---|
| V01 | warning | 19 |
| V02 | warning | 30 |
| V03 | error | 0 |
| V04 | error | 0 |
| V05 | error | 0 |
| V06 | error | 0 |
| V07 | error | 0 |
| V08 | error | 0 |
| V09 | error | 0 |
| V10 | error | 0 |
| V11 | warning | 0 |
| V12 | warning | 0 |
| V13 | error | 0 |
| V14 | error | 0 |
| V15 | error | 0 |
| V16 | warning | 0 |
| V17 | warning | 0 |
| V18 | info | 0 |
| V19 | warning | 0 |
| V20 | warning | 0 |

## Summary

- Fields >10% missing: **46** (0 required)
- Vocabulary values auto-normalized: **0** (see remediation-log.csv)
- Numeric range violations: **0**
- V01-V20 error-level violations: **0**
