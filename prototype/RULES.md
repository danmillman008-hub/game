# Rules of Neon Alley — and where each rule comes from

Three categories, never mixed:

- **[ROM]** — recovered from the original engine, executed against the original MC68000 code
  during Stage 2, and consumed from `components/sor_engine/` without modification.
- **[INTEG]** — an integration choice: how this game wires verified pieces together (order of
  calls, canvas size, camera anchor). It does not claim to be original behaviour.
- **[PROTO]** — a rule invented for this game. It has **no** bearing on the Stage-2
  behavioural specifications and must never be cited as evidence about the original game.

---

## 1. [ROM] rules consumed from the reconstructed engine

| rule | value / behaviour | source |
| --- | --- | --- |
| Rising gravity | `+$E800` (`+0.90625` px/tick²) | `$00389A`, differential scenario D3 |
| Descending gravity | `+$8800` (`+1.0625` px/tick²) | `$0038AE`, D3 |
| Terminal velocity | `vy` clamped at `$C0000` (one-sided) | `$003886`, D3 |
| Air control | `±$6000` per tick, `|vx| ≤ $38000`, writes facing into bit0 of `+$30` | `$0038C0`, D4 |
| Integration | `x += vx`, `z += vz`, `y += vy`, all 32-bit two's complement | `$00442C`, D5 |
| Freeze predicate | `(anim_offset & $FC) == $14` **and** bit7 of `+$59` → do not integrate | `$00442C`, D5 |
| Body boxes | `x1 = X_hi + b0`, `x2 = x1 + b1`; `z1 = Z_hi + z[b2][0]`, `z2 = z1 + z[b2][1]`; `y1 = Y_hi + b3`, `y2 = y1 + b4` | `$004140`, `components/data/body_boxes.json`, D6 |
| AABB test | inclusive on all three axes | `$00450C`, D6 |
| Projection | `sx = X_hi + $80 − cam_x`, `sy = (Z_hi >> 1) + Y_hi + $80 − cam_y` | `$00AF46`, D7 |
| Cull window | `sx ≥ $500`, `sx < $FF80`, `sy < $10`, `sy ≥ $200` all cull | `$00AF46`, D7 |
| Frame composition | gravity → air control → clamp → integrate | `reconstruction/slice_runner.py`, D8 |

Jump **launch** velocity is the one ROM-sourced number used directly by the prototype rather
than through a component: `JUMP_VY = −$78000` (−7.5 px/tick), the launch measured in Stage 2.
That value is written into the actor; everything that happens afterwards is the component chain.

## 2. [INTEG] wiring choices

| choice | value | why |
| --- | --- | --- |
| Virtual canvas | 384×240, upscaled | the verified cull window is ~320×256; a large canvas would silently cull the player |
| Camera anchor | `CAM_ANCHOR_X = 128` → player sits at `sx ≈ 256` | keeps the player inside the cull window at both arena ends |
| Arena | `X 48…1360`, `Z 20…170` | `Z` maps to `sy 138…213`: a playable depth band under the HUD, inside the window |
| Ground snap | after `integrate`, if airborne and `y ≥ 0` on a descending frame → `y = 0`, `vy = 0`, mark grounded | the engine integrates but does not know about this game's single floor plane |
| Actor ↔ actor push | resolve the smaller overlap axis, weight 0.25 / 0.75 versus the player, 0.5 / 0.5 between enemies | keeps bodies from stacking; the *test* is still `$00450C` |
| Camera | follow the player at the anchor, ±12 px/frame | smooth, deterministic, no interpolation state |
| Shadow | re-project the same spot with `Y = 0` | the shadow uses the verified projection twice, not a second formula |
| Draw order | sort by `Z`, then `Y`, then id | depth-aware ordering |

## 3. [PROTO] rules invented for this game

### Movement

| rule | value |
| --- | --- |
| Walk speed | `$24000` (2.25 px/frame) with `$0C000` acceleration |
| Depth speed | `$18000` (1.5 px/frame), no acceleration |
| Jump | launch `−$78000` (ROM value), then the ROM chain |
| Air control | available while `A`/`D` is held; no double jump |
| Arena bounds | hard clamp on `X` and `Z`; actors never leave the street |

The ROM's per-character walk speeds live in animation data that Stage 2 did not recover, so
the values above are new tuning and are tagged `[PROTO]` in `config.py`.

### Attacks

| attack | startup | active | recovery | damage | reach | depth | hitstun | knockback | lunge | cooldown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| punch `J` | 3 | 3 | 7 | 7 | 34 | 22 | 11 | `$18000` | `$08000` | 5 |
| kick `K` | 8 | 5 | 16 | 13 | 46 | 26 | 18 | `$30000` | `$04000` | 9 |
| enemy swing | 16 | 4 | 22 | 8 | 38 | 24 | 14 | `$20000` | `$0C000` | 0 |

All frame counts are at the fixed 60 Hz step.

- **Phases** — a hit can only land during *active* frames.
- **Direction** — the attack rectangle is placed in front of the attacker (`facing`).
- **Depth** — a separate `depth` band around the attacker's `Z`; attacks miss an enemy in a
  different lane, and `test_wrong_depth_punch_misses` holds that to account.
- **Per-attack hit tracking** — every attack instance owns a `hit_ids` set, so one swing deals
  damage at most once per target, however many active frames overlap.
- **Cooldown** — after recovery a short cooldown prevents held-key spam.
- **Lunge** — a small forward drift during startup/active so a near-miss still closes the gap.

### Damage, reactions, defence

| rule | value | note |
| --- | --- | --- |
| Player health | 80 | `$50`, chosen for familiarity with the original's maximum |
| Enemy health | 30 (thug), 42 (brute) | |
| Player i-frames after a hit | 26 frames, blinking | |
| Enemy **armour** | an enemy swing cannot be interrupted during its own startup/active frames; it still takes damage, and gets half the i-frames | added after measuring that a single fast punch stun-locked the whole encounter (autopilot took 0 damage in 791 frames) |
| Hit-stop | 3 frames punch, 5 kick, 3 enemy | freezes gameplay frames, not effects or HUD |
| Screen shake | 4 px punch, 6 px kick | |
| Knockback | horizontal impulse with `$5000` decay per frame while in hitstun | |
| Death | 46-frame fall animation, then removal | |

`U-CBT-01` (**unresolved**) covers the original game's hit-reaction and stun rules. Nothing in
this section is a claim about them.

### Enemies and flow

| rule | value |
| --- | --- |
| Enemy speed | walk `$1A000` (1.625 px/frame), depth `$14000`, acceleration `$08000` |
| Engage distance | 30 px in `X`, 6 px in `Z` |
| Lane preference | −10 / 0 / +10 px offset per enemy, so they fan out instead of stacking |
| Attack gate | one enemy may be in an attack at a time (a global token) |
| Cooldown | 36 frames after a swing, 36–64 initial delay per enemy |
| Spawn delay | 18 frames after a wave spawns |
| Waves | 2 thugs, then 1 brute; 70-frame breather between waves |
| Victory | last wave cleared → 45-frame hold → `VICTORY` |
| Defeat | player health 0 → 46-frame fall → `DEFEAT` |
| Restart | `R` → `reset()` + `start()`; ids, counters and effects reset |
| RNG | none. The game never imports `random`; ties break on actor id |

### Presentation

Purely cosmetic, `[PROTO]`: procedural skyline with parallax, neon signs, lane markings drawn
at the *same* `sy = (Z >> 1) + $80` the projection uses, scanlines, vignette, spark/ring/dust/
KO particles, floating damage numbers, HUD, title and end cards.

## 4. What this prototype does **not** claim

- It is not the original game, a remake, or a port — see `COMPLETION_REPORT.md` §1.
- Prototype AI, health, waves, attack frame data and hit reactions are new. Only the physics,
  box construction, collision predicate, projection and culling are recovered behaviour.
- Two Stage-2 open questions remain open and are untouched here: `U-CBT-01` (hit reactions)
  and `U-GRAV-01` (which state uses soft gravity `$38A6`). Soft gravity is implemented in the
  component but this prototype never selects it, so it is honest to say it is *not* exercised.
