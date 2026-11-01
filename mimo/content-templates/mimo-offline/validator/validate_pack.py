#!/usr/bin/env python3
"""اعتبارسنج بستهٔ محتوایی میمو (Mimo offline content pack validator).

Checks a pack against the recovered Mimo content contract (HANDOFF/02, HANDOFF/03) and reports problems in Persian,
each with a stable code, the JSON path and a remedy. Exit code 0 = valid, 2 = problems found, 3 = pack not found.

    python3 validate_pack.py ../../content/demo
    python3 validate_pack.py my-pack --json

Checks
  E001 tracks.json missing / unreadable
  E002 publishSetVersion missing or not an integer
  E003 tracks[] empty
  E004 duplicate track id                      E005 duplicate section index
  E006 tutorial reference without id           E007 tutorial file missing
  E008 tutorial id mismatch with file name     E009 duplicate tutorial id
  E010 duplicate chapter id                    E011 duplicate lesson id
  E012 lesson without body                     E013 unsupported contentType
  E014 unbalanced / unknown tag in lesson body E015 interaction range outside the code text
  E016 selection without a correct item        E017 selection with fewer than two items
  E018 invalid visible-if value                E019 missing asset referenced by <img>/<audio>
  E020 lesson objectives not a list            E021 empty chapter
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ALLOWED_TAGS = {
    "html", "body", "head", "style", "p", "code", "content", "text", "strong", "em", "br", "img", "a",
    "selection", "item", "interactions", "interaction", "options", "option", "webview",
    "database", "tables", "table", "header", "row", "data", "output", "h1", "h2", "h3", "ul", "ol", "li",
    "blockquote", "hr", "math", "diagram", "grammar", "audio",
}
CONTENT_TYPES = {"interactive", "executableFiles"}
VISIBILITY = {"always", "wrong", "correct"}
TAG_RE = re.compile(r"<\s*/?\s*([a-zA-Z][a-zA-Z0-9-]*)")

problems: list[dict] = []


def add(code: str, path: str, message: str, remedy: str = "") -> None:
    problems.append({"code": code, "path": path, "message": message, "remedy": remedy})


def text_of(body: str, start: int, end: int) -> str:
    return body[start:end]


def check_lesson_body(body: str, path: str) -> None:
    # 1. tag balance + known tags
    stack: list[str] = []
    for match in re.finditer(r"<\s*(/?)\s*([a-zA-Z][a-zA-Z0-9-]*)([^>]*)>", body):
        closing, tag = match.group(1), match.group(2).lower()
        if tag not in ALLOWED_TAGS:
            add("E014", path, f"تگ ناشناخته <{tag}> در سند درس.", "از تگ‌های قرارداد DSL استفاده کنید یا آن را به متن تبدیل کنید.")
        if closing:
            if not stack or stack[-1] != tag:
                add("E014", path, f"تگ <{tag}> به‌درستی بسته نشده است.", "ترتیب باز و بسته شدن تگ‌ها را اصلاح کنید.")
            else:
                stack.pop()
        elif not match.group(0).rstrip().endswith("/>") and tag not in {"br", "img", "hr", "interaction"}:
            stack.append(tag)
    if stack:
        add("E014", path, "تگ‌های باز در پایان بسته نشده‌اند: " + "، ".join(stack[-3:]), "تگ‌های باز را ببندید.")

    # 2. visible-if values
    for match in re.finditer(r'visible-if\s*=\s*"([^"]*)"', body):
        if match.group(1) not in VISIBILITY:
            add("E018", path, f"مقدار visible-if نامعتبر است: {match.group(1)!r}",
                "تنها always، wrong یا correct مجاز است.")

    # 3. interaction ranges inside the code text
    for code in re.finditer(r"<code\b[^>]*>(.*?)</code>", body, re.S):
        block = code.group(1)
        content_match = re.search(r"<content>(.*?)</content>", block, re.S)
        if not content_match:
            continue
        plain = re.sub(r"<[^>]+>", "", content_match.group(1))
        for interaction in re.finditer(r"<interaction\b([^>]*)/?>", block):
            attrs = dict(re.findall(r'(\w+)\s*=\s*"([^"]*)"', interaction.group(1)))
            if "startIndex" not in attrs or "endIndex" not in attrs:
                continue
            try:
                start, end = int(attrs["startIndex"]), int(attrs["endIndex"])
            except ValueError:
                add("E015", path, "startIndex/endIndex باید عدد باشند.", "مقدار عددی بگذارید.")
                continue
            if not (0 <= start < end <= len(plain)):
                add("E015", path,
                    f"بازهٔ تعامل ({start}..{end}) بیرون از متن کد است (طول متن = {len(plain)}).",
                    "بازه را با شمارش نویسه‌های داخل <content> اصلاح کنید.")
            elif not plain[start:end].strip():
                add("E015", path, f"بازهٔ تعامل ({start}..{end}) خالی است و پاسخ قابل استخراج نیست.",
                    "بازه را روی بخشی از کد که پاسخ است بگذارید.")

    # 4. selections
    for selection in re.finditer(r"<selection\b[^>]*>(.*?)</selection>", body, re.S):
        items = re.findall(r"<item\b([^>]*)>", selection.group(1))
        if len(items) < 2:
            add("E017", path, "یک <selection> کمتر از دو گزینه دارد.", "دست‌کم دو <item> اضافه کنید.")
        correct = [i for i in items if re.search(r'correct\s*=\s*"true"', i)]
        if not correct:
            add("E016", path, "در <selection> هیچ گزینهٔ درستی علامت‌گذاری نشده است.",
                'روی گزینهٔ درست، correct="true" بگذارید.')


def check_pack(pack_dir: Path) -> list[dict]:
    tracks_path = pack_dir / "tracks.json"
    if not tracks_path.is_file():
        add("E001", "tracks.json", "فایل tracks.json پیدا نشد.", "این فایل ریشهٔ بستهٔ محتوایی است.")
        return problems
    try:
        tracks = json.loads(tracks_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        add("E001", "tracks.json", f"JSON نامعتبر است: {exc}", "ساختار JSON را بررسی کنید.")
        return problems

    version = tracks.get("publishSetVersion")
    if not isinstance(version, int):
        add("E002", "tracks.json.publishSetVersion", "publishSetVersion باید عدد صحیح باشد.",
            "مثلاً 1 یا 753 بگذارید.")

    track_list = tracks.get("tracks") or []
    if not track_list:
        add("E003", "tracks.json.tracks", "هیچ مسیر یادگیری تعریف نشده است.", "دست‌کم یک track اضافه کنید.")

    seen_tracks: set[int] = set()
    tutorial_ids: list[int] = []

    for ti, track in enumerate(track_list):
        tpath = f"tracks[{ti}]"
        tid = track.get("id")
        if not isinstance(tid, int):
            add("E004", tpath + ".id", "شناسهٔ مسیر باید عدد باشد.", "یک عدد یکتا برای هر مسیر بگذارید.")
        elif tid in seen_tracks:
            add("E004", tpath + ".id", f"شناسهٔ مسیر تکراری است: {tid}", "شناسه‌ها باید یکتا باشند.")
        else:
            seen_tracks.add(tid)

        section_indexes: set[int] = set()
        for si, section in enumerate(track.get("sections") or []):
            spath = f"{tpath}.sections[{si}]"
            idx = section.get("index")
            if isinstance(idx, int):
                if idx in section_indexes:
                    add("E005", spath + ".index", f"index تکراری در مسیر {tid}: {idx}", "هر بخش index یکتا داشته باشد.")
                section_indexes.add(idx)
            for ri, ref in enumerate(section.get("tutorials") or []):
                rpath = f"{spath}.tutorials[{ri}]"
                ref_id = ref.get("id")
                if not isinstance(ref_id, int):
                    add("E006", rpath + ".id", "مرجع توتوریال بدون شناسهٔ عددی است.", "id عددی توتوریال را بنویسید.")
                    continue
                tutorial_ids.append(ref_id)
                file = pack_dir / f"tutorial-{ref_id}.json"
                if not file.is_file():
                    add("E007", rpath + ".id", f"فایل tutorial-{ref_id}.json وجود ندارد.",
                        "فایل توتوریال را بسازید یا مرجع را اصلاح کنید.")
                    continue
                try:
                    tutorial = json.loads(file.read_text(encoding="utf-8"))
                except json.JSONDecodeError as exc:
                    add("E007", f"tutorial-{ref_id}.json", f"JSON نامعتبر است: {exc}", "ساختار فایل را بررسی کنید.")
                    continue
                if tutorial.get("id") != ref_id:
                    add("E008", f"tutorial-{ref_id}.json.id",
                        f"شناسهٔ داخل فایل ({tutorial.get('id')}) با نام فایل ({ref_id}) یکی نیست.",
                        "شناسه‌ها را هم‌تراز کنید.")
                seen_chapters: set[int] = set()
                seen_lessons: set[int] = set()
                chapters = tutorial.get("chapters") or []
                if not chapters:
                    add("E021", f"tutorial-{ref_id}.json.chapters", "توتوریال هیچ فصلی ندارد.", "دست‌کم یک chapter اضافه کنید.")
                for ci, chapter in enumerate(chapters):
                    cpath = f"tutorial-{ref_id}.json.chapters[{ci}]"
                    cid = chapter.get("id")
                    if isinstance(cid, int):
                        if cid in seen_chapters:
                            add("E010", cpath + ".id", f"شناسهٔ فصل تکراری است: {cid}", "شناسه‌ها را یکتا کنید.")
                        seen_chapters.add(cid)
                    for li, lesson in enumerate(chapter.get("lessons") or []):
                        lpath = f"{cpath}.lessons[{li}]"
                        lid = lesson.get("id")
                        if isinstance(lid, int):
                            if lid in seen_lessons:
                                add("E011", lpath + ".id", f"شناسهٔ درس تکراری است: {lid}",
                                    "شناسهٔ درس باید در کل توتوریال یکتا باشد.")
                            seen_lessons.add(lid)
                        ctype = lesson.get("contentType")
                        if ctype not in CONTENT_TYPES:
                            add("E013", lpath + ".contentType",
                                f"contentType نامعتبر: {ctype!r}", "interactive یا executableFiles مجاز است.")
                        body = lesson.get("body") or (lesson.get("interactiveContent") or {}).get("body")
                        if not body:
                            add("E012", lpath + ".body", "درس هیچ متنی ندارد.", "بدنهٔ درس را در body بنویسید.")
                        else:
                            check_lesson_body(body, lpath + ".body")
                            for asset in re.finditer(r'<(?:img|audio)\b[^>]*src\s*=\s*"([^"]+)"', body):
                                src = asset.group(1)
                                if re.match(r"^(https?:|data:)", src):
                                    continue
                                if not (pack_dir / src).is_file():
                                    add("E019", lpath + ".body", f"فایل دارایی پیدا نشد: {src}",
                                        "مسیر را نسبت به ریشهٔ بسته اصلاح کنید یا فایل را اضافه کنید.")
                        if "objectives" in lesson and not isinstance(lesson["objectives"], list):
                            add("E020", lpath + ".objectives", "objectives باید فهرست باشد.",
                                'مثلاً ["هدف ۱", "هدف ۲"]')

    duplicates = {i for i in tutorial_ids if tutorial_ids.count(i) > 1}
    for dup in duplicates:
        add("E009", "tracks.json", f"توتوریال {dup} در بیش از یک بخش تکرار شده است.",
            "هر توتوریال را یک بار به یک بخش نسبت دهید.")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description="اعتبارسنج بستهٔ محتوایی آفلاین میمو")
    ap.add_argument("pack", type=Path)
    ap.add_argument("--json", action="store_true", help="خروجی ماشین‌خوان")
    args = ap.parse_args()

    if not args.pack.is_dir():
        print(f"بستهٔ محتوایی پیدا نشد: {args.pack}", file=sys.stderr)
        return 3

    check_pack(args.pack)

    if args.json:
        print(json.dumps({"pack": str(args.pack), "valid": not problems, "problems": problems},
                         ensure_ascii=False, indent=1))
    else:
        if not problems:
            print(f"✅ بسته معتبر است: {args.pack}")
        else:
            print(f"❌ {len(problems)} مشکل در بسته پیدا شد: {args.pack}\n")
            for problem in problems:
                print(f"  [{problem['code']}] {problem['path']}")
                print(f"      مشکل: {problem['message']}")
                if problem["remedy"]:
                    print(f"      راه‌حل: {problem['remedy']}")
    return 0 if not problems else 2


if __name__ == "__main__":
    raise SystemExit(main())
