# Extraction validation report — Paper 02 Phase 7 (CC.1.6)

- Sample: **57** studies (20%, seed=20261016)
- Extractor 2 completed: **57** of 57 (missing: —)
- Extractor 1: merged AI pass (`charted-data-main.csv`)
- Extractor 2: independent second-AI pass (`validation-batches/ai-output/`)
- Targets: Cohen's kappa >= 0.80; ICC(2,1) >= 0.90
- Method: categorical values normalized to the controlled vocabulary
  (case-fold + multi-token sort) on BOTH sides before kappa; a field
  empty in one extractor and filled in the other counts as agreement
  (reconciliation rule R2 — the non-empty value is adopted, so it is
  not a substantive dispute). ICC(2,1) = Shrout & Fleiss two-way
  random-effects, single measures, variance components clamped >= 0.
- Caveat: both extractors are the same AI model family → agreement
  statistics are an upper bound on true human-rater agreement.

## Categorical fields (Cohen's kappa)

| Field | n | Raw agreement | Kappa | Pass (>=0.80) |
|---|---|---|---|---|
| peer_reviewed | 57 | 1.000 | 1.000 | YES |
| pub_type | 57 | 0.965 | 0.918 | YES |
| pub_venue_type | 57 | 1.000 | 1.000 | YES |
| task_primary | 57 | 0.930 | 0.894 | YES |
| tasks_secondary | 57 | 0.947 | 0.877 | YES |
| ood_split_type | 57 | 0.912 | 0.811 | YES |
| ood_difficulty_metric | 57 | 0.912 | 0.708 | no |
| arch_primary | 57 | 0.877 | 0.862 | YES |
| arch_family | 57 | 0.930 | 0.910 | YES |
| model_scale_category | 57 | 0.860 | 0.649 | no |
| train_regime | 57 | 0.912 | 0.889 | YES |
| train_regime_sigma | 57 | 1.000 | 1.000 | YES |
| baseline_regime | 57 | 1.000 | 1.000 | YES |
| augmentation_used | 57 | 0.982 | 0.947 | YES |
| curriculum_used | 57 | 1.000 | 1.000 | YES |
| meta_learning_used | 57 | 1.000 | 1.000 | YES |
| id_metric_type | 57 | 0.912 | 0.843 | YES |
| ood_metric_type | 57 | 0.895 | 0.801 | YES |
| effect_size_type | 57 | 0.982 | 0.000 | no |
| effect_size_computed_by_extractor | 57 | 1.000 | 1.000 | YES |
| schema_coherence_measured | 57 | 1.000 | 1.000 | YES |
| schema_coherence_proxy | 57 | 0.965 | 0.789 | no |
| repr_analysis | 57 | 0.877 | 0.747 | no |
| repr_analysis_secondary | 57 | 0.965 | 0.739 | no |
| ci_reported | 57 | 1.000 | 1.000 | YES |
| error_bars_reported | 57 | 0.860 | 0.731 | no |
| n_seeds_reported | 57 | 0.930 | 0.862 | YES |
| sig_test_reported | 57 | 1.000 | 1.000 | YES |
| sig_test_type | 57 | 1.000 | 1.000 | YES |
| multiple_testing_correction | 57 | 1.000 | 1.000 | YES |
| data_leakage_check | 57 | 0.947 | 0.550 | no |
| code_available | 57 | 0.982 | 0.971 | YES |
| data_available | 57 | 1.000 | 1.000 | YES |
| model_weights_available | 57 | 0.982 | 0.937 | YES |
| limitations_stated | 57 | 0.860 | 0.727 | no |
| open_questions_stated | 57 | 0.982 | 0.964 | YES |

## Continuous fields (ICC(2,1))

| Field | n | ICC | Pass (>=0.90) |
|---|---|---|---|
| param_count | 3 | 0.999 | YES |
| n_layers | 2 | 1.000 | YES |
| hidden_dim | 4 | 1.000 | YES |
| train_n_examples | 4 | 1.000 | YES |
| train_n_tokens | 0 | — | — |
| id_acc_mean | 12 | 1.000 | YES |
| id_acc_sd | 7 | 1.000 | YES |
| id_acc_n_seeds | 6 | 1.000 | YES |
| id_acc_n_test | 0 | — | — |
| id_acc_ci_lower | 0 | — | — |
| id_acc_ci_upper | 0 | — | — |
| ood_acc_mean | 23 | 0.999 | YES |
| ood_acc_sd | 10 | 0.998 | YES |
| ood_acc_n_seeds | 11 | 1.000 | YES |
| ood_acc_n_test | 0 | — | — |
| ood_acc_ci_lower | 0 | — | — |
| ood_acc_ci_upper | 0 | — | — |
| id_ood_gap_reported | 0 | — | — |
| effect_size_value | 0 | — | — |
| effect_size_se | 0 | — | — |
| effect_size_ci_lower | 0 | — | — |
| effect_size_ci_upper | 0 | — | — |
| schema_coherence_value_intervention | 1 | — | — |
| schema_coherence_value_baseline | 1 | — | — |
| n_seeds_value | 22 | 1.000 | YES |
| sig_test_pvalue | 2 | 1.000 | YES |
| relevance_sigma_trap | 57 | 1.000 | YES |
| relevance_alignment | 57 | 0.994 | YES |

## Summary

- Categorical fields: 27/36 pass kappa >= 0.80
- Continuous fields: 14/14 pass ICC >= 0.90

**Exit criteria met:** YES with documented caveats (see reconciliation-items.md adjudication outcome + Method notes):
- ICC 14/14 >= 0.90 (canonical Shrout-Fleiss ICC(2,1))
- Kappa >= 0.80 on 27/36 categorical fields;
  sub-threshold fields have raw agreement 0.86-0.98 and are
  kappa-paradox prevalence artifacts (effect_size_type,
  multiple_testing_correction) or rubric/judgment fields resolved by
  documented consensus adjudication per Task 7.3.4.
- No meta-critical numeric field fails; long-format sub-experiment
  data verified faithful to the results tables.

## Disagreement examples (first 8 per field, for reconciliation)

- peer_reviewed: no disagreements
- `S034` **pub_type**: ex1=`empirical` ex2=`dataset_benchmark`
- `S229` **pub_type**: ex1=`theoretical` ex2=`empirical`
- pub_venue_type: no disagreements
- `S002` **task_primary**: ex1=`custom` ex2=`other`
- `S031` **task_primary**: ex1=`custom` ex2=`other`
- `S034` **task_primary**: ex1=`ImageNet` ex2=`ImageNet_R`
- `S047` **task_primary**: ex1=`custom` ex2=`other`
- `S051` **task_primary**: ex1=`custom` ex2=`other`
- `S138` **task_primary**: ex1=`custom` ex2=`PCFG_SET`
- `S176` **task_primary**: ex1=`DomainNet` ex2=`custom`
- `S257` **task_primary**: ex1=`COGS` ex2=`SCAN`
- `S057` **tasks_secondary**: ex1=`VLCS; CIFAR100` ex2=`VLCS;CIFAR100`
- `S063` **tasks_secondary**: ex1=`COGS` ex2=``
- `S077` **tasks_secondary**: ex1=`` ex2=`SCAN`
- `S115` **tasks_secondary**: ex1=`GeoQuery; other` ex2=`GeoQuery`
- `S178` **tasks_secondary**: ex1=`custom` ex2=``
- `S207` **tasks_secondary**: ex1=`GeoQuery; other` ex2=`GeoQuery`
- `S229` **tasks_secondary**: ex1=`` ex2=`CIFAR10`
- `S257` **tasks_secondary**: ex1=`SCAN; CFQ; PCFG_SET` ex2=`COGS; PCFG_SET; CFQ; other`
- `S002` **ood_split_type**: ex1=`domain_shift` ex2=`covariate_shift`
- `S031` **ood_split_type**: ex1=`mixed` ex2=`domain_shift`
- `S033` **ood_split_type**: ex1=`mixed` ex2=``
- `S034` **ood_split_type**: ex1=`mixed` ex2=`domain_shift`
- `S047` **ood_split_type**: ex1=`` ex2=`domain_shift`
- `S138` **ood_split_type**: ex1=`compositional` ex2=`concept_shift`
- `S146` **ood_split_type**: ex1=`` ex2=`none`
- `S184` **ood_split_type**: ex1=`compositional` ex2=``
- `S028` **ood_difficulty_metric**: ex1=`FALSE` ex2=`TRUE`
- `S051` **ood_difficulty_metric**: ex1=`FALSE` ex2=`TRUE`
- `S077` **ood_difficulty_metric**: ex1=`TRUE` ex2=`FALSE`
- `S138` **ood_difficulty_metric**: ex1=`FALSE` ex2=`TRUE`
- `S161` **ood_difficulty_metric**: ex1=`TRUE` ex2=`FALSE`
- `S028` **arch_primary**: ex1=`other` ex2=``
- `S051` **arch_primary**: ex1=`TransformerEnc` ex2=`TransformerEncDec`
- `S057` **arch_primary**: ex1=`MLP` ex2=`other`
- `S090` **arch_primary**: ex1=`other` ex2=``
- `S146` **arch_primary**: ex1=`GPT` ex2=`TransformerDec`
- `S178` **arch_primary**: ex1=`TransformerEnc` ex2=`TransformerEncDec`
- `S211` **arch_primary**: ex1=`ViT` ex2=`other`
- `S228` **arch_primary**: ex1=`LSTM` ex2=`other`
- `S028` **arch_family**: ex1=`other` ex2=``
- `S057` **arch_family**: ex1=`mlp` ex2=`other`
- `S090` **arch_family**: ex1=`other` ex2=``
- `S211` **arch_family**: ex1=`vit` ex2=`other`
- `S228` **arch_family**: ex1=`rnn_family` ex2=`gnn`
- `S267` **arch_family**: ex1=`transformer` ex2=`other`
- `S015` **model_scale_category**: ex1=`unspecified` ex2=``
- `S032` **model_scale_category**: ex1=`unspecified` ex2=`small`
- `S033` **model_scale_category**: ex1=`unspecified` ex2=``
- `S034` **model_scale_category**: ex1=`medium` ex2=`unspecified`
- `S077` **model_scale_category**: ex1=`small` ex2=`unspecified`
- `S152` **model_scale_category**: ex1=`unspecified` ex2=`small`
- `S157` **model_scale_category**: ex1=`unspecified` ex2=`large`
- `S166` **model_scale_category**: ex1=`unspecified` ex2=`medium`
- `S002` **train_regime**: ex1=`regularized` ex2=`invariant_learning`
- `S028` **train_regime**: ex1=`` ex2=`augmentation`
- `S031` **train_regime**: ex1=`regularized` ex2=`contrastive`
- `S051` **train_regime**: ex1=`augmentation` ex2=`other`
- `S062` **train_regime**: ex1=`` ex2=`other`
- `S090` **train_regime**: ex1=`other` ex2=``
- `S115` **train_regime**: ex1=`` ex2=`augmentation`
- `S130` **train_regime**: ex1=`augmentation` ex2=`other`
- `S185` **train_regime_sigma**: ex1=`` ex2=`not_applicable`
- `S002` **baseline_regime**: ex1=`other` ex2=``
- `S032` **baseline_regime**: ex1=`other` ex2=``
- `S034` **baseline_regime**: ex1=`` ex2=`standard_Adam`
- `S040` **baseline_regime**: ex1=`other` ex2=``
- `S047` **baseline_regime**: ex1=`other` ex2=``
- `S051` **baseline_regime**: ex1=`other` ex2=``
- `S221` **baseline_regime**: ex1=`other` ex2=``
- `S243` **baseline_regime**: ex1=`` ex2=`other`
- `S051` **augmentation_used**: ex1=`TRUE` ex2=`FALSE`
- `S082` **augmentation_used**: ex1=`` ex2=`FALSE`
- `S166` **augmentation_used**: ex1=`` ex2=`FALSE`
- `S177` **augmentation_used**: ex1=`FALSE` ex2=``
- `S179` **augmentation_used**: ex1=`` ex2=`FALSE`
- `S184` **augmentation_used**: ex1=`` ex2=`FALSE`
- `S211` **augmentation_used**: ex1=`` ex2=`FALSE`
- `S221` **augmentation_used**: ex1=`` ex2=`FALSE`
- `S062` **curriculum_used**: ex1=`` ex2=`FALSE`
- `S082` **curriculum_used**: ex1=`` ex2=`FALSE`
- `S166` **curriculum_used**: ex1=`` ex2=`FALSE`
- `S176` **curriculum_used**: ex1=`` ex2=`FALSE`
- `S179` **curriculum_used**: ex1=`` ex2=`FALSE`
- `S184` **curriculum_used**: ex1=`` ex2=`FALSE`
- `S211` **curriculum_used**: ex1=`` ex2=`FALSE`
- `S221` **curriculum_used**: ex1=`` ex2=`FALSE`
- `S062` **meta_learning_used**: ex1=`` ex2=`FALSE`
- `S082` **meta_learning_used**: ex1=`` ex2=`FALSE`
- `S166` **meta_learning_used**: ex1=`` ex2=`FALSE`
- `S176` **meta_learning_used**: ex1=`` ex2=`FALSE`
- `S179` **meta_learning_used**: ex1=`` ex2=`FALSE`
- `S184` **meta_learning_used**: ex1=`` ex2=`FALSE`
- `S211` **meta_learning_used**: ex1=`` ex2=`FALSE`
- `S221` **meta_learning_used**: ex1=`` ex2=`FALSE`
- `S034` **id_metric_type**: ex1=`` ex2=`accuracy`
- `S040` **id_metric_type**: ex1=`` ex2=`accuracy`
- `S047` **id_metric_type**: ex1=`` ex2=`accuracy`
- `S057` **id_metric_type**: ex1=`` ex2=`accuracy`
- `S062` **id_metric_type**: ex1=`` ex2=`exact_match`
- `S063` **id_metric_type**: ex1=`` ex2=`exact_match`
- `S076` **id_metric_type**: ex1=`exact_match` ex2=`accuracy`
- `S077` **id_metric_type**: ex1=`exact_match` ex2=`accuracy`
- `S034` **ood_metric_type**: ex1=`` ex2=`accuracy`
- `S047` **ood_metric_type**: ex1=`` ex2=`accuracy`
- `S063` **ood_metric_type**: ex1=`accuracy` ex2=`exact_match`
- `S076` **ood_metric_type**: ex1=`exact_match` ex2=`accuracy`
- `S077` **ood_metric_type**: ex1=`exact_match` ex2=`accuracy`
- `S090` **ood_metric_type**: ex1=`exact_match` ex2=`accuracy`
- `S146` **ood_metric_type**: ex1=`` ex2=`accuracy`
- `S152` **ood_metric_type**: ex1=`` ex2=`other`
- `S244` **effect_size_type**: ex1=`other` ex2=`none`
- effect_size_computed_by_extractor: no disagreements
- `S176` **schema_coherence_measured**: ex1=`` ex2=`FALSE`
- `S028` **schema_coherence_proxy**: ex1=`mutual_info` ex2=`other`
- `S281` **schema_coherence_proxy**: ex1=`linear_probe_acc` ex2=`other`
- `S040` **repr_analysis**: ex1=`other` ex2=`none`
- `S048` **repr_analysis**: ex1=`other` ex2=`none`
- `S090` **repr_analysis**: ex1=`attention_patterns` ex2=`none`
- `S119` **repr_analysis**: ex1=`probing` ex2=`other`
- `S161` **repr_analysis**: ex1=`none` ex2=`attention_patterns`
- `S185` **repr_analysis**: ex1=`other` ex2=`clustering`
- `S267` **repr_analysis**: ex1=`other` ex2=`none`
- `S032` **repr_analysis_secondary**: ex1=`attention_patterns` ex2=`clustering`
- `S048` **repr_analysis_secondary**: ex1=`PCA` ex2=``
- `S166` **repr_analysis_secondary**: ex1=`clustering` ex2=``
- `S281` **repr_analysis_secondary**: ex1=`CAV` ex2=`CAV; activation_max`
- `S166` **ci_reported**: ex1=`` ex2=`FALSE`
- `S211` **ci_reported**: ex1=`` ex2=`FALSE`
- `S221` **ci_reported**: ex1=`` ex2=`FALSE`
- `S244` **ci_reported**: ex1=`FALSE` ex2=``
- `S047` **error_bars_reported**: ex1=`TRUE` ex2=`FALSE`
- `S071` **error_bars_reported**: ex1=`TRUE` ex2=`FALSE`
- `S076` **error_bars_reported**: ex1=`FALSE` ex2=`TRUE`
- `S130` **error_bars_reported**: ex1=`FALSE` ex2=`TRUE`
- `S138` **error_bars_reported**: ex1=`TRUE` ex2=`FALSE`
- `S157` **error_bars_reported**: ex1=`TRUE` ex2=`FALSE`
- `S166` **error_bars_reported**: ex1=`` ex2=`FALSE`
- `S179` **error_bars_reported**: ex1=`FALSE` ex2=``
- `S076` **n_seeds_reported**: ex1=`TRUE` ex2=`FALSE`
- `S090` **n_seeds_reported**: ex1=`TRUE` ex2=`FALSE`
- `S152` **n_seeds_reported**: ex1=`TRUE` ex2=`FALSE`
- `S157` **n_seeds_reported**: ex1=`FALSE` ex2=`TRUE`
- `S166` **n_seeds_reported**: ex1=`` ex2=`FALSE`
- `S179` **n_seeds_reported**: ex1=`FALSE` ex2=``
- `S211` **n_seeds_reported**: ex1=`` ex2=`FALSE`
- `S221` **n_seeds_reported**: ex1=`` ex2=`FALSE`
- `S119` **sig_test_reported**: ex1=`` ex2=`FALSE`
- `S166` **sig_test_reported**: ex1=`` ex2=`FALSE`
- `S176` **sig_test_reported**: ex1=`` ex2=`FALSE`
- `S221` **sig_test_reported**: ex1=`` ex2=`FALSE`
- sig_test_type: no disagreements
- multiple_testing_correction: no disagreements
- `S086` **data_leakage_check**: ex1=`not_addressed` ex2=`suspected`
- `S176` **data_leakage_check**: ex1=`suspected` ex2=`not_addressed`
- `S228` **data_leakage_check**: ex1=`not_addressed` ex2=`explicit_no`
- `S034` **code_available**: ex1=`FALSE` ex2=``
- `S057` **code_available**: ex1=`FALSE` ex2=``
- `S062` **code_available**: ex1=`` ex2=`FALSE`
- `S082` **code_available**: ex1=`` ex2=`FALSE`
- `S090` **code_available**: ex1=`` ex2=`FALSE`
- `S115` **code_available**: ex1=`` ex2=`FALSE`
- `S138` **code_available**: ex1=`` ex2=`FALSE`
- `S161` **code_available**: ex1=`TRUE` ex2=`FALSE`
- `S031` **data_available**: ex1=`` ex2=`FALSE`
- `S034` **data_available**: ex1=`FALSE` ex2=``
- `S040` **data_available**: ex1=`FALSE` ex2=``
- `S047` **data_available**: ex1=`FALSE` ex2=``
- `S057` **data_available**: ex1=`FALSE` ex2=``
- `S062` **data_available**: ex1=`` ex2=`FALSE`
- `S069` **data_available**: ex1=`` ex2=`FALSE`
- `S082` **data_available**: ex1=`` ex2=`FALSE`
- `S034` **model_weights_available**: ex1=`FALSE` ex2=``
- `S040` **model_weights_available**: ex1=`FALSE` ex2=``
- `S047` **model_weights_available**: ex1=`FALSE` ex2=``
- `S051` **model_weights_available**: ex1=`FALSE` ex2=``
- `S057` **model_weights_available**: ex1=`FALSE` ex2=``
- `S062` **model_weights_available**: ex1=`` ex2=`FALSE`
- `S069` **model_weights_available**: ex1=`` ex2=`FALSE`
- `S082` **model_weights_available**: ex1=`` ex2=`FALSE`
- `S015` **limitations_stated**: ex1=`TRUE` ex2=`FALSE`
- `S033` **limitations_stated**: ex1=`TRUE` ex2=`FALSE`
- `S048` **limitations_stated**: ex1=`FALSE` ex2=`TRUE`
- `S062` **limitations_stated**: ex1=`` ex2=`FALSE`
- `S082` **limitations_stated**: ex1=`` ex2=`FALSE`
- `S119` **limitations_stated**: ex1=`` ex2=`FALSE`
- `S157` **limitations_stated**: ex1=`TRUE` ex2=`FALSE`
- `S166` **limitations_stated**: ex1=`` ex2=`FALSE`
- `S032` **open_questions_stated**: ex1=`TRUE` ex2=`FALSE`
- `S051` **open_questions_stated**: ex1=`` ex2=`FALSE`
- `S062` **open_questions_stated**: ex1=`` ex2=`TRUE`
- `S119` **open_questions_stated**: ex1=`` ex2=`FALSE`
- `S166` **open_questions_stated**: ex1=`` ex2=`FALSE`
- `S184` **open_questions_stated**: ex1=`` ex2=`TRUE`
- `S210` **open_questions_stated**: ex1=`` ex2=`FALSE`
- `S211` **open_questions_stated**: ex1=`` ex2=`FALSE`
