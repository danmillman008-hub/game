# Completion Report — Stage 2

**Deliverable state:** one vertical slice reconstructed, validated against the original
ROM, and documented end to end. The game as a whole is **not** reconstructed.

---

## 1. What was actually done

1. **Audited the Stage-1 work.** Re-ran the verification tool, read it line by line,
   and found that it implements three of the five experiments the documentation claims;
   two claimed experiments (cheat, jump table) had no code behind them.
2. **Went back to the binary.** Disassembled nine routines in the movement/geometry
   path, re-derived their rules, and corrected six documented claims — including a
   wrong body-box formula, a missing second box, a wrong AABB comparison order, and a
   jump table computed with the wrong integration order.
3. **Built a ROM oracle.** A harness that executes individual original subroutines on a
   real MC68000 core with synthetic actor records (`tools/rom_probe.py`).
4. **Implemented the slice** as four dependency-free modules plus a frame-stepped runner
   (`components/sor_engine/*`, `reconstruction/slice_runner.py`).
5. **Validated it differentially**: 7,740 exact integer comparisons and 140 composed
   frame-steps, zero mismatches, zero tolerances (`tests/`, `DIFFERENTIAL_VALIDATION.md`).
6. **Reproduced the two orphaned Stage-1 experiments** against the ROM (D9, D10); the
   cheat table matches, the jump table does not.
7. **Wrote the specifications, catalog, coverage matrix, reproduction guide and audit**
   so the result is usable by an agent that has none of this session's context.

## 2. Acceptance criteria

| # | Criterion | Status | Evidence |
|---|---|---|---|
| 1 | Original behaviour independently investigated | **PASS** | `AUDIT_REPORT.md` §4/§6; 9 routines re-read; 6 Stage-1 claims corrected |
| 2 | Central rules in an implementation-independent specification | **PASS** | `BEHAVIORAL_SPECIFICATIONS/WS-01…WS-04` (13-part structure each) |
| 3 | Important claims traceable to evidence | **PASS** | `EV-S2-*` records with address, experiment and result; per-rule tables in each spec |
| 4 | Implementation consumes the specification/derived config | **PASS** | `components/data/body_boxes.json` (ROM-hashed) is the only data source; module docstrings cite spec sections |
| 5 | Independent tests compare against the original | **PASS** | 7,740 comparisons executing ROM code; `evidence/stage2/stage2_verification.json` |
| 6 | Discrepancies investigated, not patched away | **PASS** | `DIFFERENTIAL_VALIDATION.md` §4: 11 defects, each with root cause; two were wrong *oracle* assumptions, one was a wrong Stage-1 claim |
| 7 | Tests reproducible with documented commands | **PASS** | `REPRODUCE.md`; `python3 tools/verify_stage2.py` → 37 passed |
| 8 | Limitations and unresolved dependencies explicit | **PASS** | `DIFFERENTIAL_VALIDATION.md` §6–7; `UPDATED_COVERAGE_MATRIX.md` §B; `KNOWLEDGE_CATALOG.md` §C |
| 9 | At least one component reusable without private knowledge | **PASS** | `components/` + `components/README.md`: contracts, invariants, failure modes, data provenance |
| 10 | A future agent can locate, understand, run and extend | **PASS** | `KNOWLEDGE_CATALOG.md` maps knowledge → evidence → component → test; `RESEARCH_LOG.md` records dead ends |

**No criterion is FAIL or BLOCKED for the declared slice.** They would all be FAIL if
applied to "the game", which is why §5 states the scope explicitly.

## 3. Numbers

| Metric | Value |
|---|---|
| Tests | 37 (24 spec, 5 ROM-behaviour, 8 differential) |
| Differential comparisons vs original code | 7,740 |
| Composed frame-steps compared | 140 |
| Routines executed on the MC68000 core | 11 |
| Routines disassembled for the slice | 9 (~430 instructions) |
| Tables extracted with provenance | 2 (13 z-pairs, 32 box records) |
| Stage-1 claims corrected | 6 (C-1…C-4, C-7, C-8) plus 3 additions (C-5, C-6, C-9) |
| Tolerances used | 0 |
| Mismatches remaining | 0 |

## 4. What changed in the repository

**Added:** `AUDIT_REPORT.md`, `BEHAVIORAL_SPECIFICATIONS/` (4 + index), `components/`,
`reconstruction/`, `tests/`, `DIFFERENTIAL_VALIDATION.md`, `KNOWLEDGE_CATALOG.md`,
`UPDATED_COVERAGE_MATRIX.md`, `REPRODUCE.md`, `COMPLETION_REPORT.md`,
`tools/rom_probe.py`, `tools/extract_slice_tables.py`, `tools/verify_stage2.py`,
`evidence/stage2/`.

**Modified:** `README.md` (Stage-2 entry point + corrected experiment claim),
`DOSSIER.md` (errata block and six corrected passages), `EVIDENCE_DATABASE.md`
(21 new `EV-S2-*` records), `RESEARCH_LOG.md` (RL-49…RL-64), `COVERAGE_MATRIX.md`
(pointer to the four-dimension successor), `.gitignore` (`work/`).

**Untouched:** the Stage-1 verification tool and its JSON output. Its assertions still
pass unchanged.

## 5. Scope statement (read this before quoting results)

The reconstruction covers **one actor class on one code path**: player kinematics,
body-box geometry, projection and their per-frame composition. It does **not** include
the state machine, attack/hurt resolution, damage, animation timing, AI, camera motion,
audio, levels or rendering. The correct claim is:

> "The movement and body-collision layer of Streets of Rage is specified, reimplemented
> and exactly validated against the original ROM; the rest of the game is not."

## 6. Why the slice was chosen

| Candidate slice | Evidence availability | Risk | Chosen |
|---|---|---|---|
| Player movement / 2.5D coords | high (self-contained routines, documented fields) | low | **yes** |
| Body-box collision | high (tables located, builder isolated) | low | **yes** (same slice) |
| Attack / hurt resolution | medium (`$00AB24` identified, record semantics unresolved) | high | no — next |
| Damage pipeline | medium (formula known, needs a hit first) | medium | no |
| Enemy AI | low per-type | high | no |

The attack slice was rejected because the six-byte threshold records at `+$72` are not
yet understood; implementing them would have meant guessing, which the project rules
forbid.

## 7. Blockers and next actions

| # | Blocker | Impact | Next concrete action |
|---|---|---|---|
| 1 | `+$72` threshold-record semantics (`$00AB24`/`$00AB88`) | blocks the attack slice | instrument `$00AB24` with a synthetic attacker/victim pair and dump the records each move actually consumes; enumerate writers of `+$70`/`+$72` |
| 2 | No full-frame scheduler harness (VDP/Z80/IO absent) | slice validated at routine level, not in a running game | add minimal VDP/Z80 stubs and step `$00AD8E`/`$00AE4C` for real frames |
| 3 | Actor-field aliasing (C-8) | blocks a single flat record model | classify fields by actor class; likely needs a per-class view layer |
| 4 | 13 dead player states (`U-STATE-01`) | FSM modelling | locate the dispatch guard for target `$000000` |
| 5 | `U-CBT-01` per-move frame data | combat fidelity | dump animation banks and correlate with state ids |

## 8. Honest assessment of the method

What worked: choosing a slice whose outputs are integers; executing the ROM instead of
trusting any document; comparing thousands of cases rather than a handful; treating
every failure as a modelling question first and a code question second.

What nearly failed: the oracle. Two of the eleven defects found were in the *probe*
(sign-extended `cmpa` and non-aliased RAM), each of which would have produced
confident, wrong "confirmations". Any future stage must treat the harness as a
first-class artifact and validate it against known-good expectations before trusting it.

What this proves: the pipeline — original binary → verified rule → specification →
component → differential test — is real and repeatable for self-contained engine
behaviour. It does not yet prove it scales to systems whose state is spread across the
whole frame; that is the next experiment, not a conclusion of this one.
