# Streets of Rage (Mega Drive, 1991) — Forensic Reverse-Engineering

This repository contains an **evidence-backed engineering audit** of *Streets of Rage / Bare Knuckle* (Sega Mega Drive, 1991) built from the ROM images in `Streets-of-Rage_Genesis_EN.zip`.

**This is not a remake, port, clone, or engine.** No gameplay was re-implemented. The only code here exists to extract, decode, measure, and validate evidence from the original binary.

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

## What the tool proves
1. All 11 images are exactly 524,288 bytes; checksums recomputed with the game's own algorithm; each derivative classified.
2. The independent Python Kosinski decoder and the **ROM's own decompressor** produce byte-identical output for the Z80 sound driver (asserted inside the tool).
3. The PRNG formula matches the ROM's routine for 16 consecutive calls, including full 32-bit state.
4. REV 00 and REV 01 behave differently on the boss damage path under identical preconditions — the actual reason REV 01 exists.
5. The dormant name-entry cheat returns exactly the values encoded in its own table.

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
