# Σ-Model V3.0+ — Issue Compilation

**Date:** 2026-06-06
**Source:** Full daily workflow execution, hardware audit, and web research.
**Purpose:** Master registry of all known issues, to be resolved before paper submission.

---

## 1. Infrastructure Issues

### I-01 — Notebook hardcodes `/kaggle/working` path (HIGH)

| Field | Value |
|-------|-------|
| **Files** | `experiments/sigma-experiment.ipynb` Cell 0, `experiments/sigma-v3-cognitive-evaluation-benchmark-suite.ipynb` Cell 0 |
| **Symptom** | `PermissionError: [Errno 13] Permission denied: '/kaggle'` on any non-Kaggle machine |
| **Root Cause** | `BASE_DIR = '/kaggle/working'` hardcoded. No fallback for local execution. |
| **Impact** | Blocks all local testing of notebooks. Forces Kaggle-only execution for even trivial changes. |
| **Fix** | Add Kaggle-detection: `BASE_DIR = '/kaggle/working' if os.path.isdir('/kaggle') else './output'` |

### I-02 — SCANDataset defined inline in notebook (MEDIUM)

| Field | Value |
|-------|-------|
| **File** | `experiments/sigma-experiment.ipynb` Cell 1 |
| **Symptom** | `AttributeError: module '__main__' has no attribute 'SCANDataset'` when `DataLoader(num_workers>0)` attempts to fork |
| **Root Cause** | `SCANDataset(Dataset)` class defined within notebook cell. Python's multiprocessing forkserver can't pickle a class defined in `__main__`. |
| **Impact** | Blocks `num_workers>0` in DataLoader on any system using forkserver (Linux Python ≥3.14). |
| **Fix** | Move full SCANDataset class into `code/sigma/utils/data.py` (stub already exists) and import it. |

### I-03 — DataLoader `num_workers` hardcoded to 2 (LOW)

| Field | Value |
|-------|-------|
| **File** | `experiments/sigma-experiment.ipynb` — DataLoader instantiation |
| **Symptom** | Suboptimal resource usage on CPU (2 workers fight over 4 cores) and no workers on GPU is wasteful |
| **Root Cause** | `num_workers=2` hardcoded without environment awareness |
| **Impact** | Low — training still works, just suboptimal |
| **Fix** | Dynamic: `num_workers = 0 if not torch.cuda.is_available() else min(2, os.cpu_count() or 1)` |

### I-04 — Missing seaborn dependency (FIXED)

| Field | Value |
|-------|-------|
| **Files** | `experiments/sigma-experiment.ipynb` (imports seaborn), `pyproject.toml` (no seaborn listed) |
| **Symptom** | `ModuleNotFoundError: No module named 'seaborn'` |
| **Status** | **FIXED** — `pip install seaborn==0.13.2` applied |
| **Remaining** | `pyproject.toml` still missing seaborn in `dependencies` — should be added |

---

## 2. Tooling Issues

### T-01 — Publication monitor lacks HTTP retry (MEDIUM)

| Field | Value |
|-------|-------|
| **File** | `scripts/monitor-pub.py` — `fetch_semantic_scholar()` |
| **Symptom** | `HTTP Error 429: Too Many Requests` on 3/4 keyword clusters during today's run |
| **Root Cause** | No retry logic. Single-shot HTTP request fails permanently on rate limit. |
| **Impact** | Semantic Scholar results silently missing from alert-log. Misses potentially critical papers. |
| **Fix** | Add exponential backoff: 3 attempts with 2s/4s/8s sleep between retries. |

### T-02 — Keyword clusters too narrow (LOW)

| Field | Value |
|-------|-------|
| **File** | `scripts/monitor-pub.py` — `KEYWORD_CLUSTERS` dict |
| **Symptom** | Misses papers on grokking, agentic cognition, metacognition benchmarks |
| **Current clusters** | schema_coherence, compositional_generalization, ood_generalization, phase_transition_training |
| **Missing** | `"grokking" phase transition`, `"metacognition" AI benchmark`, `"executive function" AI`, `"theory of mind" language model`, `"agentic" evaluation benchmark` |
| **Fix** | Add 4-5 new keyword clusters |

### T-03 — No formal test suite (MEDIUM)

| Field | Value |
|-------|-------|
| **File** | `code/tests/` — does not exist |
| **Current state** | `pyproject.toml` configures pytest with `testpaths = ["tests"]` but no tests exist |
| **Impact** | No regression protection. Code changes rely entirely on manual testing. |
| **Fix** | Create `tests/test_ode.py`, `tests/test_config.py`, `tests/test_models.py` with smoke tests |

### T-04 — No local smoke test (MEDIUM)

| Field | Value |
|-------|-------|
| **Current state** | Daily D3.1 task tries `jupyter nbconvert --execute` which requires Kaggle |
| **Impact** | No way to verify code changes without a full Kaggle session |
| **Fix** | Create `scripts/smoke_test.py` — 10s execution, tests imports + ODE math + configs + model instantiation |

---

## 3. Paper Issues

### P-01 — 5 new papers need CITE or ADDRESS (MEDIUM)

| Paper | Action | Location | Priority |
|-------|--------|----------|----------|
| Montanari & Wang (2026) — Phase Transitions for Feature Learning (`arXiv:2602.01434`) | **CITE** | §7 (Phase Structure) | Medium |
| Grokking is a Phase Transition: SLT Explains Sudden Generalization (2026, `arXiv:2603.01192`) | **CITE** | §7 | Medium |
| TailLoR — Protecting Principal Components in Parameter-Efficient Continual Learning (2026, `arXiv:2606.06494`) | **CITE** | §3.2 (Decay & Obsolescence) | Low |
| E2H Reasoner — Curriculum RL from Easy to Hard Improves LLM Reasoning (2026, `arXiv:2506.06632`) | **CITE** | §7 (Curriculum) | Medium |
| Redhardt et al. — Scaling can lead to compositional generalization (NeurIPS 2025 Spotlight) | **ADDRESS** | §2.1 — this challenges Σ-Model's central claim that structural gaps persist at scale | **High** |

### P-02 — gap_conflict_map.md needs refresh (MEDIUM)

| Field | Value |
|-------|-------|
| **Current state** | 11 queries, 41 papers, last updated March 2026 |
| **New papers needing rows** | 5 from P-01 |
| **Organisation** | Add Q12 "Phase Transitions and Curriculum Learning" for Montanari+Wang, Grokking-as-Phase-Transition, E2H. Add Redhardt to Q1. Add TailLoR to Q4. |
| **Impact** | Without update, paper positioning is stale against 3 months of new literature |

### P-03 — 12/20 claims still PENDING (HIGH, time-gated)

| Field | Value |
|-------|-------|
| **Claims** | C-008 through C-020 (all Kaggle/Prolific dependent) |
| **Status** | All PENDING — gated on Kaggle results after June 1, 2026 |
| **Blocking** | Condition 6 of verification report — 5/6 PASS, 1 PENDING |
| **Action** | Post-June 1: download results, update claims to COLLECTED or FALSIFIED, write §12 |

---

## 4. Code Quality Issues

### C-01 — 39 ruff lint errors (FIXED)

| Field | Value |
|-------|-------|
| **Count** | 39 errors found during daily workflow execution |
| **Categories** | F401 (unused imports in `__init__.py`), I001 (import sorting), E501 (line length), N806 (variable naming), unused `import os` |
| **Status** | **ALL FIXED** — 8 auto-fixed by ruff, 30 manually fixed: added `__all__` + `# noqa: F401` to 5 `__init__.py` files, fixed naming in `training.py`/`transformer.py`, line lengths in `payload.py`/`equations.py` |
| **Verification** | `ruff check code/sigma/` — all checks pass |

### C-02 — seaborn missing from `pyproject.toml` (LOW)

| Field | Value |
|-------|-------|
| **Status** | Installed in `sigma_env/` but not listed in `pyproject.toml` dependencies |
| **Impact** | Fresh `pip install -e .` will miss seaborn; notebook fails |
| **Fix** | Add `"seaborn>=0.13"` to `dependencies` in root `pyproject.toml` |

---

## 5. Workflow Design Constraints

### W-01 — Notebook execution requires Kaggle GPU

| Field | Value |
|-------|-------|
| **Hardware** | Intel i5-8250U (4c/8t @ 1.6GHz), 6.4 GiB free RAM, no GPU |
| **Runtime (local)** | 2000 timesteps × 15 runs × 3 conditions = ~days on CPU |
| **Runtime (Kaggle)** | 2-4 hours on T4x2 GPU |
| **Constraint** | All training/benchmark notebook execution must happen on Kaggle. Local testing is code-level only. |
| **Documented in** | `kaggle-runbook.md` |

### W3.1 — Paper PDF build pipeline fixed

| Field | Value |
|-------|-------|
| **Status** | **FIXED** |
| **Issue** | `make tex && make pdf` failed with multiple errors: missing pandoc-crossref binary, Unicode characters in text mode (δ, σ), missing `\tightlist`, missing `\newcounter{none}`, `\tag` inside `\[...\]`, missing checkmark/crossmark fonts |
| **Template changes** | Added `fontspec`, `unicode-math`, `\setmathfont{latinmodern-math.otf}`, `pifont`, `newunicodechar` (Greek + checkmark mappings), `\providecommand{\tightlist}`, `\newcounter{none}`. Removed `[utf8]{inputenc}` + `[T1]{fontenc}`. |
| **Makefile changes** | `--filter pandoc-crossref` removed (binary not available). `latexmk -pdf` → `latexmk -pdflua` for Unicode support. Added `-f` force flag. |
| **Lua filter** | Added `templates/lua-filters/eqn-fix.lua` — converts `\tag{N}` → `\qquad(N)` in both inline and display math, promotes inline math with `\tag` to display math |
| **Paper fix** | Replaced Unicode combining dot `∆̇(d,t)` with `\dot{\Delta}(d,t)` (U+0307 cause of cmmi10 font errors) |
| **Output** | `manuscript.pdf` generated successfully (304 KB, 3773-line .tex input). Still has minor missing-character warnings (U+0410, U+221D) that don't affect output. |
| **Regression** | `\label`/`\ref` cross-references won't work without pandoc-crossref — figures/tables will use manual numbering |

### W-02 — Weekly tasks split into local vs. Kaggle categories

**Local-only** (no GPU needed):
- Claims registry anchor sweep
- Config-vs-code parameter audit
- Payload inspection
- Literature sweep
- Figure regeneration
- Prose polish
- ODE cross-referencing
- Errata reconciliation

**Kaggle-required**:
- Full notebook execution (W1.1)
- Seed determinism test (W1.4)
- Full reproducibility audit (M1.1)

---

## Appendix: Execution Priority

```
Phase 0 — Build pipeline:
  [x] W3.1: Paper PDF build pipeline (pandoc + lualatex)

Phase 1a — Immediate local fixes:
  [x] I-01: Notebook Kaggle detection
  [x] I-02: SCANDataset → data.py
  [x] I-03: Dynamic num_workers
  [x] C-02: seaborn → pyproject.toml

Phase 1b — Tooling improvements:
  [x] T-01: Monitor script HTTP retry
  [x] T-03: Create test_ode.py, test_config.py
  [x] T-04: Create scripts/smoke_test.py

Phase 2 — Paper updates:
  [ ] P-01: 5 paper citations/addresses
  [ ] P-02: gap_conflict_map.md refresh
  [ ] T-02: Expand keyword clusters

Phase 3 — Kaggle session (triggered):
  [x] W1.1: Full notebook execution
  [—] W1.4: Seed determinism test (skipped — cudnn.benchmark incompatibility)
  [x] M1.1: Full reproducibility audit

Phase 4 — Post-June 1 2026:
  [~] P-03: Kaggle results integration (C-008 confirmed, C-009–C-020 pending)
  [x] M2.5: §12.0 ODE Validation Experiment added to manuscript.tex
```
