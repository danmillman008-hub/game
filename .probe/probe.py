import json, hashlib, time, urllib.request, urllib.error, subprocess, pathlib, os, sys

HOST="https://cpi.ufotosoft.com"
USER="7da75eed37c61d33"
IMG="http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
OUT=[]
def p(*a):
    s=" ".join(str(x) for x in a); print(s); OUT.append(s)

def hdr():
    t=str(int(time.time()))
    return {"userid":USER,"timeStamp":t,"cp":"instagram.story.art.collage","version":"407",
            "platform":"1","ifWise":"true","Content-Type":"application/json",
            "sign":hashlib.md5(("m3snil"+t).encode()).hexdigest()}

def call(path,body,host=HOST):
    req=urllib.request.Request(host+path,data=json.dumps(body).encode(),headers=hdr(),method="POST")
    try:
        with urllib.request.urlopen(req,timeout=40) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try: return json.loads(e.read().decode())
        except Exception: return {"http":e.code}
    except Exception as e: return {"err":repr(e)[:150]}

def run(cmd):
    r=subprocess.run(cmd,shell=True,capture_output=True,text=True)
    if r.returncode!=0: p("   !!",cmd,"->",(r.stderr or "")[-200:])
    return r.stdout.strip()

def make(tag,body):
    r=call("/algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask",body)
    tid=(r.get("d") or {}).get("taskId","")
    p(f"[create {tag}] c={r.get('c')} msg={r.get('m')} taskId={tid}")
    return tid

def wait(tid,limit=40):
    for i in range(limit):
        time.sleep(5)
        r=call("/algo/v1/faceFusion/aigc/beatImage2Video/queryTask",{"taskId":tid})
        d=r.get("d") or {}
        st=d.get("taskStatus") or ""
        if d.get("videoUrl"):
            p(f"  [{tid[:22]}] done at poll {i+1}: {d['videoUrl']}")
            return d["videoUrl"]
        if st in ("fail","failed"):
            p(f"  [{tid[:22]}] FAILED {json.dumps(d)[:200]}"); return ""
    p(f"  [{tid[:22]}] timeout"); return ""

def study(tag,url):
    if not url: return
    f=f"probe_out/{tag}.mp4"; pathlib.Path("probe_out").mkdir(exist_ok=True)
    try:
        req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(req,timeout=90) as r, open(f,"wb") as o:
            o.write(r.read())
        p(f"--- {tag}: downloaded {os.path.getsize(f)} bytes")
    except Exception as e:
        p(f"--- {tag}: DOWNLOAD FAILED {e!r}"); return
    try:
        meta=run('ffprobe -v error -select_streams v:0 -show_entries '
                 'stream=width,height,bit_rate,avg_frame_rate,nb_frames '
                 '-show_entries format=size,duration -of json "%s"' % f)
        j=json.loads(meta); st=j["streams"][0]; fmt=j["format"]
        w,h=int(st["width"]),int(st["height"]); size=int(fmt["size"]); dur=float(fmt["duration"])
        bpp=(size*8)/(dur*w*h*32) if w*h*dur else 0
        p(f"    {w}x{h} {dur:.2f}s {size/1024:.0f}KB bpp={bpp:.4f} Mbps={size*8/dur/1e6:.2f}")
    except Exception as e:
        p("    ffprobe failed:",repr(e)[:160])
    for i,t in enumerate([0.3,1.8,3.5]):
        run('ffmpeg -y -v error -ss %s -i "%s" -frames:v 1 -vf "scale=540:-2" probe_out/%s_f%d.jpg' % (t,f,tag,i))
    try: os.remove(f)
    except Exception: pass

p("=== probe", time.strftime("%H:%M:%SZ",time.gmtime()), "===")

# A/B: the two beat modes
a=make("GX6209", {"imageUrls":[IMG],"level":1,"effectType":6209,"prompt":"","quality":2})
b=make("NEON5202",{"imageUrls":[IMG],"level":1,"effectType":5202,"imageEffectType":7186,"prompt":"","quality":2})
p("--- waiting ---")
ua=wait(a) if a else ""
ub=wait(b) if b else ""
study("gx6209",ua)
study("neon5202",ub)

pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT),encoding="utf-8")
