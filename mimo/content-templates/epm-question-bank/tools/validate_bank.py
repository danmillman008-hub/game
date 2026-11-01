#!/usr/bin/env python3
"""Validate an .esq package: structural rules first, then EPM's own loader when the engine checkout is available.

Structural rules (always):
  * manifest declares format=esq, schemaVersion=1.0, at least one paper
  * every paper file and answer file exists and is valid JSON
  * every question has exactly four options keyed A–D
  * every question has exactly one answer entry, and its correctOption ∈ A–D and present in the options
  * question keys are unique across the package; unit types are in EPM's supported set

With `--epm <path>` (or when mimo/engines/src/epm exists) the package is also run through EPM's authoritative loader,
so the verdict matches what the importer will decide.

Usage: python3 validate_bank.py example-bank/sample-bank.esq [--epm ../../engines/src/epm]
"""
from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path

UNIT_TYPES = {"cloze", "reading", "part_b", "listening", "word_bank", "paragraph_matching"}
problems: list[str] = []


def problem(message: str) -> None:
    problems.append(message)


def validate_structure(package_path: Path) -> None:
    try:
        zf = zipfile.ZipFile(package_path)
    except zipfile.BadZipFile:
        problem("فایل یک ZIP معتبر نیست (پسوند .esq باید ZIP باشد).")
        return
    names = set(zf.namelist())
    if "manifest.json" not in names:
        problem("manifest.json در بسته نیست.")
        return
    manifest = json.loads(zf.read("manifest.json"))
    if manifest.get("format") != "esq":
        problem("فیلد format باید «esq» باشد.")
    if manifest.get("schemaVersion") != "1.0":
        problem("فقط schemaVersion=1.0 پذیرفته می‌شود.")
    papers = manifest.get("papers") or []
    if not papers:
        problem("هیچ جزوه‌ای در manifest معرفی نشده است.")
    seen_questions: set[str] = set()
    for ref in papers:
        paper_path = ref.get("path")
        answer_path = ref.get("answerPath")
        if paper_path not in names:
            problem(f"فایل جزوه در بسته نیست: {paper_path}")
            continue
        if answer_path not in names:
            problem(f"فایل کلید پاسخ در بسته نیست: {answer_path}")
            continue
        paper = json.loads(zf.read(paper_path))
        answers = json.loads(zf.read(answer_path)).get("answers") or {}
        for unit in paper.get("units") or []:
            if unit.get("type") not in UNIT_TYPES:
                problem(f"نوع واحد پشتیبانی نمی‌شود: {unit.get('type')!r} (واحد {unit.get('unitKey')})")
            if not isinstance(unit.get("passage"), dict):
                problem(f"واحد {unit.get('unitKey')}: passage باید شیء باشد (حتی {{'blocks': []}}).")
            for question in unit.get("questions") or []:
                qkey = question.get("questionKey")
                if qkey in seen_questions:
                    problem(f"شناسهٔ سؤال تکراری است: {qkey}")
                seen_questions.add(qkey)
                options = question.get("options") or []
                keys = [o.get("key") for o in options]
                if len(options) != 4:
                    problem(f"سؤال {qkey}: باید دقیقاً ۴ گزینه داشته باشد (دارد: {len(options)}).")
                if keys != ["A", "B", "C", "D"]:
                    problem(f"سؤال {qkey}: کلید گزینه‌ها باید A,B,C,D باشد (هست: {keys}).")
                if any(not (o.get("content") or "").strip() for o in options):
                    problem(f"سؤال {qkey}: یکی از گزینه‌ها خالی است.")
                if question.get("type") != "single_choice":
                    problem(f"سؤال {qkey}: نوع باید single_choice باشد (هست: {question.get('type')}).")
                answer = answers.get(qkey)
                if not answer:
                    problem(f"سؤال {qkey}: کلید پاسخ ندارد.")
                    continue
                correct = answer.get("correctOption")
                if correct not in {"A", "B", "C", "D"}:
                    problem(f"سؤال {qkey}: correctOption باید A/B/C/D باشد (هست: {correct!r}).")
                elif correct not in keys:
                    problem(f"سؤال {qkey}: correctOption={correct} در گزینه‌ها نیست.")
        extra = set(answers) - {q.get("questionKey") for u in paper.get("units") or [] for q in u.get("questions") or []}
        for key in extra:
            problem(f"کلید پاسخ برای سؤال ناموجود: {key}")


def validate_with_epm(package_path: Path, epm_root: Path) -> bool:
    sys.path.insert(0, str(epm_root))
    try:
        from backend.app.services.esq import load_esq_package, EsqValidationError  # type: ignore
    except Exception as exc:  # noqa: BLE001
        problem(f"بارگذاری اعتبارسنج بومی EPM ممکن نشد ({exc}); فقط بررسی ساختاری انجام شد.")
        return False
    try:
        package = load_esq_package(package_path)
    except EsqValidationError as exc:  # type: ignore
        for detail in getattr(exc, "details", []) or [str(exc)]:
            problem(f"اعتبارسنج EPM: {detail}")
        return False
    total = sum(len(u.get("questions") or []) for p in package.get("papers", []) for u in p.get("units", []))
    print(f"اعتبارسنج بومی EPM پذیرفت: {len(package.get('papers', []))} جزوه، {total} سؤال")
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("package", type=Path)
    ap.add_argument("--epm", type=Path, default=None, help="مسیر ریشهٔ مخزن EPM برای اعتبارسنجی بومی")
    args = ap.parse_args()

    if not args.package.is_file():
        print(f"فایل پیدا نشد: {args.package}", file=sys.stderr)
        return 2

    validate_structure(args.package)

    epm_root = args.epm
    if epm_root is None:
        candidate = Path(__file__).resolve().parents[3] / "engines" / "src" / "epm"
        if candidate.is_dir():
            epm_root = candidate
    if epm_root and epm_root.is_dir():
        validate_with_epm(args.package, epm_root)

    if problems:
        print(f"❌ {len(problems)} مشکل در بستهٔ سؤال:")
        for item in problems:
            print(f"  - {item}")
        return 2
    print(f"✅ بستهٔ سؤال معتبر است: {args.package}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
