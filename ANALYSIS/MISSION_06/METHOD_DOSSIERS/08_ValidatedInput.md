# validatedInput ViewModel, normalizer and result types

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/ValidatedInputViewModel.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC — M05 gap closed
`Lqm/d;` = `InteractiveLessonValidatedInputViewModel` (extends `base/c`),
`Lcom/getmimo/ui/lesson/interactive/validatedinput/b;` = its Fragment,
`Lqm/b;` = `EditText` text-watcher lambda (writes `Lqm/d;->S : String`).

### `Lqm/d;->E(LessonContent$Interactive)V` — expected-answer extraction
Finds the `jm/e` code block with `Interaction$ValidatedInput` (`c:I startIndex`,
`d:I endIndex`, `e:String`, `f:String[]`). From the code `CharSequence a`:
```
prefix  = a.subSequence(0, coerce(startIndex,0,len))
answer  = a.subSequence(max(0,startIndex), min(endIndex,len)).toString()   // EXPECTED
suffix  = a.subSequence(coerce(endIndex,0,len), len)
state.R = Lqm/h(answer, prefix, suffix)
```
So **the expected answer is shipped inside the lesson's own code block**, delimited by
`startIndex`/`endIndex` — not fetched from a server and not a separate JSON key.
`E()` also builds `Lym/n`/`Lym/j` render tabs with `Lym/m` prefix/suffix, calls `h0(...)`
and resets `S` to `""` via `j0("")`.

### `Lqm/i;->a(String)String` @14172860, 50 insns — NORMALIZER
```
fun normalize(s: String): String {
    val lower = s.toLowerCase(Locale.US)
    val out = StringBuilder()
    for (i in 0 until lower.length) {
        val c = lower[i]
        if (Character.isLetterOrDigit(c) || KEEP.contains(c)) out.append(c)
    }
    return out.toString()
}
```
`KEEP` from `<clinit>` = `['<', '>', '(', ')', ':', '{', '}', ',', '.']`
(`const/16 60,62,40,41,58,123,125,44,46`). Whitespace, quotes, `=`, `;`, `+`, `-`,
`/` etc. are discarded. The class also contains the Smob marker string.

### `InteractiveLessonValidatedInputFragment$setupViews$2->invokeSuspend` @10985684, 75 insns
```
vm.l <- Lum/a.a                        // validating state
val user = vm.S
val expected = vm.R?.a ?: throw ...
val normalizedEqual = normalize(user).equals(normalize(expected))
val exactEqual      = user.equals(expected)
val result = when {
    !normalizedEqual -> Lqm/g;        // INCORRECT (singleton)
    exactEqual       -> Lqm/e;        // CORRECT (singleton)
    else             -> Lqm/f(user, expected)   // CORRECT WITH PARTIAL MATCH
}
vm.b0(user)
vm.Z(result)
```
`Lqm/f` has two String fields `h` (user) and `i` (expected).

### `base/c$onValidatedInputExecuted$1->invokeSuspend` @10939224, 144 insns
`delay(300)` then `when(result)`:
- `Lqm/e` → `V()` (lessonSolvedCorrectly)
- `Lqm/f` → `b0(f.h)` + `W(f)` (lessonSolvedCorrectlyWithPartialMatch)
- `Lqm/g` → `X()` (lessonSolvedIncorrectly)
then posts `e = lessonBundle.b` and clears `f=FALSE`.

## Why this matters for offline reconstruction
Case-insensitive, punctuation-insensitive matching is a **client-side** algorithm, fully
reproducible from shipped content. M05 listed `validatedInput` expected-answer matching as
`UNKNOWN`; it is now `VERIFIED_STATIC`.

## Remaining uncertainty
- `Interaction$ValidatedInput.e : String` and `f : String[]` purpose = `UNKNOWN`
  (likely keyboard / allowed-answer hints; not decoded).
- Why the partial-match branch exists (analytics tolerance vs feedback) = `INFERRED`.
