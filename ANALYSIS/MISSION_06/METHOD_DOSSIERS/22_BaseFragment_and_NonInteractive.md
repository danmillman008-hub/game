# InteractiveLessonBaseFragment / NonInteractive / no-interaction path

**Mission:** MISSION 06 — deep client reverse engineering, Mimo Android 9.35  
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Method:** Androguard 4.1.4 disassembler over all 12 original `ANALYSIS/_INPUT/classes*.dex`;
real `invoke-*` xrefs; Kotlin inner-class names used to recover R8-renamed class names.  
**Primary bytecode evidence:** `ANALYSIS/MISSION_06/EVIDENCE/DISASM/InteractiveLessonBaseFragment.smali.txt`  
**Corpus:** `SCHEMAS/METHOD_CATALOG_MIMO.json`, `SCHEMAS/OBFUSCATION_MAP.json`,
`SCHEMAS/METHOD_NAME_MAP.json`, `CALL_GRAPHS/`.  
`SERVER CONFIRMED = 0`. No backend reconstruction.

> Classification legend: `VERIFIED_STATIC` = read directly from DEX instructions;
> `INFERRED` = named/behavioural interpretation of verified bytecode; `UNKNOWN` = not recovered.

---

## VERIFIED_STATIC
`Lcom/getmimo/ui/lesson/interactive/base/b;` = `InteractiveLessonBaseFragment` (11 votes,
29 methods). `T(View,Bundle)` wires `RunButton`, `InteractionKeyboardContainerView`,
`CodeBodyView`, `CodeHeaderView`, `DatabaseView`, `EmbeddedLessonWebView` and registers
`onLessonWebViewError(ConsoleMessage,String)` callbacks. `onViewCreated$3` emits
analytics properties `webview_type`, `webview_provider`, `webview_version`.

`Lcom/getmimo/ui/lesson/interactive/nointeraction/a;` = `NonInteractiveLessonFragment`
(20 methods). `goToNextPage$1.invokeSuspend` calls `base/c.U()` — the no-interaction
completion path (`lessonSolvedAndProceedToNextLesson`), which records `tries=1` if no
wrong answer was latched.

`Lcom/getmimo/ui/lesson/interactive/c;` = `InteractiveLessonFragment` (2 votes),
`d;` = `InteractiveLessonViewModel` (4 votes, 5 methods incl. `F`, `G`, `H` coroutines).

## Verified UI-state types
`RunButton$State` (`a` enabled / `b` disabled), `InteractionKeyboardButtonState`
(`a`, `b`, `c`), `jm/q(List,boolean)`, `jm/m`/`jm/o` solution feedback,
`jm/j` paragraph, `jm/i` image, `jm/k` webview render items, `Lym/f` interaction event.

## Remaining uncertainty
- Full Compose/XML layout hierarchy and view-binding details = `UNKNOWN` (not needed for
  behavioural reconstruction; M05 already captured runtime UI hierarchies).
