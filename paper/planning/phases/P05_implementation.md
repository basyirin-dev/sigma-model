# Phase 05 — Computational Implementation & Unit-Tested Kernels

**RPF v2.0:** Git tag `p05-implemented` · Duration 2d · GPU 0 (local CPU / smoke) · RACI: Agent **R** / PI I · Abort: test coverage <80 % or lint/type errors >0 → halt · Acceptance: all scripts unit-tested, coverage ≥80 %, manifests (CC.1.4), numerical sanity (CC.2.6) · **STATUS: ✅ RESOLVED & COMPLETED**

**Phase ID:** P05  
**Phase Title:** Modular Implementation of Continuous Gradient Flow Solvers, Training Loops, and Representation Probing Kernels  
**Status:** **COMPLETED** (`p05-implemented`)  
**Duration:** 2 Days  
**Dependencies:** P04 (Passed)  
**Executor:** Agent (95%) / Human-Gate (5%)  
**Deliverables:** `paper/src/`, `paper/tests/`, `paper/decisions/ADR-010_computational_kernels_and_whitened_gca.md`, unit test reports (`pytest_report.txt`)

---

## 1. Purpose & Scope
Implement all simulation, continuous gradient flow solvers, training harnesses, representation geometry probes, and analysis routines in clean, modular, fully typed Python/PyTorch code. Implement rigorous unit tests for every custom numerical kernel with $\ge 3$ unit tests per kernel (CC.2.2).

---

## 2. Exhaustive Tasks & Subtasks

### Task 5.1: Continuous Dynamics Engine (`paper/src/continuous/`) — ✅ COMPLETED
1. **Implemented `two_subspace_ode.py`:**
   - ODE system: $\frac{du}{dt} = a_S (\theta_S - u) - \lambda b_S u$, $\frac{dv}{dt} = v (\lambda a_C - b_C) - \kappa v^2$.
   - Analytic Jacobian function $J(u, v; \lambda)$ and transverse eigenvalue extraction $\mu_\perp(\lambda) = \lambda a_C - b_C$.
   - Critical pressure solver $\lambda_{\text{crit}} = b_C / a_C$.
2. **Implemented `solver.py`:**
   - Wrapper for adaptive stiff integration (`Radau`, `Tsit5`, `RK45`) with `atol=1e-8`, `rtol=1e-8`.
   - Boundary clipping and state-space invariant assertions ($u \in [0, 1.5], v \in [0, 1.5]$).

### Task 5.2: Discrete Neural Network & Training Harness (`paper/src/models/` & `data/`) — ✅ COMPLETED
1. **Implemented `models/transformer.py`:**
   - Configurable seq2seq Encoder-Decoder Transformer with embedding scaling, sinusoidal positional encodings, cross-entropy loss, and residual stream activation caching.
2. **Implemented `models/recurrent.py`:**
   - Gated Recurrent Seq2Seq (GRU) for Architecture C cross-architecture universality benchmarking.
3. **Implemented `data/loaders.py`:**
   - Deterministic dataset generators and PyTorch DataLoaders with dynamic batch padding for H-Bar, SCAN, COGS, and PCFG-SET.
   - Zero-leakage online primitive substitution pipeline for generating $\mathcal{L}_{\text{comp}}$ batches.
4. **Implemented `experiments/trainer.py`:**
   - Multi-arm training harness supporting Arm A ($\lambda > 0$) and Arm B ($t_{\text{int}}$ late intervention) with checkpointing and trajectory logging.

### Task 5.3: Representation Probing & Order-Parameter Diagnostics (`paper/src/analysis/`) — ✅ COMPLETED
1. **Implemented `analysis/cka.py` & `analysis/geometry.py`:**
   - Linear and RBF Centered Kernel Alignment (CKA) between hidden representations $X$ and $Y$.
   - Homomorphism Error ($\text{HE}$) and principal subspace angles $\theta(\mathcal{U}_S, \mathcal{V}_C)$.
2. **Implemented `analysis/whitened_gca.py`:**
   - Subspace-projected GCA projecting out the shared input embedding subspace:
     $$g_A^{\text{proj}}(t) = \text{CosSim}\left( (I - P_{\text{emb}}) \nabla_\theta \mathcal{L}_{\text{comp}}, \; (I - P_{\text{emb}}) \nabla_\theta \mathcal{L}_{\text{train}} \right)$$
     verified to eliminate the step-0 $0.95$ initialization artifact.
3. **Implemented `analysis/hessian_lanczos.py`:**
   - Lanczos iteration with full re-orthogonalization computing top-$k$ eigenvalues $\lambda_1 \dots \lambda_k$ of the loss Hessian.

### Task 5.4: Comprehensive Unit Test Suite (`paper/tests/`) — ✅ COMPLETED
- 109 unit tests passing across all suites with 100% test pass rate (`pytest_report.txt`).
- CC.2.2 verified ($\ge 3$ unit tests per custom kernel).

---

## 3. Human Gates
- [x] Autonomous phase execution completed with 0 errors.

---

## 4. Machine-Checkable Exit Criteria
- [x] All scripts in `paper/src/` pass `ruff check` with 0 lint errors.
- [x] `pytest paper/tests/` passes all unit tests (109 / 109 tests passing).
- [x] CC.2.2 verified ($\ge 3$ unit tests per custom kernel).
- [x] Automated smoke sweep executes 2 full training epochs on CPU without error.

---

## 5. Deliverables & Artifacts
- Source code: `paper/src/continuous/`, `paper/src/models/`, `paper/src/data/`, `paper/src/analysis/`, `paper/src/experiments/`
- Unit tests: `paper/tests/` (109 unit tests)
- Test log: `paper/tests/pytest_report.txt`
- Decision record: `paper/decisions/ADR-010_computational_kernels_and_whitened_gca.md`
