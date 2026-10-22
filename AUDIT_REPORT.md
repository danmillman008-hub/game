# Stage-2 Audit Report

**Scope:** re-audit the Stage-1 forensic dossier against the original ROM, establish
what is actually reproducible, then select and validate a first vertical slice.
**Date:** 2026-10-22 · **Branch:** `arena/eb3b2453-game`
**Original artifact:** `Streets-of-Rage_Genesis_EN.zip`, SHA-256
`f1c25bde80c00824b6fd7a9b1dfce290f1b98038ac72eee1854d8aa805a17645`
**Primary image used for all Stage-2 evidence:** `Streets of Rage (JUE) (REV 00) [!].bin`,
SHA-256 `dd44f120446654bb91c448762f3e0cd0d9b034f35d0e3266a4dc34402ada95c0`, 524,288 bytes.

---

## 1. Baseline established before any change

| Item | State found | Verified how |
|---|---|---|
| Repository | clean at `1a095ca`, branch `arena/eb3b2453-game` | `git status`, `git log` |
| Archive | present, 4,110,629 B, 11 ROMs | SHA-256 recomputed, `zipfile` listing |
| Stage-1 tool | `tools/verify_sor_forensics.py`, 348 lines | read in full, then executed |
| Stage-1 tool result | exit 0 in **0.78 s**; Z80 Kosinski cross-check OK | re-ran, compared JSON |
| Evidence bundle | `evidence/verification_results.json` | parsed, contents inspected |
| Toolchain | Python 3.11.2, capstone 5.0.7, unicorn 2.1.4 in `/tmp/re_venv` | import + version print |
| ROM scratch copies | re-extracted from the ZIP into `work/roms/` (gitignored) | `unzip` |

A fast runtime is not by itself a defect, but it prompted the question *what does the
tool actually assert?* — see §2.

## 2. What the Stage-1 tool really verifies

The committed tool performs **three** MC68000 experiments, not five:

| Experiment | Implemented? | Asserted? |
|---|---|---|
| EXP-01 Kosinski decompressor `$0085A2` | yes | **yes** — SHA-256 compared with the independent Python decoder |
| EXP-02 PRNG `$0104D8`, 8 steps | yes | **no assertion** — outputs recorded only |
| EXP-03 REV00 vs REV01 boss-`$30` police path | yes | **no assertion** — traces recorded only |
| EXP-04 dormant name-entry cheat `$005920` | **no** | — |
| EXP-05 jump trajectories | **no** | — |

`README.md` ("five controlled MC68000 experiments") and `COVERAGE_MATRIX.md`
("5 experiments: … name-entry cheat, jump trajectories") therefore overstate the
committed tool. `DOSSIER.md §8.3` additionally prints a jump table that no committed
code can produce.

This is a **documentation/provenance defect**, not a fabricated-result defect: the
cheat table and the REV00/REV01 traces in `evidence/verification_results.json` are
real, and both were independently reproduced in Stage 2 (see §4, D9/D10).

**Action taken:** the two missing experiments are now implemented against the real
ROM in `tests/test_recovered_behaviour.py`; the Stage-1 tool and its JSON output were
left untouched as historical evidence.

## 3. Reproducibility

| Check | Command | Result |
|---|---|---|
| Stage-1 evidence | `python3 tools/verify_sor_forensics.py` | PASS, 0.78 s, JSON unchanged in structure |
| Stage-2 suite | `python3 tools/verify_stage2.py` | PASS, 37 tests, 7,740 differential comparisons |
| Test-only run | `python3 -m unittest discover -s tests -v` | PASS |

Environment constraints that affect reproducibility are recorded in `REPRODUCE.md`;
the most important are: Unicorn must use `UC_CPU_M68K_M68000`, and the two RAM
windows (`$00FF0000`, `$FFFF0000`) must be **true aliases** of one buffer.

## 4. Corrections to Stage-1 claims (evidence-backed)

Each correction below was produced by re-reading the bytes *and* by executing the
routine on an MC68000 core. Nothing here is asserted from reading alone.

### C-1 (major) — body-box arithmetic was wrong in `DOSSIER.md §10.1`
Stage 1 stated `x2 = X + sbyte(a5[d1+1])`, `z2 = Z + sbyte(a6[d2+1])`,
`y2 = Y + sbyte(a5[d1+4])`, i.e. *absolute offsets*.
The ROM at `$0041A6–$0041E6` accumulates onto the value already in `d0`:

```
x1 = X_hi + b0        x2 = x1 + b1
z1 = Z_hi + z[b2].0   z2 = z1 + z[b2].1
y1 = Y_hi + b3        y2 = y1 + b4
```

`b1`, `z[b2].1` and `b4` are **extents**, not positions. Measured (`D5`, executed):

| index | table record | box built at X=1000, Z=500, Y=−20 |
|---|---|---|
| 2 | `(-3, 10, 0, -50, 50)` | `(997, 1007, 492, 508, -70, -20)` |
| 4 | `(-13, 13, 0, -51, 51)` | `(987, 1000, 492, 508, -71, -20)` |

Stage 1's formula would give `x2 = 1010` for index 2 and `y2 = +31` for index 4.

### C-2 (major) — the builder produces **two** boxes, not one
`$004140` runs twice per call: the first pass writes `+$64..+$6F` from index `+$02`,
the second writes `+$70..+$7B` from index `+$03` (a1 is never reset, so the second
pass lands 12 bytes later). Stage 1 documents only the `+$64` box and lists `+$70`
as an unrelated field.

Degenerate rules, all measured:
* `+$02 == 0` → `+$64` = six words of `$0010` (or `$0000` when `a0 == $FFFFB800`);
* `+$03 == 0` → `+$70` = six zero words;
* `+$4B` bit1 (invulnerable) → `+$70` takes the `+$02 == 0` rule.

### C-3 — AABB comparison order and inclusivity
`DOSSIER.md §10.2` says the six comparisons run **X, Z, Y**. The ROM (`$004514–
$00454E`) evaluates **Z, X, Y**, and every bound is inclusive (touching edges
overlap). Confirmed by 507 executed cases including all touching/gap boundaries (`D6`).

### C-4 — `+$54` is the *held* input byte; `+$55` is the pressed edge
`$00ADE8` performs `move.w $fc04,$b854`, and `$00813C` stores *held* at `$FC04` and
*newly pressed* at `$FC05`. Therefore the word at `+$54` is `[held][pressed]`:
`$0038C0` tests bit3 of `+$54` (held → right) while `$003914` tests bit4 of `+$55`
(pressed → B). `DOSSIER.md §7.1` labels `+$54` "pressed-buttons snapshot", which
describes only its low byte.

### C-5 — `$00442C`'s freeze predicate compares the **whole word** at `+$08`
`andi.b #$FC` masks the low byte only, then `cmpi.w #$14` compares 16 bits.
`+$08 = $0114` therefore does **not** freeze. Stage 1 gave the mask correctly but not
the consequence. (My own first implementation made this mistake; the differential
test caught it — see `RESEARCH_LOG` RL-56.)

### C-6 — `$004140` reads a **second** index and the `$B800` test is sign-extended
`cmpa.w #$b800,a0` compares against `$FFFFB800`, so only the P1 record at that exact
long address takes the special case. Probing with `$00FFB800` silently takes the
*other* branch — a probe hazard worth recording (`RL-57`).

### C-7 — jump trajectories (`DOSSIER.md §8.3`) are not reproducible and are wrong
Measured by executing `$00389A`/`$0038AE` + `$003886` + `$00442C` per frame:

| launch | neutral airtime | directional airtime | apex |
|---|---|---|---|
| −7.5 px/t | **15** ticks | **17** ticks | −27.375 px |
| −8.5 px/t | **17** | **20** | −35.719 px |
| −9.5 px/t | **19** | **22** | −45.156 px |

Stage 1 printed 18/20/22 and 20/23/25 with apexes 34.875/44.219/54.656 px.
Those values are exactly what an **integrate-then-gravity** ordering produces
(apex ≈ v²/2g + v/2). The ROM applies gravity *inside the state handler* (`$001FDC`)
**before** integration (`$001CA6`), which costs one full gravity step and one
half-step of travel. The qualitative Stage-1 claim — *the directional jump has the
same apex but longer airtime* — survives and is confirmed.

### C-8 — actor-record fields are context-aliased (structural)
`+$64..+$6F` is a six-word AABB on the player path (`$4140`) but holds approach
targets/steps for enemy code (`$009644` etc.); `+$70..+$7B` is the second AABB for
players but a count-prefixed record list for the actors consumed by `$00AD04`.
`DOSSIER.md §7.1` presents one flat meaning per offset. The table is still useful as
a *union* listing, but any implementation must key on actor class, not offset alone.

### C-9 — projection has exceptions Stage 1 did not record
`$00AF76`: bit1 of `+$01` makes an actor screen-fixed (camera offsets are not
subtracted). Culling additionally depends on type `$05` (always culled, wide left
margin `$FF80`), on bit3 of `+$01`, and on the police latch `$FA1A` (both skip
culling entirely). Measured in `D7` (1,016 executed cases).

## 5. Resolved open item (bonus)

**`U-INP-01` (`$FC06`)**: `$00813C` writes 0 to `$FC06`, then compares the two
controller reads (`cmp.b d3,d4`) and writes 1 when they differ. That is the
three-/six-button pad discriminator, i.e. `$FC06 != 0` ⇒ six-button pad.
**Confidence: HIGH** (static only; no runtime trace with real pad hardware).

## 6. Claims re-confirmed unchanged

* Player skeleton `$001C44` — byte-identical to `DOSSIER.md §8.1`, including call order.
* Actor pools: P1 `$B800`, P2 `$B880`, 66 general slots from `$B900` (`$00AD8E`, `$00AE0C`).
* Integration law (`$00442C`) and its three `add.l` operations.
* Gravity constants `$E800`, `$8800`, `$3800`, clamp `$C0000`.
* Air control `±$6000`, clamp `±$38000` — plus the newly documented facing side effects.
* Dormant cheat `$005920` — table reproduced exactly (`D9`), including the `$B800` P1/P2 split.
* Kosinski decompressor — bit-exact against the ROM's own routine (Stage-1 assertion still passes).
* PRNG closed form — still matches (Stage-1 output, unchanged).

## 7. Investigation priorities set by this audit

1. **Slice S1 (done):** 2.5D kinematics + body-box geometry + projection. Chosen because
   its routines are self-contained, its inputs are already documented, and its outputs
   are byte-exact integers — the cheapest place to prove the whole pipeline.
2. **Next (not done):** the attack-box system (`$00AB24`/`$00AB88`) and per-move frame
   data. Blocked on the semantics of the six-byte threshold records at `+$72`.
3. **Later:** animation state coupling (`+$08`/`+$0A`/`+$0D`), damage pipeline, enemy FSM.

The attack slice was *not* attempted in Stage 2; §7 of `COMPLETION_REPORT.md` states
the blocker precisely rather than pretending coverage.
