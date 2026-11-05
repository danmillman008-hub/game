# selection / single / multiple choice validation

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/SelectionViewModel.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
- `Lcom/getmimo/ui/lesson/interactive/selection/a;` = `InteractiveLessonSelectionViewModel`
  (6 methods; `L()` returns `LessonType$Selection`).
- `Lnm/b;`, `Lkm/c;`, `Lom/d;`, `Lmm/b;` are four Fragment run handlers that all call
  `Lkm/f;->b(List)Z` and then `base/c.Y(boolean)`.
- `Lkm/f;` = shared selector validator (4 methods).

### `Lkm/f;->b(Ljava/util/List;)Z` @13243392, 46 insns
```
fun isValid(selection: List<sm/a>): Boolean =
    selection.all { it.b == it.c }
```
where `Lsm/a` fields: `b:Z` (selected by learner), `c:Z` (isCorrect from content).
Bytecode: `iget-boolean v1, c; iget-boolean v0, b;` → continue loop only when both equal;
any mismatch returns `false`; an empty list falls through to `true` (the Fragment's RunButton
state prevents submitting an empty selection — `INFERRED`).
`Lkm/f;->d(List)` @13243720 maps each `sm/a` through `sm/a.a(...)` to produce the post-run
display state (wrong answers highlighted), then `Fragment.E0()` reposts it to LiveData.

### `Lnm/b;->E0()V` (selection fragment)
Calls `km/f.b(currentList)` → joins selected labels with `", "` → `base/c.b0(text)` →
`base/c.Y(result)`. Also handles a count-based variant (lines 0x0a8–0x136 of
`EVIDENCE/DISASM/SelectionFragmentRunHandler.smali.txt`) that compares the number of
correctly-chosen items to an expected count.

### `Lgm/h;->a(List)` maps `LessonModule$Selection` to
`LessonInteractionType$Selection`, `$SingleChoice` (`"selection"`) or
`$MultipleChoice` (`"multiple_choice"`) — three distinct renderer branches not previously
identified in M05.

## Remaining uncertainty
- `Lsm/a.b`/`.c` semantic names = `INFERRED` from usage.
- Exact SingleChoice vs MultipleChoice dispatch condition inside `Lgm/h.a` = `UNKNOWN`
  (437-instruction method, only partially decoded).
