# spell interaction validation

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/SpellViewModel.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
`Lcom/getmimo/ui/lesson/interactive/spell/a;` = `InteractiveLessonSpellViewModel`
(7 methods; `E()` 249 insns, `j0(Lcn/d;)`, `k0(Lpm/f;)`).
`Lpm/b;` = its Fragment (`E0()` @1283xxxx).

### `Lpm/b;->E0()V` — THE ANSWER VALIDATOR
```
val st = vm.Q ?: return           // Lpm/f
val expected = st.b               // ArrayList<cn/d> expected letters, ordered
val typed    = st.c               // ArrayList<cn/d> user letters, ordered
var ok = false
if (typed.size == expected.size) {
    ok = true
    for ((i,t) in typed.withIndex())
        if (t.a != expected[i].a) { ok = false; break }
}
val answerText = typed.filter{ it.a.isNotBlank() }.joinToString(separator = "") { it.a }
vm.b0(answerText)
vm.Y(ok)
```
Exact byte-for-byte same algorithm shape as fillTheGap but with separator `""` (letters
concatenated) instead of `" "`. Error/keyword string `"spell"`.

### Interaction model
`Interaction$Spell` fields `b:Z (isDefault)`, `c:I (startIndex)`, `d:I (endIndex)`;
the expected letter sequence comes from the code-block substring between those indices.

## Remaining uncertainty
- Whether case is normalised before this comparison = `UNKNOWN`; the bytecode shows only
  `String.equals` via `kotlin/jvm/internal/h.c`, i.e. case-sensitive.
