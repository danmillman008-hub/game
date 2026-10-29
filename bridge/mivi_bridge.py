#!/usr/bin/env python3
"""Mivi Bridge — an OpenAI-compatible Videos/Images API in front of Mivi.

Why: the open-source film studios (Jellyfish, ArcReel, Toonflow, open-higgsfield…)
all talk to providers through the OpenAI shape:

    POST {base_url}/videos        {"prompt", "model", "size", "seconds", "ratio",
                                   "input_reference": {"image_url": "data:image/…;base64,…"}}
    GET  {base_url}/videos/{id}   -> {"status": "...", "url"/"video_url": "..."}

This file implements exactly that and translates to Mivi's real endpoints
(multipleUpload -> beatImage2Video/createNormalTask -> beatImage2Video/queryTask).
Point any of those tools at it with base_url=http://127.0.0.1:8099/v1 and they
will render with Mivi, no code change on their side.

Run:            python3 mivi_bridge.py            (listens on 0.0.0.0:8099)
With options:   MIVI_USER=<userid> PORT=8099 python3 mivi_bridge.py
Stdlib only. No dependencies.
"""
from __future__ import annotations

import base64
import hashlib
import json
import os
import re
import time
import uuid
import urllib.error
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = os.environ.get("MIVI_HOST", "https://cpi.ufotosoft.com")
USER = os.environ.get("MIVI_USER", "7da75eed37c61d33")
CP = os.environ.get("MIVI_CP", "instagram.story.art.collage")
VERSION = os.environ.get("MIVI_VERSION", "407")
PORT = int(os.environ.get("PORT", "8099"))

UPLOAD = "/algo/v1/aiGenerate-aigc/multipleUpload"
CREATE = "/algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask"
QUERY = "/algo/v1/faceFusion/aigc/beatImage2Video/queryTask"

# model name -> (effectType, quality)   quality: 1=360P, 2=720P
MODELS = {
    "mivi-gx-720p": (6209, 2),
    "mivi-gx-360p": (6209, 1),
    "mivi-catwalk": (4991, 2),
    "mivi-neon-couple": (5202, 2),
    "mivi-clone": (7600, 2),
}
DEFAULT_MODEL = "mivi-gx-720p"

TASKS: dict[str, dict] = {}          # id -> {status, url, error, created, model}


def _headers(content_type: str = "application/json", extra: dict | None = None) -> dict:
    t = str(int(time.time()))
    h = {
        "userid": USER, "timeStamp": t, "cp": CP, "version": VERSION,
        "platform": "1", "ifWise": "true", "Content-Type": content_type,
        "sign": hashlib.md5(("m3snil" + t).encode()).hexdigest(),
    }
    if extra:
        h.update(extra)
    return h


def _post_json(path: str, body: dict, timeout: int = 60) -> dict:
    req = urllib.request.Request(HOST + path, data=json.dumps(body).encode(),
                                 headers=_headers(), method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def _upload_bytes(data: bytes, filename: str, ctype: str = "image/jpeg") -> str:
    """multipart upload -> public URL on Mivi's CDN."""
    boundary = uuid.uuid4().hex
    body = b"\r\n".join([
        ("--" + boundary).encode(),
        f'Content-Disposition: form-data; name="files"; filename="{filename}"'.encode(),
        f"Content-Type: {ctype}".encode(),
        b"", data,
        ("--" + boundary + "--").encode(), b"",
    ])
    req = urllib.request.Request(
        HOST + UPLOAD, data=body, method="POST",
        headers=_headers("multipart/form-data; boundary=" + boundary),
    )
    with urllib.request.urlopen(req, timeout=120) as r:
        j = json.loads(r.read().decode())
    if j.get("c") != 200 or not j.get("d"):
        raise RuntimeError(f"upload failed: {j}")
    return j["d"][0]


_DATA_URL = re.compile(r"^data:(image/[a-z+]+);base64,(.+)$", re.S)


def image_to_url(value: str) -> str:
    """Accept a data URL, a bare base64 blob, or an already-public URL."""
    v = (value or "").strip()
    if not v:
        raise RuntimeError("empty image reference")
    m = _DATA_URL.match(v)
    if m:
        ctype, b64 = m.group(1), m.group(2)
        data = base64.b64decode(b64)
        ext = "png" if "png" in ctype else "jpg"
        return _upload_bytes(data, f"ref.{ext}", ctype)
    if v.startswith("http://") or v.startswith("https://"):
        if "ufotosoft.com" in v or "wiseoel.com" in v:
            return v                      # already ours
        with urllib.request.urlopen(urllib.request.Request(v, headers={"User-Agent": "mivi-bridge"}), timeout=60) as r:
            data = r.read()
        return _upload_bytes(data, "ref.jpg")
    # assume bare base64
    return _upload_bytes(base64.b64decode(v), "ref.jpg")


def size_to_quality(size: str | None, model: str) -> int:
    if model in MODELS:
        return MODELS[model][1]
    if size:
        hm = re.search(r"(\d+)\s*[x×]\s*(\d+)", size)
        if hm:
            return 2 if max(int(hm.group(1)), int(hm.group(2))) >= 720 else 1
    return 2


def create_video(body: dict) -> dict:
    model = body.get("model") or DEFAULT_MODEL
    effect, default_quality = MODELS.get(model, MODELS[DEFAULT_MODEL])

    prompt = (body.get("prompt") or "").strip()
    ref = body.get("input_reference") or {}
    if isinstance(ref, dict):
        ref = ref.get("image_url") or ref.get("url") or ""
    if not ref:
        raise RuntimeError("Mivi needs a reference image; send input_reference.image_url")

    img_url = image_to_url(ref)
    quality = size_to_quality(body.get("size"), model) if model not in MODELS else default_quality

    payload = {"imageUrls": [img_url], "level": 1, "effectType": int(effect),
               "prompt": prompt, "quality": int(quality)}
    res = _post_json(CREATE, payload)
    if res.get("c") != 200:
        raise RuntimeError(f"create rejected c={res.get('c')} {res.get('m')}")
    tid = (res.get("d") or {}).get("taskId")
    if not tid:
        raise RuntimeError("no taskId returned")

    TASKS[tid] = {"id": tid, "status": "queued", "url": None, "error": None,
                  "created": time.time(), "model": model, "prompt": prompt,
                  "image": img_url, "quality": quality, "effect": effect}
    return {"id": tid, "object": "video", "status": "queued", "model": model,
            "created_at": int(time.time()), "seconds": str(body.get("seconds") or 4)}


def poll_video(tid: str) -> dict:
    t = TASKS.get(tid)
    if not t:
        # unknown id: ask Mivi anyway (helps if the bridge restarted)
        t = TASKS[tid] = {"id": tid, "status": "queued", "url": None, "error": None,
                          "created": time.time(), "model": DEFAULT_MODEL}
    if t.get("url"):
        return {"id": tid, "object": "video", "status": "completed", "progress": 100,
                "url": t["url"], "video_url": t["url"], "model": t.get("model")}
    try:
        res = _post_json(QUERY, {"taskId": tid})
    except Exception as e:                       # network hiccup: stay pending
        t["error"] = str(e)
        return {"id": tid, "object": "video", "status": "in_progress", "progress": 50}
    d = res.get("d") or {}
    url = d.get("videoUrl")
    status = str(d.get("taskStatus") or "").lower()
    if url:
        t["url"] = url
        return {"id": tid, "object": "video", "status": "completed", "progress": 100,
                "url": url, "video_url": url, "model": t.get("model")}
    if status in ("fail", "failed"):
        t["status"] = "failed"
        return {"id": tid, "object": "video", "status": "failed",
                "error": {"message": d.get("taskReason") or "generation failed"}}
    return {"id": tid, "object": "video", "status": "in_progress", "progress": 50}


class Handler(BaseHTTPRequestHandler):
    server_version = "MiviBridge/1.0"

    def _json(self, code: int, obj: dict):
        raw = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(raw)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Methods", "GET,POST,OPTIONS")
        self.end_headers()
        self.wfile.write(raw)

    def _read(self) -> dict:
        n = int(self.headers.get("Content-Length") or 0)
        if not n:
            return {}
        raw = self.rfile.read(n)
        try:
            return json.loads(raw.decode() or "{}")
        except Exception:
            return {}

    def do_OPTIONS(self):
        self._json(204, {})

    def do_GET(self):
        if self.path.rstrip("/") in ("/health", ""):
            return self._json(200, {"ok": True, "host": HOST, "user": USER, "models": list(MODELS)})
        if self.path.rstrip("/").endswith("/models") or self.path.startswith("/v1/models"):
            return self._json(200, {"object": "list", "data": [
                {"id": k, "object": "model", "owned_by": "mivi"} for k in MODELS]})
        m = re.match(r"^/v1/videos/([^/?]+)", self.path)
        if m:
            return self._json(200, poll_video(urllib.parse.unquote(m.group(1))))
        return self._json(404, {"error": {"message": f"no route {self.path}"}})

    def do_POST(self):
        body = self._read()
        if self.path.startswith("/v1/videos"):
            try:
                return self._json(200, create_video(body))
            except Exception as e:
                return self._json(400, {"error": {"message": str(e), "type": "mivi_error"}})
        if self.path.startswith("/v1/images/generations"):
            return self._json(501, {"error": {"message":
                "image generation is not wired yet — Mivi's image engines are "
                "stitchImage (2 refs + prompt) and createSuperResolutionNew"}})
        return self._json(404, {"error": {"message": f"no route {self.path}"}})

    def log_message(self, fmt, *args):
        print("[bridge]", fmt % args, flush=True)


if __name__ == "__main__":
    print(f"Mivi bridge on http://0.0.0.0:{PORT}/v1  ->  {HOST} (user {USER})", flush=True)
    ThreadingHTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
