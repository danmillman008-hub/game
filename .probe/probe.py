"""Face swap is open: templateIds=[1001] returned an image. Which templates exist,
and what does the output look like? Download the first hit and measure it.
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

def dl(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as o: o.write(r.read())
    return dest

def info(f):
    r = subprocess.run('ffprobe -v error -select_streams v:0 -show_entries stream=width,height '
                       '-show_entries format=size -of csv=p=0 "%s"' % f, shell=True, capture_output=True, text=True)
    return (r.stdout or "").strip().replace("\n", " ")

pathlib.Path("probe_out").mkdir(exist_ok=True)
BASE = {"level": 1, "deviceToken": "", "ifTest": False}
ok = []
for tid in list(range(1000, 1011)) + [1100, 1200, 2001, 2002]:
    r = call("/algo/v1/faceFusion/aigc/createSwapFace", {**BASE, "imageUrls": [IMG], "templateIds": [tid]})
    urls = ((r.get("d") or {}).get("urlList") or []) if isinstance(r.get("d"), dict) else []
    p(f"[swap {tid}] c={r.get('c')} {str(r.get('m'))[:50]} n={len(urls)}")
    if urls: ok.append((tid, urls[0]))
    time.sleep(0.3)

p("working templates:", [t for t, _ in ok])
if ok:
    f = dl(ok[0][1], "probe_out/swap.jpg")
    p("[swap file]", pathlib.Path(f).stat().st_size, "bytes", info(f))

pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
