"""Experiment: can our own 432x576 catalogue clip be lifted with the HD endpoint?

createVideoHdTask (non-Vidu) body from the bytecode:
    videoUrl, fileMd5, fileSize, fileTime, width, height, level, deviceToken, ifTest
So we make a clip, hash it, and ask the server to enhance it.
"""
import json, hashlib, time, urllib.request, urllib.error, subprocess, pathlib, os

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

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return (r.stdout or "").strip() or (r.stderr or "").strip()[-120:]

def fetch(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=180) as r, open(dest, "wb") as o: o.write(r.read())
    return dest

pathlib.Path("probe_out").mkdir(exist_ok=True)

# 1) make a small catalogue clip to enhance
r = call("/algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask",
         {"imageUrls": [IMG], "prompt": "", "effectType": 4991, "level": 1})
tid = (r.get("d") or {}).get("taskId", "")
p(f"[make] c={r.get('c')} tid={tid[:34]}")
url = ""
for i in range(40):
    time.sleep(6)
    q = call("/algo/v1/faceFusion/aigc/beatImage2Video/queryTask", {"taskId": tid})
    u = (q.get("d") or {}).get("videoUrl")
    if u: url = u; break
p("[make] url:", url[:110] if url else "TIMEOUT")
if not url:
    pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8"); raise SystemExit

src = fetch(url, "probe_out/hd_src.mp4")
size = os.path.getsize(src)
md5 = hashlib.md5(open(src, "rb").read()).hexdigest()
meta = run('ffprobe -v error -select_streams v:0 -show_entries stream=width,height -show_entries format=duration '
           '-of csv=p=0 "%s"' % src).replace("\n", " ")
p(f"[src] {size} bytes md5={md5[:12]}… {meta}")
try:
    w, h = meta.split(",")[0], meta.split(",")[1]
    w, h = int(w), int(h)
except Exception:
    w, h = 432, 576
dur = meta.split(",")[-1]
try: durf = float(dur)
except Exception: durf = 4.06

def try_hd(tag, body):
    r = call("/algo/v1/faceFusion/aigc/createVideoHdTask", body)
    tid = (r.get("d") or {}).get("taskId", "") if isinstance(r.get("d"), dict) else ""
    p(f"[{tag}] c={r.get('c')} {str(r.get('m'))[:70]} tid={tid[:30]}")
    return tid

base = {"videoUrl": url, "fileMd5": md5, "fileSize": size, "width": w, "height": h,
        "level": 1, "deviceToken": "", "ifTest": False}
hd_tid = try_hd("hd_sec", {**base, "fileTime": int(round(durf))})
if not hd_tid:
    hd_tid = try_hd("hd_ms", {**base, "fileTime": int(durf * 1000)})
if not hd_tid:
    hd_tid = try_hd("hd_nofiletime", {**base, "fileTime": 0, "fileMd5": md5})

if hd_tid:
    out_url = ""
    for i in range(25):
        time.sleep(6)
        q = call("/algo/v1/faceFusion/aigc/queryVideoHdTask", {"taskId": hd_tid})
        d = q.get("d") or {}
        u = d.get("videoUrl") or d.get("hdVideoUrl")
        if u: out_url = u; break
        if str(d.get("taskStatus", "")).lower() in ("fail", "failed"):
            p("[hd] failed:", json.dumps(d)[:160]); break
    p("[hd] out:", out_url[:110] if out_url else "none")
    if out_url:
        dst = fetch(out_url, "probe_out/hd_out.mp4")
        p("[hd] result:", run('ffprobe -v error -select_streams v:0 -show_entries stream=width,height,bit_rate '
                              '-show_entries format=size,duration -of csv=p=0 "%s"' % dst).replace("\n", " "))
        run('ffmpeg -y -v error -ss 1.5 -i "%s" -frames:v 1 -vf "scale=460:-2" probe_out/hd_out.jpg' % dst)

pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
