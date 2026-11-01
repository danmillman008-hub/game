#!/usr/bin/env python3
"""Build an EPM-native ESQ 1.0 package from a Persian-friendly CSV.

ESQ 1.0 is EPM's own exchange format (`docs/question-bank-format.md` in the EPM repository): a ZIP containing
manifest.json, papers/<year>.json and answers/<year>.json. Using it means the bank imports through EPM's real import
path — no custom JSON, no manual conversion per bank.

Authoring rules enforced here (and re-checked by validate_bank.py):
  * exactly four options A–D per question
  * exactly one correct option
  * unique question keys and unique numbers per paper
  * every question belongs to a unit declared once per paper
  * score is a positive number

Usage:
    python3 build_esq.py data/example-questions.csv out/example-bank.esq --title "…" --year 2026
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import zipfile
from collections import OrderedDict
from pathlib import Path

REQUIRED = ["unit_key", "unit_title", "unit_type", "question_key", "number", "stem",
            "option_a", "option_b", "option_c", "option_d", "correct"]

# ESQ 1.0 / EPM validator:  backend/app/services/esq.py  (unit.get("type") not in {...})
UNIT_TYPES = {"cloze", "reading", "part_b", "listening", "word_bank", "paragraph_matching"}


def fail(msg: str) -> "NoReturn":  # type: ignore[name-defined]
    print(f"خطا: {msg}", file=sys.stderr)
    raise SystemExit(2)


def read_rows(path: Path) -> list[dict]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        fail("فایل CSV هیچ سؤالی ندارد.")
    header = rows[0].keys()
    missing = [h for h in REQUIRED if h not in header]
    if missing:
        fail("ستون‌های لازم در CSV نیست: " + "، ".join(missing))
    # A cell beyond the last header column lands under the None key. Silently dropping it would hide a fifth option,
    # so refuse instead: the four-option rule must be enforced, not assumed.
    for idx, row in enumerate(rows, start=2):
        if None in row and any((cell or "").strip() for cell in (row[None] or [])):
            fail(f"سطر {idx}: ستون ناشناخته دارد؛ هر سؤال فقط چهار گزینه A–D می‌پذیرد.")
    return rows


def build(rows: list[dict], *, package_id: str, title: str, year: int, subject: str) -> tuple[dict, dict, dict]:
    units: "OrderedDict[str, dict]" = OrderedDict()
    answers: dict[str, dict] = {}
    seen_q: set[str] = set()
    for idx, row in enumerate(rows, start=2):  # CSV line number
        qkey = (row.get("question_key") or "").strip()
        if not qkey:
            fail(f"سطر {idx}: question_key خالی است.")
        if qkey in seen_q:
            fail(f"سطر {idx}: شناسهٔ سؤال تکراری است: {qkey}")
        seen_q.add(qkey)
        options = []
        for label in "ABCD":
            text = (row.get(f"option_{label.lower()}") or "").strip()
            if not text:
                fail(f"سطر {idx}: گزینهٔ {label} خالی است؛ هر سؤال باید چهار گزینه داشته باشد.")
            options.append({"key": label, "content": text})
        correct = (row.get("correct") or "").strip().upper()
        if correct not in {"A", "B", "C", "D"}:
            fail(f"سطر {idx}: ستون correct باید یکی از A/B/C/D باشد (مقدار: {correct!r}).")
        try:
            number = int(row.get("number") or 0)
        except ValueError:
            fail(f"سطر {idx}: number باید عدد باشد.")
        if number <= 0:
            fail(f"سطر {idx}: number باید بزرگ‌تر از صفر باشد.")
        try:
            score = float(row.get("score") or 2)
        except ValueError:
            fail(f"سطر {idx}: score باید عدد باشد.")
        metadata = {}
        if (row.get("explanation") or "").strip():
            metadata["explanation"] = row["explanation"].strip()
            metadata["explanation_language"] = "fa"
        unit_key = row["unit_key"].strip()
        unit = units.get(unit_key)
        if unit is None:
            unit_type = (row.get("unit_type") or "reading").strip()
            if unit_type not in UNIT_TYPES:
                # the authoring CSV uses friendly names; EPM only accepts its own six unit types
                unit_type = "reading"
            unit = {
                "unitKey": unit_key,
                "type": unit_type,
                "title": (row.get("unit_title") or unit_key).strip(),
                "sequence": len(units) + 1,
                "passage": {"blocks": []},
                "questions": [],
            }
            passage = (row.get("passage") or "").strip()
            if passage:
                unit["passage"] = {"blocks": [{"blockKey": "p01", "type": "paragraph", "text": passage}]}
            units[unit_key] = unit
        elif (row.get("passage") or "").strip() and not unit["passage"]["blocks"]:
            unit["passage"] = {"blocks": [{"blockKey": "p01", "type": "paragraph", "text": row["passage"].strip()}]}
        question = {
            "questionKey": qkey,
            "number": number,
            "type": "single_choice",
            "stem": (row.get("stem") or "").strip(),
            "options": options,
            "score": score,
        }
        if metadata:
            question["metadata"] = metadata
        unit["questions"].append(question)
        answers[qkey] = {"correctOption": correct, "score": score}

    for unit in units.values():
        numbers = [q["number"] for q in unit["questions"]]
        if len(set(numbers)) != len(numbers):
            fail(f"واحد {unit['unitKey']}: شمارهٔ سؤال تکراری دارد.")

    paper_key = f"{package_id}.{year}"
    manifest = {
        "format": "esq",
        "schemaVersion": "1.0",
        "packageId": package_id,
        "contentVersion": "1.0.0",
        "title": title,
        "subject": subject,
        "language": "en",
        "locale": "fa-IR",
        "publisher": "Mimo preview — محتوای نمونه",
        "license": {"spdx": "CC0-1.0", "notice": "محتوای نمونهٔ خودنوشت برای آزمون قالب؛ آزاد برای استفاده."},
        "source": {"type": "demo", "description": "سؤال‌های نمونه، نوشته‌شده برای این پیش‌نمایش."},
        "papers": [{"paperKey": paper_key, "year": year, "path": f"papers/{year}.json",
                    "answerPath": f"answers/{year}.json"}],
        "features": {"hasAnswers": True, "hasAiLabels": False, "hasAssets": False},
        "generator": {"name": "mimo-preview-epm-template", "version": "0.1.0"},
    }
    paper = {
        "paperKey": paper_key,
        "year": year,
        "title": f"{title} ({year})",
        "subject": subject,
        "units": list(units.values()),
    }
    answer_doc = {"paperKey": paper_key, "answers": answers}
    return manifest, paper, answer_doc


def write_package(out: Path, manifest: dict, paper: dict, answers: dict, year: int) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("manifest.json", json.dumps(manifest, ensure_ascii=False, indent=2))
        zf.writestr(f"papers/{year}.json", json.dumps(paper, ensure_ascii=False, indent=2))
        zf.writestr(f"answers/{year}.json", json.dumps(answers, ensure_ascii=False, indent=2))
        zf.writestr("LICENSE.txt", "محتوای نمونه — CC0-1.0")
        zf.writestr("README.md", "بانک نمونهٔ ESQ 1.0 ساخته‌شده برای پیش‌نمایش Mimo/EPM.")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", type=Path)
    ap.add_argument("out", type=Path)
    ap.add_argument("--title", default="بانک نمونهٔ کانکور — پیش‌نمایش")
    ap.add_argument("--subject", default="English (Konkur-style)")
    ap.add_argument("--year", type=int, default=2026)
    ap.add_argument("--package-id", default="ir.mimo.preview.konkur.sample")
    args = ap.parse_args()

    rows = read_rows(args.csv)
    manifest, paper, answers = build(rows, package_id=args.package_id, title=args.title,
                                     year=args.year, subject=args.subject)
    write_package(args.out, manifest, paper, answers, args.year)
    total = sum(len(u["questions"]) for u in paper["units"])
    print(f"ساخته شد: {args.out} — {total} سؤال در {len(paper['units'])} واحد، سال {args.year}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
