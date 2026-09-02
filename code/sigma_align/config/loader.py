# pyright: strict
from typing import Any, cast

import yaml


def load_config(path: str) -> dict[str, Any]:
    with open(path, "r") as f:
        data = cast(dict[str, Any], yaml.safe_load(f))
        return data


def merge_configs(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = base.copy()
    for k, v in override.items():
        if isinstance(v, dict) and k in merged and isinstance(merged[k], dict):
            sub_base = cast(dict[str, Any], merged[k])
            sub_override = cast(dict[str, Any], v)
            merged[k] = merge_configs(sub_base, sub_override)
        else:
            merged[k] = v
    return merged

