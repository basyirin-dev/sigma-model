# Screening Data Structure — Phase 4 Ready

**Purpose:** CC.4.2 compliance — screening data structure prepared for Phase 4 (Deduplication and Title/Abstract Screening)

## Directory Layout

```
screening-data/
├── README.md                  ← this file
├── records-to-screen.csv      ← (pending — generated in Phase 4 after dedup)
├── screened-in/               ← records passing title/abstract screening
│   └── (empty — populated in Phase 4)
├── screened-out/              ← records failing title/abstract screening
│   └── (empty — populated in Phase 4)
└── full-text/                 ← records proceeding to full-text review
    └── (empty — populated in Phase 5)
```

## Source Data

Raw exports are stored in `research/search-results/`:
- `scopus-prim-2026-07-29.ris` (411 records)
- `scopus-safety-2026-07-29.ris` (160 records)
- `scopus-sec-2026-07-29.ris` (71 records)
- `wos-2026-07-29.ris` (208 records)
- `wos-safety-2026-07-29.ris` (84 records)
- `acm-2026-07-29.enw` (166 records)
- `ieee-2026-07-29-part1.ris` (100 records)
- `ieee-2026-07-29-part2.ris` (36 records)
- `arxiv-primary-2026-07-29.json` (200 records)
- `arxiv-safety-2026-07-29.json` (200 records)
- `arxiv-benchmark-2026-07-29.json` (72 records)
- `arxiv-broad-2026-07-29.json` (146 records)

Automated library (academic-research-mcp, ID: 0981e757): **632 unique records** for screening.

## Next Steps (Phase 4)

1. Import all RIS/BibTeX files into Zotero reference manager
2. Run deduplication (automatic + manual)
3. Export the deduplicated list as CSV → `records-to-screen.csv`
4. Begin title/abstract screening using the screening framework (`research/screening-decisions/screening-framework.md`)
