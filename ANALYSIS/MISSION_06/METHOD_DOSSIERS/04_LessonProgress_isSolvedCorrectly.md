# LessonProgress.isSolvedCorrectly() — M05 correction

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/LessonProgress.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC — exact bytecode
`Lcom/getmimo/data/model/room/LessonProgress;->isSolvedCorrectly()Z`  
`classes.dex` code_offset `9913532`, 13 instructions:
```
000000  move-object v1, v5
000002  iget v1, v1, LessonProgress->tries I
000006  const/4 v3, 2          <- Smob junk
000008  const/4 v3, 1          <- real 1
00000a  move v0, v3
00000c  if-lt v1, v0, +004h
000010  const/4 v4, 1
000012  return v0              <- v0 == 1 (true)
000014  const/4 v3, 2
000016  const/4 v3, 0
000018  move v1, v3
00001a  return v1              <- false
```
**`return tries >= 1`.** The field is `tries`, not `attempts`.

## CORRECTION to M05
M05 (`CONTENT_MODEL.md` / `LEARNING_ENGINE.md`) recorded `isSolvedCorrectly()` as
`attempts >= 1`. M02 had only `intField >= 1`. The DEX bytecode proves the read is
`iget … ->tries I`. Reason for the earlier error: the JADX archive is incomplete and the
Room entity's two integer getters were conflated. Documented in
`17_CORRECTIONS_AND_LIMITATIONS.md`. Classification of correction: `VERIFIED_STATIC`.

## How `tries` is produced — VERIFIED_STATIC
- `base/c;->V()` (lessonSolvedCorrectly): `v2 = (C == TRUE) XOR 1` → `H(v2, d)`;
  with `C = FALSE`, `tries = 1`.
- `base/c;->X()` (lessonSolvedIncorrectly): `H(0, d)` → `tries = 0`.
- `base/c;->U()` (proceed to next): `tries = NOT(C == TRUE)`.
Thus `tries` is effectively the "solved correctly" flag (0/1) while `attempts` (`d`) counts
submissions. `LessonProgressQueue.getCorrectLessonsFirstTryCount` uses
`isSolvedCorrectly() && attempts == 1`.

## Remaining uncertainty
- Whether a wrong answer followed by a correct one in the same lesson leaves `C` FALSE
  (so `tries=1`) is `INFERRED` from `V()` overwriting `C`; not runtime-verified.
