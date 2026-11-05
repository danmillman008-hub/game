import pathlib
D=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06')
APK='48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a'
PRE=f'''# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `{APK}` (unchanged) · `SERVER CONFIRMED = 0` · classification on every finding.

---

'''
docs={}
docs['14_NATIVE_LIBRARIES_AND_JNI.md']=r'''
## VERIFIED_STATIC (M05 inventory reused; M06 DEX cross-check)
12 `.so` libraries, `arm64-v8a`, from original APK:
`libsigner.so`, `libdatastore_shared_counter.so`, `libyrf.so`, `librive-android.so`,
`libandroidx.graphics.path.so`, `libc++_shared.so`, `libimage_processing_util_jni.so`,
`libbugsnag-ndk.so`, `libbugsnag-plugin-android-anr.so`, `libsqlcipher.so`,
`libbarhopper_v3.so`, `libmlkit_google_ocr_pipeline.so`.
M04 run `41998643355` verified native loads `: ok` (`VERIFIED_RUNTIME`).

## M06 DEX cross-check — VERIFIED_STATIC
`strings_index.txt` scan of **method string constants** found `System.loadLibrary`
only in Rive-related code (`app.rive.runtime.kotlin`). No other `loadLibrary` string appeared
in method constant pools. **This is NOT proof of absence**: libraries may be loaded by
`System.load` from an absolute path, by `native` method resolution from a static initializer
whose string lives in the class string pool, or by a third-party SDK. M05's `12 .so` doc
records the shipped files; M06 does not contradict it.

## JNI boundary — what is and is not reconstructed
| Library | Role (`VERIFIED_STATIC` name + `INFERRED` purpose) | Reconstructed? |
|---|---|---|
| `libsigner.so` | request signing / attestation (`INFERRED`) | **No** — native code, network protocol, auth bypass explicitly out of scope |
| `libdatastore_shared_counter.so` | DataStore cross-process counter (`INFERRED`) | **No** |
| `libyrf.so` | third-party SDK (`UNKNOWN`) | **No** |
| `librive-android.so` | Rive animation runtime | **No** |
| `libsqlcipher.so` | encrypted SQLite (`INFERRED`) | **No** — Room SQL strings are plain DEX constants |
| `libbugsnag*` | crash/ANR reporting | **No** |
| `libimage_processing_util_jni.so`, `libbarhopper_v3.so`, `libmlkit_google_ocr_pipeline.so` | CameraX / ML Kit | **No** |

## Explicit boundary
M06 did **not** disassemble native ARM64 code, did not reconstruct JNI method tables,
did not reconstruct any network protocol/signature algorithm, did not bypass TLS/certificate
pinning, and did not perform any auth/purchase/credential work. `SERVER CONFIRMED = 0`.
`EVIDENCE/DEX_STRING_INDEX.txt` contains the exact scan output for audit.

## Remaining uncertainty
- Exact `System.loadLibrary` call sites for the 12 libraries = `UNKNOWN` (string-pool scan
  limitation described above).
- Native ↔ Kotlin API surface = `UNKNOWN`.
'''
docs['15_OFFLINE_BEHAVIOR_SPECIFICATION.md']=r'''
## Classification
`VERIFIED_STATIC` for DEX gates; `VERIFIED_RUNTIME` for M05 run evidence;
`INFERRED` where the two are correlated; `UNKNOWN` for every unobserved case.
Diagram `DIAGRAMS/09_offline_architecture.mmd`.

## What works fully offline — VERIFIED_STATIC
1. **Asset loading**: `Lye/b.b(J)`/`d()` call `AssetManager.open` on APK members;
   no network. M05 measured 10,298 curriculum JSON files across 10 locales.
2. **Deserialization**: `kotlinx.serialization` on local UTF-8 text.
3. **DSL parsing**: `org.xmlpull.v1.XmlPullParserFactory` + `StringReader`; local.
4. **Rendering**: `base/c.O()` + `Lgm/h.a()` + per-interaction ViewModels; local.
5. **Answer validation for every interaction**: `Lim/d.E0()`, `Lkm/f.b()`, `Lpm/b.E0()`,
   `Lqm/i.a()` + `setupViews$2`, `q.I()`; all local string/list comparisons.
6. **Progress writes**: `LessonProgressRepository.createLessonProgress` →
   `LessonProgressQueue.storeLessonProgress` → Room `lesson_progress` `in_queue=1`.
7. **Answer counting**: `AnswersInChapter(correct,total)` StateFlow; first-try counter;
   streak detector invocation.
8. **Preferences**: hard mode, onboarding, first-run, daily-goal DataStore values.
9. **WebView preview**: shipped HTML template + `lesson-webview.js`.

## Client-side dependency boundaries — VERIFIED_STATIC
| Operation | Gate | Offline behaviour |
|---|---|---|
| POST unsynced lesson progress | `LessonProgressRepository.postUnsyncedLessonProgress` → `NetworkUtils.a()` | logs `"No internet connection, not posting unsynced lesson progress"`, throws `NoConnectionException`; **rows remain in Room `in_queue=1`** |
| Chapter-end rewards / success state | `ChapterFinishedViewModel$handleOfflineState$1` → `f.R(cont)` (`handleChapterAlreadyCompletedState`) | falls back to local already-completed state; no server call |
| Key-gated chapters | `CanOpenChapterWithKeys$invoke$1` → `DefaultKeysRepository.c()` + `f` Flow count | `Lvn/h0 UnlockedButNoKeys` state |
| Remote code execution | `runFiles` endpoints | local `solvedContent` comparison decides correctness; remote result `UNKNOWN` |
| Streak / XP / coins / keys / ETA / daily-goal awards | `Progress`/`PostProgressResponse`/`TrackEtaResponse` bodies | `UNKNOWN` — server-owned |
| AiTutor / Remote Config / analytics | analytics + network clients | offline errors logged; not blocking lesson content |

### Exact connectivity check — VERIFIED_STATIC
`Lcom/getmimo/network/a;->a()Z` @10174360:
```
val net = ConnectivityManager.getActiveNetwork() ?: return false
val caps = ConnectivityManager.getNetworkCapabilities(net) ?: return false
return caps.hasTransport(TRANSPORT_WIFI) || caps.hasTransport(TRANSPORT_CELLULAR)
```
`b()Z` = `!a()`. 14 / 13 callers respectively.

## Runtime corroboration (M05 — no new M06 run)
`42002808217` cold start with `Active default network: none` and
`connect: Network is unreachable`; first three offline XMLs byte-identical to online;
`NetworkUnknown` / `UnknownHostException` for analytics `cdp.customer.io`; no
FATAL/ANR/tombstone. `42003884423`/`42006697783` rendered real shipped lessons
(tutorial-904, tutorial-2199, tutorial-4648, tutorial-4672, track 274) offline.
M05 run-002/003 displayed "Connect to the internet to progress further" at the path screen
while local content was still visible. `VERIFIED_BOTH` for the correlation with the gates.

## Explicit UNKNOWNs (do not overclaim)
- No offline **answer submission** was observed at runtime in M05; correct-answer offline
  state remains `UNKNOWN VERIFIED_RUNTIME`.
- Whether **every** operation is blocked offline (IAP, AiTutor, leaderboards, profile,
  code-playground publishing, account deletion) = `UNKNOWN`; only the gates above were decoded.
- `NoConnectionException` propagation to UI (toast/dialog/retry) = `UNKNOWN`.
- Offline reconnect / queue drain behaviour = `UNKNOWN` (`svc wifi enable`/`svc data enable`
  did not restore connectivity in M05 runs).
- Server response bodies and server-side progress logic = `UNKNOWN`, `SERVER CONFIRMED = 0`.
'''
docs['16_RECONSTRUCTED_ALGORITHMS.md']=r'''
All algorithms below are `VERIFIED_STATIC` from named DEX methods. Pseudocode is a faithful
restatement of bytecode, not invented specification. Raw disassembly:
`EVIDENCE/VALIDATION_RAW_DISASM.txt`, `EVIDENCE/ALGORITHM_DIGEST.txt`,
`EVIDENCE/PATH_STATE_DISASM.txt`, `EVIDENCE/DISASM/*.smali.txt`.

### A. `InteractiveLessonBaseViewModel.Y(Z)` @10954996
```
fun onLessonRun(isCorrect: Boolean) {
  if (runInProgress.value == TRUE) return
  runInProgress.value = TRUE
  viewModelScope.launch {
      if (isCorrect) lessonSolvedCorrectly() else lessonSolvedIncorrectly()
      nextPage.value = lessonBundle.chapterIndex
      runInProgress.value = FALSE
  }
}
```
### B. `V()` lessonSolvedCorrectly @10953356 (162 insns)
```
awaitBrowserOutput()
wrongLatch = FALSE; attempts++
updateSolutionFeedback()
val tries = if (wrongLatch == TRUE) 0 else 1
createLessonProgress(tries, attempts)
storeLessonProgressInMemory()
showSolutionFeedbackCorrect(); sound.playCorrect()
analytics.track(isSolvedCorrectly, …); emitLessonId(lessonId); cleanupFiles()
```
### C. `X()` lessonSolvedIncorrectly @10954596 (113 insns)
```
attempts++; wrongLatch = TRUE
createLessonProgress(0, attempts)
storeLessonProgressInMemory()
showWrongFeedbackBlock()
```
### D. `LessonProgressRepository.createLessonProgress` @10063916
```
completedAt = Instant.now()
if (completedAt < startedAt) log("CreateLessonProgress: completedAt date (…) is before startedAt date (…)")
LessonProgress(lessonId=bundle.a, completedAt, startedAt, tries, tutorialId=bundle.e,
   tutorialVersion=bundle.v, trackId=bundle.f,
   publishSetVersion = tracksRepository.currentPublishSetVersion(),
   attempts, isPracticeProgress=bundle.B, inQueue=true)
```
### E. `LessonProgress.isSolvedCorrectly()` @9913532
`return tries >= 1` — **M05 correction** (not `attempts >= 1`).
### F. fillTheGap `Lim/d.E0()` @12834200
```
selected = state.placedTokens.filter{ it.placed }
ok = selected.size == state.correctTokens.size &&
     selected.indices.all{ selected[it].text == state.correctTokens[it].text }
answer = selected.filter{ it.text.isNotBlank() }.joinToString(" ")
baseVM.b0(answer); baseVM.Y(ok)
```
### G. selection `Lkm/f.b(List)` @13243392
`return list.all { it.selected == it.isCorrect }`
### H. spell `Lpm/b.E0()`
```
typed = state.c; expected = state.b
ok = typed.size == expected.size && typed.indices.all{ typed[it].text == expected[it].text }
answer = typed.filter{ it.text.isNotBlank() }.joinToString("")
baseVM.b0(answer); baseVM.Y(ok)
```
### I. validatedInput normalizer `Lqm/i.a(String)` @14172860
```
lower = s.toLowerCase(Locale.US)
out = ""
for (c in lower) if (c.isLetterOrDigit() || c in KEEP) out += c
return out
KEEP = ['<','>','(',')',':','{','}',',','.']
```
### J. validatedInput result `setupViews$2.invokeSuspend` @10985684
```
user = vm.S; expected = vm.R.a
result = if (normalize(user) != normalize(expected)) Lqm/g
         else if (user == expected)                Lqm/e
         else                                      Lqm/f(user, expected)
vm.b0(user); vm.Z(result)
```
`onValidatedInputExecuted$1` @10939224: `delay(300)` then
`Lqm/e → V()`, `Lqm/f → b0(f.h) + W(f)`, `Lgm/g → X()`.
### K. executable `q.I()` @10912932
```
user   = codeFiles.map{ it.content }
answer = executable.files.map{ it.solvedContent }
return if (user == answer) state else errorState + IncorrectSolutionException
```
### L. `LessonProgressQueue.updateCorrectAnswersCount()` @10056956
```
queued = repo.getAllLessonProgressInQueue()
correct = queued.count{ it.isSolvedCorrectly() }
_answersInChapter.emit(AnswersInChapter(correct, queued.size))
```
### M. Offline gate `NetworkUtils.a()` @10174360 and
`LessonProgressRepository.postUnsyncedLessonProgress`
```
if (!androidNetworkUtils.a()) {
  log("No internet connection, not posting unsynced lesson progress")
  throw NoConnectionException
}
launch { POST unsyncedRows }
```
### N. DSL dispatch `Lte/c.b(String)` @14378108
```
parser = XmlPullParserFactory.newInstance().apply{ isNamespaceAware = true }.newPullParser()
parser.setInput(StringReader(html))
for each START_TAG:
  p→Lte/d.a | code→Lte/a.a | selection→Lte/e.a | img→Lte/c.a |
  webview→Lte/g.a | database→Lte/b.a | html/body/unknown→skip
```
### O. Path-map state `GetPathMapState$invoke$3` @10129608
```
for tutorial in sections (excluding Challenge):
  state = if (tutorial.isCompleted) Lvn/d0 Completed
          else if (no local progress && !sequential prerequisite met) Lvn/e0 Locked
          else if (pro/key gate fails) Lvn/h0 UnlockedButNoKeys
          else Lvn/g0 Unlocked
  chapterItem = Lvn/d(id,title,isCompleted,isCompletedInHardMode)
final Lvn/n(track, sectionStates, selectedIndex, dialogs, …)
```
The exact boolean combination in step `state` is `UNKNOWN` — shown here as the closest
faithful shape with explicit uncertainty, not a substitute rule.

## Algorithms explicitly NOT reconstructed
Scoring/XP/coins/keys/streak/daily-goal award formulas and thresholds; full unlock
predicate; `SingleChoice`/`MultipleChoice`/`Reveal` dispatch; `W()` partial-match feedback;
remote code execution; any server-side algorithm. `SERVER CONFIRMED = 0`.
'''
docs['17_CORRECTIONS_AND_LIMITATIONS.md']=r'''
## Corrections — VERIFIED_STATIC (M06 bytecode corrects M05)
| # | M05 statement | M06 correction | Evidence |
|---|---|---|---|
| C-1 | `LessonProgress.isSolvedCorrectly()` = `attempts >= 1` | **`tries >= 1`**; `classes.dex` @9913532 uses `iget … ->tries I`. `tries` is the solved flag (`V()` → 1, `X()` → 0); `attempts` is the submission counter `base/c.d` | `METHOD_DOSSIERS/04_LessonProgress_isSolvedCorrectly.md`, `EVIDENCE/DISASM/LessonProgress.smali.txt` |
| C-2 | "no scoring formula found" | Chapter-end **local** counting formula recovered: `AnswersInChapter(count{isSolvedCorrectly}, queued.size)` and `count{isSolvedCorrectly && attempts==1}`. Absolute XP/keys/streak awards still `UNKNOWN` | `METHOD_DOSSIERS/03_LessonProgressQueue.md` |
| C-3 | Interaction types ~6 | **9** `LessonInteractionType` constants including `SingleChoice`, `MultipleChoice`, `Reveal`, `None` | `METHOD_DOSSIERS/12_LessonInteractionTypeSelector.md` |
| C-4 | DSL parsed by "unknown parser" | **`org.xmlpull.v1.XmlPullParser`** via `XmlPullParserFactory` | `METHOD_DOSSIERS/11_DSL_LessonParser.md` |
| C-5 | `validatedInput` matching `UNKNOWN` | normaliser + 3-way result fully recovered | `METHOD_DOSSIERS/08_ValidatedInput.md` |
| C-6 | `solvedContent` sufficiency questioned | `q.I()` compares user file contents to shipped `solvedContent` by `List.equals` → **sufficient for correctness decision** | `METHOD_DOSSIERS/10_ExecutableLessonViewModel.md` |
| C-7 | JADX stubs suggested missing implementations | Stubs are caused by smob-injected junk `const/4` and trailing `fill-array-data-payload`; real implementations exist in DEX (`INFERRED` causal link) | `02_METHODOLOGY_AND_TOOLCHAIN.md` |
| C-8 | `NetworkUtils` inferred from strings | Exact `hasTransport(WIFI|CELLULAR)` gate recovered | `METHOD_DOSSIERS/18_NetworkUtils.md` |

## Toolchain/QA corrections made during M06
- `m06_dex.py` xref regex truncated descriptors containing spaces; fixed to `(L…->.*)$`;
  cache rebuilt (78,560 xref targets). All call graphs use the corrected cache.
- `callers()` returns 4-tuples `(caller, opcode, offset, dex)`; early scripts assumed 2.
- `class_fields.get(c)` may be `None` on library classes.
- `METHOD_CATALOG_MIMO.json` / `CLASS_CATALOG_MIMO.json` and the **first 18**
  disassembly headers were generated before the xref fix; their caller/callee *count*
  headers are stale. The `EVIDENCE/DISASM/*.smali.txt` instruction bodies are unaffected.
  `CALL_GRAPHS/*.json` were regenerated from the corrected cache and are authoritative.
- `METHOD_NAME_MAP.json` low-vote entries are heuristic; call graphs show only manually
  verified semantic names.
- `export_disasm2.py` reported `MISSING ExecuteFilesResponse` / `ExecuteLessonResponse`
  semantic labels — this is absence of a *name hint*, not proof the classes are absent.
- `LessonProgressDao` dump has 0 methods (interface); Room SQL is the authoritative evidence.
- `strings_by_method` scans only method string constants; absence of `runFiles` or
  `System.loadLibrary` in that index is **not** proof of absence.

## Known limitations — explicit
1. **No new emulator run.** Local sandbox has no emulator/ADB/SDK/Java/KVM; M05 already ran
   5 experiments. Repeating the 24-tap chain without deterministic replay was explicitly
   ruled out. M06 runtime claims reuse M05 evidence, clearly labelled.
2. **No private data extraction.** No root, no `/data/data/com.getmimo/databases` read, no
   TLS/pinning bypass, no credential/account/purchase/auth work.
3. **No server reconstruction.** `SERVER CONFIRMED = 0`; no response bodies, no backend
   business logic, no server DB, no cloud infra.
4. **No APK modification.** Original APK SHA unchanged; all DEX/assets read-only.
5. **Truncated transcripts.** Long coroutines (`Lye/b.a`, `Lye/d`, `DefaultTracksRepository.i`,
   `GetPathMapState$invoke$3`, `DefaultTrackLoader$getExecutableLesson$2`, `Lhg/e.intercept`,
   `X/W/d0/e0`) were printed partially in terminal scratch dumps; **full bodies are saved**
   in `EVIDENCE/DISASM/*.smali.txt` and `EVIDENCE/*_DISASM.txt`. Interpretations that depend
   on the undecoded remainder are marked `INFERRED`/`UNKNOWN`.
6. **JADX archive incomplete** (2,211 `.java`, many `Method not decompiled`); used only for
   cross-checked field names.

## What remains UNKNOWN (exact pointers)
`18_OPEN_QUESTIONS.md` and `19_REVERSE_ENGINEERING_COVERAGE.md` list each with class,
method, DEX offset and why it is unresolved.
'''
docs['18_OPEN_QUESTIONS.md']=r'''
## OPEN QUESTIONS — all explicitly `UNKNOWN`
`SERVER CONFIRMED = 0`. No item below is guessed or filled with a plausible value.

| # | Question | Exact pointer | Why unresolved / what would resolve it |
|---|---|---|---|
| Q-1 | Correct-answer **runtime** UI state | `base/c.V()`, M05 runs 001–005 | M05 never produced a correct answer; no new M06 run. Needs deterministic replay of `42003884423`'s exact 24 taps plus an answer that satisfies `Lqm/i.a` |
| Q-2 | Persisted `lesson_progress` row **after** an answer | Room `lesson_progress`, `LessonProgressDao` (`Lcg/a;`) | Requires root / private DB extraction — forbidden. Static write path is verified |
| Q-3 | Server response bodies for progress / runFiles / ETA / keys | `LessonProgressApi`, `HTTP_VERBS_RESOLVED.json` (53 endpoints) | Deliberately out of scope (no backend reconstruction) |
| Q-4 | Absolute XP / keys / coins / streak / daily-goal award formulas and thresholds | `Progress`, `PostProgressResponse`, `TrackEtaResponse`, `ChapterFinishedSuccessType` | Depend on server bodies; client only consumes |
| Q-5 | **Full unlock rule** (Locked / UnlockedButNoKeys / Unlocked) | `GetPathMapState$invoke$3.invokeSuspend`, `classes.dex` @10129608, 659 insns | Junk `const/4` decoys + 3 suspension labels; full body saved but boolean combination not decoded |
| Q-6 | `CanOpenChapterWithKeys` true-branch result | `CanOpenChapterWithKeys$invoke$1` @10104004 | 102-insn coroutine with unreachable-looking branch; needs full decode |
| Q-7 | `W()` partial-match feedback difference vs `V()` | `base/c.W(qm/f, cont)` @10953916, 202 insns | Body saved, not fully interpreted |
| Q-8 | `d0()` hard-mode / AI-Tutor / attempts boolean combination | `base/c.d0(cont)` @10956096, 148 insns | Body saved, not fully interpreted |
| Q-9 | `SingleChoice` vs `MultipleChoice` vs `Reveal` exact dispatch | `Lgm/h.a(List)` @12460480, 437 insns | Only type constants and marker strings verified |
| Q-10 | `Lte/a.a` full interaction/option construction | `Lte/a.a(XmlPullParser)` 490 insns | Inputs/outputs verified; internal offsets not decoded |
| Q-11 | `Interaction$ValidatedInput.e:String`, `f:String[]` semantics | `Interaction$ValidatedInput` | Fields known, usage not decoded |
| Q-12 | `Lye/b.a(Tutorial)` filter and `Lye/d` loader selection / update trigger | `Lye/b`, `Lye/d` | Which loader wins at runtime is a DI binding not decoded |
| Q-13 | `DefaultTracksRepository.i` full 409-insn state machine | `tracks/c.i(J,cont)` @9750496 | Body saved, caching/completion merge partially decoded |
| Q-14 | `Lhg/e.intercept` (network interceptor) | `Lhg/e;->intercept` | Not decoded; no request/response reconstruction attempted |
| Q-15 | `DefaultTrackLoader$getExecutableLesson$2` full coroutine | inner class | Body saved, not fully interpreted |
| Q-16 | Exact `q.I()` applicability to all executable lessons | `q.I()` @10912932, callers=1 | One MVI reducer caller not fully decoded |
| Q-17 | Remote code-execution service behaviour | `/v1/code/runfiles`, `/v1/tutorials/{id}/runFiles` | Server-owned boundary, `SERVER CONFIRMED = 0` |
| Q-18 | Full offline blocking for **every** operation (IAP, leaderboards, profile, AiTutor, publishing, account deletion) | per-feature Retrofit clients | Only progress-post, chapter-end, keys and content rendering gates decoded |
| Q-19 | `NoConnectionException` UI propagation / reconnect | `postUnsyncedLessonProgress` catch sites | Not decoded; M05 `svc wifi/data enable` did not restore connectivity |
| Q-20 | Native `.so` ↔ Kotlin API surface and `System.loadLibrary` call sites | `libsigner.so`, `libdatastore_shared_counter.so`, etc. | Method-string scan finds only Rive; no native disassembly performed (forbidden boundary) |
| Q-21 | Exact DI framework / scopes / singleton graph | `<init>` signatures in `METHOD_CATALOG_MIMO.json` | No Hilt/Koin metadata decoded |
| Q-22 | Navigation graph routes / fragment transactions | `ChapterActivity`, `MainActivity`, `PathMapFragment` | Only component names and LiveData events decoded |
| Q-23 | Force-stop / process-recreation restoration | `LessonProgressQueue`, DataStore | No runtime test, no private DB read |
| Q-24 | Room migration class list / SQL | Room identity hashes only | Not decoded in M06 |
| Q-25 | External URL offline substitution (4,257 refs, M05) | shipped lesson HTML | Content strings; no offline substitution rule decoded |

## What is NOT an open question anymore (closed in M06)
`isSolvedCorrectly` field, `createLessonProgress` 11-column mapping, all interaction
validators, `validatedInput` normaliser, executable `solvedContent` comparison, DSL parser
technology, nine interaction types, asset locale paths, offline `NetworkUtils` gate,
offline chapter-end fallback, `AnswersInChapter` counting formula, smob anti-decompilation.
'''
docs['19_REVERSE_ENGINEERING_COVERAGE.md']=r'''
## Coverage matrix
`VERIFIED_STATIC` = DEX/bytecode or shipped asset read directly;
`VERIFIED_RUNTIME` = M04/M05 emulator observation; `VERIFIED_BOTH` = both;
`INFERRED` = named interpretation of verified bytecode; `UNKNOWN` = explicitly unresolved.
`SERVER CONFIRMED = 0`.

| # | Component | Status | Primary evidence | Residual |
|---|---|---|---|---|
| 1 | Launcher / process | `VERIFIED_BOTH` | M04 `41998643355`, M01 component graph | — |
| 2 | DI container graph | `VERIFIED_STATIC` | `Lhm/b;`, 32-arg `q.<init>`, method catalog | framework `UNKNOWN` |
| 3 | Asset loaders & locales | `VERIFIED_STATIC` | `Lye/b`, `ContentLocale`, M05 stats | `Lye/d` selection `UNKNOWN` |
| 4 | JSON deserialization | `VERIFIED_STATIC` | `tracks/b.c`, `Lhb0/b.b`, `$$serializer` classes | full DTO list `INFERRED` |
| 5 | Content models / schema | `VERIFIED_BOTH` | M05 `CONTENT_SCHEMA.json`, M06 `CLASS_CATALOG_MIMO.json` | hard-mode predicate `INFERRED` |
| 6 | DSL parser | `VERIFIED_STATIC` | `Lte/c.b`, six `Lte/*` parsers | `Lte/a.a` internals `UNKNOWN` |
| 7 | Module visibility & feedback | `VERIFIED_BOTH` | `ModuleVisibility`, `base/c.c0/d0`, M05 run-004 | `d0` booleans `UNKNOWN` |
| 8 | Renderer selection | `VERIFIED_STATIC` | `Lgm/h.a`, `InteractiveLessonViewModel.E` | 3 dispatch predicates `UNKNOWN` |
| 9 | Render-item mapping | `VERIFIED_STATIC` | `base/c.O` @10949840 | adapter internals `UNKNOWN` |
| 10 | fillTheGap validation | `VERIFIED_STATIC` | `Lim/d.E0` @12834200 | — |
| 11 | selection validation | `VERIFIED_STATIC` | `Lkm/f.b` @13243392 | choice dispatch `UNKNOWN` |
| 12 | spell validation | `VERIFIED_STATIC` | `Lpm/b.E0` | — |
| 13 | validatedInput validation | `VERIFIED_STATIC` | `Lqm/i.a` @14172860, `setupViews$2` @10985684 | `e/f` fields `UNKNOWN` |
| 14 | WebView activity messages | `VERIFIED_BOTH` | `WebViewActivityResult`, `lesson-webview.js`, M05 counts | payload mapping `INFERRED` |
| 15 | executableFiles correctness | `VERIFIED_STATIC` | `q.I` @10912932 | applicability `UNKNOWN` |
| 16 | no-interaction / reveal | `VERIFIED_STATIC` | `NonInteractiveLessonFragment`, `U()` | — |
| 17 | Run dispatcher / state machine | `VERIFIED_STATIC` | `Y`, `onLessonRun$1`, `onValidatedInputExecuted$1` | `W()` `UNKNOWN` |
| 18 | `createLessonProgress` record | `VERIFIED_STATIC` | @10063916 + Room SQL | param names `INFERRED` |
| 19 | Room queue & answer counting | `VERIFIED_STATIC` | `LessonProgressQueue` @10056956/10058920 | force-stop `UNKNOWN` |
| 20 | Offline gate | `VERIFIED_BOTH` | `NetworkUtils.a` @10174360, M05 cold start | UI propagation `UNKNOWN` |
| 21 | Chapter-end online/offline | `VERIFIED_BOTH` | `handleOfflineState$1`, M05 path screens | reward thresholds `UNKNOWN` |
| 22 | Path-map states | `VERIFIED_STATIC` | `GetPathMapState$invoke$3` @10129608 | **exact unlock rule `UNKNOWN`** |
| 23 | Keys gate | `VERIFIED_STATIC` | `CanOpenChapterWithKeys$invoke$1` @10104004 | true branch `UNKNOWN` |
| 24 | Completion attachment | `VERIFIED_STATIC` | `CompletionRepository.b` @9981172 | SQL specific DAO `INFERRED` |
| 25 | Preferences / DataStore | `VERIFIED_STATIC` | `data/local/a`, M05 storage strings | full key list `UNKNOWN` |
| 26 | Code editor / hints / preview | `VERIFIED_STATIC` | `q.F`, `Ldg/a`, `CodeLanguage` | remote runner `UNKNOWN` |
| 27 | Native libraries | `VERIFIED_STATIC` (inventory) / `VERIFIED_RUNTIME` (loads) | M05 `.so` doc, M04 run | JNI surface `UNKNOWN` |
| 28 | Network API surface | `VERIFIED_STATIC` (verbs) | M02 `HTTP_VERBS_RESOLVED.json` | bodies `UNKNOWN` |
| 29 | Analytics / workers / services | `VERIFIED_STATIC` (names) | `analytics/a`, WorkManager classes | triggers `UNKNOWN` |
| 30 | smob anti-decompilation | `VERIFIED_STATIC` (bytecode) / `INFERRED` (causal link) | `classes.dex` string + junk `const/4` | — |
| 31 | Deobfuscation | `VERIFIED_STATIC` | 173 class / 596 method hints | low-vote hints `INFERRED` |
| 32 | Call graphs | `VERIFIED_STATIC` | 9 JSON, 622 real invoke edges | — |
| 33 | Runtime correct-answer state | `UNKNOWN` | M05 runs 001–005 | no deterministic M06 replay |
| 34 | Persisted progress after answer | `UNKNOWN` | Room write path static only | private DB extraction forbidden |
| 35 | Server responses / scoring / economy | `UNKNOWN` | `SERVER CONFIRMED = 0` | deliberate scope boundary |

## Deliverable inventory
19 numbered reports · 9 `.mmd` diagrams · 9 `.mmd` + 9 `.json` call graphs ·
22 method dossiers · 83 `.smali.txt` class dumps (+ `INDEX.json`) · 11 derived evidence
disassembly/digest files · 11 byte-exact original samples + manifest ·
`SCHEMAS/` 5 JSON files · `EVIDENCE_DATABASE.json` · `RUNTIME_EVIDENCE/` ·
`MISSION_06_REVIEW.md` · `README.md` · `00_INVESTIGATION_PLAN.md`.

## Reproducibility
`/home/user/_work/m06/venv/bin/python` + `EVIDENCE/M06_DEX_HARNESS.py`,
`M06_EXPORT_CATALOG.py`, `M06_METHOD_NAME_MAP.py`; no network needed; all reads from
`ANALYSIS/_INPUT/classes*.dex` and the unchanged original APK.
'''
for n,c in docs.items():
    (D/n).write_text(PRE+c.strip()+'\n',encoding='utf-8')
    print('wrote',n,len(PRE+c))
