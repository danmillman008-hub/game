# CanOpenChapterWithKeys — keys gate

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/CanOpenChapterWithKeys.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
`Lcom/getmimo/interactors/chapter/a;` = `CanOpenChapterWithKeys` (constructor injects
`Lcom/getmimo/data/source/remote/keys/a;` = `DefaultKeysRepository`).

`CanOpenChapterWithKeys$invoke$1.invokeSuspend` @10104004, 102 insns:
```
val keysRepo = this.a.a
val flag = keysRepo.c() : Boolean?          // feature/config flag
if (flag == false) {
    val count = keysRepo.f.first() : Int    // StateFlow<Int> key balance
    return count > 0
}
return <other branch>                      // not fully decoded
```
`Lvn/h0` (`UnlockedButNoKeys`) is the UI state for `count == 0`. `Lsk/a` dev-menu can override.

## Remaining uncertainty
- The `flag == true` branch and the exact `Boolean` return = `UNKNOWN`.
- Key consumption (`ChapterFinishedViewModel.E consumeKeyIfNeeded`) and any server-side
  balance update = `UNKNOWN` / server-owned boundary.
