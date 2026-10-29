"""Super-resolution round trip: create -> query -> download -> dimensions.
Plus a matrix for image2image/createImageTask, which answered 500 NullPointer
(so the path is live but our body is missing a field).
"""
import json, hashlib, time, urllib.request, urllib.error, pathlib, subprocess

HOST = "https://cpi.ufotosoft.com"
CP = "instagram.story.art.collage"; USER = "7da75eed37c61d33"
IMG = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
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

def dims(path):
    r = subprocess.run('ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of csv=p=0 "%s"' % path,
                       shell=True, capture_output=True, text=True)
    return r.stdout.strip().replace("\n", " ") or r.stderr.strip()[-80:]

def dl(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as o: o.write(r.read())
    return dest

pathlib.Path("probe_out").mkdir(exist_ok=True)
orig = dl(IMG, "probe_out/sr_src.jpg")
p("[src]", pathlib.Path(orig).stat().st_size, "bytes", dims(orig))

# ---- super resolution
r = call("/algo/v1/faceFusion/aigc/createSuperResolutionNew", {"imageUrls": [IMG], "level": 2})
p("[superres create]", json.dumps(r, ensure_ascii=False)[:300])
job = (r.get("d") or {}).get("jobId")
if job:
    out = ""
    for i in range(20):
        time.sleep(5)
        q = call("/algo/v1/faceFusion/aigc/querySuperResolutionNew", {"jobId": job})
        d = q.get("d") or {}
        p("   poll", i, "c=", q.get("c"), json.dumps(d, ensure_ascii=False)[:180])
        urls = d.get("imageUrls") or d.get("resultUrls") or []
        if urls:
            out = urls[0]; break
        if str(d.get("jobStatus", "")) in ("3", "4", "fail", "failed"): break
    if out:
        f = dl(out, "probe_out/sr_out.jpg")
        p("[superres out]", out[:110], pathlib.Path(f).stat().st_size, "bytes", dims(f))

# ---- image2image matrix
II = "/algo/v1/faceFusion/aigc/image2image/createImageTask"
cands = [
    ("a", {"imageUrls": [IMG], "prompt": "golden hour", "level": 1, "deviceToken": "", "ifTest": False, "imageRatio": "3:4"}),
    ("b", {"imageUrl": IMG, "prompt": "golden hour", "level": 1, "deviceToken": "", "ifTest": False}),
    ("c", {"imageUrls": [IMG], "prompt": "golden hour", "token": "", "level": 1, "deviceToken": "", "ifTest": False}),
    ("d", {"imageKeys": [IMG], "prompt": "golden hour", "level": 1, "deviceToken": "", "ifTest": False}),
    ("e", {"imageUrls": [IMG], "prompt": "golden hour"}),
]
for tag, body in cands:
    r = call(II, body)
    p(f"[img2img {tag}] c={r.get('c') or r.get('_http')} {str(r.get('m'))[:70]} d={json.dumps(r.get('d'), ensure_ascii=False)[:120]}")

pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
