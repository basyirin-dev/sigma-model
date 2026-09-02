"""Multi-Domain Literature Retrieval Pipeline for Paper 02.

Queries OpenAlex and arXiv across 5 research clusters:
1. Phase Transitions & Bifurcations in ML
2. Grokking & Delayed Generalization
3. Singular Learning Theory & Geometry
4. Edge of Stability & Hessian Dynamics
5. Compositional Generalization & Inductive Biases
"""

from __future__ import annotations

import json
import logging
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

CLUSTERS: dict[str, list[str]] = {
    "Bifurcations & Phase Transitions": [
        "bifurcation gradient descent neural network",
        "transcritical bifurcation loss landscape",
        "phase transition representation learning order parameter",
        "dynamical systems loss landscape bifurcations",
    ],
    "Grokking & Delayed Generalization": [
        "grokking phase transition weight decay",
        "representation formation delayed generalization",
        "circuit efficiency grokking mechanistic",
        "grokking modular arithmetic transformers",
    ],
    "Singular Learning Theory & Geometry": [
        "singular learning theory local learning coefficient phase",
        "loss landscape geometry singularities generalization",
        "Watanabe singular learning theory neural networks",
        "local learning coefficient phase transitions",
    ],
    "Edge of Stability & Hessian Dynamics": [
        "edge of stability Hessian top eigenvalue Cohen",
        "sharpness-aware minimization spectral dynamics",
        "gradient descent edge of stability neural networks",
        "Hessian spectral density learning dynamics",
    ],
    "Compositional Generalization & Inductive Biases": [
        "compositional generalization inductive bias SCAN",
        "systematic generalization representation geometry",
        "compositional generalisation failure transformers",
        "disentangled representations compositional generalization",
    ],
}

MIN_YEAR = 2018
MAX_YEAR = 2026
USER_AGENT = "SigmaModelResearch/1.0 (mailto:research@sigma-model.org)"


def normalize_title(title: str) -> str:
    """Normalize paper title for fuzzy deduplication."""
    clean = re.sub(r"[^a-zA-Z0-9 ]", "", title.lower())
    return " ".join(clean.split())


def query_openalex(query: str, per_page: int = 15) -> list[dict[str, Any]]:
    """Query the OpenAlex REST API."""
    encoded_query = urllib.parse.quote_plus(query)
    url = (
        f"https://api.openalex.org/works?search={encoded_query}"
        f"&filter=from_publication_date:{MIN_YEAR}-01-01,to_publication_date:{MAX_YEAR}-12-31"
        f"&per_page={per_page}&sort=relevance_score:desc"
    )
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            data = json.loads(response.read().decode("utf-8"))
            results: list[dict[str, Any]] = []
            for work in data.get("results", []):
                title = work.get("title") or ""
                if not title:
                    continue
                year = work.get("publication_year")
                if not year or year < MIN_YEAR or year > MAX_YEAR:
                    continue
                doi = work.get("doi") or ""
                authors = [
                    a.get("author", {}).get("display_name", "")
                    for a in work.get("authorships", [])
                    if a.get("author", {}).get("display_name")
                ]
                venue = (
                    work.get("primary_location", {})
                    .get("source", {})
                    .get("display_name", "Preprint/arXiv")
                    if work.get("primary_location") and work.get("primary_location", {}).get("source")
                    else "Preprint/arXiv"
                )
                cited_by_count = work.get("cited_by_count", 0)

                # Abstract extraction if available
                abstract_inverted = work.get("abstract_inverted_index")
                abstract = ""
                if abstract_inverted:
                    word_pos: list[tuple[int, str]] = []
                    for word, positions in abstract_inverted.items():
                        for pos in positions:
                            word_pos.append((pos, word))
                    word_pos.sort()
                    abstract = " ".join(w for _, w in word_pos)

                results.append({
                    "title": title.strip(),
                    "authors": authors[:5],
                    "year": year,
                    "venue": venue,
                    "doi": doi,
                    "arxiv_id": "",
                    "citations": cited_by_count,
                    "abstract": abstract[:400],
                    "source": "OpenAlex",
                })
            return results
    except Exception as e:
        logger.warning("OpenAlex query failed for '%s': %s", query, e)
        return []


def query_arxiv(query: str, max_results: int = 15) -> list[dict[str, Any]]:
    """Query the arXiv API via atom XML feed."""
    encoded_query = urllib.parse.quote_plus(query)
    url = f"http://export.arxiv.org/api/query?search_query=all:{encoded_query}&start=0&max_results={max_results}&sortBy=relevance&sortOrder=descending"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            xml_data = response.read()
            root = ET.fromstring(xml_data)
            ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
            results: list[dict[str, Any]] = []
            for entry in root.findall("atom:entry", ns):
                title_elem = entry.find("atom:title", ns)
                title = title_elem.text.strip().replace("\n", " ") if title_elem is not None and title_elem.text else ""
                if not title or title.lower().startswith("error"):
                    continue

                published_elem = entry.find("atom:published", ns)
                year = int(published_elem.text[:4]) if published_elem is not None and published_elem.text else 2020
                if year < MIN_YEAR or year > MAX_YEAR:
                    continue

                id_elem = entry.find("atom:id", ns)
                raw_id = id_elem.text.strip() if id_elem is not None and id_elem.text else ""
                arxiv_id = raw_id.split("/abs/")[-1] if "/abs/" in raw_id else raw_id

                summary_elem = entry.find("atom:summary", ns)
                abstract = summary_elem.text.strip().replace("\n", " ") if summary_elem is not None and summary_elem.text else ""

                authors: list[str] = []
                for author_elem in entry.findall("atom:author", ns):
                    name_elem = author_elem.find("atom:name", ns)
                    if name_elem is not None and name_elem.text:
                        authors.append(name_elem.text.strip())

                doi_elem = entry.find("arxiv:doi", ns)
                doi = doi_elem.text.strip() if doi_elem is not None and doi_elem.text else ""

                results.append({
                    "title": title,
                    "authors": authors[:5],
                    "year": year,
                    "venue": "arXiv",
                    "doi": doi,
                    "arxiv_id": arxiv_id,
                    "citations": 0,
                    "abstract": abstract[:400],
                    "source": "arXiv",
                })
            return results
    except Exception as e:
        logger.warning("arXiv query failed for '%s': %s", query, e)
        return []


def main() -> None:
    """Execute multi-cluster retrieval, deduplication, and export."""
    output_dir = Path("/home/bigbasy/Documents/sigma-model/paper/experiments/literature")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "raw_literature.json"

    seen_titles: set[str] = set()
    seen_dois: set[str] = set()
    seen_arxiv: set[str] = set()

    corpus: list[dict[str, Any]] = []
    cluster_stats: dict[str, int] = {k: 0 for k in CLUSTERS}

    logger.info("Beginning literature retrieval across 5 clusters...")

    for cluster_name, query_list in CLUSTERS.items():
        logger.info("Processing Cluster: %s", cluster_name)
        for q in query_list:
            logger.info("  Executing query: '%s'", q)
            # Fetch OpenAlex
            oa_results = query_openalex(q, per_page=12)
            time.sleep(0.3)
            # Fetch arXiv
            arxiv_results = query_arxiv(q, max_results=10)
            time.sleep(0.3)

            for item in oa_results + arxiv_results:
                norm_t = normalize_title(item["title"])
                doi = item["doi"].lower().strip() if item["doi"] else ""
                arxiv = item["arxiv_id"].lower().strip() if item["arxiv_id"] else ""

                # Deduplication check
                if norm_t in seen_titles:
                    continue
                if doi and doi in seen_dois:
                    continue
                if arxiv and arxiv in seen_arxiv:
                    continue

                seen_titles.add(norm_t)
                if doi:
                    seen_dois.add(doi)
                if arxiv:
                    seen_arxiv.add(arxiv)

                item["primary_cluster"] = cluster_name
                corpus.append(item)
                cluster_stats[cluster_name] += 1

    logger.info("Retrieval complete! Total deduplicated papers: %d", len(corpus))
    for c_name, count in cluster_stats.items():
        logger.info("  - %s: %d papers", c_name, count)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(corpus, f, indent=2, ensure_ascii=False)

    logger.info("Saved raw corpus to %s", output_file)


if __name__ == "__main__":
    main()
