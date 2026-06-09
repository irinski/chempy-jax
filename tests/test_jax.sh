#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

if [ -e "$REPO_ROOT/local_env.sh" ]
then
    source "$REPO_ROOT/local_env.sh"
fi

source "$JAX_PYENV"
export CHEMPY_PATH="$REPO_ROOT/src"
pytest "$@"
