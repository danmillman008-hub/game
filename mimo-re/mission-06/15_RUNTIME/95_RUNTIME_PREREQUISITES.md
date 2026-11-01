# Mission 6 — Runtime Prerequisites

## Environment reality (re-verified 2026-11-01)
```
java        : absent        jadx     : absent        apktool : absent
aapt2       : absent        adb      : absent        emulator: absent
python      : 3.11.2        androguard: 4.1.4        pytest  : 9.2.0
graphviz(dot): absent       mermaid-cli: absent
```
- The APK ships **only arm64-v8a and armeabi-v7a** native libraries → an x86_64 emulator image could not
  run it without translation layers, and no arm emulator is available.
- Outbound network is restricted to `github.com`, `codeload.github.com`, `api.github.com`,
  `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org` — the app's own API is unreachable, so even a
  working emulator could not complete login.
- No credentials exist and none may be requested.

## What *is* possible
- Static verification of every claim in this mission (done).
- Deterministic re-derivation via the mission-06 tools (`17_TOOLS/117_TOOLS.md`).
- Fixture-level semantic tests that exercise *source-derived algorithms* (grading normalisation, grammar
  acceptance, state transitions) without the app (Phase 19).

## What remains impossible here
Runtime observation, traffic inspection against the real backend, UI/a11y verification, performance
measurement. Each is recorded as `BLOCKED` with the missing prerequisite in P1–P5 of
`94_RUNTIME_TEST_PLAN.md`.
