import json, hashlib, time, urllib.request, urllib.error, subprocess, pathlib, os, concurrent.futures

HOST = "https://cpi.ufotosoft.com"; USER = "7da75eed37c61d33"
IMG = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
OUT = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); OUT.append(s)

def hdr():
    t = str(int(time.time()))
    return {"userid": USER, "timeStamp": t, "cp": "instagram.story.art.collage", "version": "407",
            "platform": "1", "ifWise": "true", "Content-Type": "application/json",
            "sign": hashlib.md5(("m3snil" + t).encode()).hexdigest()}

def call(path, body):
    req = urllib.request.Request(HOST + path, data=json.dumps(body).encode(), headers=hdr(), method="POST")
    try:
        with urllib.request.urlopen(req, timeout=45) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try: return {"_http": e.code, **json.loads(e.read().decode())}
        except Exception: return {"_http": e.code}
    except Exception as e: return {"_err": repr(e)[:120]}

def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if r.returncode != 0: p("  !!", (r.stderr or "")[-140:])
    return r.stdout.strip()

V5 = "/algo/v1/faceFusion/aigc/image2video/image2VideoCreateV5"
V3 = "/algo/v1/faceFusion/aigc/image2VideoCreateV3"
QUERIES = ["/algo/v1/faceFusion/aigc/image2VideoQuery",
           "/algo/v1/faceFusion/aigc/beatImage2Video/queryTask",
           "/algo/v1/faceFusion/aigc/image2video/queryTask",
           "/algo/v1/faceFusion/aigc/queryAiPhotoTask"]

def v5(tag, et, gid, audio, dur, level):
    body = {"imageUrls": [IMG], "level": level, "deviceToken": "", "audio": audio,
            "prompt": "", "ifTest": False}
    if dur is not None: body["duration"] = dur
    if gid is not None: body["googleId"] = gid
    if et is not None: body["effectType"] = et
    return tag, V5, body

TRIALS = [
    ("v5_g1",        None, "1",    False, 6, 1),
    ("v5_g1_720",    None, "1",    False, 6, 2),
    ("v5_g1_audio8", None, "1",    True,  8, 2),
    ("v5_g0",        None, "0",    False, 6, 1),
    ("v5_g100",      None, "100",  False, 6, 1),
    ("v5_gbig",      None, "1234567890123", False, 6, 1),
    ("v5_g1_nodur",  None, "1",    False, None, 1),
    ("v5_g1_ctl",    6209, "1",    False, 6, 1),
]

p("=== veo / pixverse unlock sweep", time.strftime("%H:%M:%SZ", time.gmtime()), "===")
made = []
for tag, et, gid, audio, dur, level in TRIALS:
    _, path, body = v5(tag, et, gid, audio, dur, level)
    r = call(path, body)
    d = r.get("d") or {}
    tid = d.get("taskId") or d.get("id") or ""
    p(f"[{tag}] c={r.get('c')} {str(r.get('m'))[:70]} tid={str(tid)[:34]}")
    if tid: made.append((tag, str(tid)))
    time.sleep(0.4)

def probe_query(tid):
    """which endpoint answers for a task id made by this route"""
    for q in QUERIES:
        r = call(q, {"taskId": tid})
        d = r.get("d") or {}
        yield q.rsplit("/", 1)[-1], r.get("c"), (d.get("videoUrl") or d.get("taskStatus") or str(r.get("m"))[:30])

def finish(it):
    tag, tid = it
    seen = {}
    for i in range(40):
        for name, c, info in probe_query(tid):
            seen[name] = (c, info)
            if isinstance(info, str) and info.startswith("http"):
                return tag, tid, info, seen
        time.sleep(6)
    return tag, tid, "", seen

res = []
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
    for t in ex.map(finish, made): res.append(t)

for tag, tid, url, seen in res:
    p(f"  {tag}: {'OK ' + url[:90] if url else 'NO URL'}")
    p("     q=" + json.dumps(seen, ensure_ascii=False)[:300])

pathlib.Path("probe_out").mkdir(exist_ok=True)
for tag, tid, url, seen in res:
    if not url: continue
    f = f"probe_out/{tag}.mp4"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=120) as r, open(f, "wb") as o: o.write(r.read())
    except Exception as e:
        p(f"  {tag}: dl fail {e!r}"); continue
    meta = run('ffprobe -v error -select_streams v:0 -show_entries stream=width,height,bit_rate '
               '-show_entries format=size,duration -of csv=p=0 "%s"' % f)
    p(f"  {tag}: {meta}  path={url.split('/temp/')[-1][:48]}")
    run('ffmpeg -y -v error -ss 1.5 -i "%s" -frames:v 1 -vf "scale=460:-2" probe_out/%s.jpg' % (f, tag))
    try: os.remove(f)
    except Exception: pass

pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
