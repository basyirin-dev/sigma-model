# Phase 07 — Analysis, Diagnostics, Order-Parameter Extraction & Figures

**RPF v2.0:** Git tag `p07-analysis-done` · Duration 3–5d · GPU 8 · RACI: Agent **R** / PI **A** (interpretation) · Abort: primary analysis contradicts gate result → halt · Acceptance: 5 publication figures with metadata sidecars + alt text + colorblind-safe (CC.3.4–3.6), sensitivity section, statistical tests with correction, ledger predictions resolved · **STATUS: 🔄 ACTIVE (Analysis & Figure Generation In Progress)**

**Phase ID:** P07  
**Phase Title:** Representation Geometry Diagnostics, Empirical Bifurcation Fitting, Hessian Dynamics & Figure Generation  
**Status:** **ACTIVE (Authorized)**  
**Duration:** 2–3 Days  
**Dependencies:** P06  
**Executor:** Agent (90%) / Human-Gate (10%)  
**Deliverables:** `paper/writing/figures/`, `paper/writing/results_draft.md`, `paper/decisions/ADR-007_analysis_outcomes.md`

---

## 1. Purpose & Scope
Perform rigorous statistical and geometric analysis across the generated dataset. Fit the empirical phase boundary $\hat{\lambda}_{\text{crit}}$, compute Granger causality on representation geometry (CKA), evaluate Hessian spectral trajectories, resolve all predicted observables in `planning/ledger.md`, and produce publication-grade vector figures.

---

## 2. Exhaustive Tasks & Subtasks

### Task 7.1: Empirical Phase Boundary & Separatrix Fitting
1. **Fit Step-Function Logistic Change-Point Model:**
   - Fit $P(\text{escape} \mid \lambda) = \frac{1}{1 + \exp(-k(\lambda - \lambda_{\text{crit}}))}$ via non-linear least squares.
   - Extract empirical critical threshold $\hat{\lambda}_{\text{crit}}$ and steepness parameter $k$.
   - Compute non-parametric 95% bootstrap confidence intervals (10,000 resamples).
2. **Late-Onset Separatrix Heatmap:**
   - Construct 2D heatmap matrix $P(\text{escape} \mid \lambda, t_{\text{int}})$ over the $(\lambda, t_{\text{int}})$ plane.
   - Interpolate empirical boundary and overlay the theoretical continuous-flow separatrix from Phase 02.
3. **Segmented Regression & Latency Extraction:**
   - Fit segmented linear regression $y(t) = \beta_0 + \beta_1 t + \beta_2 (t - \tau)_+$ to extract inflection time $\hat{\tau}(\lambda)$ across all conditions.

### Task 7.2: Representation Geometry Diagnostics (CKA / RGA)
1. **Layerwise CKA Trajectory Analysis:**
   - Track CKA similarity between model intermediate representations and structural equivalence matrices across all 2000 steps.
   - Measure CKA half-rise time $t_{\text{CKA}, 50\%}$ vs. OOD accuracy half-rise time $t_{\text{OOD}, 50\%}$.
2. **Granger Lead-Lag Causality Test:**
   - Estimate dynamic partial correlation regression:
     $$\text{OOD}_{t+1} = \alpha_0 + \alpha_1 \text{OOD}_t + \alpha_2 \text{Loss}_t + \alpha_3 \|\theta\|_t + \beta \text{CKA}_t + \epsilon_t$$
   - Evaluate one-sided $t$-test on $\beta > 0$ to confirm that representation geometry statistically leads OOD recovery.
3. **Whitened GCA vs. Raw GCA Verification:**
   - Verify that whitened GCA starts at $\approx 0.0$ at step 0 and rises concurrently with structural exposure, resolving the Paper 01 artifact.

### Task 7.3: Hessian Spectral Dynamics (PyHessian)
1. **Track Top Eigenvalue Trajectory $\lambda_{\text{max}}(H_t)$:**
   - Evaluate whether supercritical structural pressure modifies the Edge of Stability (EOS) ceiling ($2/\eta$).
   - Contrast Hessian sharpness dynamics in the shortcut state $E_S$ vs. the coherent state $E_C$.

### Task 7.4: Publication-Quality Figure Assembly (`paper/writing/figures/`)
Generate 5 publication-ready figures in TikZ / PGFPlots and high-resolution PNG:
1. **Figure 1 (Theoretical Phase Portrait):**
   - Stream plot of the two-subspace system $(\dot{u}, \dot{v})$ showing $E_S$ stability for $\lambda < \lambda_{\text{crit}}$ and transcritical bifurcation to $E_C$ for $\lambda > \lambda_{\text{crit}}$.
2. **Figure 2 (Empirical Phase Boundary & Escape Step Function):**
   - Subplot A: Sigmoid transition probability $P(\text{escape} \mid \lambda)$ with 95% bootstrap bands and fitted $\hat{\lambda}_{\text{crit}}$.
   - Subplot B: 2D heatmap over $(\lambda, t_{\text{int}})$ showing the late-onset recovery separatrix.
3. **Figure 3 (Representation Geometry & CKA Trajectories):**
   - CKA trajectory flows across subcritical vs. supercritical arms, illustrating rapid geometric alignment.
4. **Figure 4 (Cross-Benchmark Generalization):**
   - Side-by-side OOD recovery curves across H-Bar, SCAN (`add_primitive`, `length_split`), COGS, and PCFG-SET.
5. **Figure 5 (Hessian Spectral Density & Sharpness):**
   - Lanczos spectral density distributions comparing $E_S$ vs. $E_C$ basins.

### Task 7.5: Resolve Claims Ledger & Draft Results Narrative
1. Update `paper/planning/ledger.md` marking CLM-001 through CLM-007 as `confirmed / refuted`.
2. Write comprehensive `paper/writing/results_draft.md` summarizing all statistical findings.

---

## 3. Human Gates
- `[HUMAN-GATE]` Principal Investigator reviews all 5 generated publication figures and approves statistical conclusions.

---

## 4. Machine-Checkable Exit Criteria
- [ ] All analysis scripts in `paper/src/analysis/` run to completion with exit code 0.
- [ ] 5 publication figures generated in `paper/writing/figures/` with complete captions (CC.3.2).
- [ ] Granger causality test confirms $\beta > 0$ with $p < 0.05$.
- [ ] `paper/writing/results_draft.md` committed.
- [ ] `[HUMAN-GATE]` Scientific interpretation approved.

---

## 5. Deliverables & Artifacts
- Publication figures: `paper/writing/figures/figure1_phase_portrait.pdf`, `figure2_bifurcation_boundary.pdf`, etc.
- Results text draft: `paper/writing/results_draft.md`
- Updated ledger: `paper/planning/ledger.md`
