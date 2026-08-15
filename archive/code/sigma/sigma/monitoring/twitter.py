"""Twitter/X monitor — stub for future implementation.

Twitter/X API v2 requires OAuth 2.0 Bearer Token authentication.
To enable this module:

1. Create a Twitter Developer account at https://developer.twitter.com
2. Create an App and generate a Bearer Token
3. Set environment variable: export TWITTER_BEARER_TOKEN="your-token-here"
4. The API endpoint is: https://api.twitter.com/2/tweets/search/recent

Rate limits: 450 requests per 15-minute window (app-level auth).

Suggested queries for Σ-Model monitoring:
- "compositional generalization"
- "schema coherence"
- "grokking phase transition"
- "Σ-Model"
- "sigma suppression"

Until authenticated, this module prints a no-op message.
"""

from __future__ import annotations

import argparse
import json
import logging
import os
from datetime import datetime
from typing import Any

from . import write_json_output

logger = logging.getLogger(__name__)

TWITTER_API = "https://api.twitter.com/2/tweets/search/recent"
BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN", "")

QUERIES = [
    "compositional generalization",
    "schema coherence AI",
    "grokking phase transition",
    "Σ-Model",
    "sigma suppression neural",
]


def run(verbose: bool = False) -> dict[str, Any]:
    if verbose:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    if not BEARER_TOKEN:
        logger.info("Twitter/X monitoring skipped: TWITTER_BEARER_TOKEN not set")
        output = {
            "timestamp": datetime.now().isoformat(),
            "status": "not_configured",
            "message": (
                "Twitter/X API requires OAuth 2.0 Bearer Token. "
                "Set TWITTER_BEARER_TOKEN environment variable. "
                "See module docstring for setup instructions."
            ),
            "queries_skipped": QUERIES,
            "results": [],
        }
        write_json_output(output, "twitter.json")
        return output

    import urllib.error
    import urllib.parse
    import urllib.request

    all_tweets: list[dict[str, str]] = []
    for query in QUERIES:
        params = urllib.parse.urlencode({
            "query": query,
            "max_results": 10,
            "tweet.fields": "created_at,public_metrics,author_id",
            "sort_order": "recency",
        })
        url = f"{TWITTER_API}?{params}"
        try:
            req = urllib.request.Request(url, headers={
                "Authorization": f"Bearer {BEARER_TOKEN}",
                "User-Agent": "Sigma-Monitor/2.0",
            })
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = json.loads(resp.read())
            for tweet in data.get("data", []):
                metrics = tweet.get("public_metrics", {})
                all_tweets.append({
                    "id": tweet.get("id", ""),
                    "text": tweet.get("text", "")[:280],
                    "created_at": (tweet.get("created_at") or "")[:10],
                    "author_id": tweet.get("author_id", ""),
                    "retweets": metrics.get("retweet_count", 0),
                    "likes": metrics.get("like_count", 0),
                    "query": query,
                    "url": f"https://twitter.com/i/status/{tweet.get('id', '')}",
                })
        except Exception as e:
            logger.error("Twitter query failed for '%s': %s", query, e)

    output = {
        "timestamp": datetime.now().isoformat(),
        "status": "active",
        "total_tweets": len(all_tweets),
        "results": all_tweets,
    }
    write_json_output(output, "twitter.json")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Σ-Model Twitter/X Monitor")
    parser.add_argument("--format", choices=["json", "text"], default="text")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    result = run(verbose=args.verbose)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print("\n=== Σ-Model Twitter/X Monitor ===")
        if result["status"] == "not_configured":
            print("Status: NOT CONFIGURED")
            print(f"Message: {result['message']}")
        else:
            print("Status: ACTIVE")
            print(f"Tweets found: {result['total_tweets']}")
            for t in result["results"]:
                print(f"  [{t['created_at']}] {t['text'][:80]}...")
                print(f"    {t['url']}")


if __name__ == "__main__":
    main()
