import numpy as np
import pytest

from llm_course.lesson2 import (
    Vocabulary,
    build_cooccurrence,
    build_vocabulary,
    compute_embeddings,
    cosine,
    neighbors,
    prepare_tokens,
)


def test_prepare_tokens_and_vocab():
    tokens = prepare_tokens("Dogs chase cats!")
    assert tokens == ["dogs", "chase", "cats"]
    vocab = build_vocabulary(tokens)
    assert isinstance(vocab, Vocabulary)
    assert vocab.word_to_index["cats"] >= 0


def test_cooccurrence_window_counts():
    tokens = ["dog", "likes", "cat", "likes", "dog"]
    vocab = build_vocabulary(tokens)
    matrix = build_cooccurrence(tokens, vocab, window=1)
    dog_index = vocab.word_to_index["dog"]
    likes_index = vocab.word_to_index["likes"]
    assert matrix[dog_index, likes_index] == pytest.approx(2.0)
    assert matrix[likes_index, dog_index] == pytest.approx(2.0)


def test_embeddings_and_neighbors():
    tokens = ["dog", "runs", "fast", "dog", "chases", "cat"]
    vocab = build_vocabulary(tokens)
    cooc = build_cooccurrence(tokens, vocab, window=2)
    emb = compute_embeddings(cooc, dims=3)
    assert emb.shape[1] == 3
    # construct manual embeddings for deterministic neighbours
    manual = np.array(
        [
            [0.0, 0.8, 0.2],  # cat
            [0.1, 0.1, 0.9],  # chases
            [0.0, 1.0, 0.0],  # dog
            [0.0, 0.9, 0.1],  # fast
            [1.0, 0.0, 0.0],  # runs
        ]
    )
    vocab_manual = Vocabulary(
        words=["cat", "chases", "dog", "fast", "runs"],
        word_to_index={w: i for i, w in enumerate(["cat", "chases", "dog", "fast", "runs"])},
        index_to_word={i: w for i, w in enumerate(["cat", "chases", "dog", "fast", "runs"])},
    )
    neigh = neighbors("dog", manual, vocab_manual, k=2)
    assert neigh[0][1] == "fast"
    assert neigh[1][1] == "cat"
    assert neighbors("unknown", manual, vocab_manual) == []


def test_cosine_similarity_properties():
    a = np.array([1.0, 0.0])
    b = np.array([1.0, 0.0])
    c = np.array([0.0, 1.0])
    assert cosine(a, b) == pytest.approx(1.0)
    assert cosine(a, c) == pytest.approx(0.0, abs=1e-6)
