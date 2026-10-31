"""Runner probe: does the anime master survive a framing change?

Credit 1 gave us `am_master_src.png` — a genuine cel-anime two-shot, painted by the
video model on a blank snow canvas (frame at t=1.5, because t=0 is the fade-in).
That frame is now the only place this cast exists.

Credit 2 asks the one question that decides the rest of the film: can `compose`
take that anime master and give us a *closer* framing of the guard on the left,
keeping the same flat cel style and the same man — instead of (a) the whole pair
again or (b) a random second person?

If yes  -> every framing comes from one master and the cast is consistent by
           construction.
If no   -> the film is built only from framings the master already has (the video
           model can push in *inside* one clip, where identity is inherent).

Also writes a contact sheet so the eye judges, not the claim.
"""
import json, subprocess, sys, pathlib

MASTER = "films/short16/clips_gen/am_master_src.png"
DONOR = "films/short16/clips_gen/c_left_src.png"      # close-up framing only
OUT = "films/short16/clips_gen/am_left_cu.png"

PROMPT = ("Close-up of the guard on the left in the first image: the same young man, the same "
          "pale grey-white lamellar armour laced with red cord, the same plain dark helmet, the "
          "same quiet face. Keep the flat cel-anime style of the first image. Night at the castle "
          "gate, falling snow, warm lantern light on one cheek. 2D cel animation, anime key art, "
          "flat colour fields, hard-edged shadows, constant line width, clean black line art.")

results = {"master": MASTER, "donor": DONOR, "out": OUT, "prompt": PROMPT}
print("== compose: anime master + a semi-real close-up as the framing donor", flush=True)
rc = subprocess.run([sys.executable, "studio/cast.py", "still", "--master", MASTER,
                     "--pose", DONOR, "--prompt", PROMPT, "--out", OUT]).returncode
results["rc"] = rc
print("   rc:", rc, flush=True)

pathlib.Path("films/short16/clips_gen/am_closeup.json").write_text(
    json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")

try:
    from PIL import Image, ImageDraw
    panels = [("master (anime, 1 credit)", MASTER), ("compose -> close-up?", OUT),
              ("donor (semi-real framing only)", DONOR)]
    w = 300
    ims = []
    for label, p in panels:
        if not pathlib.Path(p).exists():
            ims.append((label, None)); continue
        im = Image.open(p).convert("RGB")
        ims.append((label, im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)))
    H = max(im.height for _, im in ims if im) + 22
    sheet = Image.new("RGB", (w * len(ims), H), "black")
    d = ImageDraw.Draw(sheet)
    for i, (label, im) in enumerate(ims):
        if im:
            sheet.paste(im, (i * w, 0))
        d.text((i * w + 4, H - 16), label, fill="white")
    out = pathlib.Path("films/anime_ten/qc/am_closeup.jpg")
    out.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(out, quality=90)
    print("wrote", out, flush=True)
except Exception as e:
    print("sheet failed:", e, flush=True)
