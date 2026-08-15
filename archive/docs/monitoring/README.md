# Σ-Model Monitoring System

Post-submission monitoring infrastructure for the Σ-Model paper. Designed for AI ingestion — run on-demand, read the output, suggest paper changes.

## Architecture

```
code/sigma/monitoring/
  __init__.py      — Package init, run_all(), state management
  pub.py           — arXiv publication monitor (14 keyword clusters, relevance filtering)
  frameworks.py    — PyPI + GitHub releases (torch, numpy, scipy, etc.)
  datasets.py      — Upstream repo commit + errata scanner
  social.py        — Reddit + Hacker News search
  twitter.py       — Twitter/X API v2 (requires TWITTER_BEARER_TOKEN env var)
  report.py        — Aggregator → briefing.md
```

## Usage

```bash
# Run all monitors
sigma-monitor-all --since 2026-04-03 --verbose

# Individual monitors
sigma-monitor-pub --since 2026-04-03 --format json --verbose
sigma-monitor-frameworks --format json
sigma-monitor-datasets --since 2026-04-03 --format json
sigma-monitor-social --format json
sigma-monitor-twitter --format json

# Generate aggregated briefing
sigma-monitor-report --stdout
```

## Output Structure

```
docs/monitoring/
  briefing.md        — Latest aggregated briefing
  latest.json        — pub.py output
  frameworks.json    — frameworks.py output
  datasets.json      — datasets.py output
  social.json        — social.py output
  twitter.json       — twitter.py output
  .state.json        — Last-run timestamps (for date filtering)
  archive/           — Historical briefings (YYYY-MM-DD.md)
```

## What Each Monitor Checks

| Monitor | Source | What it checks | Action |
|---------|--------|----------------|--------|
| pub | arXiv API | New papers matching 14 keyword clusters with post-fetch relevance filtering | Suggest citations, flag threats to claims |
| frameworks | PyPI JSON API, GitHub Releases | Package versions vs pyproject.toml upper bounds | Alert if new version might break reproducibility |
| datasets | GitHub commits, issues | Upstream repos for new commits, errata keywords | Flag if dataset changed |
| social | Reddit search.json, HN Algolia API | Subreddits + HN for relevant discussions | Gauge reception |
| twitter | Twitter API v2 | Recent search for keyword clusters | Gauge reception (requires bearer token) |

## Design Principles

- **Stdlib-only**: No third-party dependencies beyond what pyproject.toml already requires
- **Date filtering**: All monitors accept `--since` and use `.state.json` for incremental runs
- **Deduplication**: Papers/posts deduplicated by URL across clusters
- **Relevance filtering**: arXiv results post-filtered against AI/ML keyword list to reduce false positives
- **JSON output**: All monitors produce structured JSON for downstream processing
- **Briefing aggregation**: `report.py` combines all JSON outputs into a single markdown briefing
