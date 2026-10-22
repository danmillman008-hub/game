> **Superseded for Stage-2 purposes.** This file records Stage-1 *investigation* coverage.
> The four-dimensional coverage matrix (evidence / specification / implementation /
> validation) is `UPDATED_COVERAGE_MATRIX.md`. One claim below is corrected there:
> the Stage-1 tool implements three of the five experiments listed under "Coverage by
> method", not five (`AUDIT_REPORT.md` §2).

# Coverage Matrix
### Streets of Rage / Bare Knuckle (Mega Drive, 1991) — investigation coverage

Legend for **Investigated**: percentage of the subsystem's *code and data* that was actually read (not merely located).
A subsystem is only marked "complete" when its mechanisms are understood **or** its remaining unknowns are named with a resolution route.

| # | Subsystem | Investigated | Evidence (record IDs) | Confidence | Remaining unknowns |
|---|---|---:|---|---|---|
| 1 | Boot / TMSS / VDP init / checksum | 100 % | EV-BOOT-01…05 | CONFIRMED | none |
| 2 | Platform & version identification | 100 % | EV-VER-01…04 | CONFIRMED | `U-VER-01` (semantics of the second REV01 edit) |
| 3 | Binary structure (code/data partition) | 100 % | EV-LOOP-02, EV-AST-01, entropy sweep | CONFIRMED | bank-by-bank asset inventory |
| 4 | Main loop / frame scheduling | 100 % | EV-LOOP-01…05 | CONFIRMED | `U-FEEL-01` (why the double frame exists) |
| 5 | Interrupt architecture (V-Blank, modes) | 95 % | EV-LOOP-04, EV-RND-03 | CONFIRMED (bytes) / PROBABLE (purposes) | mode↔scene mapping |
| 6 | Memory map (68k RAM, VRAM, Z80, I/O) | 95 % | EV-MEM-01…04 | CONFIRMED | `$FF3FC0`–`$FF3FFF`; `U-VRAM-01` |
| 7 | Actor record layout | 70 % | EV-ACT-01…04 | CONFIRMED (21 fields) / HIGH (6) / UNKNOWN (10) | `U-ACT-01` |
| 8 | Actor pools & dispatch | 100 % | EV-ACT-02, EV-ACT-03 | CONFIRMED | `U-DISP-01`, `U-POOL-01` |
| 9 | Player architecture (states, pre-emption) | 85 % | EV-PLY-01…05 | CONFIRMED (table) / HIGH (semantics) | `U-STATE-01`, `U-CBT-01` |
| 10 | Physics model | 100 % | EV-PHY-01…03, EV-ACT-04 | CONFIRMED | per-character launch values |
| 11 | Collision / hitbox / hurtbox | 85 % | EV-COL-01…03 | CONFIRMED (math) / PROBABLE (region roles) | `U-COLL-01` |
| 12 | Combat / damage / reactions | 90 % | EV-CBT-01…04 | CONFIRMED | full per-move frame table |
| 13 | Enemy AI (10 archetypes + director) | 75 % | EV-AI-01…03 | HIGH | depth of per-type transcription |
| 14 | Boss architecture (17 handlers) | 80 % | EV-BOSS-01…03, EV-VER-02 | HIGH | 3 handlers only partially traced; `U-BOSS-01` |
| 15 | Level / spawn scripts | 70 % | EV-LVL-01…03 | HIGH (parser) / PROBABLE (fields) | `U-LVL-01`, `U-LVL-02` |
| 16 | Terrain / height model | 100 % | EV-LVL-02, EV-MEM-04 | CONFIRMED | per-round tables |
| 17 | Rendering pipeline (buffers, sort, SAT) | 90 % | EV-RND-01…03 | CONFIRMED | `U-VRAM-01` |
| 18 | Animation system | 85 % | EV-ANM-01 | CONFIRMED (structure) | data dump (`U-CBT-01`) |
| 19 | Audio — 68k sequencer | 75 % | EV-AUD-01, EV-AUD-04 | HIGH | `U-AUD-01` |
| 20 | Audio — Z80 driver & PCM | 90 % | EV-AUD-02, EV-AUD-03 | CONFIRMED (identity/format) | bank selection per song |
| 21 | Input | 95 % | EV-INP-01 | CONFIRMED | `U-INP-01` |
| 22 | Camera | 90 % | EV-CAM-01, EV-CAM-02, EV-MEM-03 | CONFIRMED | `U-CAM-01`, parallax band count |
| 23 | Asset formats / compression | 80 % | EV-AST-01, EV-AST-02 | CONFIRMED | full bank inventory |
| 24 | Resource management | 80 % | EV-MEM-01, EV-ACT-02, EV-AST-02 | HIGH | `U-VRAM-01` |
| 25 | RNG | 100 % | EV-RNG-01 | CONFIRMED | none |
| 26 | Hidden / debug / unused code | 85 % | EV-DEAD-01…03, EV-CBT-02 | CONFIRMED | `U-HID-01` |
| 27 | Regional (J/U/E, PAL) logic | 100 % (sites) | EV-BOOT-05 | CONFIRMED | `U-REG-01` |
| 28 | Version differences REV00/REV01 | 100 % | EV-VER-01…04 | CONFIRMED | `U-VER-01` |
| 29 | Cross-system dependencies | 90 % | `DOSSIER §24` | HIGH | — |
| 30 | State machines (all levels) | 90 % | EV-LOOP-02, EV-PLY-01, EV-BOSS-02 | CONFIRMED/HIGH | boss sub-phase tables |
| 31 | Recovered formulas/constants | 100 % of located sites | EV-CBT-01, EV-PHY-01, EV-RNG-01, EV-BOSS-01 | CONFIRMED | — |

## Coverage by method
| Method | Coverage contribution |
|---|---|
| Static disassembly (Capstone M68K) | ~62 000 instructions read across ~40 routines and all 22 master states |
| Table decoding | 156 type handlers, 128 player states, 22 master states, 22 enemy stat entries, 17 DAC descriptors, 10 extra-life entries, 6 cheat codes |
| Byte-exact diffing | all 11 images pairwise; 4 REV01 regions fully explained |
| Dynamic execution (Unicorn MC68000) | 5 experiments: decompressor, PRNG, boss-police branch (×2 revisions), name-entry cheat, jump trajectories |
| Reference implementation | Kosinski decoder validated bit-exactly against the ROM's own routine |
| Negative search | 4 exhaustive scans (hit-stop, VDP H/V counter, cheat reachability, delta-time) |

## What "not complete" means here
Every row above has been *examined*. Rows 7, 13, 14, 15, 18, 19, 23 are not "complete" in the strict sense: their mechanisms are established, but the **data volume** (per-move tables, per-boss phase tables, per-round terrain sources, song opcode map) has not been transcribed. That distinction is deliberate — the reverse-engineering risk in those areas is clerical, not architectural.
