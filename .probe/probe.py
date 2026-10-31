"""Runner probe: does a compose-anchored close-up hold the character?

Called by .github/workflows/probe.yml on a push that touches .probe/** — the only
place in this repo with network access to the Mivi API. Writes the result back.
"""
import subprocess, sys, pathlib

print("== cast ab-test", flush=True)
rc = subprocess.run([sys.executable, "studio/cast.py", "ab-test"]).returncode
print("rc:", rc, flush=True)

# side-by-side for the eye: the old blank-canvas anchor vs the composed one
out = pathlib.Path("films/anime_ten/qc/ab_cast.jpg")
out.parent.mkdir(parents=True, exist_ok=True)
try:
    from PIL import Image, ImageDraw
    left = Image.open("films/short16/clips_gen/c_left_src.png").convert("RGB")
    right = Image.open("films/short16/clips_gen/ab_left_guard.png").convert("RGB")
    w = 420
    def fit(im):
        h = int(im.height * w / im.width)
        return im.resize((w, h), Image.LANCZOS)
    left, right = fit(left), fit(right)
    sheet = Image.new("RGB", (w * 2, max(left.height, right.height) + 22), "black")
    sheet.paste(left, (0, 0)); sheet.paste(right, (w, 0))
    d = ImageDraw.Draw(sheet)
    d.text((6, left.height + 5), "blank canvas (old): a different man", fill="white")
    d.text((w + 6, left.height + 5), "compose master (new)", fill="white")
    sheet.save(out, quality=90)
    print("wrote", out, flush=True)
except Exception as e:
    print("side-by-side failed:", e, flush=True)
raise SystemExit(rc)
