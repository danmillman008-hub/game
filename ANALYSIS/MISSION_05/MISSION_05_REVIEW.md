# MISSION 05 — FINAL REVIEW: Offline Architecture Reconstruction

**Target:** original Mimo Android 9.35 (`com.getmimo`, `versionName=9.35`,
`versionCode=1792759685`).
**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`,
142,353,499 bytes — **unchanged**, re-verified read-only on every runner.
**Branch:** `arena/aebb90b7-game`.
**`SERVER CONFIRMED = 0`** — no backend reconstruction, no response bodies
observed or fabricated, no account, no credentials, no auth bypass, no root /
private-DB extraction, no APK/DEX/resource/manifest/signature modification.

---

## 1. Mission objective and outcome

> Reconstruct the **actual internal architecture and behaviour** of the Mimo 9.35
> *client*, with the ultimate goal of a fully functional offline application —
> faithfully, not by redesign.

**Outcome: reconstruction delivered.** The complete shipped curriculum, the
answer-validation contract, the local persistence schema, the onboarding →
lesson state machine, the offline dependency split, and the native-library
responsibilities are now documented with explicit evidence labels. M05 also
produced **five real emulator runs**, including a full 24-tap journey from the
launcher to a real interactive lesson and a network-isolated cold start that
reached the learning path and an executable lesson.

The single decisive finding, now **`VERIFIED_BOTH`**:

> **Mimo 9.35 already ships everything needed for the learning loop inside the
> APK.** The running client renders those exact asset bytes, evaluates answers
> locally, and stores progress locally. The network is needed for the economy,
> sync, account, code-execution service and remote config — not for the
> curriculum or the correct/wrong decision.

---

## 2. Deliverables (all under `ANALYSIS/MISSION_05/`)

| # | Deliverable | What it contains |
|--:|---|---|
| 1 | `00_EXECUTION_PLAN.md` | short concrete plan, based on the real remaining unknowns |
| 2 | `OFFLINE_ARCHITECTURE.md` | reconstructed layer map, data flows, offline boundary, confidence summary |
| 3 | `CONTENT_MODEL.md` | full curriculum object graph, DSL, exercise types, answer keys, shipped-vs-dynamic split, static↔runtime matches |
| 4 | `APPLICATION_STATE_MACHINE.md` | screen inventory, transitions, onboarding lifecycle, lesson lifecycle, resume |
| 5 | `LEARNING_ENGINE.md` | evaluation, scoring, XP/sparks/coins/keys, streaks, daily goals, completion, local state updates |
| 6 | `OFFLINE_DEPENDENCY_MATRIX.md` | 32-feature matrix with all 7 required columns + 4,257 external URL inventory |
| 7 | `LOCAL_STORAGE_MODEL.md` | exact Room SQL, entities, DAO operations, DataStore, outbox, resume |
| 8 | `NATIVE_LIBRARIES.md` | six `.so` purposes with JNI symbol evidence and real call sites |
| 9 | `EVIDENCE_DATABASE.json` | 112 classified findings; appended to `ANALYSIS/EVIDENCE_INDEX.json` as `mission_05_append` (M01–M04's 336 entries untouched) |
| 10 | `DIAGRAMS/` | `architecture.mmd`, `content_data_flow.mmd`, `application_state_machine.mmd`, `lesson_flow.mmd` + README |
| 11 | `OPEN_QUESTIONS.md` | 17 unresolved items, each with known evidence, exact missing information and a concrete next experiment |
| 12 | `SCHEMAS/` | `SHIPPED_CONTENT_STATS.json`, `CONTENT_SCHEMA.json`, `JADX_MODEL_FIELDS.json` |
| 13 | `SAMPLES/` | 14+ verbatim shipped assets (tracks.json, DSL lessons, executable lesson, WebView bridge JS, runtime-matched lessons) |
| 14 | `EVIDENCE/` | asset manifest with SHA-256, DEX string offsets, Room SQL, storage/onboarding strings, runtime↔static match proof |
| 15 | `RUNTIME/` | per-run findings for `42002808217`, `42003884423`, `42005358012`, `42006697783` |
| 16 | `../RUNTIME/MISSION_05/` | original PNG/XML/logcat/traces and verbatim archives of each run |

Every finding is labelled `VERIFIED_STATIC`, `VERIFIED_RUNTIME`,
`VERIFIED_BOTH`, `INFERRED`, or `UNKNOWN`. No inference is presented as fact.

---

## 3. Verified results, condensed

### 3.1 Shipped content — `VERIFIED_STATIC` (+ `VERIFIED_BOTH` for rendering)

- `assets/lessons-<10 locales>/tracks/` → **10,298** tutorial JSON files; root
  `tracks.json` has `publishSetVersion=753`.
- English: **19 tracks / 144 sections / 2,002 tutorial refs / 1,029 tutorial
  files / 1,947 chapters / 18,272 lessons**, 0 duplicate lesson IDs.
  All 144 section ranges are consistent.
- `contentType`: `interactive` 14,248 / `executableFiles` 4,024.
  DSL: `fillTheGap` 9,957, `validatedInput` 1,772, `<selection>` 7,356,
  `<webview>` 930. `visible-if`: wrong 19,101 / always 18,869 / correct 173.
- **Answer keys are shipped**: `correct="true|false"`, `startIndex/endIndex`
  ranges into `<content>`, `files[].solvedContent`, `visible-if` feedback text.
- `assets/lesson-webview.js` relays `mimo.activity.correct / wrong / completed`
  from in-WebView JS to the native client — evaluation is on-device.
- **Five shipped assets were matched with the running UI** (`VERIFIED_BOTH`):
  `tutorial-904.json` lesson 151403 ("Guess the letter" WebView),
  `tutorial-2199.json` lesson 63259 (offline executable HTML lesson),
  `tutorial-4648.json` lesson 152473 and `tutorial-4672.json` lessons
  152919/152920 (offline AI/ChatGPT lessons), and `tracks.json` track 274
  ("Automating Tasks with AI") as an offline path header.
  `EVIDENCE/RUNTIME_STATIC_MATCH.json`. Inline `<strong>` markup splits prose in
  the DSL, so naive full-string search misses some matches — these are **not**
  dynamic content.
- **Gap:** 4,257 external URL references (mimo.app 2,282, fonts.googleapis.com
  180, demo APIs, CDNs) are **not** packaged — the main offline fidelity gap.

### 3.2 Local persistence — `VERIFIED_STATIC`

- Room DB `mimo.db` with three tables, exact `CREATE TABLE` recovered from
  `classes.dex` at `@2,183,130 / @2,183,344 / @2,183,790`:
  `lesson_progress` (11 columns, PK `(lesson_id, tutorial_id)`, `in_queue`
  outbox), `chapter_completions`, `tutorial_completions`.
- Full DAO SQL recovered (insert/update/select/delete/aggregate/migrations).
- `LessonProgress.isSolvedCorrectly()` = `attempts >= 1` (M02 bytecode).
- DataStore `user_preferences` / `.preferences_pb`, `SharedPreferencesMigration`,
  ~40 named accessors (hard mode, first-run flags, onboarding, path overview).
- `ChapterFinishedViewModel$handleOfflineState` / `$handleOnlineState` prove the
  client explicitly anticipates an offline chapter end.

### 3.3 Application state machine — `VERIFIED_RUNTIME`

Five GitHub Actions runs on the original APK:

| Run | Outcome |
|---|---|
| `41998643355` (M04, reused) | exact SHA, install, launch, clean onboarding "Change your career" |
| `42001925381` | M05 branch created; 0 taps — tap-picker bug recorded honestly |
| `42002808217` | 16 taps through onboarding; **offline cold start** with `Active default network: none`; `STEP-01/02/03.xml` byte-identical to `OFFLINE-01/02/03.xml` |
| `42003884423` | **24 taps from launcher to a real interactive lesson**; off-network cold start reached the learning path + an executable lesson; incorrect-answer probe in run 4 |
| `42005358012` | **wrong-answer state captured**: "Try again" (red), `Q` button disabled, retry available; `Continue` advanced to the next lesson |
| `42006697783` | final run: a different onboarding-answer set selected **track 274 "Automating Tasks with AI"**; offline AI/ChatGPT lessons rendered. The intended correct-answer probe found no quiz options — **correct-answer state remains `UNKNOWN`** (recorded honestly) |

`VERIFIED_RUNTIME` onboarding chain: intro carousel → Welcome → motive → goal →
reassurance → role → work → experience (`NONE/A LITTLE/A LOT`) → loading →
aspect → interest → **"Front-End Developer is the best choice for you!"** →
social proof → daily goal (**Casual 5 / Regular 10 / Serious 20 minutes**) →
reminder `09:45 AM` + Android notification permission → device reassurance →
`AuthenticationActivity` → shipped **`Skip`** → `MainActivity` →
`ChapterActivity` → real lesson. **No account is needed to reach the first
lesson.** `Skip` is a normal UI control of the original app, not an auth bypass.

Resume: an offline cold start after `am force-stop` resumed at
`AuthenticationActivity` with the chosen path — onboarding selections persisted
(`VERIFIED_RUNTIME`). Per-lesson resume remains `UNKNOWN`.

### 3.4 Offline behaviour — `VERIFIED_RUNTIME`

With `svc wifi disable` + `svc data disable` → `Active default network: none`:

- Cold start, intro slides, onboarding, path UI, chapter cards and **lesson
  content** all render; an executable practice lesson shows `index.html`,
  `Browser`, `Code Editor` and starting code.
- The learning path shows a red banner **"Connect to the internet to progress
  further"**, coins `200`, keys `∞`, streak `-`.
- Logcat: `UnknownHostException: cdp.customer.io` (analytics) and repeated
  `ConnectivityService.requestNetwork` by `com.getmimo`; **no FATAL**.
- ⇒ the client's own offline gate is the main obstacle, not missing content.
  Whether progression is truly blocked, whether code execution works offline,
  and what chapter-end does offline remain `UNKNOWN`.

### 3.5 Learning engine — verified vs unknown

- **Verified:** local answer keys; local correct/wrong decision; **wrong-answer
  "Try again" state at runtime** (wrong option disabled, retry available,
  `Continue` → next lesson); Room progress rows with `in_queue`;
  `visible-if` feedback; daily-goal levels; hard-mode alternate bodies (6,058).
  **Not verified:** the correct-answer state (run 5 selected a different path)
  — explicitly `UNKNOWN`.
- **`UNKNOWN` (explicitly not invented):** all scoring formulas (XP/sparks per
  lesson, `rewardMultiplier`, first-try bonus, streak break/repair, coin
  rewards), exact chapter/tutorial completion thresholds, the
  `validatedInput` token-index algorithm, the exact unlock rule, and the
  `ExecuteFilesResponse.tests[]` semantics.

### 3.6 Native libraries — `VERIFIED_STATIC` / `VERIFIED_RUNTIME`

`librive-android.so` (Rive animation), `libsigner.so` (Adjust native signer,
JNI `nSign`/`nOnResume`), `libdatastore_shared_counter.so` (DataStore JNI),
`libandroidx.graphics.path.so` (PathIterator), `libc++_shared.so` (C++ runtime),
`libyrf.so` (references `bin/ghost/YRF`, `MainActivity`, `Subscription$Type` —
purpose `INFERRED` as integrity helper, not claimed). Four load with `: ok` on
the x86_64 emulator via ARM translation. None is an offline blocker, and none
is claimed to handle scoring or curriculum storage.

---

## 4. Offline verdict

| Concern | Verdict |
|---|---|
| Curriculum, answer keys, feedback, hints, solved code | **Fully local** — no server reconstruction needed |
| Content rendering (Compose + WebView + shipped JS/CSS/fonts) | **Fully local** for the observed lessons; 4,257 external refs need a mirror |
| Progress persistence | **Room already exists** — do not invent a new DB |
| Answer evaluation & retry | **Local** (`VERIFIED_RUNTIME` wrong state) |
| Economy / streak / leaderboard / ETA / rewards | **Server-owned** — replace with local logic or omit |
| Code execution for 4,024 executable lessons | **Server-owned** — replace with a local runner |
| Auth / AI tutor / purchases / social | **Omit** for an offline clone |
| Client's own "Connect to the internet to progress further" gate | **Must be handled** — exact trigger `UNKNOWN` |

**A faithful offline client is achievable without reconstructing any server
business logic.** M05 deliberately stopped at reconstruction: no new database,
no app skeleton, no premature implementation, no redesign.

---

## 5. Discipline, preservation, and known limitations

- Original APK untouched; all M01–M04 deliverables, `mimo-ui/UPGRADE`, v12.5-fa,
  CATALOGS, `verify_upgrade.py`, MANIFEST/ZIP untouched. New work isolated under
  `ANALYSIS/MISSION_05/` and `ANALYSIS/RUNTIME/MISSION_05/`.
- Workflow: pinned action SHA, API 36, `pixel_7`, boot procedure, and the
  **one-line `script:`** preserved. M05 added an isolated branch to
  `runtime_smoke.sh` and a one-line conditional transfer step; M04 evidence is
  never overwritten (M05 writes to its own directory).
- Two temporary Drive chunks were restored and made link-readable for the
  runner, then their config file was deleted by the runner. No new original
  private Drive file was shared. The historical M04 token URL remains in public
  Git history — a documented residual risk, not resolved here.
- No fabricated evidence, no invented credentials, no fake server responses,
  no TLS/pinning bypass, no purchases, no root/private-DB extraction.
- Automation defects (run 1 tap-picker, run 2 subshell state / avoid-list, run 4
  pipe-consuming loop) are **recorded with their exact cause** and fixed, not
  hidden. Run 5's different path selection is also documented, with the
  resulting correct-answer gap left as `UNKNOWN` rather than inferred.
- `allowBackup=false` and no root ⇒ actual `mimo.db` / `user_preferences`
  file **contents** are `UNKNOWN`; all schema facts come from the APK's own SQL
  and decompiled classes.
- Runtime evidence comes only from GitHub Actions (local sandbox has no
  emulator/ADB/SDK/Java/KVM). `SERVER CONFIRMED = 0`.

---

## 6. Deliverable index / where to start

1. `OFFLINE_ARCHITECTURE.md` — the reconstructed system in one place.
2. `OFFLINE_DEPENDENCY_MATRIX.md` — what blocks offline operation.
3. `CONTENT_MODEL.md` — the curriculum and answer keys.
4. `APPLICATION_STATE_MACHINE.md` + `RUNTIME/RUN_42003884423_FINDINGS.md` — the
   observed UI journey.
5. `LOCAL_STORAGE_MODEL.md` + `LEARNING_ENGINE.md` — persistence and behaviour.
6. `OPEN_QUESTIONS.md` — the remaining unknowns, in priority order.
7. `EVIDENCE_DATABASE.json` — machine-readable, classified evidence.

`MISSION 05 — RECONSTRUCTION COMPLETE. SERVER CONFIRMED = 0.`
