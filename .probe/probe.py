"""Field discovery loop.

For every untested endpoint: send the body, read the error, add the field the
server names, repeat. If the server answers 500 NullPointer (no field name),
bulk-add the plausible fields and try again. Prints the body that finally gets
past validation, plus the job/task id when one comes back.
"""
import json, hashlib, time, urllib.request, urllib.error, pathlib, re

HOST = "https://cpi.ufotosoft.com"
CP = "instagram.story.art.collage"; USER = "7da75eed37c61d33"
IMG = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
IMG2 = "http://algo.ufotosoft.com/original/261029/56061a5f-6fed-4807-904e-aa42782de3df.jpeg"
OUT = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); OUT.append(s)

def hdr():
    t = str(int(time.time()))
    return {"userid": USER, "timeStamp": t, "cp": CP, "version": "407", "platform": "1",
            "ifWise": "true", "Content-Type": "application/json",
            "sign": hashlib.md5(("m3snil" + t).encode()).hexdigest()}

def call(path, body):
    req = urllib.request.Request(HOST + path, data=json.dumps(body).encode(), headers=hdr(), method="POST")
    try:
        with urllib.request.urlopen(req, timeout=45) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try: return {"_http": e.code, **json.loads(e.read().decode())}
        except Exception: return {"_http": e.code}
    except Exception as e: return {"_err": repr(e)[:100]}

def guess(name):
    n = name.lower()
    if n in ("imageurls", "imagekeys", "srcimages"): return [IMG]
    if n in ("imageurl", "imagekey", "image", "srcimage", "originurl", "targeturl"): return IMG
    if n in ("audiourls", "audiokeys"): return [IMG]
    if n in ("audiokey", "audiourl"): return IMG
    if n == "token": return ""
    if n == "deviceToken".lower(): return ""
    if n in ("level", "quality", "duration", "styleid", "modelid", "templateid", "lorAid".lower(),
             "type", "gender", "imagetype", "resolution", "ratio"): return 1
    if n in ("prompt", "text", "desc"): return "same person, golden hour light"
    if n in ("iftest",): return False
    if n in ("poseSequenceId".lower(), "pixverseid", "googleid"): return "0"
    return ""

MISS = [
    re.compile(r'"([A-Za-z_]+)"\s*is\s*empty'),
    re.compile(r'([A-Za-z_]+)\s*不能为空'),
    re.compile(r'param illegal:\s*([A-Za-z_]+)'),
    re.compile(r'param error:\s*param\s+([A-Za-z_]+)'),
    re.compile(r'param error:\s*([A-Za-z_]+)'),
    re.compile(r'"([A-Za-z_]+)"\s*must'),
    re.compile(r'([A-Za-z_]+)\s+is\s+invalid'),
]

BULK = {
    "imageUrls": [IMG], "level": 1, "deviceToken": "", "ifTest": False,
    "prompt": "same person, golden hour light", "token": "",
    "ratio": "3:4", "quality": 2, "duration": 4,
}

ENDPOINTS = [
    "/algo/v1/faceFusion/aigc/image2image/createImageTask",
    "/algo/v1/faceFusion/aigc/image2image/createAiStyleTask",
    "/algo/v1/faceFusion/aigc/createInpaintAnything",
    "/algo/v1/faceFusion/aigc/createInpaintCleaner",
    "/algo/v1/faceFusion/aigc/createSwapFace",
    "/algo/v1/faceFusion/aigc/createFaceKeyTask",
    "/algo/v1/faceFusion/aigc/stitchImage/createTask",
    "/algo/v1/faceFusion/aigc/livePortraitCreate",
    "/algo/v1/faceFusion/aigc/emoVideoCreate",
    "/algo/v1/faceFusion/aigc/image2VideoCreateV2",
]

def discover(path):
    body = {}
    log = []
    for rnd in range(10):
        r = call(path, body)
        c = r.get("c") or r.get("_http")
        m = str(r.get("m") or "")
        log.append((rnd, c, m[:70], dict(body)))
        if c == 200:
            return "OK", body, r, log
        if rnd == 6:  # give up on hints, bulk-add everything still missing
            for k, v in BULK.items():
                body.setdefault(k, v)
            continue
        hit = None
        for rx in MISS:
            mm = rx.search(m)
            if mm:
                hit = mm.group(1); break
        if "NullPointer" in m or c == 500:
            for k, v in BULK.items():
                body.setdefault(k, v)
            continue
        if hit and hit not in body:
            body[hit] = guess(hit)
            continue
        if hit and hit in body:
            # value was rejected: try a different shape once
            cur = body[hit]
            body[hit] = {"": IMG, IMG: [IMG], "[URL]": 1, 1: "3:4", "3:4": "4:3"}.get(cur, 0)
            continue
        return "STUCK", body, r, log
    return "MAXROUNDS", body, call(path, body), log

results = {}
for path in ENDPOINTS:
    name = path.rsplit("/", 1)[-1]
    status, body, r, log = discover(path)
    c = r.get("c") or r.get("_http")
    p(f"## {name}: {status}  final c={c} m={str(r.get('m'))[:70]}")
    for rnd, cc, mm, bb in log[-3:]:
        p(f"   r{rnd} c={cc} {mm}")
    p("   body:", json.dumps(body, ensure_ascii=False)[:260])
    d = r.get("d")
    if isinstance(d, dict):
        p("   d.keys:", ",".join(list(d)[:10]))
        jid = d.get("jobId") or d.get("taskId")
        if jid: p("   id:", str(jid)[:50])
    results[name] = {"status": status, "c": c, "body": body, "d": d}

pathlib.Path("probe_out").mkdir(exist_ok=True)
pathlib.Path("probe_out/found.json").write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf-8")
pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
