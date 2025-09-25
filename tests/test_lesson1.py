import collections
from pathlib import Path

from llm_course.lesson1 import (
    aggregate_corpus,
    get_stats,
    get_vocab,
    learn_bpe,
    merge_vocab,
    tokenize,
)


def test_aggregate_corpus(tmp_path: Path):
    file1 = tmp_path / "a.txt"
    file2 = tmp_path / "b.txt"
    file1.write_text("hello")
    file2.write_text("world")
    text = aggregate_corpus(tmp_path, ["a.txt", "b.txt"])
    assert "hello" in text and "world" in text


def test_get_stats_counts_pairs():
    vocab = collections.Counter({"l o w </w>": 2, "l o w e r </w>": 1})
    stats = get_stats(vocab)
    assert stats[("l", "o")] == 3
    assert stats[("o", "w")] == 3


def test_merge_and_tokenize_roundtrip():
    text = "low lower lowest"
    merges = learn_bpe(text, 10)
    assert merges[0] == ("l", "o")
    vocab = get_vocab(text)
    merged_vocab = merge_vocab(merges[0], vocab)
    assert any(token.startswith("lo") for token in merged_vocab)
    assert tokenize("lower", merges) == ["lower</w>"]
    assert tokenize("lowest", merges) == ["lowest</w>"]
