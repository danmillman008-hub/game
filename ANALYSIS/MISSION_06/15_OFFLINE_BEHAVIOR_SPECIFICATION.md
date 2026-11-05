# MISSION 06 — DEEP CLIENT REVERSE ENGINEERING

**APK:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (unchanged) · `SERVER CONFIRMED = 0` · classification on every finding.

---

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
