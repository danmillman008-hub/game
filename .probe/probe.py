"""Two last shots:

A) livePortrait — the task lands in the image2video table (query answered 3036
   OVERTIME), so the route is alive. Try other modelIds and watch the real query.
B) inpaintCleaner — validation passes and the upstream answers ALGO_RPC_ERROR with
   the masks *it* produced. Try a hand-made binary mask instead (white on black),
   uploaded through multipleUpload.
"""
import json, hashlib, time, urllib.request, urllib.error, pathlib, subprocess, uuid
from PIL import Image, ImageDraw

HOST = "https://cpi.ufotosoft.com"
CP = "instagram.story.art.collage"; USER = "7da75eed37c61d33"
IMG = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
OUT = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); OUT.append(s)

def hdr(ct="application/json"):
    t = str(int(time.time()))
    return {"userid": USER, "timeStamp": t, "cp": CP, "version": "407", "platform": "1",
            "ifWise": "true", "Content-Type": ct,
            "sign": hashlib.md5(("m3snil" + t).encode()).hexdigest()}

def call(path, body):
    req = urllib.request.Request(HOST + path, data=json.dumps(body).encode(), headers=hdr(), method="POST")
    try:
        with urllib.request.urlopen(req, timeout=45) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try: return {"_http": e.code, **json.loads(e.read().decode())}
        except Exception: return {"_http": e.code}
    except Exception as e: return {"_err": repr(e)[:100]}

def upload_file(path, fname, data, ctype="image/png"):
    b = uuid.uuid4().hex
    parts = [("--" + b).encode(),
             f'Content-Disposition: form-data; name="files"; filename="{fname}"'.encode(),
             f"Content-Type: {ctype}".encode(), b"", data,
             ("--" + b + "--").encode(), b""]
    raw = b"\r\n".join(parts)
    req = urllib.request.Request(HOST + path, data=raw,
                                 headers=hdr("multipart/form-data; boundary=" + b), method="POST")
    try:
        with urllib.request.urlopen(req, timeout=120) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try: return {"_http": e.code, **json.loads(e.read().decode())}
        except Exception: return {"_http": e.code}
    except Exception as e: return {"_err": repr(e)[:100]}

def dl(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=180) as r, open(dest, "wb") as o: o.write(r.read())
    return dest

pathlib.Path("probe_out").mkdir(exist_ok=True)

# ---------- A) livePortrait with several model ids
made = []
for mid in [2, 3, 4, 5]:
    r = call("/algo/v1/faceFusion/aigc/livePortraitCreate",
             {"imageUrls": [IMG], "level": 1, "modelId": mid, "token": "", "ifFace": True})
    tid = (r.get("d") or {}).get("taskId", "") if isinstance(r.get("d"), dict) else ""
    st = (r.get("d") or {}).get("taskStatus") if isinstance(r.get("d"), dict) else ""
    p(f"[live modelId={mid}] c={r.get('c')} {str(r.get('m'))[:50]} status={st} tid={str(tid)[:30]}")
    if tid: made.append((mid, tid))

for mid, tid in made:
    for i in range(30):
        time.sleep(8)
        q = call("/algo/v1/faceFusion/aigc/image2VideoQuery", {"taskId": tid})
        d = q.get("d") or {}
        u = d.get("videoUrl")
        if u:
            f = dl(u, f"probe_out/live{mid}.mp4")
            subprocess.run('/tmp/ffmpeg -y -v error -i "%s" -frames:v 1 -q:v 2 probe_out/live{mid}.jpg'.format(mid) % f, shell=True)
            p(f"[live {mid} OUT] {u[:90]} {pathlib.Path(f).stat().st_size}")
            break
        if i in (0, 5, 12, 20):
            p(f"   live {mid} poll{i} c={q.get('c')} {str(q.get('m'))[:40]} {json.dumps(d)[:90]}")
        if q.get("c") not in (200, None): break

# ---------- B) inpaintCleaner with our own binary mask
mask = Image.new("RGB", (512, 640), (0, 0, 0))
dr = ImageDraw.Draw(mask)
dr.ellipse([156, 120, 356, 400], fill=(255, 255, 255))
mask.save("/tmp/mask.png")
up = upload_file("/algo/v1/aiGenerate-aigc/multipleUpload", "mask.png", open("/tmp/mask.png", "rb").read())
p("[mask upload]", json.dumps(up, ensure_ascii=False)[:160])
murl = (up.get("d") or [None])[0] if isinstance(up.get("d"), list) else None
if murl:
    for tag, body in [("own_mask", {"imageUrls": [IMG], "maskUrls": [murl]}),
                      ("own_mask_prompt", {"imageUrls": [IMG], "maskUrls": [murl], "prompt": "sunset"})]:
        r = call("/algo/v1/faceFusion/aigc/createInpaintCleaner", body)
        p(f"[cleaner {tag}] c={r.get('c')} {str(r.get('m'))[:60]} {json.dumps(r.get('d'), ensure_ascii=False)[:100]}")

pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
