#!/usr/bin/env python3

from __future__ import annotations

import pathlib
import sys

import yaml


ROOT = pathlib.Path(__file__).resolve().parents[1]


def main() -> int:
    failures: list[str] = []
    documents = 0
    for path in sorted(ROOT.rglob("*.yml")):
        if any(part in {".git", "dist", "context"} for part in path.parts):
            continue
        try:
            with path.open(encoding="utf-8") as stream:
                documents += sum(1 for document in yaml.safe_load_all(stream) if document is not None)
        except Exception as exc:
            failures.append(f"{path.relative_to(ROOT)}: {exc}")

    if failures:
        print("YAML validation failed:", file=sys.stderr)
        print("\n".join(f"- {failure}" for failure in failures), file=sys.stderr)
        return 1

    print(f"Validated {documents} YAML documents.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
