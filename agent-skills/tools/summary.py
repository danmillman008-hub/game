#!/usr/bin/env python3
"""خلاصهٔ Markdown از کتابخانهٔ مهارت‌ها — برای GitHub Step Summary."""
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REGISTRY = ROOT / "registry.json"


def human(path: Path) -> str:
    try:
        out = subprocess.run(["du", "-sh", str(path)], capture_output=True, text=True, timeout=30)
        return out.stdout.split("\t")[0].strip() or "?"
    except Exception:  # noqa: BLE001
        return "?"


def main() -> None:
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    lines = [
        "### کتابخانهٔ مهارت‌های ایجنت",
        "",
        "| منبع | نقش | لایسنس | مهارت |",
        "|---|---|---|---|",
    ]
    total = 0
    for src in reg["sources"]:
        base = ROOT / "vendor" / src["id"]
        n = sum(1 for _ in base.rglob("SKILL.md")) if base.is_dir() else 0
        total += n
        lines.append(f"| `{src['repo']}` | {src['role']} | {src['license']} | {n} |")
    lines += [f"| **جمع** | | | **{total}** |", "", f"حجم کل: **{human(ROOT)}** (بیرون از APK)"]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
