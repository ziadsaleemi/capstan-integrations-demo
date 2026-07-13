#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

python3 scripts/validate.py
rm -rf dist
mkdir -p dist
ansible-galaxy collection build --force --output-path dist

if command -v opa >/dev/null 2>&1; then
  opa check --strict opa
else
  echo "opa not installed; Rego compilation skipped."
fi

if command -v gator >/dev/null 2>&1; then
  (
    cd gatekeeper/tests
    gator verify suite.yml
  )
else
  echo "gator not installed; Gatekeeper suite validation skipped."
fi

echo "Capstan integration demo validation passed."
