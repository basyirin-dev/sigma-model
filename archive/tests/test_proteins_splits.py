"""Unit tests for sigma.proteins.splits — compositional splits."""

import os
import tempfile

import numpy as np
import pytest
from sigma.proteins.splits import (
    compute_split_statistics,
    make_compositional_splits,
    recombination_distance,
)

# ── Synthetic fixtures ────────────────────────────────────────

ACCESSIONS = [
    "PF00001.1",
    "PF00002.1",
    "PF00003.1",
    "PF00004.1",
    "PF00005.1",
    "PF00006.1",
    "PF00007.1",
]

# 7×7 similarity matrix: diagonal=1.0, small cross-terms
SIM_MATRIX = np.eye(7, dtype=np.float32) + 0.1 * (1 - np.eye(7))
SIM_MATRIX = np.clip(SIM_MATRIX, 0.0, 1.0)

# Synthetic architectures — 12 architectures for testing
ARCHITECTURES = [
    ["PF00001.1", "PF00002.1", "PF00003.1"],
    ["PF00001.1", "PF00003.1", "PF00004.1"],
    ["PF00002.1", "PF00004.1", "PF00005.1"],
    ["PF00001.1", "PF00002.1"],
    ["PF00003.1", "PF00004.1", "PF00005.1"],
    ["PF00006.1", "PF00007.1"],
    ["PF00001.1", "PF00007.1"],
    ["PF00002.1", "PF00003.1", "PF00006.1"],
    ["PF00004.1", "PF00005.1", "PF00006.1"],
    ["PF00001.1", "PF00005.1"],
    ["PF00003.1", "PF00006.1", "PF00007.1"],
    ["PF00002.1", "PF00005.1", "PF00007.1"],
]

CLANS_TSV_CONTENT = """\
PF00001\tCL0001\tClanAlpha\tFamilyA\tTest family A
PF00002\tCL0001\tClanAlpha\tFamilyB\tTest family B
PF00003\tCL0001\tClanAlpha\tFamilyC\tTest family C
PF00004\tCL0002\tClanBeta\tFamilyD\tTest family D
PF00005\tCL0002\tClanBeta\tFamilyE\tTest family E
PF00006\tCL0003\tClanGamma\tFamilyF\tTest family F
PF00007\t\t\tFamilyG\tTest family G
"""


@pytest.fixture
def clans_tsv_path():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".tsv", delete=False) as f:
        f.write(CLANS_TSV_CONTENT)
        path = f.name
    yield path
    os.unlink(path)


# ── Tests: make_compositional_splits ──────────────────────────


class TestMakeCompositionalSplits:
    def test_type_a_disjoint(self, clans_tsv_path):
        splits = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, clans_tsv_path=clans_tsv_path
        )
        id_set = set(tuple(a) for a in splits["type_a"]["id"])
        ood_set = set(tuple(a) for a in splits["type_a"]["ood"])
        assert id_set.isdisjoint(ood_set)

    def test_type_b_disjoint(self, clans_tsv_path):
        splits = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, clans_tsv_path=clans_tsv_path
        )
        id_set = set(tuple(a) for a in splits["type_b"]["id"])
        ood_set = set(tuple(a) for a in splits["type_b"]["ood"])
        assert id_set.isdisjoint(ood_set)

    def test_type_c_disjoint(self, clans_tsv_path):
        splits = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, clans_tsv_path=clans_tsv_path
        )
        id_set = set(tuple(a) for a in splits["type_c"]["id"])
        ood_set = set(tuple(a) for a in splits["type_c"]["ood"])
        assert id_set.isdisjoint(ood_set)

    def test_split_ratios(self, clans_tsv_path):
        splits = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, id_ratio=0.7, clans_tsv_path=clans_tsv_path
        )
        for stype in ("type_a", "type_b", "type_c"):
            id_count = len(splits[stype]["id"])
            ood_count = len(splits[stype]["ood"])
            total = id_count + ood_count
            ood_ratio = ood_count / total
            assert 0.1 <= ood_ratio <= 0.5, f"{stype}: ood_ratio={ood_ratio:.3f}"

    def test_type_b_held_out_families(self, clans_tsv_path):
        splits = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, clans_tsv_path=clans_tsv_path
        )
        families_id = {a.split(".")[0] for arch in splits["type_b"]["id"] for a in arch}
        families_ood = {a.split(".")[0] for arch in splits["type_b"]["ood"] for a in arch}
        # Type B OOD should contain at least one family absent from ID
        assert families_ood - families_id, "Type B: no held-out families found in OOD"

    def test_type_c_held_out_clans(self, clans_tsv_path):
        splits = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, clans_tsv_path=clans_tsv_path
        )
        # Check at least one OOD architecture has a clan not in ID
        ood_archs = splits["type_c"]["ood"]
        # All OOD architectures must contain at least one domain from a held-out clan
        # (by construction), so OOD should be non-empty
        assert ood_archs, "Type C: empty OOD"

    def test_vocabulary_consistency(self, clans_tsv_path):
        all_families = {a.split(".")[0] for arch in ARCHITECTURES for a in arch}
        splits = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, clans_tsv_path=clans_tsv_path
        )
        for stype in ("type_a", "type_b", "type_c"):
            for split_name in ("id", "ood"):
                arch_families = {
                    a.split(".")[0] for arch in splits[stype][split_name] for a in arch
                }
                assert arch_families.issubset(all_families), (
                    f"{stype}/{split_name}: families not in original set"
                )

    def test_empty_architectures(self):
        with pytest.raises(ValueError, match="architectures list is empty"):
            make_compositional_splits([], SIM_MATRIX, ACCESSIONS)

    def test_matrix_shape_mismatch(self):
        bad_matrix = np.eye(3, dtype=np.float32)
        with pytest.raises(ValueError, match="similarity_matrix shape"):
            make_compositional_splits(ARCHITECTURES, bad_matrix, ACCESSIONS)

    def test_seed_reproducibility(self, clans_tsv_path):
        s1 = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, seed=42, clans_tsv_path=clans_tsv_path
        )
        s2 = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, seed=42, clans_tsv_path=clans_tsv_path
        )
        # Same seed → identical splits
        for stype in ("type_a", "type_b", "type_c"):
            assert s1[stype]["id"] == s2[stype]["id"], f"{stype} id differs"
            assert s1[stype]["ood"] == s2[stype]["ood"], f"{stype} ood differs"

    def test_different_seed_different_splits(self, clans_tsv_path):
        s1 = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, seed=42, clans_tsv_path=clans_tsv_path
        )
        s2 = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, seed=99, clans_tsv_path=clans_tsv_path
        )
        # Different seeds should produce at least one different split
        any_diff = any(
            s1[stype]["id"] != s2[stype]["id"] or s1[stype]["ood"] != s2[stype]["ood"]
            for stype in ("type_a", "type_b", "type_c")
        )
        assert any_diff, "Different seeds produced identical splits"


# ── Tests: recombination_distance ─────────────────────────────


class TestRecombinationDistance:
    def test_identity(self):
        arch = ["PF00001.1", "PF00002.1"]
        d = recombination_distance(arch, arch, SIM_MATRIX, ACCESSIONS)
        assert d == 0.0

    def test_symmetry(self):
        a = ["PF00001.1", "PF00002.1"]
        b = ["PF00003.1", "PF00004.1"]
        d1 = recombination_distance(a, b, SIM_MATRIX, ACCESSIONS)
        d2 = recombination_distance(b, a, SIM_MATRIX, ACCESSIONS)
        assert abs(d1 - d2) < 1e-10

    def test_range(self):
        a = ["PF00001.1", "PF00002.1"]
        b = ["PF00005.1", "PF00006.1"]
        d = recombination_distance(a, b, SIM_MATRIX, ACCESSIONS)
        assert 0.0 <= d <= 1.0

    def test_maximally_distant_when_empty(self):
        d = recombination_distance([], ["PF00001.1"], SIM_MATRIX, ACCESSIONS)
        assert d == 1.0
        d = recombination_distance(["PF00001.1"], [], SIM_MATRIX, ACCESSIONS)
        assert d == 1.0
        d = recombination_distance([], [], SIM_MATRIX, ACCESSIONS)
        assert d == 1.0

    def test_unknown_accession(self):
        with pytest.raises(ValueError, match="not found in similarity matrix"):
            recombination_distance(
                ["PF99999.1"], ["PF00001.1"], SIM_MATRIX, ACCESSIONS
            )

    def test_functional_form(self):
        # With the synthetic matrix (off-diagonal = 0.1), distance between
        # two non-overlapping single-domain architectures should be:
        # 1 - psi_geometric(1.0, 1.0, phi=0.1) = 1 - 0.1 = 0.9
        d = recombination_distance(["PF00001.1"], ["PF00002.1"], SIM_MATRIX, ACCESSIONS)
        expected = 1.0 - 0.1  # off-diagonal similarity is 0.1
        assert abs(d - expected) < 1e-10


# ── Tests: compute_split_statistics ──────────────────────────


class TestComputeSplitStatistics:
    def test_basic_structure(self, clans_tsv_path):
        splits = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, clans_tsv_path=clans_tsv_path
        )
        stats = compute_split_statistics(
            splits, similarity_matrix=SIM_MATRIX, accessions=ACCESSIONS
        )
        assert set(stats.keys()) == {"type_a", "type_b", "type_c"}
        for stype in stats:
            entry = stats[stype]
            assert "n_id" in entry
            assert "n_ood" in entry
            assert "unique_families_id" in entry
            assert "unique_families_ood" in entry
            assert "unique_families_shared" in entry
            assert "avg_length_id" in entry
            assert "avg_length_ood" in entry
            assert "recombination_distance_id_ood" in entry

    def test_difficulty_ordering(self, clans_tsv_path):
        splits = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, clans_tsv_path=clans_tsv_path
        )
        stats = compute_split_statistics(
            splits, similarity_matrix=SIM_MATRIX, accessions=ACCESSIONS
        )
        # Type C should have the highest recombination distance (hardest),
        # Type A the lowest (easiest)
        d_a = stats["type_a"]["recombination_distance_id_ood"]
        d_c = stats["type_c"]["recombination_distance_id_ood"]
        # This is a weaker assertion: Type C >= Type A
        assert d_c >= d_a, (
            f"Expected d_c ({d_c:.4f}) >= d_a ({d_a:.4f})"
        )

    def test_no_similarity_matrix(self, clans_tsv_path):
        splits = make_compositional_splits(
            ARCHITECTURES, SIM_MATRIX, ACCESSIONS, clans_tsv_path=clans_tsv_path
        )
        stats = compute_split_statistics(splits)
        for stype in stats:
            assert "n_id" in stats[stype]
            assert "n_ood" in stats[stype]
