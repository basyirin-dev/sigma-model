# Data quality report — Paper 02 Phase 7 (Task 7.4)

- Rows (long format): **1541**
- Missing threshold: **10%**

## 7.4.1 Missing data (fields >10% missing)

| Field | Missing | Rate | |
|---|---|---|---|
| pub_type_other | 1541 | 100.0% | flag-optional/conditional |
| train_n_tokens | 1541 | 100.0% | flag-optional/conditional |
| id_ood_gap_raw | 1541 | 100.0% | flag-optional/conditional |
| id_ood_gap_se | 1541 | 100.0% | flag-optional/conditional |
| id_ood_gap_reported | 1541 | 100.0% | flag-optional/conditional |
| effect_size_se | 1541 | 100.0% | flag-optional/conditional |
| effect_size_ci_lower | 1541 | 100.0% | flag-optional/conditional |
| effect_size_ci_upper | 1541 | 100.0% | flag-optional/conditional |
| id_acc_ci_lower | 1535 | 99.6% | flag-optional/conditional |
| id_acc_ci_upper | 1535 | 99.6% | flag-optional/conditional |
| effect_size_value | 1531 | 99.4% | flag-optional/conditional |
| schema_coherence_value_baseline | 1525 | 99.0% | flag-optional/conditional |
| id_acc_n_test | 1523 | 98.8% | flag-optional/conditional |
| schema_coherence_value | 1523 | 98.8% | flag-optional/conditional |
| open_questions_extractor | 1522 | 98.8% | flag-optional/conditional |
| schema_coherence_value_intervention | 1518 | 98.5% | flag-optional/conditional |
| repr_analysis_secondary | 1513 | 98.2% | flag-optional/conditional |
| ood_acc_n_test | 1510 | 98.0% | flag-optional/conditional |
| schema_coherence_proxy_other | 1496 | 97.1% | flag-optional/conditional |
| limitations_extractor | 1484 | 96.3% | flag-optional/conditional |
| ood_acc_ci_lower | 1480 | 96.0% | flag-optional/conditional |
| ood_acc_ci_upper | 1480 | 96.0% | flag-optional/conditional |
| param_count | 1467 | 95.2% | flag-optional/conditional |
| schema_coherence_proxy | 1456 | 94.5% | flag-optional/conditional |
| sig_test_pvalue | 1446 | 93.8% | flag-optional/conditional |
| n_layers | 1410 | 91.5% | flag-optional/conditional |
| repr_analysis_layer | 1395 | 90.5% | flag-optional/conditional |
| train_n_examples | 1394 | 90.5% | flag-optional/conditional |
| id_metric_other | 1392 | 90.3% | flag-optional/conditional |
| sig_test_type | 1391 | 90.3% | flag-optional/conditional |
| data_url | 1380 | 89.6% | flag-optional/conditional |
| hidden_dim | 1369 | 88.8% | flag-optional/conditional |
| id_acc_sd | 1359 | 88.2% | flag-optional/conditional |
| augmentation_type | 1312 | 85.1% | flag-optional/conditional |
| id_acc_n_seeds | 1294 | 84.0% | flag-optional/conditional |
| ood_metric_other | 1261 | 81.8% | flag-optional/conditional |
| doi | 1257 | 81.6% | flag-optional/conditional |
| train_regime_other | 1254 | 81.4% | flag-optional/conditional |
| baseline_regime | 1201 | 77.9% | FLAG-required |
| ood_difficulty_metric_name | 1197 | 77.7% | flag-optional/conditional |
| id_ood_gap | 1189 | 77.2% | flag-optional/conditional |
| code_url | 1123 | 72.9% | flag-optional/conditional |
| tasks_secondary | 1109 | 72.0% | flag-optional/conditional |
| id_acc_mean | 1093 | 70.9% | flag-optional/conditional |
| ood_acc_n_seeds | 1057 | 68.6% | flag-optional/conditional |
| ood_acc_sd | 1042 | 67.6% | flag-optional/conditional |
| repr_analysis_finding | 1018 | 66.1% | flag-optional/conditional |
| limitations_text | 950 | 61.6% | flag-optional/conditional |
| open_questions_text | 896 | 58.1% | flag-optional/conditional |
| n_seeds_value | 888 | 57.6% | flag-optional/conditional |
| train_regime | 749 | 48.6% | FLAG-required |
| effect_size_notes | 547 | 35.5% | flag-optional/conditional |
| data_available | 494 | 32.1% | FLAG-required |
| model_weights_available | 478 | 31.0% | FLAG-required |
| task_custom_name | 476 | 30.9% | flag-optional/conditional |
| limitations_stated | 440 | 28.6% | FLAG-required |
| id_metric_type | 421 | 27.3% | FLAG-required |
| other_metrics_reported | 407 | 26.4% | flag-optional/conditional |
| open_questions_stated | 396 | 25.7% | FLAG-required |
| code_available | 388 | 25.2% | FLAG-required |
| ood_acc_mean | 321 | 20.8% | flag-optional/conditional |
| arxiv_id | 291 | 18.9% | flag-optional/conditional |
| schema_coherence_notes | 279 | 18.1% | flag-optional/conditional |
| curriculum_used | 162 | 10.5% | FLAG-required |
| meta_learning_used | 155 | 10.1% | FLAG-required |

## 7.4.2 / 7.4.3 Inconsistent coding & vocabulary normalization


## 7.4.4 Numeric range checks

- no out-of-range values

## 7.4.5 Cross-field validation (V01-V20)

| Rule | Severity | Violations |
|---|---|---|
| V01 | warning | 444 |
| V02 | warning | 1210 |
| V03 | error | 89 ⚠ |
| V04 | error | 225 ⚠ |
| V05 | error | 6 ⚠ |
| V06 | error | 0 |
| V07 | error | 0 |
| V08 | error | 0 |
| V09 | error | 39 ⚠ |
| V10 | error | 21 ⚠ |
| V11 | warning | 45 |
| V12 | warning | 91 |
| V13 | error | 0 |
| V14 | error | 0 |
| V15 | error | 0 |
| V16 | warning | 11 |
| V17 | warning | 0 |
| V18 | info | 0 |
| V19 | warning | 19 |
| V20 | warning | 0 |
- V05 (study-level, main CSV): 0 rows with id_ood_gap_raw != id_acc_mean - ood_acc_mean

## Summary

- Fields >10% missing: **65** (10 required)
- Vocabulary values auto-normalized: **0** (see remediation-log.csv)
- Numeric range violations: **0**
- V01-V20 error-level violations: **380** (per-rule: V03=89, V04=225, V05=6, V09=39, V10=21)
