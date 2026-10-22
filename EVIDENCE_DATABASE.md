# Evidence Database
### Streets of Rage / Bare Knuckle (Mega Drive, 1991) — engineering reverse-engineering

Format follows the project specification. Every record is one testable claim.
`Evidence Type` ∈ {static code, disassembly, table decode, diff, exec, ref-impl, string, struct, negative search}.
`Confidence` uses the five-class taxonomy defined in `DOSSIER.md §0.2`.
Experiments `EXP-01`…`EXP-05` are implemented in `tools/verify_sor_forensics.py` and their raw output is `evidence/verification_results.json`.

---

## A. Boot, initialisation, integrity (5 records)

### EV-BOOT-01 — Reset vector and stack pointer placement
* **Subsystem:** Boot
* **Claim:** The initial SSP is `$00FFFF00`, so 256 bytes of RAM (`$FFFF00`–`$FFFFFF`) are reserved as engine globals above the stack, and Reset PC is `$00000208`.
* **Evidence:** Vector 0 = `00FFFF00`, vector 1 = `00000208`; every global in `$FF00`–`$FFFF` is referenced by absolute-short addressing while `A7` starts at `$FFFF00`.
* **Evidence Type:** struct / static
* **Location:** ROM `$000000`–`$000007`
* **Relevant Function:** exception vector table
* **Relevant Address/Offset:** `$000000`, `$000004`
* **Experiment:** —
* **Result:** matches; `$FFxxxx` region is never used as stack in any traced routine (no `-(a7)` writes above `$FFFEFF`).
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none credible (a stack could grow downward from `$FFFF00` without touching `$FF00`–`$FFFF`)
* **Open Questions:** none

### EV-BOOT-02 — Boot sequence and VDP register image
* **Subsystem:** Boot
* **Claim:** Boot performs TMSS handshake, loads 24 VDP registers from `$0002A4`, clears 64 KiB RAM + CRAM + VSRAM, mutes PSG, then branches to `$000308`.
* **Evidence:** `$00020C`–`$0002A2` disassembly; 24 bytes at `$0002A4` = `04 14 30 34 07 78 00 00 00 00 81 3D 00 02 01 00 00 00 61 B2 …`
* **Evidence Type:** disassembly
* **Location:** `$000208`–`$000307`
* **Relevant Function:** `BootEntry` [desc]
* **Relevant Address/Offset:** `$000208`, `$0002A4`
* **Experiment:** —
* **Result:** register loop `addi.w #$100,d0 / dbra d7` with `d7 = $12` → 19 iterations after the initial write, 24 registers total.
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** the purpose of the two words at `$02A8`/`$02AC` (`$3FFF`, `$0100`) inside the register image

### EV-BOOT-03 — ROM checksum algorithm and failure path
* **Subsystem:** Integrity
* **Claim:** The boot sums all big-endian 16-bit words from `$000200` to `$07FFFF` and compares against the header word at `$00018E`; mismatch jumps to `$000412`, which paints CRAM entry 0 red and halts.
* **Evidence:** `$000338`–`$000350` loop; `$000412` writes `$000E` to `$C00000`, `$8F02` to `$C00004`, then `bra.s *`.
* **Evidence Type:** disassembly
* **Location:** `$000338`–`$000435`
* **Relevant Function:** `RomChecksumVerify` [desc]
* **Relevant Address/Offset:** `$000338`, `$00018E`, `$000412`
* **Experiment:** re-implemented the sum in `tools/verify_sor_forensics.py::compute_sega_checksum`; run on all 11 images
* **Result:** REV00 `$9409` valid; `[p1]` header patched to `$F41C` and *its* computed sum is also `$F41C`; `[p2]` has a mismatch (`$9409` vs `$134A`) and survives only because it NOPs the branch at `$0348`
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** none

### EV-BOOT-04 — Development-cart bypass
* **Subsystem:** Integrity
* **Claim:** If bit 6 of `$A1000D` is clear, the checksum verification is skipped entirely.
* **Evidence:** `$000338`: `btst.b #6,$A1000D / beq.s .skip`
* **Evidence Type:** static code
* **Location:** `$000338`–`$00033C`
* **Relevant Function:** `RomChecksumVerify` [desc]
* **Relevant Address/Offset:** `$000338`
* **Experiment:** —
* **Result:** standard Sega dev-cart detect; explains why the `[p1]`-family patches are *both* header-corrected and bypass-patched
* **Confidence:** CONFIRMED
* **Alternative Explanations:** the bit could be a region flag; rejected because it also gates the write to `$FF44` bit… (see EV-BOOT-05)
* **Open Questions:** none

### EV-BOOT-05 — Region/version latch
* **Subsystem:** Boot / regional logic
* **Claim:** `$A10001` is masked with `$C0` and stored at `$FF44` (and `$FF0044`); bit 6 = PAL, bit 7 = overseas.
* **Evidence:** `$00030C`–`$000316`; consumers at `$007F8A`, `$012DA4`, `$01A088`.
* **Evidence Type:** static code
* **Location:** `$00030C`
* **Relevant Function:** `BootEntry` [desc]
* **Relevant Address/Offset:** `$00030C`, `$FF0044`
* **Experiment:** —
* **Result:** the only PAL constants found are a VDP register-1 value (`$81748134` vs `$817C813C`) and Mr. X's telegraph timer (`$5A` vs `$B4`)
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** whether the PAL VDP value is a redesign or a port artefact (`U-REG-01`)

---

## B. Version / revision analysis (4 records)

### EV-VER-01 — Eleven images, four genuine variants
* **Subsystem:** Versions
* **Claim:** The archive contains 2 original revisions and 9 derivative/modified images; only REV00 and REV01 are original code.
* **Evidence:** byte-exact diff of all 11 images against each other; header fields; checksum validity; ASCII markers (`Console connection`, `Dumped By TSD`, `SEGARMEGA DRIVE`).
* **Evidence Type:** diff
* **Location:** whole image; markers at `$7FF40`, `$0104`, `$0120`–`$0174`
* **Relevant Function:** — (archive-level)
* **Relevant Address/Offset:** `$00018E`, `$000104`, `$7FF40`
* **Experiment:** `audit_archive()` in the tool
* **Result:** REV00 0 diffs; REV01 2092; `[b1]` 18; `[h1]` 20; `[p1]` 18; `[p1][h1]` 51; `[p2][!]` 10; `[T+Fre]` 1796; `[p1]+Spa` 1235; `[p1][h1]+Spa` 1268; `[p2]+Spa` 1227
* **Confidence:** CONFIRMED
* **Alternative Explanations:** `[p1]` could be an official revision — rejected: it rewrites the console-name string and NOPs instructions
* **Open Questions:** whether `[p1]`'s `$11995/$1199B` change is a trainer or a fix

### EV-VER-02 — REV01's substantive change is a boss soft-lock fix
* **Subsystem:** Versions / Boss
* **Claim:** REV01 inserts `tst.w $32(a0) / ble` before the police-special latch at `$0143FC`, so a dying boss no longer freezes.
* **Evidence:** byte diff `$0143FB`–`$014D61`; disassembly of both; insertion of 6 bytes shifts all following code by 6.
* **Evidence Type:** diff + disassembly + exec
* **Location:** `$0143FB`–`$014D61`
* **Relevant Function:** boss type `$30` handler
* **Relevant Address/Offset:** `$0143FC` (REV00), `$014402` (REV01)
* **Experiment:** `EXP-03` — identical preconditions (HP 0, `$FA1A = 1`, `$B800 = 1`), executed on MC68000
* **Result:** REV00 trace ends in an early `rts` with `+$67 = 1`; REV01 trace continues to `$01445E` in the normal death path
* **Confidence:** CONFIRMED
* **Alternative Explanations:** the change could target a different symptom (e.g. duplicate latch writes); rejected because the only semantic addition is the HP test
* **Open Questions:** none

### EV-VER-03 — All other REV01 differences are re-assembly consequences
* **Subsystem:** Versions
* **Claim:** Apart from date/checksum and the `$0143FC` insertion, REV01 differs only in shifted branch displacements and one rewritten block at `$014D7E`.
* **Evidence:** region 3 of the diff is 2407 bytes but aligned comparison (REV00[x] vs REV01[x+6]) leaves only the insertion *and* a second difference at `$014D7E` where a `jsr $1569C` was moved earlier and an `addq.w #1,$14(a1)` dropped.
* **Evidence Type:** diff
* **Location:** `$014D7E`–`$014DAF`
* **Relevant Function:** boss type `$30` handler
* **Relevant Address/Offset:** `$014DA4`/`$014DAC`
* **Experiment:** shifted-offset diff comparison
* **Result:** confirms a single logical edit plus mechanical re-assembly
* **Confidence:** HIGH CONFIDENCE
* **Alternative Explanations:** a second logical edit inside region 3 that coincidentally matches after a +6 shift
* **Open Questions:** semantic effect of moving `jsr $1569C` before the position copy (`U-VER-01`)

### EV-VER-04 — Modified images never touch gameplay balance
* **Subsystem:** Versions
* **Claim:** `[p1]`, `[p2]`, `[b1]`, `[h1]` modify text/checksum handling only; the translations modify text only.
* **Evidence:** every diff byte mapped: `$0104` (name), `$0336` (bypass), `$0348` (NOP), `$08F53/$08F55/$08F57` (`$90` = `nop`), `$0C97A/$0C9D0/$0CA26` opcode letter, `$11995/$1199B`, `$7FF40` (ASCII). Translation edits cluster on text strings.
* **Evidence Type:** diff
* **Location:** as listed
* **Relevant Function:** —
* **Relevant Address/Offset:** `$08F53`, `$0C97A`, `$11995`
* **Experiment:** per-byte classification of all 10 diffs vs REV00
* **Result:** no stat, physics, or AI constant is altered in any derivative
* **Confidence:** CONFIRMED
* **Alternative Explanations:** a subtle numeric change hidden in the translation streams — rejected: every changed offset is inside a text string region identified independently by the font renderer's use
* **Open Questions:** purpose of `$08F53` NOPs (in an attract/demo path)

---

## C. Main loop, scheduling, interrupts (5 records)

### EV-LOOP-01 — Fixed-timestep, V-Blank-synchronised architecture
* **Subsystem:** Scheduling
* **Claim:** One simulation tick = one video frame; the main loop busy-waits on a RAM handshake with the V-Blank ISR, and no delta-time exists.
* **Evidence:** `$010502` (`move.b #1,$FA00 / move.w #$2500,sr / tst.b $FA00 / bne.s -4 / rts`), ISR clears `$FA00`; velocities are added directly with no time scaling anywhere.
* **Evidence Type:** static code + negative search
* **Location:** `$010502`–`$010524`, `$019D16`
* **Relevant Function:** `FrameSync` [desc]
* **Relevant Address/Offset:** `$010502`, `$01050C`, `$FA00`
* **Experiment:** exhaustive search for a per-frame delta multiplier (`mulu`/`muls` against a frame-time variable) — none found
* **Result:** strictly frame-locked; PAL runs 50 Hz with no compensation
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none credible
* **Open Questions:** none

### EV-LOOP-02 — Master state dispatcher is a byte-offset table
* **Subsystem:** Program structure
* **Claim:** `$FF00` holds an *even byte offset* (0..42) into a 22-entry longword table at `$0003BA`.
* **Evidence:** `$03A2`: `move.w $FF00,d1 / move.w ($03BA,PC,d1.w),d1`… (the table stores 16-bit displacements that resolve to the 22 targets); transitions use `addq.w #2`/`subq.w #2`.
* **Evidence Type:** static code
* **Location:** `$0003A2`–`$000411`
* **Relevant Function:** `MainLoop` [desc]
* **Relevant Address/Offset:** `$0003A2`, `$0003BA`, `$FF00`
* **Experiment:** dumped all 22 targets and disassembled each
* **Result:** 22 distinct states `$00`..`$2A`, all located and labelled in `DOSSIER §25.1`
* **Confidence:** CONFIRMED
* **Alternative Explanations:** `$FF00` could be an index scaled elsewhere — rejected: no shift/multiply precedes the table read
* **Open Questions:** none

### EV-LOOP-03 — Gameplay frame call order
* **Subsystem:** Scheduling
* **Claim:** The gameplay frame executes exactly 12 subsystem calls in a fixed order: pause check, background columns, 2P scroll, spawn script, lifebar stream, round dispatch, palette cycle, **actor pass**, parallax, scripted FX, SAT kickoff, police.
* **Evidence:** `$01087A`–`$0108C6` instruction sequence.
* **Evidence Type:** static code
* **Location:** `$01087A`–`$0108C6`
* **Relevant Function:** master state `$16`
* **Relevant Address/Offset:** `$010888`–`$0108C0`
* **Experiment:** —
* **Result:** order is literal; any reordering changes observed behaviour (see EV-LOOP-05)
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** role of `$0117FC` (call #6), which reads sound-block RAM (`$F50E`)

### EV-LOOP-04 — V-Blank ISR order and frame budget
* **Subsystem:** Interrupts
* **Claim:** The ISR performs VSRAM scroll, optional CRAM DMA, display-mode dispatch, SAT DMA, pad read, sound tick — in that order — and has a lag-frame branch.
* **Evidence:** `$019D16`–`$01A0B2`.
* **Evidence Type:** disassembly
* **Location:** `$019D16`–`$01A0B2`
* **Relevant Function:** `VBlankISR` [desc]
* **Relevant Address/Offset:** `$019D16`, `$01A06E`, `$01A088`
* **Experiment:** —
* **Result:** if `$FA00` is clear at ISR entry, control jumps to `$01A088`, skipping all updates but still DMAing sprites — a graceful lag frame
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** exact rendering consequence of the lag branch (sprite duplicates vs. freeze)

### EV-LOOP-05 — Double-frame insert between collision and actor pass
* **Subsystem:** Scheduling
* **Claim:** The actor pass deliberately spends an extra frame: `jsr $010514` (a second frame-wait) sits between collision and the sorted draw pass.
* **Evidence:** `$00ADE4`: `jsr $010514` between `jsr $0043AA` and the bucket insertion.
* **Evidence Type:** static code
* **Location:** `$00ADE4`
* **Relevant Function:** actor dispatcher
* **Relevant Address/Offset:** `$00ADE4`
* **Experiment:** —
* **Result:** hit results (reaction state) become visible one frame before the sprite list reflects the new pose
* **Confidence:** HIGH CONFIDENCE
* **Alternative Explanations:** a workaround for VRAM bandwidth; cannot be distinguished statically
* **Open Questions:** whether this is the source of the game's characteristic one-frame hit feedback (`U-FEEL-01`)

---

## D. Memory map (4 records)

### EV-MEM-01 — The 64 KiB work-RAM block map
* **Subsystem:** Memory
* **Claim:** All engine state lives in `$FF0000`–`$FFFFFF`; `$F000`–`$F5FF` is audio, `$F600`–`$F9FF` is the sprite shadow, `$FA00`–`$FBFF` is frame/script state, `$FC00`–`$FC5F` is VDP command + pad + script pointers, `$E000`–`$E1FF` is camera, `$E200`–`$E9DF` is the Y-sort table.
* **Evidence:** every `move.x $FFnn` in the image, grouped by address; see `DOSSIER §6.2` for the ~120-block table.
* **Evidence Type:** static code (xref sweep)
* **Location:** `$FF0000`–`$FFFFFF`
* **Relevant Function:** —
* **Relevant Address/Offset:** `$E200`, `$F400`, `$F600`, `$FA00`, `$FC00`
* **Experiment:** scripted xref sweep of all `$FF..`/`$FE..`-relative operands
* **Result:** 120 named blocks; only `$FF3FC0`–`$FF3FFF` remains unexplained
* **Confidence:** CONFIRMED (blocks), UNKNOWN (that 64-byte hole)
* **Alternative Explanations:** the hole could be an unused high-score extension or an overflow guard band
* **Open Questions:** `$FF3FC0`–`$FF3FFF`

### EV-MEM-02 — Block clears stop below `$FF40`
* **Subsystem:** Memory
* **Claim:** The "clear RAM" idiom (`d7 = $1FA`, `jsr $0103D0`) clears 16 320 bytes (`$FF0000`–`$FF3FBF`), so the PRNG state and region latch at `$FF40`/`$FF44` survive a state reset.
* **Evidence:** `$008EBC`–`$008ECC`; `$0103D0` writes 32 longs per call.
* **Evidence Type:** static code
* **Location:** `$008EBC`, `$0103D0`
* **Relevant Function:** multiple state initialisers
* **Relevant Address/Offset:** `$0103D0`, `$FF40`
* **Experiment:** arithmetic: `$1FA+1` calls × 32 bytes = 16 320
* **Result:** `$FF0000`+16320 = `$FF3FC0`; `$FF40`..`$FF44` preserved
* **Confidence:** CONFIRMED
* **Alternative Explanations:** an off-by-one that happens to be harmless
* **Open Questions:** whether PRNG persistence across resets is intentional

### EV-MEM-03 — Two camera contexts
* **Subsystem:** Memory / Camera
* **Claim:** `$E000` and `$E100` are two structurally identical camera contexts, each with position, velocity, limits, a plane width and a sub-struct array.
* **Evidence:** `$018AF8` runs `$18C22`/`$18B3C`/`$19332` over `$E000` then `$E100` with different plane pointers (`$FF0000`/`$FF2000`) and cursors (`$EA00`/`$EB20`).
* **Evidence Type:** static code
* **Location:** `$018AF8`–`$018B3A`
* **Relevant Function:** camera update
* **Relevant Address/Offset:** `$018AF8`, `$E000`, `$E100`
* **Experiment:** —
* **Result:** layout table in `DOSSIER §19.1`
* **Confidence:** CONFIRMED (layout), HIGH CONFIDENCE (2P role split)
* **Alternative Explanations:** a second context for foreground/background parallax rather than per-player
* **Open Questions:** which is which in 1P mode (`U-CAM-01`)

### EV-MEM-04 — Terrain plane at `$FFA000` with two height tables
* **Subsystem:** Memory / Level
* **Claim:** The walkable terrain is a byte plane at `$FFA000` (two 4-bit tiles per byte, 16×8 px cells) plus two patched tables at `$FC34` (height) and `$FC38` (stand threshold).
* **Evidence:** `$00AD2A`–`$00AD8C` arithmetic and the two pointer loads.
* **Evidence Type:** static code
* **Location:** `$00AD2A`
* **Relevant Function:** `GroundQuery` [desc]
* **Relevant Address/Offset:** `$00AD54`, `$FC34`, `$FC38`, `$FFA000`
* **Experiment:** —
* **Result:** only 16 tile types per round; `Y >= threshold` decides standing
* **Confidence:** CONFIRMED
* **Alternative Explanations:** `$FC34/$FC38` could be base addresses instead of pointers — rejected because both are loaded with `movea.l`
* **Open Questions:** per-round source tables (`U-LVL-02`)

---

## E. Actor records and pools (4 records)

### EV-ACT-01 — Uniform 128-byte actor record
* **Subsystem:** Objects
* **Claim:** Every dynamic entity (players, enemies, bosses, weapons, pickups, effects, props) is a 128-byte record with a type byte at `+$00`; `type == 0` means free.
* **Evidence:** `$80` stride in every pool loop (`$00ADA0`–`$00ADBE`, `$00AE12`–`$00AE3E`); `tst.b (a0)` free-slot tests; identical physics/sprite helpers used for all types.
* **Evidence Type:** struct
* **Location:** `$00AD8E`–`$00AF00`
* **Relevant Function:** actor dispatcher
* **Relevant Address/Offset:** `+$00`, stride `$80`
* **Experiment:** —
* **Result:** 34 fields mapped with writer+consumer pairs (`DOSSIER §7.1`), 10 fields unresolved
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none credible
* **Open Questions:** `U-ACT-01`

### EV-ACT-02 — Pool layout and counts
* **Subsystem:** Objects
* **Claim:** Two player slots at `$B800`/`$B880`, 32 general actor slots at `$B900`, 24 effect slots at `$C900`, with a 66-slot walk to `$DA7F`.
* **Evidence:** `$00AE00`/`$00AE06` (players), `$0094C0` (`moveq #$1f,d7` over `$B900`), `$0095AA` (`$C900`, `#$17`), `$00AE0C` (`#$41` → 66 slots), `$00B132` (`cmpa.w #$D100`).
* **Evidence Type:** static code
* **Location:** as above
* **Relevant Function:** actor dispatcher / effect spawner
* **Relevant Address/Offset:** `$B800`, `$B900`, `$C900`, `$D100`
* **Experiment:** —
* **Result:** pool table in `DOSSIER §7.2`
* **Confidence:** CONFIRMED (boundaries), HIGH CONFIDENCE (role split)
* **Alternative Explanations:** the 32/24 split could be 48/18 with the `$D100` test as the real divider
* **Open Questions:** `U-POOL-01`

### EV-ACT-03 — 156-entry type dispatch table
* **Subsystem:** Objects
* **Claim:** `$00B236` holds one 16-bit ROM address per actor type; all 156 entries resolved to code addresses.
* **Evidence:** table dump + per-entry first-instruction decode; boss entries are `jmp $xxxxxx.l` trampolines at `$00B36A`–`$00B3C4`.
* **Evidence Type:** table decode
* **Location:** `$00B236`–`$00B3C8`
* **Relevant Function:** actor dispatcher
* **Relevant Address/Offset:** `$00B236`
* **Experiment:** enumerated types `$01`–`$9B`
* **Result:** complete table in `DOSSIER §7.3`; `$90`–`$95` resolve past ROM
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** `U-DISP-01`

### EV-ACT-04 — Split into three fields: position, depth, height
* **Subsystem:** Objects / Physics
* **Claim:** `+$10` = X (16.16), `+$14` = Z/depth (16.16), `+$18` = Y/height (16.16), with velocities at `+$1C`, `+$20`, `+$24` respectively.
* **Evidence:** integration at `$004448`–`$00445C`; the projection at `$00AF64`–`$00AF6A` (`Z>>1 + Y`); clamps at `$009F96` (X) and `$00A00E` (Z).
* **Evidence Type:** static code
* **Location:** `$004448`, `$00AF60`
* **Relevant Function:** integration / sprite builder
* **Relevant Address/Offset:** `+$10`, `+$14`, `+$18`, `+$1C`, `+$20`, `+$24`
* **Experiment:** —
* **Result:** corrects an initial misreading in which `+$20` was the vertical velocity
* **Confidence:** CONFIRMED
* **Alternative Explanations:** `+$14` as a word with a separate `+$16` subpixel — rejected because `add.l d0,$14(a0)` writes four bytes
* **Open Questions:** none

---

## F. Player system (5 records)

### EV-PLY-01 — Player is actor type `$01` with a 128-entry state table
* **Subsystem:** Player
* **Claim:** The player's per-frame dispatch is `state & $FE` into a 128-entry table of 16-bit ROM addresses at `$001CE2`; the odd value is the facing bit of the same state.
* **Evidence:** `$001C94` (`lea $1CE2(pc),a1 / jsr $00B186`); `$00B186` doubling the state byte; the table contains adjacent duplicates for every state.
* **Evidence Type:** static code + table decode
* **Location:** `$001CE2`–`$001DFE`
* **Relevant Function:** player handler
* **Relevant Address/Offset:** `$001CE2`, `$00B186`
* **Experiment:** dumped all 128 entries and read each target
* **Result:** full grouping in `DOSSIER §8.2`; 13 slots point at `$000000`
* **Confidence:** CONFIRMED (table), UNKNOWN (`U-STATE-01` for the null slots)
* **Alternative Explanations:** the null slots could be intentional "invalid state" traps
* **Open Questions:** `U-STATE-01`

### EV-PLY-02 — Pre-emption order inside the player frame
* **Subsystem:** Player
* **Claim:** Before the state machine runs, the player handler performs: forced-state check, special-move check, name/pickup proximity, timers, police knockback — and only then dispatches.
* **Evidence:** `$001C44`–`$001C7E` call sequence with early returns at `$001C7A` and `$001C92`.
* **Evidence Type:** static code
* **Location:** `$001C44`–`$001CD6`
* **Relevant Function:** player handler
* **Relevant Address/Offset:** `$001C58`, `$001C76`, `$001C94`
* **Experiment:** —
* **Result:** explains why a police call interrupts any state including attacks
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** none

### EV-PLY-03 — Character differentiation is data-only
* **Subsystem:** Player
* **Claim:** `+$50` ∈ {0,1,2} selects one of three longword pointers (`$049AE0`, `$053EFE`, `$05E90A`) used as the animation/sprite base; there is no per-character code.
* **Evidence:** `$001EA8`–`$001EB4` (`lsl.w #2,d0 / movea.l $1F20(pc,d0.w),a1`), the three pointers at `$001F20`.
* **Evidence Type:** static code
* **Location:** `$001EA8`, `$001F20`
* **Relevant Function:** player handler
* **Relevant Address/Offset:** `$001F20`–`$001F2B`
* **Experiment:** —
* **Result:** per-character differences (speed, jump impulse, reach) come from animation data, not branches
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** which animation byte controls which axis for each character (`U-CBT-01`)

### EV-PLY-04 — Special attack is a stocked resource
* **Subsystem:** Player / Combat
* **Claim:** The special attack is gated on a stock byte at `$FF21`/`$FF24`, decrements it on use, and sets `$FA1A = $101`.
* **Evidence:** `$003FCC`–`$0040A4`: `tst.b (a1) / beq return`, `subq.b #1,(a1)`, `move.w #$101,$FA1A`.
* **Evidence Type:** static code
* **Location:** `$003FCC`–`$0040A4`
* **Relevant Function:** `SpecialAttackCheck` [desc]
* **Relevant Address/Offset:** `$00402A`, `$00404C`, `$FF21`
* **Experiment:** —
* **Result:** police calls are limited (default 1, more via the dormant cheat)
* **Confidence:** CONFIRMED
* **Alternative Explanations:** the stock could be a cooldown counter — rejected because `$005952` writes lives into the same block from a table
* **Open Questions:** none

### EV-PLY-05 — Combo chain is a counter, not a timer
* **Subsystem:** Player / Combat
* **Claim:** `+$40` counts connected hits in one animation; the chain is capped at 3 by a byte comparison and re-armed via `+$41`.
* **Evidence:** `$003F02`–`$003F20` (`addq.b #1,$40(a0)`; `cmpi.b #2,$40(a0)`; `move.b #$26,$41(a0)`).
* **Evidence Type:** static code
* **Location:** `$003F02`–`$003F20`
* **Relevant Function:** player attack state
* **Relevant Address/Offset:** `$003F08`, `$003F0C`, `$003F18`
* **Experiment:** —
* **Result:** max 3-hit chain; no scaling of damage with chain length
* **Confidence:** HIGH CONFIDENCE
* **Alternative Explanations:** `+$41` could be a timer that also gates the chain
* **Open Questions:** interaction of `+$41` with `+$0D`

---

## G. Physics (3 records)

### EV-PHY-01 — Gravity constants and the neutral/directional split
* **Subsystem:** Physics
* **Claim:** Ascent gravity is `$E800` (0.90625) in both jump paths; descent is `$E800` for neutral jumps and `$8800` (1.0625) for directional jumps.
* **Evidence:** `$00389A` (unconditional `$E800`), `$0038AE` (`tst.l $24(a0) / bmi` → `$E800` else `$8800`).
* **Evidence Type:** static code + exec
* **Location:** `$00389A`–`$0038BE`
* **Relevant Function:** gravity applicators
* **Relevant Address/Offset:** `$00389A`, `$0038AE`
* **Experiment:** `EXP-05` — executed both routines against three launch velocities
* **Result:** neutral 18/20/22 ticks; directional 20/23/25 ticks; identical apex per velocity
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** which characters use which launch velocity (`U-CBT-01`)

### EV-PHY-02 — Terminal velocity clamps
* **Subsystem:** Physics
* **Claim:** Falling is clamped at `$C0000` (12.0 px/tick) for normal actors and `$100000` (16.0) after a hit.
* **Evidence:** `$003886`–`$003898`; `$00974E`–`$009758`.
* **Evidence Type:** static code
* **Location:** `$003886`, `$00974E`
* **Relevant Function:** gravity clamp / hit-reaction update
* **Relevant Address/Offset:** `$003890`, `$009758`
* **Experiment:** —
* **Result:** two distinct caps, both literal
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** none

### EV-PHY-03 — Horizontal limits and wall behaviour
* **Subsystem:** Physics
* **Claim:** Movement is bounded by restoring the previous coordinate when the proposed one exceeds a per-round band; there are no wall objects.
* **Evidence:** `$009F96`–`$009FE4`, `$00A00E`–`$00A040`; constants `$2F00000`, `$15100000`, `$14000000`, `$20000`.
* **Evidence Type:** static code
* **Location:** `$009F96`, `$00A00E`
* **Relevant Function:** `MoveXClamped` / `MoveZClamped` [desc]
* **Relevant Address/Offset:** `$009FCA`, `$009FD4`, `$00A018`
* **Experiment:** —
* **Result:** wall test = "value unchanged + flag set"; no collision response
* **Confidence:** CONFIRMED
* **Alternative Explanations:** the constants could be camera-relative rather than world absolute
* **Open Questions:** per-round band values (`U-LVL-02`)

---

## H. Collision (3 records)

### EV-COL-01 — Body box built from two ROM tables
* **Subsystem:** Collision
* **Claim:** The 12-byte world box at `+$64` is built every frame from 5-byte records in `$01ABA8` (indexed by sprite width) and 2-byte records in `$01AB8E` (indexed by a Z class byte).
* **Evidence:** `$004140`–`$0041E8`, including `d1 = idx*5` (`lsl.w #2 / add.w`) and `d2 = byte*2` for the Z table.
* **Evidence Type:** static code
* **Location:** `$004140`–`$0041E8`
* **Relevant Function:** `BuildBodyBox` [desc]
* **Relevant Address/Offset:** `$01ABA8`, `$01AB8E`, `+$64`
* **Experiment:** —
* **Result:** box layout `x1,x2,z1,z2,y1,y2` at `+$64`,`+$66`,`+$68`,`+$6A`,`+$6C`,`+$6E`
* **Confidence:** CONFIRMED (arithmetic), PROBABLE (field order X,Z,Y)
* **Alternative Explanations:** the third pair could be Z and the second Y
* **Open Questions:** `U-COLL-01`

### EV-COL-02 — Attack box list and interval-overlap test
* **Subsystem:** Collision
* **Claim:** `+$70` holds a word count followed by 6-byte attack records; overlap is decided by three interval tests with signed byte offsets.
* **Evidence:** `$00AD04` (count test), `$00AB24`/`$00AB88`/`$00AC78` (interval tests), `$00AB7C` (`adda.w #$6,a2`).
* **Evidence Type:** static code
* **Location:** `$00AB24`–`$00AD02`
* **Relevant Function:** `AttackBoxTest` [desc]
* **Relevant Address/Offset:** `+$70`, `$00AB88`
* **Experiment:** —
* **Result:** no circles, no masks; Z tested with doubled offsets
* **Confidence:** CONFIRMED (test arithmetic), PROBABLE (record field semantics)
* **Alternative Explanations:** the 6-byte records could be two 3-byte sub-records
* **Open Questions:** `U-COLL-01`

### EV-COL-03 — Multi-hit prevention via a state bit
* **Subsystem:** Collision / Combat
* **Claim:** A single attack cannot hit the same target twice because `+$4B` bit6 is set on the first hit and cleared when the animation block changes.
* **Evidence:** `$0043E6`/`$0043E6`-region checks; `$00504E`; `$0043EC` clears `+$4B` bits `$F3` at anim change.
* **Evidence Type:** static code
* **Location:** `$004134`, `$0043E6`, `$00504E`
* **Relevant Function:** combat resolution
* **Relevant Address/Offset:** `$004134`, `+$4B`
* **Experiment:** —
* **Result:** explains multi-frame active hitboxes without a hit list
* **Confidence:** HIGH CONFIDENCE
* **Alternative Explanations:** bit6 could be a general "busy" flag repurposed here
* **Open Questions:** none

---

## I. Combat (4 records)

### EV-CBT-01 — Damage is a nibble selected by animation frame
* **Subsystem:** Combat
* **Claim:** Player attack damage = low nibble of `byte($00423C + subtable + (+$50) + 3 + (+$0A))`; the high nibble is the reaction class.
* **Evidence:** `$0041EA`–`$00423A` full chain.
* **Evidence Type:** static code
* **Location:** `$0041EA`–`$00423A`
* **Relevant Function:** `SetAttackDamage` [desc]
* **Relevant Address/Offset:** `$004208`, `$004224`, `$00423C`
* **Experiment:** arithmetic traced for a sample sub-table at `$00423C` (`$0050` sentinel, `$0054`,`$0063`,…)
* **Result:** damage 0..15 per frame; reaction class 0..15
* **Confidence:** CONFIRMED
* **Alternative Explanations:** the high nibble could be a second damage component
* **Open Questions:** full per-move table (`U-CBT-01`)

### EV-CBT-02 — `$FA43` triples damage and can change reactions
* **Subsystem:** Combat
* **Claim:** With `$FA43 != 0`, the damage byte becomes `3*lo + hi`, so the applied damage is `(3*lo+hi)&$0F` and the reaction class is `(3*lo+hi)>>4`.
* **Evidence:** `$00420C`–`$004222`.
* **Evidence Type:** static code
* **Location:** `$00420C`–`$004236`
* **Relevant Function:** `SetAttackDamage` [desc]
* **Relevant Address/Offset:** `$004212`, `$FA43`
* **Experiment:** bit-level arithmetic check
* **Result:** overflow deliberately bleeds into the reaction nibble
* **Confidence:** CONFIRMED
* **Alternative Explanations:** the code could be a pack/unpack idiom unrelated to damage
* **Open Questions:** what sets `$FA43` in normal play (`U-HID-01`)

### EV-CBT-03 — HP subtraction, stun timer and death branch
* **Subsystem:** Combat
* **Claim:** Victim HP -= attacker `+$34`; below zero → death state; otherwise a 24-frame stun timer is set at `+$50`.
* **Evidence:** `$009BCC`–`$009C14`.
* **Evidence Type:** static code
* **Location:** `$009BCC`–`$009C14`
* **Relevant Function:** enemy hit-reaction state
* **Relevant Address/Offset:** `$009BD6`, `$009C02`, `$009C36`
* **Experiment:** —
* **Result:** one shared arithmetic path for players and enemies
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** none

### EV-CBT-04 — No hit-stop, no damage scaling
* **Subsystem:** Combat
* **Claim:** The engine has no hit-stop (freeze frames) and no combo damage scaling.
* **Evidence:** negative search: no global freeze counter is written from any damage path; `$FA71`/`$FA1F`/`$FA1A` are the only simulation freezes; damage is a table nibble with no chain multiplier.
* **Evidence Type:** negative search
* **Location:** whole image
* **Relevant Function:** —
* **Relevant Address/Offset:** `$004208` (only damage selector)
* **Experiment:** exhaustive xref of all writes to the three freeze flags + scan for a per-frame "hit freeze" decrementer
* **Result:** none found
* **Confidence:** CONFIRMED
* **Alternative Explanations:** hit-stop could be implemented as animation-frame duration changes — ruled out because frame duration is per-frame data, not per-hit
* **Open Questions:** none

---

## J. Enemy AI (3 records)

### EV-AI-01 — Shared AI core routine set
* **Subsystem:** Enemy AI
* **Claim:** Nine routines (`$009604`, `$009648`, `$009654`, `$00969E`, `$0096C0`, `$0096EC`, `$00973E`, `$0097FE`, `$00982C`) implement approach, facing, targeting, airborne update and velocity solving for every enemy type.
* **Evidence:** call-graph census over `$00D600`–`$017800` (top callers: `$01069E` 53×, `$0096C0` 50×, `$00A9BA` 44×, `$009604` 25×, `$0096EC` 21×).
* **Evidence Type:** static code (call census)
* **Location:** `$009604`–`$0098E8`
* **Relevant Function:** shared AI
* **Relevant Address/Offset:** `$009604`, `$0096EC`, `$00982C`
* **Experiment:** automated JSR/JSR-PC target counter
* **Result:** confirms a genuinely shared core rather than per-type duplication
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** none

### EV-AI-02 — 2P target selection is nearest-X only
* **Subsystem:** Enemy AI
* **Claim:** With two players active, an enemy targets whichever player has the smaller absolute X distance; otherwise it targets player 1.
* **Evidence:** `$0096EC`–`$00972C`.
* **Evidence Type:** static code
* **Location:** `$0096EC`–`$00972C`
* **Relevant Function:** `SelectTarget` [desc]
* **Relevant Address/Offset:** `$009716`, `$009726`
* **Experiment:** —
* **Result:** no aggro memory, no pack coordination
* **Confidence:** CONFIRMED
* **Alternative Explanations:** `|dx|` could be `dx` with sign — rejected because both values are negated when negative
* **Open Questions:** none

### EV-AI-03 — Enemy stat table layout and values
* **Subsystem:** Enemy AI / Balance
* **Claim:** `$026FCE` = 6-byte records (`HP[3]`, `ATK[3]`), effective HP = byte+1; `$027010` = 3 score IDs; `$027032` = animation pointers.
* **Evidence:** table bytes plus consumer arithmetic (`$0093CE`, `$009406`, `$000A4E` index tables).
* **Evidence Type:** table decode
* **Location:** `$026FCE`–`$02705E`
* **Relevant Function:** enemy init
* **Relevant Address/Offset:** `$026FCE`, `$027010`, `$027032`
* **Experiment:** `extract_core_tables()` in the tool
* **Result:** full table in `DOSSIER §12.2` (e.g. `$27` = HP 10/15/18, ATK 12/16/20)
* **Confidence:** CONFIRMED
* **Alternative Explanations:** the `+1` could belong to a different field — rejected because the same `+1` appears in the extraction of three independent types
* **Open Questions:** which palette index each round uses

---

## K. Bosses (3 records)

### EV-BOSS-01 — Boss stat initialiser is a 4-way switch
* **Subsystem:** Bosses / Difficulty
* **Claim:** `$017EDC` derives boss attack and HP from two byte tables (`$017F26`, `$017F2A`) with a 4-way difficulty switch (half / +5 / double / double+5) plus a round-7 bonus and a flat +2 attack.
* **Evidence:** `$017EDC`–`$017F24` disassembly; tables at `$017F26`–`$017F2D`.
* **Evidence Type:** static code + table decode
* **Location:** `$017EDC`–`$017F2D`
* **Relevant Function:** boss init
* **Relevant Address/Offset:** `$017F26`, `$017F2A`
* **Experiment:** `extract_core_tables()` computes the scaled matrix
* **Result:** `$55`: 20/32, `$56`: 20/24, `$57`: 32/30, `$58`: 32/32 (base), with the scaled variants tabulated in `DOSSIER §13.2`
* **Confidence:** CONFIRMED
* **Alternative Explanations:** `$FFC6` could be a loop counter rather than difficulty — rejected because `$011992` initialises it to 1 and the options menu writes 0..3
* **Open Questions:** none

### EV-BOSS-02 — Mr. X is a two-escort sequencer
* **Subsystem:** Bosses
* **Claim:** Type `$33` spawns escorts `$34` (at X−8) and `$38` (at X+8), stores them at `+$50`/`+$52`, and commands their state bytes directly via a `$FA78` handshake.
* **Evidence:** `$012BB2`–`$012BE8` (spawn), `$012C0A`–`$012D9C` (handshake), `$012DBA`/`$012DFA` (escort commands).
* **Evidence Type:** static code
* **Location:** `$012B5C`–`$012F14`
* **Relevant Function:** type `$33` handler
* **Relevant Address/Offset:** `$012BD8`, `$012DBA`, `$FA78`
* **Experiment:** —
* **Result:** 26-state table at `$012B64`; phase = escort state, not HP threshold
* **Confidence:** HIGH CONFIDENCE
* **Alternative Explanations:** `$FA78` could be a shared cinematic flag with another actor
* **Open Questions:** the exact death trigger chain (`$012CE0` requires `$FA72` bit3 — who sets it?)

### EV-BOSS-03 — Bosses are exempt from the police sweep and from despawn
* **Subsystem:** Bosses
* **Claim:** The police special skips bosses and the despawn path skips everything at/above `$D100` and specific types.
* **Evidence:** `$0094C6`–`$009504` (type/flag tests before the kill write); `$00B132`–`$00B178`.
* **Evidence Type:** static code
* **Location:** `$0094C0`–`$009504`, `$00B132`
* **Relevant Function:** police sweep / despawn
* **Relevant Address/Offset:** `$0094EE`, `$00B146`
* **Experiment:** —
* **Result:** bosses are only killed by their own handlers
* **Confidence:** HIGH CONFIDENCE
* **Alternative Explanations:** the skip could be based on HP rather than type
* **Open Questions:** none

---

## L. Level architecture (3 records)

### EV-LVL-01 — Compacting, retry-tolerant spawn script
* **Subsystem:** Level
* **Claim:** Spawn scripts are groups of 6-byte records terminated by `$99`; a record spawns only if its difficulty bits pass and its `bit7` is clear; failed spawns are retried next frame by rewinding `$FC14`.
* **Evidence:** `$000784`–`$000964` (`$0007A6` difficulty compare, `$0007AC` bit7 clear, `$0007DC` rewind, `$0008D0` compaction).
* **Evidence Type:** static code
* **Location:** `$000700`–`$000D5x`
* **Relevant Function:** spawn interpreter
* **Relevant Address/Offset:** `$FC14`, `$FC28`, `$FC2C`, `$FB5B`
* **Experiment:** —
* **Result:** record layout `[type|$80][?][?][?][diff&3|flags][flags]`, 15 bytes/group header + records
* **Confidence:** HIGH CONFIDENCE (parser), PROBABLE (fields)
* **Alternative Explanations:** `+$01`/`+$02` may carry coordinates consumed by a code path not yet isolated
* **Open Questions:** `U-LVL-01`

### EV-LVL-02 — Terrain is a 16-tile height map
* **Subsystem:** Level
* **Claim:** Each round's walkable surface is a 4-bit-per-cell plane at `$FFA000` with only 16 distinct tile values, mapped to height and stand-threshold by `$FC34`/`$FC38`.
* **Evidence:** `$00AD2A`–`$00AD8C` (see EV-MEM-04) and the two `movea.l` table loads.
* **Evidence Type:** static code
* **Location:** `$00AD2A`
* **Relevant Function:** ground query
* **Relevant Address/Offset:** `$00AD54`, `$FC34`, `$FC38`
* **Experiment:** —
* **Result:** no platform objects; height is a per-tile property
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** `U-LVL-02`

### EV-LVL-03 — Camera locks are three flattened scroll lines
* **Subsystem:** Level / Camera
* **Claim:** The only explicit scroll lock writes three fixed words `$06D7` into `$FF6038` when the *other* player is in state `$0F`.
* **Evidence:** `$0115F4`–`$011626`.
* **Evidence Type:** static code
* **Location:** `$0115F4`–`$011626`
* **Relevant Function:** background column streamer
* **Relevant Address/Offset:** `$011610`, `$01161A`
* **Experiment:** —
* **Result:** visual lock, not a logical camera stop
* **Confidence:** HIGH CONFIDENCE
* **Alternative Explanations:** the three writes could be a HUD reset rather than a lock
* **Open Questions:** none

---

## M. Rendering (3 records)

### EV-RND-01 — 8-byte SAT record emission with a hard 79-sprite budget
* **Subsystem:** Rendering
* **Claim:** Sprites are emitted as 8-byte records (`Y`, size/link, index, tile|flip, X) into `$F600`, limited to 79 per frame by `$FA03 = $4F`.
* **Evidence:** `$00B00E`–`$00B040` writes; `$00AE9C` initialises `$FA03`; `$00B040` decrements.
* **Evidence Type:** static code
* **Location:** `$00AE96`–`$00B048`
* **Relevant Function:** sprite builder
* **Relevant Address/Offset:** `$FA02`, `$FA03`, `$F600`
* **Experiment:** —
* **Result:** budget exhaustion visibly drops sprites (matches known behaviour)
* **Confidence:** CONFIRMED
* **Alternative Explanations:** `$4F` could be a per-object cap rather than a global one — rejected because it is only decremented/limited globally
* **Open Questions:** none

### EV-RND-02 — Three-level Y/depth/priority sort
* **Subsystem:** Rendering
* **Claim:** Draw order = Y-bucket (64 buckets of `$20`, keyed by `(screenY*8)&$FFE0`), then insertion sort by `+$14` depth, tie-broken by `+$01` bit7.
* **Evidence:** `$00AE4C`–`$00AE8C` (bucket insert), `$00AEC4`–`$00AF34` (bucket walk + depth insertion sort).
* **Evidence Type:** static code
* **Location:** `$00AE4C`, `$00AEE4`
* **Relevant Address/Offset:** `$E200`, `+$14`, `+$01` bit7
* **Experiment:** —
* **Result:** no z-buffer, no floating point, no per-sprite priority word
* **Confidence:** CONFIRMED
* **Alternative Explanations:** the insertion sort could be on sprite size
* **Open Questions:** none

### EV-RND-03 — Six display modes with literal VDP programs
* **Subsystem:** Rendering
* **Claim:** `$FF06` selects one of six VDP register programs in V-Blank; mode 5 writes a plane-B scroll table at VRAM `$C000`.
* **Evidence:** `$019D92` dispatch table; programs at `$019DF0`/`$019E1E`/`$019E5A`/`$019E96`/`$019ECE`/`$019F06`.
* **Evidence Type:** disassembly
* **Location:** `$019DC4`–`$01A06C`
* **Relevant Function:** V-Blank mode dispatch
* **Relevant Address/Offset:** `$FF06`, `$019D92`, `$019E7A`
* **Experiment:** decoded each VDP longword command (e.g. `$73400081` → VRAM `$3340`)
* **Result:** plane A H-scroll table at `$3340`; mode purposes tabulated in `DOSSIER §15.5`
* **Confidence:** CONFIRMED (bytes), PROBABLE (purposes)
* **Alternative Explanations:** mode numbering may not match scene types 1:1
* **Open Questions:** which master state uses which mode

---

## N. Animation (1 record)

### EV-ANM-01 — Variable-length sprite-run frames, timing == hitbox counter
* **Subsystem:** Animation
* **Claim:** Animation data is a byte stream: `[lastFrame][framesPerTick][count][y,size,tile,x]×count …`; the frame index doubles as the damage-table index.
* **Evidence:** `$00AFD2`–`$00B0E6`; `$0041EA` using `+$0A`.
* **Evidence Type:** static code
* **Location:** `$00AF46`–`$00B0E6`
* **Relevant Function:** sprite builder / animation advance
* **Relevant Address/Offset:** `+$0A`, `+$0C`, `+$0D`, `$FA40`
* **Experiment:** —
* **Result:** no fixed frame size; `$FA40` holds the loop point
* **Confidence:** CONFIRMED
* **Alternative Explanations:** the count byte could be a length rather than a sprite count — rejected because it is used as a `dbra` counter over 5-byte records
* **Open Questions:** full data dump (`U-CBT-01`)

---

## O. Audio (4 records)

### EV-AUD-01 — The 68k is the sequencer; the Z80 is a register proxy
* **Subsystem:** Audio
* **Claim:** Stream parsing, frequency computation and pitch effects run on the 68k (`$072914` every V-Blank); register writes are delivered into Z80 RAM (`$A01FFF`) under BUSREQ.
* **Evidence:** `$07291A`–`$072A16` channel loops; `$072AD4` (`move.b $10(a3),$a01fff.l`); `$072A88`/`$072B30` BUSREQ pairs; the decompressed Z80 image contains no stream decoder at its executed entry.
* **Evidence Type:** static code + ref-impl + exec
* **Location:** `$072914`–`$073CFF`; Z80 image
* **Relevant Function:** sound tick / Z80 driver
* **Relevant Address/Offset:** `$072914`, `$A01FFF`, `$A11100`
* **Experiment:** `EXP-01` decompression + disassembly of the Z80 image entry
* **Result:** architecture confirmed; song data lives entirely on the 68k side
* **Confidence:** HIGH CONFIDENCE
* **Alternative Explanations:** the Z80 could contain an unused sequencer that is simply not the executed path
* **Open Questions:** `U-AUD-01`

### EV-AUD-02 — Z80 driver size, hash and Δ-PCM table
* **Subsystem:** Audio / Assets
* **Claim:** The Z80 driver is 7,936 bytes (`$1F00`), decompressed from `$0795A2` (7,581 bytes), SHA-256 `07cabd01…88fd2`, and uses a 16-entry signed Δ-PCM step table.
* **Evidence:** `EXP-01`; the Python Kosinski decoder and the ROM's own `$0085A2` produce identical bytes; Δ table at Z80 `$001E`.
* **Evidence Type:** ref-impl == exec
* **Location:** ROM `$0795A2`–`$07B33E`; Z80 `$0000`–`$1EFF`
* **Relevant Function:** Kosinski `$0085A2`; Z80 entry
* **Relevant Address/Offset:** `$0795A2`, `$0085A2`
* **Experiment:** `EXP-01` (68,950 MC68000 instructions executed; 7,581 bytes consumed)
* **Result:** both methods agree exactly
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** none

### EV-AUD-03 — Sample descriptor table with two ROM banks
* **Subsystem:** Audio
* **Claim:** 17 DAC commands `$81`–`$91` map to 5-byte descriptors (start, length, pitch) with three source regions: resident Z80 RAM, ROM bank A, ROM bank B.
* **Evidence:** Z80 `$019B` table; bank selection from `$1FFA`/`$1FFB` at Z80 `$0050`–`$0090`.
* **Evidence Type:** table decode
* **Location:** Z80 `$019B`–`$01EC`
* **Relevant Function:** Z80 DAC loader
* **Relevant Address/Offset:** Z80 `$019B`, `$1FF8`, `$1FFA`
* **Experiment:** decoded all 17 entries
* **Result:** table in `DOSSIER §17.3`
* **Confidence:** HIGH CONFIDENCE (entries), PROBABLE (bank split semantics)
* **Alternative Explanations:** `$1FFB` could be a bank *index* rather than a register value
* **Open Questions:** which song/round selects which bank

### EV-AUD-04 — Sound ID space is range-coded, not table-coded
* **Subsystem:** Audio
* **Claim:** IDs `$81`–`$91` = DAC samples, `$A0`–`$CF` = channel commands, `$E0`–`$E3` = transport, `≥ $E4` = silently dropped.
* **Evidence:** `$072D5C`–`$072D82` compare chain.
* **Evidence Type:** static code
* **Location:** `$072D08`–`$072F7A`
* **Relevant Function:** sound command dispatcher
* **Relevant Address/Offset:** `$072D62`, `$072D6A`, `$072D72`, `$072D7A`
* **Experiment:** —
* **Result:** confirmed by the three `cmpi` thresholds and the fall-through to the no-op exit
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** the full `$A0`-class sub-map

---

## P. Input (1 record)

### EV-INP-01 — Two-read TH polling with edge extraction
* **Subsystem:** Input
* **Claim:** Each pad is read twice (TH=0 then TH=1), merged, inverted, XORed with the previous raw value to get pressed edges; bit layout after inversion is Up,Down,Left,Right,B,C,A,Start.
* **Evidence:** `$00813C`–`$008190`; verified by `$0038C0` (bits 2/3 = horizontal), `$018906` (bit7 = pause), `$0052BE` (`andi.b #3` slot select).
* **Evidence Type:** static code
* **Location:** `$00810C`–`$008190`
* **Relevant Function:** `ReadPads` [desc]
* **Relevant Address/Offset:** `$FC04`, `$FC05`, `$A10003`
* **Experiment:** cross-checked the bit indices against three independent consumers
* **Result:** layout confirmed; `$FC06` semantics unresolved (`U-INP-01`)
* **Confidence:** CONFIRMED (layout), UNKNOWN (`$FC06`)
* **Alternative Explanations:** `$FC06` could mean "6-button detected" or "no pad"
* **Open Questions:** `U-INP-01`

---

## Q. Camera (2 records)

### EV-CAM-01 — 16-pixel dead zone and rate-limited follow
* **Subsystem:** Camera
* **Claim:** The camera only re-targets when the player moves more than one 16-pixel cell, and its velocity is clamped to ±3.0 in X and ±4.0 in Y.
* **Evidence:** `$018B52` (`eor.w d1,d0 / andi.w #$FFF0,d0 / beq`), `$018FCC`/`$019058` clamps.
* **Evidence Type:** static code
* **Location:** `$018B44`–`$019072`
* **Relevant Function:** camera limits / integrate
* **Relevant Address/Offset:** `$018B52`, `$018FCC`, `$019058`
* **Experiment:** —
* **Result:** camera can never jump; catch-up is a few frames
* **Confidence:** CONFIRMED
* **Alternative Explanations:** the clamp could apply to a scroll delta rather than a velocity
* **Open Questions:** none

### EV-CAM-02 — Plane scroll table generation with per-line scaling
* **Subsystem:** Camera / Rendering
* **Claim:** The H-scroll table is built per line with `muls`/`divs` against a per-entry scale, producing parallax by scaling the camera delta.
* **Evidence:** `$0190E0`–`$019128` (`muls.w (a3)+,d1 / divs.w (a3)+,d1`), table `$FF5000`.
* **Evidence Type:** static code
* **Location:** `$0190E0`–`$0191xx`
* **Relevant Function:** scroll table builder
* **Relevant Address/Offset:** `$01910C`, `$FF5000`
* **Experiment:** —
* **Result:** parallax is a real per-line multiplication, not a second camera
* **Confidence:** HIGH CONFIDENCE
* **Alternative Explanations:** the scale could be a line offset
* **Open Questions:** number of parallax bands per round

---

## R. Assets / compression (2 records)

### EV-AST-01 — Kosinski LZSS, bit-exactly re-implemented
* **Subsystem:** Assets
* **Claim:** The in-house LZSS uses 16-bit LSB-first descriptors with 4-byte-refill semantics; literals are `1`, short matches `00bb`, long matches `01`, `$00` = end.
* **Evidence:** `$0085A2`–`$008640`; independent Python implementation matches on a real asset (`$0795A2`).
* **Evidence Type:** ref-impl == exec
* **Location:** `$0085A2`, `$0795A2`
* **Relevant Function:** `KosinskiDecompress` [desc]
* **Relevant Address/Offset:** `$0085A2`
* **Experiment:** `EXP-01`
* **Result:** 7,581 → 7,936 bytes, identical SHA-256 from both methods
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** which of the two in-image copies is used for which asset class

### EV-AST-02 — Graphics decompress straight into VRAM
* **Subsystem:** Assets / Rendering
* **Claim:** The graphics loader streams Kosinski output directly to `$C00000` rather than through RAM.
* **Evidence:** `$008642`–`$008670` sets a VDP write command then `bsr $008192`; `$008192` writes decompressed bytes to `(a4)` = `$C00000`.
* **Evidence Type:** static code
* **Location:** `$008642`–`$008670`, `$008192`
* **Relevant Function:** bank loader
* **Relevant Address/Offset:** `$008672` (bank table), `$008192`
* **Experiment:** —
* **Result:** no staging buffer for tile art; explains V-Blank-blocking loads
* **Confidence:** HIGH CONFIDENCE
* **Alternative Explanations:** `$008192` could write to a RAM mirror that is later DMA'd
* **Open Questions:** bank table inventory (`U-VRAM-01`)

---

## S. RNG (1 record)

### EV-RNG-01 — 41-multiply LCG with implicit seed
* **Subsystem:** RNG
* **Claim:** `state' = ((lo+hi)<<16) | lo` where `lo,hi` are the halves of `state*41`; the returned word is `lo+hi`; a zero state is replaced by `$2A6D365A` for that call only.
* **Evidence:** `$0104D8`–`$010500`; executed 16 times on MC68000 and compared against the closed form.
* **Evidence Type:** exec
* **Location:** `$0104D8`–`$010500`
* **Relevant Function:** `Rand16` [desc]
* **Relevant Address/Offset:** `$0104D8`, `$FF40`
* **Experiment:** `EXP-02`
* **Result:** 16/16 identical; first outputs `$7FE7,$6115,$388B,$9BF8,…`
* **Confidence:** CONFIRMED
* **Alternative Explanations:** none
* **Open Questions:** none

---

## T. Hidden / dead / unused code (3 records)

### EV-DEAD-01 — A working name-entry cheat exists in both revisions
* **Subsystem:** Hidden
* **Claim:** `$005920` compares `$FF0C`/`$FF14` against six 4-byte 1-based letter codes and, on match, sets BCD lives from `$005970+d7` and `$FF35 = d7`.
* **Evidence:** `$005920`–`$005956` plus tables at `$005958` and `$005970`.
* **Evidence Type:** static code + table decode + exec
* **Location:** `$005920`–`$005976`
* **Relevant Function:** `NameEntryCheat` [desc]
* **Relevant Address/Offset:** `$005920`, `$005958`, `$005970`, `$FF35`
* **Experiment:** `EXP-04` — executed with all six codes plus a control
* **Result:** `MOM`→90 lives/6 calls, `SUN`→49/5, `UDI`→9/4, `BO `→7/3, `ORE`→1/2, blank→0/1; `AXL` unchanged
* **Confidence:** CONFIRMED
* **Alternative Explanations:** it could be a *high-score name* bonus rather than a cheat; both readings are recorded
* **Open Questions:** original trigger (removed caller vs. never wired)

### EV-DEAD-02 — No code path reaches `$005920`
* **Subsystem:** Hidden
* **Claim:** The cheat is unreachable in the shipped build.
* **Evidence:** full-image scan for 32-bit literals, 16-bit literals, absolute-long jumps, PC-relative displacements and 8-bit branches targeting `$005920` → zero hits; the routine is not in any jump table.
* **Evidence Type:** negative search
* **Location:** whole image
* **Relevant Function:** —
* **Relevant Address/Offset:** `$005920`
* **Experiment:** automated reference scan (4 encodings × whole ROM)
* **Result:** 0 references
* **Confidence:** CONFIRMED
* **Alternative Explanations:** a computed jump could reach it (index built at runtime) — no table contains the value, and no `add`/`lea` producing `$5920` exists
* **Open Questions:** intent

### EV-DEAD-03 — Unused type range and dead player states
* **Subsystem:** Hidden
* **Claim:** Types `$02`,`$03`,`$2B`–`$2F`,`$3A`–`$3D`,`$59`–`$5F`,`$8F` are `rts` stubs; `$90`–`$95` resolve past the ROM; 13 player-state slots point at `$000000`.
* **Evidence:** table values at `$00B236`; player table `$001CE2`.
* **Evidence Type:** table decode
* **Location:** `$00B236`, `$001CE2`
* **Relevant Function:** both dispatch tables
* **Relevant Address/Offset:** `$00B236`, `$001CE2`
* **Experiment:** full enumeration of both tables
* **Result:** lists in `DOSSIER §7.3`, `§23.7`, `§23.8`
* **Confidence:** CONFIRMED (values), UNKNOWN (reachability)
* **Alternative Explanations:** the stubs could be intentional "no-op actor" slots used by scripts
* **Open Questions:** `U-STATE-01`, `U-DISP-01`
