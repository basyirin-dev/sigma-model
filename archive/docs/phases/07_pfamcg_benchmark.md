# Phase 07 — PfamCG-1.0 Benchmark

**Deadline**: 25 Jul 2027
**Dependencies**: Phase 01 (data pipeline), Phase 04 (insights on what constitutes meaningful OOD splits)
**Output**: PfamCG-1.0 benchmark release, validation report, dataset card

---

### Task 7.1: Benchmark split construction (`proteins/benchmark.py`)

- [ ] 7.1.1: Implement `PfamCGBenchmark` class:
  - 3 split types matching paper claims:
    - **Split A (seen-family recombination)**: all domain families appear in training; OOD tests novel *combinations* of familiar families
    - **Split B (seen-fold recombination)**: all clans/folds appear in training; OOD tests combinations where specific family instances are novel but fold compatibility is familiar
    - **Split C (cross-fold recombination)**: OOD tests combinations where one or more domains come from held-out folds/clans — severe compositional challenge
  - Each split: ID (train+val) and OOD (test) partitions
  - Optional: easy/medium/hard difficulty tiers per split
- [ ] 7.1.2: Implement `build_split_A(architectures, similarity_matrix, seed) -> dict`
  - Strategy: 80% of architectures for training, 20% held out
  - Ensure all domain families appear in training split
  - OOD architectures are those composed entirely of seen families but in unseen combinations
  - Validation: no OOD architecture's domain set is a subset of any training architecture's domain set
- [ ] 7.1.3: Implement `build_split_B(architectures, clan_map, similarity_matrix, seed) -> dict`
  - Strategy: hold out specific families (30% of families)
  - OOD architectures contain ≥1 held-out family
  - BUT: held-out families belong to clans seen in training (fold-level familiarity preserved)
- [ ] 7.1.4: Implement `build_split_C(architectures, clan_map, seed) -> dict`
  - Strategy: hold out entire clans (20% of clans)
  - OOD architectures contain ≥1 domain from a held-out clan
  - Most severe test: models must generalise to entirely novel fold contexts
- [ ] 7.1.5: Implement `compute_split_statistics(split_dict, similarity_matrix, clan_map) -> dict`
  - Report: N_architectures per split, N_families per split, avg length, avg max pairwise similarity within ID/OOD, clan distribution, difficulty metrics

### Task 7.2: HMMER bit score computation for all families

- [ ] 7.2.1: Reuse `precompute_similarity_matrix()` from Phase 01 (if not already computed for full Pfam 38.2)
  - If cached similarity matrix exists, verify and load
  - If not, compute: 22,000 × 22,000 ≈ 484M pairwise comparisons
  - Profile: wall time, cache size (22K × 22K × 4 bytes ≈ 2GB for float32)
- [ ] 7.2.2: Compute clan-level similarity matrix:
  - Average bit score between families in the same clan
  - Cross-clan bit score distribution (for Split C threshold setting)
- [ ] 7.2.3: Document: distribution of bit scores (histogram), threshold for "compatible" vs "incompatible" domain pairs

### Task 7.3: Biological validation

- [ ] 7.3.1: Validate Split A against known biology:
  - Check: do OOD architectures contain biologically plausible domain combinations? (i.e., fold-compatible pairs that happen to be unseen)
  - Use iPfam or 3did database: for each OOD domain pair, is there a known 3D interaction?
  - Report: % of OOD pairs with known interaction → should be > 0 (otherwise OOD is all impossible combinations, which is trivially hard)
- [ ] 7.3.2: Validate Split B:
  - Check: are held-out families truly absent from training architectures?
  - For each held-out family, verify it appears in ≥1 protein sequence outside our dataset (confirm it's a real family, not a Pfam artefact)
- [ ] 7.3.3: Validate Split C:
  - Check: are held-out clans truly evolutionarily distinct from training clans?
  - Use phylogenetic tree or clan hierarchy to confirm minimal recent common ancestry
- [ ] 7.3.4: Permutation test: randomly shuffle split assignments 10000 times; verify that the real splits produce a larger ΔCG gap than 99% of random splits (p < 0.01)
- [ ] 7.3.5: Document validation results in `docs/research/pfamcg-validation-report.md`

### Task 7.4: Baseline evaluation

- [ ] 7.4.1: Compute baselines for all 3 splits:
  - Random baseline: predict domain from vocabulary uniformly at random
  - Frequency baseline: predict most common domain in training set
  - Bigram baseline: predict next domain using training bigram frequencies
  - SmallProteinLM baseline (from Phase 02)
  - ESM-2 baseline (from Phase 06)
- [ ] 7.4.2: For each baseline, report: Acc_ID, Acc_OOD, ΔCG per split
- [ ] 7.4.3: Determine ΔCG difficulty tiers:
  - Easy: ΔCG < 10pp
  - Medium: ΔCG 10–30pp
  - Hard: ΔCG > 30pp

### Task 7.5: Dataset card and community release

- [ ] 7.5.1: Create dataset card following HuggingFace Datasets standard:
  - Dataset name: `PfamCG-1.0`
  - Description: compositional generalisation benchmark for protein domain architectures
  - Splits: train/val/test for each of 3 split types
  - Size: N architectures, N families, N clans
  - Data provenance: Pfam 38.2, SHA256 checksums
  - License: CC0 (same as Pfam)
  - Intended use: evaluating compositional generalisation in protein ML models
  - Limitations: based solely on domain architecture sequences, not 3D structure
- [ ] 7.5.2: Create `data/pfamcg-1.0/` directory with:
  - `README.md` — benchmark description and usage
  - `data/` — architecture IDs, splits, family metadata (CSV/JSON/Parquet)
  - `baselines/` — baseline scores
  - `evaluation/` — evaluation script (`evaluate_pfamcg.py`)
- [ ] 7.5.3: Implement `evaluate_pfamcg(model, model_type: str, split_type: str) -> dict`
  - Standard evaluation entry point: takes a model, returns acc_id, acc_ood, ΔCG
  - Supports: `small_protein_lm`, `esm2_probe`, `esm2_finetune`, `custom` (any model with compatible interface)
- [ ] 7.5.4: Upload to HuggingFace Datasets (optional, after NeurIPS acceptance):
  - Repository: `https://huggingface.co/datasets/basyirin-dev/PfamCG`
  - Include dataset card, evaluation script, baseline scores

### Task 7.6: Figure generation

- [ ] 7.6.1: Generate Figure 6 (PfamCG-1.0 overview):
  - Panel A: 3 split types visualised (Venn-like diagram showing ID/OOD family overlap)
  - Panel B: ΔCG across splits for each baseline model (grouped bar chart)
  - Panel C: Difficulty gradient (Easy/Medium/Hard) × Split type (heatmap)
  - Panel D: Permutation test result — real vs random ΔCG distribution
- [ ] 7.6.2: Register alt-text

---

**Phase 07 Exit Criteria**:
- [ ] `code/sigma/proteins/benchmark.py` implemented with 3 split types
- [ ] All 3 splits pass biological validation (compatible pairs exist, held-out families are real, clans are distinct)
- [ ] Permutation test: real splits > random at p < 0.05
- [ ] Baseline evaluations complete for all 3 splits
- [ ] Dataset card and evaluation script released in `data/pfamcg-1.0/`
- [ ] Figure 6 saved to `paper-neurips/figures/`
- [ ] Claim C-044 updated to COLLECTED or VERIFIED
