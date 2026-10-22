# Stage 1 — browser reconstruction

A playable reconstruction of Stage 1, rendered by its own Canvas renderer from
data recovered out of the original ROM and from frames the original game produced.
The ROM is never used at runtime: no emulator, no video, no pre-rendered frames
are displayed by the game.

## Run it

The game is static files; it needs no build step and no network.

```sh
cd reconstruction/stage1
python3 -m http.server 8000
# open http://localhost:8000/
```

(Any static file server works. Opening `index.html` directly from `file://` will
not load the ES modules or the PNGs.)

| key | action |
|---|---|
| arrows / WASD | move (left-right along the street, up-down changes depth) |
| J | attack |
| K | jump |
| R | restart |

## Test it

```sh
# behavioural tests, against the shipped module's own update path
node reconstruction/stage1/test/game.test.mjs

# render a frame headlessly (software canvas, no browser needed)
node reconstruction/stage1/test/render.mjs /tmp/out.png 90 "idle:60,right:120,j:20"

# compare a render against an original frame, pixel for pixel
python3 reconstruction/stage1/test/compare.py \
    reconstruction/stage1/evidence/original_f14599.ppm \
    reconstruction/stage1/evidence/recon_idle.png \
    --report /tmp/diff.png
```

`tools/setup_env.sh` creates the Python environment the extraction tools need.

## How the reference gameplay was established

Earlier work in this repository mistook the attract-mode demo, the title screen
and paused screens for gameplay. The corrected boot procedure is
`tools/scenarios/boot1p.txt` and is verified by four independent checks: stage
sprites animate, the timer counts down, the score rises when a foe is defeated,
and holding a direction moves the player and scrolls the camera.

```sh
tools/md_capture/build.sh
tools/md_capture/build/mdcap rom.bin 14600 /tmp/cap tools/scenarios/boot1p.txt --dump-from 14000
```

Playable Stage 1 begins around frame 13700; the capture window used for the art
and the comparisons here is 14300–15600, where the camera is at the stage
opening. ROM sha256 `dd44f120446654bb91c448762f3e0cd0d9b034f35d0e3266a4dc34402ada95c0`.

## Evidence status

**Recovered from the original (not written from scratch)**

| item | how | status |
|---|---|---|
| environment art | per-cell mode across frames, counting only cells no sprite covers (`tools/build_plate2.py`) → `assets/plate.png` | measured; 1097/1120 cells have an uncontested sample |
| player and enemy art | the sprite-table footprint inside a real frame, minus the plate, minus stray blobs (`tools/extract_actors.py`) | measured; each crop is the actor's own pixels |
| stage entry point and camera position | the captured frame the plate comes from | proved |
| HUD geometry and colours | read off a captured frame | measured |

**Reconstructed mechanics (implemented here, *not* the original's code path)**

Movement on a depth plane, jump arc, the three-phase attack (startup / active /
recovery), hit detection with depth tolerance and facing, damage, hitstun,
knockback, knockdown, respawn, enemy approach-and-strike AI, wave spawning,
camera follow, timer, score. These are documented as a reconstruction: they
reproduce the *observable* rules, they are not extracted from the ROM's code.

**Approximate, and known to be**

* The plate is 320 px wide — one screen. Scrolling past its width repeats the
  same art. The original streams new columns into its nametable as the camera
  advances; that path is not reproduced yet.
* Sprite animation uses three extracted poses cycled by state; the original's
  per-animation frame tables have not been read.
* Enemy AI is a plausible approach-and-attack loop, not the original's state
  machine. Enemy counts, spawn positions and timings are approximations.
* HUD text is drawn with a monospace block font, not the original's tiles.

**Unresolved**

* Plane-level VRAM decoding. Tile data decodes correctly (letters and shapes are
  legible), and the Stage-1 nametable is in VRAM, but no plane/palette/scroll
  configuration tried reproduces a captured frame (best cell agreement 8%);
  sprites reconstructed from VRAM tiles do not match the reference either
  (0% of non-transparent pixels). Root cause not yet identified, so the
  environment is recovered from rendered frames instead. Details in
  `RESEARCH_LOG.md` RL-76.
* The 8×8 cells of a real Stage-1 frame do not appear in the 56 assets decoded
  from table `$00A666` (shape matching: 3.8%), so the stage tiles come from a
  load path that has not been traced.

## Measured comparison

`compare_idle` — reconstruction vs original frame 14599 at the stage opening:

| metric | value |
|---|---|
| compared pixels | 71,680 (320×224, native size) |
| differing | 48,055 (**67.04%**) |
| environment rows (y < 168) | 35,395 |
| action rows (y ≥ 168) | 12,660 |
| HUD rows (y < 26) | 2,771 of 8,320 (33.3%) |

No scaling, shifting or filtering is applied to improve the number. The dominant
residual is the HUD font and the actors' poses, which does not mean the mechanics
match — behaviour and appearance are measured separately, and neither is claimed
complete.

Files: `evidence/original_f14599.png`, `evidence/recon_idle.png`,
`evidence/diff_idle.png` (magenta = differing pixels).

## What this is not

Not a claim of pixel-perfect or complete reproduction. Stage 1 is playable with
authentic art and approximately correct mechanics; the boss, the full stage
length, music/SFX and the exact enemy sequencing are not reconstructed.
