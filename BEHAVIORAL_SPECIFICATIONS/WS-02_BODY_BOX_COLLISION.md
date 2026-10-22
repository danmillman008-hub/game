# WS-02 — Body Boxes and AABB Overlap

**Status:** implemented and differentially validated.
**Component:** `components/sor_engine/boxes.py`, data `components/data/body_boxes.json`
**Tests:** `tests/test_component_spec.py` (Boxes, AABB), `D5` (4,160 cases), `D6` (507 cases)
**Evidence:** `EV-S2-BOX-01…04`

---

## 1. Purpose and scope
Rebuild, every frame, the two axis-aligned boxes a player carries, and decide whether
two boxes overlap. This is the geometric substrate for body blocking and for the
player-vs-player test; it is **not** the attack/hurt resolution (see §12).

## 2. Inputs and preconditions
* Position high words `X_hi` (`+$10`), `Z_hi` (`+$14`), `Y_hi` (`+$18`) — integer pixels.
* `+$02` = sprite tile-width index, `+$03` = sprite tile-height index (bytes, 0…31).
* `+$4B` bit1 = "invulnerable" (affects only the second box).
* The actor's long address, because the `$B800` special case is address-dependent.

## 3. State variables
| Field | Meaning | Confidence |
|---|---|---|
| `+$64..+$6F` | primary box: six words `x1,x2,z1,z2,y1,y2` | CONFIRMED |
| `+$70..+$7B` | secondary box, same layout | CONFIRMED (new in Stage 2) |
| `+$02` | index for the primary box | CONFIRMED |
| `+$03` | index for the secondary box | CONFIRMED |
| `+$4B` bit1 | forces the secondary box to the null form | CONFIRMED |

## 4. Data formats
Six **signed 16-bit words** per box, in pixel units, world space (not screen space).
Construction uses 16-bit `move.w`/`add.w`, so results wrap at 16 bits.
Tables (extracted verbatim into `body_boxes.json`):

* `$01AB8E` — 13 × 2 signed bytes: `[z_corner, z_extent]`
* `$01ABA8` — 32 × 5 signed bytes: `[x_corner, x_extent, z_index, y_corner, y_extent]`
  (`z_index` is 0 in every body-box record, so body boxes always use z-pair 0 = `(-8, +16)`)

## 5. Algorithm
```
build(index):
    b0,b1,b2,b3,b4 = record[index]
    x1 = s16(X_hi + b0)        x2 = s16(x1 + b1)
    z1 = s16(Z_hi + zp[b2][0]) z2 = s16(z1 + zp[b2][1])
    y1 = s16(Y_hi + b3)        y2 = s16(y1 + b4)

$004140:
    null_word = 0x0010 if a0 != 0xFFFFB800 else 0x0000

    primary   = build(+$02)                  if +$02 != 0 else filled(null_word)
    if +$4B & 0x02:      secondary = filled(null_word)
    elif +$03 != 0:      secondary = build(+$03)
    else:                secondary = filled(0x0000)
```
`filled(v)` writes the same word six times.

**The extents are cumulative.** `b1`, `z_extent` and `b4` are sizes, not positions.
This is the Stage-2 correction C-1; the Stage-1 dossier had `x2 = X + b1` etc.

### AABB predicate (`$00450C`)
```
overlap = a.z1 <= b.z2 and a.z2 >= b.z1
      and a.x1 <= b.x2 and a.x2 >= b.x1
      and a.y1 <= b.y2 and a.y2 >= b.y1
```
Evaluation order in the ROM is **Z, X, Y**; every comparison is **inclusive**, so
boxes that merely touch are overlapping. The ROM compares *A's primary* box against
*B's secondary* box, and its caller invokes it once per direction.

## 6. Edge cases
| Case | Result |
|---|---|
| `+$02 == 0`, a0 ≠ `$FFFFB800` | primary = `(16,16,16,16,16,16)` |
| `+$02 == 0`, a0 = `$FFFFB800` | primary = `(0,0,0,0,0,0)` |
| `+$03 == 0`, `+$4B` bit1 clear | secondary = `(0,0,0,0,0,0)` |
| `+$4B` bit1 set | secondary = null form above |
| index > 31 | reads adjacent ROM bytes — **undefined behaviour, not modelled** |
| X/Y/Z high word at ±32768 | ordinary signed wrap |

## 7. Outputs
Twelve bytes at `+$64` and twelve at `+$70`, rewritten every frame. No side effects
outside the record. Boxes are **integer-snapped**: sub-pixel motion does not move a
box until the high word changes.

## 8. Dependencies
* Requires WS-01 integration to have run (positions are this frame's).
* Consumed by `$004478` (player↔player) via `$00450C`; the primary box is also the
  natural input to the attack/hurt pass (`$00AB24`), which is **not** in this slice.

## 9. Timing
Called at `$001CC6`, after integration and after the attack-damage/priority helpers,
once per player per frame; the sprite pass runs later.

## 10. Revision differences
`$004140–$0041E8`, `$00450C–$004556`, `$01AB8E–$01ABCE` are **byte-identical**
between REV 00 and REV 01.

## 11. Evidence
| Claim | Evidence |
|---|---|
| two boxes, indices `+$02`/`+$03` | `EV-S2-BOX-01`, `$004140`; `D5` |
| cumulative extents | `EV-S2-BOX-02`, `$0041A6–$0041E6`; `D5` (4,160 cases) |
| null-box rules and `$B800` case | `EV-S2-BOX-03`; `D5` |
| Z,X,Y order + inclusivity | `EV-S2-BOX-04`, `$004514–$00454E`; `D6` |

## 12. Unresolved / confidence
* Construction: **CONFIRMED** (exact, all 32 indices × 65 positions × 2 address classes).
* *Semantic roles* of the two boxes: **PROBABLE**. Evidence: `$450C` compares
  primary-vs-secondary; the builder indexes one by width and one by height. Calling
  them "width box" and "height box" is descriptive, not proven.
* **Not** the attack system: `$00AB24`/`$00AB88` consumes a different table
  (`$01A68E`) and a threshold-record list at `+$72`. Its record semantics are still
  unresolved, so no attack-hitbox claim is made here.

## 13. Test cases
| # | Input | Expected |
|---|---|---|
| B1 | idx 2, X=1000, Z=500, Y=−20 | `(997,1007,492,508,-70,-20)` |
| B2 | idx 4, same | `(987,1000,492,508,-71,-20)` |
| B3 | `+$02=0`, general slot | `(16,16,16,16,16,16)` primary, `(0,…)` secondary |
| B4 | `+$02=0`, `a0=$FFFFB800` | primary `(0,0,0,0,0,0)` |
| B5 | `+$4B=0x02`, `+$03=2` | secondary = `(16,16,16,16,16,16)` |
| B6 | A=`(0,10,0,10,0,10)`, B=`(10,20,0,10,0,10)` | overlap **true** (touching) |
| B7 | A=`(0,10,0,10,0,10)`, B=`(11,20,0,10,0,10)` | overlap false |
