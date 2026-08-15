# Phase 01 — Pfam Data Pipeline

**Deadline**: 2 Aug 2026
**Dependencies**: Phase 00_repo, Phase 00_5
**Output**: `code/sigma/proteins/data.py`, `code/sigma/proteins/splits.py`, parsed Pfam dataset, compositional splits

---

### Task 1.1: Pfam data download and checksum verification

- [ ] 1.1.1: Download Pfam-A seed alignments from InterPro FTP: `https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.seed.gz` (≈165 MB)
- [ ] 1.1.2: Download Pfam-A HMM library: `https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz` (≈331 MB)
- [ ] 1.1.3: Download Pfam-A HMM data file: `https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.dat.gz` (≈637 KB)
- [ ] 1.1.4: Download Pfam clan mapping: `https://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.clans.tsv.gz`
- [ ] 1.1.5: Compute SHA256 checksums for all downloaded files and record in `docs/protein-data-registry.md`
- [ ] 1.1.6: Verify checksums against EBI SHA256SUMS file
- [ ] 1.1.7: Extract all `.gz` files to a dedicated data directory (gitignored per AGENTS.md)
- [ ] 1.1.8: Add data directory to `.gitignore` — pattern: `data/pfam/raw/`

### Task 1.2: Stockholm format parser (`proteins/data.py`)

- [ ] 1.2.1: Implement `parse_stockholm(filepath: str) -> list[dict]` using `Bio.SearchIO.parse()` or `Bio.Align.parse()` with Stockholm format
  - Parse fields: sequence ID, domain architecture string, species taxonomy, Pfam family accessions
  - Yield one record per protein sequence containing its domain architecture as ordered list of Pfam family accessions
- [ ] 1.2.2: Implement `extract_domain_architectures(records: list[dict], min_length: int = 2, max_length: int = 15) -> list[list[str]]`
  - Filter: only sequences with domain annotations (contain Pfam domain hits)
  - Filter: domain architectures with length in [min_length, max_length]
  - Filter: exclude sequences with overlapping or nested domains (ambiguity in architecture string)
  - Return: list of domain architecture sequences (each is list of Pfam accession strings like `["PF00168", "PF00041"]`)
- [ ] 1.2.3: Implement `PfamDataset(Dataset)` — PyTorch Dataset that:
  - Stores list of domain architecture sequences as integer token sequences
  - `__len__()` returns N architectures
  - `__getitem__(idx)` returns `(src_tensor, tgt_tensor)` pair for language modelling (predict next domain)
  - Handles padding, SOS/EOS tokens (reusing patterns from `SCANDataset` in `code/sigma/utils/data.py`)
- [ ] 1.2.4: Implement `build_domain_vocab(architectures: list[list[str]]) -> tuple[dict[str,int], dict[int,str]]`
  - Build token→id mapping for all Pfam accessions
  - Reserve special tokens: `<PAD>`:0, `<SOS>`:1, `<EOS>`:2, `<MASK>`:3, `<UNK>`:4
  - Also build clan-level mapping: fold each Pfam accession to its clan ID
- [ ] 1.2.5: Implement `download_pfam(output_dir: str, pfam_version: str = "38.2")` — idempotent download function with checksum verification, retry logic, and progress bar
- [ ] 1.2.6: Implement `get_domain_metadata() -> pd.DataFrame` — table with columns: pfam_accession, clan, family_name, family_type (Family/Domain/Repeat/Motif), description, length
- [ ] 1.2.7: Write unit tests for all parser functions in `tests/test_proteins_data.py`
  - Test parsing of a known Stockholm record
  - Test filter edge cases (length 1 architecture, >15 architecture, overlapping domains)
  - Test vocabulary construction and special token assignment
  - Test PfamDataset shapes and SOS/EOS token positions

### Task 1.3: HMMER bit score computation (`proteins/data.py`)

- [ ] 1.3.1: Implement `compute_domain_similarity(accession_a: str, accession_b: str, hmm_file: str) -> float`
  - Use `pyhmmer` to load HMM profiles for both Pfam families
  - Compute HMMER bit score as measure of domain similarity: `phi(d_a, d_b)`
  - Bit score = `log2(P(sequence|model) / P(sequence|null))` — phylogenetically grounded similarity metric
- [ ] 1.3.2: Implement `precompute_similarity_matrix(accessions: list[str], hmm_file: str, cache_path: str) -> np.ndarray`
  - Precompute N×N pairwise domain similarity matrix (N ≈ 22,000 families)
  - Cache to disk (`np.save` or pickle) to avoid recomputation — this is expensive (~484M comparisons)
- [ ] 1.3.3: Implement `compute_fold_compatibility(accession_a: str, accession_b: str) -> float`
  - Fold compatibility score based on: (1) same clan → high compatibility; (2) different clan but known PDB interaction → medium; (3) different clan, no known interaction → low
  - Use clan mapping file and PDB interaction data from iPfam or 3did
- [ ] 1.3.4: Write tests for HMMER integration in `tests/test_proteins_data.py`

### Task 1.4: Compositional split generation (`proteins/splits.py`)

- [ ] 1.4.1: Implement `make_compositional_splits(architectures: list[list[str]], similarity_matrix: np.ndarray, seed: int = 42) -> dict`
  - Three partition types matching Phase 3 conditions:
    - **Type A (familiar combinations)**: ID contains full architectures; OOD contains same domain families but in combinations seen during training (same-domain hold-out on sequence level)
    - **Type B (new family recombinations)**: ID contains subset of domain families; OOD contains novel combinations of those same families (domain-family-level hold-out)
    - **Type C (cross-fold recombination)**: ID contains subset of clans/folds; OOD contains combinations where one or more domains come from held-out clans (fold-level hold-out)
- [ ] 1.4.2: Implement `recombination_distance(arch_a: list[str], arch_b: list[str], similarity_matrix: np.ndarray) -> float`
  - Distance metric: `1 - psi_geometric(sim(d1,d2))` averaged over cross-domain pairs where `psi_geometric` is from `code/sigma/ode/equations.py`
- [ ] 1.4.3: Implement `compute_split_statistics(split_dict: dict) -> dict`
  - Report: architecture counts per split, unique domain families per split, domain type proportions, average architecture length, average recombination distance between ID and OOD sets
- [ ] 1.4.4: Generate the three splits and verify they produce non-trivial OOD accuracy gaps:
  - Type A ΔCG should be smallest (easiest OOD)
  - Type B ΔCG should be medium
  - Type C ΔCG should be largest (hardest OOD)
  - If splits are too easy (all models score >95%) or too hard (all models score <20%), adjust filtering thresholds
- [ ] 1.4.5: Write unit tests in `tests/test_proteins_splits.py`
  - Test that splits are disjoint (no architecture in both ID and OOD)
  - Test that vocabulary is consistent across splits
  - Test that split ratios are within configurable bounds (e.g., 80/20, 70/30, 60/40)

### Task 1.5: Data pipeline integration test

- [ ] 1.5.1: Write end-to-end integration script `scripts/verify_pfam_pipeline.py` that:
  - Downloads a small subset of Pfam (first 500 families)
  - Parses Stockholm records
  - Builds vocabulary
  - Generates compositional splits
  - Reports dataset statistics
- [ ] 1.5.2: Run pipeline on full Pfam 38.2 to verify:
  - Total architectures parsed
  - Number filtered by length constraints
  - Vocabulary size (should be ~22,000)
  - Distribution of architecture lengths (plot histogram)
- [ ] 1.5.3: Cache processed dataset to `data/pfam/processed/` for use in Phase 02+
  - Save: architecture tokens tensor, vocabulary files, split indices, similarity matrix
  - Format: PyTorch `torch.save()` for tensors, JSON/TSV for metadata

---

**Phase 01 Exit Criteria**:
- [ ] `code/sigma/proteins/data.py` fully implemented with tests
- [ ] `code/sigma/proteins/splits.py` fully implemented with tests
- [ ] Full Pfam 38.2 parsed and cached (vocab, architectures, splits, similarity matrix)
- [ ] Compositional splits validated: Type A < B < C difficulty gradient confirmed
- [ ] `PYTHONPATH=code:$PYTHONPATH python scripts/verify_pfam_pipeline.py` passes
- [ ] `pytest tests/test_proteins_data.py tests/test_proteins_splits.py` passes
- [ ] Dataset statistics documented in `docs/protein-data-registry.md`
