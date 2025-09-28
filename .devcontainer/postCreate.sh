#!/usr/bin/env bash
set -euxo pipefail

# Ensure we can find locally installed user binaries (Codespaces does not add
# ~/.local/bin to PATH by default during provisioning)
export PATH="${HOME}/.local/bin:${PATH}"

# Ensure uv is installed for the current user
if ! command -v uv >/dev/null 2>&1; then
  mkdir -p "${HOME}/.local/bin"
  curl -LsSf https://astral.sh/uv/install.sh | sh -s -- --yes
fi

# Sync the project dependencies into the managed virtual environment (creates
# .venv/ when missing)
uv sync --frozen

# Register the project virtual environment as a Jupyter kernel for notebooks
uv run python -m ipykernel install --user --name llm-course --display-name "Python (.venv)"
