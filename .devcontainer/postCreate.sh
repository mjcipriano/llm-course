#!/usr/bin/env bash
set -euxo pipefail

# Ensure uv is available system-wide
if ! command -v uv >/dev/null 2>&1; then
  INSTALL_CMD="sh -s -- --yes --install-dir /usr/local/bin"
  if command -v sudo >/dev/null 2>&1; then
    curl -LsSf https://astral.sh/uv/install.sh | sudo ${INSTALL_CMD}
  else
    curl -LsSf https://astral.sh/uv/install.sh | ${INSTALL_CMD}
  fi
fi

# Sync the project dependencies into the managed virtual environment
uv sync --frozen

# Register the project virtual environment as a Jupyter kernel for notebooks
uv run python -m ipykernel install --user --name llm-course --display-name "Python (.venv)"
