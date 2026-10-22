# Updated Coverage Matrix (Stage 2)

Stage 1 tracked *investigation* coverage. This matrix tracks four **independent**
dimensions, because documentation is not behaviour and a module is not a validation.

| Dimension | Meaning | Scale |
|---|---|---|
| **RE** | reverse-engineering evidence: how much of the mechanism is known and how strongly | 0–100 %, confidence label |
| **SPEC** | behavioural specification an implementer can follow without the binary | — / partial / full |
| **IMPL** | reusable implementation exists and is exercised | — / yes |
| **VAL** | independent validation against the original binary | — / exact / partial |

Only a row with **SPEC + IMPL + VAL** counts as reconstructed. Everything else is
research, regardless of how well documented it is.

---

## A. Reconstructed slice (this stage)

| # | Behaviour | RE | SPEC | IMPL | VAL |
|---|---|---|---|---|---|
| 1 | 16.16 arithmetic + whole-pixel reads | 100 % CONFIRMED | `WS-01 §4` | `fixed.py` | **exact** (all of D1–D8) |
| 2 | Neutral / directional / soft gravity | 100 % CONFIRMED | `WS-01 §5.1` | `kinematics.py` | **exact** 900 cases (D1) |
| 3 | Terminal-velocity clamp | 100 % CONFIRMED | `WS-01 §5.2` | `kinematics.py` | **exact** 208 cases (D2) |
| 4 | Air control + facing/anim side effects | 100 % CONFIRMED | `WS-01 §5.3` | `kinematics.py` | **exact** 400 cases (D3) |
| 5 | Integration + freeze predicate | 100 % CONFIRMED | `WS-01 §5.4` | `kinematics.py` | **exact** 409 cases (D4) |
| 6 | Body-box construction (two boxes) | 100 % CONFIRMED | `WS-02 §5–6` | `boxes.py` | **exact** 4,160 cases (D5) |
| 7 | AABB overlap predicate | 100 % CONFIRMED | `WS-02 §5` | `boxes.py` | **exact** 507 cases (D6) |
| 8 | Projection + camera exception + culling | 100 % CONFIRMED | `WS-03 §5` | `projection.py` | **exact** 1,016 cases (D7) |
| 9 | Frame composition of 1–8 | 100 % CONFIRMED | `WS-04 §5` | `slice_runner.py` | **exact** 140 frames (D8) |
| 10 | Jump airtime/apex consequences | 100 % CONFIRMED | `WS-01 §13` | via 1–5 | **exact** + corrected (D10) |
| 11 | Name-entry cheat table | 100 % CONFIRMED | catalog K-18 | — | **exact** (D9) |

**Slice totals:** 7,740 exact comparisons · 37 tests · 0 mismatches · 0 tolerances.

## B. Engine-wide status (unchanged by this stage unless marked)

| Subsystem | RE | SPEC | IMPL | VAL | Note |
|---|---|---|---|---|---|
| Boot / VDP init / checksum | CONFIRMED | — | — | Stage-1 static | out of scope |
| Master states / frame scheduling | CONFIRMED | — | — | Stage-1 static | needed before a full-frame harness |
| Actor dispatch (156 types, 66 slots) | CONFIRMED | — | — | — | next infrastructure step |
| Actor record | 21 fields CONFIRMED, 10 unknown | partial | partial (`Actor`: slice fields only) | slice fields only | C-8 aliasing must be resolved first |
| Player state machine (128 entries) | HIGH | — | — | — | `U-STATE-01` |
| Physics | **CONFIRMED** | **full** | **yes** | **exact** | this stage |
| Collision (body geometry) | **CONFIRMED** | **full** | **yes** | **exact** | this stage |
| Collision (attack/hurt) | PROBABLE | — | — | — | `U-ATT-01/02`; next slice |
| Combat / damage pipeline | CONFIRMED (formulas) | — | — | — | needs attack slice first |
| Enemy AI (10 archetypes) | HIGH | — | — | — | |
| Boss architecture (17 handlers) | HIGH | — | — | — | |
| Level / spawn scripts | HIGH parser / PROBABLE fields | — | — | — | `U-LVL-01/02` |
| Terrain height map | CONFIRMED | — | — | — | not in slice |
| Rendering (sort, buffers) | CONFIRMED | — | — | — | projection part done |
| Animation timing | CONFIRMED (structure) | — | — | — | `U-CBT-01` |
| Audio (68k sequencer + Z80) | HIGH / CONFIRMED identity | — | — | Stage-1 hash | |
| Input | CONFIRMED | partial (`WS-01 §3`) | yes (held byte) | D3 | `U-INP-03` remains |
| Camera | CONFIRMED (formula) | — | — | — | `U-CAM-01` |
| Asset formats (Kosinski, plane map) | CONFIRMED | — | — | Stage-1 bit-exact | |
| RNG | CONFIRMED | — | — | Stage-1 closed form | |
| Hidden/cheat/revisions | CONFIRMED | catalog K-18 | — | **exact** (D9) | |

## C. Coverage by method (Stage 2 additions)

| Method | Contribution |
|---|---|
| Static disassembly of the slice | 9 routines re-read instruction-by-instruction (~430 instructions) |
| ROM execution (MC68000) | 7,740 primitive comparisons + 140 composed frames + 6 jump profiles + 7 cheat codes |
| Table extraction with provenance | 13 z-pairs + 32 box records, hashed and committed |
| Byte-range revision diffing | 8 slice ranges confirmed identical in REV 00/01 |
| Negative/invariant testing | freeze word, clamp boundaries, cull edges, null-box paths |
| Spec-only tests | 24 tests that run without the emulator |

## D. What "complete" means here

The slice is complete **for its stated scope**: every rule is specified, implemented
and exactly validated. The game is **not** reconstructed: 21 of the 27 subsystems in
§B still have no behavioural specification, and the slice covers one actor class on
one code path. Any statement that this stage reconstructs Streets of Rage is false.
