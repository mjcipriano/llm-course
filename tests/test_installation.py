import importlib
import subprocess
import sys


def test_project_is_installable(tmp_path):
    target = tmp_path / "site"
    target.mkdir()
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", ".", "--target", str(target), "--no-deps"],
    )
    sys.path.insert(0, str(target))
    module = importlib.import_module("llm_course")
    assert hasattr(module, "lesson1_get_vocab")
