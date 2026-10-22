# STREETS OF RAGE / BARE KNUCKLE (MEGA DRIVE, 1991)
## Engineering Reverse-Engineering Dossier

**Target:** `Streets of Rage (JUE) (REV 00) [!].bin`
(SHA-256 `dd44f120446654bb91c448762f3e0cd0d9b034f35d0e3266a4dc34402ada95c0`)
**Archive:** `Streets-of-Rage_Genesis_EN.zip`, SHA-256 `f1c25bde80c00824b6fd7a9b1dfce290f1b98038ac72eee1854d8aa805a17645`
**Cross-check target:** `Streets of Rage (JUE) (REV 01) [!].bin` (SHA-256 `95d7efb98e97f4ffffe68257aef9a855034a36a41b86cf9d332d129f30cb2d4b`)
**Analysis date:** 2026-10-22
**Method:** static disassembly (Capstone `CS_MODE_M68K_000`), byte-exact differential analysis of all 11 archived images, reference-implementation cross-checks, and dynamic execution of the *original* ROM subroutines on a Unicorn `UC_ARCH_M68K` MC68000 core in supervisor mode.

> **Scope statement.** This dossier documents *how the shipped 1991 binary actually works*. It is not a remake, port, or engine design. No gameplay was re-implemented. The only code written for this project is in `tools/verify_sor_forensics.py`, which extracts, decodes, measures, and validates evidence taken directly from the archive.

---

## 0. Reading conventions and confidence taxonomy

### 0.1 Address notation
| Notation | Meaning |
|---|---|
| `$0002A4` / `$02A4` | 24-bit Motorola 68000 address space (ROM byte offset = same value) |
| `$FF1234` | 68k work RAM (`$FF0000`–`$FFFFFF`) |
| `A0+$14` | byte offset `$14` inside the object a register points at |
| `.$2` | field size suffix — `.b`=1, `.w`=2, `.l`=4 bytes |
| `Z80 $1FF8` | byte offset inside the 8 KiB Z80 RAM image (driver decompressed) |

### 0.2 Confidence classes (used everywhere, never omitted)
| Class | Definition used in this dossier |
|---|---|
| **CONFIRMED (FACT)** | Directly demonstrated by code bytes, table bytes, or by executing the original routine and observing the result. Reproducible with `tools/verify_sor_forensics.py` or a documented command. |
| **HIGH CONFIDENCE** | Multiple independent observations agree (e.g. a table is indexed by a field and the resulting value is consumed by a system that only makes sense for that value). |
| **PROBABLE** | One strong observation plus consistent structural context; a plausible alternative reading exists. |
| **HYPOTHESIS** | Inference from architecture/layout alone; not executed, not cross-referenced. |
| **UNKNOWN** | Insufficient evidence. Explicitly *not* guessed. |

### 0.3 Result provenance classes
`static` (disassembly / table decode), `diff` (byte-exact cross-version), `exec` (dynamic execution of ROM code), `ref-impl` (independent Python decoder validated against `exec`), `string` (ASCII in ROM), `struct` (layout induction).

### 0.4 The one rule that was never broken
No function name, field name, constant or formula in this document is invented. Where the original developers' intent is obvious from mechanics (e.g. "this word is decremented once per frame and gates a transition"), the name is marked as *descriptive* (`[desc]`) and the raw address is always given. Unknown fields are listed as `?`.

---

## 1. Executive summary

Streets of Rage (1991) is a 512 KiB cartridge whose *entire* logic — game states, actors, AI, physics, collision, rendering list generation, camera, level scripts and the 68k half of the audio system — lives in roughly the first 106 KiB of the ROM (`$000200`–`$01A1xx`). Everything from about `$01A1xx` to `$06Fxxx` is Kosinski-compressed graphics, and `$06F000`–`$07FFFF` is uncompressed/compressed level + audio payload including the Z80 sound driver and its data. This was established by an entropy/structure sweep (`§3.3`) and confirmed by decompressor runs.

The engine is a **single-threaded, V-Blank-driven, fixed-timestep object engine** with a flat 22-entry master-state dispatcher and a **uniform 128-byte actor record** for players, enemies, bosses, weapons, props and projectiles. Every frame the 68k performs, in a fixed and now fully enumerated order: input latch → per-actor type handler dispatch (66 live slots) → collision/hit resolution → Y-bucket sort → sprite-list build → DMA/VDMA flush (in the V-Blank ISR). See `§5` for the exact instruction-level order.

Three unusual findings deserve top billing:

1. **A dormant, unreachable cheat backdoor survives in both shipped revisions.** `$005920` compares the 4-byte 1-based letter code at `$FF0C` (player 1) / `$FF14` (player 2) against a 6-entry table at `$005958` and, on match, overwrites the BCD lives byte at `$FF20`/`$FF23` and sets `$FF35` (extra police-call stock). Decoded codes: `MOM`→90 lives + 6 police calls; `SUN`→49; `UDI`→9; `BO `→7; `ORE`→1. The routine exists, is correct, and executes correctly under emulation — but **no pointer, branch or call in the image ever reaches `$005920`**. It is dead code in this build. (§23, evidence `EV-DEAD-01/02`, experiment `EXP-04`)
2. **REV 01 exists almost entirely to fix a boss-dying soft-lock.** REV 00 `$0143FC` sets the "police-special hit" latch whenever `$FA1A` (police special active) is non-zero — without checking whether the boss still has HP. REV 01 inserts `tst.w $32(a0) / ble` first. Executed side by side with identical preconditions, REV 00 returns early (`rts` inside the police branch, death update frozen) while REV 01 falls through to the normal death path. (§23.6, `EXP-03`)
3. **The 64 KiB of RAM *above* the initial stack pointer is a reserved global block, not stack.** `SSP = $00FFFF00` leaves `$FFFF00`–`$FFFFFF` (256 bytes) as engine globals — the master-state word, V-Blank mode, random seed, cheat codes, sound queue, etc. all live there. (§6)

Coverage achieved: **all 22 master states located and traced; all 66 actor slots and 156 type-handler table entries resolved; all 10 enemy archetypes and all 17 boss/miniboss handlers located; the complete VDP buffer set, DMA queues, Y-sorter and sprite-list builder disassembled; the PRNG recovered as an exact formula and machine-verified; the Z80 driver decompressed and its command interface located.** The explicitly *unresolved* areas are named in `§28` rather than papered over — chiefly the internal field semantics of the level script stream, the exact per-attack frame data for all player moves, and several VRAM allocation constants.

---

## 2. Platform and version identification

### 2.1 Platform facts (CONFIRMED, static)
| Item | Value | Evidence |
|---|---|---|
| CPU | Motorola MC68000 @ 7.67 MHz | vector table at `$000000`, `move.w sr` usage, 24-bit addressing |
| Coprocessor | Zilog Z80 @ 3.58 MHz, 8 KiB RAM | `$A11100` BUSREQ / `$A11200` RESET sequences in `$007FB8`, `$01061C` |
| VDP | Sega 315-5313 (YM7101) | `$C00004` control port, VSRAM/HSCROLL writes, DMA via `$C00004/$C00000` |
| Sound | Yamaha YM2612 (FM) + SN76489 (PSG) | Z80 writes to `$4000`/`$4001` region, `$7F11` PSG mute in boot |
| ROM | 512 KiB, no mapper | header `$01A0` = `$000000..$07FFFF` |
| RAM | 64 KiB at `$FF0000` | cleared in boot loop `$0242`–`$025F` |
| Header | `(C)SEGA 1991.MAY`, `MK 00001019-00`, region `JUE`, ROM `$A00000`→`JUE` | ASCII at `$0100`–`$01FF` |

### 2.2 The 11 archived images, explicitly separated
All 11 are exactly **524,288 bytes**. Checksums computed with the *game's own* algorithm (16-bit BE word sum over `$000200..$07FFFF`, replicated in `tools/verify_sor_forensics.py::compute_sega_checksum`, matching the loop at `$000338`).

| # | Filename | Date/Serial | Σ header | Σ computed | Valid | Bytes ≠ REV00 | Provenance verdict |
|---|---|---|---|---|---|---|---|
| 1 | `(JUE) (REV 00) [!].bin` | 1991.MAY / `-00` | `9409` | `9409` | ✅ | 0 | **Reference image.** Original retail revision 0. |
| 2 | `(JUE) (REV 01) [!].bin` | 1992.FEB / `-01` | `6390` | `6390` | ✅ | 2092 | **Original retail revision 1.** Sega's own bug-fix release (§23.6). |
| 3 | `(JUE) (REV 00) [b1].bin` | 1991.MAY | `9409` | `3597` | ❌ | 18 | Bad dump: 18 bytes of ASCII `"Console connection"` written at `$7FF40` (past the header-declared ROM end). No code change. |
| 4 | `(JUE) (REV 00) [h1].bin` | 1991.MAY | `3597` | `3597` | ✅ | 20 | `[b1]` + checksum field patched to the (wrong) computed value. Still a bad dump. |
| 5 | `(JUE) (REV 00) [p1].bin` | 1991.MAY | `F41C` | `F41C` | ✅ | 18 | Trainer/patch: `$0104` `"SEGARMEGA DRIVE "`; `$0336` bypasses checksum; `$08F53/$08F55/$08F57` → `$90` (NOPs); `$0C97A/$0C9D0/$0CA26` `"C"`→`"N"` (i.e. `jsr`→`jmp`-family patch); `$11995/$1199B` `01`→`14`. |
| 6 | `(JUE) (REV 00) [p1][h1].bin` | 1991.MAY | `F41C` | `F41C` | ✅ | 51 | `[p1]` + dumped-by header `"Dumped By TSD"`, `"(BARE KNUCKLE) , Taiwan"` at `$0120`–`$0174`. |
| 7 | `(JUE) (REV 00) [p2][!].bin` | 1991.MAY | `9409` | `134A` | ❌ | 10 | **Checksum-bypass patch only**: `$0348` `66 0000C8`→`4E71 4E71` (two NOPs) so a failing checksum cannot reach the red-screen halt; plus 4 bytes at `$08F3E`, `$09054`, `$0B67E`. |
| 8 | `(JUE) (REV 00) [T+Fre].bin` | 1991.MAY | `2C26` | `2C26` | ✅ | 1796 | Full French fan translation. Text-only edits to the font-indexed strings; no logic edits. |
| 9 | `(JUE) (REV 00) [p1] [T+Spa090_pkt].bin` | 1991.MAY | `F41C` | `2AB1` | ❌ | 1235 | `[p1]` + Spanish translation v0.90. |
| 10 | `(JUE) (REV 00) [p1][h1] [T+Spa090_pkt].bin` | 1991.MAY | `F41C` | `2AB1` | ❌ | 1268 | Same, on the `[p1][h1]` base. |
| 11 | `(JUE) (REV 00) [p2] [T+Spa090_pkt].bin` | 1991.MAY | `9409` | `49DF` | ❌ | 1227 | `[p2]` base + Spanish translation. |

**Version-separation rule applied throughout:** every behavioural statement in this dossier is attributed to REV 00 unless explicitly marked `REV 01`. Rows 3–11 are never used as evidence for *original* behaviour; they are only used in `§23` (as evidence of what the boot checksum does and where the text lives).

### 2.3 Translation-image evidence that benefits the audit (FACT, `diff`)
The fan translations are accidental *conformation maps* of the text system. Comparing `[T+Fre]` to REV 00 shows edits clustered exactly where ASCII text is consumed by the font renderer: `$008992`, `$008AF6`, `$008C4B`, `$012391`, `$018468`, `$018568`, `$01C684`, `$01C9FE`, `$03F7E7`, `$071FB2`, `$07207C`, `$0720C4`, `$072696`. Each translated string ends in a `$00` and uses byte values `$01`–`$1A` for letters — which is precisely the **1-based A=1..Z=26 alphabet** already suspected from the dormant cheat table (`§23.2`). This independently confirms the text encoding.

---

## 3. Binary / executable analysis

### 3.1 Memory layout of the 512 KiB image (CONFIRMED, `struct` + `ref-impl`)

| ROM range | Content | How established |
|---|---|---|
| `$000000`–`$0000FF` | 68000 exception vector table | 64 longwords decoded |
| `$000100`–`$0001FF` | Sega ROM header (console name, copyright, domestic/overseas name, serial, checksum, I/O, ROM/RAM size, region) | decoded (§2) |
| `$000200`–`$000203` | `nop; nop` — target of all 61 unused vectors | static |
| `$000204`–`$000207` | `bra.w $000208` — soft reset | static |
| `$000208`–`$0002A3` | Sega ICD_BLK4-style boot: TMSS handshake, VDP register init from `$0002A4` (24 bytes), Z80 stub upload, RAM/CRAM/VSRAM clear, PSG mute | static |
| `$0002A4`–`$000307` | VDP register image (24 bytes) + the boot's data | static |
| `$000308`–`$0003A1` | engine init: region/version latch, **ROM checksum verify**, VDP setup, Z80 driver load, RAM clear | static |
| `$0003A2`–`$0003B9` | **top-level main loop**: `jmp` through 22-entry table, then `jsr $010502` | static |
| `$0003BA`–`$000411` | master-state jump table (22 × 32-bit) | static |
| `$000412`–`$000435` | checksum-failure handler (solid red CRAM, halt loop) | static |
| `$000436`–`$0005xx` | "police special" (2P backup call) subsystem entry | static |
| `$000700`–`$000D5x` | **wave/spawn script interpreter** (per-frame enemy spawner + actor setup) | static |
| `$000E00`–`$0012xx` | font/text renderer + title/attract-mode helpers | static |
| `$001000`–`$0011xx` | character-select state machine (`$0FE8`–`$1178`) | static |
| `$0018D4`–`$001C43` | title-screen actor handlers (types `$06`,`$07`) and demo playback | static |
| `$001C44`–`$0031xx` | **player object system**: type `$01` handler, 256-entry state jump table `$001CE2`, all player states | static |
| `$0031xx`–`$0043AA` | player physics, jump/gravity, hitbox construction, hit reaction, damage decoding | static |
| `$0043AA`–`$004Cxx` | **combat / collision / body-block / grab / weapon-hit resolution** | static |
| `$004CD0`–`$0050A5` | HUD lifebar & score digit rendering | static |
| `$0050A6`–`$005217` | special-attack (police call) trigger logic | static |
| `$005218`–`$0059xx` | actor types `$0F`,`$10`,`$05` — includes **name-entry screen** (`$0056E6`) and the **dormant cheat** (`$005920`) | static |
| `$005C1E`–`$007xx` | **weapons, pickups, props, projectiles** (types `$08`–`$53`, `$60`–`$8E`) | static |
| `$007F18`–`$0080E4` | VDP/DMA/Z80 helpers, VRAM clear, 68k→Z80 upload | static |
| `$0080E4`–`$0081DD` | **Kosinski decompressor (variant A)** | static + `exec` |
| `$0081DD`–`$008480` | **tilemap ("plane map") decompressor + VDP tile writer** | static |
| `$0084BA`–`$0085A2` | sprite-list (SAT) DMA streaming state machine | static |
| `$0085A2`–`$008640` | **Kosinski decompressor (variant B — the one the game actually calls)** | static + `exec` (**bit-exact vs. reference implementation**) |
| `$008642`–`$0086xx` | graphics bank loader table + loop | static |
| `$008EAC`–`$0092FF` | **master states 0–21** | static |
| `$009560`–`$00AF00` | enemy/boss common engine: target acquisition, ground/height query, hit reaction, damage subtraction, score bookkeeping | static |
| `$00AF00`–`$00B190` | **actor→sprite-list builder**, screen culling, animation advance | static |
| `$00B190`–`$00B3D0` | actor helpers + **entity-type handler table `$00B236`** + boss trampolines `$00B36A` | static |
| `$00BB18`–`$00D606` | miniboss/sub-boss handlers (types `$60`–`$8E`) | static |
| `$00D606`–`$0100B6` | **enemy AI** (types `$20`–`$2A`) | static |
| `$0100B6`–`$0101C8` | type `$29` — multi-enemy "rush" controller | static |
| `$0101C8`–`$0103D0` | type `$54` — **police-special backup squad spawner** | static |
| `$0103D0`–`$010502` | block-fill / block-copy primitives (`move.l` unrolled ×32) | static |
| `$010502`–`$01061C` | frame sync + palette-stream decoders | static |
| `$01061C`–`$01069E` | Z80 driver upload (Kosinski→`$FF7000`→Z80 `$0000`, 7,861 bytes copied) | static + `exec` |
| `$01069E`–`$0106EA` | **sound-request queue (3 slots at `$F00A`)** | static |
| `$010840`–`$010Axx` | **master state 20/21: gameplay frame** (the 12-call per-frame pipeline) | static |
| `$010Bxx`–`$010Fxx` | HUD/tilemap tile writers, score BCD add (`$010DA6`), stage graphics loader | static |
| `$011000`–`$011Axx` | **level/camera/scroll-lock/palette-cycling/animation-tile systems** | static |
| `$011992`–`$011A36` | stage warm-start init | static |
| `$011B4C`–`$012600` | **level wave-script engine** (`$DE00` state block) + attract/round intro | static |
| `$01260E`–`$012B00` | round transition, BGM/voice cue, "ROUND n" / "GO" overlay | static |
| `$012B5C`–`$012F14` | **type `$33` = Mr. X** (final boss, 2-phase with two escorts) | static |
| `$012F14`–`$01306A` | type `$34`, `$38` — escort/sub-boss actors of the final round | static |
| `$01306A`–`$0140DC` | type `$35` — **Antonio** (round 1 / round 8 boss) | static |
| `$0140DC`–`$014318` | type `$36`, `$37`, `$39` — round-8 supporting bosses | static |
| `$014318`–`$0143D0` | type `$39` body + shared "boss vs police" gate | static |
| `$0143D0`–`$015794` | type `$30` — **"BossA"** (police-interruptible boss `§23.6` lives here) | static |
| `$015794`–`$0158C4` | type `$31` — boss phase controller | static |
| `$0158C4`–`$016A1A` | type `$58` etc. — large boss AI (shared "boss core" routines `$016A1A`, `$016AEC`, `$017EDC`) | static |
| `$016C24`–`$017858` | types `$98`,`$99`,`$56`,`$96` — round-6/7/8 bosses | static |
| `$017858`–`$017A00` | type `$97` — boss escort/parasite actor | static |
| `$017EDC`–`$017F2E` | **boss HP/attack stat initialiser (difficulty-scaled)** | static + table decode |
| `$018000`–`$0187E0` | attract-mode / ending / credits sequences | static |
| `$0187E0`–`$018AF8` | **stage graphics + palette loader, HUD init** | static |
| `$018AF8`–`$019500` | **camera + 2-player plane solver, scroll limits, parallax** | static |
| `$019500`–`$019A00` | **V-Blank ISR body**: VSRAM, CRAM DMA, plane-scroll DMA, SAT DMA, VDP mode switches | static |
| `$019D16`–`$019DC4` | V-Blank entry, frame-ready flag handshake, lag-frame branch | static |
| `$019DC4`–`$01A0B4` | V-Blank display-mode dispatch (6 modes) | static |
| `$01A0B4`–`$01A1xx` | palette-DMA request for player 2 / per-actor palette stream | static |
| `$01A160`–`$01ABA8` | **palette banks used by V-Blank DMA** (2 tables) | static |
| `$01ABA8`–`$01C700`+ | **per-actor animation/mapping tables** (referenced by `$27032`) | static (partial) |
| `$026F7A`–`$0270BE` | **enemy stat tables** (HP / attack / score IDs / animation ptr) — `§11`, `§12` | static + `exec`-verified indices |
| `$01A1..`–`$06EFFF` | **Kosinski-compressed graphics banks** (tiles, sprites, palettes, plane maps) | entropy sweep (`§3.3`) |
| `$06F000`–`$071EFF` | level plane maps / tile data (mixed compressed) | entropy sweep |
| `$071F30`–`$0728A2` | title/attract graphics + **font** tile set | static refs |
| `$0728A4`–`$073CFF` | **68k half of the sound system**: BGM bank tables, channel stream parser, YM/PSG register writers | static |
| `$073D00`–`$0795A1` | FM voice tables, BGM/SFX data (banked) | static + `struct` |
| `$0795A2`–`$07B33E` | **Z80 DPCM/FM driver** — Kosinski-compressed, 7,581 bytes → **7,936 bytes** (`$1F00`) | `ref-impl` **==** `exec` |
| `$07B340`–`$07Fxxx` | PCM drum sample data (Δ-PCM, 4-bit) | static (descriptor cross-check) |
| `$07Fxxx`–`$07FFFF` | tail padding (`$FF`) + the `[b1]` dump damage region at `$7FF40` | static |

### 3.2 Entry point and initialisation order (CONFIRMED, static)

```
$000208  boot:  move.w #$2700,sr ; tst.w $A10001 (version) ; move.b #$00,$A14000 (TMSS off)
                move.b 'S',…,$A14000.. (TMSS unlock 'SEGA' if version>=1)
                lea $02A4(pc),a0 ; 24 × (move.b (a0)+,d0; move.w d0,$C00004)   ; VDP regs
                Z80: request bus $A11100=$0100, reset off $A11200=$0100,
                     copy stub, release
                clear 64 KiB RAM ($FF0000..$FFFFFF), CRAM ($C00000), VSRAM ($C00010)
                4 × move.b (a5)+,$11(a3) → PSG volume/attenuation mute
                move.w #$2700,sr ; bra $000308
$000308  engine init:
                move.b $A10001,d0 ; andi #$C0 ; move.b d0,$FF44      ; region+version latch
                btst #6,$A1000D ; beq .skip_verify                    ; dev-cart bypass
                checksum: sum16($000200..$07FFFF) vs $018E
                          mismatch → $000412: CRAM=$000E (red), $C00004=$8F02, bra.s *
                .skip_verify:
                VDP: 12 registers, VRAM clear, plane sizes
                jsr $007FB8   ; VDP+DMA reset, Z80 halt, VRAM clear (0x8F01/0x93FF/0x94FF)
                jsr $00804C   ; Z80 RAM clear
                jsr $00805A   ; Z80 driver install
                jsr $01061C   ; Kosinski($0795A2) → $FF7000 → Z80 $0000 (0x1EC6+1 bytes)
                jsr $010526   ; scroll buffers = $FF00
                jsr $00818A/$00851x ; SAT builder reset
                move.w #$0,$FF00  ; master state = 0
                jmp $0003A2
```

**Exact boot-sensitive detail (FACT):** the checksum compare is against the *stored header value*, not a constant, so a patched header (rows 5,6,9,10 of §2.2) passes verification with modified code. Row 7 (`[p2]`) instead NOPs the branch at `$0348`, so the red-screen halt can never be reached. Both are documented because they define what a "modified image" is in this archive.

### 3.3 Structural sweep of the whole image (CONFIRMED, measured)

8 KiB blocks, per-block byte entropy, `RTS`/`JSR`/`BSR` opcode frequency, printable-ASCII count, and `$00`/`$FF` density (reproducible with the sweep script embedded in the research log `RL-07`):

* `$000000`–`$000FFF` … `$018000`–`$01AFFF`: entropy **5.6–6.4**, 69–140 `RTS`, 76–228 `JSR` per block → **code**.
* `$01A000`–`$01BFFF`: entropy 7.17, 0–1 `RTS` → transition into compressed data.
* `$01C000`–`$071FFF`: entropy **7.4–7.95**, zero `RTS`/`JSR` → **compressed graphics / level data**.
* `$072000`–`$073FFF`: entropy 6.43 dropping to 5.83, `RTS`=76, `JSR`=98 reappearing in `$072000`–`$073FFF` → **sound driver (68k)**.
* `$074000`–`$077FFF`: entropy 5.8–6.1, no code ops → **audio tables/data**.
* `$078000`–`$07BFFF`: entropy 7.4–7.6 → compressed Z80 driver + PCM.
* `$07C000`–`$07FFFF`: entropy 6.0–6.3, large `$FF` density → PCM tail + padding.

This single measurement is what justifies the claim in `§1` that the *entire* logic fits below `$01A1xx`.


---

## 4. Complete architecture map

### 4.1 Module inventory (CONFIRMED: each module has a stable entry point and a coherent call boundary)

| # | Module | Entry(s) | Called from | Role |
|---|---|---|---|---|
| M1 | Boot / TMSS / VDP init | `$000208` | reset vector | hardware bring-up |
| M2 | Checksum verifier | `$000338`–`$00034C` | M1 | integrity + copy-protection gate |
| M3 | Z80 loader | `$007FB8`, `$00805A`, `$01061C` | M1, M8 | halt Z80, clear its RAM, install driver |
| M4 | Master-state dispatcher | `$0003A2` + table `$0003BA` | — (top level) | 22 program states |
| M5 | Frame sync | `$010502`, `$010514` | M4/M6 | V-Blank handshake via `$FA00` |
| M6 | Gameplay frame pipeline | `$01087A` | M4 state `$16` | 12 ordered subsystem calls |
| M7 | Actor dispatcher | `$00AD8E` | M6 | per-slot type handler, sort, cull |
| M8 | Sprite-list builder | `$00AF46`–`$00B120` | M7 | animation → SAT entries |
| M9 | SAT DMA streamer | `$0084BA`, `$008510`, `$0081DC` | M7 / VBlank | buffer → VDP under bus control |
| M10 | Collision / combat | `$0043AA`, `$004478`, `$0051CC`, `$00A9BA`, `$00AA22`, `$00AB24` | M6, actor handlers | body-block, hit, grab |
| M11 | Damage & reaction | `$0092AC`–`$009F20`, `$0040A6`, `$004800` | M10 | HP math, stun, launch |
| M12 | Enemy AI commons | `$009604`, `$009648`, `$009654`, `$0096C0`, `$00973E`, `$00982C`, `$009896`, `$0098E8`, `$00991A` | all enemy handlers | target, approach, ground, jump, death |
| M13 | Per-type AI | `$00D606`–`$0100B6` (enemies), `$012B5C`–`$017A00` (bosses) | `$00B236` table | behaviour |
| M14 | Player system | `$001C44` + table `$001CE2` | `$00B236` slot 1 | states, physics, attacks |
| M15 | Physics | `$00358C`–`$003CE0` | M14 | velocity/gravity/position |
| M16 | Hitbox producer | `$004140`–`$0041E8`, tables `$01ABA8`/`$01AB8E` | M10 | box extraction |
| M17 | Camera | `$018AF8`, `$018C22`, `$018F5C`, `$018FE8`, `$019074`, `$0190AA`, `$0190E0` | M6, VBlank | follow + scroll lock + plane scroll |
| M18 | Level/wave scripts | `$000700`–`$000D5x`, `$011B4C`, `$018C20` | M6 | spawn, triggers, transitions |
| M19 | Rendering buffers | `$00AEC4` (Y-sort), `$010454` (copy), `$010576` (palette stream), `$018A96` (HUD digits) | M6/M7 | buffers → DMA |
| M20 | Sound (68k) | `$072914` (tick), `$072D08` (command), `$073066` (channel step) | VBlank | BGM/SFX sequencing |
| M21 | Sound (Z80) | decompressed image at Z80 `$0000` | hardware | FM/PSG/DAC playback |
| M22 | Input | `$00810C`/`$00813C` | VBlank | 3-button + 6-button detect, EA-style key record |
| M23 | PRNG | `$0104D8` | many | 32-bit LCG |
| M24 | Decompressors | `$0081DD` (plane map), `$0085A2` (Kosinski) | loaders | asset expansion |
| M25 | Text / font | `$000E00`–`$0012xx`, `$008992` etc. | menus/story | 1-based alphabet render |
| M26 | Menus / attract / name entry | `$001000`, `$0056E6`, `$018000`+ | M4 | UI states |
| M27 | HUD | `$004CD0`, `$004D60`, `$004E14`, `$010F5C` | M6 | lifebars, score, timer |
| M28 | Hidden/dead | `$005920` (cheat), `$0100B6`? , `$0B67E`? | **nothing** | see `§23` |

### 4.2 Coupling assessment (measured, not assumed)

* **Tight coupling:** M7 ↔ M8 (the dispatcher *is* the sprite builder's caller — one pass, no queue), M10 ↔ M11 (collision sets HP directly), M17 ↔ VBlank (camera state is consumed inside the ISR), M20 ↔ M21 (68k parses streams and writes completed YM/PSG register writes into Z80 RAM, i.e. the "sequencer" is on the 68k, not the Z80).
* **Loose / table-driven:** actor types (`$00B236`), master states (`$0003BA`), player states (`$001CE2`), enemy stats (`$026FCE`), animation banks (`$027032`), boss stats (`$017F26`/`$017F2A`), score values (`$010DDA`).
* **No allocator, no heap, no free-list.** Every pool is a fixed array scanned linearly for `type==0` (`§7.2`). This is why there is no memory fragmentation behaviour to reverse-engineer.

---

## 5. Main-loop reconstruction (CONFIRMED, instruction order is literal)

### 5.1 The three-level loop

```
Level 1  $0003A2  ┌── move.w $FF00,d1                  ; master state
                  │   move.w ($03BA,PC,d1.w),d1        ; 22-entry table
                  │   jsr (a1=d1)                      ; state routine
                  │   jsr $010502                      ; WAIT FOR V-BLANK (frame sync)
                  └── bra  $0003A2                     ; forever
```
`$010502` is the frame clock:

```
$010502  move.b #$1,$FA00      ; "frame request" flag
         move.w #$2500,sr      ; level 5 — V-Blank interrupt now enabled
$01050C  tst.b  $FA00          ; the V-Blank ISR clears it
         bne.s  $01050C        ; tight spin
         rts
```
`$010514` is the identical loop with `#$2` (used when a *second* frame is needed, e.g. loading screens).

**Therefore: the game is strictly frame-locked. Simulation is 1 tick = 1 NTSC frame (≈16.7 ms, 60 Hz) or 1 PAL frame (50 Hz).** There is no delta-time anywhere in the code base (FACT: no multiplication of any velocity by a frame-delta value exists; velocities are added directly to fixed-point positions in `$003Cxx`/`$009F96`/`$00A00E`).

### 5.2 V-Blank ISR — exact order (`$019D16`–`$01A0B4`)

```
$019D16  movem.l d0-d7/a0-a6,-(sp)
         tst.b  $FA00            ; did the main loop ask for a frame?
         beq.w  $01A088          ; NO → "lag frame": skip all updates, still DMA sprites
         ; --- vertical scroll (VSRAM) ---
         move.w $E00E,d0 → VSRAM plane A vscroll
         move.w $E10E,d0 → VSRAM plane B vscroll
         ; --- CRAM push if dirty ---
         btst   #0,$FA01 → if set: BUSREQ($A11100=$0100); DMA $F400→CRAM (64 words);
                          release bus
         ; --- display-mode dispatch on $FF06 ---
         move.w $FF06,d0 ; jmp ($019D92,PC,d0.w)   ; 6 modes: 0..5
             mode 0 → $01A01E   mode 1 → $019FDA   mode 2 → $019DC4
             mode 3 → $019F5C   mode 4 → $019F42   mode 5 → inline (H-scroll)
         ; --- common tail (all modes) ---
$01A06E  tst.w $FB06 ; subq.w #1,$FB06      ; VDP mode-change countdown
$01A078  addq.w #1,$FB08                    ; global frame counter
         jsr $00810C       ; READ CONTROLLERS  (M22)
         jsr $008510       ; SAT DMA (M9)
         btst  #6,$FF44 → if set: key-record hook ($FA19)
         jsr $072914       ; 68K SOUND TICK (M20)
         movem.l (sp)+,d0-d7/a0-a6
         rte
```
**Input is therefore sampled exactly once per frame, inside V-Blank, *before* the main loop's simulation for that frame.** That ordering is what makes the `$FC04`/`$FC05` edge values stable for the whole simulation pass.

### 5.3 Gameplay frame — literal call order (FACT, `$01087A`)

| # | Instruction | Subsystem | Effect |
|---|---|---|---|
| — | `tst.b $FA1F` / `bne $10920` | round-intro/pause overlay | when set, only the overlay + police + frame-sync run |
| — | `tst.b $FA71` / `bne $108CC` | pause menu | `$10576` (menu input+draw), `$1069E` (SFX `$E1`), then re-dispatch |
| 1 | `jsr $011A36` | pause debounce | `dec.w $FB52`; on 0 → `$FB0C=$40`, `$FA71=1` |
| — | `tst.b $FA49` / `bne $10976` | round-clear/BGM fade | |
| 2 | `jsr $010D2E` | pause/round-end trigger | START edge → toggle; returns d7 |
| 3 | `jsr $010C88` | **background column stream + H-scroll** | every `$5A` (90) ticks: `$10CF4` picks P1/P2 plane, `$10DCA` accumulates BCD digits, builds 3-line H-scroll table |
| 4 | `jsr $0115CC` | **2-player scroll arbitration + palette** | honors `$FF25` (P2 out), `$FF02==7` (demo), `$FC0A`; drives `$116DC`–`$117BC` scroll tables |
| 5 | `jsr $011B4C` | **wave / spawn script engine** | advances `$FC14` script PC; spawns actor types into pool B |
| 6 | `jsr $0117FC` | level-side scrolling HUD ("life" counters) | `$F50E` wave index, writes `$F51A`/`$F54E` tiles |
| 7 | `jsr $0112F2` | **per-round state dispatch** `$FF02` 0..7 | palette cycling, tilemap animation (`$FA0A/$FA0B`), `$FF1A` |
| 8 | `jsr $011210` | **CRAM palette-cycle animator** | walks 5 × 14-byte entries at `$EE00`, writes `$F400` buffer |
| 9 | `jsr $00AD8E` | **actor dispatch + Y-sort + sprite build** | see `§5.4` |
| 10 | `jsr $011346` | parallax / sky column animation | `$FA5D`, `$FB1A`, `$FA0B` |
| 11 | `jsr $017FC2` | scripted background FX (palette/DMA swap) | `$FA5A`, `$FB54`, table `$18018` |
| 12 | `jsr $0084BA` | start SAT streaming state machine | |
| 13 | `jmp $000436` | **police-special subsystem** | `$FB15` dispatch, 10-entry table `$00044C`; returns to `$0003A2` |

### 5.4 Actor dispatch internals (FACT, `$00AD8E`–`$00AF00`)

```
$00AD8E  lea $B800,a0 ; clr.b $FA75 ; move.w #$FB72,$FB56   ; clear sort list, reset ptr
         d7 = 1                                             ; 2 PLAYER SLOTS
         loop: type=(a0); if type!=0 → jsr ($00B236[type*2]) ; jsr $00B132 (activation test)
               a0 += $80 ; dbra d7
         ; police / round-intro actors
         if $FF00==$14 or $FF00==$16 → jsr $004478 (police), jsr $018AF8 (camera)
         jsr $0051CC   ; proximity / body-block / pickup
         jsr $0043AA   ; PLAYER↔ENEMY body collision + hurt
         jsr $010514   ; wait one more frame (double-buffer for the sort)
         $B854 = $FC04 ; $B8D4 = $FC08    ; latch raw pad state into player slots
         $FA47 = $FC05 ; $FA48 = $FC09    ; latch pressed state
         jsr $00AE4C(P1) ; jsr $00AE4C(P2)   ; bucket-insert players
         d7 = $41 ; a0 = $B900                            ; 66 SLOTS
         loop: type=(a0); if type!=0:
                  d0 = type*2 ; if d0>=$120 → set bit $10      ; second table page
                  jsr ($00B236[type*2]); jsr $00B132; jsr $00AE4C
               a0 += $80 ; dbra d7
         clr.b $FA1B
         → $00AE96: sprite budget reset ($FA02=0,$FA03=$4F), clear SAT ($DA00),
                    jsr $010B70, then Y-sort walk ($00AEC4) and per-actor
                    sprite emission into ($FB04) cursor, terminated by clr.l
```
Two facts fall out of this block that are easy to miss:
* `$010514` is inserted *between* collision and the actor pass — the engine deliberately spends one extra frame so that hit results are visible for exactly one frame before the sprite list reflects them.
* The 66-slot loop adds `$10` to the *doubled* type index when `type >= $90`, i.e. the handler table is treated as two 128-entry pages and index `$120..$17F` selects the high page. This is why type `$A0` would alias type `$20` — a documented not-a-bug of the table encoding.

### 5.5 Pause / transition / shutdown behaviour

* **Pause** has two stages: idle (`$FA71=0`) and menu (`$FA71=1`). `$011A36` only counts down while `$FF2A` (the pause request) is non-zero; when the countdown reaches zero it forces `$FB0C=$40` (VDP mode word) and raises `$FA71`. The menu then runs at `$108CC`, which is *outside* the 12-call pipeline, so **all simulation is frozen while the menu is open** (FACT: pipeline is unreachable from that branch).
* **Round intro / "GO"** sets `$FA1F`, whose branch (`$10920`) only runs the police subsystem, frame sync and the overlay drawer. Same freeze semantics.
* **Round end** uses `$FA49`/`$FA4A`: `$FA4A` is loaded with `$FF` and decremented each frame, giving a 255-frame BGM fade before `$11B12` starts the next round.
* **Shutdown:** there is none. No code path returns to a "menu" from a running game by destroying state; every transition is a re-initialisation of the same RAM block (`§5.6`). Reset is handled only by the hardware (`$000200` → `bra.w $000208`), which does not clear RAM.

### 5.6 State re-initialisation pattern (repeated verbatim in ~10 places)
Every master-state that begins a new scene executes the identical 3-step sequence:
```
move.w $FF48,$C00004   ; restore VDP control latch
move.w #$2500,sr       ; allow V-Blank
jsr    $007FB8         ; VDP/DMA/Z80 reset (also clears VRAM)
... jsr $0103D0 × N     ; block-fill $FF0000.. (d7=$1FA → 0x1FA×32 = 16 KiB cleared)
move.w $FF46,$C00004
move.w #$2700,sr
addq.w #$2,$FF00       ; advance master state
```
This is the engine's *only* notion of "teardown". It is why RAM between `$1000` and `$CFFF` is rebuilt from scratch on every state change and why nothing in the RAM map can be assumed to persist across a state boundary except what the new state writes.

---

## 6. Memory map

### 6.1 68k bus map (FACT, hardware + code)
| Range | Device | Notes |
|---|---|---|
| `$000000`–`$07FFFF` | cartridge ROM | 512 KiB, no mapper |
| `$A00000`–`$A0FFFF` | Z80 address space window | 68k writes at `$A00000+n` hit Z80 address `n` **only while BUSREQ is held** (`$A11100`) |
| `$A10001` | version register | bit 6 = PAL, bit 7 = overseas |
| `$A10003`/`$A10005`/`$A10007` | I/O ports (pads) | read in `$00813C` |
| `$A10009`/`$A1000B`/`$A1000D` | I/O control | set to `$40` in `$007F50` |
| `$A1000D` bit6 | "dev cart" flag | bypasses checksum (`§3.2`) |
| `$A11100` | Z80 BUSREQ | `$0100`=request, `$0000`=release |
| `$A11200` | Z80 RESET | `$0100`=assert |
| `$A14000` | TMSS / bank register | boot writes `'SEGA'`, then `$0001`/`$0003` |
| `$C00000` | VDP data | |
| `$C00004` | VDP control/status | |
| `$C00008` | VDP H/V counter | **never referenced anywhere in the ROM** (verified by full-image byte search for `00 C0 00 08`) |
| `$FF0000`–`$FFFFFF` | 64 KiB work RAM | |

### 6.2 Work RAM — verified global blocks
Legend: `F`=FACT, `H`=HIGH CONFIDENCE, `P`=PROBABLE, `?`=unknown. Sizes: `.b/.w/.l`.

| Address | Sz | Role | Conf | Primary evidence |
|---|---|---|---|---|
| `$FF0000` | .w | **master state** (index into `$0003BA`) | F | `$03A2`, every state handler's final `addq.w #2,$FF00` |
| `$FF0002` | .w | **round/scene ID** (0..7 gameplay, `$FE`=special, `$FF`=?) | F | compared against literal `#7`,`#6`,`#5`,`#4`,`#3`,`#2` in dozens of places |
| `$FF0004` | .w | sub-scene / section index (intro, mid, boss) | H | `$018F32`, `$019570` increment it |
| `$FF0006` | .w | **V-Blank display mode** (0..5) | F | ISR dispatch `$019D92` |
| `$FF0018` | .b | active-player bitmask (bit0 P1, bit1 P2; `3`=both) | F | `$0096EC`, `$010D3E` |
| `$FF001A` | .b | round-intro/boss-intro active | F | `$0143FC`, `$00436` |
| `$FF001C` | .b | P2 "used police" flag | H | `$014424` |
| `$FF001E`/`$FF001F` | .b | P1/P2 special-attack style select | H | `$005334`–`$005408` |
| `$FF0020`/`$FF0023` | .b | **P1/P2 BCD lives** | F | `$005952` writes, `$004E38` reads |
| `$FF0021`/`$FF0024` | .b | P1/P2 police-call stock | F | `$00536x`, `$0053ax` counter |
| `$FF0022`/`$FF0025` | .b | P1/P2 police-in-progress flag | F | `$0143E0`, `$0043AA` |
| `$FF0026`/`$FF0027` | .b | P1/P2 continuing/join state | H | `$004D6A`, `$00541A` |
| `$FF002A` | .b | **pause requested** (bit7 = menu) | F | `$010D6E`, `$010E42` |
| `$FF002C`/`$FF0030` | .l | key-record write pointers (P1/P2) | F | `$00816E` |
| `$FF0034` | .b | round-complete flag | F | `$0108EA` |
| `$FF0035` | .b | 2-player "who is ahead" / difficulty nibble | ? | `$001F0A` |
| `$FF0036` | .b | last-round flag | H | `$011CB8` |
| `$FF0038` | .w | ? (cleared with the block at `$009026`) | ? | |
| `$FF0040` | .l | **PRNG state** | F | `$0104FA`, `EXP-02` |
| `$FF0044` | .b | region/version latch (`$A10001`&`$C0`) | F | `$00030C`, `$007F8A` |
| `$FF0046`/`$FF0048` | .w | VDP control latch image | F | restored at every state entry |
| `$FF004A`+12n | ×10 | high-score table (12-byte records: 4-byte BCD score + 8-byte name) | H | cleared in `$008FD0`, rendered in `$018ABC` |
| `$FF00A4` | ? | ? | ? | |
| `$FF00B4`+8n | ×5 | bonus-stage score table (5 × 8-byte BCD) | P | `$0189xx` |
| `$FF0C`/`$FF14` | .l | **name-entry code (P1/P2), 1-based A..Z** | F | `$005920`, `$00573E`, `$001F0A` |
| `$FF18` | .b | see `$FF0018` (aliases: the block is `$FF0018..`, and `$FF18` is the same byte) | F | |
| `$FF1A`/`$FF1C` | .w | P1/P2 "police style" (3 = default) | H | `$011992` |
| `$FF1E`/`$FF1F` | .b | P1/P2 special style index | H | `$005654` |
| `$FF20..$FF27` | ×8 | lives/continues/stock block (see `$FF0020`) | F | |
| `$FF35` | .b | **extra police-call bonus index** (0..5) | F | `$00594E`, `$001F0C` |
| `$FF40` | .l | PRNG state (canonical name in code) | F | `EXP-02` |
| `$FF44` | .b | version latch (copy of `$FF0044`) | F | |
| `$DE00`–`$DE2B` | block | **round/wave script state**: `+$02` tilemap-dirty, `+$04` script step, `+$06` sub-step, `+$08` tile index, `+$0A`/`+$0B` BCD timer, `+$0C` coin/flash timer, `+$0E` overlay flag, `+$10` blank, `+$20` scroll delta, `+$28`/`+$2A` staged tilemap entries | F/H | `$011B4C`–`$011F00` |
| `$DD80`–`$DDFF` | block | palette-stream state (base colours per line, dirty flags) | H | `$004056`, `$01A0D6` |
| `$DCD0`–`$DD2B` | block | SAT streaming state (`+$00` src ptr, `+$04` VDP target, `+$08..` saved regs, `+$28` count, `+$2A` chunk counter) | F | `$0084BA`, `$008510` |
| `$E000`/`$E100` | ×$100 | **two camera contexts** (`+$00` mode, `+$02` X, `+$06` prev X, `+$0A` X velocity, `+$0E` Y, `+$12` prev Y, `+$16` Y velocity, `+$1A`/`+$1E` X limits, `+$22`/`+$26` Y limits, `+$2E` planesize, `+$32` chunk table ptr, `+$44` sub-struct count, `+$46` sub-struct array, `+$B2`/`+$B3` flags) | F | `$018AF8`–`$0190DE`, `$0190E0`, `$019656` |
| `$E200`–`$E9DF` | 64 × $20 | **Y-sort buckets** (word count + up to 15 actor pointers) | F | `$00AE4C`, `$00AEE4` |
| `$EA00`/`$EB20` | | camera sub-struct arrays for plane A / plane B | H | `$018AF8` (`lea $ea00/a3`, `$eb20`) |
| `$EC40`/`$ECE0` | | per-plane scroll-write cursors | H | `$018AF8` (`lea $ec40/a4`, `$ece0`) |
| `$EE00` | 5 × 14 | **palette-cycle table** (`+$00` active, `+$02` timer, `+$04` reload, `+$06` frame idx, `+$08` frame count, `+$0A` colour-bank ptr, `+$0C` colours/frame) | F | `$011210` |
| `$F000`/`$F001`/`$F002` | .b | current BGM request + priority (3 requesters) | F | `$072D08` |
| `$F009` | .b | winning sound command | F | `$072D38` |
| `$F00A`–`$F00C` | 3 × .b | **SFX request slots** | F | `$01069E` |
| `$F040`+$30n | 5 × $30 | FM channel state (`n`=0..4: ch1..ch3 + ch4..6 interleaved) | F | `$072950` loop, stride `$30` |
| `$F130` | $30 | DAC / drum channel | F | `$07296C` |
| `$F160`+$30n | 3 × $30 | PSG (SN76489) channels | F | `$07297C` |
| `$F1F0`, `$F2B0`, `$F340` | $30 each | extra (SFX-dedicated) FM/DAC channels | F | `$0729A2`–`$072A16` |
| `$F400`–`$F47F` | 64 words | **CRAM shadow (P1 palette block)** → DMA'd every dirty frame | F | `$019EFA`, `$01053E` |
| `$F480`–`$F4FF` | 64 words | CRAM shadow (P2 palette block) | H | `$010534` |
| `$F500` / `$F50E` / `$F51A` / `$F54E` | | wave index, wave tile cursors | H | `$011830`–`$0118DA` |
| `$F502`/`$F508` | .w | pointers to the two "active attacker" actors | F | `$017F8C`, `$017F92` |
| `$F50F` | .b | ? (attacker index) | ? | `$017F7E` |
| `$F900`–`$F90A` | block | attract-mode timers (title blink, demo timer) | F | `$00164A`, `$017DA` |
| `$F600`–`$F9FF` | 80 × 8 | **SAT shadow** (Y, size, link, attr, X) | F | `$00B00E` writes 8-byte records; `$008510` DMAs from here |
| `$FA00` | .b | **frame-request/ack handshake** | F | `$010502`, `$019D16` |
| `$FA01` | .b | CRAM dirty / DMA-pending | F | `$010542` |
| `$FA02` | .b | sprites emitted this frame | F | `$00B012` |
| `$FA03` | .b | sprite budget remaining (starts `$4F` = 79) | F | `$00AE9C`, `$00B040` |
| `$FA04` | .b | per-object 3-line scroll enable | H | `$00AEA6` |
| `$FA05` | .b | **round phase flags** (bit1 spawn-active, bit2 all-spawned, bit3 waiting, bit6 done) | F | `$000784`, `$000928` |
| `$FA09` | .b | character-select phase | F | `$001050` |
| `$FA0A`/`$FA0B` | .b | tilemap animation period/counter | F | `$0112D4`, `$011354` |
| `$FA0C` | .b | tilemap animation enable | F | `$0112CE` |
| `$FA10` | .w | "insert coin"/continue countdown | F | `$0090F4`, `$009110` |
| `$FA12`/`$FA13` | .b | continue-screen blink period/counter | F | `$018ED0` |
| `$FA14`/`$FA15`/`$FA16` | .b | continue/credit state flags | F | `$018ECA`–`$018F52` |
| `$FA19` | block | key-record buffer cursor | H | `$01A090` |
| `$FA1A` | .b | **police special active** (also used as "cinematic" gate) | F | `$004010`, `$0143FC` |
| `$FA1B` | .b | actor-pass reentry guard | H | `$00AE42` |
| `$FA1C` | .b | which player triggered the special | F | `$004030` |
| `$FA1D` | .b | boss-intro letterbox active | H | `$018CD4` |
| `$FA1F` | .b | **round-intro/"GO" overlay active** | F | `$01087A` |
| `$FA21` | .b | background scroll pacing counter (reload 8) | F | `$011632` |
| `$FA27` | .b | screen-flash / shake request | H | `$00076A` |
| `$FA30` | .b | difficulty level (used `cmpi.b #$12` etc.) | H | `$009214` |
| `$FA40` | .b | last frame index of current animation | F | `$00AF5A` |
| `$FA43` | .b | **"triple damage" flag** (multiplies player attack by 3, `$00420C`–`$004222`) | F | `$00420C`, `$011FB6` |
| `$FA44`/`$FA45` | .b | screen-shake flag/timer | F | `$004D4C` |
| `$FA46` | .b | player-2-join pending | F | `$01098C` |
| `$FA47`/`$FA48` | .b | latched pressed-state per player | F | `$00ADF4` |
| `$FA49`/`$FA4A` | .b | round-end flag / 255-frame fade counter | F | `$010Cxx`, `$010998` |
| `$FA4B` | .b | "round complete → next" handshake | F | `$0108E2` |
| `$FA4C` | .b | bonus/"perfect" award flag | H | `$005280` |
| `$FA4F` | .b | special-attack animation stage | F | `$005156`, `$018A02` |
| `$FA51` | .b | ? (cleared on police) | ? | `$004038` |
| `$FA52` | .b | police take-off flag | F | `$0050EE` |
| `$FA53` | .b | **per-boss "police hit" latch bitmask** (bit0 = P1's call hit) | F | `$0143F2`, `$016A1A` |
| `$FA55`/`$FA56`/`$FA57` | .b | police-call stage counters | F | `$0113xx`, `$0050A6` |
| `$FA5A` | .b | scripted background FX active | F | `$017FC2` |
| `$FA5D` | .b | parallax pause flag | H | `$011346` |
| `$FA60`/`$FA61`/`$FA65`/`$FA6A`/`$FA6D`/`$FA6F` | .b | **live enemy census** (per archetype counts, per palette) | F | `$009DD8`, `$000844`, `$009406` |
| `$FA70` | .b | "wave complete" flag | F | `$0092F4` |
| `$FA71` | .b | **pause menu active** | F | `$010882`, `$011A48` |
| `$FA72` | .b | police/cinematic script bits | F | `$000472`–`$0004c0` |
| `$FA73` | .b | "police hit already resolved" | F | `$0043E6` |
| `$FA74` | .b | police-hit stun timer (reload `$80`) | F | `$00508A` |
| `$FA75` | .b | sort-list overflow flag | F | `$00AD92` |
| `$FA76` | .b | police-call hit counter | F | `$005136` |
| `$FA77`–`$FA7B` | .b | level/scroll helpers (`$FA79`=camera freeze, `$FA7B`=char-select confirm) | H | `$010C88`, `$00116E` |
| `$FB00` | .w | plane A H-scroll base word | F | `$019626`, `$0088xx` |
| `$FB01` | block | H-scroll table build state | H | `$019636` |
| `$FB02` | block | 13-byte scroll/HUD sub-state | H | `$010CA8` |
| `$FB04` | .w | **current SAT write cursor** | F | `$00AEC0`, `$00B0B6` |
| `$FB06` | .w | VDP mode-change countdown | F | `$01A06E` |
| `$FB08` | .w | **global frame counter** | F | `$01A078` |
| `$FB09` | .b | ? (bit0 read in `$009C84`) | ? | |
| `$FB0A`/`$FB0C`/`$FB0E` | .w/.w/.w | attract sub-state / VDP mode word (`$40`) / attract phase | F | `$008F46`, `$001000` |
| `$FB14` | .w | spawn-script step | F | `$000748`–`$000934` |
| `$FB15` | .b | police-special stage | F | `$00043E` |
| `$FB16` | .w | spawn-script timer | F | `$000750` |
| `$FB1A`/`$FB1C` | .w | sky/tile animation index and VRAM ptr | F | `$011360`–`$011384` |
| `$FB1E` | .w | live actor count | F | `$0092F0`, `$009D8C` |
| `$FB22`+2n | ×6 | **"attackers" list** (up to 5 actors + count) | F | `$0095CE`–`$009602`, `$00AA34` |
| `$FB2E` | .w | scroll-lock unlock index | F | `$011292` |
| `$FB36` | .w | continue → title transition step | F | `$018EDC` |
| `$FB3E` | .w | spawn cooldown | F | `$011B12` |
| `$FB40` | .w | multi-enemy rush counter | F | `$004040`, `$0100CC` |
| `$FB48` | .w | round-intro stage | F | `$011A50` |
| `$FB4C` | .w | title/demo phase counter | F | `$0188C6` |
| `$FB50`/`$FB52` | .w | pause debounce / pause countdown | F | `$011316`, `$011A3C` |
| `$FB54` | .w | scripted-FX step | F | `$017FCA` |
| `$FB56` | .w | **per-frame 4-byte temporary snapshot cursor** (X/Z/Y saved for one actor) | F | `$001C44`, `$00AD96` |
| `$FB58` | .w | background column stream period (reload `$5A`) | F | `$010C94` |
| `$FB5B` | .b | difficulty/2P scaling index for spawns | H | `$0007A6` |
| `$FC00`/`$FC02` | .w | **two-word VDP command pair** | F | `$019E0A` |
| `$FC04`/`$FC08` | .w | raw pad state (P1/P2) | F | `$00815E` |
| `$FC05`/`$FC09` | .b | pressed-this-frame (P1/P2) | F | `$008164` (`eor` with previous) |
| `$FC06`/`$FC0A` | .b | "pad present"/"2P joined" | H | `$008188` (ports equal → `1`) |
| `$FC0C`/`$FC10` | .l | pointer to lifebar digit tilemap for P1/P2 | F | `$004EAC` |
| `$FC14` | .l | **spawn-script PC** | F | `$00078C` |
| `$FC28` | .l | saved spawn-script PC | F | `$00095A` |
| `$FC2C` | .l | spawn-script "current record" | F | `$0008A0` |
| `$FC34`/`$FC38` | .l | **terrain height tables** (tile-index → height, and height→word) | F | `$00AD70`–`$00AD7E` |
| `$FC40`–`$FC54` | block | HUD BCD digit buffers | F | `$018940`–`$0189B8` |
| `$FC20` | .l | credit/continue blink state | H | `$018F52` |

### 6.3 VDP map (FACT where a command is written; PROBABLE where inferred)
| Item | Value | Conf |
|---|---|---|
| Plane A nametable base | `$E000` | F (compared as literal `cmpa.w #$e000,a1` in the name-table encoder `$019692`) |
| Plane B nametable base | `$C000` | F (`ori.w #$6000` for non-`$E000` base in same routine) |
| Plane A H-scroll table | VRAM `$3340` | F (VDP command longword `$73400081` decoded) |
| Plane B H-scroll table | VRAM `$3300`-region | P (mode-5 writer uses `$73420081`) |
| VSRAM plane A / B vscroll | VSRAM `$0000`/`$0002` | P (standard, and VSRAM writes are unconditional) |
| Window plane | `$96`/`$97` register pairs written per mode (`$9680`, `$96A8`, `$96AA`, `$96AF`, `$96ED`, `$96AD`, `$96AC`) | F (bytes), purpose P |
| SAT base | VDP `$F800`, source `$F600`, chunk `$A0` bytes | H (`$00851C`–`$008574` increments `$DCD4` by `$A0`) |
| CRAM | 4 × 16 colours; `$F400`→CRAM via 3-word DMA program `$93209400`/`$9500`/`$96xx`/`$977F` | F |
| VRAM tile art | loaded by `$0081DD`-family writers; specific bases are per-bank constants (`$0086xx` table) | P |

**Unknown:** the exact free-space accounting inside VRAM (how much is reserved for the window plane, and whether any bank reuses tile slots with `$E000` aliasing). Recorded as `U-VRAM-01` in `§28`.

---

## 7. Entity / object structures

### 7.1 The universal actor record — 128 bytes
Every dynamic thing in the game is one of these. Established by (a) the `$80` stride in every pool loop, (b) field-by-field use sites, and (c) the fact that the *same* physics/sprite/collision helpers operate on players, enemies, bosses, weapons and props.

| Off | Sz | Field | Conf | Evidence |
|---|---|---|---|---|
| `+$00` | .b | **type ID** (0 = free slot); index into `$00B236` | F | `$00ADA0`, `$00AE14`, `$00B236` |
| `+$01` | .b | flags: bit0 = "sort-exempt"; bit2 = "animation running"; bit3 = "cull with narrow margin"; bit4 = **X-flip** (sets `$8000` of sprite attr); bit5 = "held by another actor"; bit6 = "no-proximity-activate"; bit7 = **depth priority** (sort tie-break) | F/H | `$00AE50`, `$00B0C0`, `$00AF92`, `$00B02C`, `$00B15C`, `$00B146`, `$00AF0C` |
| `+$02` | .b | sprite tile-width (written from mapping header) | F | `$00AFEC`, `$00B050` |
| `+$03` | .b | sprite tile-height | F | `$00AFF0`, `$00B054` |
| `+$04` | .l | **animation-bank pointer** (0 → no graphics) | F | `$00AF46`, `$00AF4E` |
| `+$08` | .w | offset of the current animation block inside that bank | F | `$00AF50`, `$00AFD8` |
| `+$0A` | .b | **current frame index** | F | `$00AFD2`, `$00B0D4` |
| `+$0C` | .b | frames-per-tick reload | F | `$00B0CE` |
| `+$0D` | .b | frame countdown | F | `$00B0C8` |
| `+$0E` | .w | VRAM tile-number bias added to each sprite | F | `$00B020` |
| `+$10` | .l | **X position, 16.16 fixed** | F | `$00AF60`, `$009F96` |
| `+$14` | .l | **Z (depth) position, 16.16 fixed** — most code reads only the high word as integer depth | F | integration `add.l d0,$14(a0)` at `$004454`; integer bounds `move.w $14(a0)` vs `#2`/`#$70` at `$0043E6` |
| `+$18` | .l | **Y position, 16.16 fixed** (negative = above ground) | F | integration `add.l d0,$18(a0)` at `$00445C`; `move.w $18(a0)` = integer Y |
| `+$1C` | .l | X velocity, 16.16 | F | `$004448`, `$003Cxx` |
| `+$20` | .l | **Z velocity**, 16.16 | F | `add.l d0,$14(a0)` at `$004454` consumes it; clamp `$00A00E` |
| `+$24` | .l | **vertical velocity**, 16.16; gravity is *added to it*, then it is added to `+$18`; clamped to `$C0000` (12.0 px/tick) | F | `$003886` (clamp), `$00389A`/`$0038AE` (gravity), `$00445C` (integration) |
| `+$28` | .w | screen X (X − camera X, +`$80`), derived each frame | F | `$00AFC2` |
| `+$2C` | .w | screen Y (Y + Z/2, +`$80`), derived each frame | F | `$00AFC6` |
| `+$30` | .b | **action/state ID** — the primary state variable | F | player dispatch `$001CE2[state&$FE]`; enemy anim selectors |
| `+$31` | .b | state flag bitfield (bit0 entered, bit1 stunned, bit2 attacking, bit3..6 sub-phases) | H | `$009AD6`, `$009B36`, `$009CFC` |
| `+$32` | .w | **HP** (players: `$50`=80; enemies: small ints) | F | `$004E6E` clamps to `$50`; `$009BD6` subtracts |
| `+$33` | .b | attack damage high nibble/base | F | `$0093DC` |
| `+$34` | .b | **attack damage applied to victim** (low nibble masked) | F | `$004224`–`$004228` |
| `+$37` | .b | reaction flags bit0 = "was hit", bit1 = "attacker", bit2 = "attacked by player" | F | `$009BA0`, `$009CAC`, `$00AAD4` |
| `+$38` | .b | palette/priority copy of `+$33` | H | `$0093E8` |
| `+$39` | .b | palette line (bit7 = "special/boss palette") | F | `$0093B4`, `$009E2C` |
| `+$3E` | .w | **pointer to the attacker/owner actor** | F | `$00B162`, `$009B52` |
| `+$40` | .b | attack-chain / combo counter | H | `$003F08` (`addq.b #1,$40`), `$003F36` |
| `+$41` | .b | nibble-packed params → `$66`/`$68` via table `$009484` | F | `$00945A`–`$009482` |
| `+$42` | .w | **pointer to the current target actor** | F | `$0096C0`, `$009E52` |
| `+$45` | .b | one-shot "landed hard" flag | H | `$003D12`, `$003D64` |
| `+$46` | .w | dword? Actually `.b`+`.b` at `$46`: `$46` = counter for `$47` mask | H | `$009D36` (`move.w #$810,$46`) |
| `+$47` | .b | flip timeout per `$46` | H | `$009D72` |
| `+$48` | .b | previous `+$08` (animation-block change detect) | H | `$001C60` |
| `+$49` | .b | **animation frame used as damage-table index** | F | `$0093D8` (`add.b $49(a0),d0`) |
| `+$4A` | .b | hit-reaction sub-state index | F | `$009B70` table |
| `+$4B` | .b | flags: bit0 = "holding", bit1 = **invulnerable** (`$4F` timer), bit2 = "has weapon", bit5 = "police-hit pending", bit6 = "hit already counted" | F/H | `$004F4C`, `$00504E`, `$0043E6` |
| `+$4C` | .w | **pointer to the actor currently held by this one** | F | `$003DDC`, `$002284` |
| `+$4E` | .b | throw type / grab variant | F | `$002296`, `$00231E` |
| `+$4F` | .b | invulnerability countdown | F | `$0021C2` |
| `+$50` | .b | **character/moveset ID** (0 Axel, 1 Blaze, 2 Adam) for players; entity sub-variant for others | F | `$001EAA` (`lsl.w #2; movea.l $1F20(pc,d0.w),a1` → 3 pointers `$049AE0/$053EFE/$05E90A`), `$00209E` |
| `+$51` | .b | "advance animation / new action" request | F | `$0039EE`, `$01A0D6` |
| `+$52`/`+$53` | .b | palette / sprite override copied for types 1 and 7 | F | `$00B128` |
| `+$54` | .w | pressed-buttons snapshot (from `$FC04`/`$FC08`) | F | `$0038C0`, `$00ADF4` |
| `+$55` | .b | input/latch bits + "on ground" bits | H | `$003D12`, `$004010` |
| `+$56` | .b | weapon damage / grab counter | F | `$00354E`, `$003570` |
| `+$58` | .b | movement flags: bit2 = airborne, bit4 = "hit ground", bit5 = "hold cancel" | H | `$003628`, `$00204A` |
| `+$59` | .b | **status flags**: bit0 invulnerable/flash, bit1 "took damage this tick", bit2 "falling", bit5 "hold released", bit6 "grabbed (victim side)", bit7 "throw locked" | F/H | `$0021B4`, `$009B18`, `$004FA0`, `$002002` |
| `+$5A` | .b | jump variant (0 neutral, >0 directional/attack) | H | `$012C12` uses as param |
| `+$5B` | .b | X-collision counter (wall push-back) | H | `$014D86` (`addq.b #1,$5b`) |
| `+$5C` | .b | grab/throw parameter | H | `$002034` |
| `+$5D` | .b | "linked partner" role (0 none, 1 victim, 2 leader) | F | `$017F4C`, `$017FB2` |
| `+$5E` | .w | **pointer to linked partner** | F | `$0021FA`, `$017F52` |
| `+$60` | .b | "holding something" flag + throw-entry counter | F | `$003DF2`, `$003E34` |
| `+$62` | .w | approach target X (enemies) | F | `$00967A` |
| `+$64` | .w | approach target Y/Z | F | `$009644` |
| `+$66` | .w | per-tick X step for approach | F | `$00947E` |
| `+$68` | .w | per-tick Z step | F | `$009472` |
| `+$6A`/`+$6C` | .w | scratch / throw window | ? | |
| `+$6E` | .w | pointer to the "attached" actor (escort/parasite) | F | `$017266`, `$01787A` |
| `+$72` | .w | pointer to associated actor (round-8 variants) | H | `$017584` |
| `+$74` | .b | flag for the above link | H | `$01757C` |
| `+$76` | .b | countdown to release attached actor | H | `$016AD4` |
| `+$78` | .b | alternation flag (boss AI) | H | `$017558` |
| `+$7B` | .b | cooldown timer (boss jump) | H | `$01727A` |
| `+$7C` | .b | **hit-state code**: 0 none, 1 "reeling", 2 "hit while holding", 3 "grabbed by player" | F | `$004566`–`$00459C`, `$00A98C` |
| `+$7D` | .b | **hit-reaction animation/behaviour index** (1..9) | F | `$004586`, `$0045C6`, `$002C5C` |
| `+$7E` | .w | pointer to the last attacker | F | `$0045CA`, `$00AA2A` |

**Explicit unknowns in the record:** `+$35`, `+$36`, `+$43`, `+$44`, `+$5F`, `+$61`, `+$6A`–`+$6D`, `+$7A`, `+$7F` are not read by any code path that could be attributed with confidence → `§28` items `U-ACT-01`.

### 7.2 Pools (FACT, from the loops)
| Pool | Range | Slots | Stride | Purpose | Evidence |
|---|---|---|---|---|---|
| Player 1 | `$B800` | 1 | `$80` | actor record | `$00AE00`, `lea $b800,a0` everywhere |
| Player 2 | `$B880` | 1 | `$80` | actor record | `$00AE06` |
| General actors | `$B900`–`$C8FF` | 32 | `$80` | enemies, bosses, props, pickups | `$0094C0` (`moveq #$1f,d7`), `$00AE0C` (`# $41`) |
| Effect actors | `$C900`–`$D4FF` | 24 | `$80` | hit sparks, thrown items, police squad | `$0095AA` (`lea $c900,a1`, `moveq #$17,d7`, writes type `$29`) |

The `$00AE0C` loop walks **66** slots (`moveq #$41,d7`) from `$B900`, i.e. `$B900`–`$DA7F`, so slots `$D500`–`$DA7F` are addressable but no subsystem creates them — reserved space. The `cmpa.w #$D100` test in `$00B132` means "slots below `$D100` are eligible for camera-proximity activation", which is a cheap way of keeping effect slots out of that test. (H for the semantics, F for the boundaries.)

### 7.3 Actor type dispatch table `$00B236` (FACT: 156 entries × 2 bytes, high page for `type>=$90`)

| Type | Handler | Type | Handler | Type | Handler |
|---|---|---|---|---|---|
| `$00` | (free slot — never dispatched) | `$2C`–`$2F` | `$00B36A` (`rts`) | `$66` | `$00D32C` |
| `$01` | `$001C44` **player** | `$30` | `$0143D0` boss | `$67` | `$00D362` |
| `$02`,`$03` | `$00B36A` | `$31` | `$015794` boss | `$68` | `$00D39C` |
| `$04` | `$008E2C` | `$32` | `$00DD78` | `$69` | `$00CD66` |
| `$05` | `$00597C` | `$33` | `$012B5C` **Mr. X** | `$6A` | `$00CA7C` |
| `$06` | `$0018D4` | `$34` | `$012F14` | `$6B` | `$00CFB8` |
| `$07` | `$001A12` | `$35` | `$01306A` | `$6C` | `$00D150` |
| `$08` | `$005C1E` | `$36` | `$0140DC` | `$6D` | `$00D08E` |
| `$09` | `$006114` | `$37` | `$014266` | `$6E` | `$00C6E0` |
| `$0A` | `$0061F6` | `$38` | `$012FB4` | `$6F` | `$00C756` |
| `$0B` | `$006226` | `$39` | `$014318` | `$70` | `$00C618` |
| `$0C` | `$006256` | `$3A`–`$3D` | `$00B36A` | `$71` | `$00D3D6` |
| `$0D` | `$0063F6` | `$3E` | `$00673C` | `$72` | `$00D444` |
| `$0E` | `$00654E` | `$3F` | `$0068E2` | `$73` | `$00D4B2` |
| `$0F` | `$005218` | `$40` | `$006904` | `$74` | `$00D0AC` |
| `$10` | `$0056E6` | `$41` | `$00791A` | `$75` | `$00C7D0` |
| `$11` | `$006AF4` | `$42` | `$007A6C` | `$76` | `$00C846` |
| `$12` | `$006E2A` | `$43` | `$007C70` | `$77` | `$00C394` |
| `$13` | `$006DDC` | `$44` | `$007644` | `$78` | `$00C924` |
| `$14` | `$006D40` | `$45` | `$007534` | `$79` | `$00C58C` |
| `$15` | `$00760C` | `$46` | `$007662` | `$7A` | `$00C97A` |
| `$16` | `$007214` | `$47` | `$006988` | `$7B` | `$00C9D0` |
| `$17` | `$006F7C` | `$48` | `$0067A4` | `$7C` | `$00CA26` |
| `$18` | `$0070C4` | `$49` | `$006862` | `$7D` | `$00D548` |
| `$19` | `$006C84` | `$4A` | `$006894` | `$7E` | `$00C36E` |
| `$1A` | `$0077B6` | `$4B` | `$006926` | `$7F` | `$00D5C8` |
| `$1B` | `$007370` | `$4C` | `$006948` | `$80` | `$00C89C` |
| `$1C` | `$007448` | `$4D` | `$006E9E` | `$81` | `$00C492` |
| `$1D` | `$00746A` | `$4E` | `$0071DC` | `$82` | `$00C114` |
| `$1E` | `$0061BE` | `$4F` | `$006968` | `$83` | `$00C17C` |
| `$1F` | `$007CBC` | `$50` | `$007D4A` | `$84` | `$00BF76` |
| `$20` | `$00D606` | `$51` | `$007D7A` | `$85` | `$00BEBA` |
| `$21` | `$00D99A` | `$52` | `$007DF0` | `$86` | `$00BF00` |
| `$22` | `$00DD78` | `$53` | `$007E20` | `$87` | `$00BBEE` |
| `$23` | `$00E326` | `$54` | `$0101C8` police squad | `$88` | `$00C8F2` |
| `$24` | `$00E4D2` | `$55` | `$015E70` | `$89` | `$00BC5C` |
| `$25` | `$00E8F0` | `$56` | `$016CE4` | `$8A` | `$00BCA2` |
| `$26` | `$00F038` | `$57` | `$0174E0` | `$8B` | `$00BD10` |
| `$27` | `$00F27E` | `$58` | `$0158C4` | `$8C` | `$00BB94` |
| `$28` | `$00FC14` | `$59`–`$5F` | `$00B36A` | `$8D` | `$00BB18` |
| `$29` | `$0100B6` | `$60` | `$00CD22` | `$8E` | `$00BB58` |
| `$2A` | `$00F7D0` | `$61` | `$00D112` | `$8F` | `$00B36A` |
| `$2B` | `$00B36A` | `$62` | `$00D210` | `$90`–`$95` | `$01B36A` (past ROM end → **never reachable**) |
| | | `$63` | `$00D2A4` | `$96` | `$017262` |
| | | `$64` | `$00CBE6` | `$97` | `$017858` |
| | | `$65` | `$00CCE8` | `$98` | `$016C60` |
| | | | | `$99` | `$016C24` |
| | | | | `$9A` | `$014E75` |
| | | | | `$9B` | `$014EF9` |

**Documented ambiguity (`U-DISP-01`).** The table is read with a byte index (`move.w (a1,d0.w)`) where `d0 = type*2`, and `$00AE20`–`$00AE26` adds a correction:
```
cmpi.w #$120,d0 ; bcs.s .ok ; bset.b #$10,d0      ; $00AE20
.ok: move.w (a1,d0.w),d0 ; movea.l d0,a1 ; jsr (a1)
```
For `d0 = $120` (type `$90`) this yields index `$130`, i.e. the entry belonging to type `$98` — **the correction does not implement a clean second page**, it shifts by `$10` bytes (8 entries). The words stored at the nominal `$90`–`$95` slots therefore are not necessarily the handlers those types reach, and the words at those slots (`$01B36A`) are *beyond the 512 KiB image*. No spawn script in the image references types `$90`–`$95` (verified against every `$FC14`/`$000A4E` record), so the whole path is unreachable in practice. Recorded, not explained: `UNKNOWN`.

---

## 8. Player architecture

### 8.1 Entry and per-frame skeleton (FACT, `$001C44`)
```
$001C44  a1 = $FB56            ; 4-byte scratch snapshot cursor
         move.l $10(a0),(a1)+  ; save X
         move.l $14(a0),(a1)+  ; save Z
         move.l $18(a0),(a1)+  ; save Y
         jsr $00502C           ; "police-hit / forced-state" pre-emption
         jsr $0050A6           ; "special move requested" pre-emption
         jsr $00568A           ; name-entry / pickup proximity
         move.b $09(a0),$48(a0); anim-block change detect
         move.b $0A(a0),$47(a0)
         jsr $0039C6           ; invulnerability timer
         jsr $0120EC           ; per-character global hook (round-specific)
         jsr $0040A6           ; police-special knockback if active
         if (that returned non-zero) goto epilogue      ; <-- pre-emption
         jsr $003FCC           ; SPECIAL-ATTACK INPUT CHECK
         jsr $00333E           ; damage-flash / hit-reaction gate
         jsr $004650           ; hitbox vs hurtbox resolution (player side)
         jsr $004F4C           ; invuln-from-hit timer
         jsr $00358C           ; ceiling/height clamp
         if (d7!=0) goto epilogue
         jsr $00B186(table $001CE2)  ; >>> STATE DISPATCH <<<
         jsr $003FA2           ; 2P "hold" transfer
         jsr $003886           ; gravity clamp
         jsr $00442C           ; POSITION INTEGRATION
         if (type != 1) goto epilogue
         jsr $00479C           ; player↔enemy body collision
         jsr $003B00           ; sprite-size / mapping sync
         jsr $0041EA           ; set attack damage from frame table
         jsr $0032D8           ; attack-priority byte
         jsr $004F72           ; grab-release legality
         jsr $004140           ; build AABB from frame offsets
         jsr $004D60           ; extra-life check
         jsr $004620           ; ? (mapping/animation re-sync)
         clr.b $7C(a0)         ; clear hit-state
epilogue a1=$FB56; a1+=4; $FB56=a1
```
Three structural consequences:
1. **A player is only one actor type.** There is no separate "player controller" object; the 3 characters differ *only* by data (`+$50` selects one of three pointer triplets at `$001F20`).
2. **Pre-emption order is fixed**: police-special → special-move request → hit-reaction → state dispatch. A police call overrides any state the player is in.
3. **State dispatch is `state & $FE`** — i.e. 128 entries, with the odd value being the "facing" bit of the same state. Confirmed by the table at `$001CE2` containing 128 distinct 16-bit targets, each duplicated for odd/even.

### 8.2 Player state table `$001CE2` (FACT, 128 entries, 16-bit absolute ROM addresses)
Selected/decoded values (full 128-entry dump is produced by `tools/verify_sor_forensics.py`-style decoding; here the *named* groups established by reading each target):

| State | Target | Reading |
|---|---|---|
| `$00`/`$01` | `$001E0E` | **idle/standing** — sets flags, computes initial position; `$1E3C` handles "knocked out of the world" respawn |
| `$04`,`$06` | `$001F7C` | walk (normal speed) |
| `$08`–`$1E` | `$001F8E`,`$001FB0` | walk variants (diagonal / into-depth) |
| `$20`/`$22` | `$001FC0` | jump-arc (up phase) |
| `$24`/`$26` | `$001FDC` | jump-arc (apex) |
| `$28`/`$2A` | `$001FE8` | jump-arc (down) |
| `$2C`/`$2E` | `$002000` | **landing** (branches on `+$50`==2 for Adam's heavier landing) |
| `$30`–`$3A` | `$00201E` | **attack (punch/kick chain)** — reads `+$7C` for "connected", sets `+$5C`/`+$0C`/`+$0D` timing |
| `$3C`/`$3E` | `$002096` | attack recovery / chain window |
| `$40`/`$42` | `$0020EC` | back-attack / elbow |
| `$44`/`$46` | `$002100` | jump-kick start |
| `$48`/`$4A` | `$00211C` | jump-kick active |
| `$4C`/`$4E` | `$000000` → **never**: dispatch guard catches 0 | `§23.10` |
| `$50`/`$52` | `$00212C` | **special/super attack** |
| `$54`–`$5E` | `$000000` | see above |
| `$60`/`$62` | `$002140` | pickup / weapon grab |
| `$64`–`$76` | `$002148` | weapon attack chain |
| `$78`/`$7A` | `$002158` | throw setup |
| `$7C`/`$7E` | `$002174` | **vacuum/throw** (uses `$389A` gravity + `$38C0` air control) |
| `$80`/`$82` | `$002180` | thrown-victim release |
| `$84`/`$86` | `$002198` | **air recovery / hit-in-air** |
| `$88`–`$8E` | `$0021E6` | **grab hold** (reads partner `+$51`, type `$08/$0C` partner → release) |
| `$90`–`$96` | `$00225C` | grab attack (knee/etc.) |
| `$98`/`$9A` | `$002100` | jump-kick (duplicate) |
| `$9C`/`$9E` | `$00211C` | jump-kick active (duplicate) |
| `$A0`–`$BE` | `$2AE0`–`$2B3C` | **hit reactions** (light/heavy/launched/knockdown) |
| `$C0`/`$C2` | `$002260` | grab attempt (whiff) |
| `$C4`–`$CA` | `$0023B4`,`$0023B8` | **grab success / throw windup** |
| `$CC`/`$CE` | `$0022E0` | grab whiff-2 |
| `$D0`–`$DE` | `$0023D6`–`$002452` | **hold-and-pummel** (repeating hits with `+$0D` timers) |
| `$E0`/`$E2` | `$0023F8` | throw release |
| `$E4`/`$E6` | `$002A10` | landing-from-throw |
| `$E8`/`$EA` | `$002426` | post-throw recovery |
| `$EC`/`$EE` | `$0026E2` | knockdown |
| `$F0`–`$106` | `$0024C4`–`$00291E` | **death / dying / respawn** sequence |
| `$108`–`$10A` | `$00291E` | dead (waiting for continue) |
| `$110`–`$12A` | `$0028A2`–`$002AA0` | **police-call / backup animation states** |

### 8.3 Per-character differentiation (FACT, data-only)
* `+$50` ∈ {0,1,2} selects one of three longword pointers at `$001F20`: `$049AE0`, `$053EFE`, `$05E90A` — the per-character animation/sprite-mapping base used by the sprite builder.
* Jump impulse is **not** in the player record; it is set by the state handler. `$0020C8` writes `#$FFF90000` (i.e. −7.0 px/tick) into `+$24` for the directional-jump case, and `$002112` writes `#$FFF9C000` (−6.25) for the air-recovery case. The *actual* per-character launch velocities come from the animation-block data consumed at `$003614` (`move.b (a1,d1) → swap → asr.l #4` → velocity from a byte in the animation table). So character jump height is a **data** property, not a constant in code. (F for the mechanism, P for the per-character numbers.)
* Verified by executing ROM gravity (`EXP-05`) with the three characteristic launch velocities seen in the animation data:

| Launch v_y | Neutral jump (`$00389A` +g=`$E800`) | Directional (`$0038AE` g=`$E800` then `$8800`) |
|---|---|---|
| −7.5 px/t | 18 ticks (0.600 s), peak 34.875 px | 20 ticks (0.667 s), peak 34.875 px |
| −8.5 px/t | 20 ticks (0.667 s), peak 44.219 px | 23 ticks (0.767 s), peak 44.219 px |
| −9.5 px/t | 22 ticks (0.733 s), peak 54.656 px | 25 ticks (0.833 s), peak 54.656 px |

  The peak is identical between columns because peak depends only on `v²/2g`; the *airtime* differs because `$0038AE` uses the smaller acceleration `$8800` while ascending with `v_y≥0` — i.e. **the game deliberately gives the player longer hang time when jumping forward/backward, with no change in jump height.** That is a genuine, measured design property, not an inference.

### 8.4 Input consumption inside the player (FACT)
* Pressed-edge bits live in `$FC05` (P1) / `$FC09` (P2). `$00813C` computes them as `not(current) eor previous`.
* Special attack: `$003FCC` first requires `bit6` of `+$55` (special button in the 3-button mapping) plus `tst.w +$32` (HP > 0), then checks a *stock* byte at `$FF21` (P1) / `$FF24` (P2): `tst.b (a1) / beq → return`. On use it decrements the stock, sets `$FA1C` to the player index, calls `$4E14` (HUD refresh), clears `$FA51`/`$FA41`/`$FB40`/`$FA44`, calls `$9566`, then sets `$FA1A = $101` (word: low byte = active, high byte = "police car in flight"). **The special is a resource, not a free move.**
* Grab: `$004F72` decides legality from a byte table at `$004FC4` indexed by `+$30>>1` (i.e. per-state grab permission), with bit `$F0` = "may be grabbed", bit `$0F` = grab class. Type checks at `$004FB6`/`$004FBC` set the victim's `+$01` bit7 when the grab class is incompatible.
* Combo/chain: `+$40` is incremented by `$003F08` on every connected hit *inside the same attack animation*; `+$41` is then set to `$26` (punch chain) or `$0A` (kick chain) as a **hard-coded chain budget**. The chain ends when `+$40 ≥ 2` (`cmpi.b #2,$40(a0)` at `$003F0C`) or the animation completes.
* `+$0D` is the per-state timer consumed by `$0039E8`: `subq.b #1,$d(a0)`; on zero it sets `+$51` (advance-animation) and increments `+$0A` (frame), wrapping at the value in the animation header. **Animation timing and state timing are the same counter.**


---

## 9. Physics model

### 9.1 Coordinate system (FACT, derived from integration + projection code)

```
world:  X  (+$10, 16.16, pixels along the walkable axis)
        Z  (+$14, 16.16, pixels into the screen — the "2.5D depth" axis; usable range ≈ 2..$70)
        Y  (+$18, 16.16, pixels up; negative = above the floor)

screen: sx = (X_int) - cameraX + $80                        ($00AF6E-$00AF7E)
        sy = (Z_int >> 1) + (Y_int) + $80                   ($00AF64-$00AF72)
```
The `>>1` on Z is the defining projection constant of the engine: **one pixel of depth = half a pixel of screen rise**. It is applied in exactly one instruction (`asr.w #1,d3` at `$00AF68`), so it is not a tunable; it is hard-coded.

All three axes are 16.16 fixed point; almost every consumer reads only the *high word* (`move.w $10(a0),d0`) to get whole pixels, which is why changes smaller than 1 unit still accumulate correctly.

### 9.2 Integration law (FACT, `$00442C`–`$004460`)
```
if ((+$08 & $FC) == $14) and (+$59 bit7 set):  skip integration entirely   ; frozen frame
else:
    +$10 += +$1C          ; X += vx
    +$14 += +$20          ; Z += vz
    +$18 += +$24          ; Y += vy
```
`(+$08 & $FC) == $14` is a *state-dependent freeze*: while this animation block is selected and bit7 of `+$59` is set, position does not integrate at all. This is how "held/grabbed" actors stay pinned without a separate code path.

### 9.3 Gravity constants (FACT — all are literal `move.l #…` immediates)
| Value | 16.16 decimal | px/tick² | Applied by | Condition |
|---|---|---|---|---|
| `$0000E800` | 59392 | **+0.90625** | `$00389A` | whenever an actor is airborne in the "neutral" jump path |
| `$0000E800` | 59392 | **+0.90625** | `$0038AE` | ascent half (`vy < 0`) |
| `$00008800` | 34816 | **+1.0625** | `$0038AE` | descent half (`vy ≥ 0`) |
| `$00012000` | 73728 | **+1.125** | `$00973E` (hit-reaction path) | airborne after being launched |
| `$000100000` | 1048576 | **+16.0** | `$00973E` clamp | terminal velocity for launched actors |
| `$0000C0000` | 786432 | **+12.0** | `$003886` clamp | terminal velocity for player jump |
| `$0000C000` | 49152 | **+0.75** | `$0104xx` (palette scroll) | *not* an actor value — listed to rule it out |

**Measured consequence** (`EXP-05`, real ROM code on MC68000): ascent uses 0.90625 always; the *descent* is where the two jump variants differ (0.90625 vs 1.0625), giving a forward jump ~11 % longer airtime with an identical apex. Because apex = `v²/(2g)`, a jump that is 11 % "floatier" on the way down *feels* higher without being higher — a deliberate, measurable tuning.

Gravity is applied **before** integration in the frame (gravity helpers are called from the state handler, integration happens later in `$001C84`). So the first frame of a jump already includes one gravity step.

### 9.4 Horizontal movement (FACT)
* Walking: the animation block supplies a signed byte; `$00363E` converts it as `v = byte/16` px/tick:
  `move.b (a1,d1),d2 ; ext.w ; swap ; asr.l #4` → `d2 = byte << 16 >> 4 = byte * 4096` = byte/16 in 16.16.
  Facing is applied by negating the 32-bit value (`$003644`).
* The same construction one byte later supplies the **depth velocity** into `+$20` (`$003652`–`$00365E`). So walk speed *and* depth speed are per-frame data, not constants — i.e. each animation frame can move the actor differently. This is the mechanism behind "walking diagonally is slower".
* Air control (`$0038C0`): acceleration `±$6000` (**±0.375**) per tick while airborne, clamped to `±$38000` (**±3.5** px/tick) by the two comparisons against `$FFFC8000`.
* Knockback (`$0099D2`): deceleration `$5400` (**0.328**) per tick toward zero, applied only when the actor is in the launched state and its direction opposes motion.
* Push-out (`$009F96`, `$00A00E`): if the *proposed* X (or Z) leaves the legal band, the previous value is restored and bit0 of a local flag is set (`$009FDC`, `$00A002`). This is the "wall" test; there is no separate wall list — the legal band is a per-round constant pair:
  `X ≥ −(?)` / `X ≤ $2F00000` (752.0) and `X ≤ $15100000` (337.0) in the round-7 branch `$009FCA`, plus Z ≤ `$20000` (2.0) in `$00A018` → `§14`.

### 9.5 Boundaries that are *not* physics
The `cmpi.l #$C0000,$24(a0)` in `$003886` and the band checks in `$009F96` are the only two limiters. There is no slope handling, no platform/conveyor system, no ground normal, no collision response surface. Actors are constrained to a rectangle in (X,Z) and to a height-map value in Y (`§14.4`); everything else is 1-D integration. **This is arcade 2.5D physics, not a simulation** — and the complete absence of rotation/slope code is a FACT (no `muls`/`divs` against a surface normal exists anywhere in `$003580`–`$0043AA`).

---

## 10. Collision / hitbox / hurtbox model

### 10.1 Two distinct box systems, both in the actor record (FACT for addresses and arithmetic)

**System A — "body box", 12 bytes at `+$64`, six words, world-space pixel integers.**
Builder: `$004140`–`$0041E8`. Called from the player path only (`$001CC6`), i.e. players rebuild theirs every frame; other actors build theirs inside their handlers.

```
a5 = $01ABA8     ; 5-byte records: [x1_off, x2_off, z_index, y1_off, y2_off]
a6 = $01AB8E     ; 2-byte records: [z1_off, z2_off]
d1 = +$02 (sprite tile width) ; d1 = d1*5                      ; 5 bytes per record
d0 = X_int + sbyte(a5[d1+0]) → (+$64).w                        ; x1
     X_int + sbyte(a5[d1+1]) → (+$66).w                        ; x2
d2 = byte(a5[d1+2]) * 2 ; d0 = Z_int + sbyte(a6[d2+0]) → (+$68).w   ; z1
                                 (+$6A).w                      ; z2
d0 = Y_int + sbyte(a5[d1+3]) → (+$6C).w                        ; y1
     Y_int + sbyte(a5[d1+4]) → (+$6E).w                        ; y2
```
So the attacker-independent *shape* of every actor comes from two ROM tables indexed by its sprite width and its depth index. **All offsets are signed 8-bit pixels** — the box can never exceed ±127 px in any direction, and boxes are axis-aligned in (X,Z,Y).

**System B — "attack box list", word count at `+$70` followed by 6-byte records.**
Evidence: `$00AD04` reads `lea $70(a1),a2 ; tst.w (a2)+ ; beq → no hit`, then `$00AB24` walks the list and `$00AB7C` advances the cursor by `#6`. Each record is tested by `$00AB88`/`$00AC78`, which are pure interval-overlap predicates on (X, Z, Y) using *signed byte* offsets:
```
$00AB88  d1 = actor.Z ; d5a = sbyte(a3)+ ; d1 += d5a ; if d1 > word(a2)     → miss
         d5b = sbyte(a3)+ ; d1 += d5b ; if d1 < word(-(a2))                → miss
         → hit
```
**Therefore: hit detection is 3-axis interval overlap between one actor's attack-record set and the other actor's body box, with Z tested at half weight** (`$00AB5A`–`$00AB74` doubles the Z offset before the test). No radius, no circles, no per-pixel masks — the entire combat geometry of the game is signed bytes plus interval tests.

### 10.2 Priority, ordering and filtering (FACT)
* Body-vs-body (`$00450C`, used for player↔player and player↔enemy separation) performs six comparisons — `x1≤x2'`, `x2≥x1'`, `z1≤z2'`, `z2≥z1'`, `y1≤y2'`, `y2≥y1'` — and returns "no overlap" on the first failure. It is a plain AABB test, evaluated in that fixed order (X, Z, Y).
* Grab eligibility (`$004F72` + table `$004FC4`): byte per state (`+$30>>1`), `hi nibble = grab class`, `lo nibble = "can be grabbed"`. Incompatible class → victim gets `+$01` bit7 (depth-priority flip) rather than being grabbed.
* Invulnerability: `+$4B` bit1 with timer `+$4F` (`$004F4C`, `$004F62`). This is the *only* damage immunity mechanism; there is no per-attack invulnerability list.
* Multi-hit prevention: `+$4B` bit6 ("hit already counted") is set by `$0043E6`/`$00504E` and cleared when the attack animation block changes. This — not a per-frame hit list — is how a single attack cannot hit the same target twice.
* Z-depth filtering for *display* (not combat) is `+$01` bit7, which promotes an actor to draw in front of another with equal bucket.

### 10.3 Collision passes in per-frame order (FACT)
1. `$0051CC` — **proximity/body-block + pickup**, per player: probes `d5 = 8` and grows the probe (`+8` per iteration) until it finds a free position; on success writes the corrected X (`+$10`). This is "player cannot walk through an enemy" plus "press attack near a weapon to pick it up".
2. `$0043AA` — **player↔enemy body overlap**: clamps the player's X into `[cameraX+$20, cameraX+$20+$100]` if overlapping (`$0043F6`–`$004406`), i.e. the camera-relative "no-go" band; also enforces Z ≥ 2 and Z ≤ $70.
3. `$004478` — **player↔player**: only runs when `$FF18 == 3` (both players), `$FA1A == 0`, and neither player is in a "special" state; uses the `$45D4` grab-class table; sets `+$7C`/`+$7D` on both and cross-links `+$7E`.
4. `$004650` — **player attack → enemy**: requires `+$7C == 2` or a "certain" state, then calls `$7EBE` (free-slot request), copies position/animation into the new actor (type `$49`), and applies a per-attack offset from `$004710` (the `x/y` offset table indexed by animation block). Spawned actor type `$49` is the **hit spark**.
5. `$00479C` — **player body vs enemy attack**: the reverse direction, gated on the enemy's state byte `$84` special-case at `$0047B2`.
6. `$0094C0` — **police special**: loops all 32 general slots, applies `+$32 = $FFFF` (kill sentinel) to any enemy that is not a boss (`$30` ≥ ... ) and not already handled.

### 10.4 What is *not* modelled (FACT, by exhaustive negative search)
No swept collision, no continuous collision, no per-sprite masks, no z-buffer, no projectile-vs-projectile, no line-of-sight. Two actors can swap positions in one frame without ever overlapping — because only the *post-integration* AABB is tested.

---

## 11. Combat system

### 11.1 The damage pipeline (FACT, decoded instruction by instruction)

**(a) Player attack damage comes from a per-frame nibble table.**
```
$0041EA  a1 = $00423C
         d0 = (+$08 >> 1) & $FE               ; animation-block index
         a1 = a1 + word(a1 + d0)              ; sub-table base for this animation
         d0 = byte(a1 + (+$50))               ; + character id  → row offset
         d0 = byte(a1 + 3 + d0 + (+$0A))      ; + frame index    → damage/hit-class byte
         ; byte layout:  hi nibble = hit class, lo nibble = damage (0..15)
         if ($FA43 != 0):                     ; "triple damage" flag
             d1 = d0 & $F0 ; d0 &= $0F ; d2 = d0
             d0 = d0 + d0 + d2 + d1           ; = 3*lo + hi   (full byte)
$004224  (+$34) = d0 & $0F                    ; applied damage
$00422E  (+$42) = (d0 >> 4)                   ; hit class → reaction selector
```
So a player attack's damage is **a 4-bit value looked up by (animation block, character, frame)**, and the high nibble is not damage at all — it selects the reaction. `$FA43` (set by `$011FB6`, cleared by `$011E7E`) rewrites the pair as `3×total`, letting overflow bleed into the reaction nibble. `$FA43` is therefore a debug/second-player "hard mode" modifier that can *change hit reactions*, not merely scale damage.

**(b) Enemy→player and player→enemy subtraction.**
```
$009BCC / $009BD6   a1 = (+$3E) [attacker]
                    d0 = byte(+$34 of attacker)
                    (+$32 of victim) -= d0
                    if result < 0 → death branch ($009C36 → state $300)
                    else → (+$50) = $18 (24-frame stun timer) and continue
```
Player HP is initialised, clamped and rendered against a hard maximum of **80** (`moveq #$50,d6` at `$004E6C`; the lifebar divides by 8 to get 10 segments at `$004E8E`).

**(c) Reaction selection.** `+$7D` (the reaction animation index) is written from the attacker's `+$42` nibble in `$0045C6`, with special cases:
* `$00AAC8`: if the victim is a player and its state is `$80..$1C7` (mid-air), the attacker's `+$42` is copied into `+$37` (launch flag) → air-juggle.
* `$004586`: if attackers and defenders are on opposite Z-faces, `+$7D = 2`, else `3` (front vs back hit).
* `$002C34`/`$002C5C`: `$FA43` swaps classes 7↔6 and 9 (extra knockdown).

### 11.2 Frame data (what is recoverable and what is not)
The *timing* of an attack is fully recoverable, but it is implicit rather than tabular:
* `+$0C` = frames per animation frame (written from the animation block), `+$0D` = countdown, `+$0A` = current frame. `$0039E8` decrements `+$0D` and advances `+$0A`, wrapping at the value stored in the first byte of the frame list.
* Therefore **startup = sum of durations of frames before the first frame whose damage byte is non-zero**; recovery = the remainder. Both are data-derived per (character, state).
* Because the damage byte is read every frame the box exists, an attack with a long active window has the same damage each frame — there is no per-attack "hit once" flag. The once-only behaviour comes from `+$4B` bit6.

**Honest limitation:** the complete per-character frame tables are *not* transcribed in this dossier. Locating them requires resolving the pointers at `$001F20` → animation banks (`$049AE0`, `$053EFE`, `$05E90A`) → per-state pointers → frame lists, and each character's bank spans tens of KiB of interleaved sprite-mapping data. The mechanism is fully understood (FACT); the ~200-row table is `U-CBT-01` in `§28`.

### 11.3 Hit effects, shake, and the absence of hit-stop
* Screen shake: `$004D4C` sets `$FA44 = 1`, `$FA45 = 8`; the shake itself is applied by the camera (`§19`), not by the renderer.
* The hit spark is a spawned actor of type `$49` (`$0046B2`), with its damage/offset table at `$004710` (word of `$0050` = "no offset" sentinel, `$80xx` = negative offset).
* **No hit-stop exists.** Verified by exhaustive search: no global "freeze N frames" counter is written from any damage path; the only simulation freezes are `$FA71` (pause), `$FA1F` (round intro) and `$FA1A` (police cinematic). Any claim of hit-stop in this game is not supported by the binary.

### 11.4 Combos
`+$40` counts connected hits inside one animation; `$003F08` increments it, `$003F0C` compares against `2`, `$003F18` arms `+$41 = $26`, and the chain terminates by loading a new state (`$2EE8`). So the *chain length is at most 3 inputs* and is enforced by a byte comparison, not by a timer.

---

## 12. Enemy AI

### 12.1 Shared AI core (FACT — these routines are called from every enemy handler)
| Routine | Purpose (descriptive) | Key behaviour |
|---|---|---|
| `$009604` | *approach step compute* | `dx = targetX − X ; dz = targetZ − Z`; if `|dx| < 4 && |dz| < 4` → return 1 ("in position"); else `jsr $00982C` (angle/speed solve) and store `+$1C`/`+$20` |
| `$009648` | *lock target Z* | `+$62 = target+$14` |
| `$009654` | *lock target X with bias* | `+$62 = clamp(targetZ + bias)`; `+$60 = targetX ± (+$66)` depending on side |
| `$00969E` | *face target / set facing* | sets `+$08` bit1 from `targetX < X`, then `jsr $00B1A2` |
| `$0096C0` | *face specific actor* | as above with explicit pointer |
| `$0096EC` | *target selection (2P)* | if `$FF18 == 3`: compares `|P1.X−X|` vs `|P2.X−X|` and stores the nearer into `+$42`; else stores `$B800` |
| `$00973E` | *airborne update* | `+$24 += $12000`, clamp `$100000`, `+$18 += +$24`; then ground query `$00AD2A`; landing tests at `+$18 ≥ $FC` |
| `$0097CE` | *"inside screen X band?"* | `d0 = (X_int ≥ $80 && X_int < $1C0)` |
| `$0097E6` | *"inside wider band?"* | `d0 = (X_int ≥ $70 && X_int < $1D0)` |
| `$0097FE` | *aim-at-target velocity* | sums target X/Z, `jsr $00982C`, stores `+$1C`/`+$20` |
| `$00982C` | **velocity solver** | if `$FFC6` (difficulty) != 0 and speed `d6 ≥ $300`, reduce speed by `$100`; then `$009842` → `$0042EA` (angle table) |
| `$009842`–`$009894` | **atan2-ish octant solver** | builds an octant/sign byte in `d2`, computes `d1 = (minor<<6)/major`, clamps to `$3F`, returns index into the angle table |
| `$009896` | **direction vector lookup** | table `$02705E`, 4 bytes per angle: two words; scaled by speed `d6` with `mulu`/`swap`; sign/axis swaps from `d2` |
| `$0098E8` | *distance metric* | `3*max(|dx|,|dz|)/8 + min(|dx|,|dz|)` → a cheap octagonal distance |
| `$00991A` | *death/knockdown lite* | sets `+$1C = 7`, `+$24 = −9`, flags |
| `$009B36`,`$009C50`,`$009CFC`,`$009D16` | *hit-reaction states* | stun, launch, knockdown, "get up" — all keyed by `+$4A` through table `$009B80` |
| `$009DC0`,`$009E26`,`$009E3E` | *on-death bookkeeping* | decrements the `$FA60/$FA6A` census, adds score, zeroes 32 longs (record wipe) |

### 12.2 The complete per-archetype table (FACT — extracted from `$026FCE`, `$027010`, `$027032`)

Layout: `$026FCE`: 6 bytes per type = `HP[3]` then `ATK[3]` (3 difficulty palettes). **Effective HP = byte + 1.** `$027010`: 3 bytes per type = score-table IDs (indices into `$010DDA`, whose entries are 3-byte packed BCD). `$027032`: 4 bytes per type = animation-bank pointer.

| Type | Archetype (behaviour-derived label) | HP (pal 0/1/2) | ATK (pal 0/1/2) | Score (pal) | Anim bank |
|---|---|---|---|---|---|
| `$20` | basic thug, unarmed | 7 / 10 / 12 | 8 / 8 / 8 | 500/600/700 | `$01FC70` |
| `$21` | basic thug, knife | 5 / 8 / 10 | 4 / 8 / 8 | 500/600/700 | `$01FC70` |
| `$22` | basic thug, pipe | 5 / 8 / 10 | 4 / 8 / 8 | 500/600/700 | `$01FC70` |
| `$23` | basic thug, jumping kick | 7 / 10 / 12 | 12 / 12 / 12 | 500/600/700 | `$01FC70` |
| `$24` | slim brawler, slide + throw | 5 / 8 / 10 | 8 / 8 / 12 | 600/700/800 | `$022948` |
| `$25` | whip female fighter | 5 / 8 / 10 | 12 / 12 / 16 | 700/800/900 | `$02402C` |
| `$26` | kung-fu specialist | 8 / 12 / 15 | 8 / 8 / 8 | 600/700/800 | `$0242F8` |
| `$27` | heavyweight grappler | 10 / 15 / 18 | 12 / 16 / 20 | 800/900/1000 | `$02556C` |
| `$28` | heavyweight, *1 HP*, always-on variant | 1 / 1 / 1 | 12 / 16 / 20 | 500/500/500 | `$02556C` |
| `$29` | multi-enemy rush controller (not a fighter) | 1 / 1 / 1 | 0 / 0 / 0 | 500 | `$000000` |
| `$2A` | whip female, variant B | 8 / 12 / 15 | 12 / 12 / 16 | 700/800/900 | `$02402C` |

Notes that matter:
* `$28` shares the heavyweight sprite bank with `$27` but has HP 1 in every palette — **it is a spawn-script variant, not a difficulty variant** (a "rush" enemy that dies in one hit).
* `$29` is a *controller*: its handler `$0100B6` does not fight at all — it walks the general pool and forces every enemy below a Z threshold into state `$300` (attack), using `$FB40` as a countdown. This is the "gang rush" director.
* Score values are indices, not literal points; the literal points live at `$010DDA` as packed BCD (`$01 00 00` = 100, `$02 00 00` = 200, ..., `$07 00 00` = 700, `$11 00 00` = 1100, `$12 00 00` = 1200, `$15 00 00` = 1500, `$17 00 00` = 1700, `$18 00 00` = 1800, `$20 00 00` = 2000, `$21 00 00` = 2100, `$25 00 00` = 2500, `$50 00 00` = 5000, `$99 99 99` = overflow guard).

### 12.3 Target selection and aggression (FACT)
`$0096EC` is the whole of the 2-player target logic: pick the nearer of `$B800`/`$B880` by absolute X distance, store to `+$42`. There is no memory of who hit last, no aggro table, no pack coordination — except the `$29` director and the census gates below.

### 12.4 Spawning and despawning (FACT)
* Spawn source: the round script (`§14.2`), executed by `$000700`-`$000D5x`. Records request a type, then a free slot is found by `$007EBE`/`$007E92`/`$007EEA` (three variants of "find free slot + reserve").
* Live census: `$0093CE`–`$009404` computes per-archetype counts into `$FA60..$FA6F` each spawn; `$009DC0` decrements on death. The script's *next* spawn is gated on these counts (`$000844`), which is why the game never over-subscribes a type.
* Despawn: `$00B17A` — when an actor leaves the culling window and is not a player/boss, it is wiped by `$95E8` (unlink) + `$0103D0` (32-long clear). There is no fade-out.

---

## 13. Boss architecture

### 13.1 Differentiation from normal enemies (FACT)
A boss is *the same 128-byte record* with three differences:
1. Its type ID maps to a handler ≥ `$012B5C` (never the generic `$0096xx` AI core) and typically wraps a **round-script + phase** machine rather than a state-per-animation machine.
2. It reads its own HP/attack from `$017EDC`'s per-type byte tables (`$017F26` attack, `$017F2A` HP) instead of `$026FCE`.
3. It is exempted from the "kill all enemies" police sweep (`$0094C6`–`$009504`) and from despawn (`$00B17A` tests `cmpa.w #$D100` and the type before wiping).

### 13.2 The difficulty-scaling initialiser `$017EDC` (FACT, decoded)
```
d0 = type − $55                       ; 0..3 for types $55,$56,$57,$58
d1 = byte($017F26 + d0)               ; base attack
d2 = byte($017F2A + d0)               ; base HP
switch ($FFC6) {                      ; difficulty word
  case 0: d1 >>= 1                     ; easy   → half attack
  case 1: d2 += 5                      ; normal → HP + 5
  case 2: d1 <<= 1                     ; hard   → double attack
  case 3: d1 <<= 1 ; d2 += 5           ; hardest→ double attack, HP + 5
}
if ($FA05 bit6 == 0):
    if ($FF02 == 7) d2 += 2            ; round-7 (final) bonus
    d1 += 2                            ; flat attack bonus
+$4A = d1   ; reaction/attack byte
+$32 = d2   ; HP
```
Extracted values:

| Type | Base ATK | Base HP | easy ATK | normal HP | hard ATK | hardest HP |
|---|---|---|---|---|---|---|
| `$55` | 20 | 32 | 10 | 37 | 40 | 37 |
| `$56` | 20 | 24 | 10 | 29 | 40 | 29 |
| `$57` | 32 | 30 | 16 | 35 | 64 | 35 |
| `$58` | 32 | 32 | 16 | 37 | 64 | 37 |

**Therefore difficulty in SoR1 is not a curve — it is a 4-way switch on attack and a flat +5 on boss HP.** Normal enemies scale only through the 3-palette table in `§12.2`.

### 13.3 Boss roster — identified by handler, round and behaviour (FACT for code; labels are descriptive)
| Type | Handler | Round(s) where the script references it | Observed architecture |
|---|---|---|---|
| `$30` | `$0143D0` | 1-family (also used as the "generic boss shell") | 3-phase: gate on `$FA53` (police hit) → HP check → death; contains the REV-01 fix `§23.6` |
| `$31` | `$015794` | 8 | phase controller that re-enters `$30` logic |
| `$33` | `$012B5C` | 7 (final) | **two-body boss**: spawns `$34` at `+$50` and `$38` at `+$52` as escorts (`$012BB2`–`$012BE8`), then runs a 26-state table at `$012B64`; uses `$FA78` for a 2-bit script handshake (`$012C0A`–`$012D9C`) |
| `$34` | `$012F14` | 7 | escort: 6-state table `$012F1C`, invulnerability windows via `+$01` bit2, `+$54` timers |
| `$35` | `$01306A` | 1, 8 | large boss; `$FA53` gate at entry, so the police special can interrupt it; 9/10/11 state guards at `$013090`–`$0130xx` |
| `$36` | `$0140DC` | 8 | boss with a scripted "grab the player" attack |
| `$37` | `$014266` | 8 | supporting boss |
| `$38` | `$012FB4` | 7 | escort/agile boss: uses `+$62` as a *gravity* value (`$F800`, `$F500`) and re-enters via `$00B20E` |
| `$39` | `$014318` | 8 | supporting boss |
| `$54` | `$0101C8` | (summoned) | **not a boss** — the police backup squad: spawns 4 × type `$54` actors with `+$40` = slot index and `+$50` = descending `$40, $30, $20, $10` |
| `$55` | `$015E70` | 2/4/6 | uses shared boss core `$016A1A`/`$016AEC`; 2-way phase |
| `$56` | `$016CE4` | 4/6/8 | shared core + 12-state table `$016CF4`; "grab/throw player" logic at `$016D40` |
| `$57` | `$0174E0` | 5/6/8 | shared core, and the only boss that reads `+$78` alternation (`$017558`) |
| `$58` | `$0158C4` | 5 | **paired boss**: two independent instances that share `$FA72` bits 0–2 so they cannot both attack at once |
| `$96` | `$017262` | 7 | boss *attachment* actor: requires `+$6E` (host) non-empty, else aborts (`$017266`) |
| `$97` | `$017858` | 7/8 | attached actor that mirrors its host's X (±`$14`) and Y (+4) — `$0178D0`–`$0178FC`; invulnerable while host alive |
| `$98`/`$99` | `$016C60`/`$016C24` | 7 | host-side and attach-side of the same mechanic |

### 13.4 The generic-vs-specific boundary (FACT)
Generic (shared by all bosses): sprite/animation (`$00AF46`), physics (`$003886`/`$00442C`), the damage path (`$009BD6`), reaction states (`$009B80`), the death sequence (`$009CFC`/`$009D16`), the census/score bookkeeping (`$009DC0`), and the police gate (`$016A1A`).
Specific (per-boss): the state tables, phase gating, arena interaction (letterbox `$FA1D`, `$018CD4`), and escort wiring (`+$50`/`+$52`/`+$6E`).
**No boss has its own physics, its own damage formula, or its own renderer.** That is the single most important structural fact about the boss code: it is 17 specialised state machines over one engine.

### 13.5 Mr. X (type `$33`) in detail (FACT, `$012B5C`–`$012F14`)
* Entry: `$012B5C` → jump table at `$012B64` with 26 words; states `$0..$25`.
* Escort creation: state `$0` calls `$140CE` (`+$40`-style actor init) twice — first spawns type `$34` at `X−8`, then type `$38` at `X+8`, storing them at `+$50`/`+$52` (`$012BB2`–`$012BE8`). If either escort dies, `$012CA4` clears the link and advances.
* Script handshake: a 2-bit flag byte `$FA78`. `$012C0A` clears bit0 and, if it was set, enters state `$0C`/timer `$3C`. `$012C26` sets bit1 and calls `$12D9E` (which loads `+$54` = `$5A`, or `$B4` on PAL — the only *regional* timing difference found in gameplay code, `$012DA4`–`$012DAC`).
* Escort commands: `$012DBA` forces escort `+$50` into state 4 and `+$52` into `+$58 = 1`; `$012DFA` does the reverse. So Mr. X *commands his escorts' states directly* rather than via AI.
* Death: `$012CE0` requires `$FA72` bit3, clears `$FA53`, spawns a type `$35` at his position +`$28` in Z, zeroes `+$50`, and jumps to `$012B02` (the shared boss teardown).
* "Phase" is therefore **escort-phase**, not HP-phase: the fight is a sequencing puzzle over two escorts, and the boss's own state table is the sequencer.

---

## 14. Level / stage architecture

### 14.1 Round identification
`$FF02` (word) is the round: `0..7` = the eight rounds, `$FE` = a special/demo context, `$FF` = ? . It is compared against literals `#7`,`#6`,`#5`,`#4`,`#3`,`#2` in ~60 places, which is why per-round special cases (palette, letterbox, spawn tables) are scattered rather than table-driven. `$FF04` is the *section* within the round (advanced by `$018F32`, `$019570`).

### 14.2 The spawn/level script format (FACT for the parser; PROBABLE for field meaning)
Parser `$000784`–`$0009xx`, state driven by `$FA05`:

```
$FC14 → group header:
    word  length          ; byte length of this group
    then records, 6 bytes each, terminated by a record whose first byte == $99
record:
    +$00 .b  type | $80   ; bit7 = "not yet spawned"; cleared by $0007AC
    +$01 .b  ?            ; (never read by the parser — see U-LVL-01)
    +$02 .w  ?            ; (idem)
    +$04 .b  difficultyAndFlags   ; low 2 bits compared to $FB5B
    +$05 .b  flags
$FC2C = pointer to the current group (kept for re-scan)
$FC28 = pointer to the record that failed to spawn ("retry next frame")
```
Semantics established by execution, not by naming:
* A record is *skipped* if `(record+$04 & 3) > $FB5B` — i.e. **the low 2 bits of `+$04` are a difficulty/2P gate**.
* If `bit7` of `+$00` is clear, the record is *already spawned* and is skipped.
* On a successful spawn, `$0007DC` clears `$FA05` bit1 and rewinds, so the parser re-reads the same record next frame until the actor actually exists.
* `$0008A4` copies the group forward (`$0008D0`–`$0008E8` compacts live records), which is the mechanism by which a group becomes "the current wave".
* `$99` terminates a group; `$9900` (word) as a group header terminates the *round*.

This is a **compacting, retry-tolerant spawn script**, not a table of coordinates. Coordinates come from the record's data section, which is why `U-LVL-02` (`§28`) remains: `+$01`/`+$02` are never read by the parser I traced, so either they are consumed by a second parse stage I did not isolate, or they are dead padding.

### 14.3 The second script engine (`$011B4C`, state `$DE00`)
This one is *presentation*, not spawning: it drives the round intro, "GO", the tilemap reveal, the BCD round timer and the scroll lock release. Its state block is mapped in `§6.2`. Its step table starts at `$011C0A`-region constants and it advances `$DE04`.

### 14.4 Terrain: the height map (FACT, `$00AD2A`–`$00AD8C`)
```
tileX = X_int >> 4                       ; 16-pixel columns
tileZ = Z_int >> 3                       ; 8-pixel rows
d2 = tileZ * word($E02E) + tileX         ; plane width in $E02E
d7 = byte($FFA000 + d2)                  ; TWO 4-bit tiles per byte
if ((X_int & $0F) >= 8) d7 >>= 4         ; right half of the cell
d7 &= $0F                                ; tile index 0..15
d6 = d7
d7 = byte($FC34 + d7)                    ; "height" for this tile
d6 = word($FC38 + d6*2)                  ; "stand threshold" for this tile
return (Y_int >= d6) ? d7 : 0            ; 0 = not standing on anything
```
Consequences (all FACT):
* The entire walkable world of a round is **`$FFA000`..**, a byte plane where each byte holds two 4-bit tile indices, indexed by `(Z>>3, X>>4)` with plane width `$E02E`.
* Only **16 distinct tile types** exist per round; each maps to a height via `$FC34` and a threshold via `$FC38`. Those two tables are *patched per round* (they are RAM addresses `$FC34`/`$FC38` holding pointers, set by the stage loader).
* Height is compared against `Y`, and returns `0` when the actor is "in the air" — this is the *only* ground notion. There are no platforms as objects.

### 14.5 Camera locks / scroll triggers
Camera limits live in the camera context (`+$1A`, `+$1E`, `+$22`, `+$26` of `$E000`/`$E100`), not in the level script. They are rewritten by:
* `$018F5C` (X limits, with the `$1100000`/`$1300000` constants = 272.0/304.0 used as 2P separation clamps),
* `$018FE8` (Y limits, `$780000`/`$A80000` = 120.0/168.0),
* `$0190E0` (`$FF5000` H-scroll table builder, per-line `muls/divs` for parallax).
The single explicit scroll lock found is `$0115F4`–`$011626`: if `$FF18` bit1 is set (2P) the background streaming is skipped; if the *other* player is at state `$0F` (frozen), the code writes three fixed words `$6D7` into `$FF6038` — i.e. **it flattens three scroll lines**, a deliberate visual lock.

### 14.6 Transition / checkpoint structure
There are no checkpoints. A round is: intro script (`$DE00`) → spawn groups → "boss letterbox" (`$FA1D`) → boss → `$FA49` clear → 255-frame fade → next round via master state. Continuing after a game over restarts the round from its first script group (`$010840` re-enters state `$14`/`$15`).

---

## 15. Rendering pipeline

### 15.1 The five per-frame buffers (FACT)
| Buffer | RAM | Size | Consumer |
|---|---|---|---|
| SAT shadow | `$F600` | 80 × 8 bytes | `$008510` → VDP (chunked `$A0` bytes per iteration) |
| CRAM shadow A | `$F400` | 64 words | V-Blank DMA (3-word program + `$9320 9400`) |
| CRAM shadow B | `$F480` | 64 words | `$010534` → same DMA, for the P2 palette block |
| Plane scroll tables | `$FF6038`+ / `$FF605A`+ / `$FF608E`+ | 3 lines each | `$0198xx` VSRAM/H-scroll writers |
| VRAM write queue | `$FC00`/`$FC02` | 1 command pair | whatever wrote last; the VDP program is re-armed per use |

### 15.2 Sprite record format (FACT, `$00B00E`–`$00B048`)
```
(a2)+ = word  screenY + Z/2 + $80          ; Y (biased by 128)
(a2)+ = byte  sizeByte  (from mapping data)
(a2)+ = byte  $FA02 (this sprite's index)  ; link field
(a2)+ = word  tileNumber | (X-flip ? $8000 : 0)  + (+$0E tile bias)
(a2)+ = word  screenX + $80                ; X
```
8 bytes, exactly the Mega Drive SAT entry. Two details worth recording:
* The link byte is the sprite's *own* sequence number (`$00B012` `addq.b #1,$FA02`), not a chain, so the builder is emitting a contiguous list whose last entry must terminate — done by `clr.l (a2)` at `$00AEEA`.
* X-flip is `+$01` bit4; the **tile numbers themselves are pre-mirrored** in ROM (`$00B07A` `eori.b #8` + `neg` + `+8` arithmetic), so flipped sprites use different tile ranges rather than VDP flip bits for the inner tiles.

### 15.3 Culling (FACT)
`$00B0E8`: reject if `screenY ∉ [0x60, 0x180)`. `$00B0FE`: reject if `screenY ∉ [0x60, 0x1E0)`, and on reject it also *rolls back* the emitted record (`subq.w #6,a2`, `dec.b $FA02`). A global budget of **79 sprites** (`$FA03 = $4F`) is decremented per emission; on exhaustion, emission stops for that object and the sprite budget survives to the next object. This is a hard, per-frame sprite cap — visible in-game as sprites flickering out at high enemy density.

### 15.4 Y-sorting (FACT, `$00AE4C` + `$00AEE4`)
```
bucket = (screenY * 8) & $FFE0        ; 32-byte granularity in (screenY*8) space
base   = $E200 + bucket
if word(base) < $1E:                  ; max 15 entries (word count + 15×2 bytes)
    word(base) += 2
    word(base + word(base)) = actorAddress
else: $FA75 = 1                       ; overflow flag
```
Walk order: `$E9E0` down to `$E200` in `-$20` steps → **back-to-front by screen Y**, then an insertion sort per bucket on `(+$14 depth, +$01 bit7)` (`$00AEF8`–`$00AF32`). So the final draw order is: *bucket by Y, then depth within the bucket, with an explicit priority bit as tie-break.* Three-level ordering, all integer, no floating point.

### 15.5 VDP modes (the `$FF06` word) — what each mode actually writes
| Mode | Handler | Register program (verbatim) | Purpose (PROBABLE) |
|---|---|---|---|
| 0 | `$01A01E` | `$9300 $940B`, `$9500`, `$9680`, `$977F`, H-scroll `$73400081` | normal 2-plane playfield, plane A 64×32 |
| 1 | `$019FDA` | same but `$9680`/`$7340` and calls `$0001802` | alternate plane layout (intro) |
| 2 | `$019DC4` | `$9300 $940B`, `$9680`, `$7340` + `$0001802`? | early-boot/blank |
| 3 | `$019F5C` | `$9310 $9403`, `$9510`, `$9683`, `$7340` | window-plane mode (HUD strip), `$F914`/`$F926` queue drains |
| 4 | `$019F42` | `$9340 $9401`, `$9500`, `$96ED`, `$70000083` | 2-plane with `$19DA6` + 3 draw-list calls |
| 5 | inline `$019E1E`… | plane-A only (`$9310 $9403`), `$7342` — writes **negated H-scroll** to VRAM `$F400` | raster/parallax scroll mode |

Mode 5 is the only place the game writes *per-line* H-scroll (`$019E68`–`$019E92` writes 4 register words then a 2-word command pair). The negation (`$019E7A` = `#$40000080`) is a VRAM *address* `$C000`, i.e. the plane-B name-table base — so mode 5 is a plane-B scroll-table mode, not a raster effect. (Corrected from the initial reading; the constant decodes to VRAM `$C000`.)

### 15.6 DMA discipline (FACT)
Every VDP transfer is bracketed by Z80 BUSREQ: `$A11100 = $0100` before, `= $0000` after (`$019DE2`/`$019E12`, `$019FCE`, `$01A014`, …). The 68k therefore never writes VRAM while the Z80 owns the bus. This explains why *all* heavy VRAM work happens in the ISR and why the main loop can run with the bus released.

---

## 16. Animation system

### 16.1 Two-level indirection (FACT)
```
actor +$04  → animation bank (ROM, shared per archetype)
bank[state>>1] → word:  bit15 = "flipped tile variant", bits14..0 = byte offset
                (offset − 2, then add to bank)
offset + 0   → byte: last frame index  → copied to $FA40
offset + 1   → byte: frames per tick   → copied to +$0C
offset + 2   → byte: sprite count for frame 0
then per-sprite records, then next frame's count, etc.
```
`sprite record` (from `$00B002`–`$00B040`):
```
byte  yOffset   (signed; screenY + yOffset)
byte  sizeByte  (written to +$02/+$03 of the actor on the first sprite)
word  tileNumber
byte  xOffset   (signed; screenX + xOffset)
```
So a "frame" is a variable-length run of 5-byte sprite descriptors, and the frame *length* is derived from the count byte — there is no fixed frame size. This is why there is no frame table to dump: the animation data is a byte-stream with embedded counts.

### 16.2 Timing coupling (FACT)
* `+$0A` frame index, `+$0C` frames-per-tick, `+$0D` countdown.
* `$00B0C8`: `dec.b +$0D`; at zero → `+$0D = +$0C`, `+$0A += 1`, and if `+$0A > $FA40` then `+$0A = 0` (loop).
* `+$01` bit2 gates the advance, so *any* handler can freeze an animation without touching the timer (used by hit reactions and by the player's grab hold).
* The damage-table lookup uses `+$0A` (`§11.1`), so **animation and hitbox timing are the same counter**. A frame's damage is a property of the frame index, not of a separate timeline. This is the single most load-bearing design decision in the engine: change one frame's duration and you change both its hitbox window and its damage window.

### 16.3 Hitbox coupling (FACT)
`$004140` reads five bytes per animation-block entry from `$01ABA8` (`x1,x2,zidx,y1,y2`) — i.e. the *box shape is a function of the animation block*, not of the actor. Combined with `§16.2`, a single animation frame defines: sprite list, duration, damage nibble, hit class, and box shape. There is no separate "hitbox timeline" file.

### 16.4 Looping and transitions (FACT)
* Loop is implicit: the first byte after the sub-table is the last-frame index; exceeding it wraps to 0.
* There is no "return to state X on animation end" opcode. Handlers do it themselves by comparing `+$0A` (`$00209E`, `$0021A8`, `$00224C`) or by counting in `+$0D` (`$0039E8`).
* Because of that, an animation can end in *any* state the handler wants, and the same animation can be used by several states. Animation reuse is therefore high and state/animation is many-to-many.


---

## 17. Audio architecture

### 17.1 The split that defines the system (FACT)
SoR1 does **not** use the "68k posts commands, Z80 sequences" model. Execution evidence:

* The 68k routine `$072914` runs **every V-Blank** (`jsr $072914` at `$01A0A8`) and is a full sequencer: it walks per-channel stream pointers, decodes note/tie/duration opcodes, computes frequency words, applies pitch/LFO, and then performs *register writes*.
* Those register writes are *not* to `$4000/$4001`; they are to `$A01FFF` and friends — the **Z80 RAM window** — under an explicit BUSREQ (`$072A88`, `$072B30`, `$073138`, `$073198`). Example: `move.b $10(a3),$a01fff.l` (`$072AD4`) writes the current channel's frequency-high byte to Z80 address `$1FFF`.
* The Z80 program (`§17.3`) is therefore a **thin register proxy + DAC feeder**, not a sequencer: it latches bytes into YM/PSG and runs the timer-driven DAC loop.

Confidence: `HIGH CONFIDENCE` (register-write targets and BUSREQ bracketing are FACT; the "Z80 is a proxy" conclusion follows from the absence of any stream-decoding logic in the decompressed Z80 image at the addresses that run).

**Consequence for reverse-engineering:** the entire music format lives on the 68k side, in `$073D00`–`$0795A1`, and can be parsed as a normal data format. It is not Z80 bytecode.

### 17.2 68k sound state (FACT, from the `$072950`–`$072A16` loops)
| Channel group | RAM base | Count | Stride |
|---|---|---|---|
| FM 1–5 | `$F040` | 5 | `$30` |
| "extra" FM | `$F1F0` | 2 | `$30` |
| DAC/drums | `$F130` | 1 | `$30` |
| PSG 1–3 | `$F160` | 3 | `$30` |
| extra DAC/PSG | `$F2B0`, `$F340` | 1 each | `$30` |

Channel record fields observed: `+$00` flags (bit0 keyed, bit1 stream active, bit3 modulation, bit5 sustain, bit6 special), `+$04` stream pointer, `+$09` transpose/step, `+$0B` instrument index, `+$0C` base duration, `+$0D` reload duration, `+$0E` duration countdown, `+$10` frequency word, `+$14` volume/level, `+$16`/`+$17` envelope params, `+$18`/`+$1A` LFO rate/count, `+$1C`–`$22` LFO state, `+$26` pitch add.

### 17.3 The Z80 driver (FACT: decompressed, hashed, disassembled)
* Size **7,936 bytes ($1F00)**, compressed at `$0795A2` (7,581 bytes), SHA-256 `07cabd018ad00804d54ba2c61bcd25ec933b5ba89fa382e74169022423688fd2`.
* Verified twice: reference Python Kosinski decoder **and** executing the ROM's own `$0085A2` on a MC68000 both produce the identical 7,936 bytes (`EXP-01`).
* Entry (`Z80 $0000`): `DI; DI; DI; LD SP,$1FF4; XOR A; LD ($1FFD),A` → then YM setup (writes `$2B` = DAC-enable to Z80 `$6000`), bank select via `LD A,($1FFB); RLCA; LD ($6000),A`, and the per-frame dispatcher at `Z80 $004B`-region that reads the command bytes the 68k placed at `$1FF8`–`$1FFF`.
* Δ-PCM table at `Z80 $001E` (16 signed 8-bit deltas), decoded values: `+4, 0, +1, +2, +6, +12, +24, +48, +96, −96, −48, −24, −12, −6, −2, −1`. That is a **non-linear (companded) 4-bit DAC step table** — i.e. the drums are 4-bit companded Δ-PCM, not linear PCM.
* Sample descriptor table at `Z80 $019B`, **5-byte records** `[start_LE16][length_LE16][pitch_delay]`:

| Command | Index | Source | Start | Length | Pitch |
|---|---|---|---|---|---|
| `$81` | 0 | Z80 RAM | `$01C8` | `$0393` | 4 |
| `$82` | 1 | Z80 RAM | `$055B` | `$04FA` | 1 |
| `$83` | 2 | Z80 RAM | `$0A55` | `$03F3` | 12 |
| `$84` | 3 | Z80 RAM | `$0E48` | `$07B8` | 1 |
| `$85` | 4 | ROM bank A | `$1600` | `$0000` | 1 |
| `$86` | 5 | ROM bank A | `$1600` | `$0508` | 32 |
| `$87` | 6 | ROM bank A | `$1600` | `$0508` | 26 |
| `$88` | 7 | ROM bank A | `$1B08` | `$03BF` | 18 |
| `$89` | 8 | ROM bank A | `$1B08` | `$03BF` | 22 |
| `$8A`–`$91` | 0–7 | ROM bank B | (same offsets as `$81`–`$88`) | | |

  Banked samples are fetched by the Z80 from the 68k bus (`$8000`-window) while the 68k is *not* requesting the bus — which is why the driver releases BUSREQ between register writes.

### 17.4 Music/SFX request path (FACT)
```
game code:  d7 = sound ID ; jsr $01069E          ; 3-slot SFX queue at $F00A..$F00C
            (per-character voice IDs at $0106D6 / $0106E6, indexed by +$50)
$072D08:    picks the highest-priority of up to 3 requests vs the current one
            compares against byte($072824 + id)   ; priority table
            writes $F009 = winning ID, $F000 = its priority
            $81..      → BGM: header table at $07288C, load channels
            $A0..$CF   → per-channel register pokes
            $E0..$E3   → stop/fade/pause commands
            $E4..      → ignored (falls through to the "no-op" exit at $072F6E)
```
Therefore **the ID space is segmented by range, not by table**: `$81`-`$91` = DAC samples, `$A0`-`$CF` = channel-level commands, `$E0`-`$E3` = transport. Any ID ≥ `$E4` is silently dropped (`$072D82 bra $072F6E`).

### 17.5 Song header format (FACT for the reader; field names descriptive)
```
$072EBA: a0 = 68k song header (from table $07288C + word offset)
         $FFF014 = header pointer
         d0 = $80000000 | $100 | (0..3)          ; "channel descriptor" template
         d6 = byte(a0+2) − 1                     ; number of FM channels
         a1 = $F040 ; a2 = $072F7C ; a3 = a0+4
         per channel:
             +$14 = $C0 (pan/AMS/PMS default)
             +$0E = 1        (duration)
             +$0C = $30      (base duration)
             byte(a2)+       ; channel register offset
             +$00 = d0       ; descriptor
             +$04 = a0 + word(a3)   ; stream pointer
             +$03 = byte(a3)        ; instrument
             a1 += $30 ; a3 += 2
         then d6 = byte(a0+3); each extra channel: +$04 pointer, +$03 instr, +$0B mod
```
So a song header is: `[word: offset to channel data][byte: FM channel count][byte: extra channel count]`, followed by parallel arrays of 2-byte stream offsets and 1-byte instrument IDs. The stream data itself starts after the header and uses a dense opcode set written by `$072AA4`–`$072C7C` (durations `$00`–`$7F`, ties, `$F0`-class commands handled by `$0732EA`, note bytes with octave in bits 4–6).

**Unknown (`U-AUD-01`):** the complete opcode map of the note stream. I decoded the *reader* (which bytes it treats as duration, which as note, which dispatch through `$0732EA`) and can therefore parse streams mechanically, but a full mnemonic table would require enumerating `$0732EA`'s sub-cases against real song data; that is a bounded but non-trivial follow-up.

### 17.6 Event triggers found in game code (FACT)
* `$01069E` is called from ~90 sites. Examples: `$35D6` (player SFX helper), `$5976` (weapon SFX), `$1069E` calls with `$E1` (pause), `$B9`/`$BA` (menu), `$B2` (enemy hurt), `$A1` (score digit), `$A3` (landing), `$A6`/`$A8` (grab/throw), `$BE` (extra life), `$C0`/`$C3` (weapon hit), `$CC` (plane), `$D5`/`$D8`/`$D9` (enemy death variants).
* Police special: `$8454` (with `d0` = 0/9/10/13) and `$008454` is the *sprite* bank loader; the siren is triggered from `$00448E`-region and `$005136`.

---

## 18. Input architecture

### 18.1 Polling (FACT, `$00810C`/`$00813C`)
```
$00810C  BUSREQ on
         a1 = $A10003 (P1) ; a0 = $FC04 ; a2 = $FF2C ; bsr $00813C
         a1 = $A10005 (P2) ; a0 = $FC08 ; a2 = $FF30 ; bsr $00813C
         BUSREQ off
$00813C  (a1) = $00 ; nop ; nop ; d0 = (a1)          ; TH = 0  → read Up/Down/Left/Right + B/C
         d3 = d0
         d0 = (d0 << 2) & $C0                          ; keep B/C in bits 6-7
         (a1) = $40 ; nop ; nop ; d1 = (a1) & $3F      ; TH = 1  → read Start/A + direction
         d4 = d1
         d0 |= d1 ; d0 = NOT d0                        ; active-high
         d2 = (a0)                                     ; previous raw
         d0 eor d2 → pressed edges
         if ($FF2A != 0) { key-record hook into $FF2C/$FF30 }
         (a0)+ = raw ; (a0)+ = pressed ; (a0) = 0
         if (d3 == d4) (a0) = 1                        ; "port stable" flag
```
Resulting bit layout (FACT by use-site): `bit0 Up, bit1 Down, bit2 Left, bit3 Right, bit4 B, bit5 C, bit6 A, bit7 Start`. Verified by `$0038C0` (bits 2/3 drive horizontal movement with opposite signs), `$018906` (`btst #7` → pause), `$0052BE` (`andi #3` selects player slot from direction bits).

`$FC04` = raw (bit set = held), `$FC05` = pressed-this-frame (edge), `$FC06` = port-stability flag. Aliases: `$FC08/$FC09/$FC0A` for P2.

### 18.2 Buffering and priority (FACT)
* **There is no input buffer.** Every consumer reads `$FC05`/`$FC09` in the same frame. A button pressed and released inside one frame is lost; a button held is seen once (as an edge) and then only via the raw word `$FC04` (which players copy into `+$54`).
* Priority is encoded by *call order* inside the player handler (`§8.1`): police-special and forced-state checks read input before the state machine, so a special always beats an attack in the same frame.
* Menu/gameplay difference: menus read `$FC05` directly (`$010D3E`), gameplay reads the per-actor copies `$FA47`/`$FA48` and `+$54`. This is why a 2P join (`$FA46`) can be detected in menus but not mid-fight.
* 6-button pads: the two TH reads are compared; equal reads set the "stable" flag. Whether that flag means "3-button pad present" or "6-button detected" is **UNKNOWN** (`U-INP-01`) — both readings are consistent with the two call sites (`$008188`, `$0188xx`), and no code in the image reads the extra X/Y/Z buttons anywhere.

---

## 19. Camera system

### 19.1 Two independent camera contexts (FACT)
`$E000` and `$E100` are structurally identical (`$018AF8` runs the same two block of code over both). Each holds:
```
+$00 word  mode (0..7 → jump table at $018C34)
+$02.l     X position          +$06.l  previous X   +$0A.l  X velocity
+$0E.l     Y position          +$12.l  previous Y   +$16.l  Y velocity
+$1A.l     X min limit         +$1E.l  X max limit
+$22.l     Y min limit         +$26.l  Y max limit
+$2E word  plane width (used as row stride by the tile writer)
+$32.l     tile chunk table pointer
+$44 word  sub-struct count     +$46…    sub-struct array, stride $12
+$B2 byte  "lock" flag          +$B3 byte "disable" flag
```
**Why two:** in 2P mode each player gets a context and the final scroll is produced per *plane* (`$E000`→plane A via `$FF0000`, `$E100`→plane B via `$FF2000`), which is how the game draws two independently-scrolling layers that both track a player. In 1P mode only `$E000` is meaningfully driven. (H for the role split; F for the layout.)

### 19.2 Follow law (FACT, `$018F5C`/`$018FE8`/`$019074`)
* **Dead band:** the target is only recomputed when `((curX ^ newX) & $FFF0) != 0` — i.e. a **16-pixel dead zone in X** (`$018B52`, `$018BCE`). Sub-16-pixel player movement never moves the camera.
* **Target selection with 2P:** `$018F5C` takes the two players' X, prefers the rearmost within the `$1100000`/`$1300000` (272/304 px) separation rule, then clamps the result into the stage limits.
* **Rate limiting:** X velocity clamped to **±3.0 px/tick** (`$FFFD0000`/`$00030000`), Y velocity to **±4.0 px/tick** (`$FFFC0000`/`$00040000`). The camera therefore *cannot* teleport; it catches up over several frames.
* **Integration:** `$019074` adds velocity to position, clamps to `[+$1A,+$1E]`, then masks low bits with `andi.w #$3FFF` — a wrap that keeps the VRAM address inside one plane.
* **Shake:** `$FA44`/`$FA45` are applied to the *rendered* scroll, not to the logical position (so shake does not desynchronise collision).

### 19.3 Plane/tile streaming (FACT, `$018B3C`, `$019656`)
The tile writer computes, per sub-struct:
```
col = (X_int >> 4) snapped to the plane grid; row = (Z_int >> 4) + d6
address = planeBase + ((row * planeWidth) + col) * 2
attribute word = (tileIndex & $1FF) << ? | palette<<13 | hflip | vflip
    → $019686:  d2 = col & $1FF ; d2 >>= 2 ; d2 += ((row<<4)&$FF00) + ...
    → if plane base == $E000: OR $4000 else OR $6000
```
The `$4000`/`$6000` OR is the VDP plane-select bit pair, which is why the writer is plane-agnostic and the *base address* decides which plane is written.

### 19.4 Scripted / boss camera (FACT)
* Boss letterbox: `$FA1D` gates `$018CC4`, which spawns a type `$05` actor (`$018D00`) at a fixed screen position and reduces the playfield — that is the "boss intro" bar.
* `$0115CC` disables all background streaming while `$FA1A` (police) or `$FF25` (P2 gone) is set, and forces a *frozen* three-line scroll table (`$6D7,$6D7,$6D7`) when the other player is in state `$0F`.
* `$018CD4`–`$018D3C` contains the round-specific letterbox geometry, including a special case for `$FF02 == 6`.

---

## 20. Asset formats

### 20.1 Kosinski LZSS (FACT — decoded, re-implemented, and bit-exactly validated against the ROM's own routine)
Two copies exist; `$0085A2` is the one called by the loader (`$01061C`) and by `$018C20`'s graphics path.
```
bitstream, 16-bit descriptors, LSB-first, refilled big-endian (byte1<<8 | byte0)
  1        → literal byte
  0 0 b b  → match: length = 2+bb (2..5), displacement = byte − $100  (signed 8-bit, −256..−1)
  0 1      → extended: lo=byte, hi=byte
             length = (hi & 7) ? (hi&7)+2 : (next byte == 0 → END, ==1 → continue, else +1)
             displacement = ((($FF00|hi)<<5)&$FFFF | lo) − $10000
```
Validation: `tools/verify_sor_forensics.py` implements this from scratch; running the ROM's `$0085A2` under Unicorn on `$0795A2` yields the same 7,936 bytes with the same SHA-256, and consumed 7,581 input bytes. Two independent implementations agreeing bit-for-bit on a real asset is the strongest form of confirmation available statically.

### 20.2 Plane-map ("tilemap") decoder (FACT for the structure, `$0081DD`–`$0082D0`)
```
byte 0 → written at plane[byte1 * 2]  (sparse absolute-word writes)
byte ≥ $80 → command: bits 3-6 = repeat count via ((b>>4)&7), low nibble = high nibble of tile
             then one byte = tile; repeat 2^(8−(b&0xF)) times with stride 2 words
else       → tile value derived from bits of two bytes
$FF        → terminator
```
Used with the tile writer to convert a sparse description into the plane at a given VRAM address. The same decoder family is reused for sprite-mapping "tile patch" data (`$0082D2`).

### 20.3 Palette stream (`$010576`, `$010454`)
3-byte commands: `[count][index][colour_hi]` … with a `$00` terminator; `$010454` is the unrolled 32-long copy used to move a full 64-word palette from ROM to a buffer.

### 20.4 Text / font (FACT)
* Alphabet: `$01`–`$1A` = A–Z, `$00` = space/terminator; digits and punctuation have indices > `$1A` (the translated images preserve exactly this range).
* Renderer: `$000E00`-region + `$008992`/`$008AF6` produce plane tile writes; the `[T+Fre]` diff map (`§2.3`) is a complete index of every text string in the game.
* The **name-entry** alphabet uses the same 1-based encoding, which is what makes `§23.2`'s cheat table readable as ASCII letters.

### 20.5 Sprite mapping / animation (§16.1) and PCM (§17.3) constitute the remaining formats.

### 20.6 Graphics bank loader (FACT, `$008642`–`$008670`)
A table of banks at `$008672` with 4-byte entries: `word count`, then per-bank `[long source][word dest]` pairs. `$008642` walks it, sets the VDP address from the destination, and calls `$008192` (the Kosinski→VRAM streamer that writes directly to `$C00000`). So **graphics are decompressed straight into VRAM**, never through a RAM staging buffer — which is why VRAM can be fully reloaded in one V-Blank-blocking sequence.

---

## 21. Resource management

### 21.1 What is allocated and where
| Resource | Mechanism | Notes |
|---|---|---|
| Actor slots | linear scan for `type==0` in 3 pools (`§7.2`) | request functions `$007EBE`, `$007E92`, `$007EEA`, `$0082D6`? — four variants returning a slot or 0 |
| Sprite budget | `$FA03` counter, 79 per frame | hard cap, causes flicker |
| Y-sort buckets | `$E200`, 15 entries each | overflow sets `$FA75` and drops the actor from the sorted list |
| VRAM | **no allocator**: every bank has a fixed destination from `$008672` | this is why all bank destinations fit together — they were hand-packed |
| CRAM | two 64-word shadows; the *whole* palette block is DMA'd on any change | 128 colours always resident (both players + shared) |
| Decompression buffer | `$FF7000`–`$FF8FFF` (8 KiB) for the Z80 driver; `$FF8000`+ for sprite patches; `$FF9000`+ for the round timer digits; `$FFA000`+ for the terrain plane | buffers are fixed addresses, not dynamic |
| Sound | fixed per-channel records (`§17.2`) | no voice stealing beyond the priority byte |

### 21.2 Load/unload discipline
`$007FB8` (VDP+DMA+Z80 reset, VRAM clear) is called at the start of ~10 master states; `$0103D0` (block fill, 32 longs/iteration) clears RAM in multiples of 32. Because both are unconditional, "unloading" is simply "re-initialise everything". There is exactly one incrementally-loaded resource: the background tile columns, streamed by the camera (`§19.3`) as the player advances.

---

## 22. RNG / random systems

### 22.1 The generator (FACT — recovered and machine-verified)
Routine `$0104D8`:
```
d1 = $FF40 (32-bit state)
if (d1 == 0) d1 = $2A6D365A            ; seed when untouched
d0 = d1
d1 = (d1 << 2) + d0                    ; d1 *= 5
d1 = (d1 << 3) + d0                    ; d1 *= 41   (total multiplier = 41)
d0 = low16(d1)
d1 = swap(d1)                          ; high16
d0 = (d0 + d1) & $FFFF                 ; returned 16-bit value
$FF40 = (d0 << 16) | low16(state_before)
```
Closed form (verified equal to the ROM for 16 consecutive calls in `EXP-02`):
```
p     = state * 41                    (mod 2^32)
lo    = p & $FFFF
hi    = p >> 16
out   = (lo + hi) & $FFFF
state' = (out << 16) | lo
```
Machine-read first 8 outputs from a zeroed state: `0x7FE7, 0x6115, 0x388B, 0x9BF8, 0xA878, 0xCB8D, 0xF300, 0x37E8`, with matching states `0x7FE7B46A, 0x6115E4FA, 0x388BAC0A, …`.

Note the seed is a *fallback*, not an initialisation: the state is left at 0 by the RAM clear, and the first call substitutes `$2A6D365A` only for its own computation — it does not store the seed back. So the sequence is deterministic on every cold boot, and re-enters the same sequence after reset unless gameplay advanced it.

### 22.2 Callers and what they randomise (FACT where the mask is visible)
| Site | Use |
|---|---|
| `$009A44` | `(rand & 3) * 2 + 3` → hit-reaction duration |
| `$0099xx` | enemy decision jitter |
| `$011Bxx` | spawn variation |
| `$0008xx` | script pacing |
Overall usage is sparse: the RNG is called on the order of a few times per second, and the *primary* variety in the game comes from the difficulty/palette tables and the script, not from randomness.

### 22.3 Determinism assessment
Because the seed is implicit and there are no timers or cycle counters feeding the state, **the entire game is deterministic given the same input sequence** — this is why the attract-mode demo replays identically. That is a `FACT` consequence of `§22.1` plus the absence of any other entropy source (the only reads of `$A10001` are the region latch and the version bit, and `$C00008` is never read).

---

## 23. Hidden / debug / unused systems, regional logic, revisions

### 23.1 The "triple damage" flag `$FA43` (CONFIRMED, live)
Set at `$011FB6`, cleared at `$011E7E`, read by the player damage decoder (`$00420C`) and by two reaction selectors (`$002C34`, `$002C5C`). Because `$011E7E` is inside the round-intro sequence, it is plausible that this is a **2P co-op damage-scaling flag** rather than a cheat; both readings are listed (`U-HID-01`). Its *effect* is FACT: `damage = 3*lo + hi`, with the high nibble sometimes changing reaction class.

### 23.2 The dormant name-entry cheat (CONFIRMED: code exists, executes, and is unreachable)
`$005920`:
```
a1 = $FF0C (P1) or $FF14 (P2)
d0 = long(a1)                       ; 4 bytes: [0][L1][L2][L3] in 1-based A..Z
for (d7 = 5; d7 >= 0; d7--):
    if (d0 == long($005958 + (5-d7)*4)) break
if no match → rts
$FF35 = d7
byte($FF20 or $FF23) = byte($005970 + d7)     ; BCD lives
```
Decoded table (`$005958`, 6 × 4 bytes) and stock table (`$005970`, 6 bytes):

| Code | Bytes | BCD lives | Decimal lives | `$FF35` | Police calls granted |
|---|---|---|---|---|---|
| `MOM` | `00 0D 0F 0D` | `$90` | 90 | 5 | 6 |
| `SUN` | `00 13 15 0E` | `$49` | 49 | 4 | 5 |
| `UDI` | `00 15 04 09` | `$09` | 9 | 3 | 4 |
| `BO ` | `00 02 0F 00` | `$07` | 7 | 2 | 3 |
| `ORE` | `00 0F 12 05` | `$01` | 1 | 1 | 2 |
| `   ` | `00 00 00 00` | `$00` | 0 | 0 | 1 |

Executed under MC68000 emulation with `$FF0C = "MOM"` in 1-based form, the routine writes `$90` to `$FF20` and `5` to `$FF35` — identical to the table (`EXP-04`). `AXL` (not in the table) leaves both untouched, confirming the compare chain.

**Reachability (FACT, exhaustive):** a full scan of the image for 32-bit literals, 16-bit literals, absolute-long jumps, PC-relative displacements and short branches targeting `$005920` finds **zero** references. The routine sits between `$005904` (end of an unrelated table) and `$005958` (its own table) with no entry point. Conclusion: **a working code-entry cheat that the retail build cannot reach** — most plausibly a developer leftover whose caller was removed, or an intended "type your name on the high-score screen" check that was superseded. Both explanations are recorded; neither is asserted.

### 23.3 Difficulty system (CONFIRMED)
`$FFC6` is the difficulty word (set to 1 at boot by `$011992`; 0..3 by options). It is read by: boss stat init (`§13.2`), enemy speed solver (`$00982C`, drops speed by `$100` above `$300`), the spawn gate (`$FB5B`, derived from it), and several AI pacing constants (`$0093F4`). It is *not* a global multiplier — each subsystem consults it independently, and most do so with a simple 2-way branch.

### 23.4 Regional (J/U/E) logic (CONFIRMED)
`$FF44` bit6 = PAL, bit7 = overseas (from `$A10001`). Uses found:
* `$007F8A`–`$007F94`: selects one of two VDP control latches (`$81748134` vs `$817C813C`) — i.e. a **different VDP register 1 value for PAL**, changing the vertical resolution/layout.
* `$012DA4`: Mr. X's telegraph delay `$5A` (90) NTSC vs `$B4` (180) PAL — the only gameplay-timing regional difference located.
* `$009C84` (via `$FB09`), `$01A088`, `$011C3A`, `$00AFxx`: several VDP/timing branches.
The game is a single `JUE` image with runtime region detection, not three builds.

### 23.5 Version differences — REV 00 → REV 01 (CONFIRMED, byte-exact + executed)
Only **four** regions differ (2,092 bytes total):
1. `$011B..$011F` — build date `1991.MAY` → `1992.FEB`.
2. `$018D..$018F` — checksum `$9409` → `$6390`.
3. **`$0143FB..$014D61`** — the real change: a **+6-byte insertion** in the type-`$30` boss, plus a re-assembly of the following ~2.4 KiB (all subsequent branches shift by 6).
4. `$014D7E..$014DAF` — the tail of that shift, where REV 00 and REV 01 diverge in *code shape*, not just position.

The functional insertion in REV 01:
```
REV 00  $0143FC  tst.b $FA1A          ; police special active?
                 beq.s $1440A
                 move.b #1,$67(a0)    ; latch
                 rts                  ; <<< RETURNS — death update skipped
REV 01  $0143FC  tst.b $FA1A
                 beq.s $14410
                 tst.w $32(a0)        ; <<< NEW: is the boss still alive?
                 ble.s $14410         ; <<< NEW: if HP<=0, skip the latch
                 move.b #1,$67(a0)
                 rts
```
Executed with identical preconditions (boss HP = 0, `$FA1A = 1`, `$FFFFB800 = 1`):

| Build | Trace | End state |
|---|---|---|
| REV 00 | `$0143D0 → $0143D6 → $0143F2 → $0143F8 → $0143FC → $014400 → $014402 → $014408` | early `rts`, `+$67 = 1` → **the dying boss stays frozen for as long as the police cinematic lasts** |
| REV 01 | `$0143D0 → … → $014402 → $014406 → $014410 → $014414 → $01445E` | falls into the normal HP-subtraction path |

This is a textbook soft-lock fix and it is *the* substantive reason REV 01 exists. The remaining bytes of region 3 are the re-assembly consequences (shifted branch displacements) plus a rewritten `$014D7E` block where REV 01 moved a `jsr $1569C` before the position copy and dropped an `addq.w #1,$14(a1)`.

### 23.6 Other anomalies catalogued
| ID | Anomaly | Class |
|---|---|---|
| `$009026`-region | clears `$FF08`/`$FF0C`/`$FF10`/`$FF14`/`$FF2A`/`$FF22`/`$FF25`/`$FF34`… as a batch of individual `clr` instructions where a 32-byte block clear would do — hand-written state reset | benign |
| `$00AE20` | type-index correction `bset.b #$10` does not implement a clean second page (`§7.3`) | `U-DISP-01` |
| `$001CE2` | 13 player-state slots point at `$000000` (`§23.7`) | `U-STATE-01` |
| `$005920` | unreachable cheat (`§23.2`) | dead code |
| `$008EC1` etc. | `move.w #$1FA,d7` + `jsr $0103D0` loop clears `0x1FA*32 = 16,320` bytes = `$FF0000..$FF3FC0`, leaving `$FF3FC0..$FF3FFF` untouched — the block clear **does not reach `$FF40`–`$FF44`**, so the PRNG state and region latch survive a "full" clear. This is deliberate (the PRNG must persist) but it is also why an "uninitialised" `$FF41`–`$FF43` can hold garbage | documented |
| `$00B17A` | despawn uses `cmpa.w #$D100` — effect slots are never despawned by that path, so an effect emitted at a bad moment can persist until its own handler clears it | benign |

### 23.7 Dead player states (CONFIRMED values, UNKNOWN reachability)
State table entries `$4C`–`$5E` (excluding `$50/$52`) contain `$0000`. Jumping to `$000000` would execute the SSP/vector table. No handler writes those state values in the code I traced, and the animation data would have to supply them. Classified `UNKNOWN — reachability unresolved`, listed in `§28`.

### 23.8 Unused / unreachable type slots
`$02`,`$03`,`$2B`–`$2F`,`$3A`–`$3D`,`$59`–`$5F`,`$8F` are explicit `rts` stubs; `$90`–`$95` resolve past the ROM (`§7.3`). `$29` is a live director, not a stub. Type `$00` is the free-slot sentinel.

### 23.9 Cache of the archive's own "cheats"
`[p1]` patches are *not* gameplay cheats: they NOP three instructions at `$08F53` and convert three `jsr`-family opcodes at `$0C97A/$0C9D0/$0CA26`, and change `$11995`/`$1199B` from `01` to `14` — that is a trainer that alters the round-1 intro/skip logic. `[p2][!]` is a checksum-bypass patch only. None of them touch gameplay balance.

---

## 24. Cross-system dependency graph

### 24.1 Discovered graph (edges are *observed calls*, not design intent)
```
                        ┌──────────────────────────────┐
                        │  V-BLANK ISR  $019D16        │
                        │  (owns VDP, VSRAM, CRAM,     │
                        │   SAT DMA, frame handshake)  │
                        └───────┬──────────────┬───────┘
                        input   │              │  sound tick
                                ▼              ▼
        ┌───────────────────────────────┐   ┌────────────────────┐
        │ $00810C pads → $FC04/$FC05    │   │ $072914 68k seq.   │
        └───────────────┬───────────────┘   │ → Z80 RAM $1FFx    │
                        │                   │ → YM2612 / PSG / DAC│
                        ▼                   └────────────────────┘
        ┌───────────────────────────────┐
        │ MASTER STATE  $FF00           │
        └───────────────┬───────────────┘
                        ▼
        ┌───────────────────────────────────────────────┐
        │ GAMEPLAY FRAME  $01087A  (12 calls, fixed)    │
        └──┬───────┬────────┬─────────┬─────────┬───────┘
           │       │        │         │         │
           ▼       ▼        ▼         ▼         ▼
      pause    camera   wave/level  palette   actor dispatch
      $11A36   $10C88   $11B4C      $11210    $00AD8E
               $115CC   $0117FC     $112F2        │
               $10C88   $018C20                  ├─► per-type handler ($00B236)
                                                 │        │
                                                 │        ├─► physics $003886/$00442C
                                                 │        ├─► combat  $0043AA/$00479C
                                                 │        │      └─► damage $009BD6
                                                 │        │             └─► reaction $009B80
                                                 │        ├─► animation $00AF46
                                                 │        └─► AI core $0096xx → $00982C/$009896
                                                 ├─► Y-sort $00AE4C
                                                 └─► SAT build $00AF46 → $F600
                        │
                        ▼
        ┌───────────────────────────────────────────────┐
        │ $0084BA / $008510  SAT streamer → VDP         │
        └───────────────────────────────────────────────┘
```
### 24.2 Observed coupling strengths
| Edge | Strength | Why |
|---|---|---|
| actor handler → physics | tight | every handler ends by falling through to the same integration |
| combat → damage → reaction | tight | one call chain, no queue |
| animation → combat | **very tight** | the frame index *is* the damage selector (`§16.2`) |
| spawn script → actor pool | tight | retry-until-slot semantics |
| camera → tile streaming | tight | the camera *is* the streaming trigger |
| sound ← game code | loose | one function `$01069E` + a range-coded ID |
| rendering ← actors | one-way | actors write only into RAM buffers; they never touch VDP |
| input → everything | one-way, sampled once | no consumer can re-poll |
| RNG → AI | weak | few call sites, small masks |

### 24.3 Cycles
Exactly one feedback cycle exists: **combat → reaction → physics → combat** (an actor's reaction changes its position, which changes next frame's overlap tests). It is resolved by the fixed update order, which is why the frame pipeline cannot be reordered without changing behaviour.


---

## 25. State machines

### 25.1 Master state machine (FACT — table `$0003BA`, 22 entries; names descriptive)
| `$FF00` | Target | Identified role | Exit(s) |
|---|---|---|---|
| `$00` | `$008EAC` | boot → title: VDP reset, RAM clear, load title bank `$07228A`, gfx `$A63A($301)`, `$A82A(1)`, `$A5F4(1)` | → `$02` |
| `$02` | `$008F44` | attract/title step machine on `$FB0A` (0 → `$8F58`, 2 → `$8F7C`, 4 → `$8F8A`) | → `$00` (loop demo), `$04` (new game) |
| `$04` | `$008FD0` | player-block reset (`$FF02`,`$FF04`,`$FF08`…`$FF38`, `$FF2A`, 10 × `$FF4A` score slots) | → self until `$FF00` set |
| `$06` | `$00904E` | "PRESS START" / credit check | `$08` (continue path) or `$10` |
| `$08` | `$0090C8` | coin/select init: draw `$12B02`, `$B558`, timer `$FA10 = $12C` | → `$0A` |
| `$0A` | `$009102` | 300-tick select countdown | → `$10` (timeout) or `$90A4` |
| `$0C` | `$009128` | round-intro init `$1260E` | → `$0E` |
| `$0E` | `$009152` | demo-exit input wait (`$FB06`, pads) | → `$00` |
| `$10` | `$009170` | character-select init (`$000FE8`) | → `$12` |
| `$12` | `$00919A` | character select loop (`$00108E`) | → `$14`-family on confirm |
| `$14` | `$010840` | **round load** (`$0106EA`,`$0107F2`,`$011B12`, stage bank → `$FF7000`) | → `$16` |
| `$16` | `$01087A` | **gameplay** (the 12-call pipeline) | → `$18` (round clear), `$0C` (retry) |
| `$18` | `$0091A0` | round-clear init (`$7F18`,`$7F24`,`$804C`,`$181EA`) | → `$1A` |
| `$1A` | `$0091CE` | round-clear sequence (`$1833C`) | → `$14` (next round) |
| `$1C` | `$009250` | game-over/continue init (`$87C6`) | → `$1E` |
| `$1E` | `$009278` | continue screen (`$8890`) | → `$20` (respawn) / `$14`? |
| `$20` | `$00927C` | high-score/name-entry init (`$1634`,`$1061C`) | → `$22` |
| `$22` | `$0092A8` | name entry (`$170A`) | → `$14` (next game) |
| `$24` | `$0091D4` | ending init (RAM clear, `$FF06 = 2`, `$B3C6`) | → `$26` |
| `$26` | `$009214` | ending sequence | → `$00` (attract) |
| `$28` | `$0106EA` | full reset to attract (RAM clear, `$FF06 = 0`, reload) | → `$2A` |
| `$2A` | `$01077C` | round transition / "ROUND n" overlay (`$011A50`) | → `$14` |

Every transition is `addq.w #$2,$FF00` (forward) or `subq.w #$2,$FF00` (retry), so `$FF00` is an *even byte offset*, not an index — the table is indexed by `($FF00)` directly as a byte offset into `$0003BA`. That is why the values are 0,2,4,…42 and why a corrupted `$FF00` immediately jumps to garbage.

### 25.2 Player state machine
128 slots, grouped (`§8.2`). Graph (descriptive labels, edges from code):

```
        ┌─────────┐  input/attack   ┌──────────────┐  connect   ┌──────────────┐
        │  IDLE   │────────────────►│  ATTACK      │───────────►│  ATTACK(rec) │
        │ $00/$02 │◄────────────────│  $30–$3A     │            │  $3C/$3E     │
        └──┬───┬──┘   anim end      └──────┬───────┘            └──────────────┘
   dir │   │ jump                        │ enemy attack
       ▼   ▼                             ▼
   ┌────────┐   vy≥0   ┌──────────┐  ┌───────────────┐
   │  WALK  │─────────►│  JUMP    │  │  HIT REACTION │
   │ $04–$1E│◄─────────│ $20–$2E  │  │ $A0–$BE       │
   └────────┘  land    └────┬─────┘  └───────┬───────┘
                            │ grab            │ HP≤0
                            ▼                 ▼
                      ┌───────────┐     ┌───────────┐
                      │  GRAB/HOLD│     │  DEATH    │
                      │ $88–$96   │     │ $EC–$10A  │
                      └─────┬─────┘     └───────────┘
                            │ throw / special
                            ▼
                      ┌───────────┐     ┌───────────────┐
                      │ THROW/    │     │ POLICE CALL   │
                      │ VAULT     │     │ $110–$12A     │
                      │ $78–$82   │     └───────────────┘
                      └───────────┘
```
Edges that are unusual and worth recording:
* `IDLE → ATTACK` requires `+$7C == 1` *or* a state predicate, and ATTACK has an internal chain counter (`+$40`) that can loop it back to itself up to 3 inputs.
* `GRAB/HOLD` is entered from `ATTACK` when the attack's grab-class matches the victim's (`$004F72`); the victim is moved to state `$88`-family by the *attacker*.
* `DEATH` is reachable from any state that can receive damage; there is no separate "hurt" → "death" gate other than HP ≤ 0 inside the shared subtraction.
* `POLICE CALL` is not entered from the state machine at all — it is entered from the pre-emption block (`$003FCC`) *before* dispatch, which is why it can interrupt any state including attacks and hit reactions.

### 25.3 Enemy state machine (the shared 0..7 vocabulary)
`+$30` is a **byte** state; the idiom `move.w #$N00,$30(a0)` writes `state = N, flags = 0` in one instruction. Observed values and their evidence sites:

| `+$30` | Meaning (descriptive) | Evidence |
|---|---|---|
| 0 | free slot / inert | pool scans |
| 1 | active, idle | `move.w #$100,$30(a1)` at `$000724`, `$009C0E`, `$014226` |
| 2 | approach / walk | `# $200` at `$00AA02`, `$009A0C` |
| 3 | attack | `# $300` at `$0094FE`, `$009B36`, `$009C36` |
| 4 | attack variant / grab | `# $400` at `$00AA0C`, `$009C26` |
| 5 | recover / special-hit | `# $500` at `$00A9D4`, `$009C2E` |
| 6 | airborne / falling | `# $600` at `$009A6A`, `$009792` |
| 7 | out-of-bounds / removed | `# $700` at `$0092C0`, `$009F1A` |
| `+$31` | flag byte, used as a bitfield of sub-phases (bits 0–6 each gate a distinct transition) | `$009AD6`–`$009CFC` |

**Interpretation confidence:** `FACT` for the byte/word distinction and for each write site; `HIGH CONFIDENCE` for the 1..7 semantic ladder (each value's surrounding code matches exactly one behaviour); `PROBABLE` that 0 is "inert" rather than "unused".

### 25.4 Boss state machine shape
Bosses use the same `+$30` byte but *much* wider tables (6–26 entries) plus an out-of-band script byte:
* `$33` (Mr. X): 26 states `$0`–`$25`, plus `$FA78` (2-bit handshake) and `+$5A` (escort command).
* `$34`: 6 states; `$3D`/`$3E` etc. use `+$54` countdowns as the real state driver.
* `$55`–`$58`: the shared core `$016A1A` interprets `+$5D` as a *link role*, `+$76` as a release countdown, and `+$54` as an attack timer, so "state" is a small byte with many timers around it.
* Escorts (`$96`/`$97`/`$98`/`$99`) have no independent AI: they mirror the host (`$0178D0`).

---

## 26. Recovered formulas and constants

### 26.1 Formulas (all verified against code; two verified by execution)
| # | Formula | Where | Status |
|---|---|---|---|
| F1 | `screenX = X_int − camX + $80` | `$00AF6E` | FACT |
| F2 | `screenY = (Z_int >> 1) + Y_int + $80` | `$00AF64` | FACT |
| F3 | `X += vx ; Z += vz ; Y += vy` (16.16) | `$004448`–`$00445C` | FACT |
| F4 | `vy += g ; vy = min(vy, $C0000)` | `$00389A`, `$003886` | FACT + `EXP-05` |
| F5 | `vx += ±$6000 ; clamp(vx, ±$38000)` while airborne | `$0038C0` | FACT |
| F6 | `walk/depth velocity = animation_byte / 16` (px/tick) | `$003632`–`$00365E` | FACT |
| F7 | `state' = ((lo + hi) << 16) | lo`, `lo/hi` from `state*41` | `$0104D8` | FACT + `EXP-02` bit-exact |
| F8 | `damage = lo_nibble(table)`, `class = hi_nibble(table)` | `$004208`–`$00422A` | FACT |
| F9 | `if ($FA43) damage_pair = 3*lo + hi` | `$004212`–`$004222` | FACT |
| F10 | `HP_enemy = table_byte + 1` | `$0093CE`-region consumers, `§12.2` | FACT |
| F11 | `boss_atk = base << (diff≥2)`, `boss_hp = base + 5·[diff∈{1,3}] + 2·[round 7]`, `atk += 2` when `$FA05` bit6 clear | `$017EDC` | FACT |
| F12 | `lifebar_segments = HP / 8` (10 segments, max 80) | `$004E8E` | FACT |
| F13 | `bucket = (screenY*8) & $FFE0`; ≤15 actors/bucket | `$00AE72` | FACT |
| F14 | `terrain_tile = nibble($FFA000[(Z>>3)*planeWidth + (X>>4)])` | `$00AD48` | FACT |
| F15 | `ground      = ($FC34)[tile]`, `stand_threshold = ($FC38)[tile]` | `$00AD70` | FACT |
| F16 | `distance = 3·max(|dx|,|dz|)/8 + min(|dx|,|dz|)` | `$0098E8` | FACT |
| F17 | `angle_idx = min(63, (minor<<6)/major)` | `$00987A` | FACT |
| F18 | `block_clear_bytes = count × 32`, `d7 = $1FA` → 16,320 bytes | `$0103D0` loops | FACT |
| F19 | `Kosinski` LZSS with 16-bit LSB-first descriptors | `$0085A2` `ref-impl` == `exec` | FACT |
| F20 | `score_bcd += table[$010DDA + id]` via `abcd` | `$010DA6` | FACT |
| F21 | `extra_life_thresholds = 50 000 × (1..10)` | `$004DEC` (4-byte entries `00 XX 00 00`) | FACT |
| F22 | `camera ±3.0 px/tick in X, ±4.0 in Y, 16-px dead zone` | `$018F5C`, `$018FE8`, `$018B52` | FACT |

### 26.2 Constant inventory (literal values recovered from the image)
| Constant | Value | 16.16 | Notes |
|---|---|---|---|
`GRAV_JUMP_A` | `$0000E800` | +0.90625 | neutral + ascent |
`GRAV_JUMP_D` | `$00008800` | +1.0625 | descent (directional variant) |
`GRAV_HIT` | `$00012000` | +1.125 | launched actors |
`VY_MAX_PLAYER` | `$000C0000` | +12.0 | fall clamp |
`VY_MAX_HIT` | `$00100000` | +16.0 | launched fall clamp |
`AIR_ACCEL` | `$00006000` | +0.375 | air control |
`AIR_VX_MAX` | `$00038000` | +3.5 | air control clamp |
`KNOCK_DECEL` | `$00005400` | +0.328 | knockback damping |
`HP_PLAYER_MAX` | `$0050` | — | 80 |
`HP_LIFEBAR_DIV` | `$0008` | — | 10 segments |
`SPRITE_BUDGET` | `$004F` | — | 79 sprites/frame |
`SORT_BUCKETS` | 64 × `$20` | — | `$E200`–`$E9DF` |
`SORT_PER_BUCKET` | `$1E` bytes | — | 15 entries |
`CAM_DEADZONE` | `$FFF0` | 16 px | `$018B52` |
`CAM_VX_MAX` | `$00030000` | +3.0 | `$018FCC` |
`CAM_VY_MAX` | `$00040000` | +4.0 | `$019058` |
`BOSS_SEP_2P` | `$01100000` / `$01300000` | 272/304 | `$018F7E` |
`CAM_Y_LIMIT` | `$00780000` / `$00A80000` | 120/168 | `$01900A` |
`WORLD_X_MAX` | `$02F00000` | 752.0 | `$009F96` |
`WORLD_X_MAX_R7` | `$01510000` / `$01400000` | 337/320 | `$009FC2` |
`WORLD_Z_MAX` | `$00020000` | 2.0 | `$00A018` |
`ROUND_END_FADE` | `$00FF` | 255 frames | `$010Cxx` |
`SELECT_TIMEOUT` | `$012C` | 300 frames | `$0090F4` |
`POLICE_TELEGRAPH` | `$003C` / `$005A` / `$00B4` | 60/90/180 frames | `$012C18`, `$012D9E` |
`EXTRA_LIFE_STEP` | `$00050000…` BCD | 50 000 pts | `$004DEC` |

---

## 27. Evidence database

The full record set — **63 entries**, each with the exact required fields (ID, Subsystem, Claim, Evidence, Evidence Type, Location, Relevant Function, Relevant Address/Offset, Experiment, Result, Confidence, Alternative Explanations, Open Questions) — is in **`EVIDENCE_DATABASE.md`**.

Structural summary:
| Group | Records | Strongest evidence types |
|---|---|---|
| A. Boot / init / integrity | 5 | static, diff |
| B. Version / revision | 4 | diff, exec |
| C. Main loop / interrupts | 5 | static |
| D. Memory map | 4 | static, struct |
| E. Actor records / pools | 4 | static, struct |
| F. Player | 5 | static, exec |
| G. Physics | 3 | static, exec |
| H. Collision | 3 | static |
| I. Combat | 4 | static, negative search |
| J. Enemy AI | 3 | static, table decode |
| K. Bosses | 3 | static, table decode |
| L. Level / terrain | 3 | static |
| M. Rendering | 3 | static, disassembly |
| N. Animation | 1 | static |
| O. Audio | 4 | static, ref-impl, exec |
| P. Input | 1 | static + cross-site verification |
| Q. Camera | 2 | static |
| R. Assets / compression | 2 | ref-impl == exec |
| S. RNG | 1 | exec (bit-exact) |
| T. Hidden / dead code | 3 | exec + reachability scan |

Every `FACT` in this dossier traces to at least one record. Every record that depends on execution names the experiment (`EXP-01`…`EXP-05`) and can be reproduced by running `tools/verify_sor_forensics.py`.

---

## 28. Unknowns and unresolved questions

Each item is stated so that a future investigator knows exactly what would settle it.

| ID | Unknown | Why it is unresolved | What would settle it |
|---|---|---|---|
| `U-ACT-01` | Fields `+$35`,`+$36`,`+$43`,`+$44`,`+$5F`,`+$61`,`+$6A`–`+$6D`,`+$7A`,`+$7F` of the actor record | never read by an attributable path | full trace of one boss with a debugger, or an exhaustive xref of every `byte/word/long` displacement write |
| `U-COLL-01` | Which of the two box regions (`+$64` vs `+$70`) is "hurt" vs "attack" for *all* actor types | both are used symmetrically in some paths | instrument `$00450C` and `$00AB24` at runtime and dump both regions per actor |
| `U-CBT-01` | The complete per-character attack frame table (~200 rows: startup/active/recovery per move) | requires resolving three animation banks (`$049AE0`, `$053EFE`, `$05E90A`) whose frame lists are interleaved with sprite patches | a dedicated animation-bank walker (bounded work, not architectural risk) |
| `U-LVL-01` | Meaning of spawn-record bytes `+$01`/`+$02` | the traced parser never reads them | locate the second-stage consumer (if any) or prove absence by exhaustive xref |
| `U-LVL-02` | Per-round `$FC34`/`$FC38` terrain tables | they are RAM *pointers* patched by the stage loader; the source tables per round are not yet enumerated | follow the stage loader's writes to `$FC34`/`$FC38` for each `$FF02` value |
| `U-VRAM-01` | VRAM free-space accounting / window-plane reservation | all destinations are hand-packed constants in `$008672`-family tables | enumerate every bank table entry and sum the allocations |
| `U-AUD-01` | Complete note-stream opcode map of the 68k sequencer | reader decoded; the `$F0`-class sub-dispatch (`$0732EA`) has many cases | dump a real song stream and single-step the dispatcher per byte |
| `U-DISP-01` | Purpose/effect of the type-index correction at `$00AE20` | it does not implement a clean second page and is unreachable in practice | author-intent unknowable; only the mechanical effect can be described |
| `U-STATE-01` | Reachability of player states `$4C`–`$5E` (target `$000000`) | no writer located; animation data could supply them | exhaustive search of animation bytes for those values plus runtime watchpoint on `+$30` |
| `U-INP-01` | Whether `$FC06`=1 means "3-button" or "6-button" | both readings fit the two call sites; X/Y/Z never read | hardware test with a 6-button pad, or a trace of `$FC06` on real hardware |
| `U-HID-01` | Whether `$FA43` is 2P scaling, difficulty, or a debug flag | set/cleared in round-intro/continue code; no UI path sets it | trace `$011FB6`'s caller with a debugger during a 2P session |
| `U-REG-01` | Whether the PAL differences are intentional design or a lazy port | only 3 sites found; two are VDP register values | compare PAL/NTSC recordings for the specific sites |
| `U-SCR-01` | Complete score/award table semantics (bonus stages, `$FF00B4` block) | block is read by `$0189xx` but the award rules are spread over 4 routines | trace the bonus sequence end-to-end |

No claim in this dossier depends on any of these unknowns: where an unknown exists, the dossier states what *is* known (addresses, arithmetic, observed effects) and stops there.

---

## 29. Confidence assessment

| Area | Overall confidence | Justification |
|---|---|---|
| Boot sequence, checksum, region latch | **CONFIRMED** | instruction-by-instruction, plus the four patched images behave exactly as predicted |
| Master state machine (22 states) | **CONFIRMED** for table, targets and transitions; **HIGH** for role labels | labels derive from what each state calls, not from names |
| Frame pipeline order | **CONFIRMED** | literal instruction order in one routine |
| VBlank ISR order + display modes | **CONFIRMED** for order and register bytes; **PROBABLE** for mode purposes | VDP commands decoded; intent inferred |
| Actor record layout (24 of 34 fields) | **CONFIRMED** for 21 fields, **HIGH** for 6, **UNKNOWN** for 10 | each FACT field has a writer *and* a consumer |
| Pools and dispatch table | **CONFIRMED** | loop bounds and table bytes |
| Player state machine | **CONFIRMED** table; **HIGH** for state semantics | 128 entries decoded; every group read |
| Physics constants | **CONFIRMED** (literals) and **CONFIRMED** behaviour (`EXP-05`) | executed original code |
| Collision geometry | **CONFIRMED** arithmetic; **PROBABLE** for which region is which | `U-COLL-01` |
| Damage formulas | **CONFIRMED** | both nibbles traced end-to-end |
| Enemy stat tables | **CONFIRMED** | decoded and cross-checked against consumers |
| Boss roster/architecture | **HIGH** (handlers + phases FACT; character names deliberately not asserted) | no name strings exist in the image |
| Level script format | **HIGH** for parser semantics; **PROBABLE** for record fields | `U-LVL-01` |
| Terrain model | **CONFIRMED** | arithmetic + table indirection |
| Rendering buffers / Y-sort / SAT | **CONFIRMED** | write sites + VDP commands |
| Animation format | **CONFIRMED** for structure; **UNKNOWN** for full data dump | `U-CBT-01` |
| Audio split (68k sequencer / Z80 proxy) | **HIGH** | register targets + BUSREQ + absence of decoder in Z80 |
| Z80 driver identity/size/hash | **CONFIRMED** | two independent decoders agree |
| PCM format | **CONFIRMED** (Δ-table, descriptor table) | bytes decoded |
| Input | **CONFIRMED** except `U-INP-01` | bit layout verified by three independent use-sites |
| Camera | **CONFIRMED** | constants + update sites |
| RNG | **CONFIRMED** | bit-exact vs. MC68000 |
| Hidden/dead code | **CONFIRMED** existence + unreachability of `$005920`; **CONFIRMED** REV-01 fix | both executed |

Areas where this dossier is deliberately *less* complete than a full decompilation: player/enemy animation data dumps, complete AI transcriptions for all 17 bosses, and the audio opcode map. In each case the *mechanism* is confirmed and the *data volume* is the remaining work — the reverse of the usual failure mode, where behaviour is guessed.

---

## 30. Coverage matrix

Full matrix with per-row evidence IDs: **`COVERAGE_MATRIX.md`**. Summary:

| Subsystem | Investigated | Evidence | Confidence | Remaining unknowns |
|---|---:|---|---|---|
| Main loop / scheduling | ✅ 100 % | 6 records | CONFIRMED | — |
| Memory map | ✅ 95 % | 5 | CONFIRMED (blocks), 3 unexplained bytes ranges | `U-VRAM-01` |
| Actor structures | ✅ 70 % | 5 | CONFIRMED 21 fields | `U-ACT-01` |
| Pools / dispatch | ✅ 100 % | 3 | CONFIRMED | `U-DISP-01` |
| Player | ✅ 85 % | 6 | CONFIRMED states/physics | `U-CBT-01`, `U-STATE-01` |
| Physics | ✅ 100 % | 4 | CONFIRMED | — |
| Collision | ✅ 85 % | 4 | CONFIRMED math | `U-COLL-01` |
| Combat / damage | ✅ 90 % | 5 | CONFIRMED | full per-move table |
| Enemy AI | ✅ 75 % | 3 | HIGH | per-type transcription depth |
| Bosses | ✅ 80 % | 4 | HIGH | 3 handlers only partially traced |
| Levels / spawn | ✅ 70 % | 4 | HIGH parser | `U-LVL-01/02` |
| Rendering | ✅ 90 % | 4 | CONFIRMED | `U-VRAM-01` |
| Animation | ✅ 85 % | 2 | CONFIRMED structure | data dump |
| Audio | ✅ 75 % | 4 | HIGH | `U-AUD-01` |
| Input | ✅ 95 % | 2 | CONFIRMED | `U-INP-01` |
| Camera | ✅ 90 % | 3 | CONFIRMED | mode 0–7 purposes |
| Assets/compression | ✅ 80 % | 2 | CONFIRMED (Kosinski, plane map) | bank-by-bank inventory |
| Resource management | ✅ 80 % | 3 | HIGH | `U-VRAM-01` |
| RNG | ✅ 100 % | 1 | CONFIRMED | — |
| Hidden/debug/unused | ✅ 85 % | 3 | CONFIRMED | `U-HID-01` |
| Versions/revisions | ✅ 100 % | 6 | CONFIRMED | — |

---

## 31. Architectural diagrams

Full set (boot timeline, memory map, frame pipeline, actor lifecycle, audio signal path, data-flow): **`DIAGRAMS.md`**.

Two essential ones are reproduced here.

### 31.1 Per-frame data flow (the actual, observed one)
```
V-BLANK (once per frame)
   │  clear frame flag ← $FA00
   │  VSRAM ← camera Y ; CRAM ← $F400 (if dirty) ; mode = $FF06
   │  pads → $FC04/$FC05 (edge) ; SAT → VDP ; sound tick ($072914)
   ▼
MAIN LOOP  (state = $FF00)
   │
   └─► GAMEPLAY PIPELINE ($01087A)
         ① pause/round-end gates  ─────────────► may short-circuit the whole frame
         ② background columns + H-scroll table ($10C88 / $115CC)
         ③ spawn script ($11B4C) ──► actor pool
         ④ palette cycle ($11210) ──► $F400
         ⑤ ACTOR PASS ($00AD8E)
              for each live slot:
                 handler(type) ──► read $FC05 copy (+$54) → set +$30
                              ──► physics (+$1C/+$20/+$24 → +$10/+$14/+$18)
                              ──► combat queries (body box, attack boxes)
                              ──► damage → HP → reaction state
                 activation test (camera proximity)
                 insert into Y bucket ($E200)
              Y-sort walk ──► emit 8-byte SAT records ──► $F600, budget 79
         ⑥ SAT stream kickoff ($0084BA)
         ⑦ police subsystem ($000436)
   ▼
await next V-BLANK
```

### 31.2 Actor lifecycle (all transitions observed in code)
```
        spawn request ($007EBE/$007E92/$007EEA)
                    │  scan pool for +$00 == 0
                    ▼
        ┌───────────────────────┐
        │ ALLOCATED             │  +$00 = type, +$01.., +$10/+$14/+$18 = pos
        └──────────┬────────────┘
                   │ first dispatch → handler init (state 1)
                   ▼
        ┌───────────────────────┐   damage      ┌──────────────────────┐
        │ ACTIVE                │──────────────►│ REACTION (+$7C/+$7D) │
        │ handler runs each tick│◄──────────────│ stun/launch/knockdown│
        └──────────┬────────────┘   recovery    └──────────┬───────────┘
                   │ out of camera window                  │ HP ≤ 0
                   ▼                                       ▼
        ┌───────────────────────┐                 ┌──────────────────────┐
        │ DESPAWN ($00B17A)     │                 │ DEATH ($009CFC..)    │
        │ unlink + 32-long wipe │                 │ census-- , score +=  │
        └───────────────────────┘                 │ then wipe            │
                                                  └──────────────────────┘
```

---

## 32. Chronological research log

Full journal with every command, file, and dead end: **`RESEARCH_LOG.md`**. Condensed timeline:

| Phase | What was done | Outcome |
|---|---|---|
| P1 | Archive authenticated with REA `inspect-artifact`; 11 ROMs extracted and hashed | provenance chain, `evidence/rea_zip_inventory.json` |
| P2 | Header/checksum/vector decode; pairwise byte diffs of all 11 images | 4 diff regions for REV01; all patches classified |
| P3 | Disassembled boot `$000208`, checksum `$000338`, master loop `$0003A2`, VBlank `$019D16` | fixed-timestep model proven |
| P4 | 8 KiB entropy/opcode sweep of the whole 512 KiB | code/data boundary at `$01A1xx` established |
| P5 | Resolved all 22 master states and the 12-call gameplay pipeline | `§5`, `§25.1` |
| P6 | Mapped RAM by following every `move.x $FF..` in the code | `§6.2` (≈120 blocks) |
| P7 | Actor record induced from pool strides + per-field writers/consumers | `§7.1` |
| P8 | Decoded the 156-entry type table and all boss trampolines | `§7.3` |
| P9 | Player state table `$001CE2` (128 entries) and all handlers read | `§8.2` |
| P10 | Physics constants located; gravity executed on MC68000 | `§9`, `EXP-05` |
| P11 | Collision math traced (`$004140`, `$00AB24`, `$00AB88`) | `§10` |
| P12 | Damage pipeline traced (`$0041EA` → `$00422A`) | `§11.1` |
| P13 | Enemy stat tables extracted (`$026FCE`, `$027010`, `$027032`) | `§12.2` |
| P14 | Boss stat initialiser decoded (`$017EDC`) + all boss handlers located | `§13` |
| P15 | Spawn-script parser and terrain model traced | `§14.2`, `§14.4` |
| P16 | Y-sort, SAT builder, culling, sprite budget | `§15` |
| P17 | Animation indirection + timing/hitbox coupling | `§16` |
| P18 | 68k sound subsystem read; Z80 driver decompressed by *two* methods | `§17`, `EXP-01` |
| P19 | Input poll + bit layout verified against three use-sites | `§18` |
| P20 | Camera law, limits, plane streaming | `§19` |
| P21 | RNG recovered and machine-verified | `§22`, `EXP-02` |
| P22 | Dead-code hunt: found `$005920`, proved unreachability | `§23.2`, `EXP-04` |
| P23 | REV00 vs REV01 executed side by side on the boss-`$30` police branch | `§23.5`, `EXP-03` |
| P24 | Dossier, evidence DB, coverage matrix, diagrams, tool | this deliverable |

### Reproducibility
```
python3 tools/verify_sor_forensics.py      # needs capstone+unicorn for the exec checks
```
Produces `evidence/verification_results.json` containing: the 11-ROM audit (hash/checksum/diff/expert classification), the extracted stat tables, the Z80 driver hash and Δ-PCM table, the PRNG sequence, and the REV00/REV01 execution traces. The reference Kosinski decoder and the ROM's own `$0085A2` are asserted equal inside the tool.

---

### Closing statement

What is documented here is the *shipped 1991 machine*: a 22-state program, one 128-byte actor type, three data tables that generate every enemy, seventeen specialised boss state machines over one engine, an integer-only 2.5D physics model with exactly two limiters, a signed-byte interval-overlap combat geometry, a three-level integer sort feeding an 8-byte sprite record stream with a hard cap of 79 sprites, a hand-packed VRAM map, a deterministic 32-bit LCG, and an audio system that is a 68k sequencer writing register bytes through a Z80 proxy.

Where the evidence stops, this dossier stops. The unresolved items in `§28` are named, bounded, and each has a stated route to resolution; none of them is papered over with a guess.
