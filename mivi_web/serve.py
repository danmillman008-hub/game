#!/usr/bin/env python3
"""
serve.py — سرور محلی برای اپ وب Mivi (mivi_app.html)

چرا لازم است؟
  مرورگرها درخواست مستقیم به face-api.ufotosoft.com را به‌خاطر CORS بلاک می‌کنند.
  این اسکریپت فقط دو کار می‌کند:
    ۱) فایل mivi_app.html را روی http://localhost:8770 سرو می‌کند
    ۲) درخواستهای /proxy?u=<url> را به سرور مقصد فوروارد و پاسخ را برمی‌گرداند
       (با هدر Access-Control-Allow-Origin: *)

اجرا (بدون نیاز به pip):
    python3 serve.py
سپس مرورگر:  http://localhost:8770
"""
import os
import sys
import urllib.request
import urllib.error
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

PORT = int(os.environ.get("MIVI_PORT", "8770"))
HERE = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(HERE, "mivi_app.html")

# فقط مقصدهای مجاز برای پروکسی (جلوگیری از باز شدن پروکسی عمومی)
ALLOWED_SUFFIXES = (
    "ufotosoft.com",
    "videomate.cc",
)

HOP_BY_HOP = {
    "connection", "keep-alive", "proxy-authenticate", "proxy-authorization",
    "te", "trailers", "transfer-encoding", "upgrade", "host",
    "content-length", "content-encoding",
}


class Handler(BaseHTTPRequestHandler):
    server_version = "MiviLocal/1.0"

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path in ("/", "/mivi_app.html"):
            try:
                with open(HTML_FILE, "rb") as fh:
                    data = fh.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(data)))
                self.end_headers()
                self.wfile.write(data)
            except FileNotFoundError:
                self.send_error(404, "mivi_app.html not found next to serve.py")
            return
        if parsed.path == "/proxy":
            self._proxy("GET")
            return
        self.send_error(404)

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == "/proxy":
            self._proxy("POST")
            return
        self.send_error(404)

    def _proxy(self, method):
        qs = parse_qs(urlparse(self.path).query)
        target = qs.get("u", [""])[0]
        if not target:
            self.send_error(400, "missing u=")
            return
        host = urlparse(target).netloc.lower().split("@")[-1]
        host_no_port = host.split(":")[0]  # پورت در مقایسه دخیل نباشد
        if not any(host_no_port == s or host_no_port.endswith("." + s)
                   for s in ALLOWED_SUFFIXES):
            self.send_error(403, f"proxy target not allowed: {host}")
            return

        length = int(self.headers.get("Content-Length", 0) or 0)
        body = self.rfile.read(length) if length else None

        fwd_headers = {
            k: v for k, v in self.headers.items()
            if k.lower() not in HOP_BY_HOP
        }
        req = urllib.request.Request(target, data=body, headers=fwd_headers,
                                     method=method)
        try:
            with urllib.request.urlopen(req, timeout=180) as up:
                payload = up.read()
                self.send_response(up.status)
                self._cors()
                ctype = up.headers.get("Content-Type", "application/octet-stream")
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(payload)))
                self.end_headers()
                self.wfile.write(payload)
        except urllib.error.HTTPError as e:
            payload = e.read()
            self.send_response(e.code)
            self._cors()
            self.send_header("Content-Type",
                             e.headers.get("Content-Type", "text/plain"))
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
        except Exception as e:  # noqa: BLE001
            msg = f"proxy error: {e}".encode()
            self.send_response(502)
            self._cors()
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(msg)))
            self.end_headers()
            self.wfile.write(msg)

    def log_message(self, fmt, *args):
        sys.stderr.write("[serve] " + fmt % args + "\n")


def main():
    if not os.path.exists(HTML_FILE):
        sys.exit("mivi_app.html کنار serve.py پیدا نشد.")
    httpd = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Mivi web app:  http://localhost:{PORT}")
    print("Ctrl+C برای توقف")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nمتوقف شد.")


if __name__ == "__main__":
    main()
