#!/usr/bin/env bash
set -euxo pipefail

echo "[postCreate] Starting environment setup for llm-course"

# Ensure we can find locally installed user binaries (Codespaces does not add
# ~/.local/bin to PATH by default during provisioning)
export PATH="${HOME}/.local/bin:${PATH}"
echo "[postCreate] PATH updated to include ${HOME}/.local/bin"

# Ensure uv is installed for the current user
if ! command -v uv >/dev/null 2>&1; then
  echo "[postCreate] uv not found; installing via official installer"
  mkdir -p "${HOME}/.local/bin"
  curl -LsSf https://astral.sh/uv/install.sh | sh -s -- --yes
else
  echo "[postCreate] uv already installed at $(command -v uv)"
fi

echo "[postCreate] Resolving Python environment with uv sync"
# Sync the project dependencies into the managed virtual environment (creates
# .venv/ when missing)
uv sync --frozen

echo "[postCreate] Registering the managed virtualenv as a Jupyter kernel"
# Register the project virtual environment as a Jupyter kernel for notebooks
uv run python -m ipykernel install --user --name llm-course --display-name "Python (.venv)"

echo "[postCreate] Completed environment setup"
