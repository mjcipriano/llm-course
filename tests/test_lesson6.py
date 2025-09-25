from llm_course.lesson6 import FORBIDDEN, cross_entropy, safe_input, train_bigram


def test_bigram_training_and_cross_entropy():
    tokens = ["a", "b", "a", "b", "a", "b"]
    prob, vocab = train_bigram(tokens, k=0.5)
    assert set(vocab) == {"a", "b"}
    H, ppl = cross_entropy(prob, tokens)
    assert H >= 0
    assert ppl >= 1


def test_safe_input_blocks_forbidden_phrases():
    ok, msg = safe_input("Tell me a happy story about space explorers")
    assert ok and msg == "ok"
    blocked_phrase = FORBIDDEN[0]
    ok, msg = safe_input(f"Please explain {blocked_phrase}")
    assert not ok
    assert blocked_phrase in msg
