# Phase 05 — Computational Implementation & Unit-Tested Kernels

**RPF v2.0:** Git tag `p05-implemented` · Duration 3–5d · GPU 4 · RACI: Agent **R** / PI I · Abort: test coverage <80 % or lint/type errors >0 → halt · Acceptance: all scripts unit-tested, coverage ≥80 %, manifests (CC.1.4), numerical sanity (CC.2.6) · *Pending (locked by P03 gate).*

**Phase ID:** P05  
**Phase Title:** Modular Implementation of Continuous Gradient Flow Solvers, Training Loops, and Representation Probing Kernels  
**Status:** Pending  
**Duration:** 2–3 Days  
**Dependencies:** P04  
**Executor:** Agent (95%) / Human-Gate (5%)  
**Deliverables:** `paper02/src/`, `paper02/tests/`, `paper02/notebooks/`, unit test reports

---

## 1. Purpose & Scope
Implement all simulation, continuous gradient flow solvers, training harnesses, representation geometry probes, and analysis routines in clean, modular, fully typed Python/JAX/PyTorch code. Implement rigorous unit tests for every custom numerical kernel with $\ge 3$ unit tests per kernel (CC.2.2).

---

## 2. Exhaustive Tasks & Subtasks

### Task 5.1: Continuous Dynamics Engine (`paper02/src/continuous/`)
1. **Implement `two_subspace_ode.py` (JAX/Diffrax):**
   - Implement ODE system:
     $$\frac{du}{dt} = a_S (\theta_S - u) - \lambda b_S u, \qquad \frac{dv}{dt} = v (\lambda a_C - b_C) - \kappa v^2$$
   - Implement analytic Jacobian function $J(u, v; \lambda)$ and transverse eigenvalue extraction $\mu_\perp(\lambda) = \lambda a_C - b_C$.
   - Implement critical pressure solver $\lambda_{\text{crit}} = b_C / a_C$.
2. **Implement `solver.py`:**
   - Wrapper for Diffrax `Tsit5` / `Kvaerno5` with adaptive step size control, `atol=1e-8`, `rtol=1e-8`.
   - Implement boundary clipping and state-space invariant assertion ($u \in [0, 1], v \in [0, 1]$).

### Task 5.2: Discrete Neural Network & Training Harness (`paper02/src/models/` & `data/`)
1. **Implement `models/transformer.py`:**
   - Configurable seq2seq Encoder-Decoder Transformer with embedding scaling, sinusoidal positional encodings, and multi-head cross-attention.
   - Forward pass returning prediction logits, cross-entropy loss, and intermediate activation tensors at each layer.
2. **Implement `data/loaders.py`:**
   - Deterministic dataset generators and PyTorch DataLoaders for H-Bar, SCAN (`add_primitive`, `length_split`), COGS, and PCFG-SET.
   - Implement zero-leakage primitive substitution pipeline for generating $\mathcal{L}_{\text{comp}}$ batches on the fly.
3. **Implement `experiments/trainer.py`:**
   - Multi-arm training harness supporting:
     - Baseline ERM ($\lambda = 0$).
     - Fixed-weight compositional loss ($\lambda > 0$).
     - Late-onset intervention schedule ($\lambda = 0$ until step $t_{\text{int}}$, then $\lambda = \lambda_0$).
   - Automatic checkpointing and metric logging every 25 steps.

### Task 5.3: Representation Probing & Order-Parameter Diagnostics (`paper02/src/analysis/`)
1. **Implement `analysis/cka.py`:**
   - Linear and RBF Centered Kernel Alignment (CKA) between hidden representations $X \in \mathbb{R}^{N \times D}$ and $Y \in \mathbb{R}^{N \times D}$:
     $$\text{CKA}(K, L) = \frac{\text{HSIC}(K, L)}{\sqrt{\text{HSIC}(K, K) \text{HSIC}(L, L)}}$$
   - Memory-efficient batch formulation for tracking CKA across 2000 evaluation steps.
2. **Implement `analysis/whitened_gca.py`:**
   - Subspace-projected GCA that projects out the shared input embedding subspace:
     $$g_A^{\text{proj}}(t) = \text{CosSim}\left( (I - P_{\text{emb}}) \nabla_\theta \mathcal{L}_{\text{comp}}, \; (I - P_{\text{emb}}) \nabla_\theta \mathcal{L}_{\text{train}} \right)$$
   - Mathematically verified to eliminate the step-0 $0.95$ initialization artifact.
3. **Implement `analysis/hessian_lanczos.py`:**
   - PyHessian Lanczos iteration computing top 5 eigenvalues $\lambda_1 \dots \lambda_5$ and spectral density of the loss Hessian with respect to model parameters.

### Task 5.4: Comprehensive Unit Test Suite (`paper02/tests/`)
Implement unit tests achieving 100% test coverage across custom kernels:
1. `tests/test_two_subspace_ode.py`:
   - Test 1: Verify fixed points $E_S$ and $E_C$ match analytical coordinates.
   - Test 2: Verify $\mu_\perp < 0$ for $\lambda < \lambda_{\text{crit}}$ and $\mu_\perp > 0$ for $\lambda > \lambda_{\text{crit}}$.
   - Test 3: Verify Diffrax solver convergence against analytical exponential solutions.
2. `tests/test_cka.py`:
   - Test 1: Verify $\text{CKA}(X, X) = 1.0$.
   - Test 2: Verify $\text{CKA}(X, Y) = 0.0$ for orthogonal random matrices.
   - Test 3: Verify rotational invariance $\text{CKA}(X, XR) = \text{CKA}(X, X)$ for orthogonal matrix $R$.
3. `tests/test_whitened_gca.py`:
   - Test 1: Verify raw GCA exhibits high cosine similarity at random initialization.
   - Test 2: Verify whitened/projected GCA yields $\approx 0.0$ at random initialization.
   - Test 3: Verify whitened GCA correctly detects collinear gradients in intermediate transformer layers.
4. `tests/test_data_leakage.py`:
   - Test 1: Formally assert zero intersection between training and OOD vocabulary tuples.

---

## 3. Human Gates
- None (fully autonomous), unless unresolvable architectural blockers occur.

---

## 4. Machine-Checkable Exit Criteria
- [ ] All scripts in `paper02/src/` pass `ruff check` with 0 lint errors.
- [ ] `pytest paper02/tests/` passes all unit tests ($\ge 12$ tests across 4 test suites).
- [ ] CC.2.2 verified ($\ge 3$ unit tests per custom kernel).
- [ ] Automated smoke sweep executes 2 full training epochs on CPU/GPU without error.

---

## 5. Deliverables & Artifacts
- Source code: `paper02/src/continuous/`, `paper02/src/models/`, `paper02/src/data/`, `paper02/src/analysis/`
- Unit tests: `paper02/tests/`
- Test log: `paper02/tests/pytest_report.txt`
