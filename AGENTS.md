# Σ-Model — Agent Instructions

## Project

Σ-Model: a dynamical-systems framework for compositional generalisation failure. Core idea: standard gradient-based training drives agents into a stable low-schema-coherence equilibrium (the **σ-trap**) — depth accumulates while schema coherence is suppressed, producing high in-distribution / low out-of-distribution performance.

- **Stack**: Python 3.13.9 (via `hbar_env/` — symlinked from `/usr/bin/python3`), PyTorch 2.12.0, NumPy, SciPy, pandas, matplotlib/seaborn.
- **Package**: `sigma_align` under `code/` — built with setuptools. CLI entry: `sigma-evaluate` → `sigma_align.monitoring.evaluation:main`.
- **Active deliverable**: Paper 06 v2 — narrow σ-Trap manuscript (`paper/manuscript.tex`, TMLR format) + arXiv companion (`paper/companion/`), experiment-gated. Phase plan: `paper/planning/roadmap.md`; standards: `paper/planning/cross-cutting.md`; claim ledger: `paper/planning/claim-ledger.md`.
- **Historical**: thesis monograph and AGI-safety pipeline archived (reversible) under `archive/thesis/` and `archive/Σ-Align/`. Do not revive without a new decision.

## Commands

Always activate the venv first:
```bash
source hbar_env/bin/activate
```

| Task | Command |
|------|---------|
| Lint check | `ruff check code/sigma_align/` |
| Run tests | `PYTHONPATH=code:$PYTHONPATH pytest` (testpaths empty; no project tests yet) |
| Build Paper 06 (σ-Trap) | `make paper06` (from root) |
| Build paper PDF | `make pdf` (from `paper/`) |
| Build arXiv bundle | `make arxiv` (from `paper/`) |
| Run evaluation | `PYTHONPATH=code:$PYTHONPATH python -m sigma_align.monitoring.evaluation` |
| CLI alias | `sigma-evaluate` (installed via `pip install -e .`) |
| Git commit format | `[Tag][Scope][Δ] Description` — Tag=I(Impl)/B(Bugfix)/R(Refactor)/V(Validation), Scope=L(LaTeX)/C(Code)/W(Workflow) |

## Architecture

| Path | Role |
|------|------|
| `code/sigma_align/config/` | YAML config loader (`load_config()`, `merge_configs()`). No hardcoded params. |
| `code/sigma_align/ode/` | Σ-Model ODE: `equations.py` (RHS, sigma_critical, bifurcation), `solver.py` (SigmaODESolver — phenomenological integrator). |
| `code/sigma_align/monitoring/` | Evaluation pipeline, dataset builders, report generation, social-media scraping. |
| `code/sigma_align/utils/` | Data helpers, metrics, vocabulary utilities. |
| `code/experiments/` | Experiment configs (YAML) and run harnesses (thin orchestration only). |
| `paper/` | σ-Trap manuscript (`manuscript.tex`, TMLR), figures, bibliography, companion report (`paper/companion/`), planning docs (`paper/planning/`). |
| `docs/adrs/` | Architecture Decision Records (4 so far: monorepo, pandoc, claim-tracking, config-driven experiments). |
| `archive/` | Read-only historical artifacts (thesis, decision docs, old code, datasets, results). Do not modify. |
| `hbar_env/` | Python virtual environment. Do not modify. |

## Conventions

- **Configs**: Never hardcode params. Use YAML configs and `sigma_align.config.load_config()`. See `docs/adrs/0004-config-driven-experiments.md`.
- **Code placement**: All reusable logic in `code/sigma_align/`. Notebooks are thin orchestration layers only.
- **Paper edits**: Edit `paper/manuscript.tex` directly, then `make pdf`. Manuscript claim discipline: the model is *phenomenological* (posited ODEs, not derived from SGD); separate *model theorem / empirical observation / interpretation*; no grand-theory or "origin" claims in the narrow paper (see `paper/planning/cross-cutting.md` CC.3).
- **Type hints**: Use modern Python syntax (`dict[str, Any]`, `| None`, `float`). Ruff enforces `E,F,I,N,W` at line-length 100, target `py314`.
- **Reproducibility**: `torch.manual_seed(run_id * 42 + 7)`, `torch.backends.cudnn.deterministic = True`, `torch.backends.cudnn.benchmark = False`.
- **AMP (PyTorch)**: Use canonical `torch.amp.autocast_mode.autocast` and `torch.amp.grad_scaler.GradScaler` (the `torch.amp` re-export triggers pyright false warnings).
- **Git commits**: Format `[Tag][Scope][Δ] Description`. Tag: I(Impl)/B(Bugfix)/R(Refactor)/V(Validation). Scope: L(LaTeX)/C(Code)/W(Workflow).

## Guardrails

- Activate `hbar_env` before any Python work.
- Never modify files in `hbar_env/`, `archive/`, or `.git/`.
- Never commit large artifacts — check `.gitignore` first (datasets, raw results, build PDFs are excluded).
- No project-level tests exist yet (testpaths empty in `pyproject.toml`). Must be rewritten when adding.

## Opencode Config

- `opencode.json` at root: LSPs for pyright, ruff, yaml, taplo, marksman, bash.
- MCP servers: `sequential_thinking` (local), `context7` (remote), `gh_grep` (remote), `fetch` (local), `academic_research` (local), `zotero` (local), `arxiv` (local).
- 4 plugins: direnv, DCP (compress), context-analysis, notifier.
- Startup crash? Run `python3 -m json.tool opencode.json`, then check `~/.config/opencode/opencode.jsonc`.

## Notes

*(Quick-add space — use `remember` for durable facts.)*
