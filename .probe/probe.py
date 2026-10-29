import json, hashlib, time, urllib.request, urllib.error, os, pathlib

HOST="https://cpi.ufotosoft.com"; MIRROR="https://cpi.wiseoel.com"
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

def call(method,path,body=None,host=HOST):
    data=json.dumps(body).encode() if (method=="POST" and body is not None) else (b"{}" if method=="POST" else None)
    req=urllib.request.Request(host+path,data=data,headers=hdr(),method=method)
    try:
        with urllib.request.urlopen(req,timeout=40) as r:
            return r.status, r.read().decode("utf-8","replace")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8","replace")[:400]
    except Exception as e:
        return 0, "ERR "+repr(e)[:200]

def show(tag,res):
    p(f"[{tag}] HTTP {res[0]} :: {res[1][:260]}")

p("=== probe start", time.strftime("%H:%M:%SZ", time.gmtime()), "===")

# 1) pose catalogue — three ways
show("pose POST main",   call("POST","/algo/v1/faceFusion/aigc/getAllPoseSequenceId",{}))
show("pose GET  main",   call("GET", "/algo/v1/faceFusion/aigc/getAllPoseSequenceId"))
show("pose GET  mirror", call("GET", "/algo/v1/faceFusion/aigc/getAllPoseSequenceId",host=MIRROR))

# 2) GX with the MATCHING pair from the catalogue: "Neon Couple" = effectType 5202 / imageEffectType 7186
r=call("POST","/algo/v1/faceFusion/aigc/beatImage2Video/createNormalTask",
       {"imageUrls":[IMG],"level":1,"effectType":5202,"imageEffectType":7186,"prompt":"","quality":2})
show("GX 5202+7186", r)
tid=""
try: tid=(json.loads(r[1]).get("d") or {}).get("taskId","")
except Exception: pass
p("GX taskId:", tid)

# 3) V5 with a real catalogue effectType (5202) x a couple of googleIds
for gid in ["1","2"]:
    show(f"V5 et=5202 gid={gid}", call("POST","/algo/v1/faceFusion/aigc/image2video/image2VideoCreateV5",
        {"imageUrls":[IMG],"level":1,"deviceToken":"","googleId":gid,"audio":True,
         "effectType":5202,"prompt":"","duration":8,"ifTest":False}))

# 4) V5 with imageEffectType instead of effectType
show("V5 et=7186", call("POST","/algo/v1/faceFusion/aigc/image2video/image2VideoCreateV5",
    {"imageUrls":[IMG],"level":1,"deviceToken":"","googleId":"1","audio":True,
     "effectType":7186,"prompt":"","duration":8,"ifTest":False}))

# 5) poll the GX task, if any
if tid:
    for i in range(28):
        time.sleep(6)
        st=call("POST","/algo/v1/faceFusion/aigc/beatImage2Video/queryTask",{"taskId":tid})
        try: d=json.loads(st[1]).get("d") or {}
        except Exception: d={}
        s=d.get("taskStatus") or d.get("status") or ""
        if i%3==0: p(f"  poll#{i+1} {s or ('HTTP '+str(st[0]))}")
        if d.get("videoUrl"): p("  VIDEO:", d["videoUrl"]); break
        if s in ("fail","failed"): p("  FAILED:", json.dumps(d)[:200]); break

p("=== probe end ===")
pathlib.Path("probe_out").mkdir(exist_ok=True)
pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
