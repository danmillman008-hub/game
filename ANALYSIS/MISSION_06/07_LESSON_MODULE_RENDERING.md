# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**Target:** original Mimo Android 9.35 APK, SHA-256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged)  
**Branch:** `arena/aebb90b7-game`, baseline `d0714b40`  
**Toolchain:** Androguard 4.1.4 in `/home/user/_work/m06/venv` over all 12 original
`ANALYSIS/_INPUT/classes*.dex`; patched read-only harness `EVIDENCE/M06_DEX_HARNESS.py`.  
`SERVER CONFIRMED = 0`. Backend services, server business logic, server databases and cloud
infrastructure are **not** reconstructed; only client-side boundaries are recorded.

> Every finding is classified `VERIFIED_STATIC`, `VERIFIED_RUNTIME`, `VERIFIED_BOTH`,
> `INFERRED` or `UNKNOWN`. Evidence fields (APK path, class/method, DEX file + code offset,
> bytecode/Smali, caller/callee, SQL, runtime log, reproduction steps) are given inline or in
> the referenced `EVIDENCE/`, `SCHEMAS/`, `CALL_GRAPHS/`, `METHOD_DOSSIERS/` artefacts.

---

## Verified rendering chain
`base/c.O()` @10949840 (616 instructions) is the central renderer-input builder.
Steps read directly from bytecode:
1. store `D = LessonBundle`, `u = LessonContent$Interactive`.
2. `N()` resets RunButton/keyboard states (`InteractionKeyboardButtonState.b`).
3. iterate `getLessonModules()`, keep only modules whose `LessonModule.a` equals
   `ModuleVisibility.c` (`ALWAYS`) using `Lcom/google/android/recaptcha/internal/b.o(List)`.
4. for each kept module:
   - `Paragraph` → `jm/j(Lds/v.m(paragraph.c))` (join `ArrayList<CharSequence>`),
   - `Image` → `jm_i(image.c:String)`,
   - `Webview` → `jm/k(webview.c:String, webview.e:WebviewType)`.
5. post `ArrayList` of render items to LiveData `m` (`m0.l(Object)`).
6. repeat the filter for code/interaction blocks; build `Lym/n`/`Lym/j` tab models;
   call `h0(list, boolean)` → `Lym/f(v, list, boolean)` → LiveData `w`.

### Feedback-driven module visibility — VERIFIED_STATIC
`ModuleVisibility` = `ALWAYS / CORRECT / WRONG`. After a run:
- `V()` → `c0()` posts `jm/q(list,true)` when `T()` is true,
  plays success sound via `lesson/sound/a.a(true)`.
- `X()` → `d0()` posts `jm/o` copy with `solutionFeedbackWrong`, and M05 run-004
  rendered red "Try again" with the Q option disabled/grey (`VERIFIED_RUNTIME`).
Thus `visible-if="correct"`/`"wrong"` modules are revealed by LiveData state changes, not by
re-parsing the DSL. Exact filtering of `CORRECT`/`WRONG` modules in the adapter = `INFERRED`.

### Per-interaction render items (VERIFIED_STATIC)
| ViewModel | Render items | Evidence |
|---|---|---|
| fillTheGap | `jm/y(qc/a)` prose spans + `jm/x(qc/a,String,jm/w,I)` gaps built from `Option.c/d` char offsets | `FillTheGapViewModel.smali.txt` `E()` |
| validatedInput | `Lym/n(tabName,tabName,Lym/m(prefix,suffix),CodeLanguage)` and `Lym/j` | `ValidatedInputViewModel.smali.txt` `E()` |
| selection | `sm/a` option items with `b=selected`, `c=isCorrect` | `SelectionFragmentRunHandler.smali.txt` |
| spell | `cn/d(id,String,boolean)` letter tokens | `SpellFragmentRunHandler.smali.txt` |
| webview | `EmbeddedLessonWebView` + injected JS | `InteractiveWebViewLessonFragment.smali.txt` |
| no interaction | `NonInteractiveLessonFragment` → `U()` | `NonInteractiveLessonFragment.smali.txt` |

### Renderer selection (VERIFIED_STATIC)
`CALL_GRAPHS/06_content_pipeline.json`, `METHOD_DOSSIERS/12_LessonInteractionTypeSelector.md`.
Nine `LessonInteractionType` subclasses; `InteractiveLessonViewModel.E()` posts `Lgm/g` to
LiveData; `ChapterActivity` chooses the Fragment.

### Hard mode — VERIFIED_STATIC
`LessonContent$Interactive.hardModeModulesOrDefault()`, `getHasDifferentHardModeContent()`;
`InteractiveLessonViewModel.E()` recomputes `Lgm/h.a(hardModeLessonModules)` when hard mode
is enabled; `ChapterViewModel.shouldStartChapterInHardMode` (`PathMapViewModel.N`) and
DataStore `completed_hard_mode_chapters` / `KEY_HARD_MODE_COMPLETED_LESSON_IDS` persist it.

### Remaining uncertainty
- Exact RecyclerView/Compose adapter and `CodeBodyView`/`DatabaseView` drawing logic = `UNKNOWN`
  (M05 captured UI hierarchies; behavioural reconstruction does not require widget internals).
- Full `O()` (616 insns) contains additional module branches not decoded = `INFERRED`.
