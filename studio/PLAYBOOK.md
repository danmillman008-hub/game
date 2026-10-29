# PLAYBOOK — how I make a film from a screenplay

This is my operating procedure, not documentation for a human. When a script arrives,
I follow **MIVI-STD-1** top to bottom. Nothing is improvised twice.

Environment: `bridge/mivi_mcp.py` (Mivi + ffmpeg over MCP), `studio/filmkit.py` (the CLI),
`bridge/FILM_DIRECTOR_SKILL.md` (shot grammar), `studio/TECHNIQUES.md` (the tricks).

Hard constraints of the engine — design inside them:

| Constraint | Value |
|---|---|
| shot length | **4.03 s**, not adjustable |
| resolution | 960×1280 (720P) / 432×576 (360P) |
| seed | none — a shot cannot be re-rendered identically |
| end frame | not supported |
| native audio | none |
| text-to-video | not available — **every shot starts from an image** |
| reliable continuity | ~2 chained hops before costume/light drift |
| lip sync | account-locked on Mivi (see TECHNIQUES §L) |

---

## MIVI-STD-1 — the standard procedure

### 0 · Intake (no generation, no cost)

1. Read the screenplay. Write the **logline** and the **emotional arc** in one line each.
2. Decide the delivery: runtime, aspect (default 3:4 vertical), subtitles or VO.
3. Budget: `shots = ceil(target_seconds / 3.6)`. One render per take. Draft at 360P.

Stop and confirm with the user if the script implies >25 shots (≈90 s) — that is a
different budget conversation.

### 1 · Shot list (`filmkit plan`)

Write `script.txt` in this shape:

```
SHOT: the watchmaker lifts his head from the bench, dust in a shaft of lamplight, slow push in
VO: Every second he saved
SHOT: he looks straight into the lens, the lamp flickers once, subtle handheld drift
VO: cost him one of his own
```

Then `filmkit plan <name> --script script.txt`.

Rules for a shot line: **one motion idea**, ≤25 words, motion and light only — never
identity, never wardrobe, never a second action. A 4 s window holds one idea.

Coverage: for any scene the audience must *feel*, plan **three angles of the same
moment** (wide / medium / close) and cut between them. That is where "edited" comes
from, and it costs the same as three unrelated shots.

### 2 · Keyframes before video (`filmkit still`)

Every shot needs a still first. Sources, in order of preference:

1. `--from compose:a.png,b.png --prompt "…"` — build the frame from references
   (character + location plate). This is the only "image edit" Mivi exposes.
2. `--from upscale:assets/s01.png` — clean 2× hero still.
3. `--from file:assets/s01.png` — an approved still we already have.
4. `--from swapface:assets/s01.png --template 1001` — keep a face consistent.
5. `--from last:3` — chain (step 3b).

Spend the effort here: **the still decides the shot; the prompt only decides the motion.**

### 3 · Render (`filmkit shot`)

- Draft every shot at `--quality 1`, `--takes 2`, look at the frames, then re-render only
  the keeper at `--quality 2`.
- 3a **Accept**: `filmkit frames <clip> --at 0.5,2,3.8` and look. Reject on: extra limb,
  face change, unexplained camera move, melted background, text artifacts.
- 3b **Chain**: `filmkit chain <name> --from 3 --to 4` — the last frame of shot 3 becomes
  the still of shot 4. Use inside a scene only. **Re-anchor on an approved still after
  two hops.**

### 4 · Assemble (`filmkit assemble`)

- Default cut: hard cuts, `--crossfade 0`. Dissolve only between shots of the same scene.
- Never dissolve a change of location — it reads as a render error.
- Add pauses on the emotional beat: if the arc peaks, cut *before* the motion ends.

### 5 · Voice (`filmkit mix`)

I synthesize the narration myself, then lay it over:

1. Split the VO text at sentence boundaries; one clip per sentence.
2. Generate with my own TTS (needs a voice audition once per project; Persian voice).
3. `filmkit mix <name> --vo audio/vo.mp3 --music audio/bed.mp3 --duck`.
4. Bed sits at −18 dB and auto-ducks under the voice. Pad the audio, never shorten the
   picture (the command already does this).

The mix is verified by `filmkit qc` — `has_audio` must be `true`.

### 6 · Subtitles

- `subs/final.srt`, two lines max, ≤17 characters per second of screen time.
- Bottom-safe area: keep text in the lowest 15%, and never under a face.
- Burned by `assemble`; keep the SRT in the project for re-edits.

### 7 · QC gate — never skip

`filmkit qc <name>` must report **no issues**:
- every clip 960×1280 and 3.5–4.6 s
- `frame_delta` under ~55 between sampled frames (above = a melt)
- `has_audio` true if VO was added
- I then *look* at all five sampled frames myself before showing anything.

### 8 · Deliver (`filmkit deliver`)

- **GitHub**: `filmkit deliver <name> --github --tag v1` → release asset + URL.
- **Google Drive**: `filmkit deliver <name> --drive` writes the manifest; I upload the
  path with the Drive connector and hand back the link. (Drive re-uploads are safest for
  anything the user will watch on a phone.)

Report back with: the link, runtime, shot count, and the two frames that show the film's
best and worst continuity.

---

## Decision tree when a shot fails

```
shot rejected
├─ face/identity drifted ────────► re-anchor: rebuild the still from an approved
│                                  portrait (compose or swapface), re-render
├─ motion too big / melted ──────► cut the prompt to ONE verb, re-render
├─ model invents a new action ───► shorten to ≤12 words, add "camera holds still"
├─ engine returns nothing 3× ────► freeze-frame fallback (TECHNIQUES §H):
│                                  keep the still, Ken Burns 4 s, mark as a "photo beat"
├─ two takes both usable ────────► keep both, cut between them as coverage
└─ the scene does not work at 4 s ► split it into two shots with a cut
```

## Cost discipline

- 360P drafts, 720P only for keepers.
- Max 2 takes per shot by default; a third take needs a reason.
- Never batch-generate the whole film before seeing one finished shot.

## What I check before saying "done"

- [ ] `filmkit qc` has zero issues
- [ ] I looked at 5 frames
- [ ] runtime matches the brief ±1 shot
- [ ] subtitles readable, not over faces
- [ ] voice is audible and not clipped
- [ ] link opens (release asset / Drive)
