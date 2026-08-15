def build_vocab(pairs: list[tuple[str, str]]) -> dict[str, int]:
    vocab = {"<PAD>": 0, "<SOS>": 1, "<EOS>": 2}
    for cmd, action in pairs:
        for tok in cmd.split() + action.split():
            if tok not in vocab:
                vocab[tok] = len(vocab)
    return vocab
