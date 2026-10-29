"""Follow-up on the HD result: is c=2002 a billing problem of THIS user or a
general "credits needed" wall?  Also retry HD at level 2, and read whatever the
billing endpoints will tell us.  Read-only except the HD attempts.
"""
import json, hashlib, time, urllib.request, urllib.error, pathlib

HOST = "https://cpi.ufotosoft.com"
CP = "instagram.story.art.collage"; USER = "7da75eed37c61d33"
OUT = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); OUT.append(s)

def hdr():
    t = str(int(time.time()))
    return {"userid": USER, "timeStamp": t, "cp": CP, "version": "407", "platform": "1",
            "ifWise": "true", "Content-Type": "application/json",
            "sign": hashlib.md5(("m3snil" + t).encode()).hexdigest()}

def call(path, body, method="POST"):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(HOST + path, data=data, headers=hdr(), method=method if data else "GET")
    try:
        with urllib.request.urlopen(req, timeout=40) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try: return {"_http": e.code, **json.loads(e.read().decode())}
        except Exception: return {"_http": e.code}
    except Exception as e: return {"_err": repr(e)[:100]}

def brief(r):
    if not isinstance(r, dict): return str(r)[:90]
    d = r.get("d")
    return f"c={r.get('c') or r.get('_http')} m={str(r.get('m'))[:60]} d={json.dumps(d, ensure_ascii=False)[:200] if d is not None else None}"

# the clip the previous run made and hashed
URL = "https://algo-v1.wiseoel.com/temp/60004/261029/img2video_wanlora-20261029233329-861114-d30e4-dwt.mp4"
META = {"videoUrl": URL, "fileMd5": "0e5201cbb795", "fileSize": 861114, "width": 432, "height": 576}
FULL_MD5 = None  # unknown here; the endpoint accepted the short one before, so keep it

for lvl in (1, 2, 3):
    body = {**META, "fileTime": 4, "level": lvl, "deviceToken": "", "ifTest": False}
    p(f"[hd lvl{lvl}]", brief(call("/algo/v1/faceFusion/aigc/createVideoHdTask", body)))

# what the app shows about credits / subscription
for path, body in [
    ("/billing/property/getUpgradeInfo", {"cp": CP}),
    ("/billing/property/restore", {"cp": CP}),
    ("/algo/v1/faceFusion/aigc/queryVideoHdTask", {"taskId": "0"}),
    ("/algo/v1/faceFusion/aigc/getUserInfo", {}),
    ("/algo/v1/faceFusion/aigc/getUserIntegral", {}),
]:
    p(f"[{path.rsplit('/',1)[-1]}]", brief(call(path, body)))

pathlib.Path("probe_out").mkdir(exist_ok=True)
pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
