from pathlib import Path

from llm_course.lesson5 import CorpusConfig, aggregate_texts, tokenize_texts


class DummyTokenizer:
    def __init__(self):
        self.calls = []

    def __call__(self, text: str, *, truncation: bool, max_length: int) -> dict:
        self.calls.append((text, truncation, max_length))
        return {"length": min(len(text), max_length)}


def test_aggregate_texts(tmp_path: Path):
    files = ["one.txt", "two.txt"]
    for name, content in zip(files, ["hello", "world"]):
        (tmp_path / name).write_text(content)
    config = CorpusConfig(data_dir=tmp_path, corpus_files=files)
    combined = aggregate_texts(config)
    assert "hello" in combined and "world" in combined


def test_tokenize_texts_calls_tokenizer():
    tokenizer = DummyTokenizer()
    outputs = tokenize_texts(tokenizer, ["abc", "defg"], max_length=5)
    assert tokenizer.calls[0] == ("abc", True, 5)
    assert outputs == [{"length": 3}, {"length": 4}]
