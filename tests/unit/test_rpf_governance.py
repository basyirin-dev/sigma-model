"""RPF v2.0 Governance & Infrastructure Unit Tests."""

import yaml
from pathlib import Path
import pytest
from scripts.compliance_linter import lint_workspace
from scripts.check_phase_exit import check_p00

def test_seeds_registry_valid():
    seeds_path = Path("meta/seeds.yaml")
    assert seeds_path.exists(), "meta/seeds.yaml must exist."
    with open(seeds_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    assert "seeds" in data
    assert len(data["seeds"]) >= 3
    for seed in data["seeds"]:
        assert "seed_id" in seed
        assert "value" in seed
        assert isinstance(seed["value"], int)
        assert "provenance" in seed

def test_standards_rule_count():
    standards_path = Path("planning/standards.md")
    assert standards_path.exists()
    content = standards_path.read_text(encoding="utf-8")
    assert "### CC.1" in content
    assert "### CC.2" in content
    assert "### CC.3" in content
    assert "### CC.4" in content
    assert "### CC.5" in content
    assert "### CC.6" in content
    assert "### CC.7" in content

def test_p00_exit_check():
    passed, issues = check_p00()
    assert passed, f"P00 exit check failed with issues: {issues}"
