#!/usr/bin/env python3
"""Import an ESQ package through EPM's own import API (no bypass, no direct database writes).

Steps, exactly the ones the EPM UI performs:
  1. POST /api/question-banks/imports         (multipart file upload → draft import job)
  2. POST /api/question-banks/imports/{id}/publish
  3. GET  /api/papers                          (confirmation)

Usage:
    python3 import_bank.py example-bank/sample-bank.esq --base http://127.0.0.1:8765/api
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path


def multipart(field: str, filename: str, payload: bytes, extra_fields: dict[str, str] | None = None) -> tuple[bytes, str]:
    boundary = f"----mimo{uuid.uuid4().hex}"
    parts = [
        f"--{boundary}\r\n".encode(),
        f'Content-Disposition: form-data; name="{field}"; filename="{filename}"\r\n'.encode(),
        b"Content-Type: application/zip\r\n\r\n",
        payload,
        b"\r\n",
    ]
    for key, value in (extra_fields or {}).items():
        parts += [
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="{key}"\r\n\r\n'.encode(),
            str(value).encode(),
            b"\r\n",
        ]
    parts.append(f"--{boundary}--\r\n".encode())
    return b"".join(parts), f"multipart/form-data; boundary={boundary}"


def call(url: str, method: str = "GET", data: bytes | None = None, ctype: str | None = None) -> tuple[int, dict | list | str]:
    req = urllib.request.Request(url, method=method, data=data)
    if ctype:
        req.add_header("Content-Type", ctype)
    try:
        with urllib.request.urlopen(req, timeout=60) as res:  # noqa: S310 - localhost only
            raw = res.read().decode("utf-8", "replace")
            payload: dict | list | str = json.loads(raw) if raw.startswith(("{", "[")) else raw
            return res.status, payload
    except urllib.error.HTTPError as err:
        raw = err.read().decode("utf-8", "replace")
        try:
            return err.code, json.loads(raw)
        except json.JSONDecodeError:
            return err.code, raw


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("esq", type=Path)
    ap.add_argument("--base", default="http://127.0.0.1:8765/api")
    ap.add_argument("--no-publish", action="store_true")
    ap.add_argument("--profile", type=int, default=None, help="شناسهٔ پروفایل بانک سؤال (اختیاری)")
    args = ap.parse_args()

    if not args.esq.is_file():
        print(f"فایل پیدا نشد: {args.esq}", file=sys.stderr)
        return 2

    status, payload = call(f"{args.base}/health")
    if status != 200:
        print(f"EPM در دسترس نیست ({args.base}): {status} {payload}", file=sys.stderr)
        return 3

    extra = {"profile_id": str(args.profile)} if args.profile else None
    body, ctype = multipart("file", args.esq.name, args.esq.read_bytes(), extra)
    status, job = call(f"{args.base}/question-banks/imports", method="POST", data=body, ctype=ctype)
    if status >= 400 or not isinstance(job, dict):
        print(f"بارگذاری ناموفق بود ({status}): {job}", file=sys.stderr)
        return 4
    job_id = job.get("id")
    print(f"وظیفهٔ وارد‌سازی ساخته شد: id={job_id} وضعیت={job.get('status')}")
    warnings = job.get("warnings") or []
    if warnings:
        print("هشدارها:", warnings)

    if args.no_publish:
        return 0

    status, published = call(f"{args.base}/question-banks/imports/{job_id}/publish", method="POST", data=b"{}",
                             ctype="application/json")
    if status >= 400:
        print(f"انتشار ناموفق بود ({status}): {published}", file=sys.stderr)
        return 5
    print("منتشر شد:", json.dumps(published, ensure_ascii=False)[:300])

    status, papers = call(f"{args.base}/papers")
    if status == 200 and isinstance(papers, list):
        print(f"تعداد جزوه‌های موجود: {len(papers)}")
        for paper in papers[:5]:
            print(f"  - id={paper.get('id')} سال={paper.get('year')} عنوان={paper.get('title')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
