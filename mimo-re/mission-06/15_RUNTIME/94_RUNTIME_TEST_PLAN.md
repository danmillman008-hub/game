# Mission 6 — Runtime Test Plan

## Status: **BLOCKED** — no device/emulator/account is available in this environment.

The plan below is complete and source-derived: each test states the expectation computed from code, so it
can be executed later without re-deriving anything. No test in this document has been executed, and none
of the mission's claims are upgraded to `VERIFIED_RUNTIME`.

## Prerequisites (all missing)
| # | Requirement | Status |
|---|---|---|
| P1 | Android device or emulator | **BLOCKED** — no `adb`, no `emulator`, no x86/x86_64 native libs in the APK (`arm64-v8a`, `armeabi-v7a` only) |
| P2 | An authorized account | **BLOCKED** — none provided; RULE 3 forbids using others' accounts |
| P3 | Network access to `api.mimo.org` from the test device | **BLOCKED** — outbound access here is limited to package registries/GitHub |
| P4 | A **stock** Mimo 9.35 build | **BLOCKED** — only a third-party re-signed artifacts exists (`91_INTEGRITY_AND_TAMPERING.md`); results from it would not be attributable to Mimo |
| P5 | Instrumentation harness (Espresso/UIAutomator) | **BLOCKED** — would require building an APK without mutating source (allowed only as a separate test module, not permitted by RULE 2/no-mutation) |

## Test matrix (excerpt; full list in `96_TEST_TO_SOURCE_MATRIX.csv`)
| ID | Test | Source-derived expectation | Evidence ref |
|---|---|---|---|
| T-01 | wrong answer once, then correct, then next lesson | progress row `tries=1, attempts=2`; first-try = false | Phase 3.21, 4.26 |
| T-02 | correct answer with different quotes/case | accepted as CORRECT (normalisation) | 4.30 |
| T-03 | answer with `_` removed | accepted (false positive) | 4.30 |
| T-04 | open lesson then leave | row with `tries=0, attempts=0` | 3.21 |
| T-05 | offline lesson completion | row stays `in_queue=1`, no crash | 6.46 |
| T-06 | reconnect + push | row deleted, `reachedGoal` honoured | 6.44 |
| T-07 | executable lesson offline | hard failure (no local interpreter) | 3.23 |
| T-08 | AI tutor reply | SSE events, `finishReason=Stop` | 8.57 |
| T-09 | lesson with `<webview interaction=…>` | webview module renders, allowlist unknown | 14.90 |
| T-10 | restart lesson after solving | `lesson_reset` emitted; row effect unknown | 4.28 |
| T-11 | dark mode toggle | unknown (tokens blocked) | 10.74 |
| T-12 | deep link `https://getmimo.com/<path>` | routes via MainActivity, grammar unknown | 9.65 |

## Exit criteria for unblocking
P1+P2+P3+P4 satisfied → run T-01…T-12 with logcat + capture; only then, and not before, may a claim be
relabelled — no claim in this mission is `VERIFIED_RUNTIME` today.
