"""Social media monitor — scans Reddit and Hacker News for Σ-Model-related discussions."""

from __future__ import annotations

import argparse
import json
import logging
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from typing import Any

from . import write_json_output

logger = logging.getLogger(__name__)

REDDIT_SEARCH_QUERIES = [
    "compositional generalization",
    "schema coherence AI",
    "grokking phase transition",
    "Σ-Model",
    "sigma suppression neural",
    "curriculum learning generalization",
    "singular learning theory",
    "parameter space topology neural",
]

HN_SEARCH_QUERIES = [
    "compositional generalization",
    "schema coherence",
    "grokking phase transition",
    "neural network curriculum learning",
    "singular learning theory",
]

REDDIT_SUBREDDITS = ["MachineLearning", "artificial", "compsci", "languagelearning"]
REDDIT_API = "https://www.reddit.com/r/{subreddit}/search.json"
HN_API = "https://hn.algolia.com/api/v1/search_by_date"


def fetch_reddit(subreddit: str, query: str, limit: int = 5) -> list[dict[str, str]]:
    params = urllib.parse.urlencode({
        "q": query,
        "restrict_sr": "true",
        "sort": "new",
        "t": "month",
        "limit": limit,
    })
    url = f"{REDDIT_API.format(subreddit=subreddit)}?{params}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Sigma-Monitor/2.0 (research)"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        posts = []
        for child in data.get("data", {}).get("children", []):
            post = child.get("data", {})
            posts.append({
                "title": post.get("title", "N/A"),
                "subreddit": post.get("subreddit", subreddit),
                "url": f"https://reddit.com{post.get('permalink', '')}",
                "score": post.get("score", 0),
                "num_comments": post.get("num_comments", 0),
                "created_utc": datetime.fromtimestamp(post.get("created_utc", 0)).strftime("%Y-%m-%d"),
                "selftext": (post.get("selftext") or "")[:200],
            })
        return posts
    except urllib.error.HTTPError as e:
        if e.code == 429:
            logger.warning("Reddit rate limited for r/%s", subreddit)
        else:
            logger.warning("Reddit error %d for r/%s: %s", e.code, subreddit, e.reason)
        return []
    except Exception as e:
        logger.error("Reddit request failed: %s", e)
        return []


def fetch_hn(query: str, limit: int = 5) -> list[dict[str, str]]:
    params = urllib.parse.urlencode({"query": query, "tags": "story", "hitsPerPage": limit})
    url = f"{HN_API}?{params}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Sigma-Monitor/2.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        posts = []
        for hit in data.get("hits", []):
            posts.append({
                "title": hit.get("title", "N/A"),
                "url": hit.get("url") or f"https://news.ycombinator.com/item?id={hit.get('objectID', '')}",
                "hn_url": f"https://news.ycombinator.com/item?id={hit.get('objectID', '')}",
                "points": hit.get("points", 0),
                "num_comments": hit.get("num_comments", 0),
                "created_at": (hit.get("created_at") or "")[:10],
            })
        return posts
    except Exception as e:
        logger.error("HN request failed: %s", e)
        return []


def run(verbose: bool = False) -> dict[str, Any]:
    if verbose:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    reddit_results: dict[str, list] = {}
    for subreddit in REDDIT_SUBREDDITS:
        all_posts = []
        for query in REDDIT_SEARCH_QUERIES[:3]:
            posts = fetch_reddit(subreddit, query, limit=3)
            all_posts.extend(posts)
            time.sleep(2)
        seen_urls = set()
        unique = []
        for p in all_posts:
            if p["url"] not in seen_urls:
                seen_urls.add(p["url"])
                unique.append(p)
        reddit_results[subreddit] = unique
        logger.info("r/%s: %d unique posts", subreddit, len(unique))

    hn_results: list[dict[str, str]] = []
    for query in HN_SEARCH_QUERIES:
        posts = fetch_hn(query, limit=3)
        hn_results.extend(posts)
        time.sleep(1)
    seen_hn = set()
    unique_hn = []
    for p in hn_results:
        if p["hn_url"] not in seen_hn:
            seen_hn.add(p["hn_url"])
            unique_hn.append(p)

    output = {
        "timestamp": datetime.now().isoformat(),
        "reddit": {
            "subreddits_scanned": REDDIT_SUBREDDITS,
            "queries_used": len(REDDIT_SEARCH_QUERIES),
            "results": reddit_results,
        },
        "hacker_news": {
            "queries_used": len(HN_SEARCH_QUERIES),
            "results": unique_hn,
        },
    }

    write_json_output(output, "social.json")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Σ-Model Social Media Monitor")
    parser.add_argument("--format", choices=["json", "text"], default="text")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    result = run(verbose=args.verbose)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print("\n=== Σ-Model Social Monitor ===")
        for sub, posts in result["reddit"]["results"].items():
            if posts:
                print(f"\nr/{sub}: {len(posts)} posts")
                for p in posts:
                    print(f"  [{p['created_utc']}] {p['title']} (score={p['score']})")
        hn = result["hacker_news"]["results"]
        if hn:
            print(f"\nHacker News: {len(hn)} stories")
            for p in hn:
                print(f"  [{p['created_at']}] {p['title']} (points={p['points']})")


if __name__ == "__main__":
    main()
