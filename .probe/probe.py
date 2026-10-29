"""Round 3: collect what the newly opened endpoints actually produce.

- stitchImage   : create -> queryTask -> download
- livePortrait  : create(modelId=1) -> livePortraitQuery -> download
- inpaintAnything: it returned maskUrlList; feed a mask back and see if it edits
- createSwapFace: templateIds must be ints -> try small ids to learn the error
- createFaceKeyTask: print the full response
"""
import json, hashlib, time, urllib.request, urllib.error, pathlib, subprocess

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

def dl(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=180) as r, open(dest, "wb") as o: o.write(r.read())
    return dest

def probe(path):
    r = subprocess.run('ffprobe -v error -show_entries stream=width,height,codec_type,codec_name '
                       '-show_entries format=size,duration -of csv=p=0 "%s"' % path,
                       shell=True, capture_output=True, text=True)
    return (r.stdout or "").strip().replace("\n", " ")

pathlib.Path("probe_out").mkdir(exist_ok=True)
BASE = {"level": 1, "deviceToken": "", "ifTest": False}

# ---------- 1) stitch
r = call("/algo/v1/faceFusion/aigc/stitchImage/createTask", {**BASE, "imageUrls": [IMG, IMG2]})
tid = (r.get("d") or {}).get("taskId", "")
p("[stitch create]", r.get("c"), str(tid)[:44])
for i in range(20):
    time.sleep(4)
    q = call("/algo/v1/faceFusion/aigc/stitchImage/queryTask", {"taskId": tid})
    d = q.get("d") or {}
    u = d.get("responseUrl") or d.get("imageUrl") or d.get("url")
    if u:
        f = dl(u, "probe_out/stitch.jpg")
        p("[stitch out]", u[:100], pathlib.Path(f).stat().st_size, probe(f)); break
    if str(d.get("taskStatus", "")).lower() in ("failed", "fail"): p("[stitch fail]", d); break
else:
    p("[stitch] timeout", json.dumps(q, ensure_ascii=False)[:160])

# ---------- 2) live portrait
r = call("/algo/v1/faceFusion/aigc/livePortraitCreate", {**BASE, "imageUrls": [IMG], "modelId": 1})
tid = (r.get("d") or {}).get("taskId", "")
p("[live create]", r.get("c"), str(tid)[:44])
for i in range(25):
    time.sleep(6)
    q = call("/algo/v1/faceFusion/aigc/livePortraitQuery", {"taskId": tid})
    d = q.get("d") or {}
    u = d.get("videoUrl")
    if u:
        f = dl(u, "probe_out/live.mp4")
        p("[live out]", u[:100], pathlib.Path(f).stat().st_size, probe(f))
        subprocess.run('ffmpeg -y -v error -ss 1 -i "%s" -frames:v 1 -q:v 2 probe_out/live.jpg' % f, shell=True)
        break
    if str(d.get("taskStatus", "")).lower() in ("failed", "fail"): p("[live fail]", json.dumps(d)[:160]); break
else:
    p("[live] timeout", json.dumps(q, ensure_ascii=False)[:160])

# ---------- 3) inpaint: masks first, then edit with one of them
r = call("/algo/v1/faceFusion/aigc/createInpaintAnything", {**BASE, "imageUrls": [IMG]})
masks = [m.get("url") for m in ((r.get("d") or {}).get("maskUrlList") or [])]
p("[inpaint masks]", len(masks), (masks[0][:90] if masks else ""))
if masks:
    for tag, extra in [("with_mask", {"maskUrls": [masks[0]], "prompt": "make the background a sunset"}),
                       ("mask_label", {"maskUrls": [masks[0]], "prompt": "sunset", "label": "Background"})]:
        rr = call("/algo/v1/faceFusion/aigc/createInpaintAnything", {**BASE, "imageUrls": [IMG], **extra})
        p(f"[inpaint {tag}]", rr.get("c"), str(rr.get("m"))[:70], json.dumps(rr.get("d"), ensure_ascii=False)[:140])

# ---------- 4) swap face with integer template ids
for ids in ([1], [0], [1001]):
    r = call("/algo/v1/faceFusion/aigc/createSwapFace", {**BASE, "imageUrls": [IMG], "templateIds": ids})
    p(f"[swap {ids}]", r.get("c"), str(r.get("m"))[:80], json.dumps(r.get("d"), ensure_ascii=False)[:120])

# ---------- 5) face key: what comes back?
r = call("/algo/v1/faceFusion/aigc/createFaceKeyTask", {"images": [IMG], **BASE})
p("[faceKey]", json.dumps(r, ensure_ascii=False)[:300])

pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
