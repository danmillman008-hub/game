#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
پروکسی محلی برای «بررسی آنلاین» نرم‌افزار انبارگردانی داروخانه
==============================================================

این فایل اختیاری است و فقط زمانی لازم است که مرورگر به‌دلیل محدودیت CORS
اجازهٔ خواندن پاسخ سامانهٔ تیتک را ندهد (در «تست اتصال به تیتک» پیام blocked می‌بینید).

اجرا (روی همان کامپیوتری که برنامه در آن باز است، داخل ایران):

    python ttac-proxy.py
    python ttac-proxy.py --port 9000        # پورت دیگر
    python ttac-proxy.py --host 0.0.0.0     # دسترسی از گوشی/تبلت در همان شبکه

سپس در برنامه: تب «دیتابیس» ← بخش «بررسی آنلاین» ← کادر پروکسی محلی:

    http://127.0.0.1:8765/ttac?url={url}

سپس دکمهٔ «تست اتصال به تیتک» را بزنید.

نکته‌ها
------
* فقط به دامنه‌های رسمی تیتک اجازهٔ عبور می‌دهد (allow-list).
* هیچ داده‌ای جایی ذخیره یا ارسال نمی‌شود؛ فقط درخواست را از سمت پایتون می‌فرستد
  و پاسخ را با هدرهای CORS به مرورگر برمی‌گرداند.
* فقط کتابخانهٔ استاندارد پایتون لازم است (بدون نصب هیچ پکیجی).
"""

import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

ALLOWED_HOSTS = {
    "irc.ttac.ir",
    "newapi.ttac.ir",
    "mobile.ttac.ir",
    "ttac.ir",
    "www.ttac.ir",
    "irc.fda.gov.ir",
}

UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
)


def upstream_headers(host: str, incoming: dict) -> dict:
    """هدرهایی که سامانهٔ تیتک انتظار دارد."""
    h = {
        "User-Agent": UA,
        "Accept": "text/html,application/json,*/*",
        "Accept-Language": "fa-IR,fa;q=0.9,en;q=0.8",
        "Connection": "close",
    }
    if host.endswith("newapi.ttac.ir"):
        h["Origin"] = "https://mobile.ttac.ir"
        h["Referer"] = "https://mobile.ttac.ir/"
    else:
        h["Origin"] = "https://irc.ttac.ir"
        h["Referer"] = "https://irc.ttac.ir/"
    # عبور کلید API اپ موبایل در صورت ارسال از سمت مرورگر
    for k in ("x-ssp-api-key",):
        if incoming.get(k):
            h[k] = incoming[k]
    return h


class Handler(BaseHTTPRequestHandler):
    server_version = "ttac-proxy/1.0"
    protocol_version = "HTTP/1.1"

    def log_message(self, fmt, *args):  # لاگ کوتاه
        sys.stderr.write("[ttac-proxy] %s - %s\n" % (self.address_string(), fmt % args))

    # ---------- CORS ----------
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Private-Network", "true")
        self.send_header("Access-Control-Max-Age", "600")

    def _send(self, code, body: bytes, ctype="text/plain; charset=utf-8"):
        self.send_response(code)
        self._cors()
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    # ---------- routes ----------
    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.send_header("Content-Length", "0")
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path in ("/", "/health"):
            return self._send(200, json.dumps({"ok": True, "service": "ttac-proxy"}).encode(),
                              "application/json; charset=utf-8")

        if parsed.path != "/ttac":
            return self._send(404, "not found".encode())

        qs = urllib.parse.parse_qs(parsed.query)
        target = (qs.get("url") or [""])[0]
        if not target:
            return self._send(400, "missing ?url=".encode())

        u = urllib.parse.urlparse(target)
        if u.scheme not in ("http", "https"):
            return self._send(400, "bad scheme".encode())
        if (u.hostname or "").lower() not in ALLOWED_HOSTS:
            return self._send(403, ("host not allowed: %s" % (u.hostname or "?")).encode())

        req = urllib.request.Request(target, headers=upstream_headers(u.hostname.lower(), self.headers))
        try:
            with urllib.request.urlopen(req, timeout=12) as r:
                body = r.read()
                ctype = r.headers.get("Content-Type", "text/html; charset=utf-8")
                return self._send(r.status, body, ctype)
        except urllib.error.HTTPError as e:  # خطای HTTP سامانه را عیناً برگردان
            try:
                body = e.read()
            except Exception:
                body = b""
            return self._send(e.code, body, e.headers.get("Content-Type", "text/plain; charset=utf-8"))
        except Exception as e:
            msg = ("upstream error: %s" % e).encode("utf-8", "replace")
            return self._send(502, msg)


def main():
    ap = argparse.ArgumentParser(description="Local CORS proxy for ttac.ir")
    ap.add_argument("--host", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8765)
    a = ap.parse_args()
    srv = ThreadingHTTPServer((a.host, a.port), Handler)
    srv.daemon_threads = True
    url = "http://%s:%d/ttac?url={url}" % ("127.0.0.1" if a.host in ("0.0.0.0", "") else a.host, a.port)
    print("ttac-proxy running on %s:%d" % (a.host, a.port))
    print("در برنامه این آدرس را در کادر پروکسی بگذارید:")
    print("   " + url)
    print("(Ctrl+C برای توقف)")
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nbye")


if __name__ == "__main__":
    main()
