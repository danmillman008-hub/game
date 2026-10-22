# Architecture — what is reused, and where

The rule for this prototype was: **the verified code is on the real game path, not next to
it.** Every position, box, collision test and screen coordinate below comes out of
`components/sor_engine/`. The game adds no second implementation of any of it.

```
main.py  (window, 60 Hz accumulator, input)
   │  Command(move_x, move_z, jump, punch, kick)
   ▼
game.py  Game.update() ────────────────────────────────────────────────┐
   │   player/enemy state, attacks, waves, rules                        │
   ▼                                                                   │
entities.py  Fighter (owns one components.sor_engine.Actor)            │
   │                                                                   │
   ▼                                                                   │
adapter.py   thin pass-through + call counters   ◄── every call below  │
   │                                                                   │
   ▼                                                                   │
components/sor_engine/  fixed.py · kinematics.py · boxes.py · projection.py
   │                                                                   │
   ▼                                                                   │
render.py  — world→screen via adapter.project() only ──────────────────┘
```

`adapter.py` is the *only* file that imports `components.sor_engine`. It is deliberately
thin: each function is one line of forwarding plus a counter. There is no constant
re-declared there and no arithmetic re-done there — `prototype/tests/test_components.py`
asserts the imported functions are the same objects the components module exports
(`assertIs`), and then monkey-patches them to prove the game actually goes through them.

---

## 1. Reused component by component

| # | Reused behaviour | ROM routine | Component API | Where the game calls it |
| --- | --- | --- | --- | --- |
| 1 | **Fixed-point world** (`hi16`, `s32`) | — (data conventions) | `fixed.hi16`, `fixed.s32` | `entities.py:97,101,105` (`wx/wz/wy`), `game.py` bounds writes |
| 2 | **Frame integration + freeze predicate** | `$00442C` | `kinematics.integrate` (+ `is_frozen` inside it) | `game.py:145,151,182,195,213,219,253` — every actor, every frame |
| 3 | **Neutral gravity** (rising, walking jump) | `$00389A` → `add.l #$E800` | `kinematics.neutral_gravity` | `game.py:174` (player `air_mode="neutral"`), `game.py:193` |
| 4 | **Directional gravity** (descending) | `$0038AE` → `add.l #$8800` | `kinematics.directional_gravity` | same call sites; the branch is inside the component |
| 5 | **Terminal velocity clamp** | `$003886` → `cmpi.l #$C0000` | `kinematics.clamp_terminal_velocity` | `game.py:176,194` |
| 6 | **Air control** | `$0038C0` → `±$6000`, `|vx| ≤ $38000`, facing side effects | `kinematics.air_control` | `game.py:175` |
| 7 | **ROM-derived body boxes** | `$004140` + `components/data/body_boxes.json` (32 records) | `boxes.build_player_boxes`, `BoxTables.load` | `entities.py:108` (`boxes()` → `body_box()`), used by every hit test and body push |
| 8 | **AABB body collision** | `$00450C` | `boxes.aabb_overlap` | `game.py:274` (player→enemy), `game.py:283` (enemy→player), `game.py:332` (body-vs-body push-apart) |
| 9 | **World→screen projection** | `$00AF46` | `projection.project` | `render.py:142` (sprite position), `render.py:138` (shadow ground point, Y=0), `render.py:396` (impact effects) |
| 10 | **Sprite culling** | `$00AF46` bounds test | same `projection.project` return value | `render.py:142-146` — a culled actor is not drawn at all |

Notes that matter for honesty:

- **(2) The freeze predicate** is evaluated *inside* `integrate` on every call. The game
  additionally *uses* the return value: when $00442C suppresses a step, the game does not
  treat it as a landing (`game.py:182-190`). `test_frozen_actor_is_not_integrated_and_does_not_land`
  sets the real engine freeze state and proves it.
- **(5) The clamp is one-sided** — it only limits downward speed, exactly as the ROM does.
  The prototype does not add an upward limit.
- **(7) The tables are the ROM-derived file**, not a copy: `adapter.tables()` loads
  `components/data/body_boxes.json` (asserted: 32 records). The two regression anchors used
  in Stage 2 still hold inside the prototype:
  player at `(100, 60)` → `(97, 111, 52, 68, -42, 0)`; enemy at `(200, 60)` → `(197, 207, 52, 68, -50, 0)`.
- **(9) There is no second screen formula.** `render.py` contains no `+$80`, no `>>1` and no
  camera arithmetic; it asks `project()` for `(sx, sy, culled)` and blits there.

## 2. The one place a game constant meets a ROM constant

`project()` returns `sx = X_hi + $80 − cam_x` and culls at `sx ≥ $500` / `sy ≥ $200`, i.e. it
was written for a **320×256** viewport. The prototype therefore renders a **384×240 virtual
canvas** and integer/`smoothscale`-upscales it to the window, instead of choosing a large
canvas and fighting the cull window. The camera anchor (`CAM_ANCHOR_X = 128`) and the arena
bounds are `[INTEG]`/`[PROTO]` choices tuned so that the playable band (`sx ≈ 176…336`,
`sy ≈ 138…213`) sits inside the verified window. Nothing in `projection.py` was changed, and
`test_projection_is_the_only_screen_mapping` fails if the renderer ever stops calling it.

Vertical placement is worth stating explicitly because it looks unusual on a modern canvas:
with the ROM's `sy = (Z_hi >> 1) + Y_hi + $80`, a whole 150-unit depth range maps to 75
screen pixels. That is the recovered projection behaving as verified; the prototype adapts
its *art scale* (44 px fighters) to it, not the formula.

## 3. Ordering, exactly as in `reconstruction/slice_runner.py`

Airborne frame (player), `game.py:170-181`:

```
gravity(actor, mode)  →  air_control(actor)  →  clamp_terminal_velocity(actor)  →  integrate(actor)
```

Grounded frame: `integrate(actor)` only. Dead-falling frame: `gravity("directional")` →
`clamp_terminal_velocity` → `integrate`.

Body boxes are rebuilt from the component every time they are needed (no cached copy), so a
box can never disagree with the actor's current fixed-point position.

## 4. Why combat hitboxes are *not* ROM data

Attack rectangles are prototype data (`config.ATTACKS`, `[PROTO]`): a reach/depth/height
rectangle in front of the attacker. They are deliberately **separate** from the ROM body
boxes and are tested to differ (`test_attack_box_differs_from_body_boxes`,
`test_hit_requires_attack_box_overlap_not_body_overlap`). The *overlap test itself* is the
verified `$00450C` predicate — the prototype supplies the rectangle, the engine decides
whether rectangles touch.

The Stage-2 research did not recover the original hit-reaction tables (`U-CBT-01`), so no
hitstun, knockback, armour or i-frame number in this prototype claims ROM parity. See
`RULES.md`.

## 5. Frame pipeline

```
main.py
  clock.tick(60) → dt
  accumulate dt; while accumulator >= 1/60: game.update(Command)   (max 5 steps/frame)
  Renderer.draw(game, t) → 384×240 Surface
  smoothscale to the largest 16:10 rectangle that fits the window, centred, letterboxed
  flip
```

The simulation is a pure function of the command sequence: same inputs → same frames, bit for
bit (`test_two_runs_are_bit_identical`, `test_replay_is_deterministic`). Rendering never
mutates game state (`test_recorded_encounter_result` compares an unrendered and a rendered run
in `tools/measure_components.py`: identical outcomes).

## 6. Entity ownership

```
Fighter
├─ body : components.sor_engine.Actor    ← position, velocity, buttons, +$30 state, +$59 flags
│                                          (the verified record: nothing prototype-only lives here)
└─ [PROTO] hp, facing, grounded, attack, hitstun, iframes, knockback, timers, palette, lane
```

Keeping every prototype field *outside* the `Actor` is what makes the boundary checkable: the
engine's record only ever changes through engine functions plus the plain fixed-point fields
(`x`, `z`, `y`, `vx`, `vz`, `vy`) that the game sets at the start of a frame, which is exactly
what the original engine's own state handlers do.
