"""Runner probe: restyle the cast anchors to cel anime WITHOUT losing the face.

The composed two-shot gave us the real pair; these crops are one man each. Now the
question is whether compose can convert a semi-real still into flat cel art and keep
the same face — if yes, the anime line finally has cast-consistent anchors.
"""
import json, subprocess, sys, pathlib

STYLE = ("Convert this to 2D cel animation, anime key animation: flat colour fields, "
         "hard-edged shadows, constant line width, clean line art, same man, same face, "
         "same lamellar armour and helmet, same pose and framing. No photographic texture.")

results = {}
for side in ("left", "right"):
    src = f"films/short16/clips_gen/cast_guard_{side}.png"
    out = f"films/short16/clips_gen/cast_{side}_anime.png"
    print(f"== {side} -> {out}", flush=True)
    rc = subprocess.run([sys.executable, "studio/cast.py", "still", "--master", src,
                         "--pose", src, "--prompt", STYLE, "--out", out]).returncode
    results[side] = {"rc": rc, "out": out}
    print("   rc:", rc, flush=True)

pathlib.Path("films/short16/clips_gen/cast_restyle.json").write_text(
    json.dumps(results, indent=2), encoding="utf-8")

# contact sheet so the eye can judge, not the claim
try:
    from PIL import Image, ImageDraw
    rows = []
    for side in ("left", "right"):
        src = Image.open(f"films/short16/clips_gen/cast_guard_{side}.png").convert("RGB")
        dst = Image.open(f"films/short16/clips_gen/cast_{side}_anime.png").convert("RGB")
        w = 300
        def fit(im):
            h = int(im.height * w / im.width)
            return im.resize((w, h), Image.LANCZOS)
        rows.append((side, fit(src), fit(dst)))
    H = max(max(a.height, b.height) for _, a, b in rows) + 20
    sheet = Image.new("RGB", (w * 4, H * 2), "black")
    d = ImageDraw.Draw(sheet)
    for r, (side, src, dst) in enumerate(rows):
        sheet.paste(src, (0, r * H)); sheet.paste(dst, (w, r * H))
        d.text((4, r * H + H - 16), f"{side}: cast (composed)", fill="white")
        d.text((w + 4, r * H + H - 16), f"{side}: restyled anime", fill="white")
    outp = pathlib.Path("films/anime_ten/qc/cast_restyle.jpg")
    sheet.save(outp, quality=90)
    print("wrote", outp, flush=True)
except Exception as e:
    print("sheet failed:", e, flush=True)
