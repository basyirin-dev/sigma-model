# Phase 00 — Repository, Infrastructure & Antigravity Tooling Setup

**Phase ID:** P00  
**Phase Title:** Repository Bootstrap, Environment Pinning, Toolchain & Antigravity Tooling Setup  
**Status:** Complete (Human-Gate Signed Off)  
**Duration:** 1–2 Days  
**Dependencies:** None  
**Executor:** Agent (90%) / Human-Gate (10%)  
**Deliverables:** `paper02/meta/*`, `paper02/planning/roadmap.md`, `paper02/decisions/ADR-template.md`, `paper02/Makefile`, `paper02/src/__init__.py`

**RPF v2.0:** Git tag `p00-done` · RACI: Agent **R** / PI **A** (repo visibility, Kaggle credentials) · Abort: cannot init repo → escalate · Acceptance: repo scaffold + `ADR-template.md` with `affects-ledger-rows`/`affects-phases` fields · **Closed under v1.0.0, migrated 2026-08-23.**

---

## 1. Purpose & Scope
Establish the canonical project skeleton for Paper 02 under the Research Planning Framework (RPF v1.0.0). This includes configuring the local and cloud virtual environments, establishing the Google Antigravity developer environment (MCP servers, Plugins, LSPs), setting up git hooks, scaffolding all directories, and writing foundational meta-documentation.

---

## 2. Exhaustive Tasks & Subtasks

### Task 0.1: Antigravity IDE, MCP Servers, Plugins & LSP Configuration
1. **Model Context Protocol (MCP) Server Setup:**
   - Configure local and remote MCP servers in `opencode.json` / Antigravity config:
     - `codebase_memory` (lazy): Local knowledge graph indexing, AST symbol queries, and architecture mapping.
     - `sequential_thinking` (lazy): Complex multi-step theoretical deliberation and proof verification.
     - `fetch` & `read_url_content`: HTTP/web document retrieval for scientific preprints and technical docs.
     - `academic_research` / `arxiv` / `zotero` (local/remote): Automatic paper metadata extraction and BibTeX synchronization.
     - `context7` & `gh_grep`: Semantic codebase search and remote repository referencing.
2. **Antigravity Plugins Configuration:**
   - Enable `direnv` plugin for automatic environment variable management.
   - Enable `dcp` (Dynamic Context Pruning) plugin to manage large multi-seed logs without context overflow.
   - Enable `context-analysis` plugin for active token density tracking.
   - Enable `notifier` plugin for background task and simulation completion alerts.
3. **Language Server Protocol (LSP) Verification:**
   - Configure and verify LSPs in root `opencode.json`:
     - **Python:** `pyright` (type checking at `strict` level) and `ruff` (formatting and linting with line length 100).
     - **LaTeX:** `texlab` (autocompletion, forward/backward search, syntax diagnostics).
     - **Markdown / Data:** `marksman` (markdown link validation) and `taplo` (TOML formatting).
     - **Shell:** `bash-language-server` for execution scripts.
   - Validate LSP startup via `python3 -m json.tool opencode.json`.

### Task 0.2: Python & Numerical Environment Pinning
1. **Virtual Environment Verification:**
   - Activate pinned environment: `source hbar_env/bin/activate`.
   - Verify Python version: Python 3.13.9 / 3.14.x.
2. **Library Installation & Compatibility Check:**
   - Verify PyTorch 2.12.0+ with CUDA 12.x acceleration.
   - Install and pin continuous-time dynamical systems libraries:
     - `jax` and `jaxlib` (with GPU support).
     - `diffrax` (differentiable ODE/SDE solvers for continuous gradient flow).
     - `scipy` (bifurcation, non-linear curve fitting, and statistical testing).
     - `geomstats` (Riemannian geometry and representation manifold metrics).
     - `torch-geometric` / `curvlinops` / `pyhessian` (Hessian spectral density and top eigenvalue tracking).
3. **Generate Environment Spec:**
   - Emit `paper02/meta/ENVIRONMENT.md` recording exact package hashes, CUDA drivers, and CPU/GPU specifications.

### Task 0.3: Directory Scaffolding & Git Governance
1. **Directory Tree Construction:**
   - Scaffold the canonical RPF tree:
     ```
     paper02/
     ├── planning/
     │   └── phases/
     ├── decisions/
     ├── src/
     │   ├── continuous/
     │   ├── models/
     │   ├── data/
     │   └── analysis/
     ├── experiments/
     │   ├── configs/
     │   └── literature/
     ├── notebooks/
     ├── data/
     │   ├── raw/
     │   └── processed/
     ├── writing/
     │   ├── figures/
     │   └── supplementary/
     └── meta/
     ```
2. **Git Commit Linter & Pre-Commit Hooks:**
   - Enforce conventional commit format in `meta/AGENT_INSTRUCTIONS.md`:
     `[Tag][Scope][Δ] Description` (e.g., `[P00][Setup][INIT] Scaffold Paper 02 directory tree`).
   - Configure `.gitignore` to prevent raw tensors, large binary pickles, and LaTeX intermediate build files from polluting version control.

### Task 0.4: Meta-Documentation & ADR Scaffolding
1. **Scaffold Core Meta Documents:**
   - Write `paper02/meta/README.md` (project synopsis and quickstart commands).
   - Write `paper02/meta/AGENT_INSTRUCTIONS.md` (detailed operating manual, guardrails, and the 14 Human-Gate rules; $\ge 50$ lines).
2. **Scaffold Architecture Decision Records (ADRs):**
   - Create `paper02/decisions/ADR-template.md`.
   - Initialize `paper02/decisions/ADR-001_two_subspace_formulation.md`.

### Task 0.5: Build System & Smoke Testing
1. **Makefile Setup:**
   - Create `paper02/Makefile` supporting targets `pdf`, `clean`, `test`, `figures`, and `arxiv`.
   - Update root `Makefile` to include `paper02` target forwarding to `paper02/Makefile`.
2. **Automated Smoke Test:**
   - Create `paper02/tests/test_env_smoke.py` verifying that PyTorch, JAX, Diffrax, SciPy, and CKA routines import and execute a dummy tensor operation with exit code 0.

---

## 3. Human Gates
- `[HUMAN-GATE]` User reviews Antigravity LSP/MCP setup and confirms repository visibility and target compute environments (Local GPU + Kaggle).

---

## 4. Machine-Checkable Exit Criteria
- [ ] `paper02/planning/roadmap.md` exists with populated header, deliverable matrix, and non-negotiables.
- [ ] `paper02/planning/standards.md` exists with frozen CC.N.M rules.
- [ ] `paper02/planning/ledger.md` exists with initial claims ledger.
- [ ] `paper02/meta/AGENT_INSTRUCTIONS.md` exists and is $\ge 50$ lines.
- [ ] `paper02/meta/ENVIRONMENT.md` documents all pinned dependencies.
- [ ] `python -c "import torch, jax, diffrax, scipy, geomstats; print('Imports PASS')"` exits with code 0.
- [ ] `pytest paper02/tests/test_env_smoke.py` exits with code 0.
- [ ] `[HUMAN-GATE]` User confirms environment readiness.

---

## 5. Deliverables & Artifacts
- Scaffolding: `paper02/planning/`, `paper02/decisions/`, `paper02/src/`, `paper02/meta/`, `paper02/writing/`
- Documentation: `paper02/meta/README.md`, `paper02/meta/AGENT_INSTRUCTIONS.md`, `paper02/meta/ENVIRONMENT.md`, `paper02/decisions/ADR-template.md`
- Build files: `paper02/Makefile`, `paper02/tests/test_env_smoke.py`
