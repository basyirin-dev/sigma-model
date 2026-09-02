# Research Environment Specification (RPF v2.0)

## Host System
- **Operating System:** CachyOS (Arch Linux derivative with optimized x86-64-v3/v4 packages & BORE/EEVDF kernel)
- **Kernel:** 7.2.0-1-cachyos (PREEMPT_DYNAMIC) — doctor-verified 2026-08-27
- **Desktop Session:** KDE Plasma 6 (Wayland)
- **Primary Interactive Shell:** `fish` (/usr/bin/fish)
- **Package Manager:** `paru` (AUR helper / Pacman wrapper) — requires interactive sudo; non-interactive agent installs blocked unless an askpass helper is configured
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
- **Pi Harness:** `@earendil-works/pi-coding-agent` v0.84.3 (doctor-verified; provider: antigravity via `pi-antigravity` extension v0.4.1; active model: gemini-3.7-flash; reasoning: high)
- **Linter & Formatter:** Ruff (`ruff check`, `ruff format`) with py314 / py311 compatibility
- **Type Checker:** Pyright / Pyright-LSP
- **Workflow Orchestration:** Snakemake (`Snakefile`) / GNU Make (`Makefile`)

### Docker Clean-Room Target
For Phase P10 Clean-Room Verification, all simulations and analysis scripts run inside a pinned Docker container built from the root `Dockerfile`.

## Doctor-Verified System Snapshot (2026-08-27)

Actual versions verified by the RPF `doctor` diagnostic (source of truth for P10 clean-room pinning):

| Component | Verified Version | Notes |
|---|---|---|
| Host OS | CachyOS x86_64, kernel 7.2.0-1-cachyos | KDE Plasma 6 (Wayland) |
| Python (system) | 3.14.7 | Project venv `hbar_env/` pins 3.13.9 |
| Node.js | v24.14.1 (fnm 1.39.0) | |
| npm | 11.11.0 | |
| Bun | 1.4.0 | |
| Rust / Cargo | 1.96.0 | |
| Go | 1.27.0 | |
| Git | 2.55.0 | |
| Docker | 29.7.2 | |
| Ollama | 0.20.0 | |
| Hardware | ThinkPad laptop; 15 GiB RAM; 473 GB root disk (~40% free) | CPU temp ~67–69 °C, fan ~3185 RPM under load |

### Health-Check Findings & Resolutions
- **Systemd:** no failed units as of 2026-08-27.
- **Pi CLI crash — "No API provider registered for api: antigravity-api" (RESOLVED 2026-08-27):**
  Root causes were two-fold:
  1. `pi-antigravity@0.4.1` value-imports `@earendil-works/pi-ai` but declares only `undici` as a dependency, so the extension failed to load from `~/.pi/agent/npm/node_modules/` (MODULE_NOT_FOUND). Fixed with a symlink to the exact bundled version:
     `~/.pi/agent/npm/node_modules/@earendil-works/pi-ai` → `~/.npm-global/lib/node_modules/@earendil-works/pi-coding-agent/node_modules/@earendil-works/pi-ai`
  2. Tool-calling turns routed through pi's compat api-registry (`@earendil-works/pi-ai/compat`), which only knew built-in providers → crash on every tool turn. Fixed by a local patch to `~/.pi/agent/npm/node_modules/pi-antigravity/src/index.ts` that additionally calls `registerApiProvider(...)` with `stream`/`streamSimple` (uses `createAssistantMessageEventStream`).
  **Caveats:** the index.ts patch is local to `~/.pi/agent/npm/node_modules` and is lost by `pi update pi-antigravity` (re-apply if tool turns crash again). Worth reporting upstream (Rahularya01/pi-antigravity; earendil-works/pi).
- **`pi doctor` custom-tools warning (RESOLVED 2026-08-27):** Pi v0.84 merged custom tools into extensions. `.pi/tools/*.py` moved to `scripts/` (tracked, CI-usable); LLM-facing tools are now registered in `.pi/extensions/{rpf-governance,human-gate,manifest-enforcer}.ts`. Pre-commit hook and CI workflow updated accordingly.
- **`nvim` PATH mismatch (OPEN):** `EDITOR`, `VISUAL`, `MANPAGER` in `~/.config/fish/config.fish` point to `nvim`, but nvim is not on `$PATH`. Fix requires interactive `paru -S --noconfirm neovim` (sudo prompt) or repointing the env vars to `micro`/`vim`/`nano`.
- **MLflow tracing (informational):** `@yofriadi/pi-mlflow` logs "tracing disabled — tracking server unreachable" unless an MLflow tracking server is running; expected when MLflow is absent.
