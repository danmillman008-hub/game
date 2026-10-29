import json, hashlib, time, urllib.request, urllib.error, subprocess, pathlib, os, concurrent.futures

HOST="https://cpi.ufotosoft.com"; USER="7da75eed37c61d33"
IMG="http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
OUT=[]
def p(*a):
    s=" ".join(str(x) for x in a); print(s,flush=True); OUT.append(s)
def hdr():
    t=str(int(time.time()))
    return {"userid":USER,"timeStamp":t,"cp":"instagram.story.art.collage","version":"407",
            "platform":"1","ifWise":"true","Content-Type":"application/json",
            "sign":hashlib.md5(("m3snil"+t).encode()).hexdigest()}
def call(path,body):
    req=urllib.request.Request(HOST+path,data=json.dumps(body).encode(),headers=hdr(),method="POST")
    try:
        with urllib.request.urlopen(req,timeout=45) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try: return {"_http":e.code,**json.loads(e.read().decode())}
        except Exception: return {"_http":e.code}
    except Exception as e: return {"_err":repr(e)[:120]}
def run(cmd):
    r=subprocess.run(cmd,shell=True,capture_output=True,text=True)
    if r.returncode!=0: p("  !!",(r.stderr or "")[-140:])
    return r.stdout.strip()

# (tag, effectsType, extra body fields)
TRIALS=[
 ("lv2_7600", 7600, {"level":2,"quality":2}),
 ("lv2_4991", 4991, {"level":2,"quality":2}),
 ("lv2_6209", 6209, {"level":2,"quality":2}),
 ("q720_lv1_7600", 7600, {"level":1,"quality":2}),
 ("lv2_noq_7600", 7600, {"level":2}),
]
p("=== level sweep", time.strftime("%H:%M:%SZ",time.gmtime()), "===")
made=[]
for tag,et,extra in TRIALS:
    body={"imageUrls":[IMG],"prompt":"","effectType":et}; body.update(extra)
    r=call("/algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask",body)
    d=r.get("d") or {}; tid=d.get("taskId","")
    p(f"[{tag}] c={r.get('c')} {str(r.get('m'))[:70]} tid={tid[:30]} body={json.dumps(body)[:120]}")
    if tid: made.append((tag,tid))
    time.sleep(0.5)

def finish(it):
    tag,tid=it
    for i in range(45):
        time.sleep(6)
        r=call("/algo/v1/faceFusion/aigc/beatImage2Video/queryTask",{"taskId":tid})
        d=r.get("d") or {}
        if d.get("videoUrl"): return tag,tid,d["videoUrl"]
        if (d.get("taskStatus") or "") in ("fail","failed"): return tag,tid,""
    return tag,tid,""

res=[]
with concurrent.futures.ThreadPoolExecutor(max_workers=6) as ex:
    for t in ex.map(finish,made): res.append(t)
for tag,tid,url in res: p(f"  {tag}: {url[:100] if url else 'TIMEOUT'}")

pathlib.Path("probe_out").mkdir(exist_ok=True)
for tag,tid,url in res:
    if not url: continue
    f=f"probe_out/{tag}.mp4"
    try:
        req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(req,timeout=90) as r, open(f,"wb") as o: o.write(r.read())
    except Exception as e:
        p(f"  {tag}: dl fail {e!r}"); continue
    meta=run('ffprobe -v error -select_streams v:0 -show_entries stream=width,height,bit_rate '
             '-show_entries format=size,duration -of csv=p=0 "%s"' % f)
    p(f"  {tag}: {meta}  path={url.split('/temp/')[-1][:44]}")
    run('ffmpeg -y -v error -ss 1.5 -i "%s" -frames:v 1 -vf "scale=460:-2" probe_out/%s.jpg' % (f,tag))
    try: os.remove(f)
    except Exception: pass
pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT),encoding="utf-8")
