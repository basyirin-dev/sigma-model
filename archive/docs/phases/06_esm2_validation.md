# Phase 06 — ESM-2 Scale-Up Validation

**Deadline**: 7 Mar 2027
**Dependencies**: Phase 04, Phase 05 (results inform ESM-2 experimental design)
**Output**: ESM-2 fine-tune results, σ-trap replication check, data leakage documentation

---

### Task 6.1: ESM-2 integration

- [ ] 6.1.1: Load ESM-2 650M via `fair-esm`:
  - `esm2_t33_650M_UR50D()` from `esm.pretrained`
  - Verify model loads on GPU with ~5GB VRAM headroom (model ≈ 1.3GB, activations vary)
  - Confirm tokeniser: `Alphabet.get_til5_vocab()` from `esm.data`
  - Test forward pass on one batch of Pfam domain sequences
- [ ] 6.1.2: Map Pfam domain architectures to ESM-2 amino acid sequences:
  - For each domain architecture (list of Pfam accessions), retrieve representative amino acid sequence from Pfam seed alignment
  - Concatenate domain sequences with or without linkers (document choice)
  - Create `ESM2PfamDataset(Dataset)` that yields (tokens, domain_labels) pairs
    - `domain_labels`: per-position label indicating which Pfam family each amino acid belongs to
- [ ] 6.1.3: Implement `load_esm2_model(model_size: str = "650M", device: str = "cuda") -> tuple`
  - Returns: `(model, alphabet, batch_converter)`
  - Supports model sizes: 8M, 35M, 150M, 650M, 3B (configurable)

### Task 6.2: Data leakage documentation

- [ ] 6.2.1: Document ESM-2 training data cutoff:
  - Training set: UniRef50, September 2021 version
  - Validation set: 0.5% random subset of UniRef50
  - Training filtered: sequences with >50% identity to validation removed
- [ ] 6.2.2: Compute overlap statistics between ESM-2 training data and Pfam 38.2:
  - For each Pfam family in our dataset, check if ≥1 representative sequence appears in UniRef50 (2021)
  - Report: % of Pfam families with overlap, % fully absent
  - If overlap > 30%, adjust — use only Pfam families absent from ESM-2 training data for OOD splits
- [ ] 6.2.3: Document leakage-mitigation strategy in paper:
  - Primary analysis uses custom SmallProteinLM trained from scratch (no leakage possible)
  - ESM-2 fine-tune is reported as confirmation
  - Any leakage is conservative bias (makes σ-trap harder to detect, not easier)

### Task 6.3: ESM-2 fine-tuning pipeline

- [ ] 6.3.1: Implement `fine_tune_esm2(model, train_loader, val_loader, config) -> dict`
  - Add domain-level prediction head: `nn.Linear(esm_embedding_dim, n_pfam_families)`
  - Training: full fine-tune (all ESM-2 parameters + head) OR head-only (probe). Both.
  - Optimiser: `AdamW(lr=1e-5)` for full fine-tune, `AdamW(lr=1e-3)` for head-only
  - LR schedule: linear warmup (10% of steps) + cosine decay
  - AMP: same pattern as `train_protein_model()` — reuse from Phase 02
  - Supported ESM-2 sizes: 650M (primary), 8M (ablation)
- [ ] 6.3.2: Implement σ_A proxy measurement for ESM-2:
  - GCA: hook the 33 transformer layers of ESM-2 650M; compute gradient correlations
  - RGA: CKA between ESM-2 hidden states for random architecture pairs
  - AC: probe consistency — same linear probe as `DomainAnalogyProbe` but on ESM-2 hidden states
  - Fused: same weighted combination as `OdeAwareProteinLM`
- [ ] 6.3.3: Fine-tune ESM-2 650M on Pfam Type-B splits (new family recombinations):
  - 20 runs: 10 with standard training, 10 with additive curriculum
  - Evaluate: σ_A proxy, ΔCG, structural vs lexical gap
  - Compare: does ESM-2 show the same σ-trap pattern as SmallProteinLM?
  - Record results to `results/pfam-esm2/esm2_results.parquet`

### Task 6.4: Ablation: ESM-2 8M

- [ ] 6.4.1: Repeat fine-tuning on ESM-2 8M (6 layers, 320-dim) — controls for model scale
  - If σ-trap appears in 8M but not 650M → scale mitigates the trap (interesting result)
  - If σ-trap appears in both → the trap is architecture-independent (stronger claim)
  - If σ-trap appears in neither → ESM pretraining already confers high σ_A (must explain why)
- [ ] 6.4.2: Record results to `results/pfam-esm2/esm2_8m_results.parquet`

### Task 6.5: σ-trap replication analysis

- [ ] 6.5.1: Direct comparison: for each ESM-2 fine-tune run, compute:
  - σ_A proxy distribution
  - ΔCG by condition
  - Correlation: σ_A vs OOD accuracy (same as Phase 04 H1 analysis)
- [ ] 6.5.2: Replication check — three questions:
  - Q1: Is σ_A proxy variance substantial across ESM-2 fine-tune runs? (If all runs converge to same σ_A, σ_A isn't meaningful in this setting)
  - Q2: Does σ_A proxy predict OOD accuracy in ESM-2? (H1 replication)
  - Q3: Does curriculum training (additive condition) increase σ_A in ESM-2? (mechanism replication)
- [ ] 6.5.3: If σ-trap replicates → paper claims "the effect holds at production scale"
  - "The σ-trap is not an artefact of small custom models"
- [ ] 6.5.4: If σ-trap does NOT replicate → paper discusses why:
  - ESM-2 pretraining already induces high σ_A (the representations are compositionally structured)
  - The σ-trap is a training-from-scratch phenomenon
  - This is an informative result: pretraining mitigates, but does not eliminate, the trap

### Task 6.6: Figure generation

- [ ] 6.6.1: Generate Figure 5 (ESM-2 validation):
  - Panel A: σ_A proxy comparison — SmallProteinLM vs ESM-2 650M vs ESM-2 8M (bar chart)
  - Panel B: σ_A vs OOD accuracy scatter (ESM-2 650M only)
  - Panel C: ΔCG comparison SmallProteinLM vs ESM-2 (grouped bar)
  - Panel D: σ_A trajectory during fine-tuning (if fine-tuning data collected)
- [ ] 6.6.2: Register alt-text in `docs/figure-alt-text.md`

---

**Phase 06 Exit Criteria**:
- [ ] ESM-2 650M and 8M fine-tuning pipelines complete
- [ ] Data leakage analysis documented (overlap % between ESM-2 training data and Pfam 38.2)
- [ ] σ_A proxy successfully measured on ESM-2 models
- [ ] Replication analysis complete (trap replicates or not — documented either way)
- [ ] Figure 5 saved to `paper-neurips/figures/`
- [ ] C-039, C-040 updated with ESM-2 replication information
