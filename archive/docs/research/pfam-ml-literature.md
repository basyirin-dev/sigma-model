# Pfam in Protein ML Benchmarks — Literature Review

> **Source**: Literature review using Consensus AI (Jun 2026)
> **Purpose**: Inform baseline selection and novelty claim in the paper
> **Version target**: Pfam 38.2

---

## Overview

Pfam has been used in protein machine learning in four main ways:

1. **Pretraining corpus** — massive unlabeled sequence collection for self-supervised learning (TAPE, ProtBERT)
2. **Supervised family classification** — family-level annotation as a benchmark task (ProtCNN/ProtENN, ET-Pfam, GNN2Pfam)
3. **OOD / remote homology stress test** — split strategies that test generalization to evolutionarily distant proteins (TAPE held-out families, 25% identity clustering)
4. **Domain architecture reference** — structural and domain-level evaluation of whether models recover biologically meaningful boundaries (DPAM-AI, CATHe, ProtENN2)

---

## 1. Benchmark Landscape

### 1.1 TAPE (Tasks Assessing Protein Embeddings)

TAPE established the principle that protein ML splits should reflect **evolutionary distance** rather than naive random partitioning [Rao 2019].

| Feature | Detail |
|---------|--------|
| Pfam role | Unlabeled pretraining corpus (31 million protein domains) |
| Pretraining splits | Random 95/5 ID split + fully held-out families (~1% of data) for OOD perplexity |
| Supervised tasks | Not Pfam-family classification (secondary structure, contact prediction, remote homology, fluorescence, stability) |
| Key contribution | Established family-level holdout as an OOD evaluation protocol |

TAPE's remote homology task is fold-level rather than Pfam-family-level, making it one of the first structure-aware OOD evaluations in protein ML [Rao 2019; Brandes 2021].

### 1.2 PEER and DeepProtein

PEER is a multitask benchmark covering function, localization, structure, PPI, and protein–ligand interaction tasks [Xu 2022]. It is not Pfam-native but packages Pfam-derived tasks within its suite. DeepProtein inherits from PEER and TDC, adding a unified library layer rather than new Pfam-specific benchmarks [Xie 2024].

### 1.3 ProtCNN / ProtENN Line (Pfam Family Classification)

The dedicated Pfam family-classification benchmark:

| Study | Families | Split | Best Error |
|-------|----------|-------|------------|
| ProtCNN [Bileschi 2019] | 17,929 | 25% identity clustered within family | 27.6% |
| ProtENN [Bileschi 2019] | 17,929 | 25% identity clustered within family | 12.2% |
| LLM4Pfam [Vitale 2024] | 17,929 (1.3M train, 21K test) | 25% identity clustered | Evaluates LLMs |
| ET-Pfam [Escudero 2025] | 17,929 (1.06M train, 16K test) | 25% identity clustered | 7.00% (ensemble) |
| GNN2Pfam [Fenoy 2025] | 17,929 | 25% identity clustered | Median recall on hard subset |

**ProtCNN/ProtENN design**: Deep residual CNN over unaligned sequences, trained on Pfam seed + full alignment data. After filtering for families with ≥50 members, 17,929 families remain. Within-family 25% sequence identity clustering ensures test proteins are remote homologs of training proteins [Bileschi 2019].

**ET-Pfam improvement**: Family-weighted ensemble voting over multiple LLM embeddings + CNNs reduces error from 12.91% (best individual deep model) to 7.00% [Escudero 2025].

### 1.4 Structural Validation Benchmarks

Studies using Pfam as a structural/domain reference rather than a classification target:

| Study | Pfam Role | Split | Metric |
|-------|-----------|-------|--------|
| DMPfold [Greener 2018] | Validation set of 1,154 families with known structures | Non-homologous to training | TM-score ≥0.5 |
| CATHe [Nallapareddy 2022] | Pfam-annotated but CATH-unclassified domains | <20% identity remote homology | Structural superfamily assignment |
| DPAM-AI [Durham 2024] | Pfam 36 domain annotations | Predicted vs annotated | >50% reciprocal overlap |

---

## 2. Pfam Split Strategies

| Strategy | Typical Pfam Use | What It Tests | Known Weakness |
|----------|------------------|---------------|----------------|
| **Random sequence split** | Pfam seed family classification (e.g., DeepHiFam) [Sandaruwan 2021] | In-distribution classification | Inflated by close homologs in both train/test [Vitale 2024] |
| **Held-out family split** | TAPE pretraining corpus [Rao 2019] | OOD generalization across families | Still sequence-only, not structural novelty |
| **25% identity clustered split** | ProtCNN/ProtENN, LLM4Pfam, ET-Pfam, GNN2Pfam [Vitale 2024; Escudero 2025; Fenoy 2025] | Remote homology annotation | Severe imbalance across families; some absent from train |
| **Fold-level / structural split** | TAPE remote homology, CATHe, CATH/ECOD tests [Rao 2019; Nallapareddy 2022] | Structural generalization beyond family similarity | Less directly aligned with Pfam labels |

**Representative dataset sizes (25% identity clustered)**:

| Study | Train | Dev | Test | Families |
|-------|-------|-----|------|----------|
| LLM4Pfam [Vitale 2024] | 1,339,083 | 10% of train | 21,293 | 17,929 |
| ET-Pfam [Escudero 2025] | 1,063,492 | 16,675 | 16,343 | 17,929 |
| GNN2Pfam [Fenoy 2025] | — | — | — | 17,929 (58-family hard subset) |

---

## 3. Evaluation Methodologies

| Benchmark | Metric | Scale |
|-----------|--------|-------|
| ProtCNN/ProtENN | Top-1 error rate | 17,929 families |
| ET-Pfam | Family-weighted ensemble error (7.00%) | 17,929 families |
| LLM4Pfam | Error rate per LLM | 17,929 families |
| TAPE | Perplexity (ID + held-out family) | 31M domains |
| GNN2Pfam | Median recall (full + hard subset) | 17,929 families |
| ProtENN2 [Paysan-Lafosse 2024] | Residue-level family assignment across 19,632 families, 655 clans | Full UniProt reference proteomes |
| DPAM-AI | >50% reciprocal overlap | 52,673 Pfam domains |
| DMPfold | TM-score ≥0.5 | 1,154 families |

**Key observation**: Error rate and accuracy dominate the Pfam classification literature. Boundary quality, calibration, and false negative rates are underreported [Vitale 2024; Paysan-Lafosse 2024]. Domain architecture evaluation (DPAM-AI's overlap criterion) is a separate tradition from sequence-level family classification.

---

## 4. Domain Architecture Benchmarks

### 4.1 DPAM-AI: Pfam vs Structural Domain Boundaries

DPAM-AI mapped predicted structural domains onto Pfam 36 annotations [Durham 2024]:

- **15.4%** of 52,673 Pfam domains split into multiple structural domains
- Many Pfam functional domains are **not one-to-one** with structural units
- This label mismatch between function-oriented (Pfam) and structure-oriented definitions is a known issue

### 4.2 ProtENN2 and AI-Assisted Curation

ProtENN2 performs residue-level family assignment over 19,632 Pfam families and 655 clans, then converts contiguous predictions of ≥20 residues into domain calls [Paysan-Lafosse 2024]. This expanded UniProt reference-proteome coverage beyond standard Pfam and suppressed false positives by removing overlapping predictions from non-homologous families in different clans.

AI-driven curation has even created new Pfam families: **190 new families** were added in one study examining AI-classified candidate novel folds [Pei 2025].

### 4.3 Clustering Within Clans

Unsupervised clustering within Pfam clans (density peak clustering) found both strong agreement with manual family annotation and biologically meaningful disagreements suggesting new domains or revised boundaries [Russo 2021].

### 4.4 Family Relationship Discovery

ProtENN2-derived family embeddings evaluated for refining clan membership, using structure comparison as validation. Additional neural-network predictions beyond existing Pfam HMM calls improved family-embedding performance [Ponamareva 2024].

---

## 5. Failure Modes

### 5.1 Homology Leakage (Random Splits)

Random train/test splits place very similar homologs on both sides, allowing memorisation and overoptimistic performance [Vitale 2024; Escudero 2025; Guvenilir 2023]. This is the best-established failure mode. Random splits routinely report 97–99% accuracy on 1,000–3,000 families [Sandaruwan 2021; Golenko 2022], but this reflects within-family recognition, not true generalization.

### 5.2 Partition Imbalance

Identity-clustered Pfam splits can leave some families absent from training or heavily skewed across partitions [Escudero 2025]. This motivated balanced subsets like ET-Pfam's mini-dataset and GNN2Pfam's 58-family hard subset [Fenoy 2025].

### 5.3 Metric Mismatch

- Error rate does not account for false negatives
- High whole-sequence accuracy can hide poor residue-level or boundary-level behavior [Vitale 2024; Paysan-Lafosse 2024]
- Models can be "wrong" relative to Pfam while exposing real structural subdivisions absent from current curation [Ponamareva 2024; Durham 2024]

### 5.4 Twilight Zone / Weak Generalization

Protein family methods remain less accurate for low-similarity proteins, motivating dedicated twilight-zone models [Kabir 2022]. Even strong pretraining does not uniformly dominate simple baselines: on TAPE tasks, self-supervised models sometimes lagged state-of-the-art non-neural features, and linear/CNN baselines could rival pretrained models on fluorescence [Rao 2019; Shanehsazzadeh 2020].

### 5.5 Label-Structure Mismatch

Pfam's functional labels do not always align with structural domains [Paysan-Lafosse 2024; Durham 2024]. Many single Pfam domains contain multiple structural or evolutionary units, and repeat-rich proteins are especially problematic. Pfam curation itself notes that some large entries should be split.

---

## 6. Benchmark Gaps

| Gap | Evidence | Why It Matters |
|-----|----------|----------------|
| **Few true cross-family OOD tests** | TAPE has held-out families, but many classifiers still use random/within-family splits [Rao 2019; Sandaruwan 2021] | Reported accuracy often overstates deployment performance |
| **Limited structure-aware Pfam benchmarks** | Domain parsers and structure transfer studies exist but are separate from mainstream sequence benchmarks [Durham 2024; Nallapareddy 2022] | Sequence-only metrics miss boundary and architecture errors |
| **Imbalance and sparse families** | Some Pfam families lack enough examples for robust pHMMs or balanced ML partitions [Escudero 2025] | Rare-family performance remains undermeasured |
| **Metrics favour top-1 classification** | Error rate and accuracy dominate [Vitale 2024; Golenko 2022] | Boundary quality, calibration, false negatives underreported |
| **No recombination-distance-controlled splits** | No existing benchmark systematically varies how "novel" a domain combination is | Missing: the compositional generalisation axis |

---

## 7. Implications for Sigma-Model

### 7.1 Baseline Selection

The ProtENN/ET-Pfam benchmark line provides SOTA error rates on Pfam family classification (7.00% for ET-Pfam [Escudero 2025]; 12.2% for ProtENN [Bileschi 2019]). However, these are **not directly comparable** — they evaluate family-level remote homology annotation, not domain-architecture prediction. They establish that the 17,929-family 25%-identity-clustered split is the gold standard for OOD evaluation in Pfam ML; the sigma-model should cite this lineage as the closest existing benchmark while noting the task difference.

### 7.2 Novelty Claim

The gap analysis above directly motivates three novelty claims:

1. **PfamCG-1.0** is the first benchmark that systematically varies domain-combination **recombination distance** (Type A/B/C) rather than relying on sequence identity or family holdout alone.
2. **ΔCG** (compositional gap = ID accuracy − OOD accuracy) is a metric absent from the Pfam ML literature, which overwhelmingly reports top-1 error or accuracy without paired ID/OOD comparison.
3. **σ_A** provides a quantitative proxy for domain recombination compatibility — the literature's biggest gap is "Universal fold-compatibility rules are not established" (evidence strength 2/10 per A.2 review).

### 7.3 Caveat: Label-Structure Mismatch

DPAM-AI's finding that 15.4% of Pfam domains split into multiple structural domains [Durham 2024] is a caveat for the sigma-model. If Pfam's domain boundaries do not always correspond to structural units, then the model's domain-architecture predictions may be "correct" by one definition (structural) while "wrong" by another (Pfam). The paper should acknowledge this and, where possible, validate key results against structural domain annotations.

### 7.4 Split Construction Guidance

The 25% identity clustering method from the Pfam annotation benchmark provides a template for constructing non-leaky splits. The sigma-model's Type A/B/C splits should additionally apply this within each family to ensure that no held-out architecture shares >25% sequence identity with a training architecture.

### 7.5 Metric Positioning

The sigma-model uses **ID accuracy**, **OOD accuracy**, and **ΔCG** as primary metrics. The literature overwhelmingly uses top-1 error or accuracy. The sigma-model should:
- Report error rate alongside ΔCG for comparability with ProtENN/ET-Pfam
- Use the paired (ID, OOD) framing as a differentiator — no existing benchmark reports both and their difference

---

## 8. Implications for NeurIPS Paper

The target paper (`paper-neurips/main.tex`, "The Σ-Model in Protein Domain Architectures") is currently a skeleton with all sections as placeholders. The Pfam ML literature surveyed here fills the substance for:

- **§8 (Related Work)**: Pfam ML benchmarks subsection — describe ProtENN/ET-Pfam line as the closest existing OOD evaluation, then detail gaps that PfamCG-1.0 fills
- **§3 (Pfam Test Bed)**: Cite 25% identity clustering methodology as template for non-leaky split construction
- **§8 (Limitations)**: Cite DPAM-AI label-structure mismatch (15.4% of Pfam domains split into multiple structural domains) as a caveat for domain architecture evaluation
- **§8 (Baselines)**: Cite ProtENN error rates (12.2%) and ET-Pfam (7.00%) as SOTA for family-level annotation, noting task differences

Note: `paper-neurips/bibliography.bib` already references `mistry2021pfam`, `rives2021esm`, and `lin2023esm2`. The remaining ~18 papers are new citations for the NeurIPS paper.

---

## References

Bileschi, M. L., Belanger, D., Bryant, D., Sanderson, T., Carter, B., Sculley, D., Bateman, A., DePristo, M., & Colwell, L. J. (2019). Using deep learning to annotate the protein universe. *Nature Biotechnology*, 40, 932–937. doi:10.1038/s41587-021-01179-w

Brandes, N., Ofer, D., Peleg, Y., Rappoport, N., & Linial, M. (2021). ProteinBERT: a universal deep-learning model of protein sequence and function. *Bioinformatics*, 38, 2102–2110. doi:10.1093/bioinformatics/btac020

Durham, J., Zhang, J., Schaeffer, R. D., & Cong, Q. (2024). DPAM-AI: a domain parser for AlphaFold models powered by artificial intelligence. *Bioinformatics*, 41. doi:10.1093/bioinformatics/btae740

Escudero, S., Duarte, S., Vitale, R., Fenoy, E., Bugnon, L., Milone, D. H., & Stegmayer, G. (2025). ET-Pfam: ensemble transfer learning for protein family prediction. *Bioinformatics*, 42. doi:10.1101/2025.08.02.668111

Fenoy, E., Bugnon, L., Vitale, R., Duarte, S., Milone, D. H., & Stegmayer, G. (2025). GNN2Pfam: Integrating protein sequence and structure with graph neural networks for Pfam domain annotation. *bioRxiv*. doi:10.1101/2025.09.18.677074

Golenko, Y., Ismailova, A., Shaushenova, A., Mutalova, Z., Dossalyanov, D., Ainagulova, A., & Naizagarayeva, A. (2022). Implementation of machine learning models to determine the appropriate model for protein function prediction. *Eastern-European Journal of Enterprise Technologies*. doi:10.15587/1729-4061.2022.263270

Greener, J. G., Kandathil, S., & Jones, D. T. (2018). Deep learning extends de novo protein modelling coverage of genomes using iteratively predicted structural constraints. *Nature Communications*, 10. doi:10.1038/s41467-019-11994-0

Guvenilir, H. A. & Dogan, T. (2023). How to approach machine learning-based prediction of drug/compound–target interactions. *Journal of Cheminformatics*, 15. doi:10.1186/s13321-023-00689-w

Jamasb, A. R., Morehead, A., Joshi, C. K., Zhang, Z., Didi, K., Mathis, S. V., Harris, C., Tang, J., Cheng, J., Liò, P., Blundell, T. L. (2024). Evaluating Representation Learning on the Protein Structure Universe. *arXiv*. doi:10.48550/arxiv.2406.13864

Kabir, M. N. & Wong, L. (2022). EnsembleFam: towards more accurate protein family prediction in the twilight zone. *BMC Bioinformatics*, 23. doi:10.1186/s12859-022-04626-w

Nallapareddy, V., Bordin, N., Sillitoe, I., Heinzinger, M., Littmann, M., Waman, V. P., Sen, N., Rost, B., & Orengo, C. (2022). CATHe: detection of remote homologues for CATH superfamilies using embeddings from protein language models. *Bioinformatics*, 39. doi:10.1093/bioinformatics/btad029

Paysan-Lafosse, T., Andreeva, A., Blum, M., Chuguransky, S., Grego, T., Pinto, B. L., Salazar, G. A., Bileschi, M. L., Llinares-López, F., Meng-Papaxanthos, L., Colwell, L. J., Grishin, N. V., Schaeffer, R. D., Clementel, D., Tosatto, S. C. E., Sonhammer, E., Wood, V., & Bateman, A. (2024). The Pfam protein families database: embracing AI/ML. *Nucleic Acids Research*, 53, D523–D534. doi:10.1093/nar/gkae997

Pei, J., Andreeva, A., Grego, T., Chuguransky, S., Pinto, B. L., Flores, N. M., Paysan-Lafosse, T., Schaeffer, R. D., Bateman, A., Cong, Q., & Grishin, N. V. (2025). Exploring the Terra incognita of AI-based domain classifications. *Protein Science*, 34. doi:10.1002/pro.70392

Ponamareva, I., Andreeva, A., Bileschi, M. L., Colwell, L. J., & Bateman, A. (2024). Investigation of protein family relationships with deep learning. *Bioinformatics Advances*, 4. doi:10.1093/bioadv/vbae132

Rao, R., Bhattacharya, N., Thomas, N., Duan, Y., Chen, X., Canny, J., Abbeel, P., & Song, Y. S. (2019). Evaluating Protein Transfer Learning with TAPE. *Advances in Neural Information Processing Systems*, 32, 9689–9701. doi:10.1101/676825

Russo, E. T., Laio, A., & Punta, M. (2021). Density Peak clustering of protein sequences associated to a Pfam clan reveals clear similarities and interesting differences with respect to manual family annotation. *BMC Bioinformatics*, 22. doi:10.1186/s12859-021-04013-x

Sandaruwan, P. D. & Wannige, C. T. (2021). An improved deep learning model for hierarchical classification of protein families. *PLoS ONE*, 16. doi:10.1371/journal.pone.0258625

Shanehsazzadeh, A., Belanger, D., & Dohan, D. (2020). Is Transfer Learning Necessary for Protein Landscape Prediction? *arXiv*. doi:10.48550/arxiv.2011.03443

Vitale, R., Bugnon, L., Fenoy, E., Milone, D. H., & Stegmayer, G. (2024). Evaluating large language models for annotating proteins. *Briefings in Bioinformatics*, 25. doi:10.1093/bib/bbae177

Xie, J., Zhao, Y., & Fu, T. (2024). DeepProtein: deep learning library and benchmark for protein sequence learning. *Bioinformatics*, 41. doi:10.1093/bioinformatics/btaf165

Xu, M., Zhang, Z., Lu, J., Zhu, Z., Zhang, Y., Ma, C., Liu, R., & Tang, J. (2022). PEER: A Comprehensive and Multi-Task Benchmark for Protein Sequence Understanding. *arXiv*. doi:10.48550/arxiv.2206.02096
