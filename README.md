# Streets of Rage (Mega Drive, 1991) — Forensic Reverse-Engineering

This repository contains an **evidence-backed engineering audit** of *Streets of Rage / Bare Knuckle* (Sega Mega Drive, 1991) built from the ROM images in `Streets-of-Rage_Genesis_EN.zip`.

**This is not a remake, port, clone, or game engine.** No gameplay was re-implemented and
no playable build exists. The code here extracts, decodes, measures and validates evidence
from the original binary, plus one bounded *reconstruction slice* used to prove that
verified rules can be carried into a new implementation and checked against the original.

---

## Stage 2 — from dossier to executable knowledge

Stage 1 produced the 32-section dossier. Stage 2 went back to the binary, re-verified it,
and turned the movement/collision layer into specified, reusable, **tested** code.

| Start here | Why |
|---|---|
| **`COMPLETION_REPORT.md`** | what was done, acceptance criteria PASS/FAIL, scope statement |
| **`AUDIT_REPORT.md`** | what the Stage-1 claims really rested on, and six corrections |
| **`BEHAVIORAL_SPECIFICATIONS/`** | 4 implementation-independent specs (WS-01…WS-04) |
| **`components/`** | reusable modules + ROM-hashed data (`sor_engine`) |
| **`DIFFERENTIAL_VALIDATION.md`** | 7,740 exact comparisons vs the original, and the 11 defects found |
| **`KNOWLEDGE_CATALOG.md`** | knowledge → evidence → component → test index |
| **`UPDATED_COVERAGE_MATRIX.md`** | four independent coverage dimensions |
| **`REPRODUCE.md`** | environment, commands, pitfalls |

```bash
pip install unicorn capstone
python3 tools/verify_stage2.py     # 37 tests, 7,740 differential comparisons
```

**Headline Stage-2 results**
* The reconstruction reproduces the original **bit-exactly** for gravity, terminal clamp,
  air control, integration + freeze, both body boxes, the AABB predicate and projection:
  7,740 comparisons, **0 mismatches, 0 tolerances**.
* Two body-box formulas in the Stage-1 dossier were **wrong** (extents, not offsets), a
  second box at `+$70` was missing, and the AABB comparison order was mis-stated.
* The Stage-1 jump table is **not reproducible**: the real airtimes are 15/17/19 ticks
  (neutral) and 17/20/22 (directional) with apexes −27.375/−35.719/−45.156 px. Stage 1 had
  used an integrate-then-gravity ordering; the ROM applies gravity first.
* The Stage-1 tool implemented **three** of the five experiments its documentation
  claimed. The two missing ones (cheat, jump) are now real, ROM-executed tests.
* Scope is explicit: **one actor class, one code path**. The rest of the game is not
  reconstructed.

---

## Deliverables

| File | Contents |
|---|---|
| **`DOSSIER.md`** | The main deliverable: 32-section Engineering Reverse-Engineering Dossier (architecture, main loop, memory map, object model, player, physics, collision, combat, AI, bosses, levels, rendering, animation, audio, input, camera, assets, resources, RNG, hidden systems, versions, dependency graph, state machines, formulas, unknowns, confidence, coverage, diagrams, log). |
| **`EVIDENCE_DATABASE.md`** | 63 structured evidence records, each with ID, subsystem, claim, evidence, evidence type, location, function, address/offset, experiment, result, confidence, alternative explanations, open questions. |
| **`COVERAGE_MATRIX.md`** | Per-subsystem coverage, evidence IDs, confidence, remaining unknowns; plus coverage by method. |
| **`DIAGRAMS.md`** | Nine ASCII architectural diagrams (boot, frame ownership, gameplay pipeline, actor pass, lifecycle, RAM map, audio path, dependency graph, state machines). |
| **`RESEARCH_LOG.md`** | Chronological journal: what was tried, what worked, what was disproved, and a dead-end table so nothing is retried. |
| **`evidence/verification_results.json`** | Machine-readable output of the verification tool (archive audit, extracted tables, Z80 hash, PRNG sequence, execution traces). |
| **`evidence/rea_zip_inventory.json`** | REA (`rea-agents`) `inspect-artifact` provenance for the ZIP and its 11 members. |
| **`tools/verify_sor_forensics.py`** | The single reproducible tool: reads ROMs straight from the ZIP, verifies all 11 images, extracts tables, decompresses the Z80 driver with an independent Kosinski decoder, and runs five controlled MC68000 experiments. |

## Reproducing the evidence

```bash
python3 -m venv .venv && . .venv/bin/activate
pip install capstone unicorn
python3 tools/verify_sor_forensics.py
```

Requires the archive at the repository root. The tool never writes extracted ROMs to disk.

## What the Stage-1 tool proves
1. All 11 images are exactly 524,288 bytes; checksums recomputed with the game's own algorithm; each derivative classified.
2. The independent Python Kosinski decoder and the **ROM's own decompressor** produce byte-identical output for the Z80 sound driver (asserted inside the tool).
3. REV 00 and REV 01 behave differently on the boss damage path under identical preconditions — the actual reason REV 01 exists.

**Correction (Stage 2):** this tool implements **three** MC68000 experiments (the three
above), not the five previously claimed here. The PRNG sequence (EXP-02) and the
REV00/REV01 trace (EXP-03) are recorded without assertions, and the name-entry cheat
(EXP-04) and jump trajectories (EXP-05) had no code. The cheat and jump measurements are
now implemented and asserted in `tests/test_recovered_behaviour.py` (`D9`, `D10`); the
jump numbers in the Stage-1 dossier were found to be wrong. See `AUDIT_REPORT.md` §2.

## Headline findings
* **22 master states**, one **128-byte actor record**, **156-entry** type dispatch table, **128-entry** player state table.
* Strictly **frame-locked** simulation (no delta time anywhere), driven by a V-Blank handshake.
* **2.5D integer physics**: `screenY = Y + Z/2`, three 16.16 axes, exactly two limiters, no slopes/platforms.
* **Combat geometry** is signed-byte interval overlap with a nibble damage table indexed by animation frame — animation timing *is* hitbox timing.
* **Difficulty** is a 4-way switch on boss attack and a +5 HP bump, plus a 3-palette table for normal enemies.
* **Audio**: the 68k is the sequencer; the Z80 is a register proxy and Δ-PCM feeder (contrary to the usual Mega Drive assumption).
* **A working cheat survives in both retail revisions and is unreachable** — no code path in the image references it.
* **REV 01 exists to fix a boss soft-lock** (`tst.w $32(a0) / ble` inserted before the police-special latch).

## Confidence policy
Every claim is classified `CONFIRMED`, `HIGH CONFIDENCE`, `PROBABLE`, `HYPOTHESIS`, or `UNKNOWN`. Where evidence stops, the dossier says so and lists a resolution route (`DOSSIER §28`). Nothing was inferred into a fact.

## Note on the archive
The 11 ROMs are **not** committed here (they live inside the provided ZIP). All analysis reads them in memory. The translated and patched images are treated as derivatives and are never used as evidence for original behaviour.
