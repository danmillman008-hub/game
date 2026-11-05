# GetPathMapState — unlock state machine

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/GetPathMapState.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
`Lcom/getmimo/interactors/path/d;` = `GetPathMapState`; its `invoke$3.invokeSuspend`
@10129608, 659 instructions constructs the whole path-map state `Lvn/n`.

### Verified state classes (constructed only here)
| Class | Meaning (from `toString()` strings) |
|---|---|
| `Lvn/d0` | `Completed(id=…, isProLocked=…)` — built when `Tutorial.isCompleted()` |
| `Lvn/e0` | `Locked(id=…, isProLocked=…)` |
| `Lvn/g0` | `Unlocked(id=…, isProLocked=…)` |
| `Lvn/h0` | `UnlockedButNoKeys(id=…)` |
| `Lvn/d` | chapter item `(id,title,isCompleted,isCompletedInHardMode)` |
| `Lvn/y` / `Lvn/a0` | `Locked(index=…)` / `Unlocked(index=…)` section states |
| `Lvn/a` / `Lvn/b` | track-level `Locked(trackId…)` / `Unlocked(trackId…)` |

### Verified rules
- Tutorials of type `Challenge` are excluded from the path item list
  (`Set.of(TutorialType.Challenge).contains(t.type)`).
- A `lastOrNull()` over already-built items is used together with
  `TutorialType.isRequired()` and `Lvn/i0.d()` to decide whether the next required
  predecessor is completed → sequential unlock.
- `Tutorial.isCompleted()` → `Lvn/d0`; chapter items get `isCompleted` and a hard-mode
  flag from `Lds/w.c(Set, trackId, tutorialId, chapterId)`.
- `Tutorial.getHasProgress()`, `TutorialType.PracticeOptional`, a Pro subscription tier
  (`Lyg/c.c`), dev-menu overrides (`Lsk/a.d()/e()`), and an integer keys count decide
  `Locked` / `UnlockedButNoKeys` / `Unlocked`.
- Section states are built by `Lcc/b;->y(List, Z, Integer?, Z, Z) : ArrayList`
  (verified constructor callers `Lvn/y`, `Lvn/a0`, `Lvn/v`, `Lvn/w`).
- Final state `Lvn/n(track, sectionStates, selectedSectionIndex, dialogs, nextSectionState, …)`.

## Remaining uncertainty — explicit
The **exact boolean combination** selecting `Locked` vs `UnlockedButNoKeys` vs `Unlocked`
is `UNKNOWN` (registers `v14`, `v24`, `v31`, `v43`, `v46` are junk-obfuscated and the
659-instruction coroutine has 3 suspension labels). This is the precise unresolved
component for the unlock rule. `CanOpenChapterWithKeys` (dossier 19) is the other half.
