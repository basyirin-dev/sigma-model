#!/usr/bin/env python3
"""
Paper 01 — Phase 4: Deduplication & Reference Management

Parses all search result files (RIS, ENW, JSON), merges into a unified
library, deduplicates (DOI > arXiv ID > title match), tags by source
database, and exports as .bib and .csv.

Outputs:
  - research/clean-library/paper01-library.bib   (BibTeX)
  - research/clean-library/paper01-library.csv    (CSV)
  - research/clean-library/deduplication-report.md (stats)
"""

import csv, json, os, re, sys, logging
from collections import defaultdict
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

BASE = Path(__file__).resolve().parent.parent
RESULTS = BASE / "research" / "search-results"
OUT = BASE / "research" / "clean-library"
OUT.mkdir(parents=True, exist_ok=True)

# ── Record model ──────────────────────────────────────────────────────

class Record(dict):
    """Unified paper record with required fields."""
    REQUIRED = {"title", "source_db", "source_file"}
    OPTIONAL = {"doi", "arxiv_id", "authors", "year", "abstract",
                "keywords", "url", "journal", "publisher", "type"}

    def __missing__(self, key):
        return ""

    def dedup_key(self):
        """Primary → secondary key for deduplication."""
        doi = self.get("doi", "").strip().lower()
        if doi and doi != "none":
            return ("doi", doi)
        aid = self.get("arxiv_id", "").strip().lower()
        if aid:
            return ("arxiv", aid)
        title = self.get("title", "").strip().lower()
        # Normalize title: collapse whitespace, remove punctuation
        title = re.sub(r"[^a-z0-9\s]", "", title)
        title = re.sub(r"\s+", " ", title).strip()
        if title and len(title) > 10:
            return ("title", title)
        return None


# ── Parsers ───────────────────────────────────────────────────────────

def parse_ris(path: Path, source_tag: str) -> list[Record]:
    """Parse a RIS file.  source_tag overrides DB tag."""
    records = []
    current = None
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

            tag = line[:2]
            val = line[6:].strip() if len(line) > 6 else ""

            if tag == "TY":
                current["type"] = val
            elif tag == "TI":
                current["title"] = val
            elif tag == "AU":
                current.setdefault("authors", []).append(val)
            elif tag == "PY":
                m = re.match(r"(\d{4})", val)
                if m:
                    current["year"] = int(m.group(1))
            elif tag == "DO":
                current["doi"] = val
            elif tag == "UR":
                current["url"] = val
            elif tag == "AB":
                current["abstract"] = val
            elif tag == "KW":
                current.setdefault("keywords", []).append(val)
            elif tag == "T2":
                current["journal"] = val
            elif tag == "PB":
                current["publisher"] = val
            elif tag == "SN":
                if not current.get("issn"):
                    current["issn"] = val
            elif tag == "J2":
                if not current.get("journal_abbr"):
                    current["journal_abbr"] = val

    if current:
        records.append(current)

    # Tag source
    for r in records:
        if source_tag:
            r["source_db"] = source_tag
        r["source_file"] = path.name
        # Extract arXiv ID from URL if present
        url = r.get("url", "")
        m = re.search(r"arxiv\.org/(?:abs|pdf)/(\d+\.\d+)", url)
        if m and not r.get("arxiv_id"):
            r["arxiv_id"] = m.group(1)

    return records


def parse_enw(path: Path, source_tag: str) -> list[Record]:
    """Parse EndNote / ENW format (ACM exports)."""
    records = []
    current = None
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n\r")
            if not line.strip():
                continue
            tag = line[:2]
            val = line[3:].strip() if len(line) > 3 else ""

            if tag == "%0":
                if current:
                    records.append(current)
                current = Record()
                current["type"] = val
                continue

            if current is None:
                current = Record()

            if tag == "%T":
                current["title"] = val
            elif tag == "%A":
                current.setdefault("authors", []).append(val)
            elif tag == "%D":
                m = re.match(r"(\d{4})", val)
                if m:
                    current["year"] = int(m.group(1))
            elif tag == "%R":
                current["doi"] = val
            elif tag == "%U":
                current["url"] = val
            elif tag == "%I":
                current["publisher"] = val
            elif tag == "%B":
                current["journal"] = val
            elif tag == "%K":
                current.setdefault("keywords", []).append(val)
            elif tag == "%@" and not current.get("isbn"):
                current["isbn"] = val

    if current:
        records.append(current)

    for r in records:
        r["source_db"] = source_tag
        r["source_file"] = path.name

    return records


def parse_arxiv_json(path: Path, source_tag: str) -> list[Record]:
    """Parse arXiv API JSON export."""
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
        if m:
            r["year"] = int(m.group(1))

        cats = entry.get("categories", [])
        if cats:
            r["keywords"] = [f"arxiv:{c}" for c in cats]

        records.append(r)

    return records


def parse_openalex_json(path: Path, source_tag: str) -> list[Record]:
    """Parse OpenAlex JSON export."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    records = []
    for entry in data.get("entries", []):
        r = Record()
        r["title"] = entry.get("title", "")
        doi = entry.get("doi", "")
        if doi:
            r["doi"] = doi
        r["year"] = entry.get("year", "")
        r["source_db"] = source_tag
        r["source_file"] = path.name
        records.append(r)

    return records


def parse_review_export(path: Path, source_tag: str) -> list[Record]:
    """Parse review-export metadata.  Only creates placeholder records."""
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    count = data.get("count", 0)
    log.info("Review export references %s records (not imported — in MCP store)", count)
    return []


# ── Source definitions ────────────────────────────────────────────────

PARSERS = {
    ".ris": parse_ris,
    ".enw": parse_enw,
    ".json": None,  # dispatch by content
}

SOURCE_MAP = {
    # RIS files
    "scopus-2026-07-30.ris":              ("Scopus", "F2"),
    "scopus-f1-prim-2026-07-30.ris":      ("Scopus", "F1"),
    "scopus-f1-sec-2026-07-30.ris":       ("Scopus", "F1"),
    "scopus-f3-2026-07-30.ris":           ("Scopus", "F3"),
    "wos-2026-07-30.ris":                 ("WoS", "F2"),
    "wos-f1-2026-07-30.ris":              ("WoS", "F1"),
    "wos-f3-2026-07-30.ris":              ("WoS", "F3"),
    # ENW
    "acm-2026-07-30.enw":                 ("ACM", "F2"),
    # JSON
    "arxiv-f1-safety-2026-07-30.json":    ("arXiv", "F1"),
    "arxiv-f2-safety-gen-2026-07-30.json":("arXiv", "F2"),
    "arxiv-f3-narrow-2026-07-30.json":    ("arXiv", "F3"),
    "arxiv-f4-category-2026-07-30.json":  ("arXiv", "F4"),
    "arxiv-f5-schema-coherence-2026-07-30.json": ("arXiv", "F5"),
    "openalex-2026-07-30.json":           ("OpenAlex", "F2"),
    "google-scholar-1-core-2026-07-30.json":  ("GoogleScholar", "Q1"),
    "google-scholar-2-schema-2026-07-30.json":("GoogleScholar", "Q2"),
    "google-scholar-3-deceptive-2026-07-30.json":("GoogleScholar", "Q3"),
    "google-scholar-4-mesa-2026-07-30.json":("GoogleScholar", "Q4"),
    "review-export-2026-07-30.json":      ("CitationChaining", ""),
}


# ── Deduplication ─────────────────────────────────────────────────────

def deduplicate(records: list[Record]) -> list[Record]:
    """Deduplicate records.  Priority: DOI > arXiv ID > title.

    Returns merged records with source_db aggregated.
    """
    by_key: dict[tuple, Record] = {}
    conflicts = 0
    key_doi = {}
    key_arxiv = {}
    key_title = {}

    for rec in records:
        k = rec.dedup_key()
        if k is None:
            continue  # can't dedup this record

        kind, key = k

        if kind == "doi":
            if key in key_doi:
                conflicts += 1
                existing = key_doi[key]
                # Merge source tags
                existing["source_db"] = _merge_sources(existing["source_db"], rec["source_db"])
            else:
                key_doi[key] = rec
        elif kind == "arxiv":
            if key in key_arxiv:
                conflicts += 1
                existing = key_arxiv[key]
                existing["source_db"] = _merge_sources(existing["source_db"], rec["source_db"])
            else:
                key_arxiv[key] = rec
        elif kind == "title":
            if key in key_title:
                conflicts += 1
                existing = key_title[key]
                existing["source_db"] = _merge_sources(existing["source_db"], rec["source_db"])
            else:
                key_title[key] = rec

    log.info("Deduplication: %s unique records from %s total (%s conflicts)",
             len(key_doi) + len(key_arxiv) + len(key_title), len(records), conflicts)

    # Merge: prefer DOI-keyed (best quality), then arXiv, then title
    result = []
    seen_titles = set()
    for pool in [key_doi, key_arxiv, key_title]:
        for k, rec in pool.items():
            title_key = rec.dedup_key()
            if title_key and title_key[0] in ("doi", "arxiv"):
                pass  # always include DOI/arXiv records
            elif title_key:
                t = title_key[1]
                if t in seen_titles:
                    continue
                seen_titles.add(t)
            result.append(rec)

    return result


def _merge_sources(existing, new):
    """Merge source tags into a comma-separated unique set."""
    if not existing:
        return new
    if not new:
        return existing
    parts = set(existing.split(", "))
    parts.update(new.split(", "))
    return ", ".join(sorted(parts))


# ── Export ─────────────────────────────────────────────────────────────

def export_bibtex(records: list[Record], path: Path):
    """Export as BibTeX file."""
    bibtype_map = {
        "JOUR": "article",
        "CONF": "inproceedings",
        "Conference Paper": "inproceedings",
        "Journal Article": "article",
        "Article": "article",
    }

    with open(path, "w", encoding="utf-8") as f:
        for i, rec in enumerate(records):
            bibtype = bibtype_map.get(rec.get("type", ""), "misc")
            citekey = f"P01_{i+1:04d}"
            if rec.get("doi"):
                # Use first segment of DOI as short identifier
                short = re.sub(r"[^a-zA-Z0-9]", "", rec["doi"][:20])
                if short:
                    citekey = short[:30]

            f.write(f"@{bibtype}{{{citekey},\n")
            _bib_field(f, "title", rec.get("title", ""), True)
            _bib_field(f, "author", " and ".join(rec.get("authors", [])) if isinstance(rec.get("authors"), list) else rec.get("authors", ""))
            _bib_field(f, "year", str(rec.get("year", "")))
            _bib_field(f, "doi", rec.get("doi", ""))
            _bib_field(f, "url", rec.get("url", ""))
            _bib_field(f, "journal", rec.get("journal", ""))
            _bib_field(f, "publisher", rec.get("publisher", ""))
            _bib_field(f, "abstract", rec.get("abstract", ""), True)
            _bib_field(f, "keywords", ", ".join(rec.get("keywords", [])) if isinstance(rec.get("keywords"), list) else rec.get("keywords", ""))
            _bib_field(f, "source-db", rec.get("source_db", ""))
            f.write("}\n\n")


def _bib_field(f, name, value, is_long=False):
    if not value:
        return
    value = value.replace("&", "\\&").replace("%", "\\%").replace("$", "\\$")
    if is_long and len(value) > 80:
        f.write(f"  {name} = {{\n    {value}\n  }},\n")
    else:
        f.write(f"  {name} = {{{value}}},\n")


def export_csv(records: list[Record], path: Path):
    """Export as CSV."""
    fields = ["id", "title", "authors", "year", "doi", "arxiv_id", "url",
              "journal", "abstract", "keywords", "source_db", "source_file"]
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for i, rec in enumerate(records):
            row = dict(rec)
            row["id"] = f"P01_{i+1:04d}"
            if isinstance(row.get("authors"), list):
                row["authors"] = "; ".join(row["authors"])
            if isinstance(row.get("keywords"), list):
                row["keywords"] = "; ".join(row["keywords"])
            w.writerow(row)


def write_report(records: list[Record], source_counts: dict, path: Path):
    """Write deduplication statistics report."""
    with open(path, "w", encoding="utf-8") as f:
        f.write("# Paper 01 — Deduplication Report\n\n")
        total_raw = sum(source_counts.values())
        f.write(f"**Date**: 2026-07-30\n")
        f.write(f"**Total raw records**: {total_raw:,}\n")
        f.write(f"**Unique after dedup**: {len(records):,}\n")
        f.write(f"**Duplicates removed**: {total_raw - len(records):,}\n\n")

        f.write("## Per-Source Counts\n\n")
        f.write("| Source | Raw | After dedup |\n")
        f.write("|--------|----:|-----------:|\n")
        after = defaultdict(int)
        for r in records:
            for src in r.get("source_db", "").split(", "):
                if src:
                    after[src] += 1
        all_sources = sorted(set(list(source_counts.keys()) + list(after.keys())))
        for src in all_sources:
            raw = source_counts.get(src, 0)
            ad = after.get(src, 0)
            f.write(f"| {src} | {raw:,} | {ad:,} |\n")

        f.write("\n## Dedup Key Distribution\n\n")
        key_map = {"doi": "DOI", "arxiv": "arXiv ID", "title": "Title"}
        by_key: dict[str, int] = defaultdict(int)
        for r in records:
            k = r.dedup_key()
            if k is None:
                by_key["No key"] += 1
            else:
                by_key[key_map.get(k[0], k[0])] += 1
        for k, v in sorted(by_key.items()):
            if v:
                f.write(f"- **{k}**: {v:,} records\n")


# ── Main ──────────────────────────────────────────────────────────────

def main():
    all_records: list[Record] = []
    source_raw_counts: dict[str, int] = defaultdict(int)

    files = sorted(RESULTS.iterdir())

    for path in files:
        if not path.is_file():
            continue
        fname = path.name

        # Determine source and parser
        info = SOURCE_MAP.get(fname)
        if info is None:
            log.info("Skipping unknown file: %s", fname)
            continue

        db_name, query_label = info
        source_tag = f"{db_name}:{query_label}" if query_label else db_name
        ext = path.suffix.lower()

        if ext == ".ris":
            recs = parse_ris(path, source_tag)
        elif ext == ".enw":
            recs = parse_enw(path, source_tag)
        elif ext == ".json":
            # Dispatch by content pattern
            if fname.startswith("arxiv"):
                recs = parse_arxiv_json(path, source_tag)
            elif fname.startswith("openalex"):
                recs = parse_openalex_json(path, source_tag)
            elif fname.startswith("google"):
                recs = []
                log.info("Google Scholar file %s: 0 records", fname)
            elif fname.startswith("review"):
                recs = parse_review_export(path, source_tag)
            else:
                recs = []
                log.info("Unknown JSON file: %s", fname)
        else:
            recs = []

        all_records.extend(recs)
        if recs:
            source_raw_counts[db_name] += len(recs)
            log.info("Parsed %s: %s records → total %s", fname, len(recs), len(all_records))

    log.info("Total raw records loaded: %s", len(all_records))

    # Deduplicate
    unique = deduplicate(all_records)
    log.info("Unique records after dedup: %s", len(unique))

    # Export
    export_bibtex(unique, OUT / "paper01-library.bib")
    log.info("Exported: paper01-library.bib")

    export_csv(unique, OUT / "paper01-library.csv")
    log.info("Exported: paper01-library.csv")

    write_report(unique, dict(source_raw_counts), OUT / "deduplication-report.md")
    log.info("Exported: deduplication-report.md")

    # Summary
    print(f"\n{'='*60}")
    print(f"  Paper 01 Phase 4 — Deduplication Complete")
    print(f"{'='*60}")
    print(f"  Raw records loaded: {len(all_records):,}")
    print(f"  Unique after dedup: {len(unique):,}")
    print(f"  Duplicates removed: {len(all_records) - len(unique):,}")
    print(f"  Output directory:   {OUT}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
