#!/usr/bin/env python3
"""
Paper 01 — Phase 7: remap research/pdfs/ files to included studies (v2).

Phase 6 left the pdf->study mapping incomplete (~120 of 781 files resolved).
This script rebuilds the mapping from the PDFs directory:

  1. filename title match — exact / subtitle-prefix / distinctive containment
  2. filename surname-year match — FirstAuthor_YYYY[_arxiv|_oa].pdf (unique hit)
  3. first-page text title match — pdftotext fallback for unresolved files

Every candidate mapping is then VERIFIED by checking the PDF's first-page
text against the study title token sequence; unverified pairs are dropped
to unresolved. Containment matching is restricted to titles >= 40 chars so
short common phrases (e.g. "the value alignment problem") never act as keys.

Output:
  research/charting/pdf-map.csv       study_id, pdf_file, method, confidence
  research/charting/pdf-map-report.md coverage + dups + unresolved + dropped
"""

from __future__ import annotations

import csv
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent.parent  # .../01-scoping-review/
PDF_DIR = BASE / "research" / "pdfs"
INCLUDED_CSV = BASE / "research" / "included-studies.csv"
OUT_CSV = BASE / "research" / "charting" / "pdf-map.csv"
OUT_MD = BASE / "research" / "charting" / "pdf-map-report.md"

MIN_SUBTITLE = 20  # split-out subtitle candidates shorter than this are junk
DISTINCTIVE_LEN = 40  # min length of the SHORTER title eligible for containment
PREFIX_TAIL = re.compile(r"[\s\-:]*(a|an|the)?\s*$")  # trailing article/symbols


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def first_author_surname(authors: str) -> str:
    if not authors:
        return ""
    first = authors.split(";")[0].strip()
    if "," in first:
        return norm(first.split(",")[0])
    return norm(first.split()[-1])


def read_pdf_title(path: Path, pages: int = 3) -> str | None:
    """First N pages of text via pdftotext, arXiv header lines dropped."""
    try:
        out = subprocess.run(
            ["pdftotext", "-f", "1", "-l", str(pages), str(path), "-"],
            capture_output=True, text=True, timeout=30,
        )
    except Exception:
        return None
    lines = [ln.strip() for ln in (out.stdout or "").splitlines() if ln.strip()]
    lines = [ln for ln in lines
             if not re.match(r"^(arxiv|arXiv|\\v|\\h|.*arxiv\.org)", ln)]
    return " ".join(lines) if lines else None


def title_candidates(fname_or_text: str) -> list[str]:
    """Candidate title strings: full stem + subtitle parts (after ':' / '|') that
    are long enough to be meaningful (>= MIN_SUBTITLE chars)."""
    stem = Path(fname_or_text).stem if "/" not in fname_or_text else fname_or_text
    parts = re.split(r"[:\|]", stem)
    out: list[str] = []
    for i, p in enumerate(parts):
        p = p.strip()
        if not p:
            continue
        if i == 0 or len(norm(p)) >= MIN_SUBTITLE:
            out.append(p)
    return out


def match_title(fname: str, studies: list[dict]) -> str | None:
    """Strict title matching, best first: exact -> prefix -> distinctive containment."""
    file_norms = [norm(c) for c in title_candidates(fname)]
    best: tuple[int, str] | None = None
    for s in studies:
        t = norm(s["title"])
        if not t:
            continue
        for fn in file_norms:
            if not fn:
                continue
            if fn == t:
                score = 3
            elif min(len(fn), len(t)) >= MIN_SUBTITLE and (
                    fn.startswith(t) or t.startswith(fn)) \
                    and PREFIX_TAIL.sub("", fn) != t and PREFIX_TAIL.sub("", t) != fn:
                # subtitle-prefix: one is the other plus a subtitle clause
                score = 2
            elif min(len(fn), len(t)) >= DISTINCTIVE_LEN and (fn in t or t in fn):
                score = 1
            else:
                continue
            if best is None or score > best[0]:
                best = (score, s["study_id"])
    return best[1] if best else None


def match_surname_year(fname: str, studies: list[dict]) -> str | None:
    m = re.match(r"^(.*?)[_-](\d{4})(_arxiv|_oa)?\.pdf$", fname, re.I)
    if not m:
        return None
    surname = norm(m.group(1))
    year = m.group(2)
    if not surname or len(surname) > 40 or " " in surname:
        return None
    hits = [s for s in studies
            if first_author_surname(s["authors"]) == surname
            and str(s["year"]) == year]
    return hits[0]["study_id"] if len(hits) == 1 else None


def verify(pdf_file: str, study: dict) -> bool:
    """PDF text (first 3 pages) must contain the study's title token sequence
    (first 6 significant tokens, >=4 chars, in order)."""
    text = read_pdf_title(PDF_DIR / pdf_file)
    if not text:
        return False
    tnorm = norm(text)
    tokens = [t for t in norm(study["title"]).split() if len(t) >= 4][:6]
    if not tokens:
        return False
    pos = -1
    for tok in tokens:
        pos = tnorm.find(tok, pos + 1)
        if pos < 0:
            return False
    return True


def main() -> None:
    studies = list(csv.DictReader(open(INCLUDED_CSV, newline="", encoding="utf-8")))
    by_id = {s["study_id"]: s for s in studies}
    files = sorted(p for p in PDF_DIR.iterdir() if p.suffix.lower() == ".pdf")

    all_hits: dict[str, list[tuple[str, str]]] = {s["study_id"]: [] for s in studies}
    unresolved: list[tuple[str, str]] = []  # (file, reason)

    for f in files:
        sid = match_title(f.name, studies)
        method = "filename-title"
        if sid is None:
            sid = match_surname_year(f.name, studies)
            method = "surname-year"
        if sid is None:
            t = read_pdf_title(f)
            if t:
                sid = match_title(t, studies)
                method = "page-title"
        if sid is None:
            unresolved.append((f.name, "no match"))
            continue
        if not verify(f.name, by_id[sid]):
            unresolved.append((f.name, f"verification failed (claimed {sid})"))
            continue
        all_hits[sid].append((f.name, method))

    # pick best file per study (prefer surname-year machine names)
    mapped: dict[str, str] = {}
    for sid, hits in all_hits.items():
        if not hits:
            continue

        def rank(item: tuple[str, str]) -> tuple[int, str]:
            fn, _m = item
            machine = 0 if re.match(r"^[^_]+_\d{4}(_arxiv|_oa)?\.pdf$", fn) else 1
            return (machine, fn)
        hits.sort(key=rank)
        mapped[sid] = hits[0][0]

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["study_id", "pdf_file", "method", "confidence"])
        w.writeheader()
        for sid, fn in sorted(mapped.items()):
            w.writerow({"study_id": sid, "pdf_file": fn,
                        "method": "surname-year" if re.match(r"^[^_]+_\d{4}(_arxiv|_oa)?\.pdf$", fn)
                                  else "filename-title",
                        "confidence": "high"})

    dups = {sid: [f for f, _m in hits] for sid, hits in all_hits.items() if len(hits) > 1}
    n = len(studies)
    with open(OUT_MD, "w", encoding="utf-8") as fh:
        fh.write("# PDF remap report — Phase 7 (v2, verified)\n\n")
        fh.write(f"- Files on disk: **{len(files)}**\n")
        fh.write(f"- Studies with a verified mapped full text: **{len(mapped)} / {n}**\n")
        fh.write(f"- Duplicate files (same study): **{len(dups)}** studies\n")
        fh.write(f"- Unresolved: **{len(unresolved)}** files\n")
        if dups:
            fh.write("\n## Duplicates\n\n| study_id | files |\n|---|---|\n")
            for sid, hits in sorted(dups.items()):
                fh.write(f"| {sid} | {', '.join(hits)} |\n")
        if unresolved:
            fh.write("\n## Unresolved files\n\n| file | reason |\n|---|---|\n")
            for fn, reason in unresolved:
                fh.write(f"| `{fn}` | {reason} |\n")
    print(f"mapped {len(mapped)}/{n}; unresolved {len(unresolved)}; dups {len(dups)}")
    print(f"wrote {OUT_CSV.name} and {OUT_MD.name}")


if __name__ == "__main__":
    sys.exit(main())
