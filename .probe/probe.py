"""Read-only config/catalogue sweep: look for the server-side lists that the APK
does not contain — Veo's legal effectType set, the `example` values for the
unified/sequence paths, and the beat engine's own resource list.
Nothing here creates a task, so it costs nothing.
"""
import json, hashlib, time, urllib.request, urllib.error, pathlib

HOST = "https://cpi.ufotosoft.com"
MIRROR = "https://cpi.wiseoel.com"
CP = "instagram.story.art.collage"
USER = "7da75eed37c61d33"
OUT = []

def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); OUT.append(s)

def hdr():
    t = str(int(time.time()))
    return {"userid": USER, "timeStamp": t, "cp": CP, "version": "407", "platform": "1",
            "ifWise": "true", "Content-Type": "application/json",
            "sign": hashlib.md5(("m3snil" + t).encode()).hexdigest()}

def http(url, body=None, method=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers=hdr(), method=method or ("POST" if data else "GET"))
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            raw = r.read()
            try: return r.status, json.loads(raw.decode())
            except Exception: return r.status, raw[:400].decode("utf-8", "replace")
    except urllib.error.HTTPError as e:
        try: return e.code, json.loads(e.read().decode())
        except Exception: return e.code, "<html>"
    except Exception as e:
        return 0, repr(e)[:120]

def keys(d, depth=0):
    if isinstance(d, dict):
        out = []
        for k, v in d.items():
            n = f"{k}[{len(v)}]" if isinstance(v, (list, dict)) else f"{k}={str(v)[:40]}"
            out.append(n)
            if depth < 1 and isinstance(v, dict):
                out += [" ." + x for x in keys(v, depth + 1)]
        return out
    return [str(d)[:80]]

def show(tag, url, body=None, method=None):
    st, r = http(url, body, method)
    p(f"[{tag}] {st} {url.split('?')[1][:60] if '?' in url else url.split(HOST)[-1][:60]}")
    if isinstance(r, dict):
        p("   keys:", ", ".join(keys(r))[:300])
        if r.get("c") not in (None, 200):
            p("   c=", r.get("c"), str(r.get("m"))[:80])
    else:
        p("   raw:", str(r)[:160])

BASE_Q = f"version=407&cp={CP}&platform=1&ifHttps=true&day=0&language=en&packageLevel=1"

# 1) sibling endpoints of resourceNew, guessed from assets/config/*.json cache names
for name in ["resourceNew", "aiTools", "aitools", "aiLabGroup", "toolGroups", "resource",
             "config", "getConfig", "appConfig", "aiHomeTools", "ai_home_tools", "category"]:
    for host in [HOST]:
        show(f"vibe/{name}", f"{host}/common/vibe/{name}?{BASE_Q}")

# 2) resourceNew with group hints — every documented groupType is 1401
for extra in ["&groupType=1401&groupId=5074", "&groupType=1401&groupId=3988",
              "&day=1", "&language=fa", "&packageLevel=0", "&packageLevel=2"]:
    show("resourceNew+", f"{HOST}/common/vibe/resourceNew?{BASE_Q}{extra}")

# 3) the beat engine's own catalogue (path seen in the dex)
for body in [None, {}, {"day": 0}, {"type": 1}, {"effectType": 6209}]:
    show("beat/resourceList", f"{HOST}/storyart/ncrnau/beat/getResourceList?{BASE_Q}", body,
         "GET" if body is None else "POST")

# 4) category/resource endpoints
for app in ["instagram.story.art.collage", "vibe"]:
    show(f"category/{app}", f"{HOST}/common/category/{app}/resource?{BASE_Q}")

# 5) mirror host sanity check on the two best candidates
for path in ["/common/vibe/resourceNew", "/storyart/ncrnau/beat/getResourceList"]:
    show("mirror", f"{MIRROR}{path}?{BASE_Q}")

pathlib.Path("probe_out").mkdir(exist_ok=True)
pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
