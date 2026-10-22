# Differential Validation — reconstructed slice vs. original ROM

**Question answered:** does the Stage-2 reconstruction produce *bit-identical* results
to the original game code for the behaviours in scope?

**Answer:** yes, for 7,740 independent comparisons and 140 composed frame-steps, with
zero tolerance (exact integer equality). No comparison was relaxed to obtain a pass.

---

## 1. Method

For every rule, the original routine is executed on a **real MC68000 core** (Unicorn,
`UC_CPU_M68K_M68000`) with a synthetic 128-byte actor record. The reconstructed
component receives the same inputs. Outputs are compared as raw words/longs.

```
original ROM routine  ──execute──►  machine state  ─┐
                                                   ├── exact compare ──► PASS/FAIL
component (Python)    ──evaluate─►  Python state   ─┘
```

This is *not* a Python model of a model: the reference side is the cartridge code.
Both sides are driven from the same random seed (`20261022`), so every run is
reproducible and every failure is re-playable.

## 2. Harness

| Piece | File | Role |
|---|---|---|
| `RomProbe` | `tools/rom_probe.py` | maps ROM + RAM (two **aliased** windows), 68000 model, SR `$2700`, sentinel-return `call()` |
| `Oracle` | `tests/rom_oracle.py` | one wrapper per routine; also composes a full frame for scenario tests |
| Tests | `tests/test_differential_rom.py` | D1–D8, with a comparison counter |
| Runner | `tools/verify_stage2.py` | executes everything, writes `evidence/stage2/stage2_verification.json` |

Two harness properties turned out to be essential and are easy to get wrong:
1. `UC_CPU_M68K_M68000` must be selected explicitly; the default model mis-executes
   `dbra`/`move.w sr` idioms.
2. `$00FF0000` and `$FFFF0000` must be **true aliases** of one host buffer. Unicorn has
   no address aliasing, and mapping two independent regions silently makes the 68000's
   sign-extended short-absolute accesses read *different* memory from 32-bit accesses.

## 3. Results

| ID | Subject | Comparisons | Result |
|---|---|---:|---|
| D1 | gravity (`$00389A`, `$0038A6`, `$0038AE`) | 900 | PASS (exact) |
| D2 | terminal clamp (`$003886`) incl. `0xBFFFF/0xC0000/0xC0001/0x80000000` | 208 | PASS |
| D3 | air control (`$0038C0`) incl. side effects on `+$30`/`+$09` | 400 | PASS |
| D4 | integration + freeze (`$00442C`) | 409 | PASS |
| D5 | body boxes (`$004140`), all 32 indices × 65 positions × 2 address classes | 4,160 | PASS |
| D6 | AABB predicate (`$00450C`) incl. touching edges | 507 | PASS |
| D7 | projection + culling (`$00AF46`) incl. camera modes and `$FA1A` | 1,016 | PASS |
| D8 | composed frames (4 scenarios × 10–50 ticks) | 140 | PASS |
| **total** | | **7,740** | **0 mismatches** |

Additional ROM-executed checks (`test_recovered_behaviour.py`):
| ID | Subject | Result |
|---|---|---|
| D9 | name-entry cheat `$005920`, 6 codes + control, P1 and P2 | PASS — matches the Stage-1 table exactly |
| D10 | jump airtime/apex, 6 launch/mode combinations | PASS — **contradicts** the Stage-1 table (see §4) |

Evidence bundle: `evidence/stage2/stage2_verification.json`
(`tests`, `differential_comparisons`, `measured_jump_profiles`, `measured_cheat_table`).

## 4. Discrepancies found — and what they were

Every discrepancy below was reproduced, localised to the first divergent field, and
fixed at the level of the model (never by special-casing an output).

### 4.1 Reconstruction bugs (found by D1–D8)
| # | Symptom | Root cause | Fix |
|---|---|---|---|
| 1 | D3: animation-offset bit differed | `+$09` is the **low** byte of the word at `+$08`; I had set bit 9 (`0x0200`) instead of bit 1 (`0x0002`) | mask corrected |
| 2 | D4/D8: freeze never triggered | I keyed the freeze predicate on `+$30` (state); the ROM reads `+$08` (animation offset) | predicate reads `anim_offset` |
| 3 | D4: actor froze at `+$08 = 0x0114` | `andi.b #$FC` masks the low byte only, then `cmpi.w` compares 16 bits | compare `(anim & 0xFF00) \| (anim & 0xFC)` to `0x14` |
| 4 | D7: type `$05` not culled while police active | `$00AF8A` jumps **past** the skip branches to the bounds test | type test moved before the skip tests |
| 5 | D8: air control had no effect on scenarios | `step()` read the plan's flag but never loaded the plan's buttons into `+$54` | buttons applied at frame start |
| 6 | D2: `vy = 0x80000000` clamped | `Actor` stored the Python int `2147483648` instead of the signed value | `__post_init__` wraps all 6 32-bit fields |

### 4.2 Harness bugs (would have produced false evidence)
| # | Symptom | Root cause | Fix |
|---|---|---|---|
| 7 | D5: P1-base case returned the *non*-P1 null box | probe passed `a0 = $00FFB800`; the ROM tests `cmpa.w #$b800`, which sign-extends to `$FFFFB800` | probe uses the sign-extended address |
| 8 | D8: screen X off by a constant after earlier cases | camera words leaked between oracle calls | `frame()` pins `$E002`/`$E00E`/`$FA1A` per run |
| 9 | D9: cheat never matched | short absolute `$FF0C` was written as `0x00FF0C`, which is **ROM address 0x00FF0C**, not RAM | write `0x00FFFF0C` |
| 10 | D6: probe read zeros | two independent RAM mappings instead of aliases | `mem_map_ptr` onto one buffer |
| 11 | D5: `IndexError` at index 255 | the ROM happily reads past the 32-entry table | indices restricted to the documented range and the out-of-range behaviour documented as undefined |

Items 7–10 are the reason the harness is itself part of the deliverable: a wrong
oracle produces confident, wrong "confirmations".

### 4.3 Specification/test errors (not implementation errors)
* Four projection spec tests failed initially because I chose `X = −200` / `−1000` as
  "outside the margin" — but `sx = X + 128`, so −200 maps to −72, *inside* −896.
  Corrected inputs, not corrected implementation.
* The first jump-table test compared the apex at the end of the airtime rather than the
  minimum over the whole trajectory. Test fixed.

### 4.4 Discrepancy against Stage-1 documentation (D10)
The Stage-1 dossier's jump table (`§8.3`) does not match the ROM:

| launch | Stage-1 airtime / apex | **measured** airtime / apex |
|---|---|---|
| −7.5 neutral | 18 / 34.875 px | **15 / −27.375 px** |
| −7.5 directional | 20 / 34.875 | **17 / −27.375** |
| −8.5 neutral | 20 / 44.219 | **17 / −35.719** |
| −8.5 directional | 23 / 44.219 | **20 / −35.719** |
| −9.5 neutral | 22 / 54.656 | **19 / −45.156** |
| −9.5 directional | 25 / 54.656 | **22 / −45.156** |

The Stage-1 numbers are exactly what an integrate-then-gravity order yields
(`v²/2g + v/2`). The ROM applies gravity in the state handler **before** integration
(`$001FDC` → `$001CA6`), so each jump loses one gravity step of height and half a
step of rise. Re-deriving the closed form for the real order:

```
after n ticks:  vy_n = v0 + (n+1)·g
                y_n  = Σ_{i=1..n} vy_i = n·v0 + g·n(n+1)/2
apex where vy crosses 0, height = |v0|²/(2g) − |v0|/2 + g/8
```
For `v0 = −7.5`, `g = 0.90625`: `31.034 − 3.75 + 0.113 = 27.398`, and the discrete
minimum is −27.375 px (the last tick lands slightly before the continuous apex).
The qualitative Stage-1 finding — *same apex, longer airtime in directional jumps* —
remains correct and is now measured rather than asserted.

## 5. Tolerances

**None.** Every compared value is an integer produced by identical arithmetic.
No floating-point value appears in any comparison; the px figures in reports are
exact multiples of 1/65536. The only "tolerance-like" decision is which frames are
compared (all of them) and how culled frames are treated (screen fields are compared
only when both sides agree the actor was drawn).

## 6. What is covered, and what is not

| Covered | Range |
|---|---|
| gravity inputs | `vy ∈ [−0x40000, 0x140000]`, 300 cases per variant |
| clamp | all boundaries + 200 random values |
| air control | all 16 low-nibble button combinations × 25 velocity/flag sets |
| integration | 409 state/flag/velocity combinations incl. the exact freeze word |
| boxes | every index 0…31, 65 positions, both address classes, all null paths |
| AABB | 507 pairs incl. touching, gap-by-1, containment |
| projection | 1,016 cases across both camera modes, both cull margins, police latch |
| composition | 4 scenarios, 140 frames, every field compared every frame |

**Not covered by construction:**
* full-game emulation (no VDP, Z80, DMA, controller hardware);
* the state machine that chooses a gravity variant (scenario plans stand in);
* attack/hurt resolution, damage, animation timing, camera motion;
* non-player actor classes (their `+$64`/`+$70` meaning differs — see AUDIT C-8).

## 7. Limitations that affect the strength of the claim

1. **Function-level, not system-level.** The oracle executes the real routines, but
   outside the original scheduler. A rule could be *individually* faithful yet compose
   differently in the real frame; D8 mitigates this for the sliced order only.
2. **The plan is an assumption.** D8 proves "given this per-frame order and variant,
   the reconstruction matches". It does not prove that real players experience exactly
   those plans in every state.
3. **REV 00 only.** All runs use the `[!]` REV 00 image. The sliced ranges are
   byte-identical in REV 01, so no divergence is expected, but REV 01 was not executed
   for D1–D8.
4. **Synthetic actor records.** Real records carry neighbouring fields the slice
   ignores; the routines probed do not read them, which was verified by reading the
   disassembly, not by exhaustive instrumentation.

These limitations are the reason `COMPLETION_REPORT.md` reports a *slice* pass, not a
game-reconstruction pass.
