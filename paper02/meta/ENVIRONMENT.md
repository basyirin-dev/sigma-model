# Environment & Dependency Pinning Spec

**Project:** Paper 02 (*Critical Compositional Pressure & The Two-Subspace Law*)  
**Governance:** Research Planning Framework (RPF v2.0.0)  
**Virtual Environment:** `hbar_env/` (`source hbar_env/bin/activate`)  

---

## 1. Pinned Software Runtime & Packages

### Core Runtime
| Component | Local Host Version | Target Cloud / Cluster Version | Role in Paper 02 |
|---|---|---|---|
| **Python** | `3.14.7` | `3.13.9` / `3.14.x` | Core execution runtime |
| **PyTorch** | `2.12.0+cpu` | `2.12.0+cu124` | Discrete transformer training, multi-seed sweeps |
| **JAX** | `0.9.2` | `0.9.2` (`jax[cuda12]`) | High-performance differentiable gradient flow |
| **SciPy** | `1.17.1` | `1.17.1` | ODE numerical integration (`solve_ivp`), bifurcation roots |
| **NumPy** | `2.5.2` | `2.5.2` | Numerical tensor and linear algebra operations |
| **SymPy** | `1.14.0` | `1.14.0` | Analytical Jacobians, fixed-point eigen-analysis |
| **Optax** | `0.2.8` | `0.2.8` | First-order gradient optimization for JAX models |
| **Pandas** | `2.3.3` | `2.3.3` | Benchmark metric serialization & tidy dataframe export |
| **Matplotlib** | `3.10.8` | `3.10.8` | Vector publication figure rendering (PDF/SVG) |
| **NetworkX** | `3.6.1` | `3.6.1` | Dependency and graph composition analysis |
| **Pytest** | `9.0.2` | `9.0.2` | Test suite execution & regression assertions |
| **Ruff** | `0.15.9` | `0.15.9` | Automated linting (`E,F,I,N,W`) & formatting |

### Specialized Extended Packages (Cloud / GPU Cluster)
| Package | Pinned Version Range | Role in Paper 02 |
|---|---|---|
| **Diffrax** | `>=0.6.0` | Continuous-time differentiable ODE/SDE solvers in JAX |
| **Geomstats** | `>=2.7.0` | Manifold geometry & representation space Riemannian metrics |
| **Curvlinops** | `>=0.3.0` | Hessian spectrum, GGN operators, top eigenvalue tracking |
| **PyHessian** | `>=0.1.0` | Edge-of-Stability curvature and spectral density tracing |
| **Torch-Geometric** | `>=2.5.0` | Structural and relational graph benchmark representations |
| **Seaborn** | `>=0.13.0` | Distribution plots & regression confidence bands |


---

## 2. Hardware Environments & Execution Profiles

### Tier 1: Local Development Workstation (Prototyping & Verification)
- **Architecture:** `x86_64`
- **CPU:** Intel(R) Core(TM) i5-8250U CPU @ 1.60GHz (4 physical cores / 8 vCPUs)
- **Host Memory:** 15 GiB Physical RAM, 7.7 GiB Swap
- **Operating System:** Linux `basy-cachyos-x8664 7.2.0-1-cachyos` (x86_64)
- **Acceleration:** CPU (Optimized via NumPy OpenBLAS / JAX CPU runtime)
- **Primary Use:** Analytical ODE verification, unit tests, sanity checks, manuscript drafting, and compilation.

### Tier 2: Cloud / Remote GPU Compute (Heavy Training & Multi-Seed Sweeps)
- **Target Platforms:** Kaggle Notebooks / Cloud Compute (GCP Vertex / Lambda Labs)
- **Accelerators:** NVIDIA Tesla T4 x2 / P100 / RTX A5000 / TPU v3-8 (CUDA 12.x / cuDNN 9.x)
- **Memory:** 16GB+ VRAM, 32GB+ System RAM
- **Primary Use:** Dense multi-seed sweeps ($n=30$ seeds for Tier 1 primary falsification cells, $n=10$ seeds for Tier 2 exploratory architecture screening; $n=15$ deprecated), Hessian top eigenvalue tracking over training trajectories, continuous gradient-flow ODE simulations.

---

## 3. Reproducibility, Seeding & Precision Standards

1. **Deterministic Seeding Protocol:**
   - PyTorch: `torch.manual_seed(run_id * 42 + 7)`
   - JAX: `jax.random.PRNGKey(run_id * 42 + 7)`
   - NumPy / Python: `np.random.seed(run_id * 42 + 7)`, `random.seed(run_id * 42 + 7)`
   - CUDNN Flags: `torch.backends.cudnn.deterministic = True`, `torch.backends.cudnn.benchmark = False`
2. **Floating-Point Precision:**
   - Continuous ODE / Bifurcation solvers: Standard `float64` (double precision) for numerical stability near bifurcation critical points $\sigma_{\text{crit}}$.
   - Discrete Neural Network Training: Mixed precision `bfloat16` / `float32` using canonical PyTorch AMP (`torch.amp.autocast_mode.autocast`).
3. **Artifact Immutability:**
   - Raw simulation tensors generated during Phase 06 are saved as immutable Parquet/NPZ files in `paper02/data/raw/` with SHA-256 integrity logs.

