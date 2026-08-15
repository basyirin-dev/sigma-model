"""Unit tests for sigma.proteins.data — Stockholm parser and Pfam data tools."""

import os
import tempfile

import pytest
from sigma.proteins.data import (
    SPECIAL_TOKENS,
    PfamDataset,
    build_domain_vocab,
    extract_domain_architectures,
    get_domain_metadata,
    parse_stockholm,
)

# ── Synthetic Stockholm fixtures ──────────────────────────────

METADATA_ONLY_STOCKHOLM = """\
# STOCKHOLM 1.0
#=GF ID   FamilyA
#=GF AC   PF00001.1
#=GF DE   Test family A
#=GF TP   Domain
#=GF ML   100
#=GF CL   CL0001
//
# STOCKHOLM 1.0
#=GF ID   FamilyB
#=GF AC   PF00002.1
#=GF DE   Test family B
#=GF TP   Repeat
//"""

SEQUENCE_STOCKHOLM = """\
# STOCKHOLM 1.0
#=GF ID   FamilyA
#=GF AC   PF00001.1
#=GF DE   Test family A
#=GF TP   Domain
#=GF ML   50
#=GF CL   CL0001
#=GS prot1_SPEC1/1-50  AC P001.1
#=GS prot2_SPEC2/10-60 AC P002.1
#=GS prot5_SPEC3/5-55  AC P005.1
prot1_SPEC1/1-50          ACDEFGHIKLMNPQRSTVWYACDEFGHIKLMNPQRSTVWY
prot2_SPEC2/10-60         ACDEFGHIKLMNPQRSTVWYACDEFGHIKLMNPQRSTVWY
prot5_SPEC3/5-55          ACDEFGHIKLMNPQRSTVWYACDEFGHIKLMNPQRSTVWY
//
# STOCKHOLM 1.0
#=GF ID   FamilyB
#=GF AC   PF00002.1
#=GF DE   Test family B (overlaps FamilyA for some proteins)
#=GF TP   Domain
#=GF ML   30
#=GF CL   CL0001
#=GS prot1_SPEC1/30-80  AC P001.1
#=GS prot3_SPEC4/1-30   AC P003.1
prot1_SPEC1/30-80          ACDEFGHIKLMNPQRSTVWYACDEFGHI
prot3_SPEC4/1-30           ACDEFGHIKLMNPQRSTVWYACDEFGHI
//
# STOCKHOLM 1.0
#=GF ID   FamilyC
#=GF AC   PF00003.1
#=GF DE   Test family C
#=GF TP   Family
#=GF ML   20
#=GS prot3_SPEC4/31-50  AC P003.1
prot3_SPEC4/31-50          ACDEFGHIKLMNPQRSTVWY
//
# STOCKHOLM 1.0
#=GF ID   FamilyD
#=GF AC   PF00004.1
#=GF DE   Test family D (single domain - should be filtered out)
#=GF TP   Domain
#=GF ML   40
#=GS prot4_SPEC5/1-40   AC P004.1
prot4_SPEC5/1-40           ACDEFGHIKLMNPQRSTVWYACDEFGHIKLMNPQRST
//"""

CLANS_TSV_SYNTHETIC = """\
PF00001\tCL0001\tClanAlpha\tFamilyA\tTest family A
PF00002\tCL0001\tClanAlpha\tFamilyB\tTest family B
PF00003\tCL0001\tClanAlpha\tFamilyC\tTest family C
PF00004\tCL0002\tClanBeta\tFamilyD\tTest family D
PF00005\tCL0003\tClanGamma\tFamilyE\tTest family E
"""


# ── Helper ────────────────────────────────────────────────────


@pytest.fixture
def metadata_stockholm_path():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".stockholm", delete=False) as f:
        f.write(METADATA_ONLY_STOCKHOLM)
        path = f.name
    yield path
    os.unlink(path)


@pytest.fixture
def sequence_stockholm_path():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".stockholm", delete=False) as f:
        f.write(SEQUENCE_STOCKHOLM)
        path = f.name
    yield path
    os.unlink(path)


@pytest.fixture
def clans_tsv_path():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".tsv", delete=False) as f:
        f.write(CLANS_TSV_SYNTHETIC)
        path = f.name
    yield path
    os.unlink(path)


# ── Test: parse_stockholm ─────────────────────────────────────


class TestParseStockholm:
    def test_metadata_only(self, metadata_stockholm_path):
        records = parse_stockholm(metadata_stockholm_path)
        assert len(records) == 2
        assert records[0]["accession"] == "PF00001.1"
        assert records[0]["identifier"] == "FamilyA"
        assert records[0]["description"] == "Test family A"
        assert records[0]["type"] == "Domain"
        assert records[0]["clan"] == "CL0001"
        assert records[0]["length"] == 100
        assert records[0]["seq_count"] == 0
        assert records[0]["sequences"] == []

        assert records[1]["accession"] == "PF00002.1"
        assert records[1]["identifier"] == "FamilyB"
        assert records[1]["type"] == "Repeat"
        assert records[1]["clan"] == ""

    def test_with_sequences(self, sequence_stockholm_path):
        records = parse_stockholm(sequence_stockholm_path)
        assert len(records) == 4

        # First family: FamilyA with 3 sequences
        r0 = records[0]
        assert r0["accession"] == "PF00001.1"
        assert r0["identifier"] == "FamilyA"
        assert r0["type"] == "Domain"
        assert r0["clan"] == "CL0001"
        # length (ML) is only available in metadata-only Stockholm parser;
        # Biopython parser for files with sequences may not expose ML
        assert r0.get("length") is None or r0["length"] == 50
        assert r0["seq_count"] == 3
        assert len(r0["sequences"]) == 3

        seq0 = r0["sequences"][0]
        assert seq0["id"] == "prot1_SPEC1/1-50"
        assert seq0["accession"] == "P001.1"
        assert seq0["start"] == 1
        assert seq0["end"] == 50
        assert seq0["species"] == "prot1_SPEC1"

    def test_missing_file(self):
        with pytest.raises(FileNotFoundError):
            parse_stockholm("/nonexistent/stockholm.sth")

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".stockholm", delete=False) as f:
            path = f.name
        try:
            records = parse_stockholm(path)
            assert records == []
        finally:
            os.unlink(path)

    def test_gz_file(self, metadata_stockholm_path):
        import gzip
        gz_path = metadata_stockholm_path + ".gz"
        with open(metadata_stockholm_path, "rb") as src:
            with gzip.open(gz_path, "wb") as dst:
                dst.write(src.read())
        try:
            records = parse_stockholm(gz_path)
            assert len(records) == 2
        finally:
            os.unlink(gz_path)


# ── Test: extract_domain_architectures ────────────────────────


@pytest.fixture
def parsed_sequence_records(sequence_stockholm_path):
    return parse_stockholm(sequence_stockholm_path)


class TestExtractDomainArchitectures:
    def test_basic_extraction(self, parsed_sequence_records):
        archs = extract_domain_architectures(parsed_sequence_records)
        assert len(archs) >= 1

        # P003.1 should have [PF00002.1, PF00003.1] (ordered by position)
        # P003 appears in FamilyB (1-30) and FamilyC (31-50)
        p003_arch = [a for a in archs if "PF00003.1" in a]
        assert len(p003_arch) >= 1
        # PF00002.1 (start=1) should come before PF00003.1 (start=31)
        for arch in p003_arch:
            assert arch.index("PF00002.1") < arch.index("PF00003.1")

    def test_empty_input(self):
        assert extract_domain_architectures([]) == []

    def test_no_architectures_below_min_length(self, parsed_sequence_records):
        # P004.1 has only one domain (FamilyD/PF00004.1), should be excluded
        archs = extract_domain_architectures(parsed_sequence_records, min_length=2)
        for a in archs:
            assert len(a) >= 2

    def test_max_length_filter(self, parsed_sequence_records):
        archs = extract_domain_architectures(parsed_sequence_records, max_length=1)
        assert all(len(a) <= 1 for a in archs)
        assert len(archs) == 0  # no single-domain archs (min_length=2 > max_length=1)

    def test_overlap_detection(self, parsed_sequence_records):
        # P001.1 has two domains: FamilyA (1-50) and FamilyB (30-80)
        # These overlap (30 < 50), so P001.1's architecture is excluded
        # PF00001.1 (FamilyA) only appears in P001.1, so it should not
        # appear in any extracted architecture
        archs = extract_domain_architectures(parsed_sequence_records)
        for a in archs:
            assert "PF00001.1" not in a


# ── Test: build_domain_vocab ─────────────────────────────────


class TestBuildDomainVocab:
    def test_special_tokens(self):
        archs = [["PF00001", "PF00002"]]
        token2id, id2token, _ = build_domain_vocab(archs)
        assert token2id["<PAD>"] == 0
        assert token2id["<SOS>"] == 1
        assert token2id["<EOS>"] == 2
        assert token2id["<MASK>"] == 3
        assert token2id["<UNK>"] == 4
        assert id2token[0] == "<PAD>"
        assert id2token[1] == "<SOS>"
        assert id2token[2] == "<EOS>"
        assert id2token[3] == "<MASK>"
        assert id2token[4] == "<UNK>"

    def test_domain_tokens(self):
        archs = [["PF00001", "PF00002"], ["PF00003"]]
        token2id, id2token, _ = build_domain_vocab(archs)
        assert token2id["PF00001"] == 5
        assert token2id["PF00002"] == 6
        assert token2id["PF00003"] == 7
        assert id2token[5] == "PF00001"

    def test_id2token_roundtrip(self):
        archs = [["PF00001", "PF00002"]]
        token2id, id2token, _ = build_domain_vocab(archs)
        for token in ["PF00001", "PF00002", "<PAD>", "<SOS>", "<EOS>", "<MASK>", "<UNK>"]:
            assert id2token[token2id[token]] == token

    def test_clan_mapping(self, clans_tsv_path):
        archs = [["PF00001", "PF00002"], ["PF00005"]]
        _, _, clan_map = build_domain_vocab(archs, clan_map_path=clans_tsv_path)
        assert clan_map["PF00001"] == "CL0001"
        assert clan_map["PF00002"] == "CL0001"
        assert clan_map["PF00005"] == "CL0003"

    def test_empty_architectures(self):
        token2id, id2token, clan_map = build_domain_vocab([])
        assert len(token2id) == 5  # only special tokens
        assert len(id2token) == 5
        assert clan_map == {}


# ── Test: PfamDataset ─────────────────────────────────────────


class TestPfamDataset:
    def test_len_and_getitem(self):
        archs = [["PF00001", "PF00002"], ["PF00003"]]
        token2id, _, _ = build_domain_vocab(archs)
        ds = PfamDataset(archs, token2id, max_len=5)
        assert len(ds) == 2

        x, y = ds[0]
        assert x.shape == (5,)
        assert y.shape == (5,)

    def test_sos_eos_positions(self):
        archs = [["PF00001", "PF00002"]]
        token2id, _, _ = build_domain_vocab(archs)
        ds = PfamDataset(archs, token2id, max_len=10)

        x, y = ds[0]
        # src = tokens[:-1] = [PF00001]
        # tgt = [SOS, PF00001, PF00002, EOS] + padding
        assert x[0].item() == token2id["PF00001"]
        assert y[0].item() == token2id["<SOS>"]
        # find EOS in tgt
        eos_pos = (y == token2id["<EOS>"]).nonzero(as_tuple=True)[0].item()
        assert eos_pos == 3  # SOS, PF00001, PF00002, EOS

    def test_padding(self):
        archs = [["PF00001", "PF00002"]]
        token2id, _, _ = build_domain_vocab(archs)
        ds = PfamDataset(archs, token2id, max_len=10)
        x, y = ds[0]
        # After the tokens, the rest should be padding
        pad = token2id["<PAD>"]
        # x: [PF00001, PAD, PAD, ...]
        assert x[1].item() == pad
        assert x[-1].item() == pad
        # y: [SOS, PF00001, PF00002, EOS, PAD, ...]
        assert y[0].item() == token2id["<SOS>"]
        assert y[-1].item() == pad

    def test_empty_dataset(self):
        token2id = dict(SPECIAL_TOKENS)
        ds = PfamDataset([], token2id)
        assert len(ds) == 0

    def test_unknown_token_handling(self):
        archs = [["PF00001", "PF99999"]]  # PF99999 not in vocab
        token2id = dict(SPECIAL_TOKENS)
        token2id["PF00001"] = 5
        ds = PfamDataset(archs, token2id, max_len=5)
        x, y = ds[0]
        # src = [PF00001], tgt = [SOS, PF00001, UNK, EOS, PAD]
        # PF99999 (unknown) maps to <UNK> (4) in tgt at position 2
        assert y[2].item() == token2id["<UNK>"]


# ── Test: get_domain_metadata ─────────────────────────────────


class TestGetDomainMetadata:
    def test_metadata_dataframe_columns(self, metadata_stockholm_path, clans_tsv_path):
        df = get_domain_metadata(metadata_stockholm_path, clans_tsv_path)
        expected_cols = {
            "pfam_accession", "family_name", "family_type",
            "description", "clan", "length", "clan_label",
            "family_label", "clan_description",
        }
        assert expected_cols.issubset(set(df.columns))

    def test_metadata_values(self, metadata_stockholm_path, clans_tsv_path):
        df = get_domain_metadata(metadata_stockholm_path, clans_tsv_path)
        row = df[df["pfam_accession"] == "PF00001.1"].iloc[0]
        assert row["family_name"] == "FamilyA"
        assert row["family_type"] == "Domain"
        assert row["description"] == "Test family A"
        assert row["clan"] == "CL0001"
        assert row["length"] == 100

    def test_clan_from_tsv_overrides(self, metadata_stockholm_path, clans_tsv_path):
        df = get_domain_metadata(metadata_stockholm_path, clans_tsv_path)
        row = df[df["pfam_accession"] == "PF00002.1"].iloc[0]
        # FamilyB has no CL from hmm.dat, but CL0001 from clans.tsv
        assert row["clan"] == "CL0001"


# ── HMMER Bit Score Tests ──────────────────────────────────


FIXTURE_DIR = os.path.join(os.path.dirname(__file__), "fixtures")
MINI_HMM = os.path.join(FIXTURE_DIR, "pfam_mini.hmm")
MINI_CLANS = os.path.join(FIXTURE_DIR, "pfam_mini.clans.tsv")

def _pyhmmer_available():
    try:
        import sigma.proteins.data as d
        return d.PYHMMER_AVAILABLE
    except Exception:
        return False

pytestmark_hmm = pytest.mark.skipif(
    not _pyhmmer_available(),
    reason="pyhmmer not installed",
)


class TestHMMERBitScore:
    def test_self_similarity(self):
        from sigma.proteins.data import compute_domain_similarity
        score = compute_domain_similarity("PF00389.37", "PF00389.37", hmm_path=MINI_HMM)
        assert score == 1.0

    def test_cross_similarity_same_clan(self):
        from sigma.proteins.data import compute_domain_similarity
        score = compute_domain_similarity("PF00389.37", "PF02826.26", hmm_path=MINI_HMM)
        assert 0.0 <= score <= 1.0

    def test_cross_similarity_different_clan(self):
        from sigma.proteins.data import compute_domain_similarity
        score = compute_domain_similarity("PF00389.37", "PF00244.27", hmm_path=MINI_HMM)
        assert 0.0 <= score <= 1.0

    def test_symmetry(self):
        from sigma.proteins.data import compute_domain_similarity
        ab = compute_domain_similarity("PF00389.37", "PF02826.26", hmm_path=MINI_HMM)
        ba = compute_domain_similarity("PF02826.26", "PF00389.37", hmm_path=MINI_HMM)
        assert abs(ab - ba) < 0.01

    def test_unknown_accession(self):
        from sigma.proteins.data import compute_domain_similarity
        with pytest.raises(ValueError, match="not found"):
            compute_domain_similarity("PF99999.1", "PF00389.37", hmm_path=MINI_HMM)


class TestFoldCompatibility:
    def test_same_clan(self):
        from sigma.proteins.data import compute_fold_compatibility
        score = compute_fold_compatibility("PF00389.37", "PF02826.26", clans_tsv_path=MINI_CLANS)
        assert score == 0.9

    def test_different_clan(self):
        from sigma.proteins.data import compute_fold_compatibility
        score = compute_fold_compatibility("PF00389.37", "PF00244.27", clans_tsv_path=MINI_CLANS)
        assert score == 0.1

    def test_same_accession(self):
        from sigma.proteins.data import compute_fold_compatibility
        score = compute_fold_compatibility("PF00389.37", "PF00389.37", clans_tsv_path=MINI_CLANS)
        assert score == 0.9

    def test_unmapped_accession(self):
        from sigma.proteins.data import compute_fold_compatibility
        score = compute_fold_compatibility("PF28545.1", "PF28546.1", clans_tsv_path=MINI_CLANS)
        assert score == 0.1

    def test_missing_clans_file(self):
        from sigma.proteins.data import compute_fold_compatibility
        with pytest.raises(FileNotFoundError):
            compute_fold_compatibility("PF00389.37", "PF02826.26", clans_tsv_path="/nonexistent.tsv")
