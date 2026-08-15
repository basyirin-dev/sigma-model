# Protein Domain ML Research Reference

## 1. Pfam: Structure, Pfam-A vs Pfam-B, Data Access

### What is Pfam?
Pfam is a database of protein families, each represented by **multiple sequence alignments** and **profile hidden Markov models (HMMs)**. It is the most widely used resource for classifying protein sequences into families and domains. Since 2024, the Pfam website has been **decommissioned** and all data is served through **InterPro** (https://www.ebi.ac.uk/interpro/).

### Pfam-A vs Pfam-B
- **Pfam-A**: Curated, high-quality entries. Each family has a manually curated *seed alignment* (small representative set), a profile HMM built from it, and an automatically generated *full alignment* of all detectable sequences. ~21,979 families in v38.2 (June 2024).
- **Pfam-B**: Automatically generated clusters from UniProtKB, lower quality, not manually curated. Historically ~1/3 of Pfam-A entries originated from Pfam-B clusters. Pfam-B was regenerated in 2021 after being discontinued.
- **Pfam-N**: New deep-learning-based addition (introduced 2025) using neural networks to discover families, achieving +8.8% UniProtKB coverage (Paysan-Lafosse et al., 2025).

### Entry Types
Six types: **Family**, **Domain**, **Repeat**, **Motif**, **Coiled-coil**, **Disordered**. Related entries are grouped into **Clans** based on sequence, structure, or HMM similarity.

### Data Access URLs
| Resource | URL |
|----------|-----|
| InterPro (new home) | https://www.ebi.ac.uk/interpro/ |
| Browse Pfam entries | https://www.ebi.ac.uk/interpro/entry/pfam/ |
| Pfam FTP root | https://ftp.ebi.ac.uk/pub/databases/Pfam/ |
| Pfam-A HMM models | https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz |
| Pfam-A seed alignments | https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.seed.gz |
| Pfam-A full alignments | https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.full.gz |
| Pfam-A HMM metadata | https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.dat.gz |
| Release notes | https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/relnotes.txt |
| Pfam docs | https://pfam-docs.readthedocs.io/ |
| Pfam Xfam blog | https://xfam.wordpress.com/ |

### Key Papers
- **2025**: Paysan-Lafosse et al., "Pfam: embracing AI/ML", *Nucleic Acids Res.* 53(D1). PMID: 39540428
- **2021**: Mistry et al., "Pfam in 2021", *Nucleic Acids Res.* 49(D1). PMID: 33125078
- **Original**: Sonnhammer, Eddy, Durbin (1997), *Proteins* 28(3):405-420

---

## 2. Protein Domain Architectures

### Definition
A **protein domain architecture** is the linear ordering of domains along a protein sequence. Since domains are evolutionary units that fold independently, their arrangement defines protein function. Example: `C2-WW-HECTc` is the architecture of E3 ubiquitin ligases.

### Computational Representation
- **String/Sequence**: Ordered list of Pfam accessions, e.g., `"PF00168-PF00041-PF00632"` (C2-WW-HECTc)
- **Bigram features**: Adjacent domain pairs (`"C2-WW"`, `"WW-HECTc"`) used as features
- **Graph representation**: Nodes = domains, edges = co-occurrence in same protein (weighted by frequency)
- **Vector embedding**: Cosine similarity over domain presence/absence vectors; or weighted by domain versatility (WDAC method; Lin et al., 2009, PMC2788356)
- **One-hot encoding**: Binary vector of length N (N = total Pfam families) with 1 at positions corresponding to domains in the protein

### Key Resources
- **CDART** (NCBI): Domain architecture retrieval tool
- **SMART v10**: Mobile domain architectures (https://smart.embl.de/)
- **iPfam**: Domain-domain interactions mapped to PDB structures
- **Pfam architecture browser**: https://www.ebi.ac.uk/interpro/protein/UniProt/entry/pfam/

---

## 3. HMMER and Bit Scores

### What is HMMER?
HMMER (http://hmmer.org/) is a software suite for biosequence analysis using profile hidden Markov models. Developed by Sean Eddy's group. Current version: **3.4** (2024).

### Key Programs
| Program | Function |
|---------|----------|
| `phmmer` | Query sequence → protein database (BLASTP-like) |
| `hmmscan` | Query sequence → profile HMM database (Pfam search) |
| `hmmsearch` | Profile HMM → sequence database |
| `jackhmmer` | Iterative search (PSI-BLAST-like) |
| `hmmbuild` | Build profile HMM from MSA |
| `hmmalign` | Align sequences to profile HMM |

### Bit Scores — The Key Mechanism
A **bit score** in HMMER is defined as:

```
bit_score = log₂( P(sequence | model) / P(sequence | null) )
```

It is the log-odds ratio of the sequence's probability under the **profile HMM** (homology hypothesis) vs. the **null model** (non-homology, i.i.d. random sequence). Bit scores are:
- **Additive** across independent domains (the sum of domain bit scores = sequence bit score)
- **Independent of database size** (unlike E-values)
- **Comparable** across different profile HMMs (same units: bits)
- Used for **gathering thresholds** (GA bit score): family-specific curated cutoffs defining membership

Each Pfam entry has **two** gathering thresholds:
- **Sequence GA**: Minimum sequence-level bit score
- **Domain GA**: Minimum per-domain bit score

HMMER3 is ~100× faster than HMMER2 and comparable to BLAST in speed. The 2026 web server update (Rajković et al., 2026) uses React/JS frontend.

---

## 4. ESM Model Family

### Overview
ESM (**E**volutionary **S**cale **M**odeling) is a family of transformer protein language models from Meta AI (FAIR). Architecture: **Transformer encoder** with masked language modeling objective (15% mask), trained on UniRef sequences.

### Model Versions and Sizes

| Model | Parameters | Layers | Released | Training Data | Notes |
|-------|-----------|--------|----------|--------------|-------|
| **ESM-1** | ~670M | 33 | 2019 | UniRef50 (250M seqs) | Original (Rives et al., 2021, PNAS) |
| **ESM-1b** | ~650M | 33 | 2020 | UniRef50 | Regression head for structure |
| **ESM-1v** | ~650M | 33 | 2021 | UniRef90 | 5 ensembles; zero-shot variant prediction |
| **ESM-2** | 8M–3B (6 sizes) | 6–36 | 2022 | UniRef50 (65M unique) | Best single-sequence PLM; rotary embeddings |
| **ESM-2 15B** | 15B | ? | 2023 | UniRef50 | Used by ESMFold; perplexity 6.37 |
| **ESM C** | 300M–6B | — | 2024 | — | Outperforms ESM-2; linear scaling |
| **ESM-3** | 1.4B, 7B, **98B** | — | 2024 | 2.78B proteins | From EvolutionaryScale; multi-track |
| **ESM C (Biohub)** | open | — | 2026 | ≥6.8B proteins | ESM Atlas; sparse autoencoders |

### ESM-2 Specific Sizes
| Params | Layers | Embed Dim | Attention Heads |
|--------|--------|-----------|----------------|
| 8M | 6 | 320 | 8 |
| 35M | 12 | 480 | 8 |
| 150M | 30 | 640 | 20 |
| 650M | 33 | 1280 | 20 |
| 3B | 36 | 2560 | 40 |
| 15B | 48 | 5120 | 40 |

### ESMFold
ESMFold uses ESM-2 as a stem + folding trunk head. Predicts atomistic structures end-to-end from single sequence. ~60× faster than AlphaFold2. Used to create the **ESM Metagenomic Atlas** (>617 million structures).

### References
- ESM-2: Lin et al., *Science* 379(6637):1123-1130 (2023). DOI: 10.1126/science.ade2574
- ESM-1: Rives et al., *PNAS* 118(15):e2016239118 (2021)
- ESM-1v: Meier et al., bioRxiv 2021
- ESM-3: EvolutionaryScale, 2024 (https://www.evolutionaryscale.ai/)
- ESM C: https://www.evolutionaryscale.ai/blog/esm-cambrian
- GitHub: https://github.com/facebookresearch/esm
- PyPI: `pip install fair-esm` (v2.0) or `pip install esm` (ESM-3 SDK)

---

## 5. Existing Benchmarks for Domain Compositional Generalization

### Pfam-based Benchmarks
- **TAPE** (Tasks Assessing Protein Embeddings, 2019): Heldout Pfam families test set (~1% of families). Random 95/5 split for in-distribution; heldout families for OOD generalization. 31M sequences from Pfam pretraining corpus. Paper: Rao et al., NeurIPS 2019.
- **Bileschi et al. (2022)**: Deep learning on 17,929 Pfam families. Benchmark assesses remote homology detection. Found DL + HMMER complementary. Paper: *Nat. Biotechnol.* 40:932-937.
- **Pfam-N**: Benchmark comparing neural-network-discovered families vs standard Pfam HMM-based families. +8.8% coverage gain.
- **Blue/Cobalt splitting algorithms**: Construct benchmarks where no train-test pair exceeds 25% sequence identity. Used for Pfam family splitting.

### CATH Benchmarks
- **CATH S40 non-redundant**: ≤40% sequence identity domain structures. Standard training set for structure prediction (FoldingDiff, AlphaFold).
- **cath_datasets** (wouterboomsma/cath_datasets): Preprocessed numpy arrays for 3-class, 10-architecture, 20-topology classification tasks from CATH.
- **FoldingDiff** (microsoft/foldingdiff): Uses CATH 4.2 S40 for protein backbone diffusion.
- **DPLM** (bytedance/dplm): CATH 4.3 topology splits.

### SCOP Benchmarks
- **SCOP vs CATH comparison**: Only ~70% domain boundary agreement. Benchmark set of consistently classified domains.
- **SCOP 1.75 fold classification**: Standard for fold recognition.
- **TM-align on SCOP/CATH consistent set**: Better benchmarking (avoiding hierarchy inconsistencies).

### Compositional Generalization Gap
No dedicated benchmark for **domain compositional generalization** exists. Key challenge: models must predict architectures (`A-B-C`) unseen during training. Current works test this indirectly via:
- Heldout Pfam families (TAPE)
- Remote homology detection (Bileschi et al.)
- Fold classification (CATH/SCOP)

### URLs
- CATH: https://www.cathdb.info/ | FTP: ftp://orengoftp.biochem.ucl.ac.uk/cath/
- SCOP: https://scop.mrc-lmb.cam.ac.uk/ (SCOP 2)
- TAPE: https://github.com/songlab-cal/tape
- PEER benchmark: https://github.com/DeepGraphLearning/PEER_Benchmark
- DeepProtein: https://github.com/jiaqingxie/DeepProtein

---

## 6. Python Libraries for Protein Sequence Data

| Library | Purpose | Install | Notes |
|---------|---------|---------|-------|
| **Biopython** | General bioinformatics | `pip install biopython` | Seq/SeqRecord, parsers (FASTA, Stockholm, GenBank), HMMER integration, NCBI APIs. v1.87 (2026) |
| **fair-esm** | ESM models | `pip install fair-esm` | ESM-1, ESM-2, ESMFold, MSA Transformer. PyPI v2.0 (2022) |
| **esm** (new) | ESM-3 SDK | `pip install esm` | ESM-3, ESM C from EvolutionaryScale/Biohub |
| **transformers** | HF PLMs | `pip install transformers` | ProtBERT, ProtT5, ESM-1b/ESM-2 via AutoModel |
| **pyhmmer** | HMMER in Python | `pip install pyhmmer` | Python bindings for HMMER3 |
| **MMseqs2** (via Python) | Sequence clustering | `conda install mmseqs2` | Fast clustering for redundancy reduction |
| **protclust** | Cluster-aware splits | `pip install protclust` | MMseqs2 wrapper + dataset splitting |
| **scikit-bio** | Stockholm format | `pip install scikit-bio` | Parsing Stockholm alignment files |
| **DeepProtein** | DL benchmark suite | `pip install deepprotein` | 8 architectures on 8 protein tasks |
| **PEER** | Multi-task benchmark | GitHub only | Protein understanding tasks |
| **BioEmbeddings** | Embedding extraction | `pip install bio-embeddings` | Unified interface for ESM, ProtBERT, etc. |

---

## 7. ML Featurization of Pfam Domain Sequences

### Common Approaches

**A. Sequence-Level Features (per domain)**
- **One-hot encoding**: 20 × L matrix (L = sequence length). Standard baseline.
- **Averaged embeddings**: From ESM-1b/ESM-2 (`mean` or `bos` representations). ESM-2 650M produces 1280-dim per residue; mean pool for fixed-length.
- **Profile HMM features**: Log-odds match scores per position from `hmmsearch` alignment. Captures conservation patterns.
- **PSSM (Position-Specific Scoring Matrix)**: From PSI-BLAST iterative search.
- **Physicochemical properties**: Hydrophobicity, charge, volume, etc. (AAindex).
- **k-mer composition**: Count/frequency of length-k substrings.

**B. Architecture-Level Features (per protein)**
- **Domain order string**: `"PF00001-PF00002-PF00003"`. Used as token sequence for sequence models (like Transformer).
- **Domain bigram matrix**: Co-occurrence of adjacent domains.
- **WDAC (Weighted Domain Architecture Comparison)**: Cosine similarity over domain presence vectors, weighted by domain versatility (inverse promiscuity).
- **Graph embeddings**: Node embeddings from domain co-occurrence networks.

**C. ESM-specific featurizations** (from the `fair-esm` library)
- `per_tok`: Full sequence, embedding per amino acid (seq_len × hidden_dim)
- `mean`: Mean pooled over sequence (hidden_dim)
- `bos`: Beginning-of-sequence token embedding

**D. Deep learning end-to-end**
- Raw sequence → embedding layer → transformer/CNN/RNN
- Raw sequence → ESM (frozen pretrained) → classifier head
- Raw sequence → ESM (fine-tuned) → architecture prediction

**E. Multi-modal**
- Sequence + structure (AlphaFold coordinates) + function (GO terms) input tracks
- ESM-3 uses multi-track: sequence, structure, function simultaneously

---

## 8. Standard Train/Validation Splits in Protein ML

### Most Common Split Strategies

**A. Sequence Identity Thresholds (de facto standard)**
- **30% sequence identity** cluster: Most common for train/test separation. Used by: DeepLoc, PEER benchmark, DeepSol.
- **S40 (CATH)**: ≤40% identity within dataset, standard for structure tasks.
- **Protocol**: Cluster sequences using CD-HIT or MMseqs2 at threshold; assign clusters to train/val/test.

**B. Pfam Family/Clan Split (TAPE)**
- **Random split**: 95% train / 5% test with Pfam families as groups
- **Heldout families** (OOD): ~1% of Pfam families fully withheld
- **Heldout clans**: Entire Pfam clans withheld (harder OOD)

**C. Taxonomy Split**
- Train on sequences from certain species, test on distant ones.

**D. Time-based Split**
- Train on sequences before a cutoff date, test on newer sequences.

### Typical Ratio Conventions
| Split | Size | Notes |
|-------|------|-------|
| Training | 70–80% | |
| Validation | 5–15% | |
| Test | 10–20% | Often 10% for large databases |

### Literature Examples
- **TAPE (Rao et al., 2019)**: 95% train / 5% test (in-distribution) + heldout families (OOD)
- **Bileschi et al. (2022)**: Pfam families split by random seed at family level; 17,929 families
- **PEER (Xu et al., 2022)**: 30% sequence identity threshold, k-fold cross validation
- **ESM-2 (Lin et al., 2023)**: ~500K heldout UniRef50 clusters for evaluation
- **Elnaggar et al. (ProtBERT, 2021)**: 90/10 split at sequence level

### Tools
- **MMseqs2**: `cluster` module for redundancy reduction
- **CD-HIT**: `cd-hit -c 0.3` for 30% threshold
- **Blue/Cobalt algorithms**: Specialized Pfam splitting maintaining identity constraints
- **protclust**: Python wrapper for cluster-aware splitting

---

## 9. Pfam Website: Downloads, Schema, and Seed Alignment Format

### FTP Structure
Root: `https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/`

Key files:
| File | Description |
|------|-------------|
| `Pfam-A.hmm.gz` | Profile HMMs for all Pfam-A entries (HMMER3 format) |
| `Pfam-A.hmm.dat.gz` | Metadata for each HMM (GA thresholds, TC, NC, etc.) |
| `Pfam-A.seed.gz` | Seed alignments (Stockholm format, manually curated) |
| `Pfam-A.full.gz` | Full alignments (Stockholm format, automatically generated) |
| `Pfam-A.fasta.gz` | Full alignment sequences in FASTA |
| `active_site.dat.gz` | Active site annotations |
| `Pfam-A.clans.tsv.gz` | Clan assignments |
| `relnotes.txt` | Release notes |

### Alignment Format: Stockholm
- **Header**: `# STOCKHOLM 1.0`
- **Per-file metadata** (`#=GF`): ID, AC, DE, GA, TC, NC, TP, SQ, etc.
- **Per-sequence metadata** (`#=GS`): AC (accession), DE (description), OS (organism), DR (db ref)
- **Per-column annotation** (`#=GC`): SS_cons (consensus secondary structure)
- **Per-residue annotation** (`#=GR`): SS (secondary structure), SA (surface accessibility), PP (posterior prob)
- **Terminator**: `//`

### Seed vs Full Alignments
- **Seed**: Small, manually curated set of representative sequences. <1% of total. Used for HMM construction.
- **Full**: All sequences matching above gathering threshold. Generated by HMMER search of full UniProtKB.

### Schema Summary (flat-file)
Accession format: `PFxxxxx` (e.g., `PF00001` for 7tm_1). Clan: `CLxxxx`. Each entry has: unique ID (short name), accession, definition, type (Family/Domain/Repeat/Motif), seed source, gathering threshold (GA seq + GA dom bits).

### Pfam-N entries
New system: entries discovered via deep learning, assigned `PFNxxxxx` accessions (preliminary). Available through same FTP.

---

## 10. Fold Compatibility and Domain Neighbour Statistics

### Fold Compatibility
**Definition**: Determining whether a given domain sequence can adopt a known protein fold (3D structure). A domain is "fold compatible" if it can be confidently mapped to a known structural fold (from CATH, SCOP, ECOD).

**Validation methods**:
- **HMMER hit to fold-specific HMM**: Bit score above family gathering threshold
- **Alphafold pLDDT score**: Domains with pLDDT > 70 are usually confidently folded; > 90 is high quality
- **Foldseek structural alignment**: When predicted or experimental structure is available, TM-score > 0.5 indicates same fold
- **ECOD/Pfam harmonization** (2025 Pfam update): Systematic comparison of Pfam domain boundaries against ECOD structural classification; identified 638 missing families
- **Inconsistency detection**: If two different Pfam families match the same ECOD group → merge; if one Pfam family matches multiple ECOD groups → split

### Domain Neighbour Statistics

**Definition**: Statistical analysis of which domains co-occur in the same protein and in what order.

**Key metrics**:
- **Adjacency frequency (bigram)**: Count of domain pairs `(D_i, D_j)` that appear consecutively in architectures. Use permutation tests or z-scores to assess if co-occurrence is significant.
- **Co-occurrence matrix**: N × N matrix where entry (i,j) = number of proteins where domain i and domain j occur together (not necessarily adjacent).
- **Domain versatility (promiscuity)**: Number of distinct domain types a given domain co-occurs with. Used as inverse weight in WDAC (Lin et al., 2009).

**Resources for neighbor statistics**:
- **Pfam architecture browser**: All architectures for each family
- **SMART**: Specializes in mobile domains and their neighbors
- **iPfam**: Domain-domain interactions at interface level
- **STRING**: Functional associations; can be extended to domain level
- **CDART** (NCBI): Domain architecture retrieval tool

**Validation of neighbor statistics**:
1. **Permutation test**: Compare observed domain pair frequency vs. random expectation (shuffle domains across proteins while preserving per-domain counts).
2. **Phylogenetic conservation**: Domain pairs conserved across deep evolutionary distances are more likely functional.
3. **Structural contact**: Check if neighboring domains form physical interfaces (PDB/iPfam).
4. **Co-evolution**: Correlated mutation analysis between domains.
5. **Reassortment test**: Are observed architectures more common than expected under domain shuffling?

**Known findings** (Forslund et al., 2019):
- Domain family sizes follow power law distributions
- 87% of architectures gain complexity via fusion (5.6× more common than fission)
- ~65% of domain pairs are found in only a few species; few are universally conserved
- Promiscuous domains (e.g., kinase, SH2, WD40) form a reservoir for evolutionary recombination

---

## Quick Reference: Key URLs

| Resource | URL |
|----------|-----|
| InterPro (Pfam new home) | https://www.ebi.ac.uk/interpro/ |
| Pfam FTP downloads | https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/ |
| InterPro download page | https://www.ebi.ac.uk/interpro/download/pfam/ |
| CATH database | https://www.cathdb.info/ |
| CATH FTP | ftp://orengoftp.biochem.ucl.ac.uk/cath/ |
| HMMER | http://hmmer.org/ |
| HMMER web server | https://www.ebi.ac.uk/Tools/hmmer/ |
| ESM GitHub | https://github.com/facebookresearch/esm |
| ESM-3 EvolutionaryScale | https://www.evolutionaryscale.ai/ |
| Biopython | https://biopython.org/ |
| PEER benchmark | https://github.com/DeepGraphLearning/PEER_Benchmark |
| TAPE | https://github.com/songlab-cal/tape |
| CATH dataset (Boomsma) | https://github.com/wouterboomsma/cath_datasets |
| Stockholm format spec | http://sonnhammer.sbc.su.se/Stockholm.html |
| Pfam documentation | https://pfam-docs.readthedocs.io/ |
| SMART v10 | https://smart.embl.de/ |

---

## Recommended Papers for Your Project

1. Paysan-Lafosse et al. (2025) "Pfam: embracing AI/ML." *Nucleic Acids Res.* — Latest Pfam update with Pfam-N, ECOD harmonization
2. Lin et al. (2023) "Language models of protein sequences..." *Science* — ESM-2 backbone
3. Rao et al. (2019) "Evaluating Protein Transfer Learning with TAPE." *NeurIPS* — Benchmark methodology, heldout families
4. Bileschi et al. (2022) "Using deep learning to annotate the protein universe." *Nat. Biotechnol.* — Pfam coverage with DL
5. Mistry et al. (2021) "Pfam in 2021." *Nucleic Acids Res.* — Pfam-A/B details
6. Forslund et al. (2019) "Evolution of Protein Domain Architectures." *Methods Mol. Biol.* — Comprehensive architectural evolution review
7. Lin et al. (2009) "WDAC: Weighted Domain Architecture Comparison." *BMC Bioinformatics* — Domain similarity metric
8. Eddy (2011) "Accelerated Profile HMM Searches." *PLoS Comput. Biol.* — HMMER3 algorithm
9. Sillitoe et al. (2021) "CATH: increased structural coverage." *Nucleic Acids Res.* — CATH v4.3+
10. Potter et al. (2018, 2026) "HMMER web server updates." *Nucleic Acids Res.*

---

*Compiled from web research, June 2026. All URLs verified at time of writing.*
