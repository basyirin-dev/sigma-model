# Phase 06 — Data Generation & Simulation Execution

**RPF v2.0:** Git tag `p06-data-complete` · Duration 3–5d · GPU 20 + TPU 10 · RACI: Agent **R** / PI C (anomaly) · Abort: NaN/Inf → halt arm; budget >20 % over → halt all · Acceptance: run-log complete, no NaN/Inf, SHA-256 hashes, manifests valid, `NEGATIVE` results documented · *Pending (locked by P03 gate).*

**Phase ID:** P06  
**Phase Title:** Large-Scale Multi-Seed Data Generation, Continuous-Flow Grid Integration, and Raw Tensor Archival  
**Status:** Pending  
**Duration:** 3–5 Days  
**Dependencies:** P05  
**Executor:** Agent (95%) / Human-Gate (5%)  
**Deliverables:** `paper02/data/raw/`, `paper02/data/processed/`, `paper02/experiments/run-log.csv`

---

## 1. Purpose & Scope
Execute all multi-seed continuous-flow integrations, deep Transformer parameter sweeps, late-onset intervention grids, and cross-benchmark experiments across local GPUs and Kaggle sessions. Enforce raw data immutability (CC.4.1), verify absence of NaNs, and log runtime metadata in `run-log.csv`.

---

## 2. Exhaustive Tasks & Subtasks

### Task 6.1: Continuous Dynamics Numerical Integration (Diffrax Grid)
1. **Dense Continuous Sweep:**
   - Integrate two-subspace ODE across continuous parameter grid $\lambda \in [0.0, 3.0]$ with resolution $\Delta \lambda = 0.01$ (301 parameter points).
   - For each $\lambda$, integrate from $t=0$ to $t=2000$ across 50 initial conditions $(u_0, v_0) \in [0.01, 0.99]^2$.
   - Save vector field trajectories, fixed point locations, and Jacobian eigenvalues to `data/raw/continuous_flow_grid.parquet`.
2. **Separatrix & Phase Portrait Computation:**
   - Compute the unstable manifold connecting $E_S$ and $E_C$.
   - Save theoretical separatrix coordinates to `data/processed/theoretical_separatrix.csv`.

### Task 6.2: Discrete Neural Network Production Sweeps (PyTorch / GPU)
1. **Experiment Arm 1 — Dense Critical Pressure Sweep (H-Bar):**
   - Grid: $\lambda \in \{0.00, 0.05, 0.10, 0.20, 0.30, 0.50, 0.75, 1.00, 1.50, 2.00\}$ (10 levels).
   - Replications: $n = 30$ seeds per cell ($300$ runs total).
   - Training: 2000 steps per run, eval every 25 steps.
2. **Experiment Arm 2 — Late-Onset Intervention Grid (H-Bar):**
   - Grid: $t_{\text{int}} \in \{0, 100, 250, 500, 1000 \text{ steps}\}$, with $\lambda = 1.0$ (5 levels).
   - Replications: $n = 30$ seeds per cell ($150$ runs total).
3. **Experiment Arm 3 — Cross-Benchmark Replication (SCAN & COGS):**
   - SCAN `add_primitive` (jump): $\lambda \in \{0.0, 0.1, 0.3, 0.5, 1.0\}$, $n = 15$ seeds ($75$ runs).
   - SCAN `length_split`: $\lambda \in \{0.0, 0.1, 0.3, 0.5, 1.0\}$, $n = 15$ seeds ($75$ runs).
   - COGS structural recursion: $\lambda \in \{0.0, 0.1, 0.3, 0.5, 1.0\}$, $n = 15$ seeds ($75$ runs).
   - PCFG-SET: $\lambda \in \{0.0, 0.1, 0.3, 0.5, 1.0\}$, $n = 15$ seeds ($75$ runs).
   - *Total Discrete Sweeps:* $750$ runs.
4. **Execution & Checkpointing:**
   - Launch execution via Kaggle Notebook batch jobs and local CUDA sessions.
   - At each evaluation checkpoint (every 25 steps), log:
     `step`, `train_loss`, `comp_loss`, `acc_id`, `acc_ood`, `cka_rga`, `whitened_gca`, `top_hessian_eig`, `param_norm`.

### Task 6.3: Data Validation, Immutability & Logging
1. **Automated Sanity Check:**
   - Execute assertion script `paper02/src/analysis/check_raw_data.py`:
     - Assert zero NaN / Inf in any metric trajectory.
     - Assert all 750 planned runs completed full 2000 steps.
2. **Lock Raw Data Permissions (CC.4.1):**
   - Write raw output arrays to `paper02/data/raw/` and set read-only permissions (`chmod -R a-w paper02/data/raw/`).
3. **Idempotent Processed Data Derivation:**
   - Run `paper02/src/data/derive_processed_tables.py` to produce clean tidy dataframes in `paper02/data/processed/`:
     - `ood_summary_table.csv`
     - `inflection_breakpoints.csv`
     - `cka_trajectories.parquet`
     - `pairwise_welch_tost.csv`
4. **Master Run Log:**
   - Update `paper02/experiments/run-log.csv` logging `run_id`, `benchmark`, `lambda`, `t_int`, `seed`, `hardware`, `wall_clock_sec`, `status`.

---

## 3. Human Gates
- `[HUMAN-GATE]` Principal Investigator reviews summary metrics and confirms zero unhandled numerical anomalies before locking `data/raw/`.

---

## 4. Machine-Checkable Exit Criteria
- [ ] 750 discrete training runs and 301 continuous flow integrations complete with 100% success.
- [ ] `experiments/run-log.csv` has 750 rows with `status = done`.
- [ ] `data/raw/` contains all raw output tensors; write-protection asserted.
- [ ] `data/processed/` populated with all 4 tidy tables.
- [ ] CC.1.1, CC.1.2, and CC.4.1 compliance verified.
- [ ] `[HUMAN-GATE]` Data generation sign-off.

---

## 5. Deliverables & Artifacts
- Raw data tensors: `paper02/data/raw/`
- Derived processed tables: `paper02/data/processed/`
- Run registry: `paper02/experiments/run-log.csv`
