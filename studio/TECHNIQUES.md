# TECHNIQUES — the craft, mapped to tools

Every technique here has a concrete implementation in this repo. Nothing is "would be
nice". Where Mivi cannot do a thing, the workaround is stated plainly.

## A · Frame-first (still → video)

Mivi has no text-to-video. The still is the shot; the prompt only decides motion.

```
still  = identity, wardrobe, set, light, lens, framing      (built with compose/upscale/swapface)
prompt = one verb of motion + camera behaviour              (≤25 words)
```

Consequence: you get to *cast, light and frame* every shot before spending a render.
Use it — build the frame you actually want, not a frame the encoder happened to produce.

## B · Last-frame chaining

`filmkit chain --from N --to N+1`: last frame of N becomes the still of N+1.

- Keeps wardrobe, set, light and lens across a cut.
- **Limit: 2 hops.** After that, costume/light drift becomes visible (measured: a white
  robe drifted to pink-grey by hop 3).
- Never chain across a scene break — a hard cut to a new still is correct there.

## C · Coverage — the actual source of "edited"

One moment, several angles, cut between them:

| Angle | Prompt shape | Use |
|---|---|---|
| wide | `wide shot, he works at the bench, camera slowly pushes in` | establish |
| medium | `medium shot, hands and face, subtle handheld drift` | action |
| close | `close on his eyes, lamp reflection moves, camera holds still` | emotion |
| insert | `macro of the watch movement ticking, shallow depth of field` | hide weak motion |

Three angles of one beat = 12 s of editable material from the same still family.
Editing then chooses *when* to cut, which is what makes a film feel directed.

## D · 4-second economy

- **Cut on motion**: end a shot while the movement is still going; the next shot inherits
  the energy.
- **J-cut / L-cut**: start the next line of VO before the picture cuts (J), or let the
  previous line run 0.3 s over the new shot (L). With `filmkit mix` the audio is a single
  track, so write the SRT/VO timings with the overlap already in them.
- **Pause beats**: an empty 4 s shot after a reveal is not waste, it is air.

## E · Background separation → character insertion

What Mivi actually offers:

1. `mivi_masks` returns 7 labelled masks for an image (subject, hair, clothes, …).
2. `mivi_compose` (2+ images + prompt) blends references into a new image.
3. `createSwapFace` puts a face on a template.

So the workflow is **build the plate, then place the character**, not Photoshop-style
alpha compositing:

```
plate      = "empty workshop, lamp, dust, no people"        (compose or an approved still)
character  = approved portrait / full-body still
keyframe   = compose(plate, character, "the man stands at the bench, 50mm, side key")
```

The masks are used as *evidence* (what the subject is, where it ends) to write a better
prompt — Mivi has no endpoint that returns an edited image from a mask, so do not plan a
shot that needs one.

## F · Angles and optics vocabulary

Encode lens and light in the prompt so the look stays consistent across shots:

- optics: `24mm wide, deep focus` · `50mm, medium` · `85mm, shallow depth of field, bokeh`
- light: `hard side key, deep shadow` · `soft window light` · `practical lamp, warm 3200K` ·
  `rim light from behind` · `haze, volumetric shaft`
- camera: `camera holds still` · `slow push in` · `subtle handheld drift` · `slow tilt up`
- grade: `cool shadows, warm highlights` · `desaturated, high contrast`

Keep one lens/light pair per scene. Changing it mid-scene reads as a different location.

## G · Taking several versions of one shot

`filmkit shot --takes 2` renders the same intake twice. Without a seed every take differs,
so treat takes as *coverage of the same beat*: pick the best, or keep two and cut between
them. This is the cheapest way to buy editorial choice.

## H · Fallback when video generation refuses

If a shot fails three times (melt, no motion, wrong subject), do not keep paying:

1. Keep the still. Animate it with ffmpeg: slow Ken Burns push (`zoompan`) at 24 fps for 4 s.
2. Declare it a "photo beat". In a film with moving shots around it, one held frame reads
   as an intentional pause, not a failure.
3. Never leave a gap in the timeline — a missing shot breaks the cut rhythm.

## I · Colour and exposure matching

Chained shots drift. Before assembly, compare the mean luma of each clip's mid-frame and
pull outliers back with `eq` (one command per clip). Keep the change ≤0.08 brightness;
larger corrections look graded-on-purpose and break continuity differently.

## J · Vertical framing (960×1280)

- Subject eyes at ~38% from the top; headroom 8–12%.
- Keep faces out of the bottom 15% (subtitle safe area) and the top 10% (UI overlap).
- 3:4 is the native ratio; 16:9 output needs pad + blur, 1:1 needs a centre crop.

## K · Voice over — my own TTS

The engine has no audio, so narration is mine to synthesize:

1. Split the VO into sentences; one clip per sentence (cleaner timing, easier re-takes).
2. Generate with my TTS in the project's language (Persian for this user).
3. `filmkit mix --vo audio/vo.mp3 --music audio/bed.mp3 --duck`.
4. Speech rate ≈ 800–900 characters per minute — a 60 s film holds ≈ 850 characters.
5. Bed music at −18 dB, ducked under the voice; verify `has_audio: true` in QC.

## L · Lip sync — the honest position

Mivi's lip-sync path is the AiFace `emoVideo` endpoint (image + audio → talking clip). It
is **account-locked**: every body shape returns `c=1001 invalid user`, because the keys
come from AiFace's own upload realm, not ours. `livePortrait` creates tasks but never
completes (`3036 OVERTIME`). So there is no working native lip sync at this time.

What to do instead, in order of quality:

1. **Do not show the mouth.** Cut at the moment a character speaks: back of head, hands,
   silhouette, over-the-shoulder, listener's reaction. This is standard film grammar and
   costs nothing.
2. **VO over B-roll.** The line plays over an insert; nobody expects lip movement.
3. **Profile or off-frame dialogue.** A character speaking out of frame while we watch the
   listener is a J-cut, again free.
4. If a synchronised face is ever required: a dedicated lip-sync model on a GPU box
   (Wav2Lip-class) applied after assembly. Out of scope here — say so, do not fake it.

## M · Sound design with ffmpeg only

- Whoosh on a fast cut: 120 ms filtered noise burst, −24 dB.
- Impact on a reveal: low sine thump, −18 dB, with a 40 ms attack.
- Room tone under everything at −34 dB kills the "dead silence" feeling.
- Never let a cut land on absolute silence; it makes the edit feel broken.

## N · QC, mechanically

`filmkit qc` reports per-clip resolution/duration, samples 5 frames of the final, and
computes `frame_delta` between consecutive samples (>55/255 = suspicious melt). Then I
look at the frames — a metric cannot see a third arm.

## O · Editing rules that survive 4 s shots

1. Cut when the information changes, not when the clip ends.
2. Never cut twice in the same direction without a beat between.
3. 30° rule: two consecutive shots of the same subject need a real change of angle
   (different prompt = different angle, so plan it).
4. Match cut: end shot A on a shape and open shot B on a similar shape (lamp → moon, ring →
   window). With chaining, the match is nearly free.
5. Last shot of a scene holds longer than the others. Since length is fixed at 4.03 s,
   hold it by repeating a still (Ken Burns) or by adding a beat of black.
