"""Two remaining shots at an unlocked engine, plus the config paths that answer
GET with a param hint. Read-only calls first, then the unified/sequence create
attempts with the motion-chip words the app shows (Animate / Walk / Wave).
"""
import json, hashlib, time, urllib.request, urllib.error, pathlib

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

def http(url, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=hdr(), method="POST" if data else "GET")
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            raw = r.read()
            try: return r.status, json.loads(raw.decode())
            except Exception: return r.status, raw[:300].decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read().decode())
        except Exception: return e.code, "<html>"
    except Exception as e:
        return 0, repr(e)[:120]

def call(path, body):
    return http(HOST + path, body)[1]

Q = f"version=407&cp={CP}&platform=1&ifHttps=true&day=0&language=en&packageLevel=1"

# --- beat resource list: GET only, needs a param we do not know yet
for extra in ["", "&type=1", "&day=1", "&categoryId=0", "&groupId=5074",
              "&resourceType=1", "&beatId=0", "&packageLevel=1&start=0"]:
    st, r = http(f"{HOST}/storyart/ncrnau/beat/getResourceList?{Q}{extra}")
    msg = r.get("m") if isinstance(r, dict) else str(r)[:60]
    keys = list(r.get("d").keys()) if isinstance(r, dict) and isinstance(r.get("d"), dict) else ""
    p(f"[beatList{extra[:22]}] {st} c={r.get('c') if isinstance(r,dict) else '-'} {str(msg)[:60]} {keys}")

# --- unified: body = imageUrls, level, deviceToken, prompt, ratio, movementAmplitude, example, ifTest
UNI = "/algo/v1/faceFusion/aigc/image2video/unifiedTaskCreate"
made = []
for ex in ["Animate", "Walk", "Wave", "Dance", "animate", "walk", "wave", "Animate01"]:
    body = {"imageUrls": [IMG], "level": 1, "deviceToken": "", "prompt": "",
            "ratio": "3:4", "movementAmplitude": 1, "example": ex, "ifTest": False}
    r = call(UNI, body)
    tid = (r.get("d") or {}).get("taskId", "") if isinstance(r.get("d"), dict) else ""
    p(f"[uni:{ex}] c={r.get('c')} {str(r.get('m'))[:60]} tid={tid[:30]}")
    if tid: made.append(("uni_" + ex, tid, "unified"))

# --- sequence (new route) with a pose id guess + catalogue effect
SEQ = "/algo/v1/faceFusion/aigc/integrated/image2VideoCreateV4"
for et, pose in [(4991, "1"), (7600, "1"), (4991, "0")]:
    body = {"imageUrls": [IMG], "level": 1, "deviceToken": "", "effectType": et,
            "poseSequenceId": pose, "pixVerseId": "0", "ifTest": False}
    r = call(SEQ, body)
    tid = (r.get("d") or {}).get("taskId", "") if isinstance(r.get("d"), dict) else ""
    p(f"[seq:{et}/{pose}] c={r.get('c')} {str(r.get('m'))[:60]} tid={tid[:30]}")
    if tid: made.append((f"seq_{et}_{pose}", tid, "seq"))

p(f"created {len(made)} tasks")
pathlib.Path("probe_out").mkdir(exist_ok=True)
pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
