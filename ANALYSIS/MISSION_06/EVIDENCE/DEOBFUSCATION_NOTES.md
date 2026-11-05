# R8 name recovery and anti-decompilation notes

## VERIFIED_STATIC
R8 renamed most application classes to single letters (`base/c`, `executable/q`, `Lye/b`,
`Lte/c`, `Lqm/i`). Kotlin synthetic inner classes retain the original outer class name, so:

1. Enumerate every class with `$` in its name.
2. Take `X$foo$N` → `X` (original semantic stem).
3. Read the first `<init>` parameter — the outer instance type — to get the obfuscated class.
4. The modal `X` across all inner classes of that outer is the recovered name.

173 mappings in `SCHEMAS/OBFUSCATION_MAP.json` (e.g. `executable/q` →
`ExecutableLessonViewModel`, 46 votes). 596 method hints in
`SCHEMAS/METHOD_NAME_MAP.json` come from coroutine inner-class names such as
`lessonSolvedCorrectly$1`; **low-vote entries are heuristic**, and only manually verified
names are used as facts in call graphs/dossiers.

## Smob anti-decompilation — VERIFIED_STATIC bytecode / INFERRED causal link
`classes.dex` contains exactly one string
`Smob - Mod obfuscation tool v4.6 by Kirlif'`, emitted via `const-string` in many
`<clinit>`/constructor bodies. Method streams also contain injected `const/4 vN, <junk>`
no-ops that clobber registers not subsequently read, and trailing
`fill-array-data-payload` objects in the linear decode. Example:
`LessonProgress.isSolvedCorrectly()` @9913532 has `const/4 v3, 2` immediately overwritten
by `const/4 v3, 1`. M05's JADX `Method not decompiled` / `JADX ERROR: NullPointerException
in pass: ClassModifier` plausibly results from these decoys (`INFERRED`, not proven).
M06 filtered them before reading branches and booleans.

## Known caveats
- `METHOD_NAME_MAP.json` votes=1 is a hint, not exact-name proof.
- `EVIDENCE/TOOLCHAIN/export_disasm2.py` reported `MISSING ExecuteFilesResponse` / `ExecuteLessonResponse`
  labels — absence of a *name hint*, not proof the class/API is absent.
- `LessonProgressDao.smali.txt` has 0 methods because it is an interface; Room SQL in
  `../MISSION_05/EVIDENCE/ROOM_SQL.txt` is authoritative.
- `DEX_STRING_INDEX.txt` scans method string constants only; absence of `runFiles` or
  `System.loadLibrary` is **not** proof of absence.
- All 82 dumps and both catalogs were regenerated with the corrected xref cache
  (descriptors containing spaces preserved; 78,560 xref targets).
