"""Diagnostics for the five stubborn endpoints.

Goal: tell apart "we send the wrong body" from "the server side is broken".
An endpoint that answers NullPointerException to an EMPTY body never ran its
validation, which means the bug is theirs, not ours.
"""
import json, hashlib, time, urllib.request, urllib.error, pathlib

HOST = "https://cpi.ufotosoft.com"
CP = "instagram.story.art.collage"; USER = "7da75eed37c61d33"
IMG = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
IMG2 = "http://algo.ufotosoft.com/original/261029/56061a5f-6fed-4807-904e-aa42782de3df.jpeg"
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

def brief(r):
    return f"c={r.get('c') or r.get('_http')} m={str(r.get('m'))[:70]} d={json.dumps(r.get('d'), ensure_ascii=False)[:90]}"

# ---------- 1) does image2image validate at all?
II = "/algo/v1/faceFusion/aigc/image2image/createImageTask"
for tag, body in [("empty", {}), ("only_urls", {"imageUrls": [IMG]}),
                  ("urls_style", {"imageUrls": [IMG], "styleId": 1}),
                  ("keys", {"imageKeys": [IMG], "styleId": 1})]:
    p(f"[img2img {tag}]", brief(call(II, body)))

# ---------- 2) does inpaintCleaner validate at all?
IC = "/algo/v1/faceFusion/aigc/createInpaintCleaner"
p("[cleaner empty]", brief(call(IC, {})))
r = call("/algo/v1/faceFusion/aigc/createInpaintAnything", {"imageUrls": [IMG], "level": 1, "deviceToken": "", "ifTest": False})
masks = [x.get("url") for x in ((r.get("d") or {}).get("maskUrlList") or [])]
p("[masks]", len(masks))
if masks:
    p("[cleaner real]", brief(call(IC, {"imageUrls": [IMG], "maskUrls": [masks[0]]})))
    p("[cleaner img2]", brief(call(IC, {"imageUrls": [IMG], "maskUrls": [masks[-1]]})))

# ---------- 3) livePortrait: token / ifFace + which query answers
LP = "/algo/v1/faceFusion/aigc/livePortraitCreate"
tasks = []
for tag, extra in [("tok_empty", {"token": ""}), ("ifFace_true", {"token": "", "ifFace": True}),
                   ("ifFace_false", {"token": "", "ifFace": False})]:
    r = call(LP, {"imageUrls": [IMG], "level": 1, "modelId": 1, **extra})
    tid = (r.get("d") or {}).get("taskId", "") if isinstance(r.get("d"), dict) else ""
    p(f"[live {tag}]", brief(r))
    if tid: tasks.append(tid)

tid = tasks[0] if tasks else ""
if tid:
    time.sleep(20)
    for q in ["/algo/v1/faceFusion/aigc/livePortraitQuery",
              "/algo/v1/faceFusion/aigc/image2VideoQuery",
              "/algo/v1/faceFusion/aigc/queryAiPhotoTask",
              "/algo/v1/faceFusion/aigc/image2video/queryTask"]:
        p(f"[live q {q.rsplit('/')[ -1]}]", brief(call(q, {"taskId": tid})))

# ---------- 4) image2VideoCreateV2: does poseSequenceId want a small int?
V2 = "/algo/v1/faceFusion/aigc/image2VideoCreateV2"
for pose in ["1", "2", "10", 1, 10]:
    p(f"[v2 pose={pose!r}]", brief(call(V2, {"imageUrls": [IMG], "level": 1, "deviceToken": "",
                                                "effectType": 0, "poseSequenceId": pose,
                                                "duration": 4, "prompt": "", "enhance": False, "ifTest": False})))

# ---------- 5) emoVideo with the extra fields its builder sends
EM = "/algo/v1/faceFusion/aigc/emoVideoCreate"
for tag, extra in [("with_token", {"token": "", "signKey": "", "templateid": 1}),
                   ("with_special", {"specialPic": IMG, "face_bbox": "", "ext_bbox": ""})]:
    p(f"[emo {tag}]", brief(call(EM, {"imageKey": IMG, "audioKey": IMG, "level": 1,
                                      "deviceToken": "", "ifTest": False, **extra})))

pathlib.Path("probe_out").mkdir(exist_ok=True)
pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
