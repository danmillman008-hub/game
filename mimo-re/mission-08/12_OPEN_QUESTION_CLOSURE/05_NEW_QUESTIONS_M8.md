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
