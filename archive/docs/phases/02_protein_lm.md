# Phase 02 — Custom Protein Language Model

**Deadline**: 23 Aug 2026
**Dependencies**: Phase 01 (data pipeline complete)
**Output**: `code/sigma/proteins/models.py`, `code/sigma/proteins/train.py`, `code/sigma/proteins/metrics.py`, trained model on Pfam data

---

### Task 2.1: SmallProteinLM architecture (`proteins/models.py`)

- [ ] 2.1.1: Implement `SmallProteinLM(nn.Module)` — adapted from `SigmaTransformer` in `code/sigma/models/transformer.py`:
  - Embedding layer: `nn.Embedding(vocab_size=22000, d_model=256, padding_idx=0)`
  - PositionalEncoding: sinusoidal, `max_len=20` (domain architectures are short)
  - Transformer encoder: `nn.TransformerEncoder` with `nn.TransformerEncoderLayer` (d_model=256, nhead=8, dim_feedforward=1024, dropout=0.1, num_layers=4)
  - Output projection: `nn.Linear(d_model, vocab_size)`
  - No decoder — this is encoder-only with LM head (masked domain modelling, not seq2seq)
- [ ] 2.1.2: Implement `count_parameters()` method (inherited pattern)
- [ ] 2.1.3: Implement Xavier uniform initialisation for all weight parameters `dim > 1`
- [ ] 2.1.4: Verify model: instantiate with vocab=22000, forward-pass a batch of (8×15) token sequences, confirm output shape is (8×15×22000)
- [ ] 2.1.5: Profile memory: ~22000 × 256 = 5.6M embedding params; 4 layers × (4×256×1024 + 4×256×8×64 + …) ≈ 20M total — should fit comfortably in T4 16GB

### Task 2.2: σ_A proxy hooks (`proteins/models.py`)

- [ ] 2.2.1: Implement `OdeAwareProteinLM(SmallProteinLM)` wrapper that adds σ_A instrumentation:
  - **Gradient Correlation Analysis (GCA)**: register forward hooks on each encoder layer; compute cosine similarity between gradient vectors of adjacent layers. High GCA = high σ_A.
  - **Representational Geometry Alignment (RGA)**: compute CKA (Centered Kernel Alignment) between hidden states of random architecture pairs. High RGA = model encodes consistent geometric relationships.
  - **Abstraction Coherence (AC)**: train a linear probe on hidden states from layer L to predict domain family identity; compute consistency of probe accuracy across OOD splits. High coherence = high σ_A.
- [ ] 2.2.2: Implement `compute_gca(model: OdeAwareProteinLM, loader: DataLoader) -> float` — GCA proxy for σ_A
- [ ] 2.2.3: Implement `compute_rga(model: OdeAwareProteinLM, loader: DataLoader) -> float` — RGA proxy for σ_A
- [ ] 2.2.4: Implement `compute_ac(model: OdeAwareProteinLM, loader: DataLoader) -> float` — AC proxy for σ_A
- [ ] 2.2.5: Implement `compute_sigma_proxy(model: OdeAwareProteinLM, loader: DataLoader) -> float` — fused σ_A proxy: `tilde_sigma_A = (w_gca * GCA + w_rga * RGA + w_ac * AC) / (w_gca + w_rga + w_ac)`
  - Default weights: all equal (1.0) — can be tuned in config
- [ ] 2.2.6: Write tests: verify proxy values are in [0,1], verify random model < trained model on all three proxies

### Task 2.3: Training loop (`proteins/train.py`)

- [ ] 2.3.1: Implement `train_protein_model()` — adapted from `code/sigma/models/training.py`:
  - Input: config dict, condition, run_id, output directory
  - Seeding: `torch.manual_seed(run_id * 42 + 7)`, `cudnn.deterministic = True`
  - Model: instantiate `OdeAwareProteinLM` with config params
  - Data: load Pfam dataset splits from Phase 01 cache
  - Optimizer: `Adam(lr=config['training']['lr'])` with LR scheduling (linear warmup + cosine decay)
  - Loss: `CrossEntropyLoss(ignore_index=0)` — predict masked domain identity
  - AMP: `torch.amp.autocast_mode.autocast` + `torch.amp.grad_scaler.GradScaler` (exact canonical paths from AGENTS.md)
  - ODE coupling: integrate `code/sigma/ode/solver.py` `SigmaODESolver`, update sigma/delta per step, apply additive/multiplicative coupling to loss
  - Evaluation: `fast_evaluate()` every `eval_every` steps (token-level accuracy)
  - σ_A measurement: `compute_sigma_proxy()` every `eval_every` steps
  - Checkpoint: save model state + ODE state + proxy values every 500 steps
  - Result: pickle `{metrics, config, seed, sigma_trajectory, delta_trajectory}` to output dir
- [ ] 2.3.2: Implement `fast_evaluate_protein(model, loader, max_batches=8) -> dict` — evaluate on a subset (speed optimisation for checkpointing)
  - Returns: `{acc_id, acc_ood, loss, sigma_proxy}`
- [ ] 2.3.3: Implement `evaluate_model_protein(model, id_loader, ood_loader) -> dict` — full evaluation on train/val/OOD splits
  - Returns: `{acc_id, acc_ood, acc_by_architecture_length, acc_by_family_count, confusion_matrix}`
- [ ] 2.3.4: Implement `compute_compositional_gap(id_accuracy: float, ood_accuracy: float) -> float`
  - ΔCG = id_accuracy - ood_accuracy (in percentage points)
- [ ] 2.3.5: Support three training conditions from `pfam-base.yaml`:
  - **baseline**: standard training, no curriculum — `sigma_init=0.10`
  - **additive**: `task_loss * (1.0 + coupling_strength * (1.0 - sigma))` — `sigma_init=0.05`
  - **multiplicative**: `task_loss * (1.0 + coupling_strength * sigma)` — `sigma_init=0.05`
- [ ] 2.3.6: Support distributed/multi-GPU via PyTorch `DataParallel` (Kaggle T4 is single-GPU, but code should not be single-device-locked)

### Task 2.4: Metrics module (`proteins/metrics.py`)

- [ ] 2.4.1: Implement `compute_domain_sigma(model_runs: list[dict]) -> dict`
  - Takes list of run result dicts
  - Returns: `{mean_sigma, std_sigma, sigma_by_condition, high_sigma_group, low_sigma_group}`
- [ ] 2.4.2: Implement `compute_compositional_gap_analysis(results: list[dict]) -> dict`
  - Per-condition ΔCG statistics
  - ΔCG distribution (histogram bin counts)
  - Correlation between σ_A proxy and ΔCG
- [ ] 2.4.3: Implement `compute_construct_isolation(target_scores, target_proxy_vals, confound_vals) -> float`
  - Reuse from `code/sigma/utils/metrics.py` — import and wrap for protein context
  - CI = |corr(target, proxy)| / |corr(target, confound)|, bounded [0,1]
  - Confounds for protein: architecture length, number of domain families, sequence diversity, taxonomic distribution
- [ ] 2.4.4: Implement `compute_reliability(model_runs: list[dict]) -> float`
  - Reuse from `code/sigma/utils/metrics.py`: RA = 1 / (1 + CV^2), bounded [0,1]
- [ ] 2.4.5: Write tests in `tests/test_proteins_metrics.py`
  - Test that σ_A proxy values are bounded [0,1]
  - Test that compute_compositional_gap(100, 100) = 0
  - Test that compute_compositional_gap(90, 40) = 50
  - Test construct isolation on synthetic data with known correlations

### Task 2.5: Pilot training run

- [ ] 2.5.1: Run `train_protein_model()` for N=1 run per condition (baseline, additive, multiplicative) on Pfam Type-A splits
  - 5000 timesteps, batch_size=32, d_model=256
  - Verify: training loss decreases, accuracy increases, σ_A proxy > 0 after convergence
- [ ] 2.5.2: Verify checkpointing works: kill half-way through, resume from last checkpoint, confirm loss continues from checkpoint value
- [ ] 2.5.3: Profile memory: confirm total VRAM usage < 14GB (leaving room for Kaggle T4 16GB)
- [ ] 2.5.4: Profile time: measure seconds per 1000 steps → estimate total time for N=500
- [ ] 2.5.5: Report pilot results in `docs/lab-notebooks/2026-07-protein-pilot.md`

---

**Phase 02 Exit Criteria**:
- [ ] `models.py` — SmallProteinLM + OdeAwareProteinLM fully implemented
- [ ] `train.py` — train_protein_model with 3 conditions, AMP, ODE coupling, checkpointing
- [ ] `metrics.py` — full metrics suite with σ_A proxy, ΔCG, CI, RA
- [ ] All tests pass: `pytest tests/test_proteins_models.py tests/test_proteins_metrics.py tests/test_proteins_train.py`
- [ ] Pilot training run converges on Type-A splits with expected loss/accuracy curves
- [ ] Profile report documents: VRAM usage, time per 1000 steps, estimated N=500 wall time
