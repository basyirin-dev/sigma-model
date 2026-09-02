# Phase 03 — GATE: Central Hypothesis & Separatrix Validation (RPF v2.0)

> **THE CENTRAL MECHANISM GATE:** This phase empirically tests the riskiest theoretical assumption of Paper 02. The outcome legally binds all downstream phases. No writing (P08) or large-scale multi-benchmark sweep (P06) is permitted until `gate-result.md` is committed with a verified **PASS** and a `[HUMAN-GATE]` PROCEED directive.

| Field | Value |
|-------|-------|
| Phase ID | P03 |
| Tasks / Subtasks | 7 / 10 |
| Duration | 2–3 days |
| Compute | 2 GPU hrs (bounded; abort at 2×) |
| Git tag on close | `p03-gate-passed` / `p03-gate-failed` / `p03-gate-inconclusive` |
| Abort threshold | Compute > 2× budget → halt; primary-metric p > α with effect < minimum → FAIL |
| Status | 🔶 In progress — Tasks 3.1–3.2 complete; 450-run grid + evaluation (3.3–3.4) pending |
| Dependencies | P02 (ADR-003 hypothesis), **P02.5 (`planning/preregistration.md`)** |
| Deliverables | `planning/gate-result.md`, `experiments/YYYY-MM-DD_gate/`, `decisions/human-gates/P03_gate_directive.md` |

**RACI:** Design gate — Agent **R** / PI C · Implement & run — Agent **R** / PI I · Evaluate vs. pre-registered criteria — Agent **R** / PI I · PROCEED / RE-GATE / ABORT — PI **A**.

---

## 1. Purpose & Scope
Execute the minimum viable high-signal empirical experiment to validate whether deep neural network training undergoes a sharp supercritical bifurcation with an identifiable separatrix at $\lambda_{\text{crit}}$, or whether OOD recovery is merely a smooth, continuous dose-response curve. **All evaluation is scored against the P02.5 pre-registration (`planning/preregistration.md`) — criteria fixed before evaluation.**

---

## 2. Exhaustive Tasks & Subtasks

### Task 3.0: Power / Effect-Size Check [COMPLETE — see preregistration §5]
Verify the planned grid (n = 30 seeds/cell) has sufficient resolution or document the effect-size justification. Logged in `planning/preregistration.md` §5 (escape-fraction estimator SE ≤ 0.091 resolves the required p < 0.05 / p > 0.95 separation).

### Task 3.1: Minimal Gate Experiment Design [COMPLETE]
1. **Model & Benchmark Specifications:**
   - Architecture: 2-layer standard seq2seq Transformer ($d_{\text{model}} = 128, n_{\text{heads}} = 4, d_{\text{ff}} = 512, n_{\text{layers}} = 2$). Implemented in `paper/src/models/seq2seq_transformer.py`.
   - Grammar: H-Bar zero-leakage compositional dataset ($N_{\text{train}} = 10,000, N_{\text{OOD}} = 2,000$). Implemented in `paper/src/data/hbar_dataset.py`.
   - Optimizer: Adam ($\eta = 10^{-3}, \beta = (0.9, 0.999), \text{clip} = 1.0$), batch size 64, 2000 steps.
2. **Experimental Grid Parameters ($n = 30$ seeds per cell):**
   - **Arm A (Dense $\lambda$-Sweep, Step 0 Onset):** $\lambda \in \{0.00, 0.05, 0.10, 0.20, 0.30, 0.50, 0.75, 1.00, 1.50, 2.00\}$ — 300 runs.
   - **Arm B (Late-Onset Intervention Grid, $\lambda = 1.0$):** $t_{\text{int}} \in \{0, 100, 250, 500, 1000 \text{ steps}\}$ — 150 runs.
   - *Total Gate Runs:* 450 runs (configured in `paper/experiments/configs/gate_protocol.yaml`).

### Task 3.2: Self-Contained Gate Runner Implementation [COMPLETE]
1. [x] Write self-contained execution harness: `paper/src/experiments/run_gate.py`.
2. [x] Pin all random seeds deterministically (`seed = run_id * 42 + 7`).
3. [x] Log per-run metrics every 25 steps: `step`, `loss_train`, `loss_comp`, `acc_id`, `acc_ood`, `cka_rga`, `param_norm`.
4. [x] Implement automatic output serialization to `paper/experiments/YYYY-MM-DD_gate/all_results.pkl`.
5. [ ] **Manifest per run (CC.1.4):** emit `manifest.yaml` (config hash, seed provenance, hardware, env versions, data/output hashes, numerical sanity) for the full grid — *pending at grid execution*.
6. [ ] **Numerical sanity checks (CC.2.6):** NaN/Inf screening, convergence monitoring, residual norms — *pending at grid execution*.

### Task 3.3: Pre-Registered Decision Criteria (Evaluation Rules) [FIXED — see preregistration.md]
Evaluate data against the three non-negotiable quantitative criteria pre-registered in `planning/preregistration.md`:
1. **Criterion 1 — Sharp Step-Function Escape ($P(\text{escape} \mid \lambda)$):** escape := $\text{Acc}_{\text{OOD}} \ge 80\%$; fit 2-parameter logistic $P(\text{escape} \mid \lambda) = \frac{1}{1 + \exp(-k(\lambda - \lambda_{\text{crit}}))}$; **PASS** iff $k \ge 15.0$ and $P(\text{escape} \mid \lambda \le 0.10) < 0.05$ and $P(\text{escape} \mid \lambda \ge 0.50) > 0.95$.
2. **Criterion 2 — Late-Onset Destabilization of $E_S$:** for $t_{\text{int}} = 1000$ (trapped at step 1000, $\text{Acc}_{\text{OOD}} \le 50\%$), turning on $\lambda = 1.0$ must achieve final $\text{Acc}_{\text{OOD}} \ge 90\%$ in $\ge 90\%$ of seeds.
3. **Criterion 3 — Supercritical Asymptotic Equivalence:** pairwise TOST equivalence between all supercritical arms ($\lambda \in \{0.5, 0.75, 1.0, 1.5, 2.0\}$) within margin $\pm 2.5\%$ ($p < 0.05$, Bonferroni per preregistration §5).

### Task 3.4: Gate Verdict & Binding Decision Emission
1. Execute analysis script: `paper/src/analysis/analyze_gate.py`.
2. Compile and emit `paper/planning/gate-result.md`:
   - Explicit verdict: **PASS / FAIL / INCONCLUSIVE** (mandatory fields per RPF v2.0 §VI).
   - Tabulate raw per-seed distributions, 95 % bootstrap CIs, Welch $t$-tests, and TOST $p$-values.
   - Formulate binding constraints for Phase 04+ (e.g., locking $\hat{\lambda}_{\text{crit}} \in [0.20, 0.35]$).
3. Resolve all `decide-at-P03` ledger rows (CLM-003/004/005) and auto-flag dependents per the dependency graph.
4. Emit `decisions/human-gates/P03_gate_directive.md` for the PI directive.

### Task 3.5: Verdict Logic
- **PASS:** primary metric meets threshold; secondary metrics consistent → unlock P04.
- **FAIL:** primary metric unmet → halt; no downstream work; return to P02 or terminate (commit `p03-gate-failed`).
- **INCONCLUSIVE:** primary metric within the pre-specified ambiguity band ($k \in [10, 15)$ with ≥ 1 separation inequality violated by < 2 SE) → **trigger P03.1 sub-gate** (`phases/P03.1_subgate.md`; ≤3 runs, distinct seeds, ≤1 GPU hr, binary ≥2/3 rule). No open-ended iteration.

---

## 3. Human Gates
- `[HUMAN-GATE]` Principal Investigator reads `planning/gate-result.md` and issues one of three binding directives (PROCEED / RE-GATE / ABORT). SLA: 48h; reminder 24h; fallback at 48h = **RE-GATE** (conservative). Record: `decisions/human-gates/P03_gate_directive.md`; agent state serialized to `experiments/agent-state/P03_checkpoint.json`.

---

## 4. Machine-Checkable Exit Criteria
- [ ] 450 gate runs completed with 0 errors and 0 NaNs (excluded runs logged `NEGATIVE` per CC.4.7).
- [ ] Per-run manifests valid per the RPF v2.0 schema (CC.1.4).
- [ ] Numerical sanity checks pass for all runs (CC.2.6).
- [ ] `planning/gate-result.md` committed with mandatory fields and explicit verdict.
- [ ] All 3 pre-registered criteria numerically evaluated against `planning/preregistration.md`.
- [ ] Ledger `decide-at-P03` rows resolved; dependency graph flags propagated.
- [ ] `decisions/human-gates/P03_gate_directive.md` committed.
- [ ] `[HUMAN-GATE]` PROCEED directive signed off.

---

## 5. Deliverables & Artifacts
- Decision record (Design): `paper/decisions/ADR-005_gate_experimental_design.md`
- Pre-registration: `paper/planning/preregistration.md`
- Protocol configuration: `paper/experiments/configs/gate_protocol.yaml`
- Model & data modules: `paper/src/models/seq2seq_transformer.py`, `paper/src/data/hbar_dataset.py`
- Runner script: `paper/src/experiments/run_gate.py`
- Raw data bundle: `paper/experiments/YYYY-MM-DD_gate/all_results.pkl` (+ manifests)
- Gate document: `paper/planning/gate-result.md`
- Directive record: `paper/decisions/human-gates/P03_gate_directive.md`

## 6. Phase-Transition Checklist
- [ ] Git tag: `p03-gate-passed` / `p03-gate-failed` / `p03-gate-inconclusive`
- [ ] Gate result committed; ledger `decide-at-P03` rows resolved; dependency graph updated
- [ ] If PASS: commit `[P03][Gate][INIT] Gate PASSED: <primary_metric> = <value>`; if FAIL: same + `NEGATIVE` tag; if INCONCLUSIVE: `[P03][Gate][INIT] Gate INCONCLUSIVE: triggering P03.1`
