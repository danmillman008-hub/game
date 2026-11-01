#!/usr/bin/env python3
"""Mimo preview host — one port, three engines.

    /            → the Mimo shell (this repo, mimo/shell)
    /learn/*     → the offline learning engine modules (mimo/learn)
    /content/*   → content packs (mimo/content)
    /practice/*  → the EPM application (FastAPI, default 127.0.0.1:8765), prefix stripped
    /max/*       → the LearnHarness application (Next.js, default 127.0.0.1:3000), prefix kept (basePath=/max)

Why a reverse proxy instead of three browser tabs: the preview environment exposes a single port, and same-origin
embedding keeps cookies, assets and routing working without weakening either engine.

The proxy is deliberately thin. It does four things:
  1. forwards the request (no body buffering tricks, no rewriting of API payloads);
  2. drops `X-Frame-Options` and restrictive `frame-ancestors` so the shell may embed the engine;
  3. injects the Persian localization layer (`/__overlay/fa.js`) into engine HTML;
  4. leaves everything else byte-identical.

stdlib only.
"""
from __future__ import annotations

import argparse
import http.client
import json
import mimetypes
import os
import socket
import sys
import threading
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # …/mimo
SHELL_DIR = ROOT / "shell"
OVERLAY_DIR = ROOT / "host" / "overlay"

DEFAULTS = {
    "epm": os.environ.get("EPM_URL", "http://127.0.0.1:8765"),
    "max": os.environ.get("LH_URL", "http://127.0.0.1:3000"),
}

HOP_BY_HOP = {
    "connection", "keep-alive", "proxy-authenticate", "proxy-authorization", "te", "trailers",
    "transfer-encoding", "upgrade", "host", "content-length", "accept-encoding",
}

MIME = {
    ".js": "text/javascript; charset=utf-8",
    ".mjs": "text/javascript; charset=utf-8",
    ".css": "text/css; charset=utf-8",
    ".html": "text/html; charset=utf-8",
    ".json": "application/json; charset=utf-8",
    ".svg": "image/svg+xml",
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".woff2": "font/woff2",
    ".ico": "image/x-icon",
    ".md": "text/markdown; charset=utf-8",
    ".ebnf": "text/plain; charset=utf-8",
}


def engine_up(base: str, path: str = "/", timeout: float = 1.2) -> bool:
    try:
        req = urllib.request.Request(base + path, method="GET")
        with urllib.request.urlopen(req, timeout=timeout) as res:  # noqa: S310 - localhost only
            return res.status < 500
    except Exception:  # noqa: BLE001
        return False


class Handler(BaseHTTPRequestHandler):
    server_version = "MimoPreview/0.1"
    protocol_version = "HTTP/1.1"

    # ---------- logging ----------
    def log_message(self, fmt, *args):  # keep the console readable
        if os.environ.get("PREVIEW_VERBOSE"):
            sys.stderr.write("%s - %s\n" % (self.address_string(), fmt % args))

    # ---------- verbs ----------
    def do_GET(self):  # noqa: N802
        self.route("GET")

    def do_HEAD(self):  # noqa: N802
        self.route("HEAD")

    def do_POST(self):  # noqa: N802
        self.route("POST")

    def do_PUT(self):  # noqa: N802
        self.route("PUT")

    def do_PATCH(self):  # noqa: N802
        self.route("PATCH")

    def do_DELETE(self):  # noqa: N802
        self.route("DELETE")

    def do_OPTIONS(self):  # noqa: N802
        self.route("OPTIONS")

    # ---------- dispatch ----------
    def route(self, method: str) -> None:
        path = self.path.split("?", 1)[0]
        if path == "/api/preview/i18n-missing" and method == "POST":
            return self.collect_i18n_missing()
        if path.startswith("/api/preview/"):
            return self.preview_api(path)
        if path.startswith("/__overlay/"):
            return self.serve_overlay(path[len("/__overlay/"):])
        if path == "/practice":
            return self.redirect("/practice/")
        if path.startswith("/practice/"):
            return self.proxy("epm", method)
        if path == "/max" or path.startswith("/max/"):
            # LearnHarness (Next.js basePath=/max) canonicalises /max/ → /max, so both forms go straight through.
            return self.proxy("max", method)
        return self.serve_static(path, method)

    # ---------- own endpoints ----------
    def preview_api(self, path: str) -> None:
        if path == "/api/preview/status":
            payload = {
                "ok": True,
                "engines": {
                    "learn": {"ok": True, "kind": "builtin", "storage": "localStorage"},
                    "practice": {"ok": engine_up(DEFAULTS["epm"], "/api/health"), "url": DEFAULTS["epm"], "product": "EPM"},
                    "max": {"ok": engine_up(DEFAULTS["max"], "/max/"), "url": DEFAULTS["max"], "product": "LearnHarness"},
                },
                "content": sorted(p.name for p in (ROOT / "content").iterdir() if p.is_dir()) if (ROOT / "content").exists() else [],
            }
            self.send_json(payload)
            return
        self.send_json({"ok": False, "error": "unknown preview endpoint"}, status=404)

    def collect_i18n_missing(self) -> None:
        """The localization layer reports untranslated strings here; they become mimo/docs/i18n-missing.json."""
        length = int(self.headers.get("Content-Length") or 0)
        try:
            payload = json.loads(self.rfile.read(length) or b"{}")
        except json.JSONDecodeError:
            return self.send_json({"ok": False, "error": "invalid json"}, status=400)
        target = ROOT / "docs" / "i18n-missing.json"
        target.parent.mkdir(parents=True, exist_ok=True)
        data = {"generated": None, "engines": {}}
        if target.exists():
            try:
                data = json.loads(target.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                pass
        engine = payload.get("engine", "unknown")
        bucket = data.setdefault("engines", {}).setdefault(engine, {"counts": {}, "routes": {}})
        for item in payload.get("missing", []):
            text = item.get("text")
            if not text:
                continue
            bucket["counts"][text] = bucket["counts"].get(text, 0) + int(item.get("count") or 1)
        route = payload.get("route", "")
        if route:
            bucket["routes"][route] = sorted({i.get("text") for i in payload.get("missing", []) if i.get("text")})
        from datetime import datetime, timezone
        data["generated"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        data["note"] = "Untranslated UI strings observed by the Persian localization layer (mimo/host/overlay/fa.js)."
        target.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        self.send_json({"ok": True, "stored": len(payload.get("missing", []))})

    def send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if self.command != "HEAD":
            self.wfile.write(body)

    def redirect(self, target: str) -> None:
        self.send_response(308)
        self.send_header("Location", target)
        self.send_header("Content-Length", "0")
        self.end_headers()

    # ---------- static ----------
    def serve_static(self, path: str, method: str) -> None:
        rel = path.lstrip("/")
        if rel in ("", "index.html"):
            file = SHELL_DIR / "index.html"
            rel = "shell/index.html"
        else:
            file = (ROOT / rel).resolve()
        try:
            file.relative_to(ROOT.resolve())
        except ValueError:
            return self.send_error(403, "outside the preview root")
        if not file.exists() or not file.is_file():
            name = Path(rel).name
            if "." in name:
                # the shell is served at "/", so its relative assets arrive as /app.js and /styles.css.
                # Fall back to the shell directory before giving up.
                candidate = (SHELL_DIR / name).resolve()
                if candidate.is_file():
                    file = candidate
                else:
                    return self.send_error(404, "not found")
            else:
                # client-side routes of the shell (e.g. /learn) fall back to the app shell
                file = SHELL_DIR / "index.html"
        data = file.read_bytes()
        ctype = MIME.get(file.suffix.lower()) or mimetypes.guess_type(str(file))[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if method != "HEAD":
            self.wfile.write(data)

    def serve_overlay(self, name: str) -> None:
        file = (OVERLAY_DIR / name).resolve()
        try:
            file.relative_to(OVERLAY_DIR.resolve())
        except ValueError:
            return self.send_error(403, "outside the overlay dir")
        if not file.is_file():
            return self.send_error(404, "overlay not found")
        data = file.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", MIME.get(file.suffix, "text/javascript; charset=utf-8"))
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(data)

    # ---------- proxy ----------
    def proxy(self, engine: str, method: str) -> None:
        base = DEFAULTS[engine]
        raw = self.path
        if engine == "max":
            # /max/ → /max (upstream redirects the trailing-slash form), everything else passes through
            upstream_path = "/max" if raw in ("/max", "/max/") else raw
        else:
            upstream_path = raw[len("/practice"):] or "/"
        if not upstream_path.startswith("/"):
            upstream_path = "/" + upstream_path
        host, port = _split(base)

        length = int(self.headers.get("Content-Length") or 0)
        body = self.rfile.read(length) if length else None

        headers = {k: v for k, v in self.headers.items() if k.lower() not in HOP_BY_HOP}
        headers["Accept-Encoding"] = "identity"
        conn = http.client.HTTPConnection(host, port, timeout=60)
        try:
            conn.request(method, upstream_path, body=body, headers=headers)
            res = conn.getresponse()
            payload = res.read()
            status = res.status
            out_headers = [(k, v) for k, v in res.getheaders() if k.lower() not in {
                "x-frame-options", "content-security-policy", "content-encoding", "content-length", "connection",
                "transfer-encoding", "keep-alive",
            }]
        except (ConnectionRefusedError, socket.timeout, OSError):
            if engine == "epm":
                return self.send_error(502, "EPM is not running on %s" % base)
            return self.send_error(502, "LearnHarness is not running on %s" % base)
        finally:
            try:
                conn.close()
            except Exception:  # noqa: BLE001
                pass

        ctype = dict((k.lower(), v) for k, v in out_headers).get("content-type", "")
        if "text/html" in ctype:
            payload = _inject_overlay(payload)

        self.send_response(status)
        for key, value in out_headers:
            self.send_header(key, value)
        self.send_header("Content-Security-Policy", "frame-ancestors 'self'")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        if method != "HEAD":
            self.wfile.write(payload)


def _inject_overlay(html_bytes: bytes) -> bytes:
    try:
        html = html_bytes.decode("utf-8")
    except UnicodeDecodeError:
        return html_bytes
    tag = '<script src="/__overlay/fa.js" defer></script>'
    if tag in html:
        return html_bytes
    lower = html.lower()
    idx = lower.rfind("</body>")
    if idx == -1:
        return (html + tag).encode("utf-8")
    return (html[:idx] + tag + html[idx:]).encode("utf-8")


def _split(url: str) -> tuple[str, int]:
    rest = url.split("://", 1)[1] if "://" in url else url
    hostport = rest.split("/", 1)[0]
    if ":" in hostport:
        host, port = hostport.rsplit(":", 1)
        return host, int(port)
    return hostport, 80


def main() -> int:
    ap = argparse.ArgumentParser(description="Mimo preview host")
    ap.add_argument("--host", default=os.environ.get("PREVIEW_HOST", "0.0.0.0"))
    ap.add_argument("--port", type=int, default=int(os.environ.get("PREVIEW_PORT", "4000")))
    args = ap.parse_args()

    httpd = ThreadingHTTPServer((args.host, args.port), Handler)
    httpd.daemon_threads = True
    print(f"Mimo preview host → http://localhost:{args.port}")
    print(f"  learn      : built in ({SHELL_DIR})")
    print(f"  practice   : {DEFAULTS['epm']}  ({'up' if engine_up(DEFAULTS['epm'], '/api/health') else 'not running'})")
    print(f"  max        : {DEFAULTS['max']}  ({'up' if engine_up(DEFAULTS['max'], '/max/') else 'not running'})")
    print("  Ctrl+C to stop")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nstopped")
    finally:
        httpd.server_close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
