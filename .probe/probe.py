"""Round 4 — push the remaining doors:

1. stitchImage   : create, then poll up to 8 minutes (it said `doing`)
2. livePortrait  : create, poll with both query shapes
3. createInpaintCleaner : with a REAL mask from createInpaintAnything (the last run
                          fed a random photo as the mask, which cannot work)
4. image2image/createImageTask : try the face-key string, `images`, styleId variants
5. emoVideoCreate : feed the image URL as imageKey and see how far it gets
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

def info(f):
    r = subprocess.run('ffprobe -v error -select_streams v:0 -show_entries stream=width,height,codec_type '
                       '-show_entries format=size,duration -of csv=p=0 "%s"' % f, shell=True, capture_output=True, text=True)
    return (r.stdout or "").strip().replace("\n", " ")

pathlib.Path("probe_out").mkdir(exist_ok=True)
B = {"level": 1, "deviceToken": "", "ifTest": False}

# 1) stitch ---------------------------------------------------------------
r = call("/algo/v1/faceFusion/aigc/stitchImage/createTask", {**B, "imageUrls": [IMG, IMG2]})
tid = (r.get("d") or {}).get("taskId", "")
p("[stitch create]", r.get("c"), str(tid)[:40])
last = ""
for i in range(80):
    time.sleep(6)
    q = call("/algo/v1/faceFusion/aigc/stitchImage/queryTask", {"taskId": tid})
    d = q.get("d") or {}
    last = json.dumps(d, ensure_ascii=False)[:120]
    u = d.get("responseUrl") or d.get("imageUrl") or d.get("url")
    if u:
        f = dl(u, "probe_out/stitch.jpg")
        p("[stitch out]", u[:100], pathlib.Path(f).stat().st_size, info(f)); break
    if str(d.get("taskStatus", "")).lower() in ("failed", "fail"):
        p("[stitch fail]", last); break
    if i % 10 == 0: p("   stitch poll", i, last)
else:
    p("[stitch timeout]", last)

# 2) live portrait --------------------------------------------------------
r = call("/algo/v1/faceFusion/aigc/livePortraitCreate", {**B, "imageUrls": [IMG], "modelId": 1})
tid = (r.get("d") or {}).get("taskId", "")
p("[live create]", r.get("c"), str(tid)[:40])
last = ""
for i in range(50):
    time.sleep(6)
    q = call("/algo/v1/faceFusion/aigc/livePortraitQuery", {"taskId": tid})
    d = q.get("d") or {}
    last = json.dumps(d, ensure_ascii=False)[:140]
    u = d.get("videoUrl")
    if u:
        f = dl(u, "probe_out/live.mp4")
        p("[live out]", u[:100], pathlib.Path(f).stat().st_size, info(f))
        subprocess.run('ffmpeg -y -v error -ss 1 -i "%s" -frames:v 1 -q:v 2 probe_out/live.jpg' % f, shell=True)
        break
    if i % 8 == 0: p("   live poll", i, "c=", q.get("c"), last)
else:
    p("[live timeout]", last)

# 3) inpaint cleaner with a real mask ------------------------------------
m = call("/algo/v1/faceFusion/aigc/createInpaintAnything", {**B, "imageUrls": [IMG]})
masks = [x.get("url") for x in ((m.get("d") or {}).get("maskUrlList") or [])]
p("[masks]", len(masks))
if masks:
    for tag, extra in [("plain", {"maskUrls": [masks[0]]}),
                       ("prompt", {"maskUrls": [masks[0]], "prompt": "sunset sky"}),
                       ("cleaner_all", {"maskUrls": masks[:3]})]:
        rr = call("/algo/v1/faceFusion/aigc/createInpaintCleaner", {**B, "imageUrls": [IMG], **extra})
        p(f"[cleaner {tag}]", rr.get("c"), str(rr.get("m"))[:70], json.dumps(rr.get("d"), ensure_ascii=False)[:140])

# 4) image2image variants -------------------------------------------------
fk = call("/algo/v1/faceFusion/aigc/createFaceKeyTask", {"images": [IMG], **B})
key = (fk.get("d") or "") if isinstance(fk.get("d"), str) else ""
p("[faceKey]", str(key)[:60])
for tag, body in [
    ("key", {"imageKey": key, "prompt": "golden hour", **B}),
    ("images", {"images": [IMG], "prompt": "golden hour", **B}),
    ("style0", {"imageUrls": [IMG], "styleId": 0, "prompt": "golden hour", **B}),
    ("token_key", {"imageUrls": [IMG], "token": key, **B}),
    ("gender", {"imageUrls": [IMG], "prompt": "x", "gender": 1, "styleId": 1, **B}),
]:
    rr = call("/algo/v1/faceFusion/aigc/image2image/createImageTask", body)
    p(f"[img2img {tag}]", rr.get("c"), str(rr.get("m"))[:60], json.dumps(rr.get("d"), ensure_ascii=False)[:110])

# 5) emoVideo -------------------------------------------------------------
rr = call("/algo/v1/faceFusion/aigc/emoVideoCreate", {**B, "imageKey": IMG, "audioKey": IMG})
p("[emo]", rr.get("c"), str(rr.get("m"))[:90], json.dumps(rr.get("d"), ensure_ascii=False)[:120])

pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
