#!/usr/bin/env python3
"""اعتبارسنجی نصب مهارت‌ها — در CI هم اجرا می‌شود.

بررسی‌ها:
  ۱. هر منبع registry.json در vendor/ وجود دارد و commit آن ثبت شده است.
  ۲. هر منبع فایل لایسنس دارد (احترام به لایسنس نویسنده‌ها).
  ۳. هیچ SKILL.md خالی/ناقص (بدون front matter) نیست.
  ۴. مهارت‌ها وارد محصول نمی‌شوند (جداسازی):
       — پوشهٔ agent-skills داخل android/ نباشد
       — android/settings.gradle.kts هیچ ماژولی از agent-skills include نکند
       — هیچ فایلی در android/ به مسیر agent-skills ارجاع ندهد
       — هیچ .git یا فایل بزرگ‌تر از ۵ مگابایت داخل vendor نباشد
     (وجود فایل‌های .kt/.gradle نمونه داخل خود مخازن مهارت طبیعی است و اشکال نیست؛
      چون در گراف Gradle ما include نمی‌شوند و به APK نمی‌رسند.)
  ۵. PROJECT-RULES.md و README.md وجود دارند.

خروج: 0 = سالم، 1 = ایراد.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # agent-skills/
REPO = ROOT.parent
VENDOR = ROOT / "vendor"
REGISTRY = ROOT / "registry.json"

BUILD_LEAK = ("build.gradle", "build.gradle.kts", "settings.gradle",
              "settings.gradle.kts", "AndroidManifest.xml", "gradle.properties")
SOURCE_EXT = {".kt", ".java", ".kts", ".jar", ".aar", ".apk", ".so"}

errors: list[str] = []
notes: list[str] = []


def main() -> int:
    if not REGISTRY.exists():
        print("FAIL: registry.json پیدا نشد")
        return 1
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))

    for src in reg["sources"]:
        sid = src["id"]
        base = VENDOR / sid
        if not base.is_dir():
            errors.append(f"{sid}: پوشهٔ vendor/{sid} وجود ندارد")
            continue
        if not re.fullmatch(r"[0-9a-f]{40}", src.get("commit", "")):
            errors.append(f"{sid}: commit باید SHA کامل ۴۰ کاراکتری باشد")
        lic = base / src.get("licenseFile", "LICENSE")
        if not lic.exists():
            candidates = list(base.glob("LICEN[SC]E*"))
            if not candidates:
                errors.append(f"{sid}: فایل لایسنس پیدا نشد")
            else:
                notes.append(f"{sid}: لایسنس در {candidates[0].name} است (registry می‌گوید {lic.name})")
        skills = list(base.rglob("SKILL.md"))
        if skills:
            for s in skills:
                head = s.read_text(encoding="utf-8", errors="replace")[:400]
                if not head.lstrip().startswith("---"):
                    errors.append(f"{sid}: front matter ندارد → {s.relative_to(ROOT)}")
        else:
            notes.append(f"{sid}: بدون SKILL.md (rule/مرجع)")

    # ۴-الف: جداسازی از محصول
    if (REPO / "android" / "agent-skills").exists():
        errors.append("agent-skills داخل android/ است — باید در ریشهٔ ریپو و بیرون از محصول باشد")
    for g in ("settings.gradle.kts", "settings.gradle"):
        f = REPO / "android" / g
        if f.exists() and "agent-skills" in f.read_text(encoding="utf-8", errors="ignore"):
            errors.append(f"android/{g} ماژولی از agent-skills را include می‌کند")
    for p in VENDOR.rglob("*"):
        if p.is_dir() and p.name == ".git":
            errors.append(f"مخزن git تودرتو داخل vendor: {p.relative_to(ROOT)}")
        elif p.is_file() and p.stat().st_size > 5 * 1024 * 1024:
            errors.append(f"فایل بزرگ‌تر از ۵MB در vendor: {p.relative_to(ROOT)}")

    # ۴-ب: هیچ ارجاعی از android/ به agent-skills نباشد
    android = REPO / "android"
    if android.is_dir():
        for p in android.rglob("*"):
            if not p.is_file() or p.stat().st_size > 400_000:
                continue
            if p.suffix not in {".gradle", ".kts", ".kt", ".xml", ".pro", ".properties", ".txt", ".md"}:
                continue
            try:
                text = p.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            if "agent-skills" in text:
                errors.append(f"ارجاع از محصول به مهارت‌ها: {p.relative_to(REPO)}")

    for required in ("README.md", "PROJECT-RULES.md", "INDEX.md", "REGISTRY.md"):
        if not (ROOT / required).exists():
            errors.append(f"فایل لازم نیست: agent-skills/{required}")

    for n in notes:
        print(f"NOTE: {n}")
    if errors:
        print("\n".join(f"FAIL: {e}" for e in errors))
        print(f"\n{len(errors)} ایراد.")
        return 1
    total = sum(1 for _ in ROOT.rglob("SKILL.md"))
    print(f"OK — {len(reg['sources'])} منبع، {total} مهارت، بدون نشت به محصول.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
