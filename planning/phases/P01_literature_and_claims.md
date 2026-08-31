# Phase P01: Literature Audit & Claim Framing

## 1. Objective
Execute systematic literature review, establish PRISMA screening flow, build knowledge graph, and define the scientific claim ledger taxonomy.

## 2. Inputs & Dependencies
- `P00` complete.
- Academic search databases (arXiv, Semantic Scholar, OpenReview).

## 3. Required Deliverables
- `literature/screening-log.csv` populated with $\ge 15$ screened studies.
- `literature/knowledge-graph.json` mapping theoretical concepts and empirical evidence.
- `planning/literature-audit.md` completed.
- `planning/ledger.md` initialized with initial hypotheses (`C-01` through `C-05`).

## 4. Exit Criteria & Definition of Done
- Zero uncited claims in foundational theory sections.
- All literature screening records classified according to PRISMA standards.
- `python scripts/check_phase_exit.py P01` returns `PASS`.
