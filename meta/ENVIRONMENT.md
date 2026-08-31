# Research Environment Specification (RPF v2.0)

## Host System
- **Operating System:** CachyOS (Arch Linux derivative with optimized x86-64-v3/v4 packages & BORE/EEVDF kernel)
- **Primary Interactive Shell:** `fish` (/usr/bin/fish)
- **Package Manager:** `paru` (AUR helper / Pacman wrapper)
- **System Architecture:** Linux x86_64

## Runtime & Toolchain

### Shell Configuration & Execution Guidelines
When issuing system shell commands:
```fish
# Package installation via paru (non-interactive)
paru -S --noconfirm <package-name>

# Environment activation
source hbar_env/bin/activate.fish   # in fish
# or
source hbar_env/bin/activate        # in bash/zsh subshells
```

### Core Programming Languages & Frameworks
| Component | Pinned Version / Constraint | Provider / Source |
|---|---|---|
| **Python** | 3.11.x / 3.13.x | Host system & Docker container |
| **PyTorch** | 2.12.0+ | Wheels / CUDA 12.x / CPU |
| **JAX / Jaxlib** | 0.4.28+ | CUDA-enabled / CPU wheels |
| **Diffrax** | 0.5.1+ | JAX-based ODE/SDE numerical solver suite |
| **Julia** | 1.10.x LTS | DifferentialEquations.jl ecosystem |
| **DifferentialEquations.jl** | 7.12.0+ | Julia package registry |
| **PyHessian** | 0.1.0+ | Loss surface curvature & Lanczos spectrum |
| **Geomstats** | 2.7.0+ | Differential geometry on manifolds |
| **Giotto-tda** | 0.6.0+ | Topological data analysis & persistent homology |
| **TransformerLens** | 1.14.0+ | Mechanistic interpretability & circuit probing |
| **Quarto** | 1.4.x+ | CLI document rendering pipeline |

### Tooling & Agent Harness
- **Pi Harness:** `@earendil-works/pi-coding-agent` v0.51.x
- **Linter & Formatter:** Ruff (`ruff check`, `ruff format`) with py314 / py311 compatibility
- **Type Checker:** Pyright / Pyright-LSP
- **Workflow Orchestration:** Snakemake (`Snakefile`) / GNU Make (`Makefile`)

### Docker Clean-Room Target
For Phase P10 Clean-Room Verification, all simulations and analysis scripts run inside a pinned Docker container built from the root `Dockerfile`.
