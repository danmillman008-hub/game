# MISSION 06 — INVESTIGATION PLAN (evidence-based, short steps)

Branch `arena/aebb90b7-game`, baseline `d0714b40`. Target: original Mimo 9.35 APK
`48ce1740…7c7a` (unchanged). `SERVER CONFIRMED = 0`.

## Starting evidence (M05, not re-done)
Shipped v753 curriculum + DSL; exact Room SQL; DataStore; 5 emulator runs with
onboarding → first lesson, offline cold start, wrong-answer feedback; 5 exact
asset↔runtime matches. M01/M02 left `DEX_BYTECODE_EVIDENCE.json` (6,016 call
graph edges, 1,211 exact edges), `dexlib.py`, `dex_bytecode.py`, JADX archive
(2,211 .java), Ghidra artefacts.

## Toolchain decision (M06, new)
- Local sandbox has **no** `java`/`jadx`/`baksmali`/`apktool`/`dexdump`.
- `pip install androguard==4.1.4` into `/home/user/_work/m06/venv` (pypi.org
  allowed) **succeeded** → full Dalvik disassembler with mnemonics, operands,
  method/field/string indices, and xref construction.
- Reuse M01 `_TOOLCHAIN/dexlib.py` for independent offsets/verification.
- JADX output is incomplete (`Method not decompiled`); M06 recovers method
  bodies from **DEX bytecode**, not from stubs.

## Highest-value unresolved execution paths (ordered)
1. **Answer validation** — `fillTheGap`, `validatedInput`, `selection`, `spell`
   ViewModels: real bytecode, pseudocode, correct/incorrect/partial transitions.
2. **Content pipeline** — assets → loader → kotlinx serialization → DTO →
   runtime model → parser → `LessonModule` → renderer.
3. **Progression** — `GetPathMapState`, completion thresholds, unlock rule,
   `ChapterFinishedViewModel` offline/online branches, XP/streak/daily goal.
4. **Persistence lifecycle** — Room DAOs, `LessonProgressQueue`, DataStore,
   force-stop recovery.
5. **Code editor / executable lessons** — local vs remote execution boundary,
   `CodeDiffViewModel`, `spieglein` editor bundle, test result DTOs.
6. **Navigation / component architecture** — DI, Activity/Fragment graph,
   background workers, callbacks.
7. **Native libraries** — JNI registrations and real Java callers.
8. **Offline behaviour specification** — client-side method that blocks each
   operation, from bytecode + targeted runtime experiments.

## Method per step
`dex → class/method index → disassembly → xrefs (callers/callees) → strings →
fields → state changes → pseudocode → dossier → diagram → evidence DB entry`.
Targeted emulator experiments only for a **specific hypothesis** (e.g. does a
correct answer write `lesson_progress`), never for screenshots of known pages.

## Deliverables
01–19 as specified, plus `DIAGRAMS/` (9), `CALL_GRAPHS/`, `METHOD_DOSSIERS/`,
`SAMPLES/`, `RUNTIME_EVIDENCE/`. Coverage matrix in 19; never claim 100%.

## Classification
`VERIFIED_STATIC` / `VERIFIED_RUNTIME` / `VERIFIED_BOTH` / `INFERRED` /
`UNKNOWN` on **every** finding, with class, method, DEX file+offset, bytecode.
