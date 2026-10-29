"""End-to-end proof of the bridge, in the exact shape Jellyfish sends:

    POST /v1/videos  {"prompt", "model", "size", "seconds", "ratio",
                      "input_reference": {"image_url": "data:image/jpeg;base64,…"}}
    GET  /v1/videos/{id}   until status == completed

If this works, any OpenAI-compatible studio can render with Mivi by pointing
base_url at the bridge.
"""
import base64, json, subprocess, sys, time, urllib.request, pathlib

BRIDGE = "http://127.0.0.1:8099"
IMG = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
OUT = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); OUT.append(s)

def req(url, body=None, timeout=90):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"},
                               method="POST" if data else "GET")
    with urllib.request.urlopen(r, timeout=timeout) as resp:
        return json.loads(resp.read().decode())

# start the bridge as a child process
proc = subprocess.Popen([sys.executable, "bridge/mivi_bridge.py"],
                        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
time.sleep(2)

try:
    p("[health]", json.dumps(req(BRIDGE + "/health"))[:160])
    p("[models]", [m["id"] for m in req(BRIDGE + "/v1/models")["data"]])

    raw = urllib.request.urlopen(IMG, timeout=60).read()
    b64 = base64.b64encode(raw).decode()
    p("[image]", f"{len(raw)} bytes -> {len(b64)} chars base64")

    body = {
        "prompt": "the person breathes calmly, soft light from the left, static camera",
        "model": "mivi-gx-720p",
        "size": "960x1280",
        "seconds": 4,
        "ratio": "3:4",
        "input_reference": {"image_url": "data:image/jpeg;base64," + b64},
    }
    created = req(BRIDGE + "/v1/videos", body)
    p("[create]", json.dumps(created)[:200])
    vid = created.get("id")

    final = {}
    for i in range(60):
        time.sleep(6)
        st = req(f"{BRIDGE}/v1/videos/{vid}")
        if i % 3 == 0 or st.get("status") == "completed":
            p(f"  poll {i}: {st.get('status')}")
        if st.get("status") in ("completed", "failed"):
            final = st; break

    p("[final]", json.dumps(final)[:260])
    url = final.get("url")
    if url:
        f = str(pathlib.Path("probe_out/bridge.mp4"))
        pathlib.Path("probe_out").mkdir(exist_ok=True)
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=180) as r, open(f, "wb") as o:
            o.write(r.read())
        meta = subprocess.run('ffprobe -v error -select_streams v:0 -show_entries stream=width,height '
                              '-show_entries format=size,duration -of csv=p=0 "%s"' % f,
                              shell=True, capture_output=True, text=True).stdout.strip().replace("\n", " ")
        p("[file]", meta)
finally:
    proc.terminate()
    try:
        log = proc.communicate(timeout=5)[0]
        p("[bridge log tail]", (log or "")[-300:].replace("\n", " | "))
    except Exception:
        proc.kill()

pathlib.Path("probe_out/out.txt").write_text("\n".join(OUT), encoding="utf-8")
