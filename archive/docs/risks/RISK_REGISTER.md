# Σ-Model V3.0+ — Protein Experiments Risk Register

> **Status**: Phase 0 — initial
> **Last reviewed**: Jul 2026
> **Review cadence**: Monthly or when a phase gate is crossed

---

## How to Use This Document

Each risk is assigned a unique ID (R-001, R-002, ...) and tracked through its lifecycle. Risks are reviewed during phase transitions. When a risk materializes, it becomes an _issue_ and is moved to the Open Issues section with a remediation plan.

---

## Risk Table

| ID | Risk | Likelihood | Impact | Category | Mitigation | Monitor | Status |
|----|------|-----------|--------|----------|-----------|---------|--------|
| R-001 | Protein domain recombination may not exhibit compositional gap (null H1) — result still publishable | Medium | Medium | Scientific | Low-σ baseline already shows ΔCG in prior work; null result shifts focus to probe experiments | E1 (brittle) results after 30 runs | Open |
| R-002 | PLMs already encode domain grammar (null H2) — can refine probes or publish informative null | Medium | Medium | Scientific | Probe battery tests 3 distinct grammar types; partial evidence is informative | Probe accuracy curves | Open |
| R-003 | Computational cost of N=500 exceeds Kaggle GPU limits — low likelihood, pre-tested on T4 | Low | High | Technical | Pre-test on 50-run pilot; fallback to 3× 167-run shards across multiple GPU sessions | Kaggle runtime logs | Open |
| R-004 | JAIR paper not accepted before NeurIPS deadline — arXiv preprint sufficient for citations | Low | Medium | Timeline | Submit to arXiv 2 weeks before NeurIPS deadline; update camera-ready if accepted | JAIR review status | Open |
| R-005 | ESM-2 training data overlaps with Pfam 38.2 sequences — conservative bias (if anything, inflates baseline) | Low | Low | Validity | Document overlap explicitly; conservative bias means effect size estimate is lower bound | Sequence alignment overlap % | Open |
| R-006 | PfamCG-1.0 splits don't correlate with known biology — must validate before claiming benchmark validity | Medium | High | Validity | Validate against clan annotations and SCOP fold taxonomy before primary analysis | Clan enrichment p-values | Open |

---

## Risk Categories

| Category | Count | IDs |
|----------|-------|-----|
| Scientific | 2 | R-001, R-002 |
| Technical | 1 | R-003 |
| Timeline | 1 | R-004 |
| Validity | 2 | R-005, R-006 |

---

## Open Issues (Materialized Risks)

None yet. This section populated when a risk becomes an active issue.

---

## Review Log

| Date | Reviewed By | Notes |
|------|-------------|-------|
| Jul 2026 | Initial | Created during protein experiments infrastructure setup |
