#!/usr/bin/env python3
"""Smoke-test a running preview: every route the shell needs must answer, and every asset it references must exist.

    python3 mimo/tools/smoke_preview.py --base http://127.0.0.1:4000

Checks
  1. the shell HTML answers and references assets that also answer (catches a broken <link>/<script> path)
  2. the learn engine modules and content manifests answer
  3. /practice/ and /max answer, and the overlay is injected into both engine pages
  4. the overlay dictionaries answer and pass their basic contract (non-empty, key != value)
  5. /api/preview/status reports all three engines ok (unless the corresponding port is intentionally down)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.error
import urllib.request

failures: list[str] = []


def get(base: str, path: str) -> tuple[int, bytes]:
    try:
        with urllib.request.urlopen(base + path, timeout=10) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, b""
    except OSError as exc:
        return 0, str(exc).encode()


def check(base: str, path: str, label: str, expect: int = 200) -> bytes | None:
    status, body = get(base, path)
    ok = status == expect
    print(f"  {'PASS' if ok else 'FAIL'}  {label:<44} {path:<28} {status}")
    if not ok:
        failures.append(f"{label}: {path} → {status} (expected {expect})")
        return None
    return body


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="http://127.0.0.1:4000")
    ap.add_argument("--no-engines", action="store_true", help="skip the /practice and /max checks")
    args = ap.parse_args()
    base = args.base.rstrip("/")

    print("۱) پوسته و دارایی‌ها")
    html = check(base, "/", "shell html")
    if html:
        text = html.decode("utf-8", "replace")
        if 'dir="rtl"' not in text or 'lang="fa"' not in text:
            failures.append("shell html is not RTL/Persian")
        for ref in sorted(set(re.findall(r'(?:href|src)="(\./[^"]+)"', text))):
            check(base, "/" + ref[2:], "shell asset")

    print("۲) موتور یادگیری")
    for path in ("/learn/dsl.js", "/learn/render.js", "/learn/lesson.js", "/learn/grade.js",
                 "/learn/store.js", "/learn/model.js", "/learn/content.js",
                 "/content/index.json", "/content/demo/tracks.json", "/content/demo/tutorial-101.json"):
        check(base, path, "learn module/content")

    if not args.no_engines:
        print("۳) موتورهای جاسازی‌شده و تزریق لایهٔ ترجمه")
        for path in ("/practice/", "/max", "/practice/api/health", "/practice/api/papers"):
            body = check(base, path, "engine route")
            if body and path in ("/practice/", "/max"):
                if b"__overlay/fa.js" not in body:
                    failures.append(f"overlay not injected into {path}")
                    print(f"  FAIL  overlay not injected into {path}")

    print("۴) دیکشنری‌های ترجمه")
    for name, expected_lang in (("dict-epm.json", "zh"), ("dict-max.json", "en")):
        body = check(base, f"/__overlay/{name}", "dictionary")
        if not body:
            continue
        data = json.loads(body)
        strings = data.get("strings") or {}
        empty = [k for k, v in strings.items() if not v or v == k]
        print(f"  INFO  {name}: {len(strings)} entries, {len(data.get('patterns') or [])} patterns")
        if empty:
            failures.append(f"{name}: {len(empty)} empty/identical translations")

    print("۵) وضعیت موتورها")
    body = check(base, "/api/preview/status", "status endpoint")
    if body:
        status = json.loads(body)
        for engine, info in status.get("engines", {}).items():
            ok = bool(info.get("ok"))
            print(f"  {'PASS' if ok else 'WARN'}  {engine} ok={ok}")
            if not ok and not args.no_engines and engine in ("practice", "max"):
                failures.append(f"engine {engine} reports not ok")

    checks = 20 if not args.no_engines else 16
    print(f"\n   {checks - len(failures)}/{checks} بررسی موفق")
    if failures:
        print(f"❌ {len(failures)} مشکل:")
        for item in failures:
            print(f"  - {item}")
        return 1
    print("✅ همهٔ مسیرهای پیش‌نمایش پاسخ می‌دهند")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
