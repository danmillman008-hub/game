# fillTheGap ViewModel + Fragment run handler

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/FillTheGapViewModel.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
- `Lcom/getmimo/ui/lesson/interactive/fillthegap/a;` = `InteractiveLessonFillTheGapViewModel`
  (inner class `…$configureInteraction$1`, `…$createCursorBlinkEvents$3`). 4 methods.
- `Lim/d;` = its Fragment (has `T(View,Bundle)`, `M0()` returning the VM, `E0()` run handler).

### `a;->E(LessonContent$Interactive)V` @10964388, 210 insns
Finds first `jm/e` whose `b` is `Interaction$FillTheGap`; reads
`Interaction$FillTheGap.c : List<Option>`. Each `Option` has fields
`a:Z (isCorrect)`, `b:CharSequence (text)`, `c:I (startIndex)`, `d:I (endIndex)`.
Builds:
```
allTokens      = options.map { cn/d(120, it.b.toString(), it.a) }
correctTokens  = allTokens.filter { it.c }            // expected answer in content order
renderItems    = prose spans jm/y + gaps jm/x (from Option.c/d char offsets)
state          = Lim/a(allTokens, correctTokens, shuffledTokens?, renderItems)
Q = state; j0(state);   // posts to LiveData R
// finally: flow of cursor-blink events → configureInteraction$1/$2, launched in viewModelScope
```
Error string: `"There is no code block found with FillTheGap interaction. There must be at least one"`.

### `Lim/d;->E0()V` @12834200, 200 insns — THE ANSWER VALIDATOR
```
val st = vm.Q ?: return
val expected = st.b                       // correctTokens, ordered
val selected = st.c.filter { it.b }       // tokens the learner placed, ordered
var ok = false
if (selected.size == expected.size) {
    ok = true
    for ((i,t) in selected.withIndex())
        if (t.a != expected[i].a) { ok = false; break }
}
val answerText = selected.filter { it.a.isNotBlank() }
                         .joinToString(separator = " ") { it.a }
vm.b0(answerText)                         // stores answer for analytics
vm.Y(ok)                                  // onLessonRun(ok)
```
Comparison is **exact String equality** on `cn/d.a` (token text), in order, against the
`correct=true` options. There is no server call and no fuzzy matching on this path.

### `a;->j0(Lim/a;)V` @10965552, 137 insns
Recomputes RunButton state (`RunButton$State.a` enabled / `.b` disabled) from whether the
number of placed tokens equals the number of gaps, and posts `Lym/f` via `base/c.h0()`.

## Remaining uncertainty
- Meaning of `cn/d.b` (used by the filter) is `INFERRED` as "placed/filled"; DEX has no field names.
- `Lud/a.C(allTokens)` (third state list) is probably a shuffled keyboard pool = `INFERRED`.
