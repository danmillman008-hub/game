# WS-03 — World→Screen Projection and Sprite Culling

**Status:** implemented and differentially validated.
**Component:** `components/sor_engine/projection.py`
**Tests:** `tests/test_component_spec.py` (Projection), `D7` (1,016 cases)
**Evidence:** `EV-S2-PRJ-01…03`

---

## 1. Purpose and scope
Convert world (X, Z, Y) into screen coordinates for the sprite builder, and decide
whether an actor is drawn at all. Excludes sprite mapping, Y-sorting and VRAM writes.

## 2. Inputs / preconditions
`X_hi`, `Z_hi`, `Y_hi` (integer pixels), `+$00` type id, `+$01` flags, camera words
`$FFE002` (X) and `$FFE00E` (Y), and the police latch `$FFFA1A`.

## 3. State variables
| Field | Meaning | Confidence |
|---|---|---|
| `+$28` | screen X (word) | CONFIRMED |
| `+$2C` | screen Y (word) | CONFIRMED |
| `+$01` bit1 | screen-fixed actor (no camera subtraction) | CONFIRMED |
| `+$01` bit3 | skip culling entirely | CONFIRMED |
| `+$00` == 5 | type with the wide left cull margin | CONFIRMED (rule), role PROBABLE |

## 4. Data formats
16-bit signed words. Ceiling is pseudo-3D: depth raises the sprite by **half** its value.

## 5. Algorithm (`$00AF46–$00AFC2`)
```
sx = s16(X_hi + 0x80)
sy = s16((Z_hi >> 1) + Y_hi + 0x80)        # >>1 is an arithmetic shift
if not (+$01 & 0x02):
    sx = s16(sx - cam_x)
    sy = s16(sy - cam_y)

if type == 5:            margin = -128 ; goto bounds      # always culled
elif (+$01 & 0x08) or $FA1A != 0:  return (sx, sy, not_culled)
else:                    margin = -896

culled = sx >= 1280 or sx < margin or (u16)sy >= 512 or (u16)sy < 16
```
The vertical test is **unsigned**, so a small negative `sy` (e.g. −1 → 65535) is
culled by the `>= 512` branch rather than accepted.

## 6. Edge cases
| Case | Result |
|---|---|
| `sx == 1279` | drawn; `sx == 1280` → culled |
| `sy == 15` | culled; `sy == 16` drawn; `sy == 511` drawn; `sy == 512` culled |
| `sy` negative | culled (unsigned compare) |
| type 5 + bit3 set + police active | **still culled** (type test wins) |
| any type with `$FA1A != 0` | never culled |

When culled, `+$28`/`+$2C` keep their previous values; they are not zeroed.

## 7. Outputs
`+$28`, `+$2C` written only on the non-culled path; returns the cull decision.
Side effect: `$FA40` receives a byte read from the animation bank (`$00AF5A`) — part
of the sprite path, not modelled here.

## 8. Dependencies
Camera values come from the camera system (`$018AF8` region, not in this slice);
`+$01`/`+$00` come from the sprite/animation builder.

## 9. Timing
Sprite pass `$00AE4C`, after all actor dispatch. Projection therefore sees the final
post-integration positions of the frame.

## 10. Revision differences
`$00AF46–$00AFC2` is byte-identical in REV 00/REV 01.

## 11. Evidence
`EV-S2-PRJ-01` (formula, `$00AF60–$00AF72`), `EV-S2-PRJ-02` (camera exception,
`$00AF76`), `EV-S2-PRJ-03` (cull rules, `$00AF86–$00AFBE`); all exercised by `D7`,
which includes both camera modes and the police latch.

## 12. Unresolved / confidence
Formula and rules: **CONFIRMED**. Why type 5 is special: **UNKNOWN** (it is the only
type that bypasses the skip branches; the type table entry is a HUD/effect handler).
Exact semantics of `$FA40`: out of scope.

## 13. Test cases
| # | Input | Expected |
|---|---|---|
| P1 | X=1000, Z=500, Y=−20, cam 0/0 | `sx=1128, sy=358` |
| P2 | same, cam 300/100 | `sx=828, sy=258` |
| P3 | same + `+$01` bit1, cam 300/100 | `sx=1128, sy=358` |
| P4 | X=2000 | culled |
| P5 | Y=300, Z=500 | `sy = 678` → culled (>= 512) |
| P6 | type 5, X=−400, police active | culled |
| P7 | type 1, X=−400, bit3 set | not culled |
