# Σ-Align — Agent Instructions

## Project

Σ-Align: Schema Coherence Framework for AI Alignment and AGI Safety. Core thesis: *compositional generalization failure and AI alignment failure are the same phenomenon (the σ-trap).*

- **Stack**: Python 3.13.9 (via `hbar_env/` — symlinked from `/usr/bin/python3`), PyTorch 2.12.0, NumPy, SciPy, pandas, matplotlib/seaborn.
- **Package**: `sigma_align` under `code/` — built with setuptools. CLI entry: `sigma-evaluate` → `sigma_align.monitoring.evaluation:main`.
- **Thesis**: Monograph (chapter-based) — 10 chapters under `thesis/chapters/`, planning docs in `thesis/`, venue manuscripts in `thesis/publications/`.
- **Paper under review**: Paper 06 (Σ-Model) at JAIR → pivoting to TMLR — `paper/manuscript.tex`.

## Commands

Always activate the venv first:
```bash
source hbar_env/bin/activate
```

| Task | Command |
|------|---------|
| Lint check | `ruff check code/sigma_align/` |
| Run tests | `PYTHONPATH=code:$PYTHONPATH pytest` (testpaths empty; no project tests yet) |
| Build all papers | `make all` (from root) |
| Build monograph | `make monograph` (from root; delegates to `thesis/Makefile`) |
| Build Paper 01 | `make paper01` |
| Build Paper 02 | `make paper02` |
| Build Paper 06 (Σ-Model) | `make paper06` |
| Build paper PDF | `make pdf` (from `paper/`) |
| Run evaluation | `PYTHONPATH=code:$PYTHONPATH python -m sigma_align.monitoring.evaluation` |
| CLI alias | `sigma-evaluate` (installed via `pip install -e .`) |
| Git commit format | `[Tag][Scope][Δ] Description` — Tag=I(Impl)/B(Bugfix)/R(Refactor)/V(Validation), Scope=T(Thesis)/L(LaTeX)/C(Code)/W(Workflow) |

## Architecture

| Path | Role |
|------|------|
| `code/sigma_align/config/` | YAML config loader (`load_config()`, `merge_configs()`). No hardcoded params. |
| `code/sigma_align/ode/` | Σ-Model ODE: `equations.py` (RHS, sigma_critical, bifurcation), `solver.py` (SigmaODESolver — phenomenological integrator). |
| `code/sigma_align/monitoring/` | Evaluation pipeline, dataset builders, report generation, social-media scraping. |
| `code/sigma_align/utils/` | Data helpers, metrics, vocabulary utilities. |
| `paper/` | Σ-Model manuscript (Paper 06, JAIR → TMLR, empirical #1). LaTeX + latexmk build. |
| `thesis/` | Monograph. `monograph.tex` (main document), `narrative.md` (arc), `phase-roadmap.md` (status), `cross-cutting.md` (standards CC.1–8). |
| `thesis/chapters/XX-name/` | Each chapter folder: `manuscript/` (`.tex`), `figures/`, `phases/` (roadmap docs), `README.md`. |
| `thesis/publications/` | Venue-formatted manuscripts of the source papers (01, 02; 06 symlinked to `paper/`). |
| `thesis/front-matter/`, `thesis/back-matter/` | Title/abstract/acknowledgements/list-of-publications; glossary/notation/appendices. |
| `Σ-Align/` | Pivot decision documentation: MCDAs, audit trails, errata, paper evaluation, methodology checklists. |
| `docs/adrs/` | Architecture Decision Records (4 so far: monorepo, pandoc, claim-tracking, config-driven experiments). |
| `archive/` | Read-only historical protein-domain artifacts. Do not modify. |
| `hbar_env/` | Python virtual environment. Do not modify. |

## Conventions

- **Configs**: Never hardcode params. Use YAML configs and `sigma_align.config.load_config()`. See `docs/adrs/0004-config-driven-experiments.md`.
- **Code placement**: All reusable logic in `code/sigma_align/`. Notebooks are thin orchestration layers only.
- **Paper edits**: Edit `paper/manuscript.tex` directly, then `make pdf`. Publication manuscripts live in `thesis/publications/XX-name/`. Chapter edits: edit `thesis/chapters/XX-name/manuscript/chapterN.tex`, then `make monograph`.
- **Type hints**: Use modern Python syntax (`dict[str, Any]`, `| None`, `float`). Ruff enforces `E,F,I,N,W` at line-length 100, target `py314`.
- **Reproducibility**: `torch.manual_seed(run_id * 42 + 7)`, `torch.backends.cudnn.deterministic = True`, `torch.backends.cudnn.benchmark = False`.
- **AMP (PyTorch)**: Use canonical `torch.amp.autocast_mode.autocast` and `torch.amp.grad_scaler.GradScaler` (the `torch.amp` re-export triggers pyright false warnings).
- **Git commits**: Format `[Tag][Scope][Δ] Description`. Tag: I(Impl)/B(Bugfix)/R(Refactor)/V(Validation). Scope: T(Thesis)/L(LaTeX)/C(Code)/W(Workflow).

## Guardrails

- Activate `hbar_env` before any Python work.
- Never modify files in `hbar_env/`, `archive/`, or `.git/`.
- Never commit large artifacts — check `.gitignore` first.
- No project-level tests exist yet (testpaths empty in `pyproject.toml`). Must be rewritten when adding.

## Opencode Config

- `opencode.json` at root: LSPs for pyright, ruff, yaml, taplo, marksman, bash.
- 6 MCP servers: `sequential_thinking` (local), `context7` (remote), `gh_grep` (remote), `fetch` (local), `academic_research` (local), `zotero` (local), `arxiv` (local).
- 4 plugins: direnv, DCP (compress), context-analysis, notifier.
- Startup crash? Run `python3 -m json.tool opencode.json`, then check `~/.config/opencode/opencode.jsonc`.

## Notes

*(Quick-add space — use `remember` for durable facts.)*
