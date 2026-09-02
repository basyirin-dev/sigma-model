"""Unit tests for the multi-benchmark experimental matrix generator (Paper 02 Task 4.1)."""

from __future__ import annotations

from pathlib import Path

import pytest

from paper.src.config.matrix import (
    compute_matrix_summary,
    filter_manifests,
    generate_matrix_manifests,
    load_matrix_config,
    validate_manifests,
)


@pytest.fixture
def matrix_config_path() -> Path:
    path = Path("paper/experiments/configs/matrix_p04.yaml")
    assert path.exists(), f"Configuration file missing: {path}"
    return path


class TestMatrixLoadingAndGeneration:
    """Test loading and expansion of the experimental matrix."""

    def test_load_valid_config(self, matrix_config_path: Path) -> None:
        config = load_matrix_config(matrix_config_path)
        assert config["version"] == "2.0.0"
        assert "benchmarks" in config
        assert "architectures" in config
        assert "conditions" in config
        assert len(config["benchmarks"]) == 4
        assert len(config["architectures"]) == 3

    def test_load_nonexistent_config_raises(self) -> None:
        with pytest.raises(FileNotFoundError):
            load_matrix_config("nonexistent_path_to_matrix.yaml")

    def test_manifest_generation_counts(self, matrix_config_path: Path) -> None:
        config = load_matrix_config(matrix_config_path)
        manifests = generate_matrix_manifests(config)

        # 4 benchmarks x 3 architectures x (11 Arm A + 6 Arm B) conditions x 30 seeds
        # = 4 * 3 * 17 * 30 = 6120 runs
        expected_total = 4 * 3 * (11 + 6) * 30
        assert len(manifests) == expected_total
        assert validate_manifests(manifests)

    def test_manifest_determinism_and_hashing(self, matrix_config_path: Path) -> None:
        manifests_1 = generate_matrix_manifests(matrix_config_path)
        manifests_2 = generate_matrix_manifests(matrix_config_path)

        assert len(manifests_1) == len(manifests_2)
        for m1, m2 in zip(manifests_1, manifests_2, strict=True):
            assert m1.manifest_id == m2.manifest_id
            assert m1.hash_signature == m2.hash_signature
            assert m1.seed == m2.seed


class TestMatrixValidationAndFiltering:
    """Test manifest filtering, validation, and summary calculations."""

    def test_filter_by_benchmark(self, matrix_config_path: Path) -> None:
        manifests = generate_matrix_manifests(matrix_config_path)
        hbar_runs = filter_manifests(manifests, benchmark="hbar")

        # 1 benchmark x 3 architectures x 17 conditions x 30 seeds = 1530 runs
        assert len(hbar_runs) == 3 * 17 * 30
        assert all(m.benchmark == "hbar" for m in hbar_runs)

    def test_filter_by_architecture(self, matrix_config_path: Path) -> None:
        manifests = generate_matrix_manifests(matrix_config_path)
        arch_a_runs = filter_manifests(manifests, architecture="arch_a_transformer_2l")

        # 4 benchmarks x 1 architecture x 17 conditions x 30 seeds = 2040 runs
        assert len(arch_a_runs) == 4 * 17 * 30
        assert all(m.architecture == "arch_a_transformer_2l" for m in arch_a_runs)

    def test_filter_by_condition_type(self, matrix_config_path: Path) -> None:
        manifests = generate_matrix_manifests(matrix_config_path)
        arm_a_runs = filter_manifests(manifests, condition_type="arm_a_lambda")

        # 4 benchmarks x 3 architectures x 11 conditions x 30 seeds = 3960 runs
        assert len(arm_a_runs) == 4 * 3 * 11 * 30
        assert all(m.condition_type == "arm_a_lambda" for m in arm_a_runs)

    def test_matrix_summary_and_budget(self, matrix_config_path: Path) -> None:
        manifests = generate_matrix_manifests(matrix_config_path)
        summary = compute_matrix_summary(manifests, sec_per_run=60.0)

        assert summary.total_runs == len(manifests)
        assert summary.num_benchmarks == 4
        assert summary.num_architectures == 3
        assert summary.num_conditions == 2
        assert summary.estimated_gpu_hours == pytest.approx(
            (len(manifests) * 60.0) / 3600.0, rel=1e-2
        )
