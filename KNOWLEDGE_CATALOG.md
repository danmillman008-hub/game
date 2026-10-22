# Knowledge Catalog

An index of what this repository now *knows how to do*, where the evidence is, which
code implements it, and how it is checked. Intended entry point for a future agent that
must extend the reconstruction without re-deriving the investigation.

**Legend — status**
`V` verified (ROM-executed, exact) · `S` static-only · `P` probable · `U` unknown.
**Reuse:** `G` generalisable pattern · `T` title-specific data/behaviour.

---

## A. Behavioural knowledge (implemented)

| ID | Knowledge | Status | Evidence | Spec | Component | Test | Reuse |
|---|---|---|---|---|---|---|---|
| K-01 | Positions/velocities are signed 32-bit 16.16; whole-pixel reads are the signed high word | V | `EV-S2-KIN-01`, `EV-ACT-04` | WS-01 §4 | `fixed.hi16/s32` | spec `FixedPoint`, D1–D8 | G |
| K-02 | Neutral gravity `+0xE800` per tick, applied *before* integration | V | `EV-S2-KIN-01`, `$00389A`, `$001FDC` | WS-01 §5.1, §9 | `neutral_gravity` | D1, D9 | T |
| K-03 | Directional gravity: `0xE800` while ascending, `0x8800` while descending; sign tested before the add | V | `EV-S2-KIN-01`, `$0038AE` | WS-01 §5.1 | `directional_gravity` | D1, D9 | T |
| K-04 | Soft gravity `+0x3800` used by arc/throw paths | V | `EV-S2-KIN-01`, `$0038A6` | WS-01 §5.1 | `soft_gravity` | D1 | T |
| K-05 | Terminal velocity is a **one-sided** clamp at `0xC0000` | V | `EV-S2-KIN-02`, `$003886` | WS-01 §5.2 | `clamp_terminal_velocity` | D2 | T |
| K-06 | Air control `±0x6000`, clamp `±0x38000`, right tested first, facing side effects, no-input skips the clamp | V | `EV-S2-KIN-03`, `$0038C0` | WS-01 §5.3 | `air_control` | D3 | T |
| K-07 | Integration adds `vx`,`vz`,`vy` to three axes; a state/animation-driven freeze suppresses all three | V | `EV-S2-KIN-04`, `$00442C` | WS-01 §5.4 | `integrate`, `is_frozen` | D4, D8 | G |
| K-08 | Freeze needs the whole `+$08` word to compare equal to `$14` after masking low-byte bits 0–1, plus `+$59` bit7 | V | `EV-S2-KIN-04` | WS-01 §5.4 | `is_frozen` | D4 | T |
| K-09 | A player carries **two** 12-byte AABBs: `+$64` from `+$02`, `+$70` from `+$03` | V | `EV-S2-BOX-01`, `$004140` | WS-02 §5 | `build_player_boxes` | D5 | T |
| K-10 | Box records are corner+extent, cumulatively added, 16-bit wrap | V | `EV-S2-BOX-02`, `$0041A6–$0041E6` | WS-02 §5 | `BoxTables.build` | D5, spec `Boxes` | G |
| K-11 | Null boxes: `0x0010` fill for `+$64` (general) / `0x0000` for P1 base and for `+$70` | V | `EV-S2-BOX-03` | WS-02 §6 | `build_player_boxes` | D5 | T |
| K-12 | AABB predicate is inclusive on Z, X, Y (evaluated in that order) | V | `EV-S2-BOX-04`, `$004514–$00454E` | WS-02 §5 | `aabb_overlap` | D6 | G |
| K-13 | `sx = X_hi + $80 − cam_x`, `sy = (Z_hi >> 1) + Y_hi + $80 − cam_y` | V | `EV-S2-PRJ-01`, `$00AF60–$00AF72` | WS-03 §5 | `project` | D7 | T |
| K-14 | Actors with `+$01` bit1 are screen-fixed (no camera subtraction) | V | `EV-S2-PRJ-02` | WS-03 §5 | `project` | D7 | T |
| K-15 | Cull window: drawn iff `−896 ≤ sx < 1280` and `16 ≤ (u16)sy < 512`; skipped by `+$01` bit3 or `$FA1A ≠ 0`; type `$05` always culled with `−128` | V | `EV-S2-PRJ-03` | WS-03 §5 | `project` | D7 | T |
| K-16 | Per-frame order: gravity → air control → clamp → integrate → boxes → project | V | `EV-S2-FRM-01`, `$001C44` | WS-04 §5 | `slice_runner.step` | D8 | G |
| K-17 | Real jump metrics: 15/17, 17/20, 19/22 ticks; apex −27.375/−35.719/−45.156 px | V | `EV-S2-KIN-05`, D10 | WS-01 §13 | `run_scenario` | D9/D10 | T |
| K-18 | Name-entry cheat table (`MOM`…blank) and its `$B800` P1/P2 split | V | `EV-S2-HID-01`, `$005920` | — | — | D9 | T |
| K-19 | `+$54` = held input byte, `+$55` = pressed edge | V | `EV-S2-INP-01`, `$00ADE8`, `$00813C` | WS-01 §3 | `Actor.buttons` | D3 | G |
| K-20 | `$FC06` = three/six-button discriminator (1 = six-button) | S | `EV-S2-INP-02`, `$00813C` | — | — | — | T |

## B. Infrastructure knowledge (reusable tooling)

| ID | Knowledge | Where | Why it matters |
|---|---|---|---|
| T-01 | Running individual ROM subroutines on a 68000 core with synthetic actor records | `tools/rom_probe.py` | the oracle for every differential test |
| T-02 | Sign-extended short absolutes: `$B800` → `$FFFFB800`; RAM must be aliased, not duplicated | `tools/rom_probe.py`, AUDIT C-6 | silent wrong-oracle class of bug |
| T-03 | `UC_CPU_M68K_M68000` and `SR=$2700` are required for faithful 68000 idioms | `tools/rom_probe.py`, `REPRODUCE.md` | otherwise `dbra`/`move.w sr` break |
| T-04 | Extracting tables with provenance (ROM SHA-256 + offsets) into JSON | `tools/extract_slice_tables.py` | keeps numbers out of code |
| T-05 | Counting differential comparisons as evidence volume, not just PASS | `tools/verify_stage2.py` | prevents "one test = verified" claims |
| T-06 | Byte-range diffing between revisions to decide if a slice is revision-dependent | `AUDIT_REPORT.md` §10 | avoids untested revision claims |

## C. Known-unknown knowledge (do not assume)

| ID | Unknown | Blocks | Next action |
|---|---|---|---|
| U-ATT-01 | Semantics of the six-byte threshold records at `+$72` consumed by `$00AB24` | attack hitbox slice | trace `$00AB24` callers with a synthetic attacker/victim pair; enumerate `+$72` writers |
| U-ATT-02 | How `$01A68E` attack-shape records map to specific moves | per-move frame data | correlate `+$02`/`+$03` values with animation blocks per character |
| U-ACT-01 | 10 unread actor fields (`+$35`,`+$36`,`+$43`,`+$44`,`+$5F`,`+$61`,`+$6A–+$6D`,`+$7A`,`+$7F`) | full record model | field-access trace across all handlers |
| U-STATE-01 | 13 player states dispatch to `$000000` | player FSM | find the guard that catches 0; confirm dead vs. unreachable |
| U-CBT-01 | Per-move frame tables (banks `$049AE0`/`$053EFE`/`$05E90A`) | combat reconstruction | dump animation blocks and correlate with state ids |
| U-INP-03 | Which byte of `$FC04` the 6-button extra buttons occupy | input fidelity | disassemble `$003914`'s callers; instrument a 6-button trace |
| U-CAM-01 | Camera follow law details beyond `$018AF8` | camera slice | same differential method as this stage |

## D. How to use this catalog

1. Pick a knowledge row whose **status is V** and whose component exists → you can
   build on it directly.
2. For a `T` row, copy the *numbers* from `components/data/*.json` (they carry the ROM
   hash), never retype them.
3. For a `U` row, start from the stated next action; do not infer the missing rule.
4. To add a row: extend `EVIDENCE_DATABASE.md` with `EV-S2-…`, add a spec section,
   implement, then add a differential test that compares against the ROM — the same
   pipeline that produced K-01…K-20.
