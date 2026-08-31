# Phase P09: Hostile Red-Team Review & Statistical Audit

## 1. Objective
Subject the manuscript and codebase to adversarial review across 4 hostile reviewer personas (Methods/Stats, Ethics, Domain Expert, Reviewer 2).

## 2. Inputs & Dependencies
- `P08` manuscript draft complete.

## 3. Required Deliverables
- Persona review reports compiled under `experiments/redteam-audits/`.
- Statistical power, data leakage, and claim bound stress tests.
- Remediation patches applied to manuscript and codebase.

## 4. Exit Criteria & Definition of Done
- All identified fatal flaws resolved.
- Overclaim scanner returns zero critical violations.
- `python scripts/check_phase_exit.py P09` returns `PASS`.
