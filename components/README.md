# Reusable Components — `sor_engine`

Small, dependency-free Python modules implementing **verified** behaviours of the
Streets of Rage engine. They are not a game, not an engine, and not a port: they are
the reusable layer produced by the Stage-2 pipeline, intended to be embedded in any
runtime (Python, C, JS, an engine script) or used as an oracle for a reimplementation.

Everything here is driven by data extracted from the original ROM and is validated by
executing the original routines on an MC68000 core.

```
components/
  sor_engine/
    fixed.py       16.16 helpers with 68000 32-bit wrap semantics
    actor.py       the slice's view of the 128-byte actor record
    kinematics.py  gravity, terminal clamp, air control, integration
    boxes.py       body-box construction from ROM tables + AABB predicate
    projection.py  world→screen + cull window
  data/
    body_boxes.json  extracted tables + provenance (ROM SHA-256, offsets)
```

## Quick start

```python
from components.sor_engine import Actor, BoxTables, neutral_gravity, integrate, build_player_boxes

t = BoxTables.load()                       # reads data/body_boxes.json
a = Actor(x=983040, z=524288, y=0, vy=-491520, sprite_w=4, sprite_h=2)
neutral_gravity(a); integrate(a)
primary, secondary = build_player_boxes(a, t)
```

No third-party packages are required. The data file is loaded lazily.

## Module contracts

### `fixed.py`
| Function | Contract |
|---|---|
| `s32(v)` | wrap to signed 32 bits (models `add.l`) |
| `hi16(v)` | signed high word — the engine's whole-pixel read |
| `s16(v)` | wrap to signed 16 bits (models `add.w` box arithmetic) |

### `actor.py` — `Actor`
A **slice** of the record, not a full model. Positions/velocities are normalised to
signed 32-bit on construction. `buttons` is the **held** byte (`+$54`); the pressed
edge (`+$55`) is not modelled. `anim_offset` is the word at `+$08`; bit1 of its low
byte is the flag air control touches.

### `kinematics.py`
| Function | Mutates | Invariant |
|---|---|---|
| `neutral_gravity(a)` | `a.vy` | adds exactly `0xE800`, wrapping |
| `soft_gravity(a)` | `a.vy` | adds exactly `0x3800` |
| `directional_gravity(a)` | `a.vy` | sign tested **before** the add |
| `clamp_terminal_velocity(a)` | `a.vy` | one-sided: only lowers a `vy >= 0xC0000` |
| `air_control(a)` | `a.vx`, `a.state` bit0, `a.anim_offset` bit1 | returns whether a direction was held; skips the clamp when it was not |
| `integrate(a)` | `a.x/a.z/a.y` | returns `False` and changes nothing when frozen |

### `boxes.py`
* `BoxTables.load()` / `BoxTables(z_pairs, records)`
* `BoxTables.build(actor, index)` → `Box` (corner+extent arithmetic, 16-bit wrap)
* `build_player_boxes(actor, tables, at_p1_base=False)` → `(primary, secondary)`
* `aabb_overlap(a, b)` → `bool`, inclusive on all three axes

`Box.as_tuple()` returns `(x1, x2, z1, z2, y1, y2)` in the record's own order.

### `projection.py`
* `project(actor, cam_x, cam_y, police_active=False)` → `(sx, sy, culled)`
  with 16-bit signed coordinates.

## Failure conditions and unsupported cases
| Condition | Behaviour | Why |
|---|---|---|
| box index > 31 | `IndexError` | the ROM reads adjacent ROM bytes; undefined, deliberately not modelled |
| actor type/fields outside the documented slice | ignored | fields not in this slice are not interpreted |
| non-integer inputs | not supported | the engine is integer-only |
| `+$54` supplied as a word | wrong results | pass the held **byte** (0x00–0xFF) |
| expecting game logic | none here | no state machine, no combat, no rendering |

## Invariants
1. One call = one original frame; there is no delta time.
2. All arithmetic wraps exactly like the 68000 (`s32`/`s16`), never Python bigints.
3. Components never read ROM at runtime; the only external artifact is the JSON data.
4. `build_player_boxes` depends on the actor's **long address** (`at_p1_base`) because
   the original routine tests `cmpa.w #$B800` against it.

## Reusability
| Reusable as-is | Game-specific |
|---|---|
| 16.16 fixed-point helpers | the exact gravity constants and clamps |
| frame-stepped integration pattern | the freeze predicate's magic state `$14` |
| corner+extent AABB construction | the two ROM tables |
| inclusive AABB predicate | the half-depth projection and cull window |
| cull-window logic | type `$05` special case |

The *patterns* generalise; the *numbers* are this game's. Any port must take the
numbers from `data/body_boxes.json` (which carries the ROM hash) rather than
hard-coding them a second time.

## Evidence and tests
* `BEHAVIORAL_SPECIFICATIONS/WS-01…WS-04`
* `tests/test_component_spec.py` — 24 spec-level tests, no emulator
* `tests/test_differential_rom.py` — 7,740 exact comparisons against the ROM
* `DIFFERENTIAL_VALIDATION.md` — discrepancies found during development
