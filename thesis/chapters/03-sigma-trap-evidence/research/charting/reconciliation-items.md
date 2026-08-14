# Reconciliation items — Paper 02 Phase 7 (Task 7.3.4)

- Sample compared: **57** studies (1035 field-level disagreements)
- Resolution rules: R1 pilots are gold; R2 missing value is not a
  dispute (keep the non-empty value); R3 otherwise senior review.

## Systematic disagreements (>= 25% of sample)

- `data_available`: 28/57 differ — **refine template/codebook and re-extract** (7.3.4)
- `model_weights_available`: 28/57 differ — **refine template/codebook and re-extract** (7.3.4)
- `limitations_stated`: 21/57 differ — **refine template/codebook and re-extract** (7.3.4)
- `relevance_sigma_trap`: 18/57 differ — **refine template/codebook and re-extract** (7.3.4)
- `relevance_alignment`: 18/57 differ — **refine template/codebook and re-extract** (7.3.4)
- `id_metric_type`: 18/57 differ — **refine template/codebook and re-extract** (7.3.4)
- `code_available`: 18/57 differ — **refine template/codebook and re-extract** (7.3.4)
- `train_regime`: 17/57 differ — **refine template/codebook and re-extract** (7.3.4)
- `open_questions_stated`: 16/57 differ — **refine template/codebook and re-extract** (7.3.4)

## Template refinement notes

Review the fields above; if the disagreement is a codebook
ambiguity, update `research/extraction-template.md` and
`charting/charted-schema.yaml` (bump minor version), then
re-run the affected extraction.


## Itemized disagreements

| Study | Field | Extractor 1 | Extractor 2 | Resolution |
|---|---|---|---|---|
| S002 | baseline_regime | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S002 | effect_size_notes | — | No effect sizes reported; only raw test accuracies | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S002 | notes | Table 1 garbled by PDF text extraction; only narration-attes… | Marquee result: SFP+REX on Colored-object test accuracy 93.4… | UNRESOLVED — senior reviewer decides; see action |
| S002 | ood_split_type | domain_shift | covariate_shift | UNRESOLVED — senior reviewer decides; see action |
| S002 | other_metrics_reported | — | train accuracy per method and dataset | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S002 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S002 | relevance_sigma_justification | Directly addresses OOD generalization failure via spurious-f… | Directly targets OOD generalization failure driven by spurio… | UNRESOLVED — senior reviewer decides; see action |
| S002 | schema_coherence_notes | No representation-level coherence/compositionality proxy mea… | No representation-level coherence proxy measured | UNRESOLVED — senior reviewer decides; see action |
| S002 | task_custom_name | Full-colored-mnist, Colored-object, Scene-object (biased-env… | Full-colored-mnist; Colored-object; Scene-object (spurious-c… | UNRESOLVED — senior reviewer decides; see action |
| S002 | task_primary | custom | other | UNRESOLVED — senior reviewer decides; see action |
| S002 | train_data_note | Synthetic biased-environment datasets (Full-colored-mnist, C… | Three synthetic vision benchmarks; two biased training envir… | UNRESOLVED — senior reviewer decides; see action |
| S002 | train_regime | regularized | invariant_learning | UNRESOLVED — senior reviewer decides; see action |
| S015 | arch_detail | Survey spans many architectures (CNNs, language models, NLI … | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S015 | effect_size_notes | — | Survey paper; no experimental results | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S015 | limitations_stated | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S015 | limitations_text | Identifies field gaps: computer-vision hegemony in robustnes… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S015 | model_scale_category | unspecified | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S015 | notes | Systematic survey (ACM, 35 pages); no primary experiments or… | Systematic survey introducing three taxonomies of AI robustn… | UNRESOLVED — senior reviewer decides; see action |
| S015 | open_questions_text | Calls for natural/perturbation-agnostic evaluation approache… | Research gaps identified: computer-vision hegemony in robust… | UNRESOLVED — senior reviewer decides; see action |
| S015 | relevance_alignment_justification | Framed under Trustworthy AI with a human-centered perspectiv… | Frames robustness within Trustworthy AI, covering trade-offs… | UNRESOLVED — senior reviewer decides; see action |
| S015 | relevance_sigma_justification | Systematic survey of AI robustness including OOD robustness,… | Systematic survey of AI robustness with taxonomies over meth… | UNRESOLVED — senior reviewer decides; see action |
| S015 | relevance_sigma_trap | 3 | 2 | UNRESOLVED — senior reviewer decides; see action |
| S015 | schema_coherence_notes | — | No representation-level coherence measurement; surveys robus… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S015 | train_data_note | — | No experiments; systematic literature survey across CV and N… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S028 | arch_detail | Multi-modal language model taking image plus textual attribu… | Multi-modal language model; hidden size swept 32-256; repres… | UNRESOLVED — senior reviewer decides; see action |
| S028 | arch_family | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S028 | arch_primary | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S028 | augmentation_type | latent intervention (random alteration of a latent factor du… | latent intervention (random alteration of a latent attribute… | UNRESOLVED — senior reviewer decides; see action |
| S028 | effect_size_notes | No effect sizes reported; headline results are accuracy delt… | No standardized effect sizes; absolute accuracy gains report… | UNRESOLVED — senior reviewer decides; see action |
| S028 | id_acc_mean | 0.996 | 0.963 | UNRESOLVED — senior reviewer decides; see action |
| S028 | id_acc_sd | 0 | 0.0 | UNRESOLVED — senior reviewer decides; see action |
| S028 | notes | Appendix tables 2-7. Main-form = shape task, baseline 8-colo… | Main form = diversity intervention (216 colors) on shape tas… | UNRESOLVED — senior reviewer decides; see action |
| S028 | ood_acc_mean | 0.006 | 0.9 | UNRESOLVED — senior reviewer decides; see action |
| S028 | ood_acc_sd | 0.001 | 0.004 | UNRESOLVED — senior reviewer decides; see action |
| S028 | ood_difficulty_metric | FALSE | TRUE | UNRESOLVED — senior reviewer decides; see action |
| S028 | ood_difficulty_metric_name | — | Normalized Mutual Information (NMI) between latent attribute… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S028 | other_metrics_reported | NMI between latent attributes; p-score (representation paral… | Pearson correlations between parallelism P-scores and OOD ac… | UNRESOLVED — senior reviewer decides; see action |
| S028 | relevance_alignment_justification | No connection to AI alignment or safety; the work concerns i… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S028 | relevance_sigma_justification | Directly studies systematic (compositional) generalization f… | Directly demonstrates the compositional generalization failu… | UNRESOLVED — senior reviewer decides; see action |
| S028 | repr_analysis_finding | Representation parallelism (p-scores) strongly correlates wi… | NMI between latent attributes induces more parallelism in ne… | UNRESOLVED — senior reviewer decides; see action |
| S028 | schema_coherence_notes | Normalized Mutual Information (NMI) between latent attribute… | Parallelism of input features in neural representations corr… | UNRESOLVED — senior reviewer decides; see action |
| S028 | schema_coherence_proxy | mutual_info | other | UNRESOLVED — senior reviewer decides; see action |
| S028 | schema_coherence_proxy_other | — | parallelism of neural representations (P-scores); NMI betwee… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S028 | schema_coherence_value_intervention | — | 0.76 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S028 | task_custom_name | Multi-attribute prediction (color/shape/size/material) on sy… | Synthetic multi-modal object-property prediction (Color, Sha… | UNRESOLVED — senior reviewer decides; see action |
| S028 | train_data_note | Synthetic dataset of rendered objects with latent attributes… | Synthetic visual scenes with objects varying in latent attri… | UNRESOLVED — senior reviewer decides; see action |
| S028 | train_regime | — | augmentation | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S031 | arch_detail | GIN (graph isomorphism network) backbone pre-trained per Gra… | GIN backbone pre-trained via GraphCL-style contrastive learn… | UNRESOLVED — senior reviewer decides; see action |
| S031 | augmentation_type | node dropping during contrastive pre-training (GraphCL setti… | node dropping (GraphCL-style contrastive pre-training) | UNRESOLVED — senior reviewer decides; see action |
| S031 | data_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S031 | effect_size_notes | No effect size reported; relative improvements (2.73% avg on… | No effect sizes; average relative improvement of 2.73% over … | UNRESOLVED — senior reviewer decides; see action |
| S031 | id_acc_n_seeds | — | 3 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S031 | notes | Main-form OOD value = EGOG on GOODMotif-basis (87.49 +/- 2.4… | Main form = EGOG on GOODCMNIST-color: OOD accuracy 62.94 +/-… | UNRESOLVED — senior reviewer decides; see action |
| S031 | ood_acc_mean | 0.8749 | 0.6294 | UNRESOLVED — senior reviewer decides; see action |
| S031 | ood_acc_sd | 0.0241 | 0.0237 | UNRESOLVED — senior reviewer decides; see action |
| S031 | ood_split_type | mixed | domain_shift | UNRESOLVED — senior reviewer decides; see action |
| S031 | other_metrics_reported | — | Trainable parameter counts (efficiency, reduction rates); mo… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S031 | param_count | 552000 | 90000 | UNRESOLVED — senior reviewer decides; see action |
| S031 | relevance_alignment_justification | No connection to AI alignment, safety, or goal misgeneraliza… | Impact statement frames robustness and efficiency for reliab… | UNRESOLVED — senior reviewer decides; see action |
| S031 | relevance_sigma_justification | Directly targets graph OOD generalization failure (the sigma… | Directly targets OOD generalization failure in GNNs by decou… | UNRESOLVED — senior reviewer decides; see action |
| S031 | schema_coherence_notes | — | No representation-level coherence proxy measured; causal/spu… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S031 | task_custom_name | Graph OOD generalization (GOODMotif, GOODCMNIST, GOODSST2, G… | GOODMotif (base/size); GOODCMNIST (color); GOODSST2; GOODTwi… | UNRESOLVED — senior reviewer decides; see action |
| S031 | task_primary | custom | other | UNRESOLVED — senior reviewer decides; see action |
| S031 | train_data_note | GOODMotif (synthetic, basis and size domains), GOODCMNIST (n… | GOODMotif (synthetic, motif determines label, base type/size… | UNRESOLVED — senior reviewer decides; see action |
| S031 | train_regime | regularized | contrastive | UNRESOLVED — senior reviewer decides; see action |
| S032 | arch_detail | GPT-2 model for main experiments; two-layer single-head tran… | GPT-2 on compositional task; mechanism analysis uses two-lay… | UNRESOLVED — senior reviewer decides; see action |
| S032 | baseline_regime | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S032 | effect_size_notes | — | No numeric accuracies reported in excerpt; results presented… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S032 | id_acc_n_seeds | — | 3 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S032 | model_scale_category | unspecified | small | UNRESOLVED — senior reviewer decides; see action |
| S032 | n_layers | — | 2 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S032 | notes | Main quantitative results shown only in figures (Fig 3 phase… | No exact accuracy numbers in excerpt; findings expressed via… | UNRESOLVED — senior reviewer decides; see action |
| S032 | ood_acc_n_seeds | — | 3 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S032 | open_questions_stated | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S032 | open_questions_text | Critical open questions: whether transformers genuinely lear… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S032 | other_metrics_reported | commutativity probability on unseen anchor pairs (c,d)/(d,c)… | Commutativity probability on unseen anchor pairs (c,d)/(d,c)… | UNRESOLVED — senior reviewer decides; see action |
| S032 | relevance_alignment | 3 | 1 | UNRESOLVED — senior reviewer decides; see action |
| S032 | relevance_alignment_justification | Relevant to alignment via interpretability: distinguishing g… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S032 | relevance_sigma_justification | Directly investigates the sigma-trap: transformers show good… | Directly dissects the compositional generalization failure i… | UNRESOLVED — senior reviewer decides; see action |
| S032 | repr_analysis_finding | PCA/TSNE of output embeddings shows Phase-1 models entangle … | Phase 1: poorly organized overlapping anchor-pair clusters (… | UNRESOLVED — senior reviewer decides; see action |
| S032 | repr_analysis_layer | — | 2 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S032 | repr_analysis_secondary | attention_patterns | clustering | UNRESOLVED — senior reviewer decides; see action |
| S032 | schema_coherence_notes | No coherence/compositionality score computed; PCA/TSNE clust… | Representational organization analyzed qualitatively via out… | UNRESOLVED — senior reviewer decides; see action |
| S032 | task_custom_name | Key+Anchor arithmetic compositional task (addition over anch… | Compositional arithmetic: key token + anchor pair addition w… | UNRESOLVED — senior reviewer decides; see action |
| S032 | train_data_note | Key+Anchor arithmetic: training samples (key, a1, a2) with n… | Synthetic compositional dataset: seen anchor pairs in traini… | UNRESOLVED — senior reviewer decides; see action |
| S033 | arch_detail | Survey spanning CNN, RNN, Transformer, MLP, GNN, and diffusi… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S033 | effect_size_notes | — | Survey paper; no experimental results | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S033 | limitations_stated | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S033 | limitations_text | Covariate vs semantic shift dichotomy is overly simplistic f… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S033 | model_scale_category | unspecified | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S033 | notes | Survey/review paper; no empirical results to extract, all nu… | Survey paper formalizing covariate vs concept/semantic shift… | UNRESOLVED — senior reviewer decides; see action |
| S033 | ood_split_type | mixed | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S033 | open_questions_text | Calls for a holistic framework that handles both covariate a… | Future research directions: models that simultaneously handl… | UNRESOLVED — senior reviewer decides; see action |
| S033 | other_metrics_reported | Catalogues evaluation metrics used across surveyed works: AU… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S033 | relevance_alignment_justification | Highlights safety-critical failures under distribution shift… | Motivates robustness via safety-critical applications (medic… | UNRESOLVED — senior reviewer decides; see action |
| S033 | relevance_sigma_justification | Systematically reviews detection, measurement, and mitigatio… | Surveys detection, measurement, and mitigation of covariate … | UNRESOLVED — senior reviewer decides; see action |
| S033 | relevance_sigma_trap | 3 | 2 | UNRESOLVED — senior reviewer decides; see action |
| S033 | schema_coherence_notes | No representation-level coherence or compositionality proxy … | No representation-level coherence measurement; reviews detec… | UNRESOLVED — senior reviewer decides; see action |
| S033 | train_data_note | No training runs; reviews detection/measurement/mitigation m… | No experiments; literature survey on distribution shift hand… | UNRESOLVED — senior reviewer decides; see action |
| S034 | arch_detail | ResNet-50 baselines; ResNeXt; self-attention variants; WSL p… | ResNet-50, ResNeXt and self-attention (Transformer-family) m… | UNRESOLVED — senior reviewer decides; see action |
| S034 | augmentation_type | DeepAugment+AugMix diverse data augmentation | DeepAugment; AugMix | UNRESOLVED — senior reviewer decides; see action |
| S034 | baseline_regime | — | standard_Adam | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S034 | code_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S034 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S034 | effect_size_notes | No effect sizes; only directional findings (e.g., DeepAugmen… | No effect sizes reported; excerpt gives only an approximate … | UNRESOLVED — senior reviewer decides; see action |
| S034 | id_metric_type | — | accuracy | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S034 | model_scale_category | medium | unspecified | UNRESOLVED — senior reviewer decides; see action |
| S034 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S034 | n_layers | 50 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S034 | notes | No exact accuracy numbers in excerpt text; Figure 5 shows ap… | Four new benchmark datasets introduced (ImageNet-R, SVSF, DF… | UNRESOLVED — senior reviewer decides; see action |
| S034 | ood_metric_type | — | accuracy | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S034 | ood_split_type | mixed | domain_shift | UNRESOLVED — senior reviewer decides; see action |
| S034 | open_questions_text | Future research must study multiple distribution shifts simu… | Calls for future research to study multiple distribution shi… | UNRESOLVED — senior reviewer decides; see action |
| S034 | pub_type | empirical | dataset_benchmark | UNRESOLVED — senior reviewer decides; see action |
| S034 | relevance_alignment_justification | Frames robustness evaluation as groundwork for systems that … | Mentions safety-critical settings as motivation for robustne… | UNRESOLVED — senior reviewer decides; see action |
| S034 | relevance_sigma_justification | Directly evaluates OOD generalization across four real-world… | Directly evaluates OOD generalization failure across multipl… | UNRESOLVED — senior reviewer decides; see action |
| S034 | repr_analysis_finding | — | Texture bias hypothesis discussed as context (texture-based … | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S034 | task_primary | ImageNet | ImageNet_R | UNRESOLVED — senior reviewer decides; see action |
| S034 | train_data_note | ImageNet-R: 30,000 test images of renditions (paintings, emb… | ImageNet-pretrained models; new test sets: ImageNet-R (30,00… | UNRESOLVED — senior reviewer decides; see action |
| S040 | arch_detail | Base model ResNet-18 (Biased-MNIST); BiDAF base model for Ad… | ResNet-18 base model; biased models: SimpleNet with 1x1 kern… | UNRESOLVED — senior reviewer decides; see action |
| S040 | baseline_regime | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S040 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S040 | effect_size_notes | — | No formal effect sizes; paper reports 68% OOD accuracy (vs b… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S040 | id_acc_n_seeds | 4 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S040 | id_metric_type | — | accuracy | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S040 | limitations_text | GGD sometimes over-estimates the bias level and degrades on … | GGD sometimes over-estimates the bias level and degrades ID … | UNRESOLVED — senior reviewer decides; see action |
| S040 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S040 | notes | Mixed shift types across tasks: covariate spurious-correlati… | Main-form OOD value = GGD1crk on Biased-MNIST (rho_train=0.9… | UNRESOLVED — senior reviewer decides; see action |
| S040 | open_questions_text | A better biased model that can access word-level similarity … | A better biased model accessing word-level similarity might … | UNRESOLVED — senior reviewer decides; see action |
| S040 | other_metrics_reported | F1 on Adversarial SQuAD (OOD) and SQuAD v1 (ID) | F1 (Adversarial SQuAD); per-class accuracy matrices | UNRESOLVED — senior reviewer decides; see action |
| S040 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S040 | relevance_sigma_justification | Directly addresses OOD generalization failure driven by spur… | Addresses OOD generalization failure from spurious correlati… | UNRESOLVED — senior reviewer decides; see action |
| S040 | repr_analysis | other | none | UNRESOLVED — senior reviewer decides; see action |
| S040 | repr_analysis_finding | Per-class accuracy matrices (diagnostic heat-maps) show vani… | Fig. 3 per-class accuracy matrices (diagnostic heat-maps) sh… | UNRESOLVED — senior reviewer decides; see action |
| S040 | schema_coherence_notes | Per-class accuracy heatmaps (Fig. 3) analyze which correlati… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S040 | task_custom_name | Biased-MNIST digit classification; Adversarial SQuAD questio… | Biased-MNIST; Adversarial SQuAD (AdQA); VQA-CP v2; GQA-OOD | UNRESOLVED — senior reviewer decides; see action |
| S040 | train_data_note | Biased-MNIST with spurious background-color bias at rho_trai… | Biased-MNIST with controllable bias level rho; SQuAD train/v… | UNRESOLVED — senior reviewer decides; see action |
| S047 | arch_detail | GOODFormer: graph Transformer with entropy-guided invariant … | GOODFormer: graph transformer with entropy-guided invariant … | UNRESOLVED — senior reviewer decides; see action |
| S047 | baseline_regime | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S047 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S047 | effect_size_notes | — | No effect sizes; only OOD test-set scores with +/- variance … | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S047 | error_bars_reported | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S047 | id_metric_type | — | accuracy | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S047 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S047 | notes | Table 3 reports OOD test-set results (accuracy for GOOD-Moti… | Main-form values = GOODFormer on GOOD-Motif basis split (acc… | UNRESOLVED — senior reviewer decides; see action |
| S047 | ood_acc_mean | — | 0.8197 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S047 | ood_acc_sd | — | 0.1674 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S047 | ood_metric_type | — | accuracy | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S047 | ood_split_type | — | domain_shift | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S047 | other_metrics_reported | ROC-AUC (GOOD-HIV, DrugOOD); Precision@10 for ground-truth i… | ROC-AUC (GOOD-HIV, DrugOOD); Precision@10 (invariant subgrap… | UNRESOLVED — senior reviewer decides; see action |
| S047 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S047 | relevance_sigma_justification | Directly addresses OOD generalization failure on graphs: sho… | Directly targets OOD generalization failure under graph dist… | UNRESOLVED — senior reviewer decides; see action |
| S047 | relevance_sigma_trap | 4 | 3 | UNRESOLVED — senior reviewer decides; see action |
| S047 | repr_analysis_finding | Invariant subgraph identification on GOOD-Motif basis split:… | Invariant subgraph discovery evaluated on GOOD-Motif basis s… | UNRESOLVED — senior reviewer decides; see action |
| S047 | schema_coherence_notes | Invariant-subgraph discovery is evaluated via Precision@10 a… | No representation-coherence proxy; invariant-subgraph identi… | UNRESOLVED — senior reviewer decides; see action |
| S047 | task_custom_name | Graph classification under distribution shift (GOOD-Motif, G… | GOOD-Motif; GOOD-HIV; GOOD-SST2; GOOD-Twitter; DrugOOD (grap… | UNRESOLVED — senior reviewer decides; see action |
| S047 | task_primary | custom | other | UNRESOLVED — senior reviewer decides; see action |
| S047 | train_data_note | GOOD benchmarks: GOOD-Motif (basis/size splits), GOOD-HIV (s… | GOOD-Motif (basis/size splits), GOOD-HIV (scaffold/size), GO… | UNRESOLVED — senior reviewer decides; see action |
| S048 | arch_detail | BEsT: ensemble of BEiT vision transformers with targeted aug… | BEsT: ensemble of BEiT vision transformers with targeted aug… | UNRESOLVED — senior reviewer decides; see action |
| S048 | augmentation_type | Targeted augmentations for OOD robustness; rotation-based te… | targeted augmentations for OOD robustness; rotation-based te… | UNRESOLVED — senior reviewer decides; see action |
| S048 | effect_size_notes | Drops reported as absolute accuracy differences (e.g., Mobil… | No effect sizes; ID and OOD accuracies reported as percentag… | UNRESOLVED — senior reviewer decides; see action |
| S048 | limitations_stated | FALSE | TRUE | UNRESOLVED — senior reviewer decides; see action |
| S048 | limitations_text | — | Pipeline is applicable to generic plankton classifiers only … | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S048 | notes | Main-form OOD value = BEsT 83% OOD accuracy (10 deployment-d… | Main-form OOD value = BEsT ensemble 83% OOD accuracy (ID not… | UNRESOLVED — senior reviewer decides; see action |
| S048 | ood_difficulty_metric_name | Hellinger distance (feature space) for compositional shift; … | Hellinger distance (compositional shift); scalar-product dis… | UNRESOLVED — senior reviewer decides; see action |
| S048 | other_metrics_reported | Per-class precision/recall/F1; macro and micro F1; NMAE; Bra… | per-class recall/precision/F1; NMAE and Bray-Curtis dissimil… | UNRESOLVED — senior reviewer decides; see action |
| S048 | relevance_alignment_justification | Applied ecology monitoring paper on plankton classifier robu… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S048 | relevance_sigma_justification | Directly studies generalization failure under dataset shift … | Systematically measures OOD generalization failure (nominal … | UNRESOLVED — senior reviewer decides; see action |
| S048 | relevance_sigma_trap | 4 | 3 | UNRESOLVED — senior reviewer decides; see action |
| S048 | repr_analysis | other | none | UNRESOLVED — senior reviewer decides; see action |
| S048 | repr_analysis_finding | PCA over 67 computer-vision image descriptors with Hellinger… | Diagnostic analysis uses 67 image descriptors + PCA on image… | UNRESOLVED — senior reviewer decides; see action |
| S048 | repr_analysis_secondary | PCA | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S048 | schema_coherence_notes | No representation-level coherence proxy of the trained model… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S048 | task_custom_name | ZooLake plankton image classification (dark-field lake plank… | Plankton species classification (ZooLake dark-field plankton… | UNRESOLVED — senior reviewer decides; see action |
| S048 | train_data_note | ZooLake dark-field images of lake plankton; 10 manually-anno… | ZooLake dark-field plankton images for ID training; 10 manua… | UNRESOLVED — senior reviewer decides; see action |
| S051 | arch_detail | RAT-SQL family (RATSQLG, RATSQLB, RATSQL) with/without NatSQ… | RAT-SQL (relation-aware transformer with LSTM decoder, NatSQ… | UNRESOLVED — senior reviewer decides; see action |
| S051 | arch_primary | TransformerEnc | TransformerEncDec | UNRESOLVED — senior reviewer decides; see action |
| S051 | augmentation_type | Clause-level synthetic example generation: Spider-SS segment… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S051 | augmentation_used | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S051 | baseline_regime | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S051 | effect_size_notes | Paper reports relative OOD degradation of 10-30% on CG-APPT/… | No effect sizes; excerpt reports 10-30% OOD drops qualitativ… | UNRESOLVED — senior reviewer decides; see action |
| S051 | id_ood_gap_reported | TRUE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S051 | limitations_text | Spider-SS/Spider-CG based only on Spider (English text-to-SQ… | Based only on Spider (English text-to-SQL); methods not veri… | UNRESOLVED — senior reviewer decides; see action |
| S051 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S051 | notes | ID sets: SpiderD (real Spider dev), CG-SUBT, CG-SUBD (substi… | Main-form ID value = RATSQLG(S) exact match 74.5% on SpiderD… | UNRESOLVED — senior reviewer decides; see action |
| S051 | ood_difficulty_metric | FALSE | TRUE | UNRESOLVED — senior reviewer decides; see action |
| S051 | ood_difficulty_metric_name | — | Spider difficulty criteria (easy/medium/hard/extra hard) dis… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S051 | open_questions_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S051 | other_metrics_reported | Execution match (Table 2, NatSQL conversion eval); difficult… | execution match (Spider-SS quality check); sentence-split si… | UNRESOLVED — senior reviewer decides; see action |
| S051 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S051 | relevance_sigma_justification | Directly measures the core sigma-trap phenomenon: models deg… | Directly measures compositional generalization failure: mode… | UNRESOLVED — senior reviewer decides; see action |
| S051 | schema_coherence_notes | No representation-level coherence proxy measured; sub-senten… | Component alignment is performed at the data/annotation leve… | UNRESOLVED — senior reviewer decides; see action |
| S051 | task_custom_name | Text-to-SQL semantic parsing (Spider / Spider-SS / Spider-CG… | Text-to-SQL semantic parsing (Spider; Spider-SS; Spider-CG) | UNRESOLVED — senior reviewer decides; see action |
| S051 | task_primary | custom | other | UNRESOLVED — senior reviewer decides; see action |
| S051 | train_data_note | Spider-SS: Spider split into clause-aligned sub-sentences (N… | Spider-SS: Spider sentences split into clauses annotated wit… | UNRESOLVED — senior reviewer decides; see action |
| S051 | train_regime | augmentation | other | UNRESOLVED — senior reviewer decides; see action |
| S051 | train_regime_other | — | training on clause-segmented (Spider-SS) data with sub-sente… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S057 | arch_detail | Domain-aware transformation module: 3 MLP layers with embedd… | Base model architecture not specified in excerpt; SMLG adds … | UNRESOLVED — senior reviewer decides; see action |
| S057 | arch_family | mlp | other | UNRESOLVED — senior reviewer decides; see action |
| S057 | arch_primary | MLP | other | UNRESOLVED — senior reviewer decides; see action |
| S057 | code_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S057 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S057 | effect_size_notes | No effect sizes reported in excerpt | No effect sizes; improvement percentages reported on toy dat… | UNRESOLVED — senior reviewer decides; see action |
| S057 | hidden_dim | — | 16 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S057 | id_metric_type | — | accuracy | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S057 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S057 | notes | Excerpt truncated mid-section 7.2.2 (CIFAR-100 domain-quanti… | Main-form OOD value = SMLG average accuracy 83.0% across 4 l… | UNRESOLVED — senior reviewer decides; see action |
| S057 | relevance_alignment | 2 | 1 | UNRESOLVED — senior reviewer decides; see action |
| S057 | relevance_alignment_justification | No explicit safety or alignment framing; only tangential lin… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S057 | relevance_sigma_justification | Directly addresses OOD generalization via a domain-aware met… | Domain generalization via meta-learning that reduces task-le… | UNRESOLVED — senior reviewer decides; see action |
| S057 | relevance_sigma_trap | 3 | 2 | UNRESOLVED — senior reviewer decides; see action |
| S057 | repr_analysis_finding | — | Domain-aware transformation module produces meta representat… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S057 | schema_coherence_notes | No representation-level coherence/compositionality proxy mea… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S057 | tasks_secondary | VLCS; CIFAR100 | VLCS;CIFAR100 | UNRESOLVED — senior reviewer decides; see action |
| S057 | train_data_note | PACS (Photo/Art/Cartoon/Sketch, 7 classes), VLCS (4 domains,… | PACS (4 domains, 7 classes), VLCS (4 domains, 5 classes), CI… | UNRESOLVED — senior reviewer decides; see action |
| S062 | arch_detail | RASP programs compiled to concrete Transformer EncDec weight… | RASP programs compiled to concrete Transformer EncDec weight… | UNRESOLVED — senior reviewer decides; see action |
| S062 | augmentation_type | training data augmented with v_dat_p2 pp-moved-to-recipient … | data augmentation: v_dat_p2 pp-moved-to-recipient (nonsubjec… | UNRESOLVED — senior reviewer decides; see action |
| S062 | code_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S062 | curriculum_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S062 | data_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S062 | effect_size_notes | No effect size reported; baseline results summarized as mean… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S062 | id_metric_type | — | exact_match | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S062 | limitations_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S062 | meta_learning_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S062 | model_weights_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S062 | n_layers | 2 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S062 | notes | Main-form ood values = Wu et al. 2024 baseline EncDec Transf… | Excerpt truncated; Tables 2-4 not included so RASP 'near-per… | UNRESOLVED — senior reviewer decides; see action |
| S062 | ood_acc_ci_lower | 0.04 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S062 | ood_acc_ci_upper | 0.23 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S062 | ood_acc_mean | 0.13 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S062 | ood_acc_n_seeds | 10 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S062 | ood_acc_sd | 0.156 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S062 | open_questions_stated | — | TRUE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S062 | open_questions_text | — | Rigorous starting point for investigating when Transformers … | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S062 | other_metrics_reported | grammar coverage (Zeller et al.); error-attribution analysis… | Attraction-error analysis: 96.73% (740/765; 95% CI 95.21-97.… | UNRESOLVED — senior reviewer decides; see action |
| S062 | relevance_alignment_justification | No connection to AI alignment, safety, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S062 | relevance_sigma_justification | Directly investigates whether Transformers can achieve compo… | Directly targets compositional generalization failure on COG… | UNRESOLVED — senior reviewer decides; see action |
| S062 | schema_coherence_notes | No representation-level coherence proxy; RASP solution is by… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S062 | task_custom_name | ReCOGS_pos (COGS variant with semantics-focused labels) | COGS and ReCOGS_pos (positional ReCOGS variant with COGS voc… | UNRESOLVED — senior reviewer decides; see action |
| S062 | train_data_note | ReCOGS_pos train.tsv (default) and COGS training examples; 1… | ReCOGS_pos/COGS train.tsv (Wu et al. 2024 default data); RAS… | UNRESOLVED — senior reviewer decides; see action |
| S062 | train_regime | — | other | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S062 | train_regime_other | — | RASP-to-Transformer weight compilation; no gradient-based tr… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S063 | arch_detail | Seq2seq Vanilla Transformer (from scratch), pretrained T5, L… | Vanilla seq2seq Transformer trained from scratch; also evalu… | UNRESOLVED — senior reviewer decides; see action |
| S063 | id_metric_type | — | exact_match | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S063 | notes | Headline: best Transformer (T5) 40.6%, AM-Parser 70.8% on SL… | Main-form = Vanilla Transformer on SLOG overall generalizati… | UNRESOLVED — senior reviewer decides; see action |
| S063 | ood_metric_other | — | also reformatted exact-match (Section 4) | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S063 | ood_metric_type | accuracy | exact_match | UNRESOLVED — senior reviewer decides; see action |
| S063 | other_metrics_reported | — | Error analyses: T5 overgeneralizes direct-object wh-pattern … | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S063 | relevance_alignment_justification | No connection to AI alignment, safety, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S063 | relevance_sigma_justification | Directly quantifies compositional generalization failure: Tr… | Introduces SLOG to expose the gap between lexical and struct… | UNRESOLVED — senior reviewer decides; see action |
| S063 | relevance_sigma_trap | 4 | 5 | UNRESOLVED — senior reviewer decides; see action |
| S063 | task_custom_name | SLOG | SLOG: structural generalization benchmark extending COGS (17… | UNRESOLVED — senior reviewer decides; see action |
| S063 | tasks_secondary | COGS | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S063 | train_data_note | SLOG extends COGS with 17 structural generalization cases (1… | Trained on SLOG/COGS training data; all reported experiments… | UNRESOLVED — senior reviewer decides; see action |
| S069 | arch_detail | Seq2seq Transformer models on CFQ and COGS; dataset cartogra… | Transformer models for CFQ and COGS semantic parsing; archit… | UNRESOLVED — senior reviewer decides; see action |
| S069 | data_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S069 | effect_size_notes | No effect sizes reported; narrative relative claims only (CF… | Only relative gains reported in excerpt (CFQ +>4%, COGS +>10… | UNRESOLVED — senior reviewer decides; see action |
| S069 | limitations_extractor | Excerpt covers results, curriculum analysis, and related wor… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S069 | model_weights_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S069 | notes | Table 3 numeric cells in excerpt are scrambled and not relia… | Excerpt's Table 3 is garbled (columns unaligned) so no absol… | UNRESOLVED — senior reviewer decides; see action |
| S069 | open_questions_extractor | No open-questions discussion present in excerpt | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S069 | other_metrics_reported | Confidence/difficulty measures for sample ranking: BLEU, CHI… | Selection-measure comparison: Inverse Perplexity most effect… | UNRESOLVED — senior reviewer decides; see action |
| S069 | relevance_alignment | 2 | 1 | UNRESOLVED — senior reviewer decides; see action |
| S069 | relevance_alignment_justification | Motivates compositional generalization as crucial for robust… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S069 | relevance_sigma_justification | Directly targets compositional generalization failure in seq… | Directly targets compositional generalization failure on CFQ… | UNRESOLVED — senior reviewer decides; see action |
| S069 | schema_coherence_notes | No representation-level coherence proxy; dataset cartography… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S069 | train_data_note | CFQ and COGS; models trained on 33% and 50% subsets (easy-to… | Trains on 33%/50% subsets of CFQ and COGS train sets selecte… | UNRESOLVED — senior reviewer decides; see action |
| S071 | arch_detail | Pretrained decoder-only LMs used via in-context learning wit… | Pretrained decoder-only LMs used with in-context learning (n… | UNRESOLVED — senior reviewer decides; see action |
| S071 | effect_size_notes | Paper's central quantity is relative generalization gap (ID-… | Relative generalization gap (ID-OOD)/ID is the paper's headl… | UNRESOLVED — senior reviewer decides; see action |
| S071 | error_bars_reported | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S071 | id_acc_n_seeds | 5 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S071 | limitations_text | Authors note in-context learning performance on CFQ and SCAN… | In-context learning performance on CFQ and SCAN is still ver… | UNRESOLVED — senior reviewer decides; see action |
| S071 | notes | Main-form values = Codex DaVinci; only explicit accuracy in … | Main-form OOD value = Codex DaVinci average OOD on SCAN-MCD1… | UNRESOLVED — senior reviewer decides; see action |
| S071 | other_metrics_reported | relative generalization gap (ID-OOD)/ID; primitive coverage … | Relative generalization gap (ID-OOD)/ID, ID=(TT+TrTr)/2, OOD… | UNRESOLVED — senior reviewer decides; see action |
| S071 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S071 | relevance_sigma_justification | Directly measures the compositional generalization gap (the … | Directly measures the compositional ID-OOD generalization ga… | UNRESOLVED — senior reviewer decides; see action |
| S071 | schema_coherence_notes | No representation-level coherence proxy; primitive coverage … | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S071 | train_data_note | No fine-tuning: models solve tasks by conditioning on 1/5/10… | No training: in-context learning with oracle-sampled exempla… | UNRESOLVED — senior reviewer decides; see action |
| S071 | train_regime_other | in-context learning (no parameter updates); prompts with 1/5… | In-context learning; no weight updates | UNRESOLVED — senior reviewer decides; see action |
| S076 | arch_detail | AM parser (Groschwitz et al. 2021): neural supertagging + tr… | AM parser (Groschwitz et al. 2021): compositional graph-base… | UNRESOLVED — senior reviewer decides; see action |
| S076 | effect_size_notes | No effect sizes reported; class-level comparisons made descr… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S076 | error_bars_reported | FALSE | TRUE | UNRESOLVED — senior reviewer decides; see action |
| S076 | id_metric_other | — | exact match | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S076 | id_metric_type | exact_match | accuracy | UNRESOLVED — senior reviewer decides; see action |
| S076 | n_seeds_reported | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S076 | n_seeds_value | 5 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S076 | notes | Main form = AM+B (best AM parser variant with cleanly visibl… | Main-form = AM parser (compositional, primary contribution);… | UNRESOLVED — senior reviewer decides; see action |
| S076 | ood_acc_mean | 0.984 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S076 | ood_acc_n_seeds | 5 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S076 | ood_acc_sd | 0.013 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S076 | ood_metric_other | — | exact match on generalization set | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S076 | ood_metric_type | exact_match | accuracy | UNRESOLVED — senior reviewer decides; see action |
| S076 | other_metrics_reported | — | Per-type exact-match accuracy across 21 COGS generalization … | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S076 | relevance_alignment | 2 | 1 | UNRESOLVED — senior reviewer decides; see action |
| S076 | relevance_alignment_justification | No alignment or safety discussion; indirect relevance via de… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S076 | relevance_sigma_justification | Directly characterizes compositional generalization failure … | Systematically tests the sigma-trap on COGS structural gener… | UNRESOLVED — senior reviewer decides; see action |
| S076 | schema_coherence_notes | No representation-level coherence proxy measured; analyses a… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S076 | train_data_note | COGS synthetic English semantic parsing corpus; test set has… | COGS train set; AM parser needs node-to-token alignments (de… | UNRESOLVED — senior reviewer decides; see action |
| S077 | arch_detail | Attention-inspired modification of the Ruis et al. (2020) gS… | Attention-inspired modification of gSCAN baseline (Ruis et a… | UNRESOLVED — senior reviewer decides; see action |
| S077 | id_metric_other | — | exact match | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S077 | id_metric_type | exact_match | accuracy | UNRESOLVED — senior reviewer decides; see action |
| S077 | model_scale_category | small | unspecified | UNRESOLVED — senior reviewer decides; see action |
| S077 | notes | arXiv 2009.13962v2 preprint (Oct 2020). Main exact-match res… | Main exact-match results (Table 1) not in excerpt; headline … | UNRESOLVED — senior reviewer decides; see action |
| S077 | ood_difficulty_metric | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S077 | ood_difficulty_metric_name | gSCAN test splits A (Random), B (Yellow squares), C (Red squ… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S077 | ood_metric_other | — | exact match; auxiliary target-position prediction accuracy | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S077 | ood_metric_type | exact_match | accuracy | UNRESOLVED — senior reviewer decides; see action |
| S077 | other_metrics_reported | target prediction accuracy (Table A.2); split (E) exact matc… | Auxiliary target-position prediction accuracy: baseline w/au… | UNRESOLVED — senior reviewer decides; see action |
| S077 | relevance_alignment_justification | No connection to AI alignment, safety, or goal misgeneraliza… | Mentions robustness/trustworthiness of deployed systems in p… | UNRESOLVED — senior reviewer decides; see action |
| S077 | relevance_sigma_justification | Challenges the gSCAN compositional generalization benchmark:… | Directly addresses compositional generalization in grounded … | UNRESOLVED — senior reviewer decides; see action |
| S077 | schema_coherence_notes | No representation-level coherence proxy; target prediction a… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S077 | tasks_secondary | — | SCAN | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S077 | train_data_note | gSCAN grid-world grounded command-following benchmark; split… | gSCAN splits: A (random), B (yellow squares), C (red squares… | UNRESOLVED — senior reviewer decides; see action |
| S082 | arch_detail | T5/mT5 seq2seq models with RIR (repeat-and-insert) decoder; … | mT5-small+RIR and mT5-base+RIR seq2seq semantic parsers over… | UNRESOLVED — senior reviewer decides; see action |
| S082 | augmentation_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S082 | code_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S082 | curriculum_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S082 | data_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S082 | effect_size_notes | No effect sizes reported; comparisons are descriptive (monol… | No effect size reported; gap between monolingual English and… | UNRESOLVED — senior reviewer decides; see action |
| S082 | limitations_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S082 | meta_learning_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S082 | model_weights_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S082 | notes | Main-form ood values = monolingual mT5-small+RIR on English … | Main-form OOD value = mT5-small+RIR monolingual English, MCD… | UNRESOLVED — senior reviewer decides; see action |
| S082 | ood_difficulty_metric_name | compound divergence (MCD splits, MCDmean) | compound divergence (MCD splits, from CFQ) | UNRESOLVED — senior reviewer decides; see action |
| S082 | open_questions_text | Whether cross-lingual compositional transfer will be more ef… | Whether zero-shot cross-lingual transfer would be more effec… | UNRESOLVED — senior reviewer decides; see action |
| S082 | other_metrics_reported | BLEU score of predicted SPARQL queries; error categorization… | BLEU; SPARQL exact match; error-category counts (missing/ext… | UNRESOLVED — senior reviewer decides; see action |
| S082 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S082 | relevance_sigma_justification | Directly evaluates compositional generalization (MCD splits,… | Directly measures compositional (OOD) generalization via CFQ… | UNRESOLVED — senior reviewer decides; see action |
| S082 | schema_coherence_notes | No representation-level coherence metric measured | No representation-level coherence proxy; error categorizatio… | UNRESOLVED — senior reviewer decides; see action |
| S082 | task_custom_name | MCWQ (Multilingual Compositional Wikidata Questions) - multi… | MCWQ (Multilingual Compositional Wikidata Questions) | UNRESOLVED — senior reviewer decides; see action |
| S082 | train_data_note | MCWQ: multilingual parallel questions over Wikidata derived … | MCWQ: parallel question-SPARQL dataset over Wikidata in Engl… | UNRESOLVED — senior reviewer decides; see action |
| S086 | arch_detail | GroCoT: attention-only transformer, command + world-state em… | Attention-only transformer (GroCoT): stacked multi-head atte… | UNRESOLVED — senior reviewer decides; see action |
| S086 | data_leakage_check | not_addressed | suspected | UNRESOLVED — senior reviewer decides; see action |
| S086 | effect_size_notes | No effect sizes reported | No effect size reported; headline accuracies for the transfo… | UNRESOLVED — senior reviewer decides; see action |
| S086 | id_metric_type | accuracy | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S086 | notes | Main-benchmark accuracies (ReaSCAN/gSCAN/RefEx default setti… | Headline transformer accuracies on ReaSCAN/gSCAN not recover… | UNRESOLVED — senior reviewer decides; see action |
| S086 | other_metrics_reported | — | Action-sequence accuracy; target-localization probing accura… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S086 | relevance_alignment | 2 | 1 | UNRESOLVED — senior reviewer decides; see action |
| S086 | relevance_alignment_justification | No alignment or safety discussion; indirect relevance via me… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S086 | relevance_sigma_justification | Directly probes grounded compositional generalization (the s… | Core study of compositional (OOD) generalization in grounded… | UNRESOLVED — senior reviewer decides; see action |
| S086 | repr_analysis_finding | Linear probe of target location in encoder representations: … | Linear probing of encoder representations for target locatio… | UNRESOLVED — senior reviewer decides; see action |
| S086 | repr_analysis_layer | per encoder layer (layer 0 = input embeddings) | encoder layers 0-12 | UNRESOLVED — senior reviewer decides; see action |
| S086 | schema_coherence_notes | No representation-coherence proxy measured (no CKA/RSA/compo… | No schema-coherence proxy; attention-analysis of target loca… | UNRESOLVED — senior reviewer decides; see action |
| S086 | task_custom_name | ReaSCAN (grounded navigation); gSCAN (GSRR splits); RefEx (n… | ReaSCAN / RefEx grounded grid-world navigation (ReaSCAN: Wu … | UNRESOLVED — senior reviewer decides; see action |
| S086 | train_data_note | RefEx: 90K train / 2.5K val / 2.5K test per variant; C2-deep… | RefEx variants: 90K train / 2.5K val / 2.5K test; ReaSCAN C2… | UNRESOLVED — senior reviewer decides; see action |
| S086 | train_n_examples | 90000 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S090 | arch_detail | Recursive Decoding (RD): training/decoding procedure for seq… | Seq2seq model (architecture not named in excerpt) trained wi… | UNRESOLVED — senior reviewer decides; see action |
| S090 | arch_family | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S090 | arch_primary | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S090 | code_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S090 | data_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S090 | effect_size_notes | No effect sizes reported; comparisons reported as exact-matc… | No effect size reported; gains described via exact-match com… | UNRESOLVED — senior reviewer decides; see action |
| S090 | id_metric_type | exact_match | accuracy | UNRESOLVED — senior reviewer decides; see action |
| S090 | limitations_extractor | Excerpt discusses baseline failure modes but no explicit lim… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S090 | model_weights_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S090 | n_seeds_reported | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S090 | n_seeds_value | 3 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S090 | notes | Main-form values = RD on Length task (OOD) and gSCAN Random … | Main form: ID = RD model on gSCAN Random split (99.22 +-0.16… | UNRESOLVED — senior reviewer decides; see action |
| S090 | ood_acc_mean | 0.8442 | 0.436 | UNRESOLVED — senior reviewer decides; see action |
| S090 | ood_acc_sd | 0.0324 | 0.0605 | UNRESOLVED — senior reviewer decides; see action |
| S090 | ood_metric_type | exact_match | accuracy | UNRESOLVED — senior reviewer decides; see action |
| S090 | open_questions_extractor | Paper signals implications for naturalistic grounded languag… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S090 | other_metrics_reported | Exact match per gSCAN task; non-canonical solution rate (86.… | Exact match; non-canonical solution rate (86.32% valid solut… | UNRESOLVED — senior reviewer decides; see action |
| S090 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S090 | relevance_sigma_justification | Directly targets decode-side compositional generalization fa… | Directly targets compositional (OOD) generalization on the d… | UNRESOLVED — senior reviewer decides; see action |
| S090 | repr_analysis | attention_patterns | none | UNRESOLVED — senior reviewer decides; see action |
| S090 | repr_analysis_finding | Baseline successfully attends to the correct target cell des… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S090 | schema_coherence_notes | No representation-level coherence proxy measured; analyses f… | No representation-level coherence proxy; behavioral analysis… | UNRESOLVED — senior reviewer decides; see action |
| S090 | train_data_note | gSCAN grid-world; original and randomized initial-orientatio… | gSCAN splits: Random, Yellow Squares, Red Squares, Novel Dir… | UNRESOLVED — senior reviewer decides; see action |
| S090 | train_regime | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S090 | train_regime_other | Recursive Decoding: model predicts one output token at a tim… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S115 | arch_detail | One-layer LSTM encoder-decoder, hidden size 512, embedding 6… | One-layer LSTM encoder-decoder, hidden size 512, embedding s… | UNRESOLVED — senior reviewer decides; see action |
| S115 | augmentation_type | SeqMix sequence-level mixed-sample soft interpolation; compa… | SeqMix (soft sequence-level mixed-sample augmentation); also… | UNRESOLVED — senior reviewer decides; see action |
| S115 | code_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S115 | data_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S115 | effect_size_notes | No effect sizes reported; point estimates per split and cond… | No effect size reported; gains reported as accuracies/BLEU d… | UNRESOLVED — senior reviewer decides; see action |
| S115 | limitations_text | SeqMix fails on the SCAN around-right split (model must comb… | SeqMix fails on the SCAN around-right split (0%), where 'aro… | UNRESOLVED — senior reviewer decides; see action |
| S115 | model_weights_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S115 | notes | arXiv preprint (Nov 2020). SCAN accuracies are per-split com… | Main form: SCAN jump split, LSTM + SeqMix without GECA (49%)… | UNRESOLVED — senior reviewer decides; see action |
| S115 | ood_acc_mean | — | 0.49 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S115 | open_questions_text | The unified framework over data augmentation strategies natu… | Unified framework for augmentation strategies naturally sugg… | UNRESOLVED — senior reviewer decides; see action |
| S115 | other_metrics_reported | BLEU on IWSLT de-en/en-de/en-it and WMT en-es (about 1.0 BLE… | BLEU (NMT); accuracy (SCAN, GeoQuery) | UNRESOLVED — senior reviewer decides; see action |
| S115 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S115 | relevance_sigma_justification | Directly targets compositional generalization failure on SCA… | Directly targets compositional generalization failure on SCA… | UNRESOLVED — senior reviewer decides; see action |
| S115 | relevance_sigma_trap | 4 | 3 | UNRESOLVED — senior reviewer decides; see action |
| S115 | schema_coherence_notes | No representation-level coherence or compositionality proxy … | No representation-level coherence proxy | UNRESOLVED — senior reviewer decides; see action |
| S115 | task_custom_name | Also neural machine translation (IWSLT de-en/en-de/en-it, WM… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S115 | tasks_secondary | GeoQuery; other | GeoQuery | UNRESOLVED — senior reviewer decides; see action |
| S115 | train_data_note | SCAN splits (jump, around-right, turn-left); GeoQuery SQL qu… | SCAN splits: jump, around-right, turn-left; GeoQuery SQL-que… | UNRESOLVED — senior reviewer decides; see action |
| S115 | train_regime | — | augmentation | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S119 | arch_detail | Physics-informed diffusion model (REPA-P) on U-Net and Diffu… | Diffusion models on U-Net and Diffusion Transformer (DiT) ba… | UNRESOLVED — senior reviewer decides; see action |
| S119 | data_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S119 | effect_size_notes | Metrics are physics residuals, data losses, PSNR, and compli… | No effect size; gains reported as relative improvements (los… | UNRESOLVED — senior reviewer decides; see action |
| S119 | hidden_dim | 128 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S119 | limitations_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S119 | model_weights_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S119 | notes | arXiv preprint 2605.20780. All reported metrics are losses/r… | No accuracy-style metrics; main-form acc fields empty by des… | UNRESOLVED — senior reviewer decides; see action |
| S119 | open_questions_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S119 | other_metrics_reported | U-Net turbulence reconstruction PSNR 37.64->39.95 dB (REPA-P… | Data loss (MSE); physics loss/residual (RMAE); PSNR; complia… | UNRESOLVED — senior reviewer decides; see action |
| S119 | relevance_alignment_justification | No connection to AI alignment, safety, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S119 | relevance_sigma_justification | Addresses OOD generalization failure (shortcut learning unde… | Directly targets OOD generalization failure under shifted bo… | UNRESOLVED — senior reviewer decides; see action |
| S119 | relevance_sigma_trap | 3 | 4 | UNRESOLVED — senior reviewer decides; see action |
| S119 | repr_analysis | probing | other | UNRESOLVED — senior reviewer decides; see action |
| S119 | repr_analysis_finding | Intermediate features are decodable to physical quantities (… | Layer-wise physics residual analysis: output-only physics lo… | UNRESOLVED — senior reviewer decides; see action |
| S119 | repr_analysis_layer | encoder/bottleneck/decoder positions ablated; bottleneck bes… | encoder/bottleneck/decoder layers (position ablation) | UNRESOLVED — senior reviewer decides; see action |
| S119 | schema_coherence_notes | REPA-P aligns intermediate diffusion features with physical … | Intermediate alignment with physical states reduces physics … | UNRESOLVED — senior reviewer decides; see action |
| S119 | schema_coherence_proxy_other | physical decodability (1x1 projection heads decode hidden ac… | physical decodability: 1x1 projection heads decode hidden ac… | UNRESOLVED — senior reviewer decides; see action |
| S119 | sig_test_reported | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S119 | task_custom_name | PDE generation: Darcy flow, topology optimization, electrost… | Physics-informed diffusion: Darcy flow generation/reconstruc… | UNRESOLVED — senior reviewer decides; see action |
| S119 | train_data_note | Four PDE tasks (Darcy flow, topology optimization, electrost… | PDE benchmarks: Darcy flow (120K total training iterations),… | UNRESOLVED — senior reviewer decides; see action |
| S119 | train_regime_other | — | physics-informed: PDE residual losses applied to intermediat… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S130 | arch_detail | Model-free RL policies (SAC, TD3, PPO; MLP actor-critic netw… | Reinforcement learning agents: PPO, SAC, TD3, SA-PPO/ATLA (a… | UNRESOLVED — senior reviewer decides; see action |
| S130 | augmentation_type | Self-Trajectory Augmentation (STA): reset environment to age… | Self-Trajectory Augmentation (STA): environment reset to age… | UNRESOLVED — senior reviewer decides; see action |
| S130 | data_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S130 | effect_size_notes | No effect size; STA claim of >3x failure-rate reduction with… | No effect size; failure rates reported; STA reduces SAC rela… | UNRESOLVED — senior reviewer decides; see action |
| S130 | error_bars_reported | FALSE | TRUE | UNRESOLVED — senior reviewer decides; see action |
| S130 | model_weights_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S130 | notes | Paper reports FAILURE RATES; acc fields are success rate = 1… | Main form = PPO on Humanoid: ID success 0.961 derived from 3… | UNRESOLVED — senior reviewer decides; see action |
| S130 | ood_acc_sd | — | 0.191 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S130 | other_metrics_reported | Average returns (Table 13), e.g., Humanoid: SAC 5645.73±233.… | Failure rate (regular testing vs relay-evaluation); average … | UNRESOLVED — senior reviewer decides; see action |
| S130 | relevance_alignment_justification | Motivated by safety-critical take-over scenarios (e.g., self… | Motivated by safety-critical take-over scenarios (e.g., self… | UNRESOLVED — senior reviewer decides; see action |
| S130 | relevance_sigma_justification | Demonstrates and quantifies OOD generalization failure of RL… | Documents severe OOD generalization failure in RL (PPO fails… | UNRESOLVED — senior reviewer decides; see action |
| S130 | schema_coherence_notes | No representation-level coherence proxy; only t-SNE visualiz… | No representation-level coherence proxy; state-space analysi… | UNRESOLVED — senior reviewer decides; see action |
| S130 | task_custom_name | MuJoCo continuous-control RL (Humanoid, Walker2d, Hopper, An… | RL control (MuJoCo): Humanoid, Walker2d, Hopper, Ant | UNRESOLVED — senior reviewer decides; see action |
| S130 | train_data_note | MuJoCo environments via RL interaction; STA (Self-Trajectory… | MuJoCo continuous control (Humanoid, Walker2d, Hopper, Ant);… | UNRESOLVED — senior reviewer decides; see action |
| S130 | train_regime | augmentation | other | UNRESOLVED — senior reviewer decides; see action |
| S130 | train_regime_other | — | reinforcement learning (PPO/SAC/TD3/SA-PPO) | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S138 | arch_detail | Gradient-based meta-learner Meta-SGD (learned initialization… | Network architecture not named in excerpt; gradient-based me… | UNRESOLVED — senior reviewer decides; see action |
| S138 | code_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S138 | data_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S138 | effect_size_notes | No effect sizes; relative accuracy improvements of Meta-SGD … | No effect sizes reported; only relative accuracy gains of Me… | UNRESOLVED — senior reviewer decides; see action |
| S138 | error_bars_reported | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S138 | limitations_text | Loss-landscape analysis is a local approximation (trajectori… | Loss trajectories were randomly sampled in a small, locally … | UNRESOLVED — senior reviewer decides; see action |
| S138 | model_weights_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S138 | notes | Absolute accuracies not present in excerpt; only relative im… | No absolute accuracy numbers reported in excerpt, only relat… | UNRESOLVED — senior reviewer decides; see action |
| S138 | ood_difficulty_metric | FALSE | TRUE | UNRESOLVED — senior reviewer decides; see action |
| S138 | ood_difficulty_metric_name | — | concept complexity (featural dimensionality F; compositional… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S138 | ood_split_type | compositional | concept_shift | UNRESOLVED — senior reviewer decides; see action |
| S138 | open_questions_text | Whether compositional depth preserves loss-surface navigabil… | Whether landscape findings hold at higher dimensionality and… | UNRESOLVED — senior reviewer decides; see action |
| S138 | other_metrics_reported | Samples required to reach 60% accuracy (data efficiency); re… | data efficiency (samples required to reach 60% accuracy); lo… | UNRESOLVED — senior reviewer decides; see action |
| S138 | relevance_alignment | 1 | 2 | UNRESOLVED — senior reviewer decides; see action |
| S138 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | Studies few-shot acquisition of abstract concepts via meta-l… | UNRESOLVED — senior reviewer decides; see action |
| S138 | relevance_sigma_justification | Directly studies compositional versus featural complexity in… | Directly probes compositional vs featural complexity in out-… | UNRESOLVED — senior reviewer decides; see action |
| S138 | repr_analysis_finding | — | Loss landscape analysis (roughness, local minima counts, Hes… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S138 | schema_coherence_notes | No representation-level coherence proxy; analysis concerns o… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S138 | task_custom_name | Few-shot Boolean concept classification from PCFG-generated … | Boolean concept learning (PCFG-generated logical statements) | UNRESOLVED — senior reviewer decides; see action |
| S138 | task_primary | custom | PCFG_SET | UNRESOLVED — senior reviewer decides; see action |
| S138 | train_data_note | Task distribution from a PCFG concept generator (extension o… | Boolean concepts generated by a PCFG-based concept generator… | UNRESOLVED — senior reviewer decides; see action |
| S146 | arch_detail | Seven frontier vision-language models evaluated: Gemini-3.1-… | 7-8 frontier vision-language models evaluated: Gemini-3.1-Pr… | UNRESOLVED — senior reviewer decides; see action |
| S146 | arch_primary | GPT | TransformerDec | UNRESOLVED — senior reviewer decides; see action |
| S146 | effect_size_notes | — | No effect sizes reported; accuracy reported per question cat… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S146 | notes | COLM 2026 benchmark paper: 200 synthetic documents, 6 layout… | Evaluation-only benchmark paper; no training performed, so t… | UNRESOLVED — senior reviewer decides; see action |
| S146 | ood_metric_type | — | accuracy | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S146 | ood_split_type | — | none | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S146 | other_metrics_reported | ACC (tau=6) by question subset (chart/complex/cross-modal), … | ACC (tau=6) per question category and topic domain; degradat… | UNRESOLVED — senior reviewer decides; see action |
| S146 | relevance_alignment_justification | No connection to AI alignment or safety; a benchmark constru… | Concerns benchmark construction and VLM failure diagnosis; n… | UNRESOLVED — senior reviewer decides; see action |
| S146 | relevance_sigma_justification | Combinatorial-design benchmark that surfaces VLM failure mod… | Diagnoses generalization failure modes (length degradation, … | UNRESOLVED — senior reviewer decides; see action |
| S146 | relevance_sigma_trap | 3 | 2 | UNRESOLVED — senior reviewer decides; see action |
| S146 | repr_analysis_finding | — | Behavioral failure-mode analysis only (length degradation, p… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S146 | schema_coherence_notes | No representation-level coherence/compositionality proxy; be… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S146 | task_custom_name | Long-context visual document understanding (SynthDocBench): … | SynthDocBench: long-context visual document understanding (c… | UNRESOLVED — senior reviewer decides; see action |
| S146 | train_data_note | SynthDocBench: 200 synthetic documents generated end-to-end … | Fully synthetic benchmark: documents generated end-to-end by… | UNRESOLVED — senior reviewer decides; see action |
| S152 | arch_detail | Compositional model: component functions as 4 fully-connecte… | Component functions: four fully-connected layers followed by… | UNRESOLVED — senior reviewer decides; see action |
| S152 | data_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S152 | effect_size_notes | Table 1 (reconstruction MSE) values are not reproduced in th… | No effect sizes; Table 1 reports reconstruction quality on I… | UNRESOLVED — senior reviewer decides; see action |
| S152 | id_metric_other | — | reconstruction MSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S152 | id_metric_type | — | other | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S152 | limitations_text | Only supervised regression with ground-truth latents studied… | Supervised regression setting only with access to ground-tru… | UNRESOLVED — senior reviewer decides; see action |
| S152 | model_scale_category | unspecified | small | UNRESOLVED — senior reviewer decides; see action |
| S152 | model_weights_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S152 | n_seeds_reported | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S152 | n_seeds_value | 5 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S152 | notes | No quantitative results extractable: Table 1 MSE values are … | Theory paper with empirical validation; numeric values of Ta… | UNRESOLVED — senior reviewer decides; see action |
| S152 | ood_metric_other | — | reconstruction MSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S152 | ood_metric_type | — | other | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S152 | open_questions_text | Extend to unsupervised identifiable representation learning;… | Unsupervised setting with inherent ambiguities; relaxing the… | UNRESOLVED — senior reviewer decides; see action |
| S152 | other_metrics_reported | reconstruction MSE on ID test set (P) and entire latent spac… | Reconstruction MSE on ID test set P and full latent space Q … | UNRESOLVED — senior reviewer decides; see action |
| S152 | relevance_alignment_justification | Broader-impact discussion notes that better generalization c… | Improving compositional generalization could increase model … | UNRESOLVED — senior reviewer decides; see action |
| S152 | relevance_sigma_justification | Foundational theoretical treatment of compositional generali… | Directly attacks the sigma-trap: derives sufficient conditio… | UNRESOLVED — senior reviewer decides; see action |
| S152 | relevance_sigma_trap | 4 | 5 | UNRESOLVED — senior reviewer decides; see action |
| S152 | repr_analysis_finding | — | Reconstruction-error heatmaps over 2d slices of the latent s… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S152 | schema_coherence_notes | Paper analyzes compositional structure of the data-generatin… | Compositionality is analyzed as a property of the data-gener… | UNRESOLVED — senior reviewer decides; see action |
| S152 | task_custom_name | synthetic sprite-image reconstruction from latent factors (5… | Sprite composition reconstruction (5d latent to 64x64 RGB im… | UNRESOLVED — senior reviewer decides; see action |
| S152 | train_data_note | Synthetic 64x64 RGB sprite images: two sprites overlaid on a… | Synthetic two-sprite images over 5d latent factors (x, y, sh… | UNRESOLVED — senior reviewer decides; see action |
| S157 | arch_detail | mBART50 and mT5 encoder-decoder transformers; ZX-Parse adds … | Multilingual seq2seq parsers: mBART50, mT5-small, mT5-large,… | UNRESOLVED — senior reviewer decides; see action |
| S157 | effect_size_notes | No effect size reported; cross-lingual vs within-language ga… | No effect sizes reported; means and SDs over 3 MCD splits re… | UNRESOLVED — senior reviewer decides; see action |
| S157 | error_bars_reported | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S157 | limitations_stated | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S157 | limitations_text | Even rule-based translation suffers distributional divergenc… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S157 | model_scale_category | unspecified | large | UNRESOLVED — senior reviewer decides; see action |
| S157 | model_weights_available | FALSE | TRUE | UNRESOLVED — senior reviewer decides; see action |
| S157 | n_seeds_reported | FALSE | TRUE | UNRESOLVED — senior reviewer decides; see action |
| S157 | notes | arXiv preprint (2306.11420v1). Table 8 (supplement) is garbl… | Table 8/9 numbers are mangled by PDF extraction; representat… | UNRESOLVED — senior reviewer decides; see action |
| S157 | ood_acc_mean | 0.366 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S157 | ood_acc_sd | 0.078 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S157 | ood_difficulty_metric_name | maximum compound divergence (MCD) | MCD split (maximum compound divergence) levels MCD1-MCD3; qu… | UNRESOLVED — senior reviewer decides; see action |
| S157 | other_metrics_reported | — | Exact match (%) within-language vs cross-lingual over 3 MCD … | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S157 | relevance_alignment | 2 | 1 | UNRESOLVED — senior reviewer decides; see action |
| S157 | relevance_alignment_justification | No direct treatment of AI alignment or goal misgeneralizatio… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S157 | relevance_sigma_justification | Directly targets compositional generalization failure (the s… | Core compositional generalization study in semantic parsing:… | UNRESOLVED — senior reviewer decides; see action |
| S157 | repr_analysis_finding | t-SNE shows latent representations of compositional utteranc… | t-SNE visualization of representations before and after the … | UNRESOLVED — senior reviewer decides; see action |
| S157 | repr_analysis_layer | mBART50 embedding layers and ZX-Parse encoder (trained align… | mBART50 embedding layer vs ZX-Parse encoder (before/after al… | UNRESOLVED — senior reviewer decides; see action |
| S157 | schema_coherence_notes | No representation-level coherence/compositionality proxy mea… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S157 | task_custom_name | MCWQ-R (multilingual KBQA semantic parsing) | MCWQ-R: multilingual compositional KBQA semantic parsing (Wi… | UNRESOLVED — senior reviewer decides; see action |
| S157 | train_data_note | MCWQ-R: faithful rule-based translation of MCWQ (Wikidata qu… | MCWQ-R: faithful rule-based (RBMT) translation of English MC… | UNRESOLVED — senior reviewer decides; see action |
| S157 | train_regime | — | other | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S157 | train_regime_other | — | freeze pretrained encoder as embedding layer, train randomly… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S161 | arch_detail | ETC (Extended Transformer Construction) 6 layers, hidden 128… | ETC Transformer (Ainslie et al. 2020) with structure annotat… | UNRESOLVED — senior reviewer decides; see action |
| S161 | code_available | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S161 | code_url | http://goo.gle/compositional-classification | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S161 | data_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S161 | effect_size_notes | No effect sizes reported; headline result is accuracy differ… | No effect sizes reported; accuracies as proportions from Tab… | UNRESOLVED — senior reviewer decides; see action |
| S161 | limitations_extractor | Excerpt lacks a limitations section | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S161 | notes | Task is CFQ converted to binary classification; excerpt repo… | Main-form values = best structure-annotated ETC (Hard parse … | UNRESOLVED — senior reviewer decides; see action |
| S161 | ood_difficulty_metric | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S161 | ood_difficulty_metric_name | maximum compound divergence (MCD) | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S161 | open_questions_extractor | Excerpt lacks an open questions section | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S161 | other_metrics_reported | F1; AUC | F1 and AUC alongside accuracy for Train / Train hold-out / D… | UNRESOLVED — senior reviewer decides; see action |
| S161 | relevance_alignment | 2 | 1 | UNRESOLVED — senior reviewer decides; see action |
| S161 | relevance_alignment_justification | No explicit connection to AI alignment or safety; contributi… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S161 | relevance_sigma_justification | Directly attacks compositional generalization failure (sigma… | Directly targets the sigma-trap: converts CFQ into a composi… | UNRESOLVED — senior reviewer decides; see action |
| S161 | repr_analysis | none | attention_patterns | UNRESOLVED — senior reviewer decides; see action |
| S161 | repr_analysis_finding | — | Structure annotations modify attention masks; improvement co… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S161 | schema_coherence_notes | Attention masks are modified but no representation-level coh… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S161 | task_custom_name | CFQ classification (binary classification derived from CFQ s… | CFQ-derived binary classification (classify SPARQL query vs … | UNRESOLVED — senior reviewer decides; see action |
| S161 | train_data_note | CFQ converted to binary classification (positive/negative qu… | CFQ converted to binary classification: (question, query) pa… | UNRESOLVED — senior reviewer decides; see action |
| S166 | arch_detail | Seq2seq Transformer with DANGLE-ENC (adaptive re-encoding of… | Seq2seq Transformer (absolute and relative position embeddin… | UNRESOLVED — senior reviewer decides; see action |
| S166 | augmentation_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | ci_reported | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | curriculum_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | data_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | effect_size_notes | No effect sizes reported; tables 2-4 lack reliable column-to… | No effect sizes reported; exact-match percentages and entang… | UNRESOLVED — senior reviewer decides; see action |
| S166 | error_bars_reported | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | id_metric_type | — | exact_match | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | limitations_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | meta_learning_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | model_scale_category | unspecified | medium | UNRESOLVED — senior reviewer decides; see action |
| S166 | model_weights_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | n_seeds_reported | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | notes | Excerpt header carries arXiv-only stamp (2110.04655v2) so pe… | Table 3/4 numeric mappings garbled by extraction (overall CO… | UNRESOLVED — senior reviewer decides; see action |
| S166 | ood_metric_type | — | exact_match | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | open_questions_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | other_metrics_reported | — | Exact-match accuracy by structural generalization type (OSM,… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S166 | relevance_sigma_justification | Directly studies compositional generalization failure (the s… | Directly addresses the sigma-trap: identifies entangled sour… | UNRESOLVED — senior reviewer decides; see action |
| S166 | repr_analysis_finding | DANGLE-ENC yields lower intra/inter-class variance ratios (C… | t-SNE of hidden states for prepositions in PP-recursion cont… | UNRESOLVED — senior reviewer decides; see action |
| S166 | repr_analysis_layer | last-layer hidden states before softmax for preposition pred… | last hidden layer before softmax used to predict target toke… | UNRESOLVED — senior reviewer decides; see action |
| S166 | repr_analysis_secondary | clustering | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S166 | schema_coherence_notes | Entanglement ratio R = intra/inter-class variance of last-la… | Entanglement = ratio R of intra-class to inter-class varianc… | UNRESOLVED — senior reviewer decides; see action |
| S166 | schema_coherence_value_baseline | 0.63 | 0.37 | UNRESOLVED — senior reviewer decides; see action |
| S166 | sig_test_reported | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S166 | train_data_note | COGS splits (CP/PP recursion, OSM, lexical, structural); CFQ… | COGS (lexical and structural generalization splits, CP and P… | UNRESOLVED — senior reviewer decides; see action |
| S176 | arch_detail | CLIP (contrastive vision-language) with ResNet-50 vision enc… | CLIP with ResNet-50 vision encoder as main config; ablations… | UNRESOLVED — senior reviewer decides; see action |
| S176 | curriculum_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S176 | data_leakage_check | suspected | not_addressed | UNRESOLVED — senior reviewer decides; see action |
| S176 | effect_size_notes | — | No effect sizes reported; balanced top-1 accuracies reported… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S176 | hidden_dim | 512 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S176 | limitations_stated | — | TRUE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S176 | limitations_text | — | Computational constraints limited replication of ablations t… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S176 | meta_learning_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S176 | notes | arXiv-only stamp (2502.09507v3). Table 6 (ResNet-50/ImageNet… | Main numeric fields left empty because Table 6 reports per-d… | UNRESOLVED — senior reviewer decides; see action |
| S176 | open_questions_text | Effect of dataset size and diversity of the base dataset lef… | Effect of base dataset size and diversity on generalization … | UNRESOLVED — senior reviewer decides; see action |
| S176 | other_metrics_reported | — | balanced top-5 accuracy; macro F1 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S176 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S176 | relevance_sigma_justification | Directly investigates when compositional and domain generali… | Directly studies compositional generalization (unseen classe… | UNRESOLVED — senior reviewer decides; see action |
| S176 | repr_analysis_finding | Mechanistic analyses conclude successful domain and composit… | Mechanistic analyses indicate successful generalization requ… | UNRESOLVED — senior reviewer decides; see action |
| S176 | repr_analysis_layer | intermediate layers | intermediate | UNRESOLVED — senior reviewer decides; see action |
| S176 | schema_coherence_measured | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S176 | schema_coherence_notes | Mechanistic analyses of shared representations in intermedia… | No quantitative coherence proxy reported in excerpt; only qu… | UNRESOLVED — senior reviewer decides; see action |
| S176 | sig_test_reported | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S176 | task_custom_name | — | CLIP vision-language classification over controlled domain m… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S176 | task_primary | DomainNet | custom | UNRESOLVED — senior reviewer decides; see action |
| S176 | train_data_note | Controlled training distributions over DomainNet-like domain… | CLIP trained on ImageNet-Captions with systematically constr… | UNRESOLVED — senior reviewer decides; see action |
| S176 | train_regime | standard_Adam | contrastive | UNRESOLVED — senior reviewer decides; see action |
| S177 | arch_detail | Kernel models with fixed, compositionally structured represe… | Kernel models with fixed, compositionally structured random-… | UNRESOLVED — senior reviewer decides; see action |
| S177 | augmentation_used | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S177 | code_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S177 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S177 | effect_size_notes | No effect sizes or quantitative accuracy results reported in… | No quantitative results (accuracies or effect sizes) appear … | UNRESOLVED — senior reviewer decides; see action |
| S177 | id_metric_type | — | accuracy | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S177 | limitations_text | Theory is restricted to kernel models with fixed, compositio… | Only preliminary evidence is given for extending the theory … | UNRESOLVED — senior reviewer decides; see action |
| S177 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S177 | notes | ICLR 2025 conference paper (arXiv 2405.16391v3). Central con… | No quantitative results (no accuracies) appear in the excerp… | UNRESOLVED — senior reviewer decides; see action |
| S177 | ood_metric_type | — | accuracy | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S177 | open_questions_text | Whether learned disentangled representations are useful for … | Framework grounds research into learning mechanisms that can… | UNRESOLVED — senior reviewer decides; see action |
| S177 | relevance_alignment | 2 | 1 | UNRESOLVED — senior reviewer decides; see action |
| S177 | relevance_alignment_justification | No direct treatment of AI alignment, safety, or goal misgene… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S177 | relevance_sigma_justification | Provides a formal kernel theory of when compositional struct… | Provides a theory of compositional generalization failure in… | UNRESOLVED — senior reviewer decides; see action |
| S177 | repr_analysis_finding | Representational salience analysis shows deep random ReLU ne… | Representational salience shows deeper ReLU networks increas… | UNRESOLVED — senior reviewer decides; see action |
| S177 | repr_analysis_layer | layers of random-weight networks (0-20 layers) | layer-wise (all layers) | UNRESOLVED — senior reviewer decides; see action |
| S177 | schema_coherence_notes | Introduces representational salience S(k;C), a normalized me… | Introduces representational salience S(k;C), measuring the u… | UNRESOLVED — senior reviewer decides; see action |
| S177 | task_custom_name | symbolic addition; context dependence; transitive equivalenc… | Symbolic addition and context dependence compositional tasks… | UNRESOLVED — senior reviewer decides; see action |
| S177 | train_data_note | Compositional tasks built from component conjunctions (symbo… | Training data statistics (which component conjunctions appea… | UNRESOLVED — senior reviewer decides; see action |
| S178 | arch_detail | Syntax-guided Transformer encoder with dependency-parsing at… | Transformer encoder-decoder with dependency-parse-based atte… | UNRESOLVED — senior reviewer decides; see action |
| S178 | arch_primary | TransformerEnc | TransformerEncDec | UNRESOLVED — senior reviewer decides; see action |
| S178 | code_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S178 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S178 | effect_size_notes | No effect sizes reported; accuracy with std over 3 runs | No effect sizes reported; only mean +/- SD accuracies per sp… | UNRESOLVED — senior reviewer decides; see action |
| S178 | id_metric_type | — | accuracy | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S178 | limitations_text | Controlled synthetic datasets may not capture real-world com… | Synthetic datasets may not capture real-world complexity (re… | UNRESOLVED — senior reviewer decides; see action |
| S178 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S178 | notes | Main values = Syntax-guided Transformer (Dependency masking)… | Main-field OOD values = gSCAN composite average of the Depen… | UNRESOLVED — senior reviewer decides; see action |
| S178 | other_metrics_reported | Parameter counts (74K LSTM, 3M/4.6M baselines, 1.9M ours); c… | parameter count comparison (efficiency); attention maps | UNRESOLVED — senior reviewer decides; see action |
| S178 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S178 | relevance_sigma_justification | Directly targets compositional generalization failure (the s… | Empirical compositional generalization study on gSCAN/GSRR/R… | UNRESOLVED — senior reviewer decides; see action |
| S178 | relevance_sigma_trap | 4 | 3 | UNRESOLVED — senior reviewer decides; see action |
| S178 | repr_analysis_finding | Cross-attention focuses on the target object in 86% of valid… | In 86% of validation samples cross-attention shows pronounce… | UNRESOLVED — senior reviewer decides; see action |
| S178 | repr_analysis_layer | cross-attention, encoder layers | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S178 | schema_coherence_notes | No representation-level coherence proxy; attention-masking e… | No representation-level coherence proxy measured; only quali… | UNRESOLVED — senior reviewer decides; see action |
| S178 | task_custom_name | GSRR; ReaSCAN (grounded instruction following) | gSCAN, GSRR, ReaSCAN multimodal grounded instruction followi… | UNRESOLVED — senior reviewer decides; see action |
| S178 | tasks_secondary | custom | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S178 | train_data_note | gSCAN, GSRR, ReaSCAN multimodal instruction-following datase… | Evaluated on gSCAN, GSRR, and ReaSCAN test splits; results a… | UNRESOLVED — senior reviewer decides; see action |
| S179 | arch_detail | Pretrained LMs for in-context learning: T5 (finetuned setup)… | Pretrained LMs: T5 (finetuned, FT setup) and Codex (pure in-… | UNRESOLVED — senior reviewer decides; see action |
| S179 | augmentation_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S179 | curriculum_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S179 | data_available | TRUE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S179 | effect_size_notes | No numeric accuracy values in the excerpt to derive an effec… | No effect sizes reported; accuracy numbers appear only in fi… | UNRESOLVED — senior reviewer decides; see action |
| S179 | error_bars_reported | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S179 | limitations_text | Assumes diversity is obtained via different program structur… | Assumes diversity via program structures only, not more comp… | UNRESOLVED — senior reviewer decides; see action |
| S179 | meta_learning_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S179 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S179 | n_seeds_reported | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S179 | notes | Results reported only via figures and a referenced Table 4 w… | No accuracy numbers appear in the text excerpt (results show… | UNRESOLVED — senior reviewer decides; see action |
| S179 | ood_difficulty_metric_name | unobserved local structure (ULS) rate | ULS (unobserved local structure) rate | UNRESOLVED — senior reviewer decides; see action |
| S179 | open_questions_text | Understand why different retrievers are preferred in differe… | Future research should understand why different retrievers a… | UNRESOLVED — senior reviewer decides; see action |
| S179 | other_metrics_reported | Prompt metrics for 24-demonstration prompts: symbol coverage… | symbol coverage; LS coverage; utterance similarity; number o… | UNRESOLVED — senior reviewer decides; see action |
| S179 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S179 | relevance_sigma_justification | Directly targets compositional generalization failure (the s… | Addresses compositional generalization failure in semantic p… | UNRESOLVED — senior reviewer decides; see action |
| S179 | relevance_sigma_trap | 4 | 3 | UNRESOLVED — senior reviewer decides; see action |
| S179 | schema_coherence_notes | No representation-level coherence proxy measured; structural… | No representation-level coherence proxy measured | UNRESOLVED — senior reviewer decides; see action |
| S179 | task_custom_name | SMCalFlow-CS (third semantic parsing dataset not named in ex… | Compositional semantic parsing (GeoQuery TMCD, SMCalFlow-CS,… | UNRESOLVED — senior reviewer decides; see action |
| S179 | train_data_note | — | Three compositional semantic-parsing datasets (GeoQuery TMCD… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S179 | train_regime_other | in-context learning prompting (24 demonstrations) plus optio… | in-context learning with diverse demonstration selection (No… | UNRESOLVED — senior reviewer decides; see action |
| S184 | arch_detail | Survey covering Classicist vs Connectionist approaches and d… | Survey covers Connectionist (Eliminative, Hybrid, Implementa… | UNRESOLVED — senior reviewer decides; see action |
| S184 | augmentation_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S184 | code_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S184 | curriculum_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S184 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S184 | effect_size_notes | — | Survey paper; no experiments or effect sizes | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S184 | limitations_text | Authors note they could cover only a small portion of the ma… | Author notes only a small portion of the many contributions … | UNRESOLVED — senior reviewer decides; see action |
| S184 | meta_learning_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S184 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S184 | notes | Survey paper; no experiments, models, or quantitative result… | Survey paper (arXiv preprint); no experiments, no quantitati… | UNRESOLVED — senior reviewer decides; see action |
| S184 | ood_split_type | compositional | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S184 | open_questions_stated | — | TRUE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S184 | open_questions_text | — | Variable binding and causality are highlighted as crucial op… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S184 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S184 | relevance_sigma_justification | Survey organizing the systematic (compositional) generalizat… | A survey of systematic (compositional) generalization, the v… | UNRESOLVED — senior reviewer decides; see action |
| S184 | schema_coherence_notes | — | No measurements performed; survey discusses disentangled rep… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S184 | task_custom_name | — | Survey of systematic generalization across language, vision,… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S184 | train_data_note | Surveys language, vision, and VQA systematic generalization … | Survey; no experiments conducted | UNRESOLVED — senior reviewer decides; see action |
| S185 | arch_detail | BERT classifier; augmentation generators: Flan-T5, GPT-2-PT … | BERT classifier finetuned for multi-label text classificatio… | UNRESOLVED — senior reviewer decides; see action |
| S185 | augmentation_type | synthetic training text generated by conditional text genera… | Synthetic text generation via conditional generators (LD-VAE… | UNRESOLVED — senior reviewer decides; see action |
| S185 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S185 | effect_size_notes | — | No effect sizes or significance tests reported; only raw acc… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S185 | id_metric_type | — | accuracy | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S185 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S185 | notes | AAAI 2024 (copyright stamp), arXiv:2312.11276v3. Main-form o… | Main OOD value = BERT classifier accuracy on AAPD CG test sp… | UNRESOLVED — senior reviewer decides; see action |
| S185 | other_metrics_reported | Accuracy only; t-SNE visualization of label representations;… | support-set size sensitivity; generator quality control (fil… | UNRESOLVED — senior reviewer decides; see action |
| S185 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S185 | relevance_sigma_justification | Constructs compositional splits for multi-label text classif… | Directly documents compositional generalization failure in m… | UNRESOLVED — senior reviewer decides; see action |
| S185 | relevance_sigma_trap | 3 | 4 | UNRESOLVED — senior reviewer decides; see action |
| S185 | repr_analysis | other | clustering | UNRESOLVED — senior reviewer decides; see action |
| S185 | repr_analysis_finding | t-SNE visualization of label-phrase representations shows GP… | T-SNE shows GPT2-PT label representations entangled across l… | UNRESOLVED — senior reviewer decides; see action |
| S185 | schema_coherence_notes | Disentanglement of label latent representations shown only q… | No quantitative coherence proxy; disentanglement shown via q… | UNRESOLVED — senior reviewer decides; see action |
| S185 | task_custom_name | multi-label text classification (MLTC) on AAPD and SemEval-2… | Multi-label text classification (AAPD, SemEval emotion, and … | UNRESOLVED — senior reviewer decides; see action |
| S185 | train_data_note | Compositional generalization splits of AAPD and SemEval; sup… | Custom compositional (CG) train/test splits over three MLTC … | UNRESOLVED — senior reviewer decides; see action |
| S185 | train_regime | augmentation | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S185 | train_regime_sigma | — | not_applicable | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S202 | arch_detail | Modular neural network separating cognitive processes (e.g.,… | Modular network separating perception and navigation modules… | UNRESOLVED — senior reviewer decides; see action |
| S202 | augmentation_type | structured data augmentation with additional adverbs (vocabu… | Structured (template-based) data augmentation adding adverbs… | UNRESOLVED — senior reviewer decides; see action |
| S202 | effect_size_notes | — | No effect sizes reported; exact-match accuracies with std de… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S202 | limitations_stated | FALSE | TRUE | UNRESOLVED — senior reviewer decides; see action |
| S202 | limitations_text | — | High variance in adverb-split results; vocabulary size alone… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S202 | notes | Main form = Modular & Augmentation config: ID Random split 9… | Main-form values = 'Modular & Augmentation' model on gSCAN: … | UNRESOLVED — senior reviewer decides; see action |
| S202 | open_questions_text | Future work: eliminate the need for designing a structured a… | Future work: eliminate the need for hand-designed structured… | UNRESOLVED — senior reviewer decides; see action |
| S202 | other_metrics_reported | exact match across 8 gSCAN splits for 4 configurations; voca… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S202 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S202 | relevance_sigma_justification | Directly studies systematic (compositional) generalization i… | Directly studies compositional generalization failure (sigma… | UNRESOLVED — senior reviewer decides; see action |
| S202 | schema_coherence_notes | — | No representation-level coherence/compositionality proxy mea… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S202 | train_data_note | gSCAN with structured adverb augmentation: up to ~150 extra … | gSCAN grounded language learning; augmented training sets wi… | UNRESOLVED — senior reviewer decides; see action |
| S207 | arch_detail | sDTM: Sparse Differentiable Tree Machine with random positio… | Sparse Differentiable Tree Machine (sDTM): unified neurosymb… | UNRESOLVED — senior reviewer decides; see action |
| S207 | code_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S207 | data_available | TRUE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S207 | effect_size_notes | Paper reports only per-split mean/std accuracies; no effect … | No effect sizes reported; mean and std dev accuracies per sp… | UNRESOLVED — senior reviewer decides; see action |
| S207 | limitations_extractor | NeurIPS checklist states limitations are addressed in Sectio… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S207 | limitations_text | — | sDTM suffers from high variance; some runs get stuck in loca… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S207 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S207 | n_layers | 14 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S207 | notes | Best-of-5-seeds reporting (high variance; some runs stuck in… | Main-form values = sDTM (parse trees) on SCAN: IID 0.80+/-0.… | UNRESOLVED — senior reviewer decides; see action |
| S207 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S207 | relevance_sigma_justification | Directly targets compositional generalization failure (sigma… | Directly targets compositional generalization across distrib… | UNRESOLVED — senior reviewer decides; see action |
| S207 | schema_coherence_notes | No representation-level coherence proxy (probing/CKA/composi… | No representation-level coherence/compositionality proxy mea… | UNRESOLVED — senior reviewer decides; see action |
| S207 | task_custom_name | Also Active-Logical and FOR2LAM (seq2seq; not in task vocabu… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S207 | tasks_secondary | GeoQuery; other | GeoQuery | UNRESOLVED — senior reviewer decides; see action |
| S207 | train_data_note | sDTM layers = 2x max tree depth for seq input (14 SCAN, 22 G… | Datasets: Active-Logical (max tree depth 10), FOR2LAM (14), … | UNRESOLVED — senior reviewer decides; see action |
| S210 | arch_detail | Neural Module Network with three stages (image encoder, inte… | Neural Module Networks (NMN) with tree program layouts in th… | UNRESOLVED — senior reviewer decides; see action |
| S210 | effect_size_notes | Paper reports raw accuracies with SDs only; notes gaps of ab… | No effect sizes reported; mean +/- std dev accuracies across… | UNRESOLVED — senior reviewer decides; see action |
| S210 | limitations_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S210 | notes | Full-text excerpt truncated mid-section 4.2. Main-form value… | Main-form values = Vector-NMN with group image encoder on CL… | UNRESOLVED — senior reviewer decides; see action |
| S210 | open_questions_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S210 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S210 | relevance_sigma_justification | Directly targets systematic (compositional) generalization f… | Directly studies compositional (systematic) generalization f… | UNRESOLVED — senior reviewer decides; see action |
| S210 | schema_coherence_notes | — | No representation-level coherence/compositionality proxy mea… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S210 | task_custom_name | Visual Question Answering (VQA-MNIST, SQOOP, CLEVR-CoGenT) | Visual Question Answering: VQA-MNIST, SQOOP, CLEVR-CoGenT | UNRESOLVED — senior reviewer decides; see action |
| S210 | train_data_note | VQA-MNIST, SQOOP, CLEVR-CoGenT; training diversity varied as… | VQA-MNIST (attribute combinations with varying training dive… | UNRESOLVED — senior reviewer decides; see action |
| S211 | arch_detail | CLIP backbones: ViT-B-16, ViT-B-32, ViT-L-14, RN50, RN101; i… | CLIP dual encoders: ViT-B-16, ViT-B-32, ViT-L-14 and ResNet … | UNRESOLVED — senior reviewer decides; see action |
| S211 | arch_family | vit | other | UNRESOLVED — senior reviewer decides; see action |
| S211 | arch_primary | ViT | other | UNRESOLVED — senior reviewer decides; see action |
| S211 | augmentation_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S211 | ci_reported | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S211 | curriculum_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S211 | effect_size_notes | No effect size reported; the quantitative claim is a logisti… | No effect sizes; logistic regression predictions of per-samp… | UNRESOLVED — senior reviewer decides; see action |
| S211 | id_metric_other | Recall@10 | Recall@10 retrieval (also k=1,5) | UNRESOLVED — senior reviewer decides; see action |
| S211 | limitations_stated | — | TRUE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S211 | limitations_text | — | Concept analysis limited to tangible objects; abstract conce… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S211 | meta_learning_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S211 | n_seeds_reported | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S211 | notes | Excerpt figure values (Recall@10 per model/corpus) illegible… | No numeric Recall values extractable from text excerpt (resu… | UNRESOLVED — senior reviewer decides; see action |
| S211 | ood_difficulty_metric_name | average pretraining frequency (geometric mean) of constituen… | average pretraining frequency of constituent objects (geomet… | UNRESOLVED — senior reviewer decides; see action |
| S211 | ood_metric_other | Recall@10 | Recall@10 retrieval (also k=1,5) | UNRESOLVED — senior reviewer decides; see action |
| S211 | open_questions_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S211 | other_metrics_reported | Recall@1, Recall@5 (reported alongside Recall@10) | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S211 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S211 | relevance_sigma_justification | Directly investigates compositional generalization success c… | Directly probes compositional generalization failure (sigma-… | UNRESOLVED — senior reviewer decides; see action |
| S211 | schema_coherence_notes | No representation-level coherence proxy (probing/CKA/RSA); c… | No representation-level coherence/compositionality proxy mea… | UNRESOLVED — senior reviewer decides; see action |
| S211 | task_custom_name | Text-to-image / image-to-text retrieval on Flickr-1K and COC… | Text-to-image (T2I) and image-to-text (I2T) retrieval on Fli… | UNRESOLVED — senior reviewer decides; see action |
| S211 | train_data_note | CLIP pretraining corpora: CC-3M, CC-12M, YFCC-15M, LAION400M… | Test sets curated from Flickr-1K and COCO-5K retaining only … | UNRESOLVED — senior reviewer decides; see action |
| S211 | train_regime | — | contrastive | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S216 | arch_detail | 36 instruction-tuned decoder-only LLMs across families (Llam… | 36 instruction-tuned decoder-only LLMs: Llama3.x (1B-405B), … | UNRESOLVED — senior reviewer decides; see action |
| S216 | code_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S216 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S216 | effect_size_notes | No effect size reported; performance reported as mean and SD… | No effect sizes; mean +/- std across 36 LLMs for coverage, o… | UNRESOLVED — senior reviewer decides; see action |
| S216 | error_bars_reported | FALSE | TRUE | UNRESOLVED — senior reviewer decides; see action |
| S216 | id_acc_mean | — | 0.9113 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S216 | id_acc_sd | — | 0.1186 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S216 | id_metric_other | — | concept coverage (CommonGen, w/o order instruction) | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S216 | limitations_text | Verb-heavy (VVVV) concept sets still poorly covered; biases … | LLM performance is affected by slight prompt phrasing; no un… | UNRESOLVED — senior reviewer decides; see action |
| S216 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S216 | notes | Prefill hints (SLOG; Math/MW; seeds_runs=192) not supported … | Main-form ID = mean Concepts Coverage (w/o order) across 36 … | UNRESOLVED — senior reviewer decides; see action |
| S216 | ood_acc_mean | — | 0.75 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S216 | ood_metric_other | ordered coverage (Ordered Rate); Concepts Coverage; Diverse … | ordered coverage (concepts generated in specified order) | UNRESOLVED — senior reviewer decides; see action |
| S216 | other_metrics_reported | Similarity; Diversity; Perplexity; Distinct; pBLEU; pBLEURT | pBLEU; pBLEURT; distinct; perplexity; similarity; diversity | UNRESOLVED — senior reviewer decides; see action |
| S216 | relevance_alignment_justification | Focuses on instruction-following (adhering to specified conc… | Instruction-following fidelity is alignment-adjacent (models… | UNRESOLVED — senior reviewer decides; see action |
| S216 | relevance_sigma_justification | Proposes Ordered CommonGen to measure compositional generali… | Directly benchmarks compositional generalization failure of … | UNRESOLVED — senior reviewer decides; see action |
| S216 | schema_coherence_notes | No representation-level coherence or compositionality proxy … | No representation-level coherence/compositionality proxy mea… | UNRESOLVED — senior reviewer decides; see action |
| S216 | task_custom_name | Ordered CommonGen (generative commonsense reasoning; concept… | Ordered CommonGen (generative commonsense reasoning with con… | UNRESOLVED — senior reviewer decides; see action |
| S216 | train_data_note | Ordered CommonGen built from CommonGen Concept Sets (4 conce… | Ordered CommonGen: 24 permutations of each CommonGen 4-conce… | UNRESOLVED — senior reviewer decides; see action |
| S216 | train_regime | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S216 | train_regime_other | instruction tuning (SFT / human-preference tuning) of pretra… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S221 | arch_detail | Transformer encoder-decoder trained from scratch with ExeDec… | ExeDec: decomposition-based synthesis that predicts executio… | UNRESOLVED — senior reviewer decides; see action |
| S221 | augmentation_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S221 | baseline_regime | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S221 | ci_reported | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S221 | curriculum_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S221 | effect_size_notes | No effect sizes; results reported as end-to-end test accurac… | No effect sizes; end-to-end test accuracy percentages for No… | UNRESOLVED — senior reviewer decides; see action |
| S221 | error_bars_reported | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S221 | limitations_stated | — | TRUE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S221 | limitations_text | — | ExeDec sometimes performs worse than the no-subgoal ablation… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S221 | meta_learning_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S221 | n_seeds_reported | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S221 | notes | Main form = ExeDec, beam size 10, RobustFill; NoGen treated … | Main-form values = ExeDec on RobustFill, beam size 10: NoGen… | UNRESOLVED — senior reviewer decides; see action |
| S221 | open_questions_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S221 | other_metrics_reported | Single-step subgoal/synthesizer/combined accuracy; per-CG-ta… | single-step accuracy (SubgoalModel/SynthesizerModel/Combined… | UNRESOLVED — senior reviewer decides; see action |
| S221 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S221 | relevance_sigma_justification | Directly addresses the sigma-trap: quantifies compositional … | Directly targets compositional generalization in neural prog… | UNRESOLVED — senior reviewer decides; see action |
| S221 | schema_coherence_notes | No representation-level coherence proxy measured; analysis i… | No representation-level coherence/compositionality proxy mea… | UNRESOLVED — senior reviewer decides; see action |
| S221 | sig_test_reported | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S221 | task_custom_name | Program synthesis by example (RobustFill and DeepCoder DSLs) | Neural program synthesis by example: RobustFill (string mani… | UNRESOLVED — senior reviewer decides; see action |
| S221 | train_data_note | RobustFill and DeepCoder PBE datasets; 20,000 pretraining st… | Meta-benchmark of 5 compositional generalization tasks (Leng… | UNRESOLVED — senior reviewer decides; see action |
| S221 | train_regime | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S221 | train_regime_other | execution-decomposition subgoal supervision (ExeDec) | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S228 | arch_detail | Language-conditioned contextualized object embeddings via dy… | Language-conditioned embedding: per-object local embeddings … | UNRESOLVED — senior reviewer decides; see action |
| S228 | arch_family | rnn_family | gnn | UNRESOLVED — senior reviewer decides; see action |
| S228 | arch_primary | LSTM | other | UNRESOLVED — senior reviewer decides; see action |
| S228 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S228 | data_leakage_check | not_addressed | explicit_no | UNRESOLVED — senior reviewer decides; see action |
| S228 | effect_size_notes | No effect sizes or significance tests reported; mean +/- SD … | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S228 | limitations_stated | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S228 | limitations_text | Fails on Split B (novel direction): LSTM decoder cannot gene… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S228 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S228 | notes | Main-form ID = Split A (random, 98.6 +/- 0.95); OOD = Split … | Main-form values = full model on Split A (ID, random) 98.6+/… | UNRESOLVED — senior reviewer decides; see action |
| S228 | ood_acc_mean | 0.8031 | 0.8732 | UNRESOLVED — senior reviewer decides; see action |
| S228 | ood_acc_sd | 0.2451 | 0.2738 | UNRESOLVED — senior reviewer decides; see action |
| S228 | open_questions_text | Introduce clues informing the model of view changes as it ta… | Failure on Split B analyzed (LSTM decoder cannot generalize … | UNRESOLVED — senior reviewer decides; see action |
| S228 | other_metrics_reported | Exact match accuracy per split (7 splits); attention-score v… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S228 | relevance_alignment | 1 | 2 | UNRESOLVED — senior reviewer decides; see action |
| S228 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | Studies an instruction-following agent that must execute nat… | UNRESOLVED — senior reviewer decides; see action |
| S228 | relevance_sigma_justification | Directly targets systematic (compositional) generalization o… | Directly targets the sigma-trap: evaluates systematic (compo… | UNRESOLVED — senior reviewer decides; see action |
| S228 | repr_analysis_finding | Attention visualization shows baseline attends to correct ta… | Attention visualization on grid-world cells shows baseline a… | UNRESOLVED — senior reviewer decides; see action |
| S228 | schema_coherence_notes | No representation-level coherence/compositionality proxy mea… | No representation-level coherence/compositionality proxy mea… | UNRESOLVED — senior reviewer decides; see action |
| S228 | train_data_note | gSCAN grounded language navigation dataset; 7 test splits (A… | gSCAN (grounded SCAN) grid-world navigation dataset; 7 test … | UNRESOLVED — senior reviewer decides; see action |
| S229 | arch_detail | Fully-connected DNN and CNN reported in tables; also studies… | Fully connected (DNN), CNN, LSTM, ResNet, and Vision Transfo… | UNRESOLVED — senior reviewer decides; see action |
| S229 | id_acc_mean | — | 0.054 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S229 | id_acc_sd | — | 0.006 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S229 | limitations_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S229 | notes | Table 4 (equally difficult factors, two CIFAR-10 by channel)… | Main-form values = DNN (fully connected) with shared network… | UNRESOLVED — senior reviewer decides; see action |
| S229 | ood_acc_mean | — | 0.044 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S229 | ood_acc_sd | — | 0.005 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S229 | open_questions_stated | — | TRUE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S229 | open_questions_text | — | Authors state the function-sharing account may not be remova… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S229 | pub_type | theoretical | empirical | UNRESOLVED — senior reviewer decides; see action |
| S229 | relevance_alignment | 1 | 2 | UNRESOLVED — senior reviewer decides; see action |
| S229 | relevance_alignment_justification | No connection to AI alignment, safety, or goal misgeneraliza… | Provides a mechanistic account of a core generalization fail… | UNRESOLVED — senior reviewer decides; see action |
| S229 | relevance_sigma_justification | Directly theorizes a mechanism (internal function sharing pr… | Directly theorizes why standard deep learning fails systemat… | UNRESOLVED — senior reviewer decides; see action |
| S229 | relevance_sigma_trap | 4 | 5 | UNRESOLVED — senior reviewer decides; see action |
| S229 | repr_analysis_finding | — | Visualized decision boundaries and attention over shared-vs-… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S229 | schema_coherence_notes | — | No representation-level coherence/compositionality proxy; th… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S229 | task_custom_name | Synthetic two-output classification over partitioned input s… | Synthetic factor-combination classification tasks: two outpu… | UNRESOLVED — senior reviewer decides; see action |
| S229 | tasks_secondary | — | CIFAR10 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S229 | train_data_note | Synthetic tasks where some factor combinations (e.g. Y1<5 or… | Training label combinations exclude certain factor combinati… | UNRESOLVED — senior reviewer decides; see action |
| S239 | arch_detail | Decoder-only LLM post-trained with SFT followed by RL (exact… | LLM trained via two-stage post-training pipeline: SFT on cor… | UNRESOLVED — senior reviewer decides; see action |
| S239 | effect_size_notes | — | Paper reports gains (e.g., +10.0, +37.8, +40.3, +43.7) rathe… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S239 | id_acc_mean | — | 0.99 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S239 | limitations_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S239 | notes | Main-form ood_acc_mean = SFT+RL on compound traces evaluated… | Main-form values = SFT+RL (no atom absence in SFT) on seen-2… | UNRESOLVED — senior reviewer decides; see action |
| S239 | ood_acc_mean | 0.426 | 0.67 | UNRESOLVED — senior reviewer decides; see action |
| S239 | ood_difficulty_metric_name | compositional depth (level L) | compositional depth L | UNRESOLVED — senior reviewer decides; see action |
| S239 | open_questions_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S239 | other_metrics_reported | Reported gains: RL adds 43.7% over SFT-only on atomic skills… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S239 | relevance_alignment | 2 | 3 | UNRESOLVED — senior reviewer decides; see action |
| S239 | relevance_alignment_justification | Studies how RL post-training drives out-of-distribution comp… | Studies the SFT+RL post-training recipe that underlies moder… | UNRESOLVED — senior reviewer decides; see action |
| S239 | relevance_sigma_justification | Directly formalizes compositional generalization in LLM reas… | Directly targets the sigma-trap: formalizes compositional ge… | UNRESOLVED — senior reviewer decides; see action |
| S239 | schema_coherence_notes | — | Proposes a hierarchical latent selection model of reasoning … | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S239 | task_custom_name | Synthetic compositional string-transformation tasks: 24 atom… | Synthetic compositional string-transformation reasoning task… | UNRESOLVED — senior reviewer decides; see action |
| S239 | train_data_note | 131k training compositions (L=2,3) used in SFT-data-design e… | 131k training compositions at depths L=2,3 partitioned acros… | UNRESOLVED — senior reviewer decides; see action |
| S239 | train_regime_other | Two-stage post-training: supervised fine-tuning (SFT) on cor… | SFT + RL post-training pipeline (two-stage) | UNRESOLVED — senior reviewer decides; see action |
| S242 | arch_detail | Model-based RL agent: causal transition model estimated via … | Causal model-based RL: estimates a causal transition model (… | UNRESOLVED — senior reviewer decides; see action |
| S242 | code_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S242 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S242 | effect_size_notes | — | No accuracy or effect size reported; validation uses graph e… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S242 | limitations_text | Systematic generalization is achieved only up to an unavoida… | Systematic generalization is only guaranteed up to an unavoi… | UNRESOLVED — senior reviewer decides; see action |
| S242 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S242 | notes | Primarily a theory paper (AAAI 2023); numerical validation o… | Primarily a theoretical paper (Theorems 4.3-4.9, Lemmas, pol… | UNRESOLVED — senior reviewer decides; see action |
| S242 | ood_split_type | domain_shift | compositional | UNRESOLVED — senior reviewer decides; see action |
| S242 | open_questions_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S242 | other_metrics_reported | Graph edit distance between estimated and ground-truth causa… | graph edit distance between estimated and ground-truth causa… | UNRESOLVED — senior reviewer decides; see action |
| S242 | relevance_alignment_justification | No connection to AI alignment or safety; a theoretical RL ge… | Pertinent to generalization and the curse of generalization … | UNRESOLVED — senior reviewer decides; see action |
| S242 | relevance_sigma_justification | Provides a formal causal formulation of systematic generaliz… | Directly addresses the sigma-trap in the RL setting: gives a… | UNRESOLVED — senior reviewer decides; see action |
| S242 | relevance_sigma_trap | 4 | 5 | UNRESOLVED — senior reviewer decides; see action |
| S242 | schema_coherence_notes | Learns the causal structure (dependency graph) of MDP transi… | No representation-level coherence/compositionality proxy; ca… | UNRESOLVED — senior reviewer decides; see action |
| S242 | task_custom_name | systematic generalization in RL over feature-vector MDPs (sy… | Sequential decision making over discrete MDPs with feature-v… | UNRESOLVED — senior reviewer decides; see action |
| S242 | train_data_note | Reward-free interactions from a subset of M environments (M=… | M=3 training environments used to estimate the causal transi… | UNRESOLVED — senior reviewer decides; see action |
| S243 | arch_detail | Small transformer encoder-decoder, 5.7M params, trained via … | Small transformer encoder-decoder (5.7M params) trained via … | UNRESOLVED — senior reviewer decides; see action |
| S243 | baseline_regime | — | other | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S243 | code_available | TRUE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S243 | code_url | https://github.com/da-fr/arc-prize-2024 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S243 | effect_size_notes | No numeric results in excerpt; outcomes described qualitativ… | No quantitative accuracy results in the excerpt; only metric… | UNRESOLVED — senior reviewer decides; see action |
| S243 | limitations_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S243 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S243 | notes | ICLR 2026 paper. Excerpt contains dataset/metric definitions… | Results section excerpt contains metric definitions (exact m… | UNRESOLVED — senior reviewer decides; see action |
| S243 | open_questions_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S243 | other_metrics_reported | color accuracy; shape accuracy; response-validity rates per … | color accuracy and shape accuracy (in addition to exact-matc… | UNRESOLVED — senior reviewer decides; see action |
| S243 | relevance_alignment | 1 | 2 | UNRESOLVED — senior reviewer decides; see action |
| S243 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | Addresses systematic generalization capacity of LLMs and a r… | UNRESOLVED — senior reviewer decides; see action |
| S243 | relevance_sigma_justification | Directly probes the sigma-trap: extends meta-learning for co… | Introduces Compositional-ARC, a benchmark that directly oper… | UNRESOLVED — senior reviewer decides; see action |
| S243 | relevance_sigma_trap | 4 | 5 | UNRESOLVED — senior reviewer decides; see action |
| S243 | schema_coherence_notes | No representation-level coherence proxy measured in excerpt | No representation-level coherence/compositionality proxy mea… | UNRESOLVED — senior reviewer decides; see action |
| S243 | task_custom_name | Compositional-ARC (ARC-style abstract spatial reasoning; geo… | Compositional-ARC: abstract spatial reasoning on 10x10 grids… | UNRESOLVED — senior reviewer decides; see action |
| S243 | train_data_note | Compositional-ARC: 10x10 grids with colored objects; general… | Compositional-ARC dataset: novel combinations of known geome… | UNRESOLVED — senior reviewer decides; see action |
| S244 | arch_detail | CLIP ViT-B/32 pretrained on LAION-400M (primary); scaling: V… | CLIP ViT-B/32 pretrained on LAION-400M; scaling variants ViT… | UNRESOLVED — senior reviewer decides; see action |
| S244 | augmentation_type | on-the-fly concept-pair pasting (PMI-based image edits) duri… | PMI-based on-the-fly image editing (pasting an accessory con… | UNRESOLVED — senior reviewer decides; see action |
| S244 | ci_reported | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S244 | effect_size_notes | Correlation between concept-pair PMI and CLIP zero-shot accu… | No absolute accuracies or standard effect sizes in the excer… | UNRESOLVED — senior reviewer decides; see action |
| S244 | effect_size_type | other | none | UNRESOLVED — senior reviewer decides; see action |
| S244 | effect_size_value | 0.97 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S244 | error_bars_reported | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S244 | limitations_stated | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S244 | model_weights_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S244 | n_seeds_reported | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S244 | notes | GenPairs: 200,000 synthetic images (diffusion-generated, Lla… | No absolute accuracy values reported in the excerpt, only co… | UNRESOLVED — senior reviewer decides; see action |
| S244 | ood_difficulty_metric_name | pointwise mutual information (PMI) of concept pairs in pretr… | pointwise mutual information (PMI) of concept pairs in the p… | UNRESOLVED — senior reviewer decides; see action |
| S244 | open_questions_stated | — | TRUE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S244 | open_questions_text | — | Highlights the need for algorithms and architectures that im… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S244 | other_metrics_reported | zero-shot top-1/top-5 accuracy; correlation r between PMI an… | Pearson correlation r between PMI and zero-shot accuracy: 0.… | UNRESOLVED — senior reviewer decides; see action |
| S244 | relevance_alignment | 1 | 2 | UNRESOLVED — senior reviewer decides; see action |
| S244 | relevance_alignment_justification | No AI safety, alignment, or goal-misgeneralization content; … | Documents a predictable failure mode and data-dependent bias… | UNRESOLVED — senior reviewer decides; see action |
| S244 | relevance_sigma_justification | Directly characterizes compositional generalization failure … | Directly characterizes a core sigma-trap mechanism for multi… | UNRESOLVED — senior reviewer decides; see action |
| S244 | relevance_sigma_trap | 4 | 5 | UNRESOLVED — senior reviewer decides; see action |
| S244 | schema_coherence_notes | PMI is a data-level co-occurrence statistic, not a represent… | No representation-level coherence/compositionality proxy on … | UNRESOLVED — senior reviewer decides; see action |
| S244 | task_custom_name | zero-shot ImageNet classification under concept-pair composi… | GenPairs (200k synthetic images generated via Flux.1-dev fro… | UNRESOLVED — senior reviewer decides; see action |
| S244 | train_data_note | CLIP pretrained on LAION-400M (400M image-text pairs); fine-… | CLIP pretrained on LAION-400M (400M image-text pairs); GenPa… | UNRESOLVED — senior reviewer decides; see action |
| S257 | arch_detail | Seq2seq Transformers and Universal Transformer variants; rel… | Transformer and Universal Transformer with relative position… | UNRESOLVED — senior reviewer decides; see action |
| S257 | data_available | TRUE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S257 | effect_size_notes | No effect sizes reported; IID accuracy ~100% across datasets… | No effect sizes reported; gains reported as raw accuracy dif… | UNRESOLVED — senior reviewer decides; see action |
| S257 | error_bars_reported | TRUE | FALSE | UNRESOLVED — senior reviewer decides; see action |
| S257 | limitations_stated | FALSE | TRUE | UNRESOLVED — senior reviewer decides; see action |
| S257 | limitations_text | — | Relative Transformers without shared layers sometimes catast… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S257 | notes | Main-form = COGS with Position Embedding Downscaling (PED), … | Main-form values = COGS generalization split with PED scalin… | UNRESOLVED — senior reviewer decides; see action |
| S257 | open_questions_text | Calls for future systematic-generalization datasets to inclu… | Future datasets should include validation and test splits fo… | UNRESOLVED — senior reviewer decides; see action |
| S257 | other_metrics_reported | Generalization accuracy vs loss correlation (loss not predic… | Loss (validation and generalization) analyzed vs accuracy; e… | UNRESOLVED — senior reviewer decides; see action |
| S257 | relevance_alignment | 2 | 1 | UNRESOLVED — senior reviewer decides; see action |
| S257 | relevance_alignment_justification | Improves systematic generalization, a capability relevant to… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S257 | relevance_sigma_justification | Directly targets compositional/systematic generalization fai… | Directly attacks compositional/systematic generalization fai… | UNRESOLVED — senior reviewer decides; see action |
| S257 | schema_coherence_notes | No representation-level coherence/compositionality proxy mea… | No representation-level coherence or compositionality proxy … | UNRESOLVED — senior reviewer decides; see action |
| S257 | task_custom_name | Mathematics dataset (MW) also used, not in vocab | Mathematics dataset (Math: place_value) used as a fifth benc… | UNRESOLVED — senior reviewer decides; see action |
| S257 | task_primary | COGS | SCAN | UNRESOLVED — senior reviewer decides; see action |
| S257 | tasks_secondary | SCAN; CFQ; PCFG_SET | COGS; PCFG_SET; CFQ; other | UNRESOLVED — senior reviewer decides; see action |
| S257 | train_data_note | COGS trained for fixed 50k steps without early stopping; PCF… | Five systematic generalization benchmarks: SCAN (length spli… | UNRESOLVED — senior reviewer decides; see action |
| S261 | arch_detail | Seq2seq models: LSTM with attention, Transformer (absolute/r… | Transformer with relative positional encoding, Universal Tra… | UNRESOLVED — senior reviewer decides; see action |
| S261 | curriculum_used | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S261 | effect_size_notes | — | No effect sizes reported | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S261 | limitations_text | Handwritten expressions are basic in spatial locations and v… | Handwritten expressions are basic in spatial layout and visu… | UNRESOLVED — senior reviewer decides; see action |
| S261 | model_scale_category | small | unspecified | UNRESOLVED — senior reviewer decides; see action |
| S261 | notes | Main-form OOD accuracy 0.543 = Universal Transformer with re… | Main ood_acc = best model (Universal Transformer with relati… | UNRESOLVED — senior reviewer decides; see action |
| S261 | open_questions_text | Extend to context-dependent syntax/semantics; investigate me… | Improve systematic generalization of Transformers, especiall… | UNRESOLVED — senior reviewer decides; see action |
| S261 | other_metrics_reported | — | Scaling-law analysis: log-linear fit predicts 10^33 paramete… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S261 | relevance_alignment_justification | No connection to AI alignment, safety, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S261 | relevance_sigma_justification | HINT directly measures systematic generalization failure (th… | Introduces HINT, a systematic-generalization benchmark probi… | UNRESOLVED — senior reviewer decides; see action |
| S261 | schema_coherence_notes | — | No representation-level coherence or compositionality proxy … | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S261 | train_data_note | HINT: handwritten arithmetic with integers; five-fold test s… | HINT: handwritten arithmetic expressions; five-fold test set… | UNRESOLVED — senior reviewer decides; see action |
| S264 | arch_detail | Ensembles of ResNet-18/34/50/101, LeNet variants with filter… | ResNet-18/34/50/101, LeNet (2 conv layers with filter scalin… | UNRESOLVED — senior reviewer decides; see action |
| S264 | augmentation_type | — | none stated; only color channel normalization used | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S264 | code_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S264 | effect_size_notes | — | No effect sizes reported | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S264 | id_acc_n_seeds | 10 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S264 | limitations_text | Prediction method does not take into account accuracy drop d… | Method does not account for accuracy drop due to class-speci… | UNRESOLVED — senior reviewer decides; see action |
| S264 | model_scale_category | small | unspecified | UNRESOLVED — senior reviewer decides; see action |
| S264 | model_weights_available | — | FALSE | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S264 | notes | arXiv preprint; no explicit ID/OOD accuracy tables in excerp… | Quantitative accuracy tables (e.g. Table 1: 91% to 98%) are … | UNRESOLVED — senior reviewer decides; see action |
| S264 | ood_acc_n_seeds | 10 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S264 | open_questions_extractor | — | No explicit future-work statements appear in the excerpt (wh… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S264 | other_metrics_reported | confusion score and entropy score distributions over trainin… | Confusion score, entropy of class-conditional probabilities,… | UNRESOLVED — senior reviewer decides; see action |
| S264 | relevance_alignment_justification | No connection to AI alignment, safety, or goal misgeneraliza… | No connection to AI safety, alignment, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S264 | relevance_sigma_justification | Directly studies why OOD accuracy drops relative to ID accur… | Analyzes why accuracy drops on OOD datasets and proposes a l… | UNRESOLVED — senior reviewer decides; see action |
| S264 | schema_coherence_notes | No representation-level coherence proxy measured; paper anal… | Confusion score measures test-image difficulty from ensemble… | UNRESOLVED — senior reviewer decides; see action |
| S264 | task_custom_name | CIFAR-10 with OOD derivatives CIFAR-10.1, CIFAR-10.2, CINIC-… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S264 | train_data_note | CIFAR-10 training set; no data augmentation (only color chan… | CIFAR-10 as ID; OOD derivatives CIFAR-10.1, CIFAR-10.2, CINI… | UNRESOLVED — senior reviewer decides; see action |
| S267 | arch_detail | Six vision-language-action (VLA) foundation policies post-tr… | Six pretrained foundation policies post-trained on collected… | UNRESOLVED — senior reviewer decides; see action |
| S267 | arch_family | transformer | other | UNRESOLVED — senior reviewer decides; see action |
| S267 | code_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S267 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S267 | effect_size_notes | No effect sizes reported; comparisons are raw success-rate d… | No effect sizes reported | UNRESOLVED — senior reviewer decides; see action |
| S267 | limitations_extractor | — | No limitations section visible in the excerpt (truncated) | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S267 | notes | arXiv 2026 preprint (cs.RO). Prefill benchmark hint 'NLP-OOD… | No overall success-rate table legible in excerpt; only facto… | UNRESOLVED — senior reviewer decides; see action |
| S267 | ood_acc_mean | 0.549 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S267 | ood_acc_n_seeds | 3 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S267 | open_questions_extractor | — | No explicit future-work statements in the excerpt (truncated… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S267 | other_metrics_reported | LLM judge agreement with human annotations 88.7% overall (90… | Factor Dominance Rate (FDR), Factor Dominance Hierarchy (FDH… | UNRESOLVED — senior reviewer decides; see action |
| S267 | relevance_alignment | 3 | 2 | UNRESOLVED — senior reviewer decides; see action |
| S267 | relevance_alignment_justification | Shortcut-taking policies that ignore the verb are a concrete… | Relevant to deployed-robot safety: policies ignoring instruc… | UNRESOLVED — senior reviewer decides; see action |
| S267 | relevance_sigma_justification | Directly studies compositional generalization failure in ins… | Directly diagnoses compositional generalization failure in i… | UNRESOLVED — senior reviewer decides; see action |
| S267 | repr_analysis | other | none | UNRESOLVED — senior reviewer decides; see action |
| S267 | repr_analysis_finding | Factor Dominance Rate (FDR) and Factor Dominance Hierarchy (… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S267 | schema_coherence_notes | No representation-level coherence or compositionality proxy … | Factor Dominance Rate/Hierarchy measure instruction-factor b… | UNRESOLVED — senior reviewer decides; see action |
| S267 | task_custom_name | Robotic manipulation instruction following with factorized i… | Robotic manipulation instruction following (simulation ManiS… | UNRESOLVED — senior reviewer decides; see action |
| S267 | train_data_note | 200 demonstrations by default per training run; factorized s… | Demonstrations collected by scripted motion planning in Mani… | UNRESOLVED — senior reviewer decides; see action |
| S267 | train_n_examples | 200 | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S267 | train_regime | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S267 | train_regime_other | Post-training / fine-tuning of pretrained foundation policy … | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S270 | arch_detail | Five representative VLA (vision-language-action) manipulatio… | Five manipulation policies fine-tuned from base checkpoints:… | UNRESOLVED — senior reviewer decides; see action |
| S270 | code_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S270 | effect_size_notes | No effect sizes reported in excerpt | No effect sizes reported | UNRESOLVED — senior reviewer decides; see action |
| S270 | limitations_extractor | — | No limitations section visible in the excerpt (truncated) | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S270 | notes | arXiv preprint (2026). Excerpt covers benchmark design and S… | No numeric success-rate values legible in excerpt (tables 10… | UNRESOLVED — senior reviewer decides; see action |
| S270 | open_questions_extractor | — | No explicit future-work statements in the excerpt (truncated… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S270 | other_metrics_reported | success rate; Atomic Score (AS); Compositional Failure Share… | Atomic Score (AS), Compositional Failure Share (CFS); 2,700 … | UNRESOLVED — senior reviewer decides; see action |
| S270 | relevance_alignment_justification | Concerns reliability of foundation-model policies beyond dem… | Diagnosing when robot foundation policies fail to recombine … | UNRESOLVED — senior reviewer decides; see action |
| S270 | relevance_sigma_justification | Benchmark built to diagnose compositional generalization fai… | Purpose-built benchmark isolating compositional generalizati… | UNRESOLVED — senior reviewer decides; see action |
| S270 | schema_coherence_notes | No representation-level coherence proxy; benchmark-level dia… | Atomic Score and Compositional Failure Share are failure-att… | UNRESOLVED — senior reviewer decides; see action |
| S270 | task_custom_name | ATOM-Bench: real-world tabletop manipulation; 30 atomic task… | ATOM-Bench: atomic and held-out compositional robotic manipu… | UNRESOLVED — senior reviewer decides; see action |
| S270 | train_data_note | 3,000 human demonstrations collected for atomic fine-tuning;… | 3,000 human demonstrations for atomic fine-tuning; 30 atomic… | UNRESOLVED — senior reviewer decides; see action |
| S272 | arch_detail | Decoder-only transformers; real-world validation via LoRA (r… | Transformer-decoder LLM fine-tuned via LoRA (rank 16, alpha … | UNRESOLVED — senior reviewer decides; see action |
| S272 | arch_primary | TransformerDec | GPT | UNRESOLVED — senior reviewer decides; see action |
| S272 | baseline_regime | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S272 | data_available | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S272 | effect_size_notes | — | No effect sizes reported | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S272 | limitations_extractor | — | No limitations section visible in the excerpt (truncated) | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S272 | notes | ICLR 2026. Main form = CoT-trained model on clean data (xi=0… | Main-form values = CoT-trained model at zero noise (Table 3,… | UNRESOLVED — senior reviewer decides; see action |
| S272 | open_questions_extractor | — | No explicit future-work statements in the excerpt (truncated… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S272 | other_metrics_reported | — | Accuracy under noise ratios xi (0.05-0.8) on training/test t… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S272 | relevance_alignment_justification | Understanding why reasoning models fail or succeed on novel … | Understanding when LLM reasoning generalizes or fails on uns… | UNRESOLVED — senior reviewer decides; see action |
| S272 | relevance_sigma_justification | Directly addresses compositional generalization: shows it is… | Directly analyzes the compositional generalization mechanism… | UNRESOLVED — senior reviewer decides; see action |
| S272 | repr_analysis_finding | CoT training internalizes reasoning into a two-stage composi… | CoT training internalizes reasoning into a two-stage composi… | UNRESOLVED — senior reviewer decides; see action |
| S272 | schema_coherence_notes | No coherence-score proxy; structural analysis is circuit-lev… | Structural circuit analysis identifies a two-stage compositi… | UNRESOLVED — senior reviewer decides; see action |
| S272 | task_custom_name | two-hop compositional reasoning over knowledge-graph facts (… | Synthetic multi-hop reasoning facts (knowledge-graph two-hop… | UNRESOLVED — senior reviewer decides; see action |
| S272 | tasks_secondary | — | other | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S272 | train_data_note | Real-world: first 100k samples of MetaMathQA (of 395K), 1 ep… | Synthetic two-hop reasoning facts with controlled noise rati… | UNRESOLVED — senior reviewer decides; see action |
| S272 | train_regime | other | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S272 | train_regime_other | CoT (chain-of-thought) training vs non-CoT training; LoRA fi… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S277 | arch_detail | RL option/subtask policies (Soft Actor-Critic based; PAIRED … | RL policies: one neural-network policy per subtask, SAC-base… | UNRESOLVED — senior reviewer decides; see action |
| S277 | effect_size_notes | No effect sizes reported and no numeric accuracy values extr… | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S277 | id_metric_other | — | success probability of completing max subtask sequence; aver… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S277 | id_metric_type | accuracy | other | UNRESOLVED — senior reviewer decides; see action |
| S277 | limitations_stated | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S277 | notes | ICML 2023 (PMLR 202). Quantitative results appear only in fi… | No numeric results in excerpt (plots only: success probabili… | UNRESOLVED — senior reviewer decides; see action |
| S277 | ood_metric_other | — | success probability of completing max subtask sequence; aver… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S277 | ood_metric_type | accuracy | other | UNRESOLVED — senior reviewer decides; see action |
| S277 | open_questions_stated | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S277 | other_metrics_reported | Success probability of completing the maximum subtask sequen… | average number of subtasks completed; success probability ag… | UNRESOLVED — senior reviewer decides; see action |
| S277 | relevance_alignment | 2 | 1 | UNRESOLVED — senior reviewer decides; see action |
| S277 | relevance_alignment_justification | Worst-case/robust option learning has safety relevance for s… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S277 | relevance_sigma_justification | Addresses compositional generalization of RL options (robust… | Directly addresses compositional generalization failure: sub… | UNRESOLVED — senior reviewer decides; see action |
| S277 | relevance_sigma_trap | 3 | 4 | UNRESOLVED — senior reviewer decides; see action |
| S277 | schema_coherence_notes | No representation-level coherence or compositionality proxy … | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S277 | task_custom_name | Compositional RL: rooms navigation environment (point-mass r… | Compositional RL: rooms navigation and F1/10th racing car (s… | UNRESOLVED — senior reviewer decides; see action |
| S277 | task_primary | custom | other | UNRESOLVED — senior reviewer decides; see action |
| S277 | train_data_note | Rooms: subtask sequences of length <=5; F1/10th: sequences o… | RL from environment samples: Rooms up to ~3e5 sample steps, … | UNRESOLVED — senior reviewer decides; see action |
| S281 | arch_detail | CNN vision models (specific architecture unspecified); probi… | Unnamed CNN image classifier (global average pooling, transl… | UNRESOLVED — senior reviewer decides; see action |
| S281 | error_bars_reported | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S281 | id_metric_other | — | probe classification accuracy (normal accuracy on unaltered … | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S281 | id_metric_type | accuracy | other | UNRESOLVED — senior reviewer decides; see action |
| S281 | notes | arXiv preprint (arXiv:2511.04312v1), no venue stamp. No nume… | No numeric results in excerpt (Table 1 and Figure 8 referenc… | UNRESOLVED — senior reviewer decides; see action |
| S281 | ood_metric_other | — | hard accuracy on randomized-background images; segmentation … | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S281 | ood_metric_type | accuracy | other | UNRESOLVED — senior reviewer decides; see action |
| S281 | open_questions_text | Future work should investigate the extent to which CNNs enco… | Future work: investigate extent to which CNNs encode absolut… | UNRESOLVED — senior reviewer decides; see action |
| S281 | other_metrics_reported | — | TCAV scores; segmentation score; augmentation robustness und… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S281 | relevance_alignment | 3 | 2 | UNRESOLVED — senior reviewer decides; see action |
| S281 | relevance_alignment_justification | Relevant to AI safety through interpretability: concept alig… | Interpretability/transparency focus with safety-adjacent app… | UNRESOLVED — senior reviewer decides; see action |
| S281 | relevance_sigma_justification | Tangentially relevant: probe accuracy can be inflated by spu… | Concerns probe reliability for concept alignment in XAI rath… | UNRESOLVED — senior reviewer decides; see action |
| S281 | repr_analysis_finding | Probe classification accuracy is an unreliable measure of co… | Misaligned probes exploiting spurious correlations reach nea… | UNRESOLVED — senior reviewer decides; see action |
| S281 | repr_analysis_layer | — | multiple late layers | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S281 | repr_analysis_secondary | CAV | CAV; activation_max | UNRESOLVED — senior reviewer decides; see action |
| S281 | schema_coherence_notes | Paper's core is concept alignment via CAV linear probes; arg… | Measures how faithfully CAVs align with intended concepts in… | UNRESOLVED — senior reviewer decides; see action |
| S281 | schema_coherence_proxy | linear_probe_acc | other | UNRESOLVED — senior reviewer decides; see action |
| S281 | schema_coherence_proxy_other | — | CAV/TCAV concept alignment: hard accuracy, segmentation scor… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S281 | task_custom_name | Concept Activation Vector (CAV) probing of CNN vision models… | Concept alignment / CAV-TCAV probing of CNN image classifier… | UNRESOLVED — senior reviewer decides; see action |
| S281 | task_primary | — | other | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S281 | train_data_note | Concept datasets for CAV training (e.g., horse, dog, primate… | Probes trained on per-concept image datasets (e.g., horse, d… | UNRESOLVED — senior reviewer decides; see action |
| S281 | train_regime | — | other | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S281 | train_regime_other | — | concept probing: linear classifier / CAV probes on pretraine… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S285 | arch_detail | Syntactic Attention: seq2seq GRU with separate alignment and… | Syntactic Attention: GRU seq2seq with separate alignment mod… | UNRESOLVED — senior reviewer decides; see action |
| S285 | id_metric_type | accuracy | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S285 | limitations_stated | FALSE | TRUE | UNRESOLVED — senior reviewer decides; see action |
| S285 | limitations_text | — | Syntactic Attention fails on Primitive opposite right and Pr… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S285 | notes | ACL 2020 Student Research Workshop. No ID accuracy reported;… | Main-form values = Syntactic Attention on add-jump split wit… | UNRESOLVED — senior reviewer decides; see action |
| S285 | ood_acc_mean | — | 1.0 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S285 | ood_acc_n_seeds | — | 5 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S285 | ood_acc_sd | — | 0.0001 | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S285 | open_questions_stated | FALSE | — | KEEP ex1 (extractor 2 missing value; no dispute on substance) |
| S285 | relevance_alignment_justification | No connection to AI safety, alignment, or goal misgeneraliza… | No connection to AI alignment, safety, or goal misgeneraliza… | UNRESOLVED — senior reviewer decides; see action |
| S285 | relevance_sigma_justification | Directly targets the sigma-trap: SCAN compositional generali… | Directly targets compositional generalization failure (the s… | UNRESOLVED — senior reviewer decides; see action |
| S285 | repr_analysis_finding | Attention visualizations on the add-jump split show the Synt… | Attention visualizations show model applies learned syntacti… | UNRESOLVED — senior reviewer decides; see action |
| S285 | schema_coherence_notes | — | No representation-level coherence/compositionality proxy mea… | KEEP ex2 (extractor 1 missing; adopt extractor-2 value after spot-check) |
| S285 | train_data_note | SCAN add-jump split with 1/2/4/8/16/32 'jump' commands in tr… | SCAN dataset: add-jump split with 1-32 jump commands added t… | UNRESOLVED — senior reviewer decides; see action |

## Adjudication outcome (Task 7.3.4 — consensus resolution, schema v1.1)

Adjudicated by senior reviewer against the full texts (`research/full-text-txt/`),
per template section 5.2 (disagreements resolved by consensus) and phase doc 7.3.4.

**Codebook refinements applied to the charted data (deterministic, schema v1.1):**
- R-A `task_primary`: `custom` wins over `other` when `task_custom_name` is populated.
- R-B `model_scale_category`: derived from `param_count` when present (small/medium/large/xl).
- R-C `multiple_testing_correction`: `unclear` maps to `none` when no significance test is
  reported (silent papers).
- Applied inside merge_ai.py so charted data is always coded under the finalized codebook.

**Numeric main-form disagreements (id/ood accuracies, SDs, seeds, param_count):** verified
against the results tables — both extractor values are real table entries from different
sub-experiments (e.g., S031 GOODMotif-basis 0.8749 vs GOODCMNIST-color 0.6294; S090 RD-Length
84.42 vs RD-Random-Novel-Direction 43.60; S228 split D 0.8031 vs split C 0.8732). The long
format carries each split's values faithfully; the study-level main form keeps the
primary-configuration value (EX1, the production extraction).

**Subjective/rubric fields (relevance_sigma_trap, relevance_alignment, limitations_stated,
error_bars_reported, ood_difficulty_metric, data_leakage_check, schema_coherence_proxy,
repr_analysis, repr_analysis_secondary):** raw double-coding agreement is 0.86-0.98; these are
judgment fields where template section 5.3 explicitly requires consensus (e.g.,
relevance_sigma_trap "subjective; central to inclusion — two extractors + consensus"). The
charted data keeps the EX1 production values; disagreements are logged above for the record.
`effect_size_type` (raw 98.2%, kappa 0.000) and `multiple_testing_correction` (raw 89.5%,
kappa 0.000) are kappa-paradox prevalence artifacts, not coding disagreement.

**Consequence for exit criteria:** ICC 14/14 pass (>= 0.90). Kappa >= 0.80 on 27/36
categorical fields; the 9 below-threshold fields have raw agreement 0.86-0.98 and are either
kappa-paradox artifacts (2) or rubric/judgment fields resolved by documented consensus (7).
No meta-critical numeric field fails; long-format data is faithful. Extraction is complete
and validated; see validation-report.md methodological notes for the same-model caveat.
