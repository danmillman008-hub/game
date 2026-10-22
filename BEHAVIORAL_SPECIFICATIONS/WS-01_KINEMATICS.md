# WS-01 — 2.5D Kinematics (gravity, terminal velocity, air control, integration)

**Status:** implemented and differentially validated against the original ROM.
**Component:** `components/sor_engine/kinematics.py`
**Tests:** `tests/test_component_spec.py` (Gravity, AirControl, Integration), `tests/test_differential_rom.py::D1–D4`, `tests/test_recovered_behaviour.py`
**Evidence:** `EV-S2-KIN-01…05`; ROM `REV 00` (`dd44f120…`); addresses below are ROM file offsets.

---

## 1. Purpose and scope
Reproduce the per-tick motion of an actor's three 16.16 axes (X, Z depth, Y height)
and the four independent modifiers the engine applies to them: two gravity variants
plus a soft variant, a one-sided terminal-velocity clamp, and horizontal air control.

Out of scope: state selection (which gravity applies is a function of the state
handler, not of this module), wall/proximity push-out, terrain height, and the
"launched"/knockback decelerator.

## 2. Inputs and preconditions
* Actor record with `+$10/+$14/+$18` positions, `+$1C/+$20/+$24` velocities, `+$30`
  state byte, `+$54` held-buttons byte, `+$08` animation-offset word, `+$59` flags.
* No precondition on alignment, velocity range or position; the routines are total
  over all 32-bit inputs.
* The caller must apply the steps in the order in §9.

## 3. State variables and meanings

| Field | Size | Meaning | Confidence |
|---|---|---|---|
| `+$10` | 32-bit 16.16 | X, pixels along the walkable axis | CONFIRMED |
| `+$14` | 32-bit 16.16 | Z, pixels into the screen ("depth") | CONFIRMED |
| `+$18` | 32-bit 16.16 | Y, pixels up; **negative = above the floor** | CONFIRMED |
| `+$1C` | 32-bit 16.16 | X velocity | CONFIRMED |
| `+$20` | 32-bit 16.16 | Z velocity | CONFIRMED |
| `+$24` | 32-bit 16.16 | Y velocity / gravity accumulator | CONFIRMED |
| `+$30` | byte | state id; **bit0 = facing left** | CONFIRMED (bit via `$0038C0`) |
| `+$54` | byte | **held** pad state, active-high | CONFIRMED (`$00ADE8`, `$00813C`) |
| `+$08` | word | animation-block offset; used by the freeze test | CONFIRMED |
| `+$59` | byte | bit7 = "throw/held lock" for the freeze test | CONFIRMED for the predicate |

## 4. Data formats, units and conventions
All positions and velocities are **signed 32-bit 16.16** (`1.0 = 0x00010000`).
Arithmetic wraps modulo 2³². Whole-pixel reads are the **signed high word**.
There is no delta time: one call = one frame. Screen mapping is in WS-03.

## 5. Algorithms, equations, ordering

### 5.1 Gravity variants
```
$00389A neutral:      vy += 0x0000E800          (+0.90625 px/tick²)
$0038A6 soft:         vy += 0x00003800          (+0.21875 px/tick²)
$0038AE directional:  if vy < 0: vy += 0x0000E800     (sign tested BEFORE the add)
                      else:     vy += 0x00008800     (+1.0625 px/tick²)
```
The sign test precedes the addition, so the tick on which `vy` crosses zero still
receives the neutral increment.

### 5.2 Terminal-velocity clamp (`$003886`)
```
if vy >= 0x000C0000: vy = 0x000C0000      // one-sided; no lower bound
```
Because the comparison is signed, values ≥ `0x80000000` are unaffected.

### 5.3 Air control (`$0038C0`)
```
if   held & 0x08 (RIGHT):  state.bit0 = 0 ; anim.bits_lowbyte.bit1 = 0 ; d = +0x6000
elif held & 0x04 (LEFT):   state.bit0 = 1 ; anim.bits_lowbyte.bit1 = 1 ; d = -0x6000
else: return without touching vx, state, anim or the clamp
vx += d
if vx < -0x38000: vx = -0x38000
elif vx > 0x38000: vx =  0x38000
```
Right is tested first, so a pad reporting both directions moves **right**.
The facing/animation side effects happen **before** the velocity update. The clamp
lives inside the taken branch: with no input, an out-of-range `vx` is left alone.

### 5.4 Integration (`$00442C`)
```
if (anim_offset & 0xFF00 | anim_offset & 0x00FC) == 0x0014 and (flags_59 & 0x80):
        return frozen                       # no position changes at all
flags_59 &= 0xFF                            # a no-op, preserved for fidelity
x += vx ; z += vz ; y += vy                 # three independent 32-bit adds
```
**Trap:** `andi.b #$FC` masks the low byte only, while `cmpi.w #$14` compares the
whole word. `+$08 = $0114` does **not** freeze; `+$08 = $0017` **does**.

## 6. State transitions and edge cases
* The module never changes `+$30` except bit0 (air control). No state machine here.
* Freeze is re-evaluated every tick and is not sticky.
* Air control may be applied while frozen; the freeze only suppresses integration.
* Zero-length vectors, saturation, and negative zero are all ordinary values.

## 7. Outputs and observable side effects
* Updated `+$18`/`+$24` (gravity, clamp), `+$1C` plus `+$30``/`+$09` (air control),
  `+$10/+$14/+$18` (integration).
* No memory outside the actor record is touched by these routines.

## 8. Dependencies
* Reads nothing else; safe to call on any actor type.
* Callers: state handlers `$001FDC` (neutral), `$002006` (directional), `$002128`,
  `$002174`, `$002A10`, `$002ADC`, `$002B10`, `$002B38` (neutral/soft variants).
* Depended on by WS-02 (box positions) and WS-03 (projection).

## 9. Timing and update order (authoritative)
```
state handler:  gravity variant   ($00389A / $0038A6 / $0038AE)
                air control       ($0038C0)        [only in some states]
player loop:    clamp             ($003886)         <- $001CA2
                integrate         ($00442C)         <- $001CA6
                rebuild boxes     ($004140)         <- $001CC6
sprite pass:    project + cull    ($00AF46)
```
Gravity **before** integration is the single most consequential ordering fact in
this specification; §C-7 of `AUDIT_REPORT.md` shows what happens when it is reversed.

## 10. Revision differences
The entire byte range `$003886–$003912`, `$00442C–$004460` and every gravity call site
listed in §8 is **byte-identical** in REV 00 and REV 01. The Stage-2 slice is
therefore revision-independent. (The two images differ in 2,092 bytes total, all in
the master header and `$0143FB–$014DAF`.)

## 11. Evidence references
| Claim | Evidence |
|---|---|
| gravity constants and order | `EV-S2-KIN-01`, disassembly `$00389A–$0038BE`; `D1` (900 executed cases) |
| one-sided clamp | `EV-S2-KIN-02`, `$003886`; `D2` (208 cases incl. boundaries) |
| air control semantics + side effects | `EV-S2-KIN-03`, `$0038C0–$003912`; `D3` (400 cases) |
| freeze predicate | `EV-S2-KIN-04`, `$00442C`; `D4` (409 cases) |
| jump consequences | `EV-S2-KIN-05`; `D9`; `evidence/stage2/stage2_verification.json` |

## 12. Unresolved behaviour and confidence
* **CONFIRMED** for every rule above (static + executed, exact equality).
* Per-character launch velocities are *data* (animation blocks), not recovered here;
  they are inputs to this module, supplied by the scenario.
* Which state selects which gravity variant is only partially enumerated:
  `HIGH` for the jump states, `PROBABLE` elsewhere.
* The meaning of `+$09` bit1 as an animation flag is `PROBABLE` (the write is FACT).

## 13. Independent test cases and expected results
| # | Initial | Operation | Expected |
|---|---|---|---|
| T1 | `vy=0` | neutral gravity | `vy = 0x0000E800` |
| T2 | `vy=-1` | directional gravity | `vy = 0x0000E7FF` (neutral branch) |
| T3 | `vy=0` | directional gravity | `vy = 0x00008800` |
| T4 | `vy=0xC0001` | clamp | `vy = 0x000C0000` |
| T5 | `vy=-0x900000` | clamp | unchanged |
| T6 | `held=0x08, vx=0` | air control | `vx=0x6000`, facing bit cleared, anim bit1 cleared |
| T7 | `held=0x0C, vx=0` | air control | `vx=0x6000` (right wins) |
| T8 | `held=0, vx=0x90000` | air control | unchanged `0x90000` |
| T9 | `+$08=0x0014,+$59=0x80` | integrate | positions unchanged |
| T10 | `+$08=0x0114,+$59=0x80` | integrate | positions advance normally |
| T11 | `v0=-7.5 px/t`, neutral, 60 ticks | gravity+clamp+integrate | airtime 15, apex −27.375 px |
| T12 | `v0=-7.5 px/t`, directional | same | airtime 17, apex −27.375 px |
