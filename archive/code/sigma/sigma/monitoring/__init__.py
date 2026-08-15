"""Σ-Model monitoring subsystem — publication alerts, framework tracking, dataset errata, social scans."""

from __future__ import annotations

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

MONITORING_DIR = Path(__file__).resolve().parents[3] / "docs" / "monitoring"
STATE_FILE = MONITORING_DIR / ".state.json"


def ensure_monitoring_dir() -> Path:
    MONITORING_DIR.mkdir(parents=True, exist_ok=True)
    (MONITORING_DIR / "archive").mkdir(exist_ok=True)
    return MONITORING_DIR


def load_state() -> dict[str, str]:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {}


def save_state(state: dict[str, str]) -> None:
    ensure_monitoring_dir()
    STATE_FILE.write_text(json.dumps(state, indent=2))


def last_run(cluster: str | None = None) -> str | None:
    state = load_state()
    if cluster:
        return state.get(f"{cluster}_last_run")
    return state.get("last_run")


def update_last_run(cluster: str | None = None) -> None:
    state = load_state()
    now = datetime.now().isoformat()
    if cluster:
        state[f"{cluster}_last_run"] = now
    state["last_run"] = now
    save_state(state)


def write_json_output(data: Any, filename: str) -> Path:
    path = ensure_monitoring_dir() / filename
    path.write_text(json.dumps(data, indent=2, default=str))
    return path


def run_all(since: str | None = None, verbose: bool = False) -> dict[str, Any]:
    results: dict[str, Any] = {}
    from .datasets import run as run_datasets
    from .frameworks import run as run_frameworks
    from .pub import run as run_pub
    from .social import run as run_social

    results["pub"] = run_pub(since=since, verbose=verbose)
    results["frameworks"] = run_frameworks(verbose=verbose)
    results["datasets"] = run_datasets(verbose=verbose)
    results["social"] = run_social(verbose=verbose)
    return results
