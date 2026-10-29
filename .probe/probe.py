"""Does an upscaled input make a better video?

1. upscale the source image with createSuperResolutionNew (measured: 1152x1536 -> 2304x3072)
2. make the same clip twice: from the original URL and from the upscaled URL
3. download both, measure sharpness (Laplacian var), noise (Immerkaer) and bitrate
4. save one frame of each so the pictures can be compared by eye
"""
import json, hashlib, time, urllib.request, urllib.error, pathlib, subprocess, os
import numpy as np
from PIL import Image

HOST = "https://cpi.ufotosoft.com"
CP = "instagram.story.art.collage"; USER = "7da75eed37c61d33"
IMG = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
SR_URL_FILE = "probe_out/sr_url.txt"
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

def sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return (r.stdout or "").strip() or (r.stderr or "").strip()[-100:]

def metrics(jpg):
    a = np.asarray(Image.open(jpg).convert("L"), dtype=np.float64)
    # Laplacian variance = sharpness
    k = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float64)
    from numpy.lib.stride_tricks import sliding_window_view as sw
    lap = (sw(a, (3, 3)) * k).sum(axis=(2, 3))
    sharp = lap.var()
    # Immerkaer noise sigma
    m = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]], dtype=np.float64)
    conv = (sw(a, (3, 3)) * m).sum(axis=(2, 3))
    sigma = np.sqrt(np.pi / 2) / 6 * np.abs(conv).mean()
    return sharp, sigma

pathlib.Path("probe_out").mkdir(exist_ok=True)

# ---- 1) upscale the source (level 3 = "imagesharpen-3")
r = call("/algo/v1/faceFusion/aigc/createSuperResolutionNew", {"imageUrls": [IMG], "level": 3})
job = (r.get("d") or {}).get("jobId")
sr = ""
for i in range(20):
    time.sleep(5)
    q = call("/algo/v1/faceFusion/aigc/querySuperResolutionNew", {"jobId": job})
    urls = (q.get("d") or {}).get("imageUrls") or []
    if urls: sr = urls[0]; break
p("[superres]", sr[:110] if sr else "no url", "job", str(job)[:40])
pathlib.Path(SR_URL_FILE).write_text(sr or IMG)

# ---- 2) two clips, same prompt and settings
PROMPT = "the person breathes calmly, soft window light from the left, static camera"
made = []
for tag, src in (("orig", IMG), ("srup", sr or IMG)):
    b = {"imageUrls": [src], "level": 1, "effectType": 6209, "prompt": PROMPT, "quality": 2}
    r = call("/algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask", b)
    tid = (r.get("d") or {}).get("taskId", "") if isinstance(r.get("d"), dict) else ""
    p(f"[make {tag}] c={r.get('c')} tid={tid[:34]}")
    if tid: made.append((tag, tid))

# ---- 3) poll, download, measure
for tag, tid in made:
    url = ""
    for i in range(40):
        time.sleep(6)
        q = call("/algo/v1/faceFusion/aigc/beatImage2Video/queryTask", {"taskId": tid})
        u = (q.get("d") or {}).get("videoUrl")
        if u: url = u; break
    if not url:
        p(f"[{tag}] TIMEOUT"); continue
    f = dl(url, f"probe_out/{tag}.mp4")
    meta = sh('ffprobe -v error -select_streams v:0 -show_entries stream=width,height,bit_rate '
              '-show_entries format=size,duration -of csv=p=0 "%s"' % f).replace("\n", " ")
    sh('ffmpeg -y -v error -ss 1.5 -i "%s" -frames:v 1 -q:v 2 "probe_out/%s.jpg"' % (f, tag))
    sharp, sigma = metrics(f"probe_out/{tag}.jpg")
    p(f"[{tag}] {meta}  sharp={sharp:.1f} noise={sigma:.2f}  frame={tag}.jpg")
    os.remove(f)

pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
