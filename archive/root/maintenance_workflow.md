# H-Bar V3.0+ — Daily / Weekly / Monthly Maintenance Workflow

**Scope:** All debugging, adaptive maintenance, enhancements, and internal improvements.
**Owner:** Independent researcher (single maintainer).
**Golden rule:** Activate `source hbar_env/bin/activate` before any Python work.
**Date:** 2026-06-06

---

## How To Use This Document

Each timeframe (daily / weekly / monthly) is split into the four quadrants:

| Quadrant | Focus | Typical Effort |
|----------|-------|----------------|
| **1. Debugging** | Factual, logical, technical errors that weaken claims | Find & fix |
| **2. Adaptive Maintenance** | Responding to ecosystem drift (benchmarks, norms, hardware) | Track & adjust |
| **3. Enhancements** | Minor additive improvements in clarity, coverage, rigour | Polish |
| **4. Internal Improvements** | Structural health, reproducibility, knowledge management | Sustain |

For each task: **what to do**, **why**, **how**, **expected duration**, and **verification**.

---

## I. DAILY WORKFLOW (~20–45 min)

Quick tasks that catch problems before they compound. Best done at the start or end of a work session.

### 1.1 Debugging — Daily

| # | Task | What | Why | How | Duration | Verify |
|---|------|------|-----|-----|----------|--------|
| D1.1 | **Publication monitor run** | Check arXiv / Semantic Scholar for new papers matching H-Bar keywords | Prevents missed competition or supporting evidence | `python scripts/monitor-pub.py` | 5 min | Check `docs/alert-log.md` was updated |
| D1.2 | **Errata log review** | Read `docs/errata/errata-log.md` for newly opened entries | Catch issues before they compound | Read file; if new errata appeared, triage severity | 2 min | Confirm no new HIGH entries |
| D1.3 | **Notebook cell 0 verification** | Check both notebooks import without errors and configs parse | Broken imports silently rot | `cd experiments && python -c "from hbar import *; print('OK')"` | 3 min | Exit code 0, prints "OK" |
| D1.4 | **Quick lint** | Run ruff on any files modified today | Typos and unused imports accumulate | `ruff check code/hbar/` | 2 min | No new errors vs. yesterday |

### 1.2 Adaptive Maintenance — Daily

| # | Task | What | Why | How | Duration | Verify |
|---|------|------|-----|-----|----------|--------|
| D2.1 | **arXiv new-submissions scan** | Browse daily arXiv cs.AI / cs.CL / cs.LG new submissions (last 24 h) | Catch papers that directly overlap or challenge H-Bar claims | https://arxiv.org/list/cs.AI/new (or RSS via monitor script) | 10 min | Log any relevant paper to `docs/alert-log.md` manually |
| D2.2 | **Benchmark dataset status** | Confirm SCAN / COGS / PCFG-SET zip archives are intact and extracts are clean | Datasets are the empirical foundation | `ls -la hackathon/*.zip` and verify one list file | 2 min | All 3 zips present; at least one extract test passes |

### 1.3 Enhancements — Daily

| # | Task | What | Why | How | Duration | Verify |
|---|------|------|-----|-----|----------|--------|
| D3.1 | **Notebook kernel check** | Verify both `.ipynb` files open without kernel errors | Catches stale dependencies before experiment runs | `jupyter nbconvert --to notebook --execute --inplace experiments/h-bar-experiment.ipynb --allow-errors --ExecutePreprocessor.timeout=60` (quick smoke test only; stop after cell 1) | 5 min | Cell 1 completes without ImportError |
| D3.2 | **Docstring freshness** | If any Python function was modified, ensure docstring matches signature | Prevents internal confusion | Check `git diff` for modified `.py` files; verify docstrings | 3 min | No docstring/signature mismatch |

### 1.4 Internal Improvements — Daily

| # | Task | What | Why | How | Duration | Verify |
|---|------|------|-----|-----|----------|--------|
| D4.1 | **Git hygiene** | Ensure working tree is clean before end of session | Prevents lost work and ambiguous state | `git status` | 1 min | Clean (or staged, with clear commit message) |
| D4.2 | **Config sanity** | Verify `experiments/configs/base.yaml` parses and all 5 benchmark configs merge without conflict | Config rot is silent but deadly | `python -c "from hbar.config import load_config, merge_configs; base=load_config('experiments/configs/base.yaml'); print('base OK'); [print(f'h-{t}: {len(merge_configs(base, load_config(f\"experiments/configs/h-{t}.yaml\")))} keys') for t in ['ptb','afb','mcb','dcb','stb']]"` | 3 min | All 6 configs load without KeyError |

---

## II. WEEKLY WORKFLOW (~2–4 h)

Deeper tasks that reset the baseline. Best scheduled at a consistent weekly checkpoint (e.g., Friday afternoon or Monday morning).

### 2.1 Debugging — Weekly

| # | Task | What | Why | How | Duration | Verify |
|---|------|------|-----|-----|----------|--------|
| W1.1 | **Full notebook execution** | Run both notebooks end-to-end | Catches numerical drift, silent NaN, or hardware-dependent discrepancies | `jupyter nbconvert --to notebook --execute experiments/h-bar-experiment.ipynb --ExecutePreprocessor.timeout=3600` | 45 min | Exit code 0; output files generated |
| W1.2 | **Claims registry anchor sweep** | Ensure every `<!-- CLAIM:C-NNN -->` in `paper.md` has an entry in `docs/claims-registry.md` and vice versa | Claim tracking is the single-source-of-truth for verifiability | `grep '<!-- CLAIM:' paper/paper.md | sort > /tmp/anchors.txt && cut -d'|' -f2 docs/claims-registry.md | grep C- | tr -d ' ' | sort > /tmp/registry.txt && diff /tmp/anchors.txt /tmp/registry.txt` | 5 min | No differences (or only expected PENDING entries) |
| W1.3 | **Config-versus-code parameter audit** | Verify base.yaml values match default arguments in `equations.py` and `training.py` | Disagreement between config and code is the most common reproducibility bug | Read `code/hbar/ode/equations.py` defaults, cross-check against `experiments/configs/base.yaml` ODE section | 10 min | Every parameter in equations.py that has a config equivalent matches base.yaml |
| W1.4 | **Seed determinism test** | Run one condition (baseline) twice with same seed; confirm bit-identical output | Non-determinism from CUDA / MPS / order-of-operations erodes confidence | Run 2 copies of the experiment with `global_seed: 2024`; `diff` outputs | 30 min | Outputs byte-identical (or known-non-deterministic ops documented) |
| W1.5 | **Payload inspection** | Quick-inspect 5 Kaggle JSONL payloads for malformed lines | Kaggle ingestion silently fails on bad JSONL | `python -c "import json; [print(f'{f}: {len(open(f\"kaggle_payloads/{f}_pilot.jsonl\").readlines())} lines OK') for f in ['hafb','hdcb','hmcb','hptb','hstb']]"` | 5 min | All 5 files parse as valid JSON with non-zero line count |

### 2.2 Adaptive Maintenance — Weekly

| # | Task | What | Why | How | Duration | Verify |
|---|------|------|-----|-----|----------|--------|
| W2.1 | **Competitor literature sweep** | Review new papers from arXiv + Semantic Scholar that arrived this week; assess if any require citation, differentiation, or §2.2 update | Field moves fast; stale related work signals lack of rigour | Read `docs/alert-log.md` entries; for each relevant paper, read abstract + conclusion; decide CITE / ADDRESS / SCOPE OUT | 30 min | Update `gap_conflict_map.md` if new paper is relevant |
| W2.2 | **Benchmark SOTA re-check** | Check if any new SOTA has been published on SCAN / COGS / PCFG-SET that would shift baseline expectations | Baselines that looked strong 3 months ago may look weak now | Search "SCAN compositional generalization 2026", "COGS 2026 benchmark", "PCFG-SET 2026" | 15 min | Update baseline numbers in `paper/paper.md` §2.1 if needed |
| W2.3 | **Python dependency audit** | Check that all packages in `pyproject.toml` are still current within major version; no deprecated APIs used | Framework migrations (PyTorch 2.x compile, JAX, CUDA) can silently break training | `pip list --outdated | grep -E "numpy|scipy|torch|datasets|pandas|pyyaml"` | 5 min | No critical updates that would block the paper |
| W2.4 | **Kaggle platform check** | Verify Kaggle benchmark SDK is still compatible; check for API deprecation notices | Kaggle platform changes can break the evaluation pipeline | Visit Kaggle docs / forums; check `kaggle-benchmarks` PyPI page | 10 min | Log any needed migration to `docs/adrs/` |

### 2.3 Enhancements — Weekly

| # | Task | What | Why | How | Duration | Verify |
|---|------|------|-----|-----|----------|--------|
| W3.1 | **Figure regeneration** | Rebuild all TikZ figures from source to confirm they compile and look correct | Figures are the paper's visual argument; broken TikZ is an immediate defect | `cd paper && for f in figures/figure*.tex; do latexmk -pdf "$f" 2>&1 | tail -3; done` | 15 min | All figures render without error |
| W3.2 | **Paper prose polish pass** | Read one major section of `paper/paper.md` for clarity, consistency, and typos | Small prose improvements compound into a clean submission | Pick one section (§1–§5 rotation); read through; apply edits | 30 min | 3–5 improvements per section (typo fix, clarity rephrase, notation check) |
| W3.3 | **Demo / artifact link check** | Verify all URLs in `artifacts/demo-links.md` and CITATION.cff are live | Bad links signal abandonment | `artifacts/demo-links.md` is currently TBD — if any links have been added, verify they resolve | 5 min | All links resolve with HTTP 200 |

### 2.4 Internal Improvements — Weekly

| # | Task | What | Why | How | Duration | Verify |
|---|------|------|-----|-----|----------|--------|
| W4.1 | **ODE cross-referencing sweep** | Ensure every equation reference in `paper.md` points to the correct number and the equation exists | Equation number drift is the most common LaTeX bug | Search `paper.md` for `Eq.` and `eq:`; spot-check 10 random references | 10 min | All spot-checked references resolve to the correct equation |
| W4.2 | **Documentation consistency check** | Verify `program.md`, `README.md`, and `AGENTS.md` are consistent on process | Disjointed process docs cause confusion | Diff key sections: workflow structure, protected elements, language rules | 15 min | No contradiction between docs |
| W4.3 | **Unit test run** | Execute any existing unit tests (or write smoke tests for core ODE functions) | Even a 2-test suite catches regressions | `python -m pytest --tb=short` (target `code/tests/` if it exists, else create `tests/`) | 5 min | All tests pass |
| W4.4 | **Errata log reconciliation** | Check whether any errata entries correspond to OPEN issues elsewhere or to claims-registry gaps | Errata that aren't propagated become lost institutional knowledge | Cross-reference `docs/errata/errata-log.md` with `documentation/register.md` | 10 min | Every errata has a register reference or a clear "no issue needed" note |

---

## III. MONTHLY WORKFLOW (~1–2 days)

Major structural reviews that keep the paper submission-ready and the project sustainable. Best scheduled as a 1–2 day block at month-end.

### 3.1 Debugging — Monthly

| # | Task | What | Why | How | Duration | Verify |
|---|------|------|-----|-----|----------|--------|
| M1.1 | **Full reproducibility audit** | Complete re-run from clean environment: venv creation → pip install → config load → ODE validation → benchmark suite → metric calculation | Gold standard for reproducibility; catches deep-seated environmental drift | 1. Create fresh venv: `python3.14 -m venv /tmp/hbar-audit && source /tmp/hbar-audit/bin/activate && pip install -e .` <br>2. Run both notebooks end-to-end <br>3. Compare output files with committed references | 3 h | All metrics match committed baselines within floating-point tolerance (1e-6) |
| M1.2 | **Statistical re-evaluation** | Recompute all quantitative claims in C-001–C-020 with correct statistical tests | Wrong test choice (t-test vs Mann-Whitney, missing Bonferroni) is the most common empirical bug | Identify each claim's statistical procedure; verify: (a) normality assumption checked, (b) parametric vs. non-parametric justified, (c) multiple comparisons corrected, (d) confidence intervals reported | 2 h | Written justification for each statistical choice in `docs/claims-registry.md` footer |
| M1.3 | **Proof-reading sweep** | Read entire `paper/paper.md` for narrative bugs: strawman baselines, overclaiming, misattribution, figure axis errors | Reviewer scrutiny catches these; fix them before submission | Print-preview the PDF; read linearly with a critical eye for: (a) "first to" statements — verify, (b) competitor descriptions — are they fair?, (c) axis labels — do they match text?, (d) swapped model names in captions | 3 h | List of 5–10 critical fixes applied |
| M1.4 | **Kaggle payload audit (post-June 1 only)** | Verify all 5 JSONL payloads against their track definitions: correct fields, correct conditions, correct ordering | Malformed payloads invalidate the entire hackathon | Read each track definition and cross-check against the corresponding JSONL: condition structure, metric keys, split sizes | 1 h | All payloads structurally valid per track definitions |

### 3.2 Adaptive Maintenance — Monthly

| # | Task | What | Why | How | Duration | Verify |
|---|------|------|-----|-----|----------|--------|
| M2.1 | **Full SOTA benchmark refresh** | Re-evaluate: are H-Bar's baselines still SOTA? Have any datasets been deprecated? Are new benchmarks standard? | A paper whose baselines are 6+ months old looks weak | Systematic search: SCAN leaderboard, COGS leaderboard, PCFG-SET, HELM, MMLU-Pro, BigBench. Update numbers in `paper/paper.md` §2.1. Check dataset deprecation notices. | 4 h | Updated §2.1 baseline table; dataset status verified with source |
| M2.2 | **Conference / journal norm review** | Check latest submission guidelines for target venue (ICLR/NeurIPS/ICML/JMLR): page limits, reproducibility checklist, ethics statement, CRediT author statement | Submission requirements change annually | Read latest call for papers; check for new requirements: (a) broader impact statement format, (b) reproducibility checklist items, (c) paper ownership / AI authorship policies | 1 h | Document any new requirements in `documentation/ARXIV_SUBMISSION_GUIDE.md` |
| M2.3 | **Environmental reporting update** | Recompute FLOPs and estimated CO2e for training runs | Several conferences now require carbon footprint statements | Estimate based on: GPU-hours × TDP × PUE × regional carbon intensity. Document in appendix or new §10 subsection. | 1 h | Add environmental impact paragraph if not already present |
| M2.4 | **Framework compatibility re-check** | Verify `hbar_env` still works with latest PyTorch / JAX / CUDA toolchain on available hardware | PyTorch 2.x compile, CUDA 12.x, and Python 3.14 all evolve quickly | `python -c "import torch; print(torch.__version__); print(torch.cuda.is_available())"`; run training smoke test | 30 min | Training loop completes without deprecation warnings |
| M2.5 | **Kaggle results window (critical — post-June 1)** | Check Kaggle competition status for H-PTB / H-AFB / H-MCB / H-DCB / H-STB | This is the single gating factor for Condition 6 of verification | Visit Kaggle; download results if available; integrate into §12 "Empirical Grounding" as described in `documentation/verification_report.md` §Condition-6-action | 4 h | §12 written and claims C-008–C-020 updated from PENDING to COLLECTED or FALSIFIED |

### 3.3 Enhancements — Monthly

| # | Task | What | Why | How | Duration | Verify |
|---|------|------|-----|-----|----------|--------|
| M3.1 | **Notation glossary creation / update** | Generate a table of all symbols, definitions, first-use equation, and dimensionality | Readers routinely get lost in the symbol soup; a glossary is the highest-ROI clarity improvement | Extract all notation from `paper.md` §3–§6; create a LaTeX table sorted alphabetically; insert after abstract or as appendix C | 2 h | Every symbol used ≥3 times appears in glossary; no symbols missing |
| M3.2 | **Failure mode gallery** | Compile a figure showing 3–4 representative failure cases of H-Bar models with analysis | Demonstrates scientific honesty and deepens reader trust | From OOD accuracy breakdowns, pick 1–2 structural generalization failures and 1–2 attention fidelity failures; create annotated figure + analysis paragraph | 3 h | New figure + 200–300 word analysis added to §10 Limitations |
| M3.3 | **Human evaluation feasibility check** | Assess whether a small Prolific / MTurk study (N=30–50) for 1–2 benchmarks is feasible before commitment to N=200 | Small pilot can validate the human baseline protocol described in hackathon tracks | Draft a 10-question pilot; estimate cost (N=30 × $2 = $60); check IRB requirements | 2 h | Feasibility assessment + cost estimate documented |
| M3.4 | **Colab / Hugging Face Space** | Deploy a minimal interactive demo of the HBarTransformer or ODE visualisation | Dramatically increases paper visibility and reader engagement | Create a Streamlit/Gradio app in `artifacts/demo/` that plots σ_A(t) and δ_A(t) trajectories; deploy to Spaces if possible | 4 h | Working demo link added to `artifacts/demo-links.md` |
| M3.5 | **TL;DR / Practitioner summary** | Write a 1-page plain-language summary of what H-Bar says, why it matters, and how to use it | Non-expert readers (reviewers from adjacent fields, industry practitioners) need orienting | Write ~500 words covering: problem → core idea → one equation → one prediction → one benchmark → limitations | 1 h | Document saved as `artifacts/practitioner-summary.md` |

### 3.4 Internal Improvements — Monthly

| # | Task | What | Why | How | Duration | Verify |
|---|------|------|-----|-----|----------|--------|
| M4.1 | **Full verification sweep** | Re-run all 6 conditions from `documentation/verification_report.md` | Conditions drift as the paper evolves; periodic re-verification prevents silent regression | 1. Register empty? — check `documentation/register.md` <br>2. Stanford dimensions ≥ 8/10 — re-run diagnostic <br>3. Gap & conflict map actioned — verify all rows <br>4. Integration map consistent — verify all 30 rows <br>5. PIRL citation resolved — grep for forward cites <br>6. Hackathon results integrated — conditionally | 3 h | Updated `documentation/verification_report.md` with new date and status |
| M4.2 | **Gap & conflict map refresh** | Re-survey the literature for papers published since last refresh that interact with H-Bar's 11 queries | The gap/conflict map is the paper's positioning infrastructure; it must be current | For each of Q1–Q11, run a targeted search (Semantic Scholar + arXiv) with date filter "since last refresh". Add new papers, re-classify existing ones if needed. | 4 h | Updated `gap_conflict_map.md` with 0–10 new entries; all existing entries still accurate |
| M4.3 | **Integration map verification** | Walk every row in `integration_map.md` and confirm the equation references, coupling mechanisms, and consistency status are still correct | Integration map rows go stale when equations are renumbered or sections reorganised | For each of 30 rows: find the variable's definition in `paper.md`, verify equation numbers, verify coupling description, update Consistency Verified if needed | 2 h | All 30 rows Verified = YES; any changed rows note the reason |
| M4.4 | **Bibliography hygiene** | Audit all 50+ references: update arXiv preprints to final venue versions, remove dead URLs, add DOIs, check citation counts | Outdated references are the most common reviewer complaint | For each reference: (a) search for updated venue version, (b) verify URL resolves, (c) add DOI where missing, (d) update `arxiv-submission/bibliography.bib` | 2 h | Updated `arxiv-submission/bibliography.bib`; no dead URLs |
| M4.5 | **Issue register refresh** | Review all 62 RESOLVED issues; check if any need re-opening due to recent changes | An issue that was RESOLVED may have been re-exposed by recent edits | For each issue: (a) read the fix description, (b) check current `paper.md` to confirm fix is still present, (c) if fix is missing or regression detected, re-open | 1 h | All 62 still RESOLVED (or new OPEN issues documented) |
| M4.6 | **Branch / tag management** | Create a Git tag for the current state if significant milestone reached (e.g., pre-submission, post-Kaggle) | Version tags tie paper versions to experimental results | `git tag -a v3.0.1 -m "Pre-submission: all Condition 1–5 verified, Kaggle pending"` (or appropriate message) | 10 min | Tag created |
| M4.7 | **Checkpoint reviews** | If AlphaEvolve cycle has been active, update `checkpoint_a_review.md` and `checkpoint_b_review.md` | Checkpoint reviews are the mechanism for tracking paper health across edit cycles | Re-read both checkpoint files; add new observations; update dimension scores if needed | 1 h | Both checkpoint files current |
| M4.8 | **CHANGELOG update** | Maintain a `CHANGELOG.md` at repo root summarising significant changes per month | Essential for anyone (including future self) to understand what changed when | Write entries for all significant paper edits, code changes, config changes, documentation updates | 30 min | CHANGELOG.md exists and covers the month's changes |

---

## IV. SPECIAL EVENTS (Ad-hoc)

### 4.1 New Issue Discovery (Any Time)

When a bug, gap, or opportunity is identified outside the scheduled workflow:

1. **Open new issue** — Add entry to `documentation/register.md` with status OPEN, severity, affected sections
2. **Run AlphaEvolve** — Follow `program.md` Modes 1+2: generate 5 variants, score them, apply top variant
3. **Update artifacts** — Propagate changes to `integration_map.md`, `gap_conflict_map.md`, `docs/claims-registry.md`
4. **Update checkpoint reviews** — Add note to `checkpoint_a_review.md` or `checkpoint_b_review.md`
5. **Mark RESOLVED** — Update `documentation/register.md`

### 4.2 Pre-Submission Sprint (1–2 Weeks Before Target Venue Deadline)

1. **Full reproducibility audit** (M1.1) — mandatory; must pass
2. **Proof-reading sweep** (M1.3) — mandatory; must produce zero blocking issues
3. **Full verification sweep** (M4.1) — mandatory; all 6 conditions must be PASS
4. **Bibliography hygiene** (M4.4) — mandatory; every reference must be final-venue
5. **arXiv submission** — `cd paper && make arxiv`; verify archive; upload via arXiv web interface
6. **CITATION.cff update** — ensure version, date, DOI (once assigned) are correct
7. **Post-submission** — tag commit `git tag -a v3.0-submitted -m "Submitted to [Venue] on [Date]"`

### 4.3 Post-Kaggle-Results Sprint (Triggered After June 1, 2026)

1. **Download results** — Kaggle → download CSV/JSONL for all 5 tracks
2. **Claims update** — Update C-008–C-020 from PENDING → COLLECTED or FALSIFIED in `docs/claims-registry.md`
3. **Write §12** — "Empirical Grounding" section as described in `documentation/verification_report.md` Condition 6 action
4. **Benchmark validity recomputation** — Recompute CI, FD, DG, RA with actual Kaggle results using `code/hbar/utils/metrics.py`
5. **Prediction verification** — For each of P1–P8 where Kaggle data provides an observable proxy: PASS / PARTIAL PASS / FAIL
6. **Update verification report** — Set Condition 6 from PENDING → PASS
7. **Tag version** — `git tag -a v3.0-kaggle -m "Kaggle results integrated"`
8. **Notify** — Update README.md with badge or summary of empirical validation status

---

## V. METRICS & TRACKING

| Metric | Target | How to Measure | Frequency |
|--------|--------|----------------|-----------|
| **Claims verified** | 20/20 COLLECTED or DESIGNED | `docs/claims-registry.md` status column | Monthly |
| **Verification conditions** | 6/6 PASS | `documentation/verification_report.md` | Monthly |
| **Register OPEN issues** | 0 | `documentation/register.md` | Weekly |
| **Integration map consistency** | 30/30 YES | `integration_map.md` | Monthly |
| **Gap/conflict map freshness** | No paper >90 days old unactioned | `gap_conflict_map.md` last-updated | Monthly |
| **Notebook executability** | Both notebooks run to completion | `jupyter nbconvert --to notebook --execute` | Weekly |
| **Reproducibility (clean venv)** | Metrics match committed baselines within 1e-6 | Full reproducibility audit | Monthly |
| **Bibliography currency** | 100% final-venue, 0 dead URLs | Manual spot-check of 10 random refs | Monthly |
| **Publication alerts reviewed** | 100% of alerts triaged within 1 week | `docs/alert-log.md` last-triaged | Weekly |
| **Lint cleanliness** | 0 ruff errors | `ruff check code/hbar/` | Daily |

---

## VI. QUICK-START CHEAT SHEET

```bash
# ── Daily ──────────────────────────────────────────────
source hbar_env/bin/activate
python scripts/monitor-pub.py          # D1.1
ruff check code/hbar/                  # D1.4
python -c "from hbar import *"         # D1.3
python -c "from hbar.config import load_config, merge_configs; base=load_config('experiments/configs/base.yaml'); merge_configs(base, load_config('experiments/configs/h-ptb.yaml'))"  # D4.2

# ── Weekly ──────────────────────────────────────────────
cd experiments && jupyter nbconvert --to notebook --execute h-bar-experiment.ipynb --ExecutePreprocessor.timeout=3600  # W1.1
grep '<!-- CLAIM:' paper/paper.md | sort > /tmp/anchors.txt  # W1.2
cd / && python -m pytest --tb=short                           # W4.3
pip list --outdated | grep -E "numpy|scipy|torch|datasets"    # W2.3

# ── Monthly ──────────────────────────────────────────────
# Full reproducibility audit (M1.1)
python -m venv /tmp/hbar-audit && source /tmp/hbar-audit/bin/activate
pip install -e /home/bigbasy/Documents/hbar-v3
# Run both notebooks...
# Update verification report (M4.1)

# Git tagging
git tag -a v3.0.x -m "description"     # M4.6
```

---

## VII. APPENDIX: Post-Kaggle Workflow (Detailed)

This section is the detailed execution plan for the critical path once Kaggle results are released after June 1, 2026.

**Trigger:** Kaggle announces competition results for H-PTB, H-AFB, H-MCB, H-DCB, H-STB.

### Step 1: Download and Verify (immediate)
```bash
mkdir -p kaggle_results/raw
# Download from Kaggle platform (manual or via kaggle CLI)
kaggle competitions download h-ptb -p kaggle_results/raw/
kaggle competitions download h-afb -p kaggle_results/raw/
kaggle competitions download h-mcb -p kaggle_results/raw/
kaggle competitions download h-dcb -p kaggle_results/raw/
kaggle competitions download h-stb -p kaggle_results/raw/
```

### Step 2: Parse into Structured Data
Each track yields:
- Model-wise scores on the primary metric
- Per-condition breakdown (baseline / additive / multiplicative where applicable)
- Frontier model identity

### Step 3: Claims Update Matrix

| Claim | Pre-Result Status | Expected Action if Confirmed | Expected Action if Falsified |
|-------|-------------------|------------------------------|------------------------------|
| C-008 | PENDING | Update to COLLECTED; report gap size | Update to FALSIFIED; analyse why |
| C-010–C-012 | PENDING | Update to COLLECTED; report OOD ratios | Update to FALSIFIED; revise Prediction 7 |
| C-013–C-014 | PENDING | Update to COLLECTED; report α̂_A values | Update to FALSIFIED; revise α_A ODE |
| C-015 | PENDING | Update to COLLECTED; report ζ̂_A | Update to FALSIFIED; revise self-model ODE |
| C-016–C-017 | PENDING | Update to COLLECTED; report β̂_1 and BCR | Update to FALSIFIED; revise Ξ_A structure |
| C-018–C-019 | PENDING | Update to COLLECTED; report ROI_Schema | Update to FALSIFIED; revise social cognition ODE |
| C-020 | PENDING | Update to COLLECTED; compare human vs model | Update to FALSIFIED; analyse human/model divergence |

### Step 4: Write §12

Structure:
- **§12.1** — Setup: Kaggle competitions, models evaluated, metrics
- **§12.2** — Learning track (H-PTB): results, comparison with Prediction 7
- **§12.3** — Attention track (H-AFB): results, comparison with Prediction 2
- **§12.4** — Metacognition track (H-MCB): results, comparison with Prediction 4
- **§12.5** — Executive track (H-DCB): results, comparison with Prediction 5
- **§12.6** — Social track (H-STB): results, comparison with Prediction 8
- **§12.7** — Cross-track analysis: which models show systematic σ_A signatures
- **§12.8** — Updated predictions: any revisions needed
- **§12.9** — Updated benchmark validity scores (CI, FD, DG, RA)

### Step 5: Revise Predictions (§9)

If results disconfirm any prediction, add a qualified sub-section:
> **§9.N.** *Revised Prediction N in light of Kaggle results:* [description of what was observed, what it implies for the ODE, and whether the core mechanism survives or needs modification]

### Step 6: Final Verification

1. Recompute all four validity metrics from actual results
2. Run the full 6-condition verification sweep
3. Tag: `git tag -a v3.0-empirical -m "Kaggle empirical grounding complete"`
4. Update arXiv submission with new §12

---

*End of maintenance workflow document. This file is not committed to Git (see `.gitignore`).*
