"""Can Mivi generate NEW stills (close-ups, new angles) from one master frame?

This is the key question for an unlimited image pipeline: text-to-image does not exist
on Mivi and `image2image/createImageTask` is a server-side NPE. What does exist is
`stitchImage/createTask` (>=2 images + prompt, engine tomoviee_i2i_wplus0_v1_fast).

Three things to establish:
  1. does the same image twice pass the >=2 check?
  2. does master + a crop of itself yield a real close-up?
  3. what does the query return — an image, a list, or a one-frame mp4?
"""
import json, pathlib, time, sys

sys.path.insert(0, "bridge")
import mivi_mcp as M

OUT = pathlib.Path("probe_out"); OUT.mkdir(exist_ok=True)
A = pathlib.Path("films/before_leaving/assets")
LOG = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); LOG.append(s)


def compose_raw(images, prompt, tag, poll_s=260):
    urls = [M.as_url(str(i)) for i in images]
    body = {"imageUrls": urls, "level": 1}
    if prompt:
        body["prompt"] = prompt
    r = M._post(M.STITCH_CREATE, body)
    p(f"[{tag}] create c={r.get('c')} m={r.get('m')} d={json.dumps(r.get('d'))[:160]}")
    if r.get("c") != 200:
        return None
    tid = (r.get("d") or {}).get("taskId")
    deadline = time.time() + poll_s
    saw = None
    while time.time() < deadline:
        q = M._post(M.STITCH_QUERY, {"taskId": tid})
        d = q.get("d") or {}
        saw = d
        urls_out = []
        for key in ("imageUrl", "url", "videoUrl"):
            if d.get(key):
                urls_out.append(d[key])
        for key in ("urlList", "imageUrlList", "maskUrlList"):
            if isinstance(d.get(key), list):
                urls_out += d[key]
        if urls_out:
            p(f"[{tag}] ready keys={list(d.keys())} -> {urls_out[0][:110]}")
            ext = ".mp4" if urls_out[0].lower().endswith(".mp4") else ".png"
            path = OUT / f"{tag}{ext}"
            M.download(urls_out[0], str(path))
            p(f"[{tag}] saved {path} {path.stat().st_size} B")
            return path
        time.sleep(8)
    p(f"[{tag}] timeout, last d={json.dumps(saw)[:200]}")
    return None


p("=== upload refs")
master = M.as_url(str(A / "master_wide.png"))
raha = M.as_url(str(A / "ref_raha.png"))
arad = M.as_url(str(A / "ref_arad.png"))
p("master", master[:90])

# 1) same image twice
compose_raw([A / "master_wide.png", A / "master_wide.png"],
            "cinematic film still, rainy bus stop at dusk, two people, teal and amber",
            "same_twice")

# 2) master + crop of the woman -> close-up
compose_raw([A / "master_wide.png", A / "ref_raha.png"],
            "cinematic close-up film still of the young woman's face, eyes lowered, "
            "one tear on her cheek, rain in her hair, warm streetlamp key light, "
            "teal shadows, 85mm shallow depth of field, film grain",
            "closeup_raha")

# 3) two crops -> a two-shot
compose_raw([A / "ref_raha.png", A / "ref_arad.png"],
            "cinematic two-shot film still: the man stands holding a black umbrella over "
            "the seated woman, rainy bus stop at dusk, teal and amber grade, film grain",
            "twoshot")

# 4) three inputs
compose_raw([A / "master_wide.png", A / "ref_raha.png", A / "ref_umbrella.png"],
            "cinematic film still: she lifts her chin to look at him, umbrella tilted "
            "over her, rain streaks in the lamplight, 85mm, shallow depth of field",
            "three_inputs")

(OUT / "out.txt").write_text("\n".join(LOG), encoding="utf-8")
