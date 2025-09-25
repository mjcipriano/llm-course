import pytest

torch = pytest.importorskip("torch")

from llm_course.lesson4 import SelfAttention, TinyTransformer, decode, encode


def _set_identity_weights(attn: SelfAttention) -> None:
    with torch.no_grad():
        attn.qkv.weight.zero_()
        hidden = attn.qkv.weight.shape[1]
        attn.qkv.weight[:hidden, :] = torch.eye(hidden)
        attn.qkv.weight[hidden : 2 * hidden, :] = torch.eye(hidden)
        attn.qkv.weight[2 * hidden :, :] = torch.eye(hidden)
        attn.proj.weight.copy_(torch.eye(hidden))


def test_self_attention_is_causal():
    attn = SelfAttention(n_embd=2, n_head=1)
    _set_identity_weights(attn)
    x = torch.tensor([[[1.0, 0.0], [0.0, 5.0]]])
    out = attn(x)
    first_token = out[0, 0]
    assert torch.allclose(first_token, torch.tensor([1.0, 0.0]), atol=1e-5)


def test_tiny_transformer_forward_and_generate():
    vocab_size = 5
    model = TinyTransformer(vocab_size=vocab_size, n_embd=8, n_head=2, n_layer=1, block_size=4)
    x = torch.zeros((2, 4), dtype=torch.long)
    logits, loss = model(x, x)
    assert logits.shape == (2, 4, vocab_size)
    assert loss is not None
    context = torch.zeros((1, 1), dtype=torch.long)
    generated = model.generate(context, max_new_tokens=3)
    assert generated.shape == (1, 4)


def test_encode_decode_roundtrip():
    stoi = {"a": 0, "b": 1}
    itos = {0: "a", 1: "b"}
    ids = encode("abba", stoi)
    assert ids.tolist() == [0, 1, 1, 0]
    assert decode(ids, itos) == "abba"
