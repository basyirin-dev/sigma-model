# Σ-Model — Agent Instructions

## Project

Σ-Model: a dynamical-systems framework for compositional generalisation failure. Core idea: standard gradient-based training drives agents into a stable low-schema-coherence equilibrium (the **σ-trap**) — depth accumulates while schema coherence is suppressed, producing high in-distribution / low out-of-distribution performance.

- **Stack**: Python 3.13.9 (via `hbar_env/` — symlinked from `/usr/bin/python3`), PyTorch 2.12.0, NumPy, SciPy, pandas, matplotlib/seaborn.
- **Defining paper**: the active deliverable lives under `paper/` — *Critical Compositional Pressure & Two-Subspace Law*. This is the capstone manuscript; it absorbed the σ-Trap results. It is **no longer "Paper 02"**, but THE defining paper.
- **Paper 01 (superseded)**: the former σ-Trap manuscript was **rejected by TMLR, absorbed into the defining paper, and is archived** under `archive/paper01/`. Do not edit it or revive it as a peer deliverable.
- **Legacy package**: `sigma_align` under `code/` (built with setuptools; CLI `sigma-evaluate` → `sigma_align.monitoring.evaluation:main`) is the **legacy** implementation and is slated for retirement. The defining paper's canonical source is `paper/src/`.
- **Historical**: thesis monograph and AGI-safety pipeline archived (reversible) under `archive/thesis/` and `archive/Σ-Align/`. Do not revive without a new decision.

## Commands

Always activate the venv first:
```bash
source hbar_env/bin/activate
```

| Task | Command |
|------|---------|
| Lint check | `ruff check code/ tests/ paper/src/ paper/tests/` (or `make lint`) |
| Run tests | `PYTHONPATH=.:code:paper/src:$PYTHONPATH pytest tests/ paper/tests/` (or `make test`) |
| Build defining paper PDF | `make paper` (from root) |
| Build defining paper PDF (in-dir) | `make pdf` (from `paper/`) |
| Build submission packages | `make submission` (from root) |
| Package arXiv bundle | `make arxiv` (from root) |
| Run evaluation (legacy) | `PYTHONPATH=code:$PYTHONPATH python -m sigma_align.monitoring.evaluation` |
| CLI alias | `sigma-evaluate` (installed via `pip install -e .`) |
| Git commit format | `[Tag][Scope][Δ] Description` — Tag=I(Impl)/B(Bugfix)/R(Refactor)/V(Validation), Scope=L(LaTeX)/C(Code)/W(Workflow) |

## Architecture

| Path | Role |
|------|------|
| `paper/` | Defining paper: manuscript (`writing/manuscript.tex`), source code (`paper/src/`), tests (`paper/tests/`), figures, data, planning/ledger/preregistration, submission packages (`submission_*`). |
| `paper/src/` | Canonical code for the defining paper: `analysis/`, `continuous/` (Two-Subspace ODE + solver), `models/`, `data/`, `experiments/`, `config/`. |
| `code/sigma_align/` | **Legacy** package (config/ode/monitoring/utils + `sigma-evaluate` CLI). Slated for retirement; superseded by `paper/src/`. |
| `code/experiments/` | Legacy experiment harnesses and configs (thin orchestration only). |
| `tests/` | Root infrastructure/unit tests (`tests/unit/`, `tests/integration/`, `tests/reproducibility/`). |
| `paper01/` → `archive/paper01/` | Superseded σ-Trap paper (rejected by TMLR, absorbed into the defining paper). Read-only. |
| `planning/` | Root research-planning framework (RPF) phases, roadmap, ledger, standards. |
| `decisions/` | ADRs and human-gate decision records. |
| `docs/adrs/` | Architecture Decision Records (monorepo, pandoc, claim-tracking, config-driven, defining-paper). |
| `docs/research_programme/` | Master research programme & theoretical foundations. |
| `docs/career_and_academic_roadmap/` | Academic roadmap & 30 lifelong goals. |
| `archive/` | Read-only historical artifacts (thesis, old code, datasets, results, superseded papers). Do not modify. |
| `hbar_env/` | Python virtual environment. Do not modify. |

## Conventions

- **Configs**: Never hardcode params. Use YAML configs and the paper's config loader (`paper/src/config/`). See `docs/adrs/0004-config-driven-experiments.md`.
- **Code placement**: All reusable logic for the defining paper lives in `paper/src/`. `code/` is legacy pending retirement. Notebooks are thin orchestration layers only.
- **Paper edits**: Edit `paper/writing/manuscript.tex` directly, then `make pdf` (or `make -C paper pdf`). Manuscript claim discipline: the model is *phenomenological* (posited ODEs, not derived from SGD); separate *model theorem / empirical observation / interpretation*. As the defining paper, it may present the full programme (including the absorbed σ-Trap results) — standard-scoping constraints that applied to the narrow paper now apply to the defining paper instead.
- **Type hints**: Use modern Python syntax (`dict[str, Any]`, `| None`, `float`). Ruff enforces `E,F,I,N,W` at line-length 100, target `py314`.
- **Reproducibility**: `torch.manual_seed(run_id * 42 + 7)`, `torch.backends.cudnn.deterministic = True`, `torch.backends.cudnn.benchmark = False`.
- **AMP (PyTorch)**: Use canonical `torch.amp.autocast_mode.autocast` and `torch.amp.grad_scaler.GradScaler` (the `torch.amp` re-export triggers pyright false warnings).
- **Git commits**: Format `[Tag][Scope][Δ] Description`. Tag: I(Impl)/B(Bugfix)/R(Refactor)/V(Validation). Scope: L(LaTeX)/C(Code)/W(Workflow).

## Guardrails

- Activate `hbar_env` before any Python work.
- Never modify files in `hbar_env/`, `archive/`, or `.git/`.
- Never edit the archived superseded Paper 01 (`archive/paper01/`) or re-serve it as a peer deliverable.
- Never commit large artifacts — check `.gitignore` first (datasets, raw results, build PDFs, submission bundles are excluded).
- The root `tests/` plus `paper/tests/` make up the automated suite; run `make test` before declaring a change done. Update `pyproject.toml` testpaths if adding new aggregates.

## Opencode Config

- `opencode.json` at root: LSPs for pyright, ruff, yaml, taplo, marksman, bash.
- MCP servers: `sequential_thinking` (local), `context7` (remote), `gh_grep` (remote), `fetch` (local), `academic_research` (local), `zotero` (local), `arxiv` (local).
- 4 plugins: direnv, DCP (compress), context-analysis, notifier.
- Startup crash? Run `python3 -m json.tool opencode.json`, then check `~/.config/opencode/opencode.jsonc`.

## Notes

*(Quick-add space — use `remember` for durable facts.)*
