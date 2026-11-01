#!/usr/bin/env python3
"""Prepare the EPM checkout for hosting under /practice — the smallest set of changes that makes prefix hosting work.

1. package-lock.json: some upstream lock entries resolve through a regional mirror that is unreachable here; rewriting
   the host to registry.npmjs.org keeps every pinned version and lets `npm install` complete. (No dependency bumps.)
2. Nothing else is changed. The Vue app keeps its own router (hash history) and its own API client; the only build
   flags are `--base=/practice/` and `VITE_API_ROOT=/practice/api`, passed on the command line by the bootstrap script.

Idempotent: safe to run repeatedly.
"""
from __future__ import annotations

import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent
EPM = ROOT / "src" / "epm"


def main() -> int:
    if not EPM.is_dir():
        print(f"EPM checkout not found at {EPM}; run tools/bootstrap_engines.sh first.", file=sys.stderr)
        return 2
    lock = EPM / "frontend" / "package-lock.json"
    if lock.is_file():
        text = lock.read_text(encoding="utf-8")
        if "registry.npmmirror.com" in text:
            backup = lock.with_suffix(".json.orig")
            if not backup.exists():
                backup.write_text(text, encoding="utf-8")
            lock.write_text(text.replace("registry.npmmirror.com", "registry.npmjs.org"), encoding="utf-8")
            print("patched package-lock.json registry host (versions unchanged)")
        else:
            print("package-lock.json already uses registry.npmjs.org")
    marker = EPM / ".mimo-prepared"
    marker.write_text(json.dumps({"prepared": True, "changes": ["lockfile registry host"]}, indent=1) + "\n",
                      encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
