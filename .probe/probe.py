"""The stitch endpoint turned out to be an image COMPOSER (engine gx_img2img_speed_2511):
two photos in, one 960x1280 picture out. Does it also take a prompt? That would be
the image+prompt -> image tool we were after.
"""
import json, hashlib, time, urllib.request, urllib.error, pathlib, subprocess

HOST = "https://cpi.ufotosoft.com"
CP = "instagram.story.art.collage"; USER = "7da75eed37c61d33"
A = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
B = "http://algo.ufotosoft.com/original/261029/56061a5f-6fed-4807-904e-aa42782de3df.jpeg"
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

def dl(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=180) as r, open(dest, "wb") as o: o.write(r.read())
    return dest

pathlib.Path("probe_out").mkdir(exist_ok=True)
BASE = {"level": 1, "deviceToken": "", "ifTest": False}

CASES = [
    ("one_prompt", {"imageUrls": [A], "prompt": "same person, golden hour light, looking at camera"}),
    ("two_prompt", {"imageUrls": [A, B], "prompt": "the two people stand side by side in a studio"}),
    ("two_ratio", {"imageUrls": [A, B], "prompt": "the two people stand side by side", "videoRatio": "3:4"}),
]

for tag, extra in CASES:
    r = call("/algo/v1/faceFusion/aigc/stitchImage/createTask", {**BASE, **extra})
    tid = (r.get("d") or {}).get("taskId", "") if isinstance(r.get("d"), dict) else ""
    p(f"[{tag} create] c={r.get('c')} {str(r.get('m'))[:60]} tid={str(tid)[:34]}")
    if not tid: continue
    for i in range(60):
        time.sleep(6)
        q = call("/algo/v1/faceFusion/aigc/stitchImage/queryTask", {"taskId": tid})
        d = q.get("d") or {}
        u = d.get("responseUrl") or d.get("imageUrl") or d.get("url")
        if u:
            f = dl(u, f"probe_out/st_{tag}.bin")
            out = subprocess.run('/tmp/ffmpeg -y -v error -i "%s" -frames:v 1 -q:v 2 probe_out/st_%s.jpg' % (f, tag),
                                 shell=True, capture_output=True, text=True)
            p(f"[{tag} out] {u[:100]} {pathlib.Path(f).stat().st_size} bytes")
            break
        if str(d.get("taskStatus", "")).lower() in ("failed", "fail"):
            p(f"[{tag} fail]", json.dumps(d, ensure_ascii=False)[:120]); break
    else:
        p(f"[{tag}] timeout")

pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
