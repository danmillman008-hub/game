#!/usr/bin/env python3
"""Mivi MCP server — generation + editing tools for any MCP client.

Generation tools call Mivi (via the same signed HTTP layer as bridge/mivi_bridge.py).
Editing tools call local ffmpeg. Nothing else. Stdlib only.

Register it with Claude Code / Cursor / Codex:

    {
      "mcpServers": {
        "mivi-film": { "command": "python3", "args": ["/abs/path/bridge/mivi_mcp.py"] }
      }
    }

Then an agent can: upload a still -> animate it -> take the last frame -> animate
that -> concatenate -> burn subtitles, i.e. build a film from a screenplay.
"""
from __future__ import annotations

import base64
import filecmp
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import uuid

HOST = os.environ.get("MIVI_HOST", "https://cpi.ufotosoft.com")
USER = os.environ.get("MIVI_USER", "7da75eed37c61d33")
CP = os.environ.get("MIVI_CP", "instagram.story.art.collage")
VERSION = os.environ.get("MIVI_VERSION", "407")
def _which(name: str, env_key: str) -> str:
    v = os.environ.get(env_key) or shutil.which(name)
    if v:
        return v
    try:                              # imageio-ffmpeg ships a static binary, no ffprobe
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        return name


FFMPEG = _which("ffmpeg", "FFMPEG")
FFPROBE = _which("ffprobe", "FFPROBE")

UPLOAD = "/algo/v1/aiGenerate-aigc/multipleUpload"
CREATE = "/algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask"
QUERY = "/algo/v1/faceFusion/aigc/beatImage2Video/queryTask"
STITCH_CREATE = "/algo/v1/faceFusion/aigc/stitchImage/createTask"
STITCH_QUERY = "/algo/v1/faceFusion/aigc/stitchImage/queryTask"
SUPERRES = "/algo/v1/faceFusion/aigc/createSuperResolutionNew"
SWAPFACE = "/algo/v1/faceFusion/aigc/createSwapFace"
MASKS = "/algo/v1/faceFusion/aigc/createInpaintAnything"

VIDEO_MODELS = {
    "mivi-gx-720p": (6209, 2),
    "mivi-gx-360p": (6209, 1),
    "mivi-catwalk": (4991, 2),
    "mivi-neon-couple": (5202, 2),
    "mivi-clone": (7600, 2),
}


# --------------------------------------------------------------------------- http
def _headers(ctype="application/json"):
    t = str(int(time.time()))
    return {
        "userid": USER, "timeStamp": t, "cp": CP, "version": VERSION,
        "platform": "1", "ifWise": "true", "Content-Type": ctype,
        "sign": hashlib.md5(("m3snil" + t).encode()).hexdigest(),
    }


def _post(path, body, timeout=90):
    req = urllib.request.Request(HOST + path, data=json.dumps(body).encode(),
                                 headers=_headers(), method="POST")
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def _upload(data: bytes, name="ref.jpg", ctype="image/jpeg"):
    b = uuid.uuid4().hex
    body = b"\r\n".join([
        ("--" + b).encode(),
        f'Content-Disposition: form-data; name="files"; filename="{name}"'.encode(),
        f"Content-Type: {ctype}".encode(),
        b"", data, ("--" + b + "--").encode(), b"",
    ])
    req = urllib.request.Request(HOST + UPLOAD, data=body, method="POST",
                                 headers=_headers("multipart/form-data; boundary=" + b))
    with urllib.request.urlopen(req, timeout=180) as r:
        j = json.loads(r.read().decode())
    if j.get("c") != 200 or not j.get("d"):
        raise RuntimeError(f"upload failed: {j}")
    return j["d"][0]


_DATA = re.compile(r"^data:(image/[a-z+]+);base64,(.+)$", re.S)


def as_url(value: str) -> str:
    """local path | http URL | data URL | bare base64  ->  Mivi CDN URL"""
    v = (value or "").strip()
    if not v:
        raise ValueError("empty image reference")
    m = _DATA.match(v)
    if m:
        return _upload(base64.b64decode(m.group(2)), "ref.png" if "png" in m.group(1) else "ref.jpg",
                       m.group(1))
    if v.startswith(("http://", "https://")):
        if "ufotosoft.com" in v or "wiseoel.com" in v:
            return v
        with urllib.request.urlopen(urllib.request.Request(v, headers={"User-Agent": "mivi-mcp"}),
                                    timeout=120) as r:
            return _upload(r.read(), os.path.basename(urllib.parse.urlparse(v).path) or "ref.jpg")
    if os.path.exists(v):
        with open(v, "rb") as f:
            data = f.read()
        ext = os.path.splitext(v)[1].lower().lstrip(".") or "jpg"
        return _upload(data, f"ref.{ext}", "image/png" if ext == "png" else "image/jpeg")
    return _upload(base64.b64decode(v), "ref.jpg")


def download(url: str, path: str) -> str:
    os.makedirs(os.path.dirname(os.path.abspath(path)) or ".", exist_ok=True)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=300) as r, open(path, "wb") as f:
        shutil.copyfileobj(r, f)
    return path


def _run(args, timeout=600):
    p = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    if p.returncode != 0:
        raise RuntimeError((p.stderr or p.stdout or "command failed")[-800:])
    return p.stdout


# --------------------------------------------------------------------------- tools
def t_upload(a):
    return {"url": as_url(a["image"]), "note": "public Mivi CDN url"}


def t_video(a):
    model = a.get("model") or "mivi-gx-720p"
    effect, quality = VIDEO_MODELS.get(model, VIDEO_MODELS["mivi-gx-720p"])
    if "quality" in a:
        quality = int(a["quality"])
    # `images` (plural) is a probe, not a promise: the endpoint takes an array, so a
    # second entry may mean first/last-frame. Nothing in the app code says so.
    imgs = a.get("images") or [a["image"]]
    body = {"imageUrls": [as_url(x) for x in imgs], "level": 1, "effectType": effect,
            "prompt": a.get("prompt") or "", "quality": int(quality)}
    r = _post(CREATE, body)
    if r.get("c") != 200:
        raise RuntimeError(f"create rejected: c={r.get('c')} {r.get('m')}")
    d = r.get("d") or {}
    return {"task_id": d.get("taskId"), "model": model, "effect_type": effect,
            "quality": quality, "cost_hint": "1 render credit"}


def t_video_status(a):
    r = _post(QUERY, {"taskId": a["task_id"]})
    d = r.get("d") or {}
    return {"c": r.get("c"), "status": d.get("taskStatus"), "video_url": d.get("videoUrl"),
            "reason": d.get("taskReason")}


def t_video_wait(a):
    tid = a["task_id"]
    deadline = time.time() + float(a.get("timeout_s", 420))
    last = {}
    while time.time() < deadline:
        last = t_video_status({"task_id": tid})
        if last.get("video_url"):
            out = a.get("out")
            if out:
                download(last["video_url"], out)
                last["saved"] = os.path.abspath(out)
            return last
        if str(last.get("status") or "").lower() in ("fail", "failed"):
            return last
        time.sleep(float(a.get("interval_s", 6)))
    last["timeout"] = True
    return last


def t_compose(a):
    imgs = [as_url(x) for x in a["images"]]
    if len(imgs) < 2:
        raise ValueError("Mivi's composer needs at least 2 images")
    body = {"imageUrls": imgs, "level": 1}
    if a.get("prompt"):
        body["prompt"] = a["prompt"]
    r = _post(STITCH_CREATE, body)
    if r.get("c") != 200:
        raise RuntimeError(f"compose rejected: c={r.get('c')} {r.get('m')}")
    tid = (r.get("d") or {}).get("taskId")
    deadline = time.time() + float(a.get("timeout_s", 420))
    while time.time() < deadline:
        q = _post(STITCH_QUERY, {"taskId": tid})
        d = q.get("d") or {}
        # the composer reports its output in `responseUrl`; older paths used imageUrl/url
        url = (d.get("responseUrl") or d.get("imageUrl") or d.get("url")
               or (d.get("urlList") or [None])[0])
        if url:
            out = {"task_id": tid, "image_url": url}
            if a.get("out"):
                download(url, a["out"]); out["saved"] = os.path.abspath(a["out"])
            return out
        if str(d.get("taskStatus") or "").lower() in ("fail", "failed"):
            return {"task_id": tid, "failed": d.get("taskReason")}
        time.sleep(8)
    return {"task_id": tid, "timeout": True}


def t_upscale(a):
    r = _post(SUPERRES, {"imageUrls": [as_url(a["image"])], "level": 1})
    return {"c": r.get("c"), "result": r.get("d"), "message": r.get("m")}


def t_swapface(a):
    r = _post(SWAPFACE, {"imageUrls": [as_url(a["image"])],
                         "templateIds": [int(a.get("template_id", 1001))], "level": 1})
    return {"c": r.get("c"), "result": r.get("d"), "message": r.get("m")}


def t_masks(a):
    r = _post(MASKS, {"imageUrls": [as_url(a["image"])], "level": 1})
    return {"c": r.get("c"), "masks": r.get("d")}


def t_last_frame(a):
    out = a["out"]
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    _run([FFMPEG, "-y", "-v", "error", "-sseof", "-0.4", "-i", a["video"],
          "-update", "1", "-frames:v", "1", out])
    return {"saved": os.path.abspath(out)}


def t_concat(a):
    clips = a["clips"]
    out = a["out"]
    xf = float(a.get("crossfade_s", 0) or 0)
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    if xf <= 0:
        lst = out + ".txt"
        with open(lst, "w", encoding="utf-8") as f:
            for c in clips:
                f.write(f"file '{os.path.abspath(c)}'\n")
        _run([FFMPEG, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst,
              "-c", "copy", out])
        os.remove(lst)
        return {"saved": os.path.abspath(out), "mode": "concat"}

    # xfade chain
    args = [FFMPEG, "-y", "-v", "error"]
    for c in clips:
        args += ["-i", c]
    durs = [float(_run([FFPROBE, "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", c]).strip() or 0) for c in clips]
    fc, prev, acc = [], "[0:v]", durs[0]
    for i in range(1, len(clips)):
        lbl = f"[v{i}]"
        off = max(acc - xf, 0)
        fc.append(f"{prev}[{i}:v]xfade=transition=fade:duration={xf}:offset={off:.3f}{lbl}")
        prev, acc = lbl, acc + durs[i] - xf
    args += ["-filter_complex", ";".join(fc), "-map", prev, "-c:v", "libx264",
             "-crf", str(int(a.get("crf", 18))), "-pix_fmt", "yuv420p",
             "-movflags", "+faststart", out]
    _run(args)
    return {"saved": os.path.abspath(out), "mode": "xfade", "duration_s": round(acc, 2)}


def t_subtitle(a):
    out = a["out"]
    srt = a["srt"]
    style = a.get("style") or "Fontsize=20,PrimaryColour=&H00FFFFFF,Outline=1,Shadow=0"
    _run([FFMPEG, "-y", "-v", "error", "-i", a["video"],
          "-vf", f"subtitles={srt}:force_style='{style}'",
          "-c:a", "copy", out])
    return {"saved": os.path.abspath(out)}


def t_probe(a):
    out = _run([FFPROBE, "-v", "error", "-print_format", "json",
                "-show_format", "-show_streams", a["path"]])
    j = json.loads(out)
    v = next((s for s in j.get("streams", []) if s.get("codec_type") == "video"), {})
    return {"width": v.get("width"), "height": v.get("height"),
            "fps": v.get("r_frame_rate"),
            "duration_s": float(j.get("format", {}).get("duration") or 0),
            "bytes": int(j.get("format", {}).get("size") or 0)}


TOOLS = [
    ("mivi_upload", "Upload a local image (or re-host a URL) and get a Mivi CDN URL.",
     {"image": {"type": "string", "description": "local path, http URL, data URL or base64"}},
     ["image"]),
    ("mivi_video", "Animate one still into a ~4.03 s clip with a prompt. Returns a task id.",
     {"image": {"type": "string"}, "prompt": {"type": "string"},
      "model": {"type": "string", "enum": list(VIDEO_MODELS)},
      "quality": {"type": "integer", "enum": [1, 2], "description": "1=360P 2=720P"}},
     ["image"]),
    ("mivi_video_status", "One poll of a clip task.",
     {"task_id": {"type": "string"}}, ["task_id"]),
    ("mivi_video_wait", "Poll until the clip is ready (or timeout) and optionally download it.",
     {"task_id": {"type": "string"}, "out": {"type": "string"},
      "timeout_s": {"type": "number"}, "interval_s": {"type": "number"}}, ["task_id"]),
    ("mivi_compose", "Image + image + prompt -> one new image (Mivi's composer). Needs >=2 images.",
     {"images": {"type": "array", "items": {"type": "string"}, "minItems": 2},
      "prompt": {"type": "string"}, "out": {"type": "string"}}, ["images"]),
    ("mivi_upscale", "2x super resolution on an image.",
     {"image": {"type": "string"}}, ["image"]),
    ("mivi_swapface", "Swap a face in an image using a template id (1000-1010, 1100, 1200, 2001, 2002).",
     {"image": {"type": "string"}, "template_id": {"type": "integer"}}, ["image"]),
    ("mivi_masks", "Segment an image into 7 labelled masks.",
     {"image": {"type": "string"}}, ["image"]),
    ("film_last_frame", "Extract the last frame of a clip (for chaining shots).",
     {"video": {"type": "string"}, "out": {"type": "string"}}, ["video", "out"]),
    ("film_concat", "Join clips into one file, optional crossfade between them.",
     {"clips": {"type": "array", "items": {"type": "string"}},
      "out": {"type": "string"}, "crossfade_s": {"type": "number"},
      "crf": {"type": "integer"}}, ["clips", "out"]),
    ("film_subtitle", "Burn an SRT into a video.",
     {"video": {"type": "string"}, "srt": {"type": "string"}, "out": {"type": "string"},
      "style": {"type": "string"}}, ["video", "srt", "out"]),
    ("film_probe", "Inspect a media file (size, duration, fps).",
     {"path": {"type": "string"}}, ["path"]),
]
HANDLERS = {
    "mivi_upload": t_upload, "mivi_video": t_video, "mivi_video_status": t_video_status,
    "mivi_video_wait": t_video_wait, "mivi_compose": t_compose, "mivi_upscale": t_upscale,
    "mivi_swapface": t_swapface, "mivi_masks": t_masks, "film_last_frame": t_last_frame,
    "film_concat": t_concat, "film_subtitle": t_subtitle, "film_probe": t_probe,
}


# --------------------------------------------------------------------------- mcp
def tool_list():
    return [{"name": n, "description": d,
             "inputSchema": {"type": "object", "properties": p,
                             "required": r, "additionalProperties": False}}
            for n, d, p, r in TOOLS]


def handle(msg):
    method = msg.get("method")
    mid = msg.get("id")
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": mid, "result": {
            "protocolVersion": "2024-11-05",
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": "mivi-film", "version": "1.0.0"}}}
    if method in ("notifications/initialized", "initialized"):
        return None
    if method == "ping":
        return {"jsonrpc": "2.0", "id": mid, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": mid, "result": {"tools": tool_list()}}
    if method == "tools/call":
        p = msg.get("params") or {}
        name, args = p.get("name"), (p.get("arguments") or {})
        fn = HANDLERS.get(name)
        if not fn:
            return {"jsonrpc": "2.0", "id": mid,
                    "error": {"code": -32601, "message": f"unknown tool {name}"}}
        try:
            out = fn(args)
            return {"jsonrpc": "2.0", "id": mid, "result": {
                "content": [{"type": "text", "text": json.dumps(out, ensure_ascii=False)}],
                "isError": False}}
        except Exception as e:
            return {"jsonrpc": "2.0", "id": mid, "result": {
                "content": [{"type": "text", "text": f"{type(e).__name__}: {e}"}],
                "isError": True}}
    return {"jsonrpc": "2.0", "id": mid,
            "error": {"code": -32601, "message": f"no method {method}"}}


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except Exception:
            continue
        resp = handle(msg)
        if resp is not None:
            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
