#!/usr/bin/env python3
"""ساخت INDEX.md از روی فایل‌های SKILL.md موجود در vendor/ + registry.json.

اجرا:  python3 agent-skills/tools/build_index.py
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # agent-skills/
VENDOR = ROOT / "vendor"
REGISTRY = ROOT / "registry.json"
OUT = ROOT / "INDEX.md"

FRONT = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)


def parse_front_matter(path: Path) -> tuple[str, str]:
    """(name, description) را از front matter سادهٔ YAML بیرون می‌کشد."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return path.parent.name, ""
    m = FRONT.match(text)
    if not m:
        return path.parent.name, ""
    block = m.group(1)
    name = path.parent.name
    nm = re.search(r"^name:\s*[\"']?([^\"'\n]+)", block, re.M)
    if nm:
        name = nm.group(1).strip()
    desc = ""
    dm = re.search(r"^description:\s*(>-?|>|\|-?|\|)?\s*(.*(?:\n(?:\s{2,}\S.*|$))*)", block, re.M)
    if dm:
        raw = (dm.group(2) or "").replace("\n", " ")
        desc = re.sub(r"\s+", " ", raw).strip().strip('"').strip("'")
    return name, desc


def one_line(text: str, limit: int = 170) -> str:
    text = text.replace("|", "/")
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def main() -> None:
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    rows: dict[str, list[tuple[str, str, str]]] = {}
    for src in reg["sources"]:
        base = VENDOR / src["id"]
        entries: list[tuple[str, str, str]] = []
        if base.exists():
            for skill in sorted(base.rglob("SKILL.md")):
                name, desc = parse_front_matter(skill)
                rel = skill.parent.relative_to(ROOT).as_posix()
                entries.append((name, one_line(desc), rel))
        rows[src["id"]] = entries

    lines = [
        "# فهرست مهارت‌ها",
        "",
        "> این فایل **خودکار** ساخته می‌شود: `python3 agent-skills/tools/build_index.py`",
        "> دستی ویرایش نکنید.",
        "",
        "قبل از هر کار، `agent-skills/PROJECT-RULES.md` را بخوانید. سپس فقط مهارت مرتبط",
        "با کار جاری را باز کنید — نه همه را.",
        "",
        "## نقشهٔ سریع فازها",
        "",
        "| کار جاری | اول از کجا بخوانم |",
        "|---|---|",
        "| build، AGP، R8، اندازهٔ APK | `vendor/android-official-skills/` (جست‌وجوی نام مهارت) + `android/skills` R8 |",
        "| ViewModel، UiState، Flow، side-effect | `vendor/chrisbanes-skills/skills/compose-state-and-effects/` و `kotlin-concurrency-and-flow/` |",
        "| نوشتن/اصلاح صفحهٔ Compose | `vendor/compose-kotlin-agent-skills/SKILL.md` + `references/02-compose-ui.md` + `00-banned-antipatterns.md` |",
        "| Room، DAO، migration | `vendor/android-agent-skills/skills/android-room-database/` |",
        "| اسکنر CameraX + ML Kit | `vendor/android-official-skills/camera/camerax/` + `vendor/compose-kotlin-agent-skills/references/12-camera-mlkit.md` |",
        "| اعلان محلی و WorkManager (فاز H) | `vendor/android-agent-skills/skills/android-workmanager-notifications/` |",
        "| تست UI / instrumentation / ADB | `vendor/android-testing-skills/` |",
        "| بازبینی معماری با شدت‌بندی | `vendor/android-review/skills/` (هفت حوزه) |",
        "| بازبینی UX و جریان کاربر | `vendor/mobile-app-ux-auditor-skill/skills/mobile-app-ux-auditor/` |",
        "",
        "---",
        "",
    ]

    for src in reg["sources"]:
        entries = rows[src["id"]]
        title = src["title"]
        lines += [
            f"## {title} — `{src['repo']}`",
            "",
            f"- نقش: **{src['role']}** · لایسنس: {src['license']} · "
            f"commit: `{src['commit'][:10]}`",
            f"- کِی: {src['useWhen']}",
            f"- تعداد مهارت یافت‌شده: **{len(entries)}**",
            "",
        ]
        if not entries:
            lines += ["_(بدون SKILL.md؛ ساختار rule/مرجع دارد — فایل README خودش را ببینید.)_", ""]
        else:
            lines += ["| مهارت | چه کاری می‌کند | مسیر |", "|---|---|---|"]
            for name, desc, rel in entries:
                lines.append(f"| `{name}` | {desc} | `{rel}` |")
            lines.append("")

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    total = sum(len(v) for v in rows.values())
    print(f"INDEX.md نوشته شد — {total} مهارت از {len(rows)} منبع.")


if __name__ == "__main__":
    main()
