# Phase 12.5 — Questions opened *by* mission-8

Mission-8 found things that were invisible to the earlier registers. They are recorded as new questions with the
status rules of `01_CLOSURE_METHOD.md`.

| ID | Question | Status | Evidence today | What would close it |
|---|---|---|---|---|
| A1 | Is the literal `mimo-auth-production` a Firebase tenant id, an emulator project, or a preference key? | `GENUINELY_UNKNOWN` | constructor string list of `…authentication.a` (`05_…/evidence/DEX_auth_interceptors_and_repository.json`) | trace the string argument to its first consumer |
| A2 | Where is sign-out implemented? | `PARTIALLY_CLOSED` | `com.getmimo.ui.authentication.logout.{a,b}` exist; bodies unread | read both classes at DEX level |
| A3 | What does the `Runnable` scheduled inside `ku.a.d` do? | `NOT_RECOVERED` | `new-instance Lapp/rive/c;` + `lev.b;->a(Runnable)` | read the `app.rive.c` branch used there |
| A4 | In what order do `hg.e` (network guard) and `fh.a` (authorization) run? | `GENUINELY_UNKNOWN` | both are `okhttp3.Interceptor` implementations; the builder arm was not read | read `ae.m` case 20 interceptor list order |
| A5 | Are tokens ever cached outside Firebase? | `PARTIALLY_CLOSED` (negative evidence) | no app write-site found; negative scan only | a write-site scan for token-like keys in app classes |
| A6 | Does account deletion clear the local Firebase user? | `NOT_RECOVERED` | `AccountDeleteWork` referenced by `account.a.c()` | read `AccountDeleteWork.doWork` |
| A7 | Which `ri.b`-annotated endpoints exist? | `PARTIALLY_CLOSED` | annotation `ri.b` proven; per-service annotation sites not enumerated | scan service interfaces for the annotation |
| A8 | Does the WebView bridge expose any other JS interface name besides the proven dispatch method? | `NOT_RECOVERED` | `addJavascriptInterface` site proven; the interface object name/JS surface not read | read `lesson-webview.js` (asset not yet decoded) |
| A9 | What are the `kind` values flowing from the lesson page? | `NOT_RECOVERED` | only the four JSON keys are proven | read the JS asset, or the Kotlin handler beyond key parsing |
| A10 | Is `f9.j`'s tag-17 branch part of the app or library code? | `GENUINELY_UNKNOWN` | merged class; constants come from `m50.*` which are not app types | trace the constructor call site that passes tag 17 |

None of these replaces an existing question; all are additive and cited by the phase that raised them.

## Questions raised by Stage 2 (content delivery)

| ID | Question | Status | Evidence so far |
|---|---|---|---|
| A11 | is `getPublishSetVersion` compared with a stored value anywhere? | open | repository accessor `tracks.c.c()J` reads the cached bundle; no comparison site found |
| A12 | does a missing locale fall back to `en`? | open | `ye.b` derives the base from `"lessons-"` + locale with no observed branch |
| A13 | are content stream/parse failures caught, and where? | open | no handler on the `ye.b` stream path in Phase 2 |
| A14 | what are the two extra JSON documents in `id`, `it`, `pl`, `tr` (1,032 vs 1,030)? | open | corpus statistics only |

## Questions raised by Stage 3 (lesson engine)

| ID | Question | Status | Blocker |
|---|---|---|---|
| A15 | which module owns `<output>` | open | variant field names obfuscated |
| A16 | does a chapter auto-complete on its last lesson? | open | needs `U`/`V` bodies |
| A17 | meaning of the five boolean flags in `InteractiveLessonBaseViewModel` | open | needs `O` (616 insns) read |
| A18 | is `base.c.K` `initialiseCodeBlocks` or `storeLessonProgressInMemory`? | open | two families, one method |
| A19 | recovered name of `base.c.O` | open | no lambda family maps to it |
| A20 | is `hardModeLessonModules` parsed from the same document? | open | one grammar only in parser pools |

## Questions raised by Stage 4 (interaction engine)

| ID | Question | Status | Blocker |
|---|---|---|---|
| A21 | do `WRONG`-gated modules also render after a partial verdict? | open | partial emits `jm.n`, not `jm.o` |
| A22 | meaning of the six `jm.o` booleans (hint / solution / retry / AI tutor) | open | argument order not recoverable from the constructor |
| A23 | which types use `mm.b.E0` pass-through grading | open | `E0` state flow contents not read |
| A24 | duration of the delay before verdict dispatch | open | `kotlinx.coroutines.a.g` call constant |
| A25 | can executable lessons produce a partial verdict? | open | `qm.f` has one construction site |
| A26 | who produces `Output.ConsoleOutput` in the interactive branch | open | no producer found |
| A27 | which composable consumes `browserOutputDeferred` | open | UI layer, Phase 11 |
| A28 | what selects MultipleChoice vs SingleChoice | open | two state holders, same predicate |
