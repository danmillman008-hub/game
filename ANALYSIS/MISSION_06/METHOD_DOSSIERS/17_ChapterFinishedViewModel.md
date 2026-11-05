# ChapterFinishedViewModel — online/offline chapter end

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/ChapterFinishedViewModel.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
`Lcom/getmimo/ui/chapter/chapterendview/main/f;` = `ChapterFinishedViewModel` (13 votes).
Inner classes `ChapterFinishedViewModel$handleOfflineState$1` and
`$handleOnlineState$1` (+ `$1$1`, `$1$2`) exist — M05 already noted them.

`handleOfflineState$1.invokeSuspend` (48 insns):
```
val vm = this.b
vm.R(cont)      // f->R = handleChapterAlreadyCompletedState
catch (t) { log(t) }
```
i.e. **offline chapter end falls back to the already-completed local state**, with no server
call. `f->G` = `handleOnlineState`, `f->F` =
`getChapterEndSuccessStateWithRetry`, `f->E` = `consumeKeyIfNeeded`,
`f->R` = `handleChapterAlreadyCompletedState`, `f->O` = `onContinue`,
`f->I`/`S` = `onChapterFinishedScreenShown`, `f->M` = `shouldShowRatingBottomSheet`,
`f->N` = `shouldShowStreakChallengeScreen`, `f->H` = refresh after streak-goal purchase.

Strings in the class: `streakChallengeCoinPrice`, `userCoins`,
`DAILY_GOAL_NOT_REACHED|REACHED|ALREADY_REACHED_EARLIER_TODAY`
(`ChapterFinishedSuccessType`), `chapterFinishedStreakChallengeFragment`, etc.

## Offline significance
This is the precise client-side method behind M05 run-002/003's
"Connect to the internet to progress further" while local content remained visible: the
chapter-end screen branches offline to local completion state instead of fetching
server-owned rewards. `VERIFIED_STATIC` for the branch; `VERIFIED_RUNTIME` for the screen
text comes from M05 run evidence.

## Remaining uncertainty
- Success-type thresholds (daily goal, streak, XP) = `UNKNOWN`, require server response bodies
  which M06 deliberately did not reconstruct.
