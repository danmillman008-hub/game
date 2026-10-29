"""Field discovery, round 2 — the server doubles the field name in its messages
(`imageUrlsimageUrls不能为空`), so instead of regexing a name we scan the message
for known field names and add whichever is missing.

Also tries the two upload endpoints that hand out `imageKey` / `audioKey`, since
emoVideoCreate asks for exactly those.
"""
import json, hashlib, time, urllib.request, urllib.error, pathlib, re, uuid

HOST = "https://cpi.ufotosoft.com"
CP = "instagram.story.art.collage"; USER = "7da75eed37c61d33"
IMG = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
IMG2 = "http://algo.ufotosoft.com/original/261029/56061a5f-6fed-4807-904e-aa42782de3df.jpeg"
OUT = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); OUT.append(s)

def hdr(extra=None):
    t = str(int(time.time()))
    h = {"userid": USER, "timeStamp": t, "cp": CP, "version": "407", "platform": "1",
         "ifWise": "true", "Content-Type": "application/json",
         "sign": hashlib.md5(("m3snil" + t).encode()).hexdigest()}
    if extra: h.update(extra)
    return h

def call(path, body):
    req = urllib.request.Request(HOST + path, data=json.dumps(body).encode(), headers=hdr(), method="POST")
    try:
        with urllib.request.urlopen(req, timeout=45) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try: return {"_http": e.code, **json.loads(e.read().decode())}
        except Exception: return {"_http": e.code}
    except Exception as e: return {"_err": repr(e)[:100]}

def upload(path, url):
    data = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=90).read()
    b = uuid.uuid4().hex
    parts = [("--" + b).encode(), b'Content-Disposition: form-data; name="files"; filename="a.jpg"',
             b"Content-Type: image/jpeg", b"", data, ("--" + b + "--").encode(), b""]
    raw = b"\r\n".join(parts)
    h = hdr({"Content-Type": "multipart/form-data; boundary=" + b})
    h.pop("sign"); t = h["timeStamp"]
    h["sign"] = hashlib.md5(("m3snil" + t).encode()).hexdigest()
    req = urllib.request.Request(HOST + path, data=raw, headers=h, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try: return {"_http": e.code, **json.loads(e.read().decode())}
        except Exception: return {"_http": e.code}
    except Exception as e: return {"_err": repr(e)[:100]}

FIELDS = ["imageUrls", "maskUrls", "templateIds", "images", "imageKey", "audioKey", "modelId",
          "poseSequenceId", "effectType", "prompt", "level", "deviceToken", "token", "styleId",
          "ratio", "duration", "quality", "ifTest", "pixVerseId", "googleId", "videoUrl",
          "fileMd5", "fileSize", "fileTime", "width", "height", "jobId", "taskId", "imageEffectType"]

def missing(msg):
    low = msg
    hits = []
    for f in FIELDS:
        if (f + f) in low or (f in low and ("不能为空" in low or "not empty" in low or "not null" in low)):
            hits.append(f)
    return hits

def guess(f):
    if f.endswith("Urls") or f in ("images", "templateIds"):
        return [IMG, IMG2] if f in ("images", "templateIds") else [IMG]
    if f in ("imageKey", "audioKey", "imageUrl"):
        return IMG
    if f in ("level", "quality", "duration", "styleId", "modelId", "ratio", "width", "height"): return 1
    if f == "prompt": return "same person, golden hour light"
    if f == "ifTest": return False
    if f in ("deviceToken", "token"): return ""
    return "0"

BASE = {"imageUrls": [IMG], "level": 1, "deviceToken": "", "ifTest": False}

TARGETS = [
    ("inpaintAnything", "/algo/v1/faceFusion/aigc/createInpaintAnything", dict(BASE)),
    ("inpaintCleaner", "/algo/v1/faceFusion/aigc/createInpaintCleaner",
     {"imageUrls": [IMG], "maskUrls": [IMG2], "level": 1, "deviceToken": "", "ifTest": False}),
    ("swapFace", "/algo/v1/faceFusion/aigc/createSwapFace", dict(BASE)),
    ("faceKey", "/algo/v1/faceFusion/aigc/createFaceKeyTask", {"images": [IMG], "level": 1, "deviceToken": "", "ifTest": False}),
    ("stitch", "/algo/v1/faceFusion/aigc/stitchImage/createTask",
     {"imageUrls": [IMG, IMG2], "level": 1, "deviceToken": "", "ifTest": False}),
    ("livePortrait", "/algo/v1/faceFusion/aigc/livePortraitCreate",
     {"imageUrls": [IMG], "level": 1, "deviceToken": "", "ifTest": False}),
    ("image2image", "/algo/v1/faceFusion/aigc/image2image/createImageTask",
     {"imageUrls": [IMG], "prompt": "same person, golden hour light"}),
]

# ---- the two upload endpoints that may hand out keys
for up in ["/algo/v1/faceAnimation/multipleUpload", "/algo/v1/faceFusion/aigc/image2VideoCustomer/upload"]:
    r = upload(up, IMG)
    p(f"[upload {up.rsplit('/',1)[-1]}] {json.dumps(r, ensure_ascii=False)[:220]}")

for name, path, body in TARGETS:
    seen = []
    r = {}
    for rnd in range(8):
        r = call(path, body)
        c = r.get("c") or r.get("_http"); m = str(r.get("m") or "")
        seen.append((rnd, c, m[:80]))
        if c == 200: break
        miss = [f for f in missing(m) if f not in body]
        if miss:
            for f in miss: body[f] = guess(f)
            continue
        if c == 500:
            for f in ("prompt", "token", "ratio", "quality"):
                body.setdefault(f, guess(f))
            break
        break
    d = r.get("d")
    p(f"## {name}: c={r.get('c') or r.get('_http')} {str(r.get('m'))[:80]}")
    for x in seen[-2:]: p(f"   r{x[0]} c={x[1]} {x[2]}")
    p("   body:", json.dumps(body, ensure_ascii=False)[:300])
    if isinstance(d, dict): p("   d:", json.dumps(d, ensure_ascii=False)[:200])

pathlib.Path("probe_out").mkdir(exist_ok=True)
pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
