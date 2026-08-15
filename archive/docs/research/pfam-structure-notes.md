# Pfam 38.2 — Internal Structure Notes

> **Source**: Literature review using Consensus AI (Jun 2026)
> **Purpose**: Inform data pipeline design for Phase 01 (what data to download, how to parse, what filters to apply)
> **Version target**: Pfam 38.2 (current release at time of research)

---

## Overview

Pfam 38.2 is organized as a layered sequence-family system:

| Layer | Scope | Curation |
|-------|-------|----------|
| **Pfam-A** | ~20,795 manually curated families | Permanent accession, seed alignment, profile HMM, annotation |
| **Pfam-B** | ~177,011 provisional clusters | MMSeqs2 + FAMSA, no HMMs, no annotation, archive-only |
| **Clans** | 600+ higher-order evolutionary groups | HMMER cross-matches, SCOOP, HHsearch, structural evidence |
| **Seed alignments** | Representative low-redundancy homologs | Manually curated, stable across releases |
| **Full alignments** | All GA-thresholded matches | Automatic (HMM search of pfamseq) |
| **Structural cross-links** | PDB, SCOP, CATH, ECOD | SIFTS mappings, HMMER annotations, bidirectional seeding |

This architecture has been stable since the late 1990s [Sonnhammer 1997; Bateman 1999; Mistry 2021].

---

## 1. Pfam-A vs Pfam-B

### 1.1 Pfam-A (Curated Families)

Pfam-A is the curated, annotated core — what most publications mean when they refer to "Pfam families" [Sonnhammer 1997; Sammut 2008]. Each Pfam-A entry has:

- Permanent accession (e.g., `PF00001`)
- Curated annotation (function, domain boundaries, literature references)
- Representative seed alignment (low-redundancy, manually verified)
- Profile HMM built from the seed
- Family-specific gathering threshold (GA) for building the full alignment

**Scale in 38.2**: ~20,795 families. DPAM-AI reports representative 3D structures for 18,487 of these (89%) [Durham 2024].

### 1.2 Pfam-B (Provisional Clusters)

Pfam-B is an unannotated supplement of computationally generated multiple sequence alignments for regions not covered by Pfam-A [Paysan-Lafosse 2024]. Built with **MMSeqs2 clustering** and **FAMSA alignments**, released as archive files rather than website-integrated entries.

**Scale in 38.2**: 177,011 families, mean 125 sequences per family, mean alignment length **432 amino acids** [Paysan-Lafosse 2024].

**History**: Introduced as automatic complement [Sonnhammer 1997; Bateman 1999]; removed entirely in Pfam 29.0 [Finn 2016]; reintroduced with MMSeqs2-based pipeline in later releases [Mistry 2021]. In 38.2, Pfam-B serves as a **discovery layer** for possible future Pfam-A families, not a parallel curated classification [Paysan-Lafosse 2024; Sammut 2008].

---

## 2. Seed Alignments, Full Alignments, and Stockholm Format

### 2.1 Seed Alignments

The seed alignment is the **manually curated core** of each Pfam-A family [Mistry 2021; Finn 2016; Bateman 1999]:

- Contains a representative, low-redundancy set of homologs
- Designed to change infrequently (only when family scope or alignment quality improves) [Bateman 1999; Finn 2010]
- Defines the family's domain boundaries
- Used to train the profile HMM

### 2.2 Full Alignments

Generated automatically by:

1. Searching the profile HMM against **pfamseq** (Pfam's non-redundant protein sequence database)
2. Collecting all sequence regions that pass the **family-specific gathering threshold (GA)**
3. Aligning matches back to the HMM model [Mistry 2021; Finn 2016; El-Gebali 2019]

**Critical**: Pfam explicitly warns against using a universal E-value cutoff instead of per-family GA thresholds — this lowers sensitivity and increases false positives [Mistry 2021; Punta 2012].

### 2.3 Stockholm Format Annotations

Pfam flatfiles use a **Stockholm-like** annotated alignment format. Key field labels [Bateman 1999]:

| Label | Meaning |
|-------|---------|
| `AU` | Author of the alignment |
| `SE` | Seed evidence source |
| `AL` | Alignment method |
| `BM` | HMM building method |
| `GA` | Gathering threshold(s) |
| `TC` | Trusted cutoff |
| `NC` | Noise cutoff |
| `SQ` | Sequence count |

Over time, Pfam added structural and active-site markup to alignments where available [Bateman 2002; Coggill 2008].

This seed/full alignment + family-specific threshold pattern is shared across the Xfam resource family (cf. Rfam) — it is a deliberate family-database design pattern [Nawrocki 2014; Gardner 2008].

---

## 3. Clans and Domain Architecture

### 3.1 Clans (Higher-Order Groups)

Clans group related Pfam families sharing a **common evolutionary origin** [Finn 2016; Sammut 2008]. Assignment uses multiple evidence types:

- HMMER cross-matches between HMM profiles
- SCOOP (derived from shared PDB domain partners)
- HHsearch HMM–HMM comparison
- Known protein structures [Finn 2016; El-Gebali 2019; Steinegger 2019]

**Scale**: Clan counts rose from 559 (Pfam 29.0) → 628 (32.0) → 635 (33.1) [Finn 2016; El-Gebali 2019; Mistry 2021]. Expected ~640+ in 38.2.

**Overlap resolution**: Clan members may overlap on sequences. Pfam resolves this by retaining the most significant match, except for seed regions (which remain assigned to their defining family) [El-Gebali 2019]. This makes clans partly a biological grouping and partly a conflict-management layer.

### 3.2 Domain Architecture Representation

Domain architecture = the ordered combination of domains along a protein chain. Pfam provides:

- Graphical architecture views for query sequences
- Tools such as PfamAlyzer for searching specific domain combinations [Bateman 1999; Punta 2012]
- Full architectures in Stockholm alignment files

**Length characteristics**: The best 38.2-era statistic is the mean Pfam-B alignment length of **432 aa** [Paysan-Lafosse 2024]. No direct overall mean for full Pfam-A domain architectures is available in the reviewed papers.

---

## 4. Links to PDB, SCOP, and CATH

### 4.1 PDB Integration (iPfam)

Pfam families are designed, where possible, to correspond to structural domains [Bateman 2002; Punta 2012]. iPfam maps families onto PDB structures:

- Mappings built from **SIFTS** residue-level UniProt↔PDB links
- Supplemented with RCSB HMMER annotations for newer structures
- **iPfam 1.0**: 272,900 structural domains from 6,634 distinct Pfam entries across 87,386 PDB entries [Finn 2013a; Finn 2013b]

### 4.2 SCOP / SCOPe

Relationship is close but **not one-to-one** [Bateman 2003]:

- Many Pfam families originate from SCOP families
- But one Pfam family can map to multiple SCOP families, and vice versa
- SCOP explicitly acknowledges that mapping is imprecise because boundaries and membership criteria differ [Andreeva 2019]
- SCOPe continues to classify structures from large Pfam families not yet covered in SCOPe [Chandonia 2022]

### 4.3 CATH

CATH provides an independent structural domain hierarchy with explicit links to Pfam and InterPro [Sillitoe 2021; Waman 2024].

**Bidirectional seeding**: Pfam 27.0 built **100 new Pfam-A families** from unmatched CATH domains — structural databases help seed new sequence families, and Pfam classifications help interpret structural space [Finn 2013a].

**AlphaFold-era bridge**: ~9,000 Pfam families analysed against ECOD using predicted structures; over half received confident structural-hierarchy assignments [Pei 2024].

---

## 5. Key Statistics Summary

| Metric | Value | Source |
|--------|-------|--------|
| Pfam-A families | ~20,795 | [Durham 2024] |
| Pfam-A families with 3D structure | 18,487 (89%) | [Durham 2024] |
| Pfam-B families | 177,011 | [Paysan-Lafosse 2024] |
| Mean Pfam-B alignment length | 432 aa | [Paysan-Lafosse 2024] |
| Mean Pfam-B sequences per family | 125 | [Paysan-Lafosse 2024] |
| Clans | ~640+ (est. from trend: 559→628→635) | [Finn 2016; El-Gebali 2019; Mistry 2021] |
| Structural domains mapped (iPfam 1.0) | 272,900 | [Finn 2013b] |
| Distinct Pfam entries in iPfam 1.0 | 6,634 | [Finn 2013b] |
| PDB entries covered by iPfam 1.0 | 87,386 | [Finn 2013b] |
| Pfam families analysed vs ECOD | ~9,000 | [Pei 2024] |
| New Pfam-A families from CATH domains | 100 | [Finn 2013a] |

---

## 6. Data Downloads for Phase 01

### 6.1 Recommended Files

Based on the Phase 01 pipeline specification and reconciled with this research:

| File | URL | Purpose | Referenced in |
|------|-----|---------|---------------|
| `Pfam-A.seed.gz` | `https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.seed.gz` | Seed alignments (Stockholm) | Phase 01 Task 1.1.1 |
| `Pfam-A.hmm.gz` | `https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz` | HMM profiles for bit-score computation | Phase 01 Task 1.1.2 |
| `Pfam-A.hmm.dat.gz` | `https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.dat.gz` | Metadata (family type, description, length) | Phase 01 Task 1.2.6 |
| `Pfam-A.clans.tsv.gz` | `https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.clans.tsv.gz` | Clan mapping for fold-compatibility scoring | Phase 01 Task 1.1.4 |
| `Pfam-A.full.gz` | `https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.full.gz` | Full alignments (not strictly needed for pipeline; seed is sufficient) | Protein data registry suggestion |

### 6.2 Version Note

- All documentation has been updated to reference **Pfam 38.2** (the current release).
- **Recommendation**: Use `current_release` URLs and pin the version (e.g., `Pfam/38.2/` subdirectory) after download.

### 6.3 Data Directory Reconciliation

| Source | Listed files | Missing from source |
|--------|-------------|-------------------|
| Phase 01 Task 1.1 | `Pfam-A.seed.gz`, `Pfam-A.hmm.gz`, `Pfam-A.hmm.dat.gz`, `Pfam-A.clans.tsv.gz` | `Pfam-A.full.gz`, `Pfam-A.reg` |
| Protein data registry | `Pfam-A.hmm.gz`, `Pfam-A.full.gz`, `Pfam-A.seed.gz`, `Pfam-A.reg` | `Pfam-A.hmm.dat.gz`, `Pfam-A.clans.tsv.gz` |

**Recommendation**: Download the union of both sets (all 6 files). The `.hmm.dat.gz` file is needed for family-type metadata; `.clans.tsv.gz` is needed for clan-based fold compatibility. The `.full.gz` and `.reg` files are optional (seed is sufficient for architecture parsing).

---

## 7. Pipeline Implications

The research above motivates the following design decisions for Phase 01:

### 7.1 Parsing: Use GA Thresholds, Not Universal E-value

Pfam literature consistently warns against universal E-value cutoffs [Mistry 2021; Punta 2012]. The pipeline should:

- Parse per-family GA (gathering), TC (trusted), and NC (noise) thresholds from `Pfam-A.hmm.dat.gz`
- Use **GA** as the primary inclusion criterion for domain architectures
- Document threshold choice in the protein data registry

### 7.2 Filtering: Clan Overlap Resolution

When two Pfam families overlap on the same sequence region and belong to the same clan, the pipeline should:

- Retain the match with the highest significance (per HMMER bit score)
- Except for seed regions, which stay assigned to their defining family [El-Gebali 2019]
- Exclude architectures with unresolved overlap ambiguity

### 7.3 Domain Architecture Length Bounds

Phase 01 already specifies `min_length=2, max_length=15` (Task 1.2.2). The mean Pfam-B architecture length of 432 aa [Paysan-Lafosse 2024] provides a sanity check: architectures outside reasonable bounds (too short = fragments; too long = likely mis-annotated) should be filtered.

### 7.4 Family-Type Metadata for Filtering

`Pfam-A.hmm.dat.gz` classifies families into types: **Family**, **Domain**, **Repeat**, **Motif**, **Disordered**. The pipeline should:

- Consider restricting to `Family` and `Domain` types for architecture modelling (excluding `Repeat`/`Motif` which may follow different compositional rules)
- Or retain all types and use type as a covariate in analysis

### 7.5 HMMER Bit Scores for Domain Similarity

The ODE framework requires a domain similarity metric `phi(d_a, d_b)`. HMMER bit scores (log2 of the odds ratio) are:

- Phylogenetically grounded
- Computable via `pyhmmer` HMM–HMM comparison
- Used implicitly in Pfam's GA threshold design

Phase 01 Task 1.3 already specifies this approach; the research confirms it is well-motivated.

### 7.6 Structural Validation for Split Generation

For fold-compatibility scoring in compositional splits (Phase 01 Task 1.3.3):

- Clan membership ([1] → same clan) provides a strong compatibility signal [Finn 2016]
- PDB interaction data from iPfam or 3did can validate whether OOD combinations are biologically plausible
- CATH assignments can serve as an independent structural hierarchy for cross-validation [Sillitoe 2021]

### 7.7 Version Pinning

Pin to a specific Pfam release for reproducibility. All configs and the data registry now reference **Pfam 38.2**.

---

## References

Andreeva, A., Kulesha, E., Gough, J., & Murzin, A. (2019). The SCOP database in 2020: expanded classification of representative family and superfamily domains of known protein structures. *Nucleic Acids Research*, 48, D376–D382. doi:10.1093/nar/gkz1064

Bateman, A., Birney, E., Durbin, R., Eddy, S., Finn, R., & Sonnhammer, E. (1999). Pfam 3.1: 1313 multiple alignments and profile HMMs match the majority of proteins. *Nucleic Acids Research*, 27(1), 260–262. doi:10.1093/nar/27.1.260

Bateman, A., Birney, E., Cerruti, L., Durbin, R., Etwiller, L., Eddy, S., Griffiths-Jones, S., Howe, K., Marshall, M., & Sonnhammer, E. (2002). The Pfam protein families database. *Nucleic Acids Research*, 30(1), 276–280.

Bateman, A., Coin, L., Durbin, R., Finn, R., Hollich, V., Griffiths-Jones, S., Khanna, A., Marshall, M., Moxon, S., Sonnhammer, E., Studholme, D., Yeats, C., & Eddy, S. (2003). The Pfam protein families database. *Nucleic Acids Research*, 32(Database issue), D138–D141. doi:10.1093/nar/gkh121

Chandonia, J., Guan, L., Lin, S., Yu, C., Fox, N., & Brenner, S. (2021). SCOPe: improvements to the structural classification of proteins — extended database to facilitate variant interpretation and machine learning. *Nucleic Acids Research*, 50, D553–D559. doi:10.1093/nar/gkab1054

Coggill, P., Finn, R., & Bateman, A. (2008). Identifying Protein Domains with the Pfam Database. *Current Protocols in Bioinformatics*, 23. doi:10.1002/0471250953.bi0205s23

Durham, J., Zhang, J., Schaeffer, R. D., & Cong, Q. (2024). DPAM-AI: a domain parser for AlphaFold models powered by artificial intelligence. *Bioinformatics*, 41. doi:10.1093/bioinformatics/btae740

El-Gebali, S., Mistry, J., Bateman, A., Eddy, S., Luciani, A., Potter, S. C., Qureshi, M., Richardson, L. J., Salazar, G. A., Smart, A., Sonnhammer, E., Hirsh, L., Paladin, L., Piovesan, D., Tosatto, S. C. E., & Finn, R. (2018). The Pfam protein families database in 2019. *Nucleic Acids Research*, 47, D427–D432. doi:10.1093/nar/gky995

Finn, R., Bateman, A., Clements, J., Coggill, P. C., Eberhardt, R. Y., Eddy, S., Heger, A., Hetherington, K., Holm, L., Mistry, J., Sonnhammer, E., Tate, J., & Punta, M. (2013a). Pfam: the protein families database. *Nucleic Acids Research*, 42, D222–D230. doi:10.1093/nar/gkt1223

Finn, R., Coggill, P., Eberhardt, R. Y., Eddy, S., Mistry, J., Mitchell, A., Potter, S. C., Punta, M., Qureshi, M., Sangrador-Vegas, A., Salazar, G. A., Tate, J., & Bateman, A. (2015). The Pfam protein families database: towards a more sustainable future. *Nucleic Acids Research*, 44, D279–D285. doi:10.1093/nar/gkv1344

Finn, R., Marshall, M., & Bateman, A. (2005). iPfam: visualization of protein–protein interactions in PDB at domain and amino acid resolutions. *Bioinformatics*, 21(3), 410–412. doi:10.1093/bioinformatics/bti011

Finn, R., Miller, B. L., Clements, J., & Bateman, A. (2013b). iPfam: a database of protein family and domain interactions found in the Protein Data Bank. *Nucleic Acids Research*, 42, D364–D373. doi:10.1093/nar/gkt1210

Finn, R., Mistry, J., Tate, J. G., Coggill, P. C., Heger, A., Pollington, J. E., Gavin, O., Gunasekaran, P., Ceric, G., Forslund, K., Holm, L., Sonnhammer, E., Eddy, S., & Bateman, A. (2007). The Pfam protein families database. *Nucleic Acids Research*, 38, D211–D222. doi:10.1093/nar/gkp985

Gardner, P., Daub, J., Tate, J., Nawrocki, E. P., Kolbe, D. L., Lindgreen, S., Wilkinson, A., Finn, R., Griffiths-Jones, S., Eddy, S., & Bateman, A. (2008). Rfam: updates to the RNA families database. *Nucleic Acids Research*, 37, D136–D140. doi:10.1093/nar/gkn766

Mistry, J., Chuguransky, S., Williams, L., Qureshi, M., Salazar, G. A., Sonnhammer, E., Tosatto, S. C. E., Paladin, L., Raj, S., Richardson, L. J., Finn, R., & Bateman, A. (2020). Pfam: The protein families database in 2021. *Nucleic Acids Research*, 49, D412–D419. doi:10.1093/nar/gkaa913

Nawrocki, E. P., Burge, S. W., Bateman, A., Daub, J., Eberhardt, R. Y., Eddy, S., Floden, E., Gardner, P., Jones, T. A., Tate, J., & Finn, R. (2014). Rfam 12.0: updates to the RNA families database. *Nucleic Acids Research*, 43, D130–D137. doi:10.1093/nar/gku1063

Paysan-Lafosse, T., Andreeva, A., Blum, M., Chuguransky, S., Grego, T., Pinto, B. L., Salazar, G. A., Bileschi, M. L., Llinares-López, F., Meng-Papaxanthos, L., Colwell, L. J., Grishin, N. V., Schaeffer, R. D., Clementel, D., Tosatto, S. C. E., Sonhammer, E., Wood, V., & Bateman, A. (2024). The Pfam protein families database: embracing AI/ML. *Nucleic Acids Research*, 53, D523–D534. doi:10.1093/nar/gkae997

Pei, J., Andreeva, A., Chuguransky, S., Pinto, B. L., Paysan-Lafosse, T., Schaeffer, R. D., Bateman, A., Cong, Q., & Grishin, N. V. (2024). Bridging the Gap between Sequence and Structure Classifications of Proteins with AlphaFold Models. *Journal of Molecular Biology*, 436, 168764. doi:10.1016/j.jmb.2024.168764

Punta, M., Coggill, P., Eberhardt, R. Y., Mistry, J., Tate, J., Boursnell, C., Pang, N., Forslund, K., Ceric, G., Clements, J., Heger, A., Holm, L., Sonnhammer, E., Eddy, S., Bateman, A., & Finn, R. (2011). The Pfam protein families database. *Nucleic Acids Research*, 40, D290–D301. doi:10.1093/nar/gkr1065

Sammut, S., Finn, R., & Bateman, A. (2008). Pfam 10 years on: 10000 families and still growing. *Briefings in Bioinformatics*, 9(3), 210–219. doi:10.1093/bib/bbn010

Sillitoe, I., Bordin, N., Dawson, N., Waman, V. P., Ashford, P., Scholes, H. M., Pang, C. S. M., Woodridge, L., Rauer, C., Sen, N., Abbasian, M., Le Cornu, S., Lam, S., Berka, K., Vareková, I., Vareková, R., Lewis, T. E., & Orengo, C. (2020). CATH: increased structural coverage of functional space. *Nucleic Acids Research*, 49, D266–D273. doi:10.1093/nar/gkaa1079

Sillitoe, I., Dawson, N., Lewis, T. E., Das, S., Lees, J. G., Ashford, P., Tolulope, A., Scholes, H. M., Senatorov, I. S., Bujan, A., Ceballos Rodriguez-Conde, F., Dowling, B., Thornton, J., & Orengo, C. (2018). CATH: expanding the horizons of structure-based functional annotations for genome sequences. *Nucleic Acids Research*, 47, D280–D284. doi:10.1093/nar/gky1097

Sonnhammer, E., Eddy, S., Birney, E., Bateman, A., & Durbin, R. (1998). Pfam: multiple sequence alignments and HMM-profiles of protein domains. *Nucleic Acids Research*, 26(1), 320–322. doi:10.1093/nar/26.1.320

Sonnhammer, E., Eddy, S., & Durbin, R. (1997). Pfam: A comprehensive database of protein domain families based on seed alignments. *Proteins: Structure*, 28. doi:10.1002/(sici)1097-0134(199707)28:3<405::aid-prot10>3.0.co;2-l

Steinegger, M., Meier, M., Mirdita, M., Voehringer, H., Haunsberger, S. J., & Soeding, J. (2019). HH-suite3 for fast remote homology detection and deep protein annotation. *BMC Bioinformatics*, 20. doi:10.1186/s12859-019-3019-7

Waman, V. P., Bordin, N., Lau, A., Kandathil, S., Wells, J., Miller, D., Velankar, S., Jones, D. T., Sillitoe, I., & Orengo, C. A. (2024). CATH v4.4: major expansion of CATH by experimental and predicted structural data. *Nucleic Acids Research*, 53, D348–D355. doi:10.1093/nar/gkae1087
