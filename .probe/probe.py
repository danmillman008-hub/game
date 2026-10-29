import json, hashlib, time, urllib.request, urllib.error, subprocess, pathlib, os, concurrent.futures

HOST="https://cpi.ufotosoft.com"
USER="7da75eed37c61d33"
IMG="http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
OUT=[]
def p(*a):
    s=" ".join(str(x) for x in a); print(s,flush=True); OUT.append(s)

def hdr():
    t=str(int(time.time()))
    return {"userid":USER,"timeStamp":t,"cp":"instagram.story.art.collage","version":"407",
            "platform":"1","ifWise":"true","Content-Type":"application/json",
            "sign":hashlib.md5(("m3snil"+t).encode()).hexdigest()}

def call(path,body=None,host=HOST,method="POST"):
    data=json.dumps(body if body is not None else {}).encode()
    req=urllib.request.Request(host+path,data=data,headers=hdr(),method=method)
    try:
        with urllib.request.urlopen(req,timeout=45) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try: return {"_http":e.code, **json.loads(e.read().decode())}
        except Exception: return {"_http":e.code}
    except Exception as e: return {"_err":repr(e)[:120]}

def run(cmd):
    r=subprocess.run(cmd,shell=True,capture_output=True,text=True)
    if r.returncode!=0: p("  !!",cmd,"->",(r.stderr or "")[-160:])
    return r.stdout.strip()

p("=== probe", time.strftime("%H:%M:%SZ",time.gmtime()), "===")

# ---------- فاز ۱: اندپوینت‌های فقط-خواندنی (بدون اعتبار) ----------
p("\n--- phase 1: read-only catalogues ---")
READ=["/algo/v1/faceFusion/aigc/queryAiPhotoModels",
      "/algo/v1/faceFusion/aigc/image2VideoCustomer/queryTemplate",
      "/algo/v1/faceFusion/aigc/getAllPoseSequenceId",
      "/algo/v1/faceFusion/aigc/image2VideoDetect",
      "/algo/v1/faceFusion/aigc/getFaceInfo"]
for path in READ:
    r=call(path,{})
    body=json.dumps(r,ensure_ascii=False)
    p(f"[{path.split('/')[-1]}] {body[:420]}")

# ---------- فاز ۲: کدام افکت روی کدام موتور می‌نشیند ----------
p("\n--- phase 2: engine routing per effectsType (beat/createNormalTask) ---")
CAND=[4899,6093,5291,5202,7969,5926,5319,4991,4877,5041,6686,7849,7600,4990,5031,5141]
made=[]
for et in CAND:
    r=call("/algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask",
           {"imageUrls":[IMG],"level":1,"effectType":et,"prompt":"","quality":2})
    d=r.get("d") or {}
    tid=d.get("taskId","")
    p(f"  et={et:<5} c={r.get('c')} msg={str(r.get('m'))[:60]} taskId={tid[:34]}")
    if tid: made.append((et,tid))
    time.sleep(0.4)

p(f"\n--- {len(made)} tasks created; polling in parallel ---")

def finish(item):
    et,tid=item
    for i in range(40):
        time.sleep(6)
        r=call("/algo/v1/faceFusion/aigc/beatImage2Video/queryTask",{"taskId":tid})
        d=r.get("d") or {}
        if d.get("videoUrl"): return et,tid,d["videoUrl"]
        if (d.get("taskStatus") or "") in ("fail","failed"): return et,tid,""
    return et,tid,""

results=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
    for et,tid,url in ex.map(finish,made):
        p(f"  et={et:<5} -> {url[:96] if url else 'TIMEOUT/FAIL'}")
        results.append((et,url))

pathlib.Path("probe_out").mkdir(exist_ok=True)
for et,url in results:
    if not url: continue
    f=f"probe_out/e{et}.mp4"
    try:
        req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(req,timeout=90) as r, open(f,"wb") as o: o.write(r.read())
    except Exception as e:
        p(f"  e{et}: download failed {e!r}"); continue
    meta=run('ffprobe -v error -select_streams v:0 -show_entries stream=width,height '
             '-show_entries format=size,duration -of csv=p=0 "%s"' % f)
    p(f"  e{et}: {meta} path={url.split('/temp/')[-1][:40]}")
    run('ffmpeg -y -v error -ss 1.5 -i "%s" -frames:v 1 -vf "scale=420:-2" probe_out/e%d.jpg' % (f,et))
    try: os.remove(f)
    except Exception: pass

pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT),encoding="utf-8")
