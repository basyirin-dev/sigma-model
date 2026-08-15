import os

import pytest
from sigma.config import load_config, merge_configs

CONFIG_DIR = "experiments/configs"
BASE = os.path.join(CONFIG_DIR, "base.yaml")
ALL_CONFIGS = [
    "base.yaml",
    "h-ptb.yaml",
    "h-afb.yaml",
    "h-mcb.yaml",
    "h-dcb.yaml",
    "h-stb.yaml",
]


def test_all_configs_exist():
    for cfg in ALL_CONFIGS:
        path = os.path.join(CONFIG_DIR, cfg)
        assert os.path.isfile(path), f"Missing config: {path}"


def test_base_config_loads():
    cfg = load_config(BASE)
    assert isinstance(cfg, dict)
    assert len(cfg) > 0, "Base config should have keys"


def test_base_config_has_core_keys():
    cfg = load_config(BASE)
    assert "model" in cfg, "base config should have 'model'"
    assert "training" in cfg, "base config should have 'training'"
    assert "ode" in cfg, "base config should have 'ode'"


def test_ptb_config_has_override():
    cfg = load_config(os.path.join(CONFIG_DIR, "h-ptb.yaml"))
    assert cfg.get("benchmark") is not None, "Benchmark configs should have a benchmark key"


def test_afb_config_has_override():
    cfg = load_config(os.path.join(CONFIG_DIR, "h-afb.yaml"))
    assert cfg.get("benchmark") is not None


def test_mcb_config_has_override():
    cfg = load_config(os.path.join(CONFIG_DIR, "h-mcb.yaml"))
    assert cfg.get("benchmark") is not None


def test_dcb_config_has_override():
    cfg = load_config(os.path.join(CONFIG_DIR, "h-dcb.yaml"))
    assert cfg.get("benchmark") is not None


def test_stb_config_has_override():
    cfg = load_config(os.path.join(CONFIG_DIR, "h-stb.yaml"))
    assert cfg.get("benchmark") is not None


def test_merge_configs_deep():
    base = {"a": 1, "b": {"c": 2, "d": 3}}
    override = {"b": {"c": 99}, "e": 4}
    merged = merge_configs(base, override)
    assert merged["a"] == 1
    assert merged["b"]["c"] == 99
    assert merged["b"]["d"] == 3
    assert merged["e"] == 4


def test_merge_configs_override_scalar():
    base = {"x": 1, "y": 2}
    override = {"x": 99}
    merged = merge_configs(base, override)
    assert merged["x"] == 99
    assert merged["y"] == 2


def test_merge_configs_empty_override():
    base = {"a": 1}
    merged = merge_configs(base, {})
    assert merged == base


def test_load_config_raises_on_missing():
    with pytest.raises(FileNotFoundError):
        load_config("nonexistent.yaml")
