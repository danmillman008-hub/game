"""Build the film's key stills on Mivi (2-image composer), then look at them.

No local image generation: `stitchImage` with exactly two references is the only
image engine on this account, and it now returns via `responseUrl` (fixed in
bridge/mivi_mcp.py: t_compose).

Produces, for «قبل از رفتن»:
  s01_wide      master frame (wide, both characters)
  s04_raha_cu   close-up of Raha from master + her crop
  s09_arad_cu   close-up of Arad from master + his crop
  s12_two       two-shot built from the two crops
"""
import json, pathlib, sys

sys.path.insert(0, "bridge")
import mivi_mcp as M

A = pathlib.Path("films/before_leaving/assets")
OUT = A / "stills"
OUT.mkdir(parents=True, exist_ok=True)
LOG = []


def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); LOG.append(s)


JOBS = [
    ("s04_raha_cu", "master_wide.png", "ref_raha.png",
     "cinematic close-up film still of the young woman's face, eyes lowered, holding back "
     "tears, rain droplets in her dark wavy hair, warm streetlamp key light from the left, "
     "cool teal shadows, 85mm shallow depth of field, film grain, 3:4 vertical"),
    ("s09_arad_cu", "master_wide.png", "ref_arad.png",
     "cinematic close-up film still of the young man's face under a black umbrella, "
     "worried tender expression, rain on his coat collar, warm rim light from the "
     "streetlamp behind, cool teal ambient, 85mm shallow depth of field, film grain, "
     "3:4 vertical"),
    ("s12_two", "ref_raha.png", "ref_arad.png",
     "cinematic two-shot film still at a rainy bus stop at dusk: the man stands beside the "
     "seated woman holding a black umbrella tilted over her, both in charcoal and grey "
     "wool coats, wet pavement reflections, teal and amber grade, film grain, 3:4 vertical"),
]

for tag, a_ref, b_ref, prompt in JOBS:
    p(f"\n[{tag}] compose")
    try:
        r = M.t_compose({"images": [str(A / a_ref), str(A / b_ref)], "prompt": prompt,
                         "out": str(OUT / f"{tag}.jpeg"), "timeout_s": 420})
    except Exception as exc:
        p(f"  EXC {type(exc).__name__}: {exc}")
        continue
    p("  ->", json.dumps(r)[:220])
    if r.get("saved"):
        from PIL import Image
        im = Image.open(r["saved"])
        p(f"  size {im.size}  {pathlib.Path(r['saved']).stat().st_size} B")

(OUT / "images_log.txt").write_text("\n".join(LOG), encoding="utf-8")
pathlib.Path("probe_out/out.txt").write_text("\n".join(LOG), encoding="utf-8")
