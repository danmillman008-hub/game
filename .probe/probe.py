"""Second route with an `enhance` flag + the image-side endpoints.

Bytecode bodies so far:
  createAiPhotoTaskV2 : imageUrls, level, deviceToken, effectType, poseSequenceId,
                        duration, prompt, enhance, ifTest      -> image2VideoCreateV2
  createAiPhotoTaskV3 : imageUrls, level, deviceToken, pixVerseId, duration, prompt, enhance, ifTest
Read-only attempts below are cheap; only the V2 creates can cost credits.
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

def call(path, body):
    req = urllib.request.Request(HOST + path, data=json.dumps(body).encode(), headers=hdr(), method="POST")
    try:
        with urllib.request.urlopen(req, timeout=45) as r: return json.loads(r.read().decode())
    except urllib.error.HTTPError as e:
        try: return {"_http": e.code, **json.loads(e.read().decode())}
        except Exception: return {"_http": e.code}
    except Exception as e: return {"_err": repr(e)[:100]}

def show(tag, path, body):
    r = call(path, body)
    d = r.get("d")
    extra = ""
    if isinstance(d, dict): extra = " keys=" + ",".join(list(d)[:8])
    elif isinstance(d, list): extra = f" list[{len(d)}]"
    p(f"[{tag}] c={r.get('c') or r.get('_http')} {str(r.get('m'))[:80]}{extra}")
    return r

# ---------- 1) image -> video, second route, with `enhance`
V2 = "/algo/v1/faceFusion/aigc/image2VideoCreateV2"
for tag, et, enh in [("v2_6209_enh", 6209, True), ("v2_6209_noenh", 6209, False),
                     ("v2_0_enh", 0, True)]:
    show(tag, V2, {"imageUrls": [IMG], "level": 1, "deviceToken": "", "effectType": et,
                   "poseSequenceId": "", "duration": 4, "prompt": "آرام نفس می‌کشد", "enhance": enh,
                   "ifTest": False})

# ---------- 2) image upscale
SR = "/algo/v1/faceFusion/aigc/createSuperResolutionNew"
show("superres_min", SR, {"imageUrls": [IMG]})
show("superres_full", SR, {"imageUrls": [IMG], "level": 2, "deviceToken": "", "ifTest": False})

# ---------- 3) image generation / restyle from an image + prompt
II = "/algo/v1/faceFusion/aigc/image2image/createImageTask"
show("img2img_min", II, {"imageUrls": [IMG], "prompt": "same person, golden hour light"})
show("img2img_style", II, {"imageUrls": [IMG], "prompt": "same person, golden hour light",
                           "styleId": 0, "level": 1, "deviceToken": "", "ifTest": False})
show("img2img_model", II, {"imageUrls": [IMG], "prompt": "same person, golden hour light",
                           "modelId": 0, "level": 1, "deviceToken": "", "ifTest": False})

AS = "/algo/v1/faceFusion/aigc/image2image/createAiStyleTask"
show("aistyle_min", AS, {"imageUrls": [IMG]})
show("aistyle_style", AS, {"imageUrls": [IMG], "styleId": 0, "level": 1, "deviceToken": "", "ifTest": False})

pathlib.Path("probe_out").mkdir(exist_ok=True)
pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
