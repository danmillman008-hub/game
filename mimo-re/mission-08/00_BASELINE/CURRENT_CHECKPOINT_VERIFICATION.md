# Mission 8 — Checkpoint verification (re-entry)

**Verified:** 2026-11-01 · **Branch:** `arena/ecb8af07-game` · **HEAD:** `f78dccbf4083d7907682e40b5fd151a91d20cb61`
**Remote:** identical (`git ls-remote` returns the same SHA) · **Working tree:** clean at start of pass

This file re-establishes the checkpoint before any new investigation. Nothing below is copied from a stage
report; each number was recomputed in this pass.

## 1. Repository state

| Check | Result |
|---|---|
| repository root | `/home/user/game` |
| branch | `arena/ecb8af07-game` |
| HEAD | `f78dccb` (matches the reported checkpoint) |
| remote ref | `f78dccb` — in sync, no force-push, no rewrite |
| mission-04…07 modified? | **no** (untracked changes only under `mimo-re/mission-08/`) |

## 2. Delivered stages present

| Stage | Directory | Verified content |
|---|---|---|
| A | `00_BASELINE/` | 9 artefacts + INPUT_HASHES / TOOLS_AND_ENVIRONMENT added in this pass |
| B | `01_DEEP_CLASS_INVESTIGATION/` | 9 artefacts + evidence |
| C | `02_METHOD_RELATIONSHIPS/` | 7 documents + gzipped graph + focus extract |
| D | `05_AUTHENTICATION_CLOSURE/` | 6 documents + 2 evidence dumps |
| E | `12_OPEN_QUESTION_CLOSURE/`, `16_FINAL_AUDIT/` | 7 + 4 artefacts |
| — | stage reports | `STAGE_A_REPORT.md` … `STAGE_D_REPORT.md` present |

## 3. Registers (recomputed, not quoted)

| Register | Value |
|---|---|
| canonical questions | **39** — `CLOSED_STATIC 14 · PARTIALLY_CLOSED 11 · NOT_RECOVERED 7 · GENUINELY_UNKNOWN 3 · BACKEND_ONLY 2 · BLOCKED_BY_ENVIRONMENT 2` |
| canonical domains | **45** — `FULLY 24 · SUBSTANTIALLY 9 · PARTIALLY 7 · NOT_INVESTIGATED 5` |
| deep-investigation queue | **2,178** rows |
| typed call graph | **85,724** edges (85,725 CSV lines including header) |
| method register | **637** methods / **61** classes — `BEHAVIOUR_RECONSTRUCTED 9 · DEX_INSPECTED 44 · JAVA_INSPECTED 2 · BODY_PRESENT_NOT_READ 561 · SIGNATURE_ONLY 21` |
| runtime-verified | **0** |

## 4. Inherited suites (unmodified)

`complete-extraction` **23** · `mission-05` **44** · `mission-06` **21** · `mission-07` **15** — all green. No test
was edited, skipped or weakened. Details: `REGRESSION_TEST_RESULTS.md`.

## 5. Input hashes

`INPUT_HASHES.json` pins the APK, all 12 dex files, and the three derived inputs (`arsc_full.json`,
`strings_by_id.json`, `manifest.xml`). APK SHA-256 begins `48ce1740aa4b1f892a…`; dex set totals **28,836,088 bytes**.

## 6. New structural finding in this pass — the dex set is 4 real + 8 module stubs

| dex | bytes | classes | content |
|---|---|---|---|
| `classes.dex` | 16,237,920 | 12,944 | app + libraries |
| `classes2.dex` | 9,766,936 | 13,155 | app + libraries |
| `classes3.dex` | 2,802,944 | 3,318 | app + libraries |
| `classes12.dex` | 19,520 | 21 | `bin.ghost.*` |
| `classes4.dex` … `classes11.dex` | **1,096 each** | **2 each** | exactly `com.getmimo.data.content.<locale>.BuildConfig` + `.R` for **ru, pt, id, it, pl, fr, tr, es** |

Implications that must not be forgotten:

1. **The twelve-dex "universe" is really four dex plus eight single-module stubs.** Any future statement about
   "12 dex" must say this.
2. **Eight locale content modules exist as Play feature modules** whose only classes in the base APK are
   `BuildConfig` and `R`. The lesson content for those locales is *not* in the base APK — this is the mechanism
   behind Q-05 ("dynamic feature module contents absent"), now evidenced rather than assumed.
3. It also explains why `R`-lookups for those locales exist while no locale content classes do.

This finding is recorded as **C-12** in `HISTORICAL_FINDINGS_RECONCILIATION.md` (added this pass; it refines rather
than corrects Q-05, which stays `BLOCKED_BY_ENVIRONMENT` because the module payloads are still absent).

## 7. Phase status at the checkpoint

`CURRENT_STAGE_STATUS.json` lists all 25 brief phases with their state. Seven areas are *not started*: content
delivery, lesson engine, interaction/grading, learner model, persistence, AI tutor, executable lessons, UI/Rive,
background, analytics, subscriptions, localization, failure handling, coverage closure, end-to-end, testing,
runtime, architecture and final audit.

## 8. Re-entry decision

Continue with **Stage 1 — symbol and lambda recovery** (the brief's Phase 1), because every later phase consumes
it: content delivery, lesson engine and AI tutor all live in renamed classes.
