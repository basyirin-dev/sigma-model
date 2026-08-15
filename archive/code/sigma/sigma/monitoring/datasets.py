"""Dataset errata monitor — checks upstream repos for commits, issues, and deprecation notices."""

from __future__ import annotations

import argparse
import json
import logging
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from typing import Any

from . import write_json_output

logger = logging.getLogger(__name__)

TRACKED_DATASETS: dict[str, dict[str, str | None]] = {
    "SCAN": {
        "owner_repo": "brendenlake/SCAN",
        "pinned_commit": "c4b756cbc010d75c912f16c42c8f15dc6b7e6c8f",
    },
    "COGS": {
        "owner_repo": "najoungkim/COGS",
        "pinned_commit": None,
    },
    "PCFG-SET": {
        "owner_repo": "i-machine-think/am-i-compositional",
        "pinned_commit": "4f75bdd78889150dd78e90bbb7ddec840204c159",
    },
}

GITHUB_API = "https://api.github.com"


def _gh_get(path: str) -> dict | list | None:
    url = f"{GITHUB_API}{path}"
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": "Sigma-Monitor/2.0",
            "Accept": "application/vnd.github.v3+json",
        })
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        logger.warning("GitHub API error %s for %s: %s", e.code, path, e.reason)
        return None
    except Exception as e:
        logger.error("GitHub request failed for %s: %s", path, e)
        return None


def fetch_recent_commits(owner_repo: str, since: str = "2026-04-03") -> list[dict[str, str]]:
    path = f"/repos/{owner_repo}/commits?since={since}T00:00:00Z&per_page=10"
    data = _gh_get(path)
    if data is None or not isinstance(data, list):
        return []
    commits = []
    for c in data:
        sha = c.get("sha", "")[:12]
        msg = c.get("commit", {}).get("message", "").split("\n")[0][:120]
        date = c.get("commit", {}).get("author", {}).get("date", "")[:10]
        author = c.get("commit", {}).get("author", {}).get("name", "unknown")
        commits.append({"sha": sha, "message": msg, "date": date, "author": author})
    return commits


def fetch_recent_issues(owner_repo: str, since: str = "2026-04-03") -> list[dict[str, str]]:
    path = f"/repos/{owner_repo}/issues?state=all&since={since}T00:00:00Z&per_page=10&sort=updated"
    data = _gh_get(path)
    if data is None or not isinstance(data, list):
        return []
    issues = []
    errata_keywords = ["errata", "bug", "fix", "deprecat", "wrong", "incorrect", "broken"]
    for issue in data:
        title = issue.get("title", "")
        body = (issue.get("body") or "")[:200]
        labels = [l.get("name", "") for l in issue.get("labels", [])]
        is_errata = any(kw in title.lower() or kw in body.lower() for kw in errata_keywords)
        issues.append({
            "number": issue.get("number", 0),
            "title": title,
            "state": issue.get("state", "unknown"),
            "created_at": (issue.get("created_at") or "")[:10],
            "labels": labels,
            "is_potential_errata": is_errata,
            "url": issue.get("html_url", ""),
        })
    return issues


def check_commit_ahead(owner_repo: str, pinned_commit: str | None) -> dict[str, Any]:
    if not pinned_commit:
        return {"has_new_commits": False, "reason": "No pinned commit to compare"}
    commits = fetch_recent_commits(owner_repo)
    new_after_pin = [c for c in commits if c["date"] > "2026-04-03"]
    return {
        "has_new_commits": len(new_after_pin) > 0,
        "new_commit_count": len(new_after_pin),
        "commits": new_after_pin,
    }


def run(verbose: bool = False, since: str = "2026-04-03") -> dict[str, Any]:
    if verbose:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    results: dict[str, Any] = {}
    for name, meta in TRACKED_DATASETS.items():
        owner_repo = str(meta["owner_repo"])
        pinned_commit = meta["pinned_commit"]
        logger.info("Checking %s (%s)", name, owner_repo)
        commit_check = check_commit_ahead(owner_repo, pinned_commit)
        issues = fetch_recent_issues(owner_repo, since=since)
        errata_issues = [i for i in issues if i["is_potential_errata"]]

        alert = commit_check["has_new_commits"] or len(errata_issues) > 0
        results[name] = {
            "owner_repo": meta["owner_repo"],
            "pinned_commit": meta["pinned_commit"],
            "commit_check": commit_check,
            "total_issues": len(issues),
            "errata_issues": errata_issues,
            "alert": alert,
        }
        if alert:
            logger.warning("ALERT %s: new commits=%d, errata issues=%d",
                           name, commit_check.get("new_commit_count", 0), len(errata_issues))

    output = {
        "timestamp": datetime.now().isoformat(),
        "since": since,
        "total_datasets": len(TRACKED_DATASETS),
        "alerts": sum(1 for r in results.values() if r["alert"]),
        "datasets": results,
    }

    write_json_output(output, "datasets.json")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Σ-Model Dataset Errata Monitor")
    parser.add_argument("--since", default="2026-04-03")
    parser.add_argument("--format", choices=["json", "text"], default="text")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    result = run(verbose=args.verbose, since=args.since)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print("\n=== Σ-Model Dataset Monitor ===")
        print(f"Since: {result['since']}")
        print(f"Datasets: {result['total_datasets']}")
        print(f"Alerts: {result['alerts']}")
        for name, data in result["datasets"].items():
            status = "ALERT" if data["alert"] else "OK"
            commits = data["commit_check"].get("new_commit_count", 0)
            errata = len(data["errata_issues"])
            print(f"  [{status}] {name}: {commits} new commits, {errata} errata issues")
            if data["alert"]:
                for issue in data["errata_issues"]:
                    print(f"    Issue #{issue['number']}: {issue['title']}")


if __name__ == "__main__":
    main()
