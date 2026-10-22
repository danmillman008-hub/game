# Chronological Research Log
### Streets of Rage / Bare Knuckle (Mega Drive, 1991) — forensic RE journal

Format: `RL-nn` — tool/action → observation → decision.
Every entry is reproducible; commands are given where they matter.

---

## Phase 0 — Groundwork

**RL-01** *Environment / repo.* Inspected `/home/user/game`: a single 4,110,629-byte ZIP (`Streets-of-Rage_Genesis_EN.zip`, SHA-256 `f1c25bde…a17645`) on branch `arena/eb3b2453-game`.
→ Decision: never commit the extracted ROMs (5.5 MB of duplicates); read them from the ZIP in memory in every tool.

**RL-02** *Tooling survey.* System Python has no `capstone`/`unicorn`. Created `/tmp/re_venv` with `capstone` (M68K only — **no Z80 backend**) and `unicorn` (has `UC_ARCH_M68K`).
→ Consequence: a Z80 disassembler must be hand-written if Z80 code needs disassembly beyond byte-level reasoning. In the end the Z80 analysis was done by byte-level decoding plus the 68k side, so no full Z80 disassembler was required. Recorded as a known limitation.

**RL-03** *Ghidra attempt.* `gh release download` for Ghidra/Temurin fails: the redirect to `release-assets.githubusercontent.com` closes with `EOF` under the container's proxy.
→ Dead end. Abandoned; Capstone + Unicorn proved sufficient. Do not retry.

**RL-04** *REA (`morluto/rea`) integration.* Cloned to `/tmp/rea`, read `README.md`, `AGENTS.md`, `SKILL.md`, `docs/raw-binary.md`, `docs/cli.md`. Installed `rea-agents` 6.7.0. Ran `rea inspect-artifact` and `rea inventory-artifact` on the ZIP.
→ Evidence IDs recorded: `ev_4899ae28…9f627` (inspect), `ev_ff529169…808a2` (inventory); manifest `agm_56ebee8d…e15`. Output preserved as `evidence/rea_zip_inventory.json`.
→ Adopted REA's `observed / derived / inference / unknown` discipline as the confidence taxonomy in `DOSSIER §0.2`. REA's own `m68k` lane needs a local Ghidra, which is unavailable here (RL-03), so only its artefact/ledger layer was used.

---

## Phase 1 — Archive and version forensics

**RL-05** *Header decode, all 11 images.* Parsed `$0100`–`$01FF`: console, copyright, domestic/overseas name, serial, checksum, I/O, ROM/RAM size, region.
→ Two originals: `MK 00001019-00` (1991.MAY, `$9409`) and `-01` (1992.FEB, `$6390`). Nine derivatives.

**RL-06** *Checksum algorithm recovery.* Read `$000338`–`$000350` and re-implemented the sum in Python.
→ `[p1]` has a **correct** checksum for its own patched content (`$F41C`), but its `$0336` also bypasses verification; `[p2]` is invalid (`$9409` vs `$134A`) and survives only via the NOP at `$0348`. This changed how derivatives are classified: they are not "bad dumps", they are *patched* dumps.

**RL-07** *Pairwise diffs.* Byte diff of every image against REV00 and REV01.
→ REV01 differs in exactly 4 regions; the third (`$0143FB`–`$014D61`) is a **+6-byte insertion**, proven by re-aligning at `+6` and finding only one remaining divergence (`$014D7E`).

**RL-08** *Structural sweep.* 8 KiB block statistics (entropy, `RTS`/`JSR`/`BSR` counts, ASCII density, `$00`/`$FF` density) over the whole image.
→ Code ends at `$01A1xx`; `$01C000`–`$071FFF` is compressed graphics (entropy 7.4–7.95, zero code opcodes); sound code reappears `$072000`–`$073FFF`. This one measurement scoped the entire rest of the project.

**RL-09** *Translation images as conformation maps.* Diffed `[T+Fre]` and the Spanish packs against REV00.
→ Edits cluster on text and use `$01`–`$1A` for A–Z, independently confirming the alphabet encoding later needed to decode the dormant cheat (RL-25).

---

## Phase 2 — Program skeleton

**RL-10** *Boot disassembly.* `$000208`–`$000307`.
→ Sega ICD_BLK4-style: TMSS, 24 VDP registers from `$0002A4`, RAM/CRAM/VSRAM clear, PSG mute, `bra $000308`.

**RL-11** *Checksum gate + init.* `$000308`–`$000435`.
→ Region latch to `$FF44`; checksum branch `$0348`; failure path `$000412` (red CRAM, halt).

**RL-12** *Master loop.* `$0003A2`–`$0003B8` + table `$0003BA`.
→ 22 entries; `$FF00` is a **byte offset**, transitions are `addq/subq #2`. Then `jsr $010502` = frame sync.

**RL-13** *Frame sync semantics.* `$010502` / `$010514`.
→ Busy-wait on `$FA00`; `$010514` is a second variant. Later (RL-19) it turned out `$010514` is used *inside* the actor pass — a double frame.

**RL-14** *V-Blank ISR.* `$019D16`–`$01A0B2`.
→ Order: VSRAM → CRAM DMA → mode dispatch (`$FF06`) → `$FB06`/`$FB08` → pad read → SAT DMA → sound tick → `rte`. Lag-frame branch at `$01A088`.

**RL-15** *Master state census.* Disassembled all 22 state routines.
→ Labelled boot, attract, character select, round load, gameplay, round clear, continue, name entry, ending, full reset, round transition (§25.1). Noticed the repeated "VDP latch + `$007FB8` + block clear + `addq.w #2,$FF00`" idiom — the engine's only teardown.

---

## Phase 3 — Data structures

**RL-16** *RAM mapping by xref.* Scripted sweep of every `$FF..`/`$FE..` short operand, grouped by address, then read each consumer.
→ ~120 blocks catalogued (§6.2). Highlights: `$E200` Y-sort table, `$F400` CRAM shadow, `$F600` SAT shadow, `$FA00` frame handshake, `$FC14` spawn-script PC.

**RL-17** *Actor record induction.* Started from the `$80` stride in `$00AD8E` and `$00B236`, then for each candidate offset searched for a writer and a consumer.
→ 24 fields nailed down, 10 left unknown rather than guessed. Two corrections happened here: `+$14`/`+$18` are 32-bit 16.16 values (not words), and `+$20` is the **depth** velocity while `+$24` is the vertical velocity (integration at `$004448`–`$00445C` settled it).

**RL-18** *Dispatch table.* Decoded all 156 entries of `$00B236`, followed the `jmp` trampolines at `$00B36A`.
→ Complete type map (§7.3). Found the `$00AE20` index correction and recorded it as an ambiguity instead of forcing an interpretation.

**RL-19** *Actor pass anatomy.* Read `$00AD8E`–`$00AF34`.
→ Two player slots then 66 general slots; activation test; bucket insertion; then the `$E9E0`→`$E200` walk with an insertion sort on depth + priority bit.

---

## Phase 4 — Player and physics

**RL-20** *Player entry.* `$001C44`–`$001CE0`.
→ Pre-emption chain (police → special → hit → state) then `jsr $00B186` dispatch. Also found the 4-byte `$FB56` snapshot cursor.

**RL-21** *Player state table.* Dumped 128 entries of `$001CE2`; read every target.
→ Grouped into idle/walk/jump/land/attack/jump-kick/special/pickup/weapon/throw/grab/hit/death/police (§8.2). Found 13 slots → `$000000`.

**RL-22** *Physics constants.* Located `$003886`, `$00389A`, `$0038AE`, `$0038C0`.
→ Gravity `$E800`/`$8800`, clamp `$C0000`, air control `±$6000` clamped `±$38000`.

**RL-23** *First Unicorn attempt failed.* Executing `$0085A2` raised `UC_ERR_EXCEPTION` and then a storm of `UC_HOOK_INTR` events at `$85AE`.
→ Root cause: Unicorn defaults to a 68020-class core where `dbra` with a word counter and `move.w sr` semantics differ. Fixed with `ctl_set_cpu_model(UC_CPU_M68K_M68000)`. **This is a reusable lesson: always pin the CPU model.**

**RL-24** *Jump trajectory experiment (`EXP-05`).* Executed `$00389A` and `$0038AE` plus the `$003886` clamp against three launch velocities, integrating `+$24` into a scratch Y.
→ Neutral: 18/20/22 ticks, apex 34.9/44.2/54.7 px. Directional: 20/23/25 ticks, **same apex**. This measured the "floatier forward jump" property directly instead of inferring it.

---

## Phase 5 — Collision and combat

**RL-25** *Box builder.* `$004140`–`$0041E8`.
→ Two ROM tables: `$01ABA8` (5-byte records) and `$01AB8E` (2-byte records); six words written to `+$64`. Established the arithmetic (`idx*5`, `byte*2`).

**RL-26** *Box tests.* `$00AB24`, `$00AB88`, `$00AC78`, `$00ACA6`, `$00450C`.
→ All are interval-overlap predicates with signed byte offsets; Z is doubled before comparison. Region roles left as `U-COLL-01` because both regions appear on both sides in different paths.

**RL-27** *Damage decoder.* `$0041EA`–`$00423A`.
→ Damage = low nibble indexed by (anim block, character, frame); high nibble = reaction class. `$FA43` rewrites as `3*lo+hi`.

**RL-28** *HP path.* `$009BCC`/`$004E6C`.
→ Shared subtraction; player max 80; 10-segment lifebar = HP/8.

**RL-29** *Hit-stop hunt (negative).* Searched for a global freeze counter written from damage paths, and for any delta-time multiply.
→ None. Recorded explicitly as `EV-CBT-04` so future readers do not "add" a mechanic that is not there.

---

## Phase 6 — Enemies and bosses

**RL-30** *Call census.* Automated JSR/JSR-PC target counting over `$00D600`–`$017800`.
→ Revealed the shared AI core (`$0096C0` 50×, `$009604` 25×, `$0096EC` 21×) — i.e. enemies are data over nine routines, not per-type code blobs.

**RL-31** *Stat tables.* `$026FCE`, `$027010`, `$027032`.
→ HP/ATK per difficulty palette, score IDs, animation pointers (§12.2). Discovered `$28` = 1 HP heavyweight (a script variant).

**RL-32** *Boss stat initialiser.* `$017EDC`.
→ 4-way difficulty switch + round-7 bonus + flat +2 attack; tables at `$017F26`/`$017F2A`. First extraction attempt mis-read the tables as words and produced absurd HP values (28672); corrected by reading the byte loads in the code.

**RL-33** *Boss handlers.* Read `$012B5C`, `$012F14`, `$012FB4`, `$01306A`, `$0140DC`, `$014266`, `$014318`, `$0143D0`, `$015794`, `$0158C4`, `$015E70`, `$016CE4`, `$0174E0`, `$017262`, `$017858`, `$016C24`, `$016C60`.
→ 17 specialised state machines; Mr. X = two escorts + `$FA78` handshake; `$55`–`$58` share the `$016A1A`/`$016AEC` core.

**RL-34** *Deliberate restraint.* No boss character names exist in the image. Rather than import community names as fact, bosses are labelled by type ID + observed behaviour + round.

---

## Phase 7 — Level, rendering, audio

**RL-35** *Spawn parser.* `$000700`–`$000D5x`.
→ Compacting retry-tolerant script: group header word, 6-byte records, `$99` terminator, difficulty bits, `bit7` spawn flag, rewind on failure.

**RL-36** *Terrain.* `$00AD2A`.
→ `$FFA000` plane, two nibbles per byte, 16 px × 8 px cells, height from `$FC34`, threshold from `$FC38`.

**RL-37** *Rendering.* `$00AE4C`, `$00AEC4`, `$00AF46`–`$00B120`, `$0084BA`, `$008510`.
→ Y buckets, depth insertion sort, 8-byte SAT records, 79-sprite cap, chunked SAT DMA from `$F600`.

**RL-38** *VDP mode decode.* Decoded every VDP longword in the ISR.
→ `$73400081` = VRAM `$3340` (plane A H-scroll); `$70000083` = VRAM `$3000`; plane bases `$C000`/`$E000` from the `cmpa.w #$e000` test in the name-table writer. Corrected an earlier assumption that mode 5 was a raster effect — it is a plane-B scroll-table mode.

**RL-39** *Audio read.* `$072914` tick, `$072D08` command, `$073066` step, `$072E74` channel-pointer table, `$07288C` song table.
→ Found `$A01FFF` register writes under BUSREQ ⇒ the 68k is the sequencer. This contradicts the usual assumption for Mega Drive sound and is recorded as `EV-AUD-01` at HIGH CONFIDENCE.

**RL-40** *Z80 decompression (`EXP-01`).* Ran the ROM's `$0085A2` on `$0795A2` under MC68000; wrote an independent Python decoder.
→ Both produce 7,936 bytes, SHA-256 `07cabd01…88fd2`. Read the Z80 entry, the Δ-PCM table at `$001E`, and the 17 descriptors at `$019B`.

---

## Phase 8 — Hidden systems and revisions

**RL-41** *Dead-code hunt.* Scanned for routines with no inbound references.
→ `$005920` has none. Decoded its tables: `MOM / SUN / UDI / BO / ORE / blank` → 90/49/9/7/1/0 lives and 6/5/4/3/2/1 police calls.

**RL-42** *Cheat verification (`EXP-04`).* Executed `$005920` with all six codes plus a control, `$FF0C` encoded as 1-based letters.
→ Exactly the table's values; control untouched. Confirms the code is functional *and* that the encoding is 1-based.

**RL-43** *Reachability proof (negative).* Four-encoding scan for any reference to `$005920`.
→ Zero. Classified as dead code, with both plausible historical explanations recorded (`EV-DEAD-01/02`).

**RL-44** *REV difference experiment (`EXP-03`).* First attempt used the wrong precondition (player inactive), so both revisions returned early at `$0143F0` and the test was inconclusive. Re-ran with `$FFFFB800 = 1` and the correct continuation addresses (`$014458` / `$01445E`).
→ REV00: early `rts`, `+$67 = 1`, death frozen. REV01: falls through to the normal death path. This is the reason REV01 exists.

**RL-45** *PRNG recovery (`EXP-02`).* Read `$0104D8`, derived the closed form, then executed 16 calls on MC68000.
→ 16/16 identical, including the full 32-bit state after each call.

---

## Phase 9 — Deliverables

**RL-46** *Tool consolidation.* Wrote `tools/verify_sor_forensics.py`: archive audit (11 images), table extraction, Kosinski reference decoder, and the five Unicorn experiments with assertions (`ref-impl == exec` for the decompressor).
→ One command reproduces every executed claim in the dossier.

**RL-47** *Self-correction pass.* Two errors were found and fixed during documentation rather than left in place:
1. `+$20`/`+$24` were initially labelled vertical-velocity and gravity-accumulator; integration order proved `+$20` is depth velocity.
2. The `$00B236` high-page claim ("types `$90`–`$95` jump outside ROM") was overstated; the `bset.b #$10` correction does not implement a second page, so the mapping is recorded as `U-DISP-01` instead of a conclusion.

**RL-48** *Documentation.* Wrote `DOSSIER.md` (32 sections), `EVIDENCE_DATABASE.md` (63 records), `COVERAGE_MATRIX.md`, `DIAGRAMS.md`, `RESEARCH_LOG.md`, `README.md`.

---

## Dead ends (do not repeat)
| Attempt | Why it failed | Replacement |
|---|---|---|
| Download Ghidra/Temurin from GitHub Releases | proxy closes the redirect (`EOF`) | Capstone + Unicorn + custom decoders |
| Use REA's `m68k` raw-binary lane | needs a local Ghidra + Java | used REA only for artefact provenance |
| Default Unicorn CPU model | 68020 semantics break `dbra`/`sr` idioms | `ctl_set_cpu_model(UC_CPU_M68K_M68000)` |
| Execute `$005920` with ASCII `"MOM"` | encoding is 1-based A=1, not ASCII | encode as `00 0D 0F 0D` |
| Test the boss-police branch with no active player | both revisions exit at `$0143F0` | set `$FFFFB800 = 1` |
| Read `$017F26`/`$017F2A` as words | produced impossible HP (28672) | read the byte loads in `$017EDC` |
| Treat `$000512` word writes to `+$30` as state values | `+$30` is a byte; the word also clears `+$31` | byte state + separate flag byte |
| Expect a Z80 sequencer | Z80 image has no stream decoder on its executed path | 68k sequencer + Z80 register proxy |

---

# Stage 2 — From dossier to executable knowledge

**RL-49** *Audit of the Stage-1 tool.* Read `tools/verify_sor_forensics.py` line by line
instead of trusting its exit code. It implements **three** Unicorn experiments
(EXP-01, 02, 03), not five: the name-entry cheat and jump-trajectory experiments
described in `README.md`, `COVERAGE_MATRIX.md` and `RESEARCH_LOG` **RL-46** have no code
behind them. EXP-02 and EXP-03 also record results without asserting anything; only the
Kosinski hash is asserted. → Correction recorded in `AUDIT_REPORT.md §2`; the missing
experiments were re-implemented against the ROM rather than deleted from the record.
This entry deliberately does **not** rewrite RL-46; it records that RL-46 overstated the
tool.

**RL-50** *Slice selection.* Candidates: movement/coordinates, body collision, attack
resolution, damage, AI. Chose movement + body collision because the routines are
self-contained, the record fields were already located, and the outputs are integers
(no rendering/audio dependencies). Attack resolution was rejected for now: `$00AB24`
reads six-byte threshold records at `+$72` whose fields are not understood; implementing
them would require guessing.

**RL-51** *Toolchain re-established.* `/tmp` does not survive between sessions here, so
the venv and scratch ROMs had to be rebuilt; moved all scratch work to the gitignored
`work/` directory inside the repository. Reinstalled capstone 5.0.7 / unicorn 2.1.4.

**RL-52** *Read the skeleton instead of the summary.* Disassembled `$001C44`. It matches
`DOSSIER §8.1` byte-for-byte (calls are `jsr d16(pc)`, not absolute). This confirmed the
Stage-1 skeleton and, more importantly, fixed the **frame order** used later: gravity
happens inside the state dispatch, clamp at `$001CA2`, integration at `$001CA6`, box
rebuild at `$001CC6`.

**RL-53** *An xref tool that lied.* First call-graph scan found **zero** references to
every physics routine because it only matched absolute `jsr`. The engine uses
`jsr d16(pc)` (`4EBA`). After adding PC-relative forms, the callers appeared:
`$00389A` ← `$001FDC`, `$002128`, `$002174`, `$002A10`, `$002ADC`, `$002B10`, `$002B38`;
`$0038AE` ← `$002006`, `$0020E4`, `$00219C`, `$0024BE`, `$002AA0`; `$0038A6` ← `$002A6E`
only. → Lesson: a negative xref result is only as good as the encodings you searched.

**RL-54** *A gravity constant the dossier never listed.* `$0038A6` adds `$3800`
(+0.21875 px/tick²) and is reached from exactly one site (`$002A6E`). Added to the spec
as the "soft" variant. → Shows the value of re-reading code rather than re-reading notes.

**RL-55** *The box builder does not match the dossier.* Read `$004140` and saw that
`$41AC`/`$41E2`/`$41C6` add the second table byte to the value already in `d0`, i.e.
`x2 = x1 + extent`, not `X + offset`. Executed the routine to settle it: index 2 at
X=1000 gives `x2 = 1007`, not `1010`. Also discovered a **second** box being written at
`+$70` because `a1` is never reset between the two passes. → `AUDIT_REPORT.md` C-1, C-2.

**RL-56** *Two of my own bugs, caught by the tests.* (a) I masked `0x0200` for `+$09`
bit1 — wrong by 8 bits, since `+$09` is the low byte of the `+$08` word. (b) I keyed the
freeze predicate on `+$30` (state) although the ROM reads `+$08` (animation offset);
after fixing that, `+$08 = 0x0114` still froze because `andi.b #$FC` masks only the low
byte and `cmpi.w` compares 16 bits. → Both became regression tests (D3, D4).

**RL-57** *The oracle was wrong twice.* (a) `cmpa.w #$b800` sign-extends to
`$FFFFB800`; probing with `a0 = $00FFB800` silently takes the other branch, making the
P1 special case look like a general case. (b) Mapping `0x00FF0000` and `0xFFFF0000` as
two Unicorn regions creates two *distinct* memories; the 68000 accesses the same byte
through both, so all short-absolute reads returned zeros. Fixed with `mem_map_ptr` onto
one host buffer. → Recorded in `REPRODUCE.md §6`; without this the differential suite
would have "confirmed" nonsense.

**RL-58** *Writing to ROM by accident.* The cheat probe wrote the name bytes to
`0x00FF0C`, which is ROM offset 65,292, not RAM `$FF0C`. The correct 32-bit form of the
sign-extended short absolute is `0x00FFFF0C`. The routine then returned sentinels and the
test failed loudly — a benign outcome of a dangerous mistake (Unicorn maps ROM writable).
→ `REPRODUCE.md §6.3`, `DIFFERENTIAL_VALIDATION.md` §4.2 #9.

**RL-59** *Discovered `$FC06` (resolves U-INP-01).* `$00813C` writes 0 then 1 depending on
whether the two controller reads differ: the three-/six-button discriminator.
**HIGH** confidence, static only.

**RL-60** *The jump table in the dossier is wrong.* Ran the ROM chain per frame for three
launch speeds × two gravity variants. Real airtimes are 15/17, 17/20, 19/22 ticks with
apex −27.375/−35.719/−45.156 px; the dossier printed 18/20/22, 20/23/25 and
34.875/44.219/54.656 px. The dossier's numbers are exactly the `integrate → gravity`
ordering (`v²/2g + v/2`); the ROM does `gravity → integrate`. The *qualitative* claim
(same apex, longer airtime when directional) survives. → `AUDIT_REPORT.md` C-7,
`DIFFERENTIAL_VALIDATION.md` §4.4.

**RL-61** *Cheat table reproduced.* Executed `$005920` with all six codes plus a control,
for both players. Every value matches `DOSSIER §23.2`, including the `$B800`-dependent
choice of `$FF20` vs `$FF23`. The Stage-1 table was right; the Stage-1 *tool* simply
never ran it.

**RL-62** *Revision check before claiming anything.* Diffed every byte range used by the
slice between REV 00 and REV 01: 8/8 ranges identical. The 2,092 differing bytes are the
master header plus `$0143FB–$014DAF` (the known boss-handler patch). → The slice is
revision-independent, and that is now a measured statement rather than an assumption.

**RL-63** *Spec tests failed for the right reason.* Four projection expectations were
wrong because I forgot the `+$80` bias when choosing "outside the margin" positions
(X=−200 maps to −72, inside −896). Fixed the *tests*, not the implementation — the
distinction matters and is recorded in `DIFFERENTIAL_VALIDATION.md §4.3`.

**RL-64** *Why the slice is not the game.* Wrote `COMPLETION_REPORT.md §5` to state the
scope explicitly: one actor class, one code path, no state machine, no combat. The
method is proven for self-contained routines; whether it scales to frame-wide systems is
the next experiment.

## Additional dead ends (Stage 2)

| Attempt | Why it failed | Replacement |
|---|---|---|
| Absolute-only xref scan | engine calls are `jsr d16(pc)`; found 0 callers | match `4EBA`/`4EFA`/`61xx`/`lea d16(pc)` |
| Two independent Unicorn RAM mappings | not aliases; short-absolute reads saw zeros | `mem_map_ptr` on one buffer |
| `a0 = 0x00FFB800` for the P1 box test | `cmpa.w` compares against `$FFFFB800` | use the sign-extended address |
| Writing `$FF0C` as `0x00FF0C` | that is ROM, not RAM | `0x00FFFF0C` |
| `Actor(vy=0x80000000)` | Python int, not signed 32-bit | wrap in `__post_init__` |
| Trusting `DOSSIER §10.1` box formulas | extents were read as offsets | execute `$004140` and compare |

## Stage 3 — a playable prototype on top of the slice

**RL-65** *Scope decision, recorded before the work.* The user authorised a *small* playable
prototype that demonstrably reuses `components/sor_engine`. The prohibition on reproducing or
porting the original game is unchanged. Therefore *Neon Alley* (`prototype/`) is a new game:
original characters, arena, art, enemy AI, attack frame data and health. Its only link to the
original is that its movement, collision and drawing go through the verified modules.

**RL-66** *Evidence separation, stated up front.* Three categories are kept apart and labelled
in `prototype/RULES.md`: `[ROM]` (differential-verified behaviour, consumed from `components/`),
`[INTEG]` (how this game wires those pieces), `[PROTO]` (new rules). No prototype rule was
added to `BEHAVIORAL_SPECIFICATIONS/`, and no evidence file was edited. The Stage-2 open
question `U-CBT-01` (hit-reaction rules) is precisely why every hitstun/knockback/armour
number here is `[PROTO]`.

**RL-67** *The cull window forced the canvas, not the other way round.* The first render used a
960×540 canvas and the player was invisible: `$00AF46` culls at `sx ≥ $500` (320) and
`sy ≥ $200`, so the verified routine was doing exactly what it was validated to do. The fix
was to render a 384×240 virtual canvas and scale it up, and to re-derive the camera anchor so
the playable band lands inside `sx ≈ 176…336`. Editing `projection.py` would have been a
re-baseline of verified behaviour — rejected.

**RL-68** *Measured stun-lock, fixed as a prototype rule.* The first autopilot run reached
VICTORY at frame 791 with 80/80 health: every player hit cancelled the enemy's startup, so the
encounter was decided by attack speed alone. Giving the enemy swing armour through its own
startup/active frames (damage still lands) produced lost health on the recorded run and a real
DEFEAT path with no input (frame 1,025). This is a gameplay decision, not a claim about the
original's hit reactions.

**RL-69** *Reuse proved by patching, not by assertion.* `prototype/tests/test_components.py`
monkey-patches `kinematics.integrate` and `projection.project` and fails if the game keeps
working regardless. A frozen actor (real `$00442C` freeze state) is shown to stop integrating
and to not be read as landing. `soft_gravity` is implemented and verified but genuinely unused
by this game; it is reported as unused rather than routed through artificially.

**RL-70** *Regression guard.* After all prototype work: `tools/verify_stage2.py` → 37 passed,
7,740 comparisons, ROM `dd44f120…95c0`; `tools/verify_sor_forensics.py` → 11 ROMs. Baseline
unchanged, so the prototype did not disturb the evidence layer.

**RL-71** *The browser build is a port, and it is proved to be one.* Requested after Stage 3:
an HTML file that opens and plays. Python cannot run in a browser without shipping a runtime
and a server, so `prototype/web/neon_alley.js` re-implements the engine arithmetic and the game
1:1. Rather than ask for trust, `prototype/tools/web_conformance.py` replays recorded (875
frames), passive (1,025) and synthetic (1,840) input through both engines and diffs every field
of every frame with **no tolerance** — all three match exactly. A deliberate one-constant defect
(`$E800 → $E900`) is caught at frame 300, so the harness is known to bite. The shipped page is
additionally executed in a stub DOM (`prototype/web/page_smoke.js`): ENTER, walk 300→432,
punch, jump, victory in 722 frames at 56 HP, restart. Caveat recorded honestly: there is no
real browser in this environment, so the page is verified functionally and its drawing calls
are exercised, not eyeballed; the pixel canvas is the same 384×240 and scales by integers, so
no resampling loss is introduced.

**RL-72** *Graphics decompressor cracked, and proved byte-exact against the real game.* The
routine at `$008192` was re-read from the ROM and reimplemented in `tools/sor_gfx_format.py`
(pure Python, no emulator). Format: header word → `tiles = header & $1FFF`, output is
`tiles × 32` bytes; a Huffman-style prefix table built exactly like `$8280` (record `A` starts a
value group, `B` gives length/count, `$FF` terminates, entries are written into
`1 << (8 - length)` slots); then a bit stream of (value, count) nibble runs, with an escape for
8-bit prefixes `>= $FC` that carries 3 bits of count and 4 bits of value. Header bit 15 selects
a second variant: the output handler at `$825E`/`$8274` **XOR-chains each 32-bit long with the
previous one**, starting from zero.

Verification is not a judgement call. `tools/md_capture/` builds a headless Genesis Plus GX
with two observation-only hooks (VDP data-port sink + instruction hook), runs the unmodified
ROM, and records every call to `$008192` with its exact output. Over a 1600-frame scripted run
the game performs 11 decompressions covering 10 distinct sources; **all 11 reproduce
byte-for-byte** (`tools/validate_gfx.py` → `evidence/gfx_decoder_validation.json`). The harness
was rebuilt from a clean download to confirm those numbers do not depend on a stale build.

Pixel format settled independently of that: Mega Drive 4bpp tiles are 32 bytes, 4 bytes per
row, two pixels per byte, high nibble leftmost. The earlier "planar" reading produced a mean
neighbour difference of 3.18 on real data versus 1.15 for the packed reading, and the packed
reading renders the SEGA logotype from `$0722A2` recognisably. `tools/gfx_render.py` keeps both
so the comparison is reproducible.

Asset discovery: the master graphics table is at `$00A666` — 8-byte records
`{long src, word vram, word flag}`, 56 entries (`tools/gfx_assets.py`). 43 decode; 13 fail with
unassigned prefixes at output byte 0, which means those sources are **not** in this format and
are left as an open question rather than forced. The genuinely loaded graphics match the table
(`$01CEC0 → $7800` and `$01CEC0 → $57E0` both appear, matching the two captures of that source).

Correction to earlier notes: banks are not Kosinski, and the 31-entry table at `$8672` that
`tools/gfx_banks.py` parses is *a* VRAM layout table but not the list the game actually feeds to
`$008192` during play. `$A666` is. Both are kept; the difference is recorded here rather than
silently overwritten.
