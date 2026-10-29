import json, hashlib, time, urllib.request, urllib.error, pathlib

HOST = "https://cpi.ufotosoft.com"; USER = "7da75eed37c61d33"
IMG = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
V5 = "/algo/v1/faceFusion/aigc/image2video/image2VideoCreateV5"
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
        with urllib.request.urlopen(req, timeout=30) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try: return {"_http": e.code, **json.loads(e.read().decode())}
        except Exception: return {"_http": e.code}
    except Exception as e: return {"_err": repr(e)[:100]}

CANDS = list(range(0, 21)) + [100, 200, 300, 400, 500, 1000, 1001, 1002, 1003, 2000, 2001, 2002,
                              3000, 4000, 5000, 5400, 6000, 6001, 6100, 7000, 7100, 7200, 7900,
                              8000, 9000, 9999, 10000, 10001, 31100]

p("=== V5 effectType whitelist sweep", time.strftime("%H:%M:%SZ", time.gmtime()), "===")
legal, other = [], []
for et in CANDS:
    body = {"imageUrls": [IMG], "level": 1, "deviceToken": "", "audio": False,
            "prompt": "", "duration": 6, "ifTest": False,
            "googleId": "1", "effectType": et}
    r = call(V5, body)
    c, m = r.get("c"), str(r.get("m"))
    if "effectType illegal" in m:
        pass
    else:
        (legal if c == 200 else other).append((et, c, m[:80]))
        p(f"  et={et} c={c} {m[:80]}")
p(f"scanned {len(CANDS)} effectType values; non-'effectType illegal' hits: {len(legal)} legal, {len(other)} other")

pathlib.Path("probe_out").mkdir(exist_ok=True)
pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
