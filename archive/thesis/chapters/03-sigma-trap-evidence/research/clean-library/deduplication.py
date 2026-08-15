#!/usr/bin/env python3
"""
Paper 02 — Phase 4: Deduplication & Reference Management

Parses all search result files (RIS, ENW, JSON), merges with the
existing review library (632 unique records from automated searches),
deduplicates (DOI > arXiv ID > title), tags by source database,
and exports as .bib, .csv, and .ris.

Outputs:
  - research/clean-library/paper02-library.bib    (BibTeX)
  - research/clean-library/paper02-library.csv     (CSV with screening columns)
  - research/clean-library/paper02-library.ris     (RIS for screening tools)
  - research/clean-library/paper02-screening.csv   (CSV with decision columns)
  - research/clean-library/deduplication-report.md (stats)
"""

import csv, json, os, re, sys, logging
from collections import defaultdict
from pathlib import Path
from typing import Any

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

BASE = Path(__file__).resolve().parent.parent.parent  # .../02-systematic-review/
RESULTS = BASE / "research" / "search-results"
OUT = BASE / "research" / "clean-library"
OUT.mkdir(parents=True, exist_ok=True)


# ── Record model ──────────────────────────────────────────────────────

class Record(dict):
    """Unified paper record."""

    def dedup_key(self):
        doi = self.get("doi", "").strip().lower()
        if doi and doi != "none":
            return ("doi", doi)
        aid = self.get("arxiv_id", "").strip().lower()
        if aid:
            return ("arxiv", aid)
        title = self.get("title", "").strip().lower()
        title = re.sub(r"[^a-z0-9\s]", "", title)
        title = re.sub(r"\s+", " ", title).strip()
        if title and len(title) > 10:
            return ("title", title)
        return None


# ── Parsers ───────────────────────────────────────────────────────────

def parse_ris(path: Path, source_tag: str) -> list[Record]:
    records, current = [], None
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n\r")
            if line.startswith("ER  -"):
                if current:
                    records.append(current)
                current = None
                continue
            if not current:
                current = Record()
            tag, val = line[:2], line[6:].strip() if len(line) > 6 else ""
            if tag == "TY": current["type"] = val
            elif tag == "TI": current["title"] = val
            elif tag == "AU": current.setdefault("authors", []).append(val)
            elif tag == "PY":
                m = re.match(r"(\d{4})", val)
                if m: current["year"] = int(m.group(1))
            elif tag == "DO": current["doi"] = val
            elif tag == "UR": current["url"] = val
            elif tag == "AB": current["abstract"] = val
            elif tag == "KW": current.setdefault("keywords", []).append(val)
            elif tag == "T2": current["journal"] = val
            elif tag == "PB": current["publisher"] = val
    for r in records:
        r["source_db"] = source_tag
        r["source_file"] = path.name
        url = r.get("url", "")
        m = re.search(r"arxiv\.org/(?:abs|pdf)/(\d+\.\d+)", url)
        if m and not r.get("arxiv_id"):
            r["arxiv_id"] = m.group(1)
    return records


def parse_enw(path: Path, source_tag: str) -> list[Record]:
    records, current = [], None
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n\r")
            if not line.strip():
                continue
            tag, val = line[:2], line[3:].strip() if len(line) > 3 else ""
            if tag == "%0":
                if current: records.append(current)
                current = Record()
                current["type"] = val
                continue
            if current is None: current = Record()
            if tag == "%T": current["title"] = val
            elif tag == "%A": current.setdefault("authors", []).append(val)
            elif tag == "%D":
                m = re.match(r"(\d{4})", val)
                if m: current["year"] = int(m.group(1))
            elif tag == "%R": current["doi"] = val
            elif tag == "%U": current["url"] = val
            elif tag == "%I": current["publisher"] = val
            elif tag == "%B": current["journal"] = val
            elif tag == "%K": current.setdefault("keywords", []).append(val)
    if current: records.append(current)
    for r in records:
        r["source_db"] = source_tag
        r["source_file"] = path.name
    return records


def parse_arxiv_json(path: Path, source_tag: str) -> list[Record]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    records = []
    for entry in data.get("entries", []):
        r = Record()
        r["title"] = entry.get("title", "")
        r["arxiv_id"] = entry.get("arxiv_id", "")
        r["abstract"] = entry.get("abstract", "")
        r["url"] = entry.get("arxiv_url", "")
        r["authors"] = entry.get("authors", [])
        r["source_db"] = source_tag
        r["source_file"] = path.name
        pub = entry.get("published", "")
        m = re.match(r"(\d{4})", pub)
        if m: r["year"] = int(m.group(1))
        cats = entry.get("categories", [])
        if cats: r["keywords"] = [f"arxiv:{c}" for c in cats]
        records.append(r)
    return records


# ── Source mapping ────────────────────────────────────────────────────

SOURCE_MAP = {
    "scopus-prim-2026-07-29.ris":     ("Scopus", "primary"),
    "scopus-safety-2026-07-29.ris":   ("Scopus", "safety"),
    "scopus-sec-2026-07-29.ris":      ("Scopus", "secondary"),
    "wos-2026-07-29.ris":             ("WoS", "primary"),
    "wos-safety-2026-07-29.ris":      ("WoS", "safety"),
    "acm-2026-07-29.enw":             ("ACM", "F2"),
    "ieee-2026-07-29-part1.ris":      ("IEEE", "part1"),
    "ieee-2026-07-29-part2.ris":      ("IEEE", "part2"),
    "arxiv-primary-2026-07-29.json":  ("arXiv", "primary"),
    "arxiv-safety-2026-07-29.json":   ("arXiv", "safety"),
    "arxiv-benchmark-2026-07-29.json":("arXiv", "benchmark"),
    "arxiv-broad-2026-07-29.json":    ("arXiv", "broad"),
}


# ── Deduplication ─────────────────────────────────────────────────────

def deduplicate(records: list[Record]) -> tuple[list[Record], dict]:
    """Deduplicate by DOI > arXiv ID > title. Returns (unique, stats)."""
    key_doi, key_arxiv, key_title = {}, {}, {}
    conflicts = {"doi": 0, "arxiv": 0, "title": 0}

    for rec in records:
        k = rec.dedup_key()
        if k is None:
            continue
        kind, key = k
        pool = {"doi": key_doi, "arxiv": key_arxiv, "title": key_title}
        if key in pool[kind]:
            conflicts[kind] += 1
            existing = pool[kind][key]
            existing["source_db"] = _merge_sources(existing["source_db"], rec["source_db"])
        else:
            pool[kind][key] = rec

    # Build unique list: DOI first (best quality), then arXiv, then title
    result = []
    seen_titles = set()
    for pool in [key_doi, key_arxiv, key_title]:
        for k, rec in pool.items():
            dk = rec.dedup_key()
            if dk and dk[0] in ("doi", "arxiv"):
                result.append(rec)
            elif dk and dk[1] not in seen_titles:
                seen_titles.add(dk[1])
                result.append(rec)

    stats = {
        "total_raw": len(records),
        "unique": len(result),
        "doi_unique": len(key_doi),
        "arxiv_unique": len(key_arxiv),
        "title_unique": len(key_title),
        "doi_conflicts": conflicts["doi"],
        "arxiv_conflicts": conflicts["arxiv"],
        "title_conflicts": conflicts["title"],
    }
    return result, stats


def _merge_sources(existing, new):
    if not existing: return new
    if not new: return existing
    parts = set(existing.split(", "))
    parts.update(new.split(", "))
    return ", ".join(sorted(parts))


def _field_present(r: Record, field: str) -> bool:
    val = r.get(field, "")
    if isinstance(val, list):
        return len(val) > 0 and any(v.strip() for v in val)
    return bool(val and str(val).strip())
    if not existing: return new
    if not new: return existing
    parts = set(existing.split(", "))
    parts.update(new.split(", "))
    return ", ".join(sorted(parts))


# ── Exports ────────────────────────────────────────────────────────────

def export_bibtex(records: list[Record], path: Path):
    bibtype_map = {"JOUR": "article", "CONF": "inproceedings",
                   "Conference Paper": "inproceedings", "Journal Article": "article", "Article": "article"}
    with open(path, "w", encoding="utf-8") as f:
        for i, rec in enumerate(records):
            bibtype = bibtype_map.get(rec.get("type", ""), "misc")
            citekey = f"P02_{i+1:04d}"
            if rec.get("doi"):
                short = re.sub(r"[^a-zA-Z0-9]", "", rec["doi"][:20])
                if short: citekey = short[:30]
            f.write(f"@{bibtype}{{{citekey},\n")
            _bf(f, "title", rec.get("title", ""), True)
            _bf(f, "author", " and ".join(rec.get("authors", [])) if isinstance(rec.get("authors"), list) else rec.get("authors", ""))
            _bf(f, "year", str(rec.get("year", "")))
            _bf(f, "doi", rec.get("doi", ""))
            _bf(f, "url", rec.get("url", ""))
            _bf(f, "journal", rec.get("journal", ""))
            _bf(f, "publisher", rec.get("publisher", ""))
            _bf(f, "abstract", rec.get("abstract", ""), True)
            _bf(f, "keywords", ", ".join(rec.get("keywords", [])) if isinstance(rec.get("keywords"), list) else rec.get("keywords", ""))
            _bf(f, "source-db", rec.get("source_db", ""))
            f.write("}\n\n")


def _bf(f, name, value, is_long=False):
    if not value: return
    value = value.replace("&", "\\&").replace("%", "\\%")
    if is_long and len(value) > 80:
        f.write(f"  {name} = {{\n    {value}\n  }},\n")
    else:
        f.write(f"  {name} = {{{value}}},\n")


def export_csv(records: list[Record], path: Path):
    fields = ["id", "title", "authors", "year", "doi", "arxiv_id", "url",
              "journal", "abstract", "keywords", "source_db", "source_file"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for i, rec in enumerate(records):
            row = dict(rec)
            row["id"] = f"P02_{i+1:04d}"
            if isinstance(row.get("authors"), list): row["authors"] = "; ".join(row["authors"])
            if isinstance(row.get("keywords"), list): row["keywords"] = "; ".join(row["keywords"])
            w.writerow(row)


def export_ris(records: list[Record], path: Path):
    """Export as RIS format for screening tools like Rayyan/Covidence."""
    type_map = {"JOUR": "JOUR", "CONF": "CONF", "inproceedings": "CONF",
                "article": "JOUR", "misc": "JOUR"}
    with open(path, "w", encoding="utf-8") as f:
        for i, rec in enumerate(records):
            rtype = type_map.get(rec.get("type", ""), "JOUR")
            f.write(f"TY  - {rtype}\n")
            f.write(f"TI  - {rec.get('title', '')}\n")
            authors = rec.get("authors", [])
            if isinstance(authors, list):
                for a in authors: f.write(f"AU  - {a}\n")
            elif authors:
                f.write(f"AU  - {authors}\n")
            f.write(f"PY  - {rec.get('year', '')}\n")
            if rec.get("doi"): f.write(f"DO  - {rec['doi']}\n")
            if rec.get("arxiv_id"): f.write(f"ID  - {rec['arxiv_id']}\n")
            if rec.get("url"): f.write(f"UR  - {rec['url']}\n")
            if rec.get("journal"): f.write(f"T2  - {rec['journal']}\n")
            if rec.get("abstract"): f.write(f"AB  - {rec['abstract']}\n")
            if rec.get("keywords"):
                kws = rec["keywords"]
                if isinstance(kws, list):
                    for kw in kws: f.write(f"KW  - {kw}\n")
                else:
                    f.write(f"KW  - {kws}\n")
            if rec.get("publisher"): f.write(f"PB  - {rec['publisher']}\n")
            f.write(f"N1  - Source-DB: {rec.get('source_db', '')}\n")
            f.write(f"ER  - \n\n")


def export_screening_csv(records: list[Record], path: Path):
    fields = [
        "id", "title", "authors", "year", "doi", "arxiv_id", "abstract",
        "keywords", "source_db", "journal", "url",
        "decision", "reason_code", "notes",
    ]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for i, rec in enumerate(records):
            row = {k: rec.get(k, "") for k in fields[:11]}
            row["id"] = f"P02_{i+1:04d}"
            if isinstance(row.get("authors"), list): row["authors"] = "; ".join(row["authors"])
            if isinstance(row.get("keywords"), list): row["keywords"] = "; ".join(row["keywords"])
            row["decision"] = ""
            row["reason_code"] = ""
            row["notes"] = ""
            w.writerow(row)


# ── Report ────────────────────────────────────────────────────────────

def write_report(records: list[Record], stats: dict, source_raw: dict, path: Path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Paper 02 — Deduplication Report\n\n")
        f.write(f"**Date**: 2026-07-29\n")
        f.write(f"**Total raw records**: {stats['total_raw']:,}\n")
        f.write(f"**Unique after dedup**: {stats['unique']:,}\n")
        f.write(f"**Duplicates removed**: {stats['total_raw'] - stats['unique']:,}\n\n")

        f.write("## Per-Source Counts\n\n")
        f.write("| Source | Raw | After dedup |\n")
        f.write("|--------|----:|-----------:|\n")
        after = defaultdict(int)
        for r in records:
            for src in r.get("source_db", "").split(", "):
                if src: after[src] += 1
        all_src = sorted(set(list(source_raw.keys()) + list(after.keys())))
        for src in all_src:
            raw = source_raw.get(src, 0)
            ad = after.get(src, 0)
            f.write(f"| {src} | {raw:,} | {ad:,} |\n")

        f.write("\n## Dedup Key Distribution\n\n")
        f.write(f"- **DOI**: {stats['doi_unique']:,} records\n")
        f.write(f"- **arXiv ID**: {stats['arxiv_unique']:,} records\n")
        f.write(f"- **Title**: {stats['title_unique']:,} records\n\n")

        f.write("## Conflict Stats\n\n")
        f.write(f"- DOI conflicts (duplicates): {stats['doi_conflicts']}\n")
        f.write(f"- arXiv ID conflicts: {stats['arxiv_conflicts']}\n")
        f.write(f"- Title conflicts: {stats['title_conflicts']}\n\n")

        # Field completeness
        CHECK_FIELDS = ["title", "authors", "year", "doi", "url", "abstract", "keywords", "source_db", "journal"]
        f.write(f"## Field Completeness (n={len(records):,})\n\n")
        f.write("| Field | Present | Coverage |\n")
        f.write("|-------|--------:|--------:|\n")
        for field in CHECK_FIELDS:
            present = sum(1 for r in records if _field_present(r, field))
            pct = round(present / len(records) * 100, 1)
            flag = " ⚠️" if pct < 50 else ""
            f.write(f"| {field} | {present:,} | {pct}%{flag} |\n")

        # Multi-source
        multi = [r for r in records if ',' in r.get("source_db", "")]
        f.write(f"\n## Multi-Source Records\n\n")
        f.write(f"**Records with multiple source tags**: {len(multi)} of {len(records)} ({len(multi)/len(records)*100:.1f}%)\n\n")

        # Limitations
        f.write("\n## Limitations\n\n")
        f.write("- OpenAlex results (~400) not in file form (stored in academic-research-mcp review library)\n")
        f.write("- Citation chaining results (503 new unique) also in review library\n")
        f.write("- PsycINFO: no institutional access\n")
        f.write("- PhilPapers: API blocked (requires JS)\n")
        f.write("- Google Scholar (860 found): extraction too difficult\n")
        f.write("- Semantic Scholar: API rate-limited\n")


# ── Main ──────────────────────────────────────────────────────────────

def main():
    all_records: list[Record] = []
    source_raw: dict[str, int] = defaultdict(int)

    for path in sorted(RESULTS.iterdir()):
        if not path.is_file():
            continue
        fname = path.name
        info = SOURCE_MAP.get(fname)
        if info is None:
            continue

        db_name, query_label = info
        source_tag = f"{db_name}:{query_label}" if query_label else db_name
        ext = path.suffix.lower()

        if ext == ".ris":
            recs = parse_ris(path, source_tag)
        elif ext == ".enw":
            recs = parse_enw(path, source_tag)
        elif ext == ".json":
            recs = parse_arxiv_json(path, source_tag)
        else:
            recs = []

        all_records.extend(recs)
        if recs:
            source_raw[db_name] += len(recs)
            log.info("  %-45s %s records → total %s", fname, len(recs), len(all_records))

    log.info("Total raw records loaded: %s", len(all_records))

    # Deduplicate
    unique, stats = deduplicate(all_records)
    log.info("Unique after dedup: %s (removed %s)", stats["unique"], stats["total_raw"] - stats["unique"])
    log.info("  Dedup keys: DOI=%s arXiv=%s Title=%s", stats["doi_unique"], stats["arxiv_unique"], stats["title_unique"])

    # Export
    export_bibtex(unique, OUT / "paper02-library.bib")
    export_csv(unique, OUT / "paper02-library.csv")
    export_ris(unique, OUT / "paper02-library.ris")
    export_screening_csv(unique, OUT / "paper02-screening.csv")
    write_report(unique, stats, dict(source_raw), OUT / "deduplication-report.md")

    print(f"\n{'='*60}")
    print(f"  Paper 02 Phase 4 — Deduplication Complete")
    print(f"{'='*60}")
    print(f"  Raw records loaded:      {stats['total_raw']:>5,}")
    print(f"  Unique after dedup:      {stats['unique']:>5,}")
    print(f"  Duplicates removed:      {stats['total_raw'] - stats['unique']:>5,}")
    print(f"  BibTeX:                  paper02-library.bib")
    print(f"  CSV:                     paper02-library.csv")
    print(f"  RIS:                     paper02-library.ris")
    print(f"  Screening CSV:           paper02-screening.csv")
    print(f"  Report:                  deduplication-report.md")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
