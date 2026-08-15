# Phase 00 — Cross-Cutting Concerns

**Deadline**: Ongoing
**Dependencies**: None
**Output**: Phase execution checklist enforced across all experimental phases

---

This document defines requirements that apply to **every** phase below. Each phase document will reference these by number. All phases must comply unless explicitly exempted.

---

### CC.1: Reproducibility

- [ ] CC.1.1: Every training run uses `torch.manual_seed(run_id * 42 + 7)` + `np.random.seed(run_id * 42 + 7)` — inherited from `code/sigma/models/training.py`
- [ ] CC.1.2: `cudnn.deterministic = True` set before any model instantiation
- [ ] CC.1.3: Every experiment config sets a `global_seed` in its YAML file
- [ ] CC.1.4: All random operations (data shuffling, weight init, noise injection) accept an explicit `seed` parameter — never use implicit global state
- [ ] CC.1.5: Full `pip freeze` captured per experiment run; lockfile updated after dep changes
- [ ] CC.1.6: GPU model, CUDA version, PyTorch version, and Python version logged at start of every training script
- [ ] CC.1.7: Every result pickle contains the full config dict and seed used

### CC.2: Data Provenance

- [x] CC.2.1: Every dataset used must have a pinned version, download URL, and SHA256 checksum recorded in a data registry doc — *registry created; SHA256 TBD until Phase 01 download*
- [x] CC.2.2: Pfam 38.2 version string must appear in every experiment config under `data.pfam_version` — *present in pfam-base.yaml*
- [x] CC.2.3: Extracted data directories are gitignored; only the download script and checksums are committed — *experiments/data/pfam/ in .gitignore*
- [ ] CC.2.4: Train/validation/OOD splits must be reproducible from seed alone — *requires splits.py implementation in Phase 01/07*

### CC.3: Claim Tracking

- [ ] CC.3.1: Every quantitative result in the paper must have a `<!-- CLAIM:C-NNN -->` anchor in `docs/claims-registry.md`
- [ ] CC.3.2: New claims for this paper start at C-039
- [ ] CC.3.3: Each claim transitions through states: DESIGNED → PENDING → COLLECTED → VERIFIED
- [ ] CC.3.4: `scripts/verify_empirical_claims.py` must pass before paper submission (see [Phase 08](08_paper_writing.md))

### CC.4: Testing Requirements

- [ ] CC.4.1: All new Python modules must have corresponding test files in `tests/`
- [ ] CC.4.2: Minimum 60% line coverage for protein subpackage (code review threshold, not strict automated gate)
- [ ] CC.4.3: ODE solver unit tests must still pass after any changes to shared code in `code/sigma/ode/`
- [ ] CC.4.4: All config YAML files must load successfully via `sigma.config.load_config()`
- [ ] CC.4.5: Smoke test (`scripts/smoke_test.py`) must pass before any experiment batch run

### CC.5: Documentation Requirements

- [ ] CC.5.1: Every public function in `code/sigma/proteins/` must have a Google-style docstring — *requires module implementation in Phases 01–07*
- [x] CC.5.2: Every YAML config must have inline comments explaining non-obvious parameters — *all 10 configs reviewed and annotated*
- [ ] CC.5.3: Notebooks must have a comment header cell documenting purpose, author, and date — *requires notebook creation in Phase 03+*
- [x] CC.5.4: Phase documents updated with completion status as work progresses — *Phase 00_5 complete; CC.8 matrix updated*
- [x] CC.5.5: CHANGELOG.md updated after each phase completion — *Phase 00_5 entry added*

### CC.6: Figure Generation Standards

- [ ] CC.6.1: All figures must use Okabe-Ito colourblind-safe palette (defined in `paper/manuscript.tex` preamble)
- [ ] CC.6.2: All figures must have alt-text registered in `docs/figure-alt-text.md`
- [ ] CC.6.3: Figure generation scripts must be committed (notebook cell or `.py` file) — no manually constructed figures
- [ ] CC.6.4: Resolution: ≥ 300 DPI for raster, PDF/EPS for vector where possible

### CC.7: GPU & Compute Hygiene

- [ ] CC.7.1: Clear GPU cache (`torch.cuda.empty_cache()`) between independent runs
- [ ] CC.7.2: Log peak GPU memory per run for cost estimation
- [ ] CC.7.3: Use `torch.amp.autocast_mode.autocast` and `torch.amp.grad_scaler.GradScaler` for all training (inherited pattern)
- [ ] CC.7.4: Set `torch.backends.cudnn.benchmark = True` only for fixed input sizes

---

### CC.8: Phase Compliance Matrix

| Phase | CC.1 (Reprod) | CC.2 (Proven) | CC.3 (Claims) | CC.4 (Tests) | CC.5 (Docs) | CC.6 (Figs) | CC.7 (GPU) |
|-------|---------------|---------------|---------------|--------------|--------------|--------------|------------|
| 00_repo | — | — | Required | — | ✅ Done | — | — |
| 00_5 | — | ✅ Done | — | — | ✅ Done | — | — |
| 01 | Required | Required | — | Required | Required | — | — |
| 02 | Required | — | — | Required | Required | — | Required |
| 03 | Required | Required | PENDING | — | Required | Required | Required |
| 04 | Required | — | Required | Required | Required | Required | — |
| 05 | Required | Required | PENDING | Required | Required | Required | Required |
| 06 | Required | Required | PENDING | Required | Required | Required | Required |
| 07 | Required | Required | Required | Required | Required | Required | — |
| 08 | — | — | Required | Required | Required | Required | — |
| 09 | — | — | Required | — | Required | — | — |
