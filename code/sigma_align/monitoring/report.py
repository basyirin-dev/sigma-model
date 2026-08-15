"""Aggregator — reads all monitoring JSON outputs and produces a markdown briefing."""

from __future__ import annotations

import argparse
import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any

from . import MONITORING_DIR, ensure_monitoring_dir

logger = logging.getLogger(__name__)


def _load_json(filename: str) -> dict[str, Any] | None:
    path = MONITORING_DIR / filename
    if not path.exists():
        logger.warning("File not found: %s", path)
        return None
    return json.loads(path.read_text())


def _format_pub_section(data: dict[str, Any] | None) -> str:
    if data is None:
        return "## Publications\n\n_No data available._\n\n"
    lines = ["## Publications\n\n"]
    lines.append(f"**Since:** {data.get('since', 'N/A')}  \n")
    lines.append(f"**Total new papers:** {data.get('total_new_papers', 0)}  \n\n")

    for cluster_name, cluster_data in data.get("clusters", {}).items():
        papers = cluster_data.get("papers", [])
        if not papers:
            continue
        readable = cluster_name.replace("_", " ").title()
        lines.append(f"### {readable} ({len(papers)} papers)\n\n")
        for p in papers:
            title = p.get("title", "N/A")
            date = p.get("date", "N/A")
            url = p.get("url", "")
            authors = ", ".join(p.get("authors", [])[:3])
            if len(p.get("authors", [])) > 3:
                authors += " et al."
            summary = p.get("summary", "")[:150]
            lines.append(f"- **{title}** ({date})")
            if authors:
                lines.append(f"  - Authors: {authors}")
            if url:
                lines.append(f"  - URL: {url}")
            if summary:
                lines.append(f"  - Summary: {summary}...")
            lines.append("")
    return "".join(lines)


def _format_frameworks_section(data: dict[str, Any] | None) -> str:
    if data is None:
        return "## Framework Releases\n\n_No data available._\n\n"
    lines = ["## Framework Releases\n\n"]
    alerts = data.get("alerts", 0)
    lines.append(f"**Packages checked:** {data.get('total_packages', 0)}  \n")
    lines.append(f"**Alerts:** {alerts}  \n\n")

    for pkg, pkg_data in data.get("packages", {}).items():
        status = "ALERT" if pkg_data.get("alert") else "OK"
        ver = pkg_data.get("pypi", {}).get("latest_version", "error")
        constraint = pkg_data.get("pyproject_constraint", "")
        lines.append(f"- **{pkg}**: v{ver} (constraint: {constraint}) — [{status}]")
        if pkg_data.get("alert"):
            lines.append(f"  - _{pkg_data.get('alert_reason', '')}_")
        gh = pkg_data.get("github", {})
        if gh and not gh.get("error"):
            lines.append(f"  - GitHub latest: {gh.get('tag', '?')} ({gh.get('published_at', '?')})")
    lines.append("")
    return "".join(lines)


def _format_datasets_section(data: dict[str, Any] | None) -> str:
    if data is None:
        return "## Dataset Errata\n\n_No data available._\n\n"
    lines = ["## Dataset Errata\n\n"]
    alerts = data.get("alerts", 0)
    lines.append(f"**Datasets checked:** {data.get('total_datasets', 0)}  \n")
    lines.append(f"**Alerts:** {alerts}  \n\n")

    for name, ds_data in data.get("datasets", {}).items():
        status = "ALERT" if ds_data.get("alert") else "OK"
        cc = ds_data.get("commit_check", {})
        new_commits = cc.get("new_commit_count", 0)
        errata = len(ds_data.get("errata_issues", []))
        lines.append(f"- **{name}** ({ds_data.get('owner_repo', '?')}): [{status}]")
        lines.append(f"  - New commits since {data.get('since', '?')}: {new_commits}")
        if ds_data.get("pinned_commit"):
            lines.append(f"  - Pinned: `{ds_data['pinned_commit'][:12]}`")
        if errata > 0:
            lines.append("  - **Potential errata issues:**")
            for issue in ds_data.get("errata_issues", []):
                lines.append(f"    - #{issue['number']}: {issue['title']} ({issue['state']})")
    lines.append("")
    return "".join(lines)


def _format_social_section(data: dict[str, Any] | None) -> str:
    if data is None:
        return "## Social Media\n\n_No data available._\n\n"
    lines = ["## Social Media\n\n"]

    reddit = data.get("reddit", {})
    for sub, posts in reddit.get("results", {}).items():
        if not posts:
            continue
        lines.append(f"### r/{sub} ({len(posts)} posts)\n\n")
        for p in posts:
            lines.append(f"- [{p.get('created_utc', '?')}] {p.get('title', 'N/A')} "
                         f"(score={p.get('score', 0)}, comments={p.get('num_comments', 0)})")
            lines.append(f"  - {p.get('url', '')}")
        lines.append("")

    hn = data.get("hacker_news", {}).get("results", [])
    if hn:
        lines.append(f"### Hacker News ({len(hn)} stories)\n\n")
        for p in hn:
            lines.append(f"- [{p.get('created_at', '?')}] {p.get('title', 'N/A')} "
                         f"(points={p.get('points', 0)}, comments={p.get('num_comments', 0)})")
            lines.append(f"  - {p.get('url', '')}")
        lines.append("")

    twitter = data.get("twitter")
    if twitter:
        if twitter.get("status") == "not_configured":
            lines.append("### Twitter/X\n\n_Status: not configured (set TWITTER_BEARER_TOKEN)_\n\n")
        else:
            tweets = twitter.get("results", [])
            if tweets:
                lines.append(f"### Twitter/X ({len(tweets)} tweets)\n\n")
                for t in tweets:
                    lines.append(f"- [{t.get('created_at', '?')}] {t.get('text', '')[:100]}...")
                    lines.append(f"  - {t.get('url', '')}")
                lines.append("")

    return "".join(lines)


def _action_items(pub: dict | None, fw: dict | None, ds: dict | None) -> str:
    items = []
    if pub and pub.get("total_new_papers", 0) > 0:
        items.append("- **Review new papers** for citation opportunities or claim challenges.")
    if fw and fw.get("alerts", 0) > 0:
        items.append("- **Framework alerts**: new versions may exceed pyproject.toml upper bounds.")
    if ds and ds.get("alerts", 0) > 0:
        items.append("- **Dataset alerts**: upstream changes detected — verify reproducibility.")
    if not items:
        items.append("- No action items. All clear.")
    return "## Action Items\n\n" + "\n".join(items) + "\n\n"


def generate_briefing() -> str:
    pub = _load_json("latest.json")
    fw = _load_json("frameworks.json")
    ds = _load_json("datasets.json")
    social = _load_json("social.json")
    twitter = _load_json("twitter.json")
    if social and twitter:
        social["twitter"] = twitter

    now = datetime.now()
    header = (
        f"# Σ-Model Monitoring Briefing\n\n"
        f"**Generated:** {now.strftime('%Y-%m-%d %H:%M')}  \n\n"
        f"---\n\n"
    )
    body = (
        _action_items(pub, fw, ds)
        + _format_pub_section(pub)
        + _format_frameworks_section(fw)
        + _format_datasets_section(ds)
        + _format_social_section(social)
    )
    footer = f"\n---\n\n_Generated by `sigma-monitor-report` at {now.isoformat()}_\n"
    return header + body + footer


def run(verbose: bool = False) -> Path:
    ensure_monitoring_dir()
    briefing = generate_briefing()

    main_path = MONITORING_DIR / "briefing.md"
    main_path.write_text(briefing)
    logger.info("Briefing written to %s", main_path)

    archive_path = MONITORING_DIR / "archive" / f"{datetime.now().strftime('%Y-%m-%d')}.md"
    archive_path.write_text(briefing)
    logger.info("Archive written to %s", archive_path)

    return main_path


def main() -> None:
    parser = argparse.ArgumentParser(description="Σ-Model Monitoring Report Generator")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--stdout", action="store_true", help="Print briefing to stdout")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    path = run(verbose=args.verbose)
    print(f"Briefing written to: {path}")

    if args.stdout:
        print(path.read_text())


if __name__ == "__main__":
    main()
