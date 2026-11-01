#!/usr/bin/env python3
"""End-to-end check against the running EPM engine, using only its public API.

Flow (the same one the EPM UI performs):
    start exam → fetch exam → answer questions → submit → read score → read history → read wrong bank

The script answers 4 questions correctly, 1 incorrectly and leaves 1 blank, then asserts the server's arithmetic.

Usage:
    python3 e2e_exam_test.py --csv data/example-questions.csv --base http://127.0.0.1:8765/api
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

PASS, FAIL = "PASS", "FAIL"
results: list[tuple[str, str, str]] = []


def call(url: str, method: str = "GET", payload: dict | None = None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, method=method, data=data)
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=60) as res:  # noqa: S310 - localhost only
            raw = res.read().decode("utf-8", "replace")
            try:
                return res.status, json.loads(raw or "{}")
            except json.JSONDecodeError:
                return res.status, raw
    except urllib.error.HTTPError as err:
        return err.code, err.read().decode("utf-8", "replace")


def check(name: str, ok: bool, detail: str = "") -> None:
    results.append((PASS if ok else FAIL, name, detail))
    print(f"[{PASS if ok else FAIL}] {name}" + (f" — {detail}" if detail else ""))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--csv", type=Path, default=Path("data/example-questions.csv"))
    ap.add_argument("--base", default="http://127.0.0.1:8765/api")
    ap.add_argument("--count", type=int, default=6)
    ap.add_argument("--profile", type=int, default=6, help="پروفایل بانک سؤال که آزمون از آن نمونه می‌گیرد")
    args = ap.parse_args()

    with args.csv.open(encoding="utf-8-sig", newline="") as fh:
        rows = list(csv.DictReader(fh))
    # the exam session API exposes the question id/stem but not the external key, so match on the stem as well
    answer_key = {row["question_key"]: row["correct"].strip().upper() for row in rows}
    by_stem = {row["stem"].strip(): row["correct"].strip().upper() for row in rows}

    status, exam = call(f"{args.base}/exam/start", "POST", {"profile_id": args.profile, "count": args.count, "minutes": 20})
    if status >= 400:
        print(f"آزمون شروع نشد ({status}): {exam}")
        return 1
    exam_id = exam["id"]
    check("شروع آزمون", exam.get("total_questions") == args.count, f"exam_id={exam_id}")

    status, session = call(f"{args.base}/exam/sessions/{exam_id}")
    questions = session.get("questions", [])
    check("دریافت سؤال‌ها", len(questions) == args.count, f"{len(questions)} سؤال")
    check("هر سؤال چهار گزینه دارد", all(len(q["options"]) == 4 for q in questions),
          str({q["id"]: len(q["options"]) for q in questions}))

    planned = []
    for idx, question in enumerate(questions):
        key = question.get("question_key") or ""
        options = [o["key"] for o in question["options"]]
        correct = answer_key.get(key) or by_stem.get((question.get("stem") or "").strip())
        if correct is None:
            check("شناسایی پاسخ درست", False, f"سؤال ناشناخته: {question.get('id')}")
            return 1
        if idx < 4:
            planned.append((question, correct, "درست"))
        elif idx == 4:
            wrong = next(k for k in options if k != correct)
            planned.append((question, wrong, "نادرست"))
        else:
            planned.append((question, None, "بی‌پاسخ"))

    for question, answer, label in planned:
        if answer is None:
            continue
        status, _ = call(f"{args.base}/exam/sessions/{exam_id}/answers/{question['id']}", "PUT", {"answer": answer})
        if status >= 400:
            check(f"ثبت پاسخ {label}", False, f"HTTP {status}")
    check("ثبت پاسخ‌ها", True, "۴ درست، ۱ نادرست، ۱ بی‌پاسخ")

    status, submitted = call(f"{args.base}/exam/sessions/{exam_id}/submit", "POST", {})
    if status >= 400:
        check("تحویل آزمون", False, str(submitted))
        return 1
    check("تحویل آزمون", submitted.get("status") in {"submitted", "graded"}, str(submitted.get("status")))

    status, review = call(f"{args.base}/exam/sessions/{exam_id}")
    score = review.get("score")
    max_score = review.get("max_score")
    check("نمره محاسبه شد", score == 8 and max_score == 12, f"score={score}/{max_score}")
    check("شمارش درست/نادرست", review.get("correct_count") == 4 and review.get("wrong_count") == 1
          and review.get("unanswered_count") == 1,
          f"correct={review.get('correct_count')} wrong={review.get('wrong_count')} blank={review.get('unanswered_count')}")
    check("بازبینی پاسخ‌ها ماندگار است", any(q.get("answered") for q in review.get("questions", [])))

    status, history = call(f"{args.base}/exam/history")
    ok = status == 200 and isinstance(history, (list, dict))
    check("تاریخچهٔ آزمون", ok, f"HTTP {status}")

    status, wrong = call(f"{args.base}/wrong")
    ok_wrong = status == 200 and isinstance(wrong, (list, dict))
    if isinstance(wrong, dict):
        ok_wrong = ok_wrong and (wrong.get("total", 0) >= 1 or bool(wrong.get("items")))
    check("دفتر اشتباهات در دسترس است", ok_wrong, f"HTTP {status}")

    failed = [r for r in results if r[0] == FAIL]
    print(f"\n{len(results) - len(failed)}/{len(results)} بررسی موفق")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
