# WS-04 — Frame Composition of the Slice

**Status:** implemented (`reconstruction/slice_runner.py`) and validated end-to-end.
**Tests:** `D8` (140 frame-steps across 4 scenarios), `test_component_spec.py`.
**Evidence:** `EV-S2-FRM-01`, `EV-S2-FRM-02`.

---

## 1. Purpose and scope
Define the exact order in which WS-01…WS-03 are applied to produce one frame of
player motion and geometry. This is the part that makes the components a
*reconstruction* rather than four independent functions.

Scope: one player actor, no state machine, no collision response, no rendering.

## 2. Inputs and preconditions
A scenario supplies the initial actor fields, a per-frame plan
(`gravity` variant, optional `air_control`, held `buttons`, camera) and a frame count.
The plan stands in for the state machine: in the real game the state handler decides
which gravity variant runs and whether air control is evaluated.

## 3. State variables
The union of WS-01…WS-03 fields, plus the derived `+$28`/`+$2C`.
`Actor` normalises `x,z,y,vx,vz,vy` to signed 32-bit on construction, mirroring memory.

## 4. Data formats
As WS-01. Scenario files are JSON; integers are raw 16.16 values (no floats), so
scenarios are exact and diffable.

## 5. Algorithm (one frame)
```
a.buttons = plan.buttons                    # +$54
1. gravity(a)                               # $00389A / $0038A6 / $0038AE
2. if plan.air_control: air_control(a)      # $0038C0
3. clamp_terminal_velocity(a)               # $003886
4. integrate(a)                             # $00442C
5. primary, secondary = build_boxes(a)      # $004140
6. sx, sy, culled = project(a, cam)         # $00AF46
   if not culled: a.screen_x, a.screen_y = sx, sy
```
Steps 1–2 happen inside the state handler; 3–4 in the player skeleton; 5 later in the
same skeleton; 6 in the sprite pass after all actors have run.

## 6. Edge cases
* Frozen actor: step 4 is a no-op, but 5 and 6 still run (boxes and screen position
  track the *unchanged* position).
* Air control with no direction held: no velocity change, but the clamp is skipped.
* Culled actor: screen fields retain the previous frame's values.

## 7. Outputs
A per-frame trace of positions, velocities, screen coordinates, cull flag, both boxes,
state byte and animation offset. This is the comparison surface for `D8`.

## 8. Dependencies
WS-01 → WS-02 → WS-03 in that order. The tables JSON must match the ROM hash recorded
in its provenance block.

## 9. Timing
Frame-locked. No delta time exists anywhere in the original engine; a "tick" is one
pass of `$00AD8E`/`$00AE4C`.

## 10. Revision differences
None: every routine in the chain is byte-identical across REV 00/01.

## 11. Evidence
`EV-S2-FRM-01` (call order, `$001C44` + `$00ADD2–$00ADDC`), `EV-S2-FRM-02`
(per-frame equivalence, `D8`).

## 12. Unresolved / confidence
Composition order: **CONFIRMED**. The scenario *plans* are a deliberate abstraction:
they encode which variant a state uses, and that mapping is only `HIGH` confidence
outside the jump states. The slice therefore claims fidelity **conditional on the
plan**, and D8 verifies exactly that conditional claim.

## 13. Test cases
Scenarios shipped in `reconstruction/scenarios/`:
| Scenario | Frames | What it exercises |
|---|---|---|
| `neutral_jump` | 40 | neutral gravity, full arc, box rebuild while airborne |
| `directional_jump_left` | 40 | directional gravity, air control left, camera offset |
| `frozen_hold` | 10 | freeze predicate (state `$14` + `$59` bit7) |
| `launched_descent` (in tests) | 50 | non-zero Z velocity, pre-existing height |

All four are compared field-by-field against the ROM in `D8`; 140 frame-steps, zero
divergence.
