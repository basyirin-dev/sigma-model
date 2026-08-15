# Biological Validation Criteria for Benchmark Splits

> **Source**: Research output using AI Deep Research (Jun 2026)
> **Purpose**: Define actionable, quantitative validation tests for PfamCG-1.0 benchmark splits; prioritise false negative detection; inform Phase 07 validation pipeline
> **Target paper**: `paper-neurips/main.tex` ("The Σ-Model in Protein Domain Architectures")

---

## Overview

A benchmark partitioning Pfam domain architectures into ID/OOD sets by recombination distance must validate that the splits genuinely test **compositional generalisation** — not sequence novelty, fold novelty, or trivial artefacts of data partitioning. The primary concern is **false negatives**: biologically plausible domain combinations placed in the OOD set, which inflate ΔCG and misrepresent model capability. False negatives are more harmful than false positives (implausible combos in the OOD set) because they directly undermine the benchmark's claim to test *novel* recombination.

The validation framework operates at three layers:

| Layer | Method | Primary Goal |
|-------|--------|-------------|
| **1. Statistical** | Permutation test + JSD | Confirm split is non-random and compositionally distinct |
| **2. Biological (tiered)** | iPfam/SIFTS → co-occurrence → STRING | Quantify false negative rate from real biological data |
| **3. Rule-based (supplementary)** | CATH, conserved modules, clan patterns | Catch edge cases missed by layers 1–2 |

---

## 1. Statistical Framework

### 1.1 Permutation Test

Validates that the empirical ΔCG (compositional gap = Acc_ID − Acc_OOD) is unlikely under a null hypothesis of random partitioning.

**Procedure:**
1. Compute observed ΔCG from the candidate split.
2. Shuffle architecture train/test labels 10,000 times, recompute ΔCG each time → null distribution.
3. p-value = (count of shuffled ΔCG ≥ observed ΔCG) / 10,000.

**Threshold:** p < 0.01 (reject null that split is random).

**Rationale for 10,000 permutations:** Provides stable p-value estimates at the 0.01 level (versus 1,000 permutations, which yields only ~10 extreme samples at α = 0.01 — insufficient for reliable estimation).

### 1.2 Jensen-Shannon Divergence (JSD)

Continuous measure of compositional dissimilarity between ID and OOD adjacency distributions.

**Procedure:**
1. Build domain adjacency frequency matrices for ID (training) and OOD (test) corpora.
2. Normalise each matrix into a probability distribution over domain pairs.
3. Compute JSD between the two distributions (symmetric, bounded [0, 1]).

**Interpretation:** Higher JSD = OOD contains more domain pairs rare or absent in ID → harder generalisation task.

**Threshold:** JSD > 90th percentile relative to a neutral model (random architectures with matched domain frequencies).

**Dual requirement:** A valid split must satisfy *both* p < 0.01 *and* JSD above threshold. A significant p-value with low JSD indicates statistically non-random but trivially easy; high JSD with non-significant p-value may reflect structure from noise.

---

## 2. Tiered Biological Validation

A three-tier hierarchy assesses whether OOD domain pairs are genuinely novel or biologically plausible (false negatives). Query data sources from most definitive to most noisy.

### Tier 1 — Physical Interaction (Gold Standard)

**Sources:** iPfam + 3did databases, mapped via PDBe-SIFTS (Structure Integration with Function, Taxonomy and Sequence) at residue level.

**Procedure:**
1. Compile all unique domain pairs appearing in the OOD test set.
2. For each pair, query iPfam/3did for known 3D structural interactions.
3. Cross-reference with SIFTS to confirm the interacting residues map to the specific Pfam domains in the architecture.

**Interpretation:** A domain pair with a confirmed residue-level structural interaction is **unequivocally a plausible combination**. Every such pair in the OOD set is a definitive false negative.

**Output:** Count |P¹_plausible| of Tier 1–confirmed OOD pairs.

### Tier 2 — Evolutionary Co-Occurrence

**Source:** Domain co-occurrence network from a large, phylogenetically diverse collection of proteomes.

**Procedure:**
1. Construct network where nodes = Pfam domains, edges weighted by co-occurrence frequency across diverse species.
2. For each OOD domain pair, compute co-occurrence score (normalised for individual domain frequencies).
3. Flag pairs exceeding the 95th percentile of all possible domain pair scores.

**Interpretation:** High co-occurrence across evolutionarily distant species suggests functional or structural constraint — these pairs are likely compatible even without resolved 3D structure.

**Output:** Count |P²_plausible| of Tier 2–flagged OOD pairs (≥95th percentile).

**Role:** Bridges the coverage gap left by incomplete PDB structural data in Tier 1.

### Tier 3 — Functional Association (Noisy Sanity Check Only)

**Source:** STRING database (experimental, gene neighbourhood, co-expression, text mining).

**Procedure:**
1. For each OOD domain pair, retrieve STRING combined score for the proteins containing those domains.
2. Flag pairs with scores above a high confidence threshold (e.g., > 0.7).

**Interpretation:** STRING associations do not imply direct physical interaction — two proteins can share a pathway without binding. Do **not** use Tier 3 for FNR calculation.

**Role:** Triage edge cases for manual curation; flag potential false negatives for deeper investigation. High STRING score + no Tier 1/2 evidence → candidate for literature review.

---

## 3. Rule-Based Contextual Filters

Rule-based checks are supplementary — they identify high-confidence edge cases but cannot substitute for statistical or tiered biological validation.

| Check | Purpose | Resource | Output |
|-------|---------|----------|--------|
| **Structural incompatibility** | Identify physically impossible domain combinations (false positives) | CATH fold classification | % of OOD pairs flagged as incompatible |
| **Conserved functional modules** | Catch egregious FNs — domain pairs that co-occur in known functional systems | Curated literature list (kinase-SH2, SH3-polyproline, Ig-Fn3, etc.) | Count of known modules appearing in OOD |
| **Clan co-occurrence patterns** | Refine Tier 2 analysis — domains from the same clan co-occurring in complex architectures | Pfam clan hierarchy | Multi-domain architecture complexity within clans |

### 3.1 Known Conserved Modules

These pairs are evolutionarily co-dependent and should never appear as OOD if both partner families are in the training set:

- Kinase + SH2 (cell signalling)
- SH3 + polyproline motif (cell signalling)
- Immunoglobulin + Fibronectin type III (cell adhesion)
- EF-hand + IQ motif (calcium signalling)
- Peptidase + Inhibitor (proteolytic regulation)
- AAA ATPase + associated domain (ATPase regulation)

### 3.2 CATH Incompatibility Filter

Query CATH for incompatible structural pairings. If CATH assigns two domains to folds known to be sterically incompatible, the pair is a likely false positive. This checks for erroneous OOD inclusion rather than FN detection.

---

## 4. Quantitative Metrics and Thresholds

| Metric | Definition | Formula / Method | Target Threshold |
|--------|------------|-----------------|------------------|
| **Permutation p-value** | Probability of observed ΔCG under null (random partitioning) | (shuffled ΔCG ≥ observed) / 10,000 | p < 0.01 |
| **JSD** | Jensen-Shannon divergence between ID and OOD adjacency distributions | JSD(P_ID || P_OOD) | > 90th percentile of neutral model |
| **FNR** | False negative rate: fraction of OOD pairs that are biologically plausible | (|P¹_plausible| + |P²_plausible|) / |P_OOD| | < 5% |
| **CATH incompatibility** | Fraction of OOD pairs structurally impossible | | < 2% (diagnostic only) |
| **Conserved modules** | Number of known modules in OOD | | 0 (hard fail if > 0 and module families in training) |

### 4.1 FNR Formula

$$FNR = \frac{|P^{\text{T1}}_{\text{plausible}}| + |P^{\text{T2}}_{\text{plausible}}|}{|P_{\text{OOD}}|}$$

Where:
- |P_OOD| = total unique domain pairs in OOD test set
- |P^T1_plausible| = pairs with confirmed Tier 1 structural interaction
- |P^T2_plausible| = pairs exceeding 95th percentile of co-occurrence in Tier 2

Tier 3 (STRING) is excluded from the denominator to avoid inflating FNR with noisy functional associations.

---

## 5. Actionable Protocol

A 5-step iterative cycle for developing and validating PfamCG-1.0 splits:

### Step 1: Initial Partition
Partition architectures by recombination distance using the chosen algorithm (see `docs/research/existing-benchmarks.md` §4 for split strategies). Generate candidate ID (train+val) and OOD (test) sets.

### Step 2: Statistical Validation
- Compute ΔCG for the candidate split.
- Run permutation test (10,000 shuffles) → p-value.
- Compute JSD between ID/OOD adjacency distributions.
- **Pass condition:** p < 0.01 AND JSD > 90th percentile.

### Step 3: Biological Plausibility Assessment
- Compile all unique domain pairs in OOD.
- Query **Tier 1** (iPfam + SIFTS) → count |P¹_plausible|.
- Query **Tier 2** (co-occurrence network) → count |P²_plausible|.
- Query **Tier 3** (STRING) → flag for manual review (not for FNR).
- Query **rule-based filters** (CATH, conserved modules) → supplementary counts.

### Step 4: Pass/Fail Determination
| Criterion | Pass | Fail |
|-----------|------|------|
| Permutation p-value | < 0.01 | ≥ 0.01 |
| JSD | > 90th percentile | ≤ 90th percentile |
| FNR | < 5% | ≥ 5% |
| Conserved modules in OOD | 0 | > 0 (hard fail) |

**Pass:** All criteria met → split is validated for PfamCG-1.0 release.

**Fail:** Any criterion unmet → proceed to Step 5.

### Step 5: Refine and Iterate
- If FNR ≥ 5% (too many false negatives): relax recombination distance cutoff or refine clustering to group more related architectures into ID.
- If p ≥ 0.01 (split not statistically distinct): tighten recombination distance cutoff.
- If JSD ≤ 90th percentile (OOD too similar to ID): increase proportion of distant recombination pairs in OOD.
- Update partitioning parameters, re-run Steps 1–4. Continue until all criteria pass.

---

## 6. Phase 07 Implications

This document directly informs Phase 07 (PfamCG-1.0 Benchmark) Tasks 7.3.1–7.3.5:

| Phase 07 Task | Current Specification | Research Recommendation | Delta |
|---------------|---------------------|------------------------|-------|
| **7.3.1** (iPfam validation) | Check known 3D interactions for OOD pairs | Augment with PDBe-SIFTS residue-level mapping; formalise as Tier 1 of FNR calculation | ✅ Aligned, add SIFTS detail |
| **7.3.2** (Split B holdout) | Verify held-out families exist in ≥1 protein outside dataset | Add co-occurrence network as Tier 2 validation | ✅ Aligned, formalise co-occurrence |
| **7.3.3** (Split C clans) | Phylogenetic tree / clan hierarchy check | Add clan co-occurrence patterns + JSD metric | ❌ JSD metric missing |
| **7.3.4** (Permutation test) | 1,000 permutations | **Increase to 10,000** (stable p-value at α = 0.01) | ❌ Increase permutations |
| **7.3.5** (Validation report) | Document results | Add FNR, JSD, and conserved-module checks to report | ❌ Add metrics |
| **Not in Phase 07** | — | Add FNR as explicit validation metric with < 5% target | **New** |
| **Not in Phase 07** | — | Add conserved module hard-fail check | **New** |

### Recommended Updates to Phase 07 (`docs/phases/07_pfamcg_benchmark.md`)

1. **Task 7.3.4**: Change "1000 times" → "10,000 times" and update exit criterion p < 0.05 → p < 0.01.
2. **Task 7.3.5**: Rename to "Biological validation report" and add: FNR calculation, JSD values, conserved module audit.
3. **New subtask 7.3.6**: "Compute FNR = (|P_T1| + |P_T2|) / |P_OOD|; verify < 5%."
4. **New subtask 7.3.7**: "Check conserved modules list against OOD pairs; if any module is partially present in training, fail."

---

## Cross-References

- `docs/research/existing-benchmarks.md` — ΔCG definition, PfamCG-1.0 split strategies, novelty claim
- `docs/research/pfam-structure-notes.md` — Pfam clans, domain architecture representation for Tier 2 analysis
- `docs/phases/07_pfamcg_benchmark.md` — Phase 07 task mapping with delta recommendations
- `paper-neurips/main.tex` — Validation results may inform §4 (PfamCG-1.0 benchmark) methods description
