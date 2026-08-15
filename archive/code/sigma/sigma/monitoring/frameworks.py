"""Framework release monitor — checks PyPI for version updates against project dependencies."""

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

TRACKED_PACKAGES: dict[str, dict[str, str]] = {
    "numpy": {"current": ">=2.0,<3.0", "latest_known": "2.4.6"},
    "scipy": {"current": ">=1.14,<2.0", "latest_known": "1.17.1"},
    "torch": {"current": ">=2.10,<3.0", "latest_known": "2.12.0"},
    "matplotlib": {"current": ">=3.8,<4.0", "latest_known": "3.10.9"},
    "pandas": {"current": ">=2.0,<3.0", "latest_known": "2.3.3"},
    "datasets": {"current": ">=2.20,<3.0", "latest_known": "5.0.0"},
    "pyarrow": {"current": ">=14", "latest_known": "24.0.0"},
    "tikzplotlib": {"current": ">=0.10", "latest_known": "0.10.1"},
    "seaborn": {"current": ">=0.13", "latest_known": "0.13.2"},
    "triton": {"current": ">=3.0", "latest_known": "3.7.0"},
}

PYPI_API = "https://pypi.org/pypi/{package}/json"
GITHUB_RELEASES_API = "https://api.github.com/repos/{owner}/{repo}/releases/latest"

GITHUB_REPOS: dict[str, str] = {
    "torch": "pytorch/pytorch",
    "numpy": "numpy/numpy",
    "scipy": "scipy/scipy",
    "matplotlib": "matplotlib/matplotlib",
    "pandas": "pandas-dev/pandas",
    "datasets": "huggingface/datasets",
}


def fetch_pypi_latest(package: str) -> dict[str, Any]:
    url = PYPI_API.format(package=package)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Sigma-Monitor/2.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        info = data.get("info", {})
        versions = list(data.get("releases", {}).keys())
        return {
            "package": package,
            "latest_version": info.get("version", "unknown"),
            "summary": info.get("summary", ""),
            "requires_python": info.get("requires_python", ""),
            "home_page": info.get("home_page", ""),
            "release_date": _get_release_date(data),
            "all_versions": versions[-10:],
            "error": None,
        }
    except Exception as e:
        logger.error("PyPI query failed for %s: %s", package, e)
        return {"package": package, "error": str(e)}


def _get_release_date(pypi_data: dict) -> str:
    info = pypi_data.get("info", {})
    version = info.get("version", "")
    releases = pypi_data.get("releases", {})
    if version in releases:
        files = releases[version]
        if files:
            upload = files[0].get("upload_time_iso_8601", "")
            if upload:
                return upload[:10]
    return "unknown"


def fetch_github_latest(owner_repo: str) -> dict[str, Any]:
    url = GITHUB_RELEASES_API.format(owner=owner_repo.split("/")[0], repo=owner_repo.split("/")[1])
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Sigma-Monitor/2.0", "Accept": "application/vnd.github.v3+json"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read())
        return {
            "tag": data.get("tag_name", "unknown"),
            "name": data.get("name", ""),
            "published_at": data.get("published_at", "")[:10],
            "prerelease": data.get("prerelease", False),
            "url": data.get("html_url", ""),
            "error": None,
        }
    except Exception as e:
        logger.warning("GitHub query failed for %s: %s", owner_repo, e)
        return {"error": str(e)}


def _parse_upper_bound(constraint: str) -> str | None:
    for part in constraint.split(","):
        part = part.strip()
        if part.startswith("<"):
            return part[1:]
    return None


def _version_tuple(v: str) -> tuple[int, ...]:
    parts = []
    for p in v.split("."):
        try:
            parts.append(int(p))
        except ValueError:
            break
    return tuple(parts)


def run(verbose: bool = False) -> dict[str, Any]:
    if verbose:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    results: dict[str, Any] = {}

    for package, meta in TRACKED_PACKAGES.items():
        pypi = fetch_pypi_latest(package)
        github = None
        if package in GITHUB_REPOS:
            github = fetch_github_latest(GITHUB_REPOS[package])

        alert = False
        alert_reason = ""
        if not pypi.get("error") and pypi.get("latest_version"):
            upper = _parse_upper_bound(meta["current"])
            if upper:
                latest = pypi["latest_version"]
                if _version_tuple(latest) >= _version_tuple(upper):
                    alert = True
                    alert_reason = f"Latest {latest} >= upper bound {upper}"

        results[package] = {
            "pyproject_constraint": meta["current"],
            "pypi": pypi,
            "github": github,
            "alert": alert,
            "alert_reason": alert_reason,
        }

        if alert:
            logger.warning("ALERT %s: %s", package, alert_reason)
        elif verbose:
            logger.info("OK %s: %s", package, pypi.get("latest_version", "?"))

    output = {
        "timestamp": datetime.now().isoformat(),
        "total_packages": len(TRACKED_PACKAGES),
        "alerts": sum(1 for r in results.values() if r["alert"]),
        "packages": results,
    }

    write_json_output(output, "frameworks.json")
    return output


def main() -> None:
    parser = argparse.ArgumentParser(description="Σ-Model Framework Release Monitor")
    parser.add_argument("--format", choices=["json", "text"], default="text")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    result = run(verbose=args.verbose)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print("\n=== Σ-Model Framework Monitor ===")
        print(f"Checked: {result['total_packages']} packages")
        print(f"Alerts: {result['alerts']}")
        for pkg, data in result["packages"].items():
            status = "ALERT" if data["alert"] else "OK"
            ver = data["pypi"].get("latest_version", "error") if not data["pypi"].get("error") else "error"
            print(f"  [{status}] {pkg}: {ver} (constraint: {data['pyproject_constraint']})")
            if data["alert"]:
                print(f"         {data['alert_reason']}")


if __name__ == "__main__":
    main()
