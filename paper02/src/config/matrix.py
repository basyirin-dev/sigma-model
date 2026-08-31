"""Experimental Matrix Configuration and Manifest Generation for Paper 02.

This module formalizes the multi-benchmark experimental matrix under RPF v2.0
(Task 4.1), translating declarative YAML configs into structured, deterministic,
and machine-verifiable execution manifests.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class BenchmarkSpec:
    """Specification of a compositional benchmark suite."""

    key: str
    name: str
    domain: str
    vocab_size: int
    splits: dict[str, Any]
    dataset_sizes: dict[str, int]


@dataclass(frozen=True)
class ArchitectureSpec:
    """Specification of a sequence model architecture."""

    key: str
    family: str
    name: str
    d_model: int
    num_layers: int
    extra_params: dict[str, Any]


@dataclass(frozen=True)
class ConditionSpec:
    """Specification of an experimental supervision condition."""

    key: str
    condition_type: str
    description: str
    params: dict[str, Any]


@dataclass(frozen=True)
class ExperimentManifest:
    """A fully-resolved, immutable execution manifest for a single experimental run."""

    manifest_id: str
    benchmark: str
    split: str
    architecture: str
    condition_type: str
    condition_name: str
    lambda_val: float
    intervention_step: int | None
    seed: int
    run_id: int
    max_steps: int
    batch_size: int
    lr: float
    deterministic: bool
    hash_signature: str

    def to_dict(self) -> dict[str, Any]:
        """Convert manifest to serializable dictionary."""
        return asdict(self)


@dataclass(frozen=True)
class MatrixSummary:
    """Summary metrics of the expanded experimental matrix."""

    total_runs: int
    num_benchmarks: int
    num_architectures: int
    num_conditions: int
    runs_by_benchmark: dict[str, int]
    runs_by_architecture: dict[str, int]
    runs_by_condition_type: dict[str, int]
    estimated_gpu_hours: float


def load_matrix_config(yaml_path: str | Path) -> dict[str, Any]:
    """Load and parse the declarative matrix YAML configuration."""
    path = Path(yaml_path)
    if not path.exists():
        raise FileNotFoundError(f"Matrix config not found at: {path}")
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError("Invalid YAML format: root must be a mapping.")
    return data


def _generate_manifest_hash(manifest_dict: dict[str, Any]) -> str:
    """Generate deterministic SHA-256 signature for an experiment manifest."""
    serialized = json.dumps(manifest_dict, sort_keys=True)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()[:16]


def generate_matrix_manifests(
    config_or_path: dict[str, Any] | str | Path,
) -> list[ExperimentManifest]:
    """Expand a declarative matrix configuration into a complete list of execution manifests.

    Args:
        config_or_path: Parsed config dictionary or path to YAML config file.

    Returns:
        List of immutable, fully-resolved ExperimentManifest instances.
    """
    if isinstance(config_or_path, (str, Path)):
        config = load_matrix_config(config_or_path)
    else:
        config = config_or_path

    global_cfg = config.get("global", {})
    seed_base = int(global_cfg.get("seed_base", 42))
    seed_offset = int(global_cfg.get("seed_offset", 7))
    num_seeds = int(global_cfg.get("num_seeds", 30))
    deterministic = bool(global_cfg.get("deterministic", True))
    max_steps = int(global_cfg.get("training", {}).get("max_steps", 2000))
    batch_size = int(global_cfg.get("training", {}).get("batch_size", 64))
    lr = float(global_cfg.get("optimizer", {}).get("lr", 0.001))

    benchmarks = config.get("benchmarks", {})
    architectures = config.get("architectures", {})
    conditions = config.get("conditions", {})

    manifests: list[ExperimentManifest] = []

    for bench_key, bench_data in benchmarks.items():
        splits = bench_data.get("splits", {})
        default_split = next(iter(splits.keys())) if splits else "default"

        for arch_key in architectures:
            # Expand Arm A: Dense Lambda Sweep
            if "arm_a_dense_pressure_sweep" in conditions:
                cond_data = conditions["arm_a_dense_pressure_sweep"]
                lambda_grid = cond_data.get("lambda_grid", [0.0, 1.0])

                for lam in lambda_grid:
                    lam_val = float(lam)
                    cond_name = f"arm_a_lambda_{lam_val:.3f}"

                    for run_id in range(num_seeds):
                        seed = run_id * seed_base + seed_offset
                        raw_payload = {
                            "benchmark": bench_key,
                            "split": default_split,
                            "architecture": arch_key,
                            "condition_type": "arm_a_lambda",
                            "condition_name": cond_name,
                            "lambda_val": lam_val,
                            "intervention_step": None,
                            "seed": seed,
                            "run_id": run_id,
                            "max_steps": max_steps,
                            "batch_size": batch_size,
                            "lr": lr,
                        }
                        hash_sig = _generate_manifest_hash(raw_payload)
                        manifest_id = (
                            f"{bench_key}_{arch_key}_{cond_name}_seed_{run_id:02d}_{hash_sig[:6]}"
                        )

                        manifest = ExperimentManifest(
                            manifest_id=manifest_id,
                            benchmark=bench_key,
                            split=default_split,
                            architecture=arch_key,
                            condition_type="arm_a_lambda",
                            condition_name=cond_name,
                            lambda_val=lam_val,
                            intervention_step=None,
                            seed=seed,
                            run_id=run_id,
                            max_steps=max_steps,
                            batch_size=batch_size,
                            lr=lr,
                            deterministic=deterministic,
                            hash_signature=hash_sig,
                        )
                        manifests.append(manifest)

            # Expand Arm B: Late Intervention
            if "arm_b_late_intervention" in conditions:
                cond_data = conditions["arm_b_late_intervention"]
                fixed_lam = float(cond_data.get("fixed_lambda", 1.0))
                intervention_steps = cond_data.get("intervention_steps", [0, 500, 1000])

                for t_int in intervention_steps:
                    t_int_val = int(t_int)
                    cond_name = f"arm_b_tint_{t_int_val}"

                    for run_id in range(num_seeds):
                        seed = run_id * seed_base + seed_offset
                        raw_payload = {
                            "benchmark": bench_key,
                            "split": default_split,
                            "architecture": arch_key,
                            "condition_type": "arm_b_late_intervention",
                            "condition_name": cond_name,
                            "lambda_val": fixed_lam,
                            "intervention_step": t_int_val,
                            "seed": seed,
                            "run_id": run_id,
                            "max_steps": max_steps,
                            "batch_size": batch_size,
                            "lr": lr,
                        }
                        hash_sig = _generate_manifest_hash(raw_payload)
                        manifest_id = (
                            f"{bench_key}_{arch_key}_{cond_name}_seed_{run_id:02d}_{hash_sig[:6]}"
                        )

                        manifest = ExperimentManifest(
                            manifest_id=manifest_id,
                            benchmark=bench_key,
                            split=default_split,
                            architecture=arch_key,
                            condition_type="arm_b_late_intervention",
                            condition_name=cond_name,
                            lambda_val=fixed_lam,
                            intervention_step=t_int_val,
                            seed=seed,
                            run_id=run_id,
                            max_steps=max_steps,
                            batch_size=batch_size,
                            lr=lr,
                            deterministic=deterministic,
                            hash_signature=hash_sig,
                        )
                        manifests.append(manifest)

    return manifests


def validate_manifests(manifests: list[ExperimentManifest]) -> bool:
    """Verify structural validity and uniqueness invariants across generated manifests."""
    if not manifests:
        raise ValueError("Manifest list is empty.")

    manifest_ids: set[str] = set()
    condition_seeds: dict[tuple[str, str, str, str], set[int]] = {}

    for m in manifests:
        # Check manifest ID uniqueness
        if m.manifest_id in manifest_ids:
            raise ValueError(f"Duplicate manifest ID detected: {m.manifest_id}")
        manifest_ids.add(m.manifest_id)

        # Check parameter bounds
        if m.lambda_val < 0.0:
            raise ValueError(f"Invalid negative lambda_val in manifest: {m.manifest_id}")
        if m.max_steps <= 0:
            raise ValueError(f"Invalid max_steps <= 0 in manifest: {m.manifest_id}")
        if m.batch_size <= 0:
            raise ValueError(f"Invalid batch_size <= 0 in manifest: {m.manifest_id}")

        # Check seed uniqueness per cell
        cell_key = (m.benchmark, m.architecture, m.condition_type, m.condition_name)
        if cell_key not in condition_seeds:
            condition_seeds[cell_key] = set()
        if m.seed in condition_seeds[cell_key]:
            raise ValueError(
                f"Duplicate seed {m.seed} detected in cell {cell_key} for manifest {m.manifest_id}"
            )
        condition_seeds[cell_key].add(m.seed)

    return True


def compute_matrix_summary(
    manifests: list[ExperimentManifest], sec_per_run: float = 70.0
) -> MatrixSummary:
    """Compute summary statistics and compute budget for a set of manifests."""
    runs_by_bench: dict[str, int] = {}
    runs_by_arch: dict[str, int] = {}
    runs_by_cond: dict[str, int] = {}

    for m in manifests:
        runs_by_bench[m.benchmark] = runs_by_bench.get(m.benchmark, 0) + 1
        runs_by_arch[m.architecture] = runs_by_arch.get(m.architecture, 0) + 1
        runs_by_cond[m.condition_type] = runs_by_cond.get(m.condition_type, 0) + 1

    total_runs = len(manifests)
    total_gpu_hours = (total_runs * sec_per_run) / 3600.0

    return MatrixSummary(
        total_runs=total_runs,
        num_benchmarks=len(runs_by_bench),
        num_architectures=len(runs_by_arch),
        num_conditions=len(runs_by_cond),
        runs_by_benchmark=runs_by_bench,
        runs_by_architecture=runs_by_arch,
        runs_by_condition_type=runs_by_cond,
        estimated_gpu_hours=round(total_gpu_hours, 2),
    )


def generate_tiered_manifests(
    config_or_path: dict[str, Any] | str | Path,
    tier: int | str = "all",
) -> list[ExperimentManifest]:
    """Generate authorized Tier 1 and Tier 2 Phase 06 manifests.

    Tier 1 (Primary Falsification): 4 benchmarks x 1 arch x 6 lambdas x 30 seeds = 720 runs.
    Tier 2 (Exploratory Scaling): 4 benchmarks x 2 archs x 3 lambdas x 10 seeds = 240 runs.
    """
    if isinstance(config_or_path, (str, Path)):
        config = load_matrix_config(config_or_path)
    else:
        config = config_or_path

    global_cfg = config.get("global", {})
    seed_base = int(global_cfg.get("seed_base", 42))
    seed_offset = int(global_cfg.get("seed_offset", 7))
    deterministic = bool(global_cfg.get("deterministic", True))
    max_steps = int(global_cfg.get("training", {}).get("max_steps", 2000))
    batch_size = int(global_cfg.get("training", {}).get("batch_size", 64))
    lr = float(global_cfg.get("optimizer", {}).get("lr", 0.001))

    benchmarks = config.get("benchmarks", {})
    manifests: list[ExperimentManifest] = []

    # Generate Tier 1: Primary Change-Point Matrix
    if tier in (1, "1", "all", "both"):
        tier1_arch = "arch_a_transformer_2l"
        tier1_lambdas = [0.000, 0.015, 0.020, 0.025, 0.030, 0.500]
        tier1_seeds = 30

        for bench_key, bench_data in benchmarks.items():
            splits = bench_data.get("splits", {})
            default_split = next(iter(splits.keys())) if splits else "default"

            for lam in tier1_lambdas:
                lam_val = float(lam)
                cond_name = f"tier1_lambda_{lam_val:.3f}"

                for run_id in range(tier1_seeds):
                    seed = run_id * seed_base + seed_offset
                    raw_payload = {
                        "benchmark": bench_key,
                        "split": default_split,
                        "architecture": tier1_arch,
                        "condition_type": "tier_1_primary",
                        "condition_name": cond_name,
                        "lambda_val": lam_val,
                        "intervention_step": None,
                        "seed": seed,
                        "run_id": run_id,
                        "max_steps": max_steps,
                        "batch_size": batch_size,
                        "lr": lr,
                    }
                    hash_sig = _generate_manifest_hash(raw_payload)
                    manifest_id = (
                        f"p06_t1_{bench_key}_{tier1_arch}_{cond_name}_seed_{run_id:02d}_{hash_sig[:6]}"
                    )

                    manifest = ExperimentManifest(
                        manifest_id=manifest_id,
                        benchmark=bench_key,
                        split=default_split,
                        architecture=tier1_arch,
                        condition_type="tier_1_primary",
                        condition_name=cond_name,
                        lambda_val=lam_val,
                        intervention_step=None,
                        seed=seed,
                        run_id=run_id,
                        max_steps=max_steps,
                        batch_size=batch_size,
                        lr=lr,
                        deterministic=deterministic,
                        hash_signature=hash_sig,
                    )
                    manifests.append(manifest)

    # Generate Tier 2: Exploratory Scaling Matrix
    if tier in (2, "2", "all", "both"):
        tier2_archs = ["arch_b_transformer_4l", "arch_c_recurrent_gru"]
        tier2_lambdas = [0.000, 0.025, 0.500]
        tier2_seeds = 10

        for bench_key, bench_data in benchmarks.items():
            splits = bench_data.get("splits", {})
            default_split = next(iter(splits.keys())) if splits else "default"

            for arch_key in tier2_archs:
                for lam in tier2_lambdas:
                    lam_val = float(lam)
                    cond_name = f"tier2_lambda_{lam_val:.3f}"

                    for run_id in range(tier2_seeds):
                        seed = run_id * seed_base + seed_offset
                        raw_payload = {
                            "benchmark": bench_key,
                            "split": default_split,
                            "architecture": arch_key,
                            "condition_type": "tier_2_exploratory",
                            "condition_name": cond_name,
                            "lambda_val": lam_val,
                            "intervention_step": None,
                            "seed": seed,
                            "run_id": run_id,
                            "max_steps": max_steps,
                            "batch_size": batch_size,
                            "lr": lr,
                        }
                        hash_sig = _generate_manifest_hash(raw_payload)
                        manifest_id = (
                            f"p06_t2_{bench_key}_{arch_key}_{cond_name}_seed_{run_id:02d}_{hash_sig[:6]}"
                        )

                        manifest = ExperimentManifest(
                            manifest_id=manifest_id,
                            benchmark=bench_key,
                            split=default_split,
                            architecture=arch_key,
                            condition_type="tier_2_exploratory",
                            condition_name=cond_name,
                            lambda_val=lam_val,
                            intervention_step=None,
                            seed=seed,
                            run_id=run_id,
                            max_steps=max_steps,
                            batch_size=batch_size,
                            lr=lr,
                            deterministic=deterministic,
                            hash_signature=hash_sig,
                        )
                        manifests.append(manifest)

    return manifests


def filter_manifests(
    manifests: list[ExperimentManifest],
    benchmark: str | None = None,
    architecture: str | None = None,
    condition_type: str | None = None,
) -> list[ExperimentManifest]:
    """Filter manifests by benchmark, architecture, or condition type."""
    filtered = manifests
    if benchmark is not None:
        filtered = [m for m in filtered if m.benchmark == benchmark]
    if architecture is not None:
        filtered = [m for m in filtered if m.architecture == architecture]
    if condition_type is not None:
        filtered = [m for m in filtered if m.condition_type == condition_type]
    return filtered
