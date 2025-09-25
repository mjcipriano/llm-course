import math

import pytest

from llm_course.lesson3 import cross_entropy, ngrams, sample, train_ngram


def test_ngrams_generation():
    tokens = ["a", "b", "c", "d"]
    assert list(ngrams(tokens, 2)) == [("a", "b"), ("b", "c"), ("c", "d")]
    with pytest.raises(ValueError):
        list(ngrams(tokens, 0))


def test_train_ngram_probability():
    tokens = ["hello", "world", "hello", "planet"]
    prob, vocab = train_ngram(tokens, n=2, k=1.0)
    assert set(vocab) == {"hello", "world", "planet"}
    p = prob(("hello",), "world")
    assert 0.0 < p < 1.0


def test_sample_returns_tokens():
    tokens = ["hi", "there", "hi", "friend"]
    prob, vocab = train_ngram(tokens, n=2, k=1.0)
    out = sample(prob, vocab, n=2, max_len=5, seed=0)
    assert len(out) == 5
    assert set(out).issubset(set(vocab))


def test_cross_entropy_reasonable():
    tokens = ["a", "b", "a", "b", "a", "b", "a", "b"]
    prob, _ = train_ngram(tokens, n=2, k=0.5)
    H = cross_entropy(prob, tokens, n=2, split=0.5)
    assert H >= 0
    with pytest.raises(ValueError):
        cross_entropy(prob, tokens, n=2, split=1.5)
