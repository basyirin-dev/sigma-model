"""arXiv publication monitor for Σ-Model keyword clusters."""

from __future__ import annotations

import argparse
import json
import logging
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from typing import Any

from . import (
    last_run,
    update_last_run,
    write_json_output,
)

logger = logging.getLogger(__name__)

KEYWORD_CLUSTERS: dict[str, list[str]] = {
    "schema_coherence": [
        '"schema coherence" AI',
        '"schema coherence" neural network',
        "representational coherence AI",
    ],
    "compositional_generalization": [
        '"compositional generalization" neural',
        '"compositional generalisation" benchmark',
        "SCAN COGS CFQ PCFG-SET",
        "systematic generalization benchmark 2026",
    ],
    "ood_generalization": [
        '"out-of-distribution" generalization neural',
        '"OOD generalization" transformer',
        "high-dimensional OOD detection 2026",
    ],
    "phase_transition_training": [
        '"phase transition" neural network training',
        '"curriculum learning" phase transition',
        "training dynamics phase change AI",
    ],
    "grokking_phase_transition": [
        '"grokking" phase transition',
        "sudden generalization grokking",
        "grokking mechanistic interpretability",
    ],
    "metacognition_AI": [
        '"metacognition" AI benchmark',
        "metacognitive monitoring language model",
        "self-evaluation LLM calibration",
    ],
    "executive_function_AI": [
        '"executive function" AI',
        '"cognitive control" neural network',
        "inhibitory control reinforcement learning",
    ],
    "theory_of_mind_LM": [
        '"theory of mind" language model',
        '"mental state" reasoning AI',
        "belief reasoning neural network",
    ],
    "agentic_evaluation": [
        '"agentic" evaluation benchmark',
        "autonomous agent benchmark 2026",
        "tool-use LLM benchmark generalization",
    ],
    "sigma_suppression": [
        '"sigma suppression" AI',
        "feature suppression representation learning",
        "schema coherence sigma suppression",
    ],
    "curriculum_learning_compositional": [
        '"curriculum learning" compositional generalization',
        "easy-to-hard curriculum neural network",
        "task ordering generalization",
    ],
    "parameter_space_topology": [
        '"parameter space" topology neural network',
        "loss landscape topology generalization",
        "Fisher information geometry deep learning",
    ],
    "singular_learning_theory": [
        '"singular learning theory"',
        "Watanabe singular learning",
        "algebraic geometry neural network",
    ],
    "boundary_case_memory": [
        '"boundary case" memorization neural',
        "edge case overfitting generalization",
        "long-tail generalization boundary",
    ],
}

ARXIV_NS = {"atom": "http://www.w3.org/2005/Atom"}


def _retry_urlopen(
    req: urllib.request.Request,
    max_retries: int = 3,
    base_delay: float = 2.0,
) -> bytes:
    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return resp.read()
        except urllib.error.HTTPError as e:
            if e.code == 429 and attempt < max_retries - 1:
                delay = base_delay * (2**attempt)
                logger.warning("429 rate limited, retrying in %.0fs (attempt %d/%d)", delay, attempt + 1, max_retries)
                time.sleep(delay)
            else:
                raise
    raise RuntimeError(f"Max retries ({max_retries}) exceeded for {req.full_url}")


def fetch_arxiv(query: str, max_results: int = 10) -> list[dict[str, str]]:
    encoded = urllib.parse.quote(query)
    url = (
        f"http://export.arxiv.org/api/query?search_query=all:{encoded}"
        f"&max_results={max_results}&sortBy=submittedDate&sortOrder=descending"
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Sigma-Monitor/2.0"})
        data = _retry_urlopen(req).decode("utf-8")
    except Exception as e:
        logger.error("arXiv query failed: %s", e)
        return [{"error": f"arXiv query failed: {e}"}]

    root = ET.fromstring(data)
    results = []
    for entry in root.findall("atom:entry", ARXIV_NS):
        title_el = entry.find("atom:title", ARXIV_NS)
        published_el = entry.find("atom:published", ARXIV_NS)
        link_el = entry.find("atom:id", ARXIV_NS)
        summary_el = entry.find("atom:summary", ARXIV_NS)
        authors_el = entry.findall("atom:author", ARXIV_NS)

        authors = []
        for author in authors_el:
            name_el = author.find("atom:name", ARXIV_NS)
            if name_el is not None and name_el.text is not None:
                authors.append(name_el.text.strip())

        title = (title_el.text or "").strip() if title_el is not None else "N/A"
        date = (published_el.text or "")[:10] if published_el is not None else "N/A"
        url_str = (link_el.text or "").strip() if link_el is not None else "N/A"
        summary = ((summary_el.text or "").strip()[:300]) if summary_el is not None else "N/A"

        results.append({
            "title": title,
            "date": date,
            "url": url_str,
            "authors": authors,
            "summary": summary,
        })
    return results


def _filter_by_date(papers: list[dict[str, str]], since: str) -> list[dict[str, str]]:
    filtered = []
    for p in papers:
        if "error" in p:
            filtered.append(p)
            continue
        if p.get("date", "N/A") >= since:
            filtered.append(p)
    return filtered


def _dedup(papers: list[dict[str, str]]) -> list[dict[str, str]]:
    seen_urls: set[str] = set()
    deduped = []
    for p in papers:
        url = p.get("url", "")
        if url and url in seen_urls:
            continue
        if url:
            seen_urls.add(url)
        deduped.append(p)
    return deduped


_RELEVANCE_KEYWORDS = frozenset([
    "neural", "deep learning", "machine learning", "transformer", "attention",
    "generalization", "generalisation", "compositional", "schema", "grokking",
    "phase transition", "curriculum", "training dynamics", "loss landscape",
    "out-of-distribution", "representation learning", "meta-learning",
    "reinforcement learning", "language model", "LLM", "AI", "cognitive",
    "benchmark", "compositional generalization", "compositional generalisation",
    "SCAN", "COGS", "PCFG", "singular learning", "Fisher information",
    "neural network", "gradient", "parameter space", "feature learning",
])


def _is_relevant(paper: dict[str, str]) -> bool:
    """Post-fetch relevance filter: reject papers with no AI/ML signal."""
    text = (paper.get("title", "") + " " + paper.get("summary", "")).lower()
    return any(kw in text for kw in _RELEVANCE_KEYWORDS)


def run(since: str | None = None, verbose: bool = False) -> dict[str, Any]:
    if verbose:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    if since is None:
        prev = last_run("pub")
        since = prev[:10] if prev else "2026-04-03"

    logger.info("Scanning arXiv since %s across %d keyword clusters", since, len(KEYWORD_CLUSTERS))

    all_results: dict[str, Any] = {}
    seen_urls: set[str] = set()

    for cluster_name, queries in KEYWORD_CLUSTERS.items():
        cluster_papers: list[dict[str, str]] = []
        for q in queries:
            papers = fetch_arxiv(q, max_results=5)
            cluster_papers.extend(papers)
            time.sleep(1.5)

        cluster_papers = [p for p in cluster_papers if "error" not in p]
        cluster_papers = _filter_by_date(cluster_papers, since)
        cluster_papers = _dedup(cluster_papers)
        cluster_papers = [p for p in cluster_papers if _is_relevant(p)]

        new_papers = []
        for p in cluster_papers:
            url = p.get("url", "")
            if url not in seen_urls:
                seen_urls.add(url)
                new_papers.append(p)

        all_results[cluster_name] = {
            "query_count": len(queries),
            "papers_found": len(new_papers),
            "papers": new_papers,
        }
        logger.info("Cluster %s: %d new papers", cluster_name, len(new_papers))

    output = {
        "timestamp": datetime.now().isoformat(),
        "since": since,
        "total_clusters": len(KEYWORD_CLUSTERS),
        "total_new_papers": sum(c["papers_found"] for c in all_results.values()),
        "clusters": all_results,
    }

    write_json_output(output, "latest.json")
    update_last_run("pub")
    logger.info("Total new papers: %d", output["total_new_papers"])
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Σ-Model arXiv Publication Monitor")
    parser.add_argument("--since", help="Only show papers after this date (YYYY-MM-DD)")
    parser.add_argument("--format", choices=["json", "text"], default="text", help="Output format")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose logging")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    result = run(since=args.since, verbose=args.verbose)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print("\n=== Σ-Model arXiv Monitor ===")
        print(f"Since: {result['since']}")
        print(f"Clusters: {result['total_clusters']}")
        print(f"New papers: {result['total_new_papers']}")
        for cluster_name, data in result["clusters"].items():
            if data["papers_found"] > 0:
                print(f"\n--- {cluster_name} ({data['papers_found']}) ---")
                for p in data["papers"]:
                    print(f"  [{p['date']}] {p['title']}")
                    print(f"    {p['url']}")


if __name__ == "__main__":
    main()
