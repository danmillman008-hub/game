#!/usr/bin/env python3
"""Prepare the LearnHarness checkout for hosting under /max.

Single change: `basePath: "/max"` in next.config.ts. Next.js then serves every asset, route and API under the prefix,
so the Mimo shell can host the real application inside one origin. No application logic is touched.

Idempotent: safe to run repeatedly.
"""
from __future__ import annotations

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent
LH = ROOT / "src" / "learnharness"


def main() -> int:
    cfg = LH / "next.config.ts"
    if not cfg.is_file():
        print(f"LearnHarness checkout not found at {LH}; run tools/bootstrap_engines.sh first.", file=sys.stderr)
        return 2
    text = cfg.read_text(encoding="utf-8")
    if 'basePath: "/max"' in text:
        print("basePath already set")
        return 0
    match = re.search(r"const nextConfig: NextConfig = \{\n", text)
    if not match:
        print("could not find the nextConfig object; LearnHarness changed shape upstream", file=sys.stderr)
        return 3
    insert = ('\t// [mimo-preview] served by the Mimo shell under /max (single hosting change, no app logic)\n'
              '\tbasePath: "/max",\n')
    text = text[:match.end()] + insert + text[match.end():]
    cfg.write_text(text, encoding="utf-8")
    print("added basePath=/max to next.config.ts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
