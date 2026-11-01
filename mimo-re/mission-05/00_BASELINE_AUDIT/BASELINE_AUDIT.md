# Mission 5 — Baseline Audit (Phase 0)

## Scope
Establish the exact starting state before any new reverse engineering: repository commit, branch
sync state, prior-artifact integrity, test status, APK identity, and the list of historical claims
that must be re-validated rather than trusted.

## Method
`git rev-parse HEAD`, `git status --porcelain`, `git rev-list --count`, `git log -1`,
`git ls-remote`, `find | wc`, `md5sum`/`sha256sum` on the APK, `pytest -q` on the frozen
mission-04 suite. No file in `mimo-re/complete-extraction/` or `mimo-re/final/` was modified
(verified by `git status` after every phase).

## Sources (all local, all reproducible)
| Source | Identifier |
|---|---|
| Repository | `danmillman008-hub/game`, branch `arena/ecb8af07-game` |
| Starting commit | `9dbc278f07bd085f3da00e6012c7c412be358bf0` |
| Prior deliverable | `mimo-re/complete-extraction/` (399 files, 5.2 MB, frozen) |
| APK | `Mimo_9.35 (1).apk`, md5 `f9cef2d8029e59da3668ec1c18e21566`, sha256 `48ce1740…1e0f7c7a` |
| Package identity | `com.getmimo`, versionName `9.35`, versionCode `1792759685`, minSdk 28, targetSdk 36 |

## Findings
1. **Tree clean, branch in sync** at the start of the mission; `origin/arena/ecb8af07-game` == HEAD.
2. **Mission-04 test suite passes unchanged: 23 passed.** It is treated as a regression gate for
   every later phase (still green at mission end, plus the new mission-05 tests below).
3. **Prior artifacts intact.** `mimo-re/complete-extraction/` was read-only for this mission; all new
   output is confined to `mimo-re/mission-05/`. Two mission-04 artifacts were *superseded rather than
   edited*: the annotation dump and the API catalogue — both had defects (see `MISSION_05_REPORT.md`
   §corrections) and are replaced by `evidence/ANNOTATIONS_V2.csv` and `evidence/API_CATALOG_V2.csv`.
4. **History re-validation list** (each item re-checked in Phases 2–4, results in
   `22_FINAL_AUDIT/FINAL_AUDIT.md`):
   - the interactive-lesson parser is obfuscated (`te.a`–`te.g`), not `lessonparser`;
   - `tries` / `attempts` semantics in `lesson_progress`;
   - validated-input grading is case/whitespace-insensitive (or not);
   - HTTP verbs of the 62 annotated Retrofit methods;
   - response DTOs of those methods (previously UNKNOWN);
   - Room schema columns and primary keys;
   - "305 analytics events" and "137 Segment events";
   - native libraries present in the APK and their identity.

## Evidence labels
- Starting commit / clean tree / test result / APK hashes: **VERIFIED_STATIC** (command output).
- Runtime behaviour of the shipped app: **BLOCKED** (no device, no emulator, no adb in this
  environment — see `01_TOOLCHAIN_AND_ENVIRONMENT/`).

## Limitations
Baseline verification is a *filesystem and VCS* statement only. It says nothing about whether the
prior findings were correct; that is the subject of the rest of the mission.

## Unresolved
- Whether the APK under analysis is the exact build shipped to production at the same moment
  (versionCode 1792759685 is the only anchor). Labelled **INFERRED_HIGH**, not verified.

## Reproduction
```bash
git -C /home/user/game rev-parse HEAD          # 9dbc278f07bd085f3da00e6012c7c412be358bf0 (start)
git -C /home/user/game status --porcelain      # empty
md5sum "/tmp/apk/Mimo_9.35 (1).apk"            # f9cef2d8029e59da3668ec1c18e21566
cd mimo-re/complete-extraction/16_AUTOMATED_TESTS && python -m pytest -q   # 23 passed
```
