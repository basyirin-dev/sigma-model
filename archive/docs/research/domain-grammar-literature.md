# Protein Domain Recombination Grammar — Literature Review

> **Source**: Literature review using Consensus AI (Jun 2026)
> **Purpose**: Inform hypothesis framing for H1/H2 and split construction in Phase 01/Phase 07
> **Version target**: Pfam 38.2

---

## Overview

Protein domain architectures follow a **constrained recombinatorial grammar**: evolution reuses a small subset of possible domain combinations, strongly biases domain order and neighbours, and generates most new architectures through fusion, terminal gain/loss, duplication, and occasional shuffling rather than free recombination [Yu 2019; Apic 2001a; Fong 2007].

This is the central biological premise for the sigma-model's compositional gap hypothesis (H1): if domain combinations are non-random and reuse is highly biased, then models trained on observed architectures should systematically struggle with OOD combinations. The recombination distance (Type A/B/C split design) maps directly onto the known constraint gradient: familiar combinations → new family recombinations → cross-fold recombinations.

**Key statistic**: In 40 genomes covering all three domains of life, 783 SCOP superfamilies formed only **1,307 adjacent combinations** — a tiny fraction of the ~300,000 theoretically possible pairs [Apic 2001a].

---

## 1. Key Papers

Three papers anchor the empirical frame:

| Paper | Method | Scale | Key Finding |
|-------|--------|-------|-------------|
| [Yu 2019] | N-gram model (bigram, trigram, skipgram) across major clades | ~20,000 Pfam families across bacteria, archaea, eukaryotes | Near-universal information gain from domain-order modelling; formal "grammar" characterisation of architectures |
| [Apic 2001a] | Pairwise domain adjacency enumeration from SCOP superfamilies | 40 complete proteomes (all 3 kingdoms) | 1,307 adjacent pairs from 783 superfamilies; sparse, hub-like network; kingdom-specific combinations reuse universal families |
| [Apic 2001b] | Same method on 7 early genomes | 624 superfamilies → 585 pairwise combos | Consistent sparsity; small set of versatile hubs account for most connections |
| [Fong 2007] | Maximum parsimony reconstruction of architecture evolution | 159 proteomes | 87% of architectures gained complexity through simple changes; fusion 5.6× more common than fission |
| [Cui 2025] | Vector-space embedding of domain architectures (word2vec-style) | 159 proteomes | Fusion dominates parsimonious histories; vector semantics capture functional relationships between domain arrangements |

**Additional landmark reviews**: [Forslund 2012] and [Sammut 2008] provide comprehensive surveys of the mechanisms and constraints.

---

## 2. Combination Constraints

### 2.1 Sparse Adjacency Networks

Across all studies, the domain-pair network is sparse, highly uneven, and scale-free-like:

- **40 genomes**: 783 SCOP superfamilies → 1,307 adjacent pairs. Kingdom-specific combinations disproportionately reuse families already present across all three kingdoms rather than newly invented families [Apic 2001a].
- **7 early genomes**: 624 superfamilies → 585 pairwise combinations, with a small set of versatile hubs dominating [Apic 2001b].
- **Duplication channel**: A strong correlation exists between a domain's abundance and its number of distinct partners. Observed repertoires are much smaller than random models predict because successful combinations are repeatedly duplicated rather than independently re-sampled [Vogel 2005].

### 2.2 Hub Domains and Promiscuity

A small minority of domain families act as highly versatile hubs (e.g., protein kinase, immunoglobulin, SH3, P-loop NTPase), pairing with many different partners. Most domain families have only 1–2 partners [Apic 2001a; Apic 2001b].

### 2.3 Historical vs Structural Constraints

The literature splits constraints into three classes [Forslund 2012]:

1. **Historical**: Many combinations arise once and spread by duplication. "Supra-domains" (recurrent multi-domain units) behave as larger reusable building blocks [Vogel 2005; Alves 2009].
2. **Structural**: Domain order is usually fixed; reversed orders are rare (<2% of AB pairs occur as BA). Successful recombination depends on interdomain geometry, orientation, and linker properties [Bashton 2002; Gräwe 2020].
3. **Mutational**: Fusion, fission, terminal addition/loss, and duplication explain most architecture evolution. Fusion is consistently more common than fission [Fong 2007; Dohmen 2020; Pasek 2006].

---

## 3. Fold Compatibility

### 3.1 Experimental Evidence

The strongest direct evidence for biophysical constraints on domain compatibility comes from a massively parallel insertion screen:

| Feature | Detail |
|---------|--------|
| System | Kir2.1 ion channel + inserted motifs/domains [Coyote-Maestas 2021] |
| Scale | >300,000 recombination variants |
| Readout | Surface expression (folding/trafficking proxy) |
| Key finding | Large structured inserts favoured at termini; donor and recipient biophysics jointly determine compatibility |
| Implication | Grammar is partly biophysical, not just historical |

This is the only large-scale direct experiment. It confirms that insertion position matters, fold size matters, and compatibility is jointly determined by both the inserted domain and the recipient context [Coyote-Maestas 2021].

### 3.2 Bioengineering Evidence

Rule-based domain insertion and linker design remain highly context-dependent:
- Linker composition (flexible vs rigid, length, charge) strongly affects fusion protein function [Gräwe 2020].
- Computational prediction of insertion sites for allosteric switches works for some candidates but universal rules remain incomplete [Wolf 2024].
- De novo design of multi-domain proteins is advancing but still limited for complex architectures [Listov 2024].

**Summary**: Universal fold-compatibility rules are not yet established. The claim scores **weak (2/10)** in evidence strength [Coyote-Maestas 2021; Listov 2024]. This is the key gap that sigma-model's σ_A metric could help fill.

---

## 4. Domain Order and Neighbours

### 4.1 Order Constraints

Domain order is highly conserved:
- Only **~2%** of known AB superfamily combinations occur in both AB and BA orders [Bashton 2002].
- When both orders exist, they usually differ in geometry and function — reversal is not neutral.
- N→C orientation is enforced by the physics of polypeptide chain connectivity and co-translational folding.

### 4.2 Positional Effects

Domain losses and duplications occur preferentially at protein ends:
- **Termini** are hotspots for domain gain and loss; substitutions in the middle of architectures are rare [Weiner 2006].
- Internal domain neighbourhoods are harder to change than terminal positions.
- This bias has direct implications for split construction: architectures with internal rearrangements represent a harder OOD class than terminal additions/deletions.

### 4.3 Neighbour Preferences

Certain domain pairs are evolutionarily conserved (e.g., kinase + SH2, immunoglobulin superfamily pairs). These "supra-domains" are reused as quasi-atomic units across diverse proteins [Alves 2009; Vogel 2005]. The n-gram model of [Yu 2019] quantifies this: bigram and trigram frequencies significantly exceed random expectation across all major clades.

---

## 5. Evolutionary Mechanisms

### 5.1 Fusion Dominance

Fusion is the dominant mechanism for creating new domain architectures:

| Study | Scale | Key result |
|-------|-------|------------|
| [Fong 2007] | 159 proteomes | Fusion accounts for 5.6× as many architectures as fission; 87% of new architectures arise via simple changes |
| [Dohmen 2020] | 5 eukaryotic clades | Four event types (fusion, fission, terminal gain, terminal loss) explain ~70% of rearrangements across plants, animals, fungi, insects |
| [Pasek 2006] | Bacterial microsynteny | Fusion/fission explains 27–64% of multidomain evolution; terminal indels especially common |
| [Buljan 2010] | Animal genomes | Domain gains dominated by exon fusion; duplication precedes gain in ≥80% of cases; retroposition <1% |

### 5.2 Lineage-Specific Patterns

- **Fungi**: Unusually high domain loss rates [Dohmen 2020].
- **Bacteria**: Microsynteny suggests fusion/fission is the dominant force [Pasek 2006].
- **Phages**: Active, ongoing domain shuffling concentrated in receptor-binding proteins, endolysins, tail proteins, and replication proteins (analysis of 133,574 proteins) [Smug 2023].
- **Non-ribosomal peptide synthesis**: Recombination events create vast chemical diversity through modular assembly lines [Baunach 2021].

### 5.3 Mechanism Summary

| Mechanism | Relative Frequency | Notes |
|-----------|------------------|-------|
| Gene fusion | Highest (5.6× fission) | Adjacent genes or exon fusion from neighbouring loci |
| Terminal gain/loss | High | Especially at N/C termini |
| Duplication | Precedes most gains (>80%) | Creates substrate for fusion |
| Gene fission | Low (1:5.6) | Less common route |
| Shuffling | Variable | High in phages, low in most cellular genomes |
| Retroposition | Negligible (<1%) | [Buljan 2010] |

---

## 6. Evidence Quality Assessment

| Claim | Evidence Strength | Support |
|-------|------------------|---------|
| **Only a small subset of possible domain combinations is realised** | Strong (9/10) | Replicated across multiple comparative datasets (40, 159 proteomes); consistent n-gram and pairwise sparsity [Yu 2019; Apic 2001a; Apic 2001b] |
| **Fusion is the dominant mechanism** | Strong (8/10) | Multiple phylogenomic reconstructions agree across diverse clades [Fong 2007; Dohmen 2020; Pasek 2006] |
| **Domain order and neighbourhood strongly constrain viability** | Moderate (7/10) | Comparative order bias is robust; Kir2.1 screen supports positional effects [Bashton 2002; Weiner 2006; Coyote-Maestas 2021] |
| **Supra-domains channel later innovation** | Moderate (6/10) | Good observational support for duplicated successful pairs; fewer direct tests [Vogel 2005; Alves 2009] |
| **Universal fold-compatibility rules are known** | Weak (2/10) | Evidence remains system-specific; authors explicitly call current rules coarse [Coyote-Maestas 2021; Listov 2024] |

**Main limitation**: Statistical "grammar" models show non-randomness but cannot distinguish selection, mutational bias, structural compatibility, and annotation artefacts [Yu 2019; Fong 2007]. Direct compatibility data remains narrow (mostly one recipient system in the Kir2.1 screen).

---

## 7. Classification Caveat: SCOP vs Pfam Clans

Most of the foundational literature cited above (Apic 2001, Bashton 2002, Vogel 2005, Alves 2009) uses **SCOP superfamilies** as their classification unit. Phase 01 of this project uses **Pfam clans** for Type C (cross-fold) split construction. These are **not interchangeable**:

| Property | SCOP Superfamilies | Pfam Clans |
|----------|-------------------|------------|
| Basis | Structural (3D fold + evolutionary relatedness) | Sequence (HMMER cross-matches, HHsearch, SCOOP) |
| Coverage | ~2,000 superfamilies (mostly PDB-derived) | ~640+ clans (full Pfam proteome coverage) |
| Relationship | One SCOP family → one superfamily | One Pfam family → one clan |
| Mapping | SCOP superfamilies are narrower, structurally defined | Pfam clans are broader, sequence-based |

**Why Pfam clans are still the right choice for this project**:
1. The data pipeline already depends on Pfam — clan mappings are available directly from the Pfam distribution (`Pfam-A.clans.tsv.gz`), whereas SCOP mappings require a separate cross-database join.
2. Pfam clans cover the full sequence space (~20,795 Pfam families), whereas SCOP coverage is limited by PDB structure availability.
3. The literature constraint gradient (familiar → new combination → new fold) is biologically meaningful under either classification system — the specific grouping criterion changes the interpretation granularity but not the experimental logic.

**Caveat for interpretation**: Type C split results should be described as "cross-clan" rather than "cross-fold" when using Pfam. Where the paper makes a generalisation to fold-level generalisation, this should be explicitly flagged as relying on Pfam clans as a proxy for structural folds. A sensitivity analysis using a SCOP-mapped subset of architectures would strengthen this claim.

---

## 8. Implications for Sigma-Model

### 8.1 Hypothesis H1: Compositional Gap

The finding that only a small fraction of domain combinations is observed in nature, and that existing combinations strongly constrain future ones, directly supports H1. If architectures follow a constrained grammar, then models trained on observed architectures will systematically underperform on OOD combinations — the compositional gap (ΔCG). The gradient of constraint strength (familiar → new family → cross-clan) predicts a corresponding gradient in ΔCG.

### 8.2 Hypothesis H2: σ_A and Recombination Distance

The evolutionary mechanisms (fusion dominance, terminal bias, hub domain promiscuity) provide the biological basis for quantifying recombination distance. Domains from the same clan that are never observed together are more likely to be "compatible but unobserved" (Type B) than domains from different clans (Type C). The Kir2.1 screen confirms that some cross-clan combinations are viable but position-dependent — supporting the idea of a continuous compatibility metric (σ_A) rather than a binary allowed/forbidden distinction.

### 8.3 Phase 01 Split Design

| Split Type | Literature Basis | Biological Interpretation |
|------------|----------------|--------------------------|
| **Type A** (familiar combinations) | Supra-domains, recurrent pairs [Vogel 2005; Alves 2009] | Architectures drawn from the same distribution as training |
| **Type B** (new family recombinations) | Fusion mechanisms, domain promiscuity [Fong 2007; Buljan 2010] | Biologically plausible OOD — domains known to recombine but in novel arrangements |
| **Type C** (cross-clan) | Fold compatibility constraints [Bashton 2002; Coyote-Maestas 2021] | Hard OOD — may be structurally incompatible or evolutionarily unprecedented |

The Type B/C boundary is the most biologically interesting: Type B captures the fusion-dominated regime where most real evolution happens, while Type C captures the structural constraint regime where new combinations are rarest.

### 8.4 Phase 07 Benchmark Validation

The Kir2.1 screen provides the best available experimental benchmark for assessing whether OOD architectures are biologically plausible [Coyote-Maestas 2021]. However, its limitation (single recipient system) means the benchmark should describe OOD plausibility as "informed by experimental evidence" rather than "validated".

### 8.5 The σ_A Gap

The literature's weakness on universal fold-compatibility rules (2/10 evidence score) is exactly where sigma-model's σ_A metric contributes novelty. If σ_A correlates with recombination distance and predicts OOD accuracy, it provides a quantitative compatibility proxy that the literature currently lacks.

---

## 9. Implications for NeurIPS Paper

The target paper (`paper-neurips/main.tex`, "The Σ-Model in Protein Domain Architectures") is currently a skeleton with all sections as placeholders. The domain grammar literature surveyed here fills the substance for:

- **§1 (Introduction)**: Cite sparse combination statistics (783 superfamilies → 1,307 pairs) to motivate compositional generalisation as biologically grounded [Apic 2001; Yu 2019]
- **§2 (Background) / §3 (Pfam test bed)**: Cite evolutionary mechanisms to contextualise the Type A/B/C split design [Fong 2007; Dohmen 2020; Buljan 2010]
- **§8 (Related Work)**: Cite fold compatibility gap (evidence strength 2/10) to establish σ_A metric's novelty [Coyote-Maestas 2021; Listov 2024]

None of the 27 papers in this review are cited in `paper-neurips/bibliography.bib` — all are new citations for the NeurIPS paper.

---

## References

Alves, R., Vilaprinyó, E., Sorribas, A., & Herrero, E. (2009). Evolution based on domain combinations: the case of glutaredoxins. *BMC Evolutionary Biology*, 9, 66. doi:10.1186/1471-2148-9-66

Apic, G., Gough, J., & Teichmann, S. (2001a). Domain combinations in archaeal, eubacterial and eukaryotic proteomes. *Journal of Molecular Biology*, 310(2), 311–325. doi:10.1006/jmbi.2001.4776

Apic, G., Gough, J., & Teichmann, S. (2001b). An insight into domain combinations. *Bioinformatics*, 17(Suppl 1), S83–S89. doi:10.1093/bioinformatics/17.suppl_1.s83

Bashton, M. & Chothia, C. (2002). The geometry of domain combination in proteins. *Journal of Molecular Biology*, 315(4), 927–939. doi:10.1006/jmbi.2001.5288

Baunach, M., Chowdhury, S., Stallforth, P., & Dittmann, E. (2021). The Landscape of Recombination Events That Create Nonribosomal Peptide Diversity. *Molecular Biology and Evolution*, 38, 2116–2130. doi:10.1093/molbev/msab015

Bepler, T. & Berger, B. (2021). Learning the Protein Language: Evolution, Structure and Function. *Cell Systems*, 12, 654–669.e3. doi:10.1016/j.cels.2021.05.017

Buljan, M., Frankish, A., & Bateman, A. (2010). Quantifying the mechanisms of domain gain in animal proteins. *Genome Biology*, 11, R74. doi:10.1186/gb-2010-11-7-r74

Coyote-Maestas, W., Nedrud, D., Suma, A., He, Y., Matreyek, K. A., Fowler, D., Carnevale, V., Myers, C., & Schmidt, D. (2021). Probing ion channel functional architecture and domain recombination compatibility by massively parallel domain insertion profiling. *Nature Communications*, 12. doi:10.1038/s41467-021-27342-0

Cui, X., Xiao, Y., Stolzer, M., & Durand, D. (2025). Vector semantics of multidomain protein architectures. *Bioinformatics Advances*, 6. doi:10.1101/2025.07.07.663606

Dohmen, E., Klasberg, S., Bornberg-Bauer, E., Perrey, S., & Kemena, C. (2020). The modular nature of protein evolution: domain rearrangement rates across eukaryotic life. *BMC Evolutionary Biology*, 20. doi:10.1186/s12862-020-1591-0

Ferruz, N., Schmidt, S., & Höcker, B. (2022). ProtGPT2 is a deep unsupervised language model for protein design. *Nature Communications*, 13. doi:10.1038/s41467-022-32007-7

Fong, J. H., Geer, L. Y., Panchenko, A., & Bryant, S. (2007). Modeling the evolution of protein domain architectures using maximum parsimony. *Journal of Molecular Biology*, 366(1), 307–315. doi:10.1016/j.jmb.2006.11.017

Forslund, K. & Sonnhammer, E. (2012). Evolution of protein domain architectures. *Methods in Molecular Biology*, 856, 187–216. doi:10.1007/978-1-61779-585-5_8

Gräwe, A., Ranglack, J., Weyrich, A., & Stein, V. (2020). iFLinkC: an iterative functional linker cloning strategy for the combinatorial assembly and recombination of linker peptides with functional domains. *Nucleic Acids Research*, 48, e24. doi:10.1093/nar/gkz1210

Harrison, S. (2003). Variation on an Src-like theme. *Cell*, 112(6), 737–740. doi:10.1016/s0092-8674(03)00196-x

Listov, D., Goverde, C. A., Correia, B. E., & Fleishman, S. (2024). Opportunities and challenges in design and optimization of protein function. *Nature Reviews Molecular Cell Biology*. doi:10.1038/s41580-024-00718-y

Madani, A., Krause, B., Greene, E., Subramanian, S., Mohr, B. P., Holton, J., Olmos, J. L., Xiong, C., Sun, Z. Z., Socher, R., Fraser, J., & Naik, N. (2023). Large language models generate functional protein sequences across diverse families. *Nature Biotechnology*, 41, 1099–1106. doi:10.1038/s41587-022-01618-2

Pasek, S., Risler, J., & Brézellec, P. (2006). Gene fusion/fission is a major contributor to evolution of multi-domain bacterial proteins. *Bioinformatics*, 22(12), 1418–1423. doi:10.1093/bioinformatics/btl135

Smug, B. J., Szczepaniak, K., Rocha, E. P. C., Dunin-Horkawicz, S., & Mostowy, R. J. (2023). Ongoing shuffling of protein fragments diversifies core viral functions linked to interactions with bacterial hosts. *Nature Communications*, 14. doi:10.1038/s41467-023-43236-9

Vogel, C., Teichmann, S., & Pereira-Leal, J. (2005). The relationship between domain duplication and recombination. *Journal of Molecular Biology*, 346(1), 355–365. doi:10.1016/j.jmb.2004.11.050

Weiner, J., Beaussart, F., & Bornberg-Bauer, E. (2006). Domain deletions and substitutions in the modular protein evolution. *FEBS Journal*, 273. doi:10.1111/j.1742-4658.2006.05220.x

Wolf, B., Shehu, P., Brenker, L., von Bachmann, A., Kroell, A., Southern, N. T., Holderbach, S., Eigenmann, J., Aschenbrenner, S., Mathony, J., & Niopek, D. (2024). Rational engineering of allosteric protein switches by in silico prediction of domain insertion sites. *Nature Methods*, 22, 1698–1706. doi:10.1038/s41592-025-02741-z

Yu, L., Tanwar, D. K., Penha, E. D. S., Wolf, Y., Koonin, E., & Basu, M. (2019). Grammar of protein domain architectures. *Proceedings of the National Academy of Sciences*, 116, 3636–3645. doi:10.1073/pnas.1814684116

Zheng, W., Zhou, X., Wuyun, Q., Pearce, R., Li, Y., & Zhang, Y. (2020). FUpred: detecting protein domains through deep-learning-based contact map prediction. *Bioinformatics*. doi:10.1093/bioinformatics/btaa217

Zheng, W., Wuyun, Q., Li, Y., Liu, Q., Zhou, X., Peng, C., Zhu, Y., Freddolino, L., & Zhang, Y. (2025). Deep-learning-based single-domain and multidomain protein structure prediction with D-I-TASSER. *Nature Biotechnology*, 44, 641–653. doi:10.1038/s41587-025-02654-4

Zhou, X., Zheng, W., Li, Y., Pearce, R., Zhang, C., Bell, E. W., Zhang, G., & Zhang, Y. (2022). I-TASSER-MTD: a deep-learning-based platform for multi-domain protein structure and function prediction. *Nature Protocols*, 17, 2326–2353. doi:10.1038/s41572-022-00728-0
