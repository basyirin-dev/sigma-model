# Phase 06 — Data Generation & Simulation Execution

**RPF v2.0:** Git tag `p06-data-complete` · Duration 3–5d · GPU 20 + TPU 10 · RACI: Agent **R** / PI C (anomaly) · Abort: NaN/Inf → halt arm; budget >20 % over → halt all · Acceptance: run-log complete, no NaN/Inf, SHA-256 hashes, manifests valid, `NEGATIVE` results documented · **STATUS: ⏸ BLOCKED_ON_REMEDIATION (Production Not Authorized)**

**Phase ID:** P06  
**Phase Title:** Large-Scale Multi-Seed Data Generation, Continuous-Flow Grid Integration, and Raw Tensor Archival  
**Status:** **BLOCKED_ON_REMEDIATION** (Gate baseline ingested; Multi-benchmark production pending dedicated authorization)  
**Duration:** 3–5 Days  
**Dependencies:** P05 (Passed), Pre-Phase 06 Remediation (Active)  
**Executor:** Agent (95%) / Human-Gate (5%)  
**Deliverables:** `paper/data/raw/`, `paper/data/processed/`, `paper/experiments/run-log.csv`, `paper/notebooks/kaggle_p06_tiered_cross_benchmark_sweep.ipynb`

---

## 1. Purpose & Scope
Execute authorized Phase 06 production sweeps across local GPUs and Kaggle sessions under the tiered matrix design (ADR-007 Amendment). Enforce raw data immutability (CC.4.1), verify absence of NaNs, and log runtime metadata in `run-log.csv`.

> **Governance Note on Inherited Gate Evidence:**  
> Phase 03 Gate data (450 runs on H-Bar) represents inherited baseline mechanism validation. It does **not** substitute for the Phase 06 dense boundary sweep ($\lambda \in \{0.015, 0.020, 0.025, 0.030\}$) or cross-benchmark production runs (SCAN, COGS, PCFG-SET).

---

## 2. Exhaustive Tasks & Subtasks

### Task 6.0: Inherited Gate Baseline Ingestion & Continuous Grid — ✅ COMPLETED
1. **Gate Baseline Ingestion:**
   - Ingested 450 Phase 03 Gate runs into `paper/data/raw/all_results.pkl` ($n=30$ seeds across 10 coarse $\lambda$ levels and 5 late-intervention levels).
2. **Continuous Flow Grid:**
   - Integrated calibrated two-subspace ODE continuous gradient flow system ($\lambda_{\text{crit}} = 0.025$, ADR-011) across 301 parameter points $\lambda \in [0.0, 3.0]$.
   - Saved 1,505 vector field trajectories to `paper/data/raw/continuous_flow_grid.csv`.

### Task 6.1: Tier 1 Primary Change-Point Production (720 Runs) — ⏳ PENDING_AUTHORIZATION
1. **Execution Scope:**
   - 4 Benchmarks ($\hbar$, SCAN `add_primitive_jump`, COGS, PCFG-SET) $\times$ 1 Architecture (Transformer 2L) $\times$ 6 $\lambda$ levels ($0.000, 0.015, 0.020, 0.025, 0.030, 0.500$) $\times$ 30 seeds = **720 runs**.
2. **Execution Protocol:**
   - Execute under deterministic Kaggle batch orchestration with PyTorch AMP and in-situ diagnostic probing.

### Task 6.2: Tier 2 Exploratory Architecture Scaling (240 Runs) — ⏳ PENDING_AUTHORIZATION
1. **Execution Scope:**
   - 4 Benchmarks $\times$ 2 Architectures (Transformer 4L, GRU Seq2Seq) $\times$ 3 $\lambda$ levels ($0.000, 0.025, 0.500$) $\times$ 10 seeds = **240 runs**.
2. **Execution Protocol:**
   - Exploratory screening to test capacity invariance and non-attention universality.

### Task 6.3: Production Zero-Leakage Re-Audit & Checksum Verification — ⏳ PENDING_AUTHORIZATION
1. **Re-Audit Execution:**
   - Re-run `paper/src/data/audit_leakage.py` asserting pairwise strict disjointness $\forall i \neq j: \text{supp}(\mathcal{D}_i) \cap \text{supp}(\mathcal{D}_j) = \emptyset$ on all production dataset splits.
2. **Integrity Manifests:**
   - Verify SHA-256 hashes against `paper/data/raw/checksums.sha256`.

### Task 6.4: Production Data Validation, Tidy Derivation & Master Log — ⏳ PENDING_AUTHORIZATION
1. **Automated Sanity Check:**
   - Run `paper/src/analysis/check_raw_data.py` asserting 0 NaNs and 0 Infs across all production tensors.
2. **Tidy Table Derivation:**
   - Run `paper/src/data/derive_processed_tables.py` generating tidy summary tables.
3. **Master Run Registry:**
   - Update `paper/experiments/run-log.csv` registering all 960 production runs.

---

## 3. Human Gates
- [x] Task 6.0: Principal Investigator Mechanism Gate audit passed.
- [ ] Task 6.4: Multi-benchmark production execution directive and final dataset audit sign-off.

---

## 4. Machine-Checkable Exit Criteria
- [x] Task 6.0: 450 gate baseline runs and 301 continuous flow integrations ingested.
- [ ] Tier 1 Primary Change-Point sweep complete (720 runs, $n=30$, 0 unhandled failures).
- [ ] Tier 2 Exploratory Architecture Scaling sweep complete (240 runs, $n=10$, 0 unhandled failures).
- [ ] `experiments/run-log.csv` updated with all 960 production run records.
- [ ] `data/raw/` contains all raw output tensors; write-protection asserted.
- [ ] Zero-leakage audit passes on all production benchmark splits with 0 overlaps.
- [ ] `data/processed/` populated with updated tidy tables across all 4 suites.
- [ ] CC.1.1, CC.1.2, and CC.4.1 compliance verified.
- [ ] 100% test pass rate across unit test suite.

---

## 5. Deliverables & Artifacts
- Raw data tensors: `paper/data/raw/` (`all_results.pkl`, `hbar_splits.json`, `scan_splits.json`, `cogs_splits.json`, `pcfg_set_splits.json`, `checksums.sha256`, `continuous_flow_grid.csv`)
- Derived processed tables: `paper/data/processed/` (`ood_summary_table.csv`, `inflection_breakpoints.csv`, `cka_trajectories.csv`, `pairwise_welch_tost.csv`, `theoretical_separatrix.csv`)
- Run registry: `paper/experiments/run-log.csv`
- Turnkey production notebook: `paper/notebooks/kaggle_p06_tiered_cross_benchmark_sweep.ipynb`
