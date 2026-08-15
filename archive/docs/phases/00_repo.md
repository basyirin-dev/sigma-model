# Phase 00_repo — Repo & Tooling Infrastructure

**Deadline**: 5 Jul 2026
**Dependencies**: None
**Output**: Repository infrastructure ready for protein work

---

### Task R.1: Create `code/sigma/proteins/` subpackage stub

- [x] R.1.1: Create directory: `code/sigma/proteins/`
- [x] R.1.2: Create `__init__.py` with provisional exports (can be empty initially, populated per phase)
- [x] R.1.3: Create stub modules: `data.py`, `models.py`, `train.py`, `probes.py`, `metrics.py`, `benchmark.py`, `splits.py`
- [x] R.1.4: Each stub has a module-level docstring and `pass` — no implementation yet

### Task R.2: Add new dependencies

- [x] R.2.1: Add `biopython>=1.83` to `requirements.txt` — Stockholm format parsing, Pfam data handling
- [x] R.2.2: Add `pyhmmer>=0.10` to `requirements.txt` — HMMER3 bindings for domain similarity bit scores
- [x] R.2.3: Add `fair-esm>=2.0` to `requirements.txt` — ESM model loading for Phase 6 validation
- [x] R.2.4: Run `pip install` in activated `hbar_env` to verify all three install cleanly
- [x] R.2.5: Regenerate `requirements-lock.txt` with `pip freeze | grep -E "^(biopython|pyhmmer|fair-esm|numpy|scipy|torch|pyyaml|tqdm|matplotlib|datasets|seaborn|pandas|pyarrow|triton)==" > requirements-lock.txt`
- [x] R.2.6: Verify `PYTHONPATH=code:$PYTHONPATH python scripts/smoke_test.py` still passes after dep addition

### Task R.3: Create experiment configs

- [x] R.3.1: Create `experiments/configs/pfam-base.yaml` — shared protein experiment params:
  - `model.d_model: 256`, `model.nhead: 8`, `model.num_layers: 4`, `model.vocab_size: 22000`
  - `training.n_timesteps: 5000`, `training.batch_size: 32`, `training.max_seq_len: 20`
  - `data.pfam_version: "38.2"`, `data.min_domain_arch_length: 2`, `data.max_domain_arch_length: 15`
  - `data.recombination_distance_metric: "hmm_bit_score"`
  - `ode` section identical to `base.yaml` (domain-agnostic params)
  - `conditions` section: baseline/additive/multiplicative with protein-appropriate sigma_init values
  - `experiment.n_runs_per_condition: 15` (scales to N=500 per condition in Phase 3)
- [x] R.3.2: Create `experiments/configs/pfam-brittle.yaml` — N=500 brittle domain experiment:
  - `experiment.n_runs_per_condition: 167` (3 conditions = 501 runs ≈ N=500)
  - `experiment.conditions: ["familiar_combos", "new_families", "cross_fold"]`
  - `statistical.alpha: 0.00625`, `statistical.test: "welch_t"`
- [x] R.3.3: Create `experiments/configs/pfam-grammar.yaml` — grammar induction probes
- [x] R.3.4: Create `experiments/configs/pfam-benchmark.yaml` — PfamCG-1.0 benchmark
- [x] R.3.5: Verify all configs load: `PYTHONPATH=code:$PYTHONPATH python -c "from sigma.config import load_config; cfg = load_config('experiments/configs/pfam-base.yaml'); print('OK:', cfg['model']['d_model'])"`

### Task R.4: Create `paper-neurips/` scaffold

- [x] R.4.1: Create directory: `paper-neurips/`
- [x] R.4.2: Create `paper-neurips/Makefile` following pattern from `paper-jmlr/Makefile`:
  - Targets: `pdf` (pdflatex + bibtex), `arxiv` (tar.gz bundle), `clean`
  - NeurIPS uses `pdflatex` (not lualatex) — confirm with style file
- [x] R.4.3: Create `paper-neurips/main.tex` — minimal scaffold with `\documentclass{neurips_2027}` and placeholder sections matching the paper outline
- [x] R.4.4: Download `neurips_2027.sty` from https://neurips.cc/ (official style file)
- [x] R.4.5: Create `paper-neurips/bibliography.bib` — copy relevant entries from `paper/bibliography.bib`, add placeholders for new citations
- [x] R.4.6: Create `paper-neurips/figures/` directory with `.gitkeep`
- [x] R.4.7: Create `paper-neurips/supplement/` directory with `.gitkeep`
- [x] R.4.8: Verify `make pdf` compiles (even if content is placeholder)

### Task R.5: Register new claims

- [x] R.5.1: Add C-039 to `docs/claims-registry.md` in DESIGNED status:
  > C-039 | σ-trap replicates in protein domain data (H1) | PENDING | §4 | ΔCG ≥ threshold
- [x] R.5.2: Add C-040: ΔCG ≥ 30pp for low-σ models on Pfam OOD splits — DESIGNED
- [x] R.5.3: Add C-041: PLMs encode surface co-occurrence, not domain grammar (H2) — DESIGNED
- [x] R.5.4: Add C-042: Structural OOD accuracy < lexical OOD accuracy by >10pp — DESIGNED
- [x] R.5.5: Add C-043: Multiplicative model fits better than additive (H3) — DESIGNED
- [x] R.5.6: Add C-044: PfamCG-1.0 benchmark valid against known biology — DESIGNED
- [x] R.5.7: Reserve C-045 to C-050 for claims discovered during experimentation

### Task R.6: Create `docs/protein-data-registry.md`

- [x] R.6.1: Document Pfam 38.2 download URL, SHA256 checksum, release date
- [x] R.6.2: Document expected disk footprint after extraction
- [x] R.6.3: Document data directory structure (what paths will contain what files)
- [x] R.6.4: Document which files are gitignored and why

### Task R.7: Create `docs/risks/` and risk register

- [x] R.7.1: Create `docs/risks/RISK_REGISTER.md` following OpenSciRe format
- [x] R.7.2: Register at minimum these risks:
  - R-001: Protein domain recombination may not exhibit compositional gap (null H1) — Medium probability, publishable
  - R-002: PLMs already encode domain grammar (null H2) — Medium, refine probes or publish informative null
  - R-003: Computational cost of N=500 exceeds Kaggle GPU limits — Low, pre-tested
  - R-004: JAIR paper not accepted before NeurIPS submission — Low, cite arXiv
  - R-005: ESM-2 training data overlaps with Pfam 38.2 sequences — Low, conservative bias
  - R-006: PfamCG-1.0 splits don't correlate with known biology — Medium, validate first

### Task R.8: Verify OpenCode configuration

- [x] R.8.1: Check `opencode.json` is valid JSON: `python3 -m json.tool opencode.json`
- [x] R.8.2: Verify MCP servers still running: `sequential_thinking`, `context7`, `gh_grep`
- [x] R.8.3: Check if any protein-specific plugins would be useful (likely none needed)
- [x] R.8.4: Update `AGENTS.md` with new commands (pfam experiment execution, protein-specific lint paths)

---

**Phase 00_repo Exit Criteria**:
- [x] All 8 tasks complete
- [x] `PYTHONPATH=code:$PYTHONPATH python scripts/smoke_test.py` passes
- [ ] `ruff check code/sigma/` passes — 35 pre-existing errors (mostly E501 line-too-long, non-blocking)
- [ ] `pytest tests/` passes — needs `PYTHONPATH=code:$PYTHONPATH pytest tests/` (pre-existing issue, not a regression)
- [x] All new configs load without error
