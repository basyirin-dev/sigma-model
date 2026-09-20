# Original User Request

## 2026-09-19T16:11:53Z

<USER_REQUEST>
Execute Phase 0 of the manuscript remediation plan: conduct an exhaustive numerical, logical, and bibliographic audit of all 17 checkable defects identified in §7.2 of the peer review (the full text of the peer review is available at `/home/bigbasy/Documents/sigma-model/.agents/PEER_REVIEW.md`), reconcile all derived tables against raw per-seed logs, correct theoretical and statistical inconsistencies, and establish a turnkey single-command verification pipeline for the defining manuscript.

Working directory: /home/bigbasy/Documents/sigma-model
Integrity mode: development
Reference Document: `/home/bigbasy/Documents/sigma-model/.agents/PEER_REVIEW.md`

## Requirements

### R1. Hard-Error Numerical & Statistical Audit (§7.2 Items 1–4, 7–16)
Audit and reconcile every numerical and statistical quantity flagged in Section 7.2 of the peer review against raw per-seed experimental logs:
1. Recompute information criteria (AIC/BIC) and log-likelihoods for change-point model selection under exact formulas ($2k - 2\ln\mathcal{L}$ for seed Bernoulli MLE; $n\ln(\text{RSS}/n) + 2k$ for aggregate proportions); transparently report that continuous sigmoidal forms (Logistic, Probit, Gompertz) are statistically indistinguishable ($\Delta\text{AIC} < 0.3$), reject Piecewise-Linear on seed likelihood, and justify the logistic model on normal-form grounds.
2. Reconcile Intent-to-Treat (ITT) standard deviations and Welch $t$-test / FDR adjusted $p$-values across all cells in Table 8 / Table 9 so that bimodal mixture variance and within-subcohort variances strictly agree with raw seed data.
3. Standardize the $\hbar$ ERM baseline accuracy across all sections and tables to eliminate inconsistent figures (reconciling the 63.3%, 45.9%, 34.7%, and 34.2% citations).
4. Transparently report pre-registered Criterion 1 outcomes ($P(\text{escape} \mid \lambda \le 0.010)$ vs observed escape at $\lambda = 0$).
5. Reconcile cross-table and figure discrepancies (Table 1 vs Table 4 vs Figure 4; PCFG-SET baseline in Table 2 vs Table 4; Table 7 run accounting distinguishing the 960 core production runs from sub-studies; GRU encoder parameter counts; participation ratio calculation $\ge 2.29$; and degrees of freedom for bivariate VAR Granger causality tests).

### R2. Theoretical Consistency & Kramers Decommissioning (§7.2 Items 5, 6; §7.3)
Resolve theoretical inconsistencies between posited ODE formulations and empirical observations:
1. Excise speculative Kramers barrier arguments and ungrounded potential energy formulations ($V(v) = -\frac{1}{2}\mu_{\perp} v^2 + \frac{1}{3}\kappa v^3$) from Appendix B.7; reframe subcritical escape as stochastic finite-sample fluctuations without invoking nonexistent potential barriers.
2. Reconcile the theoretical fixed point $v^* = (\lambda - \lambda_c)/\kappa$ with the empirical operationalization and escape criterion ($v > 0.5$).

### R3. Turnkey Single-Command Table Regeneration & Log Verification
Implement and verify a turnkey reproduction script (e.g. expanding `paper/src/data/derive_processed_tables.py` or providing `scripts/verify_audit_reproducibility.py`):
1. Programmatically regenerate all 17 processed CSV tables and figure data tables directly from raw per-seed run logs.
2. Validate that every number, mean, standard deviation, and test statistic reported in the manuscript tables is bit-for-bit identical to the derived data tables.

### R4. Manuscript, Bibliography & Repository Asset Alignment
1. Update `paper/writing/manuscript.tex` to incorporate all corrected statistics, tables, and rescoped theoretical narratives.
2. Audit `paper/writing/bibliography.bib` and correct misattributed or inaccurate citations identified in §7.2 Item 17 (Kim & Linzen 2020, Hupkes et al. 2020, Wu et al. 2023, Merrill et al., Nakkiran et al., Ghorbani / Yao).
3. Ensure all repository links and references consistently point to `https://github.com/basyirin-dev/sigma-model` and confirm submission bundles (`paper/supplementary_materials.zip`, `paper/arxiv_bundle.tar.gz`) are fully synchronized.

## Verification Resources
- Existing test suites: `make test` / `pytest tests/ paper/tests/`
- Table derivation engine: `python -m paper.src.data.derive_processed_tables`
- Compilation suite: `make paper` (from root) or `make pdf` (from `paper/`)

## Acceptance Criteria

### Audit & Statistical Invariants
- [ ] All 17 items from Review §7.2 are audited and formally resolved with verifiable proofs or calculations.
- [ ] Model selection statistics in Table 9 / Table 10 correctly reflect log-likelihoods, AIC, and BIC without sign reversals or log-likelihood ceiling violations.
- [ ] ITT standard deviations, mixture variances, and Welch $t$-test values in Table 8 / Table 9 match raw seed calculations ($n=30$ per cell).
- [ ] Bivariate VAR Granger causality $F$-test reporting specifies correct test degrees of freedom and corresponding $p$-values.
- [ ] Appendix B.7 contains no ungrounded Kramers escape barrier claims.
- [ ] Participation ratio arithmetic in §3.2 mathematically agrees with reported principal component percentages ($\ge 2.29$).
- [ ] Recurrent model parameter counts in Appendix D.4 reflect actual architecture dimensions.
- [ ] Run inventory in Table 7 transparently accounts for all runs (distinguishing core 960 production runs from sub-studies).
- [ ] Bibliography citations flagged in §7.2 Item 17 are verified and accurately cited.

### Automated Pipelines & Build Health
- [ ] Turnkey table derivation script executes without error and regenerates all CSV tables from raw logs.
- [ ] Dedicated automated audit script verifies that all numbers in LaTeX tables match regenerated CSV tables with 0 unresolved discrepancies.
- [ ] All unit and integration tests pass via `make test` (`pytest tests/ paper/tests/`).
- [ ] `make paper` (or `make -C paper pdf`) compiles the defining manuscript cleanly with zero undefined references or citations.
</USER_REQUEST>
