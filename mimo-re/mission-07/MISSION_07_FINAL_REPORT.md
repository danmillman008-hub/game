# MISSION 7 — Mimo Complete Internal Structure

**Artifact**: `Mimo_9.35 (1).apk` — 142,353,499 B, sha256 `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`, 12 dex, 29,454 classes.
**Branch** `arena/ecb8af07-game` · **start commit** `3db0902528945c64a107ca7663d459b541d632b3` (Mission 6).
**Tests**: mission-07 15 passed · mission-06 21 · mission-05 44 · mission-04 23.
**Runtime claims: 0.** Every statement below is `VERIFIED_STATIC` unless labelled otherwise.

---

## I. What Mission 7 changed relative to Mission 6

| Gain | Detail | Document |
|---|---|---|
| Design tokens unlocked | manual ARSC decode → **1,198 colour keys + 1,401 dimen keys** with values and config variants | `12_UI_RESOURCES/77`, `78` |
| Analytics dispatch reconstructed | `com.getmimo.analytics.a` singleton: `FirebaseAnalytics.logEvent` via `e(String,Map)`, Adjust adid/attribution, FCM token, Remote-Config fetch; events are `ge.j(name,index)` + typed `NumberProperty/StringProperty` | `10_ANALYTICS_CONFIG/82`, `83` |
| Events with call sites | **14** events verified (`launch`, `open_lesson`, `finish_lesson`, `finish_tutorial`, `finish_track`, `lesson_reset`, `lesson_interaction_delete`, `login`, `login_manual_enter_password`, `facebook_like`, `get_help`, `open_privacy_policy`, `exit_free_trial_screen`, `onboarding_work_function_picked`) | `evidence/EVENTS_WITH_CALLSITES.csv` |
| Full `lesson_reset` payload | `lesson_id, tutorial_id, tutorial_version, track_id, attempts, duration` (7 properties) | `05_RUNTIME_AND_GRADING/31` |
| Tutor context model | typed `SystemMessage{Interactive,Executable}` + `UserMessage{Executable,InstantPrompt{ExplainError,ExplainInteractiveMistake}}`; prompt text comes from `Resources` | `09_STREAMING/67` |
| Feature flags | they are **Firebase Remote Config AB-test user groups** fetched during analytics init, not a flag matrix | `10_ANALYTICS_CONFIG/84` |
| Keys consumption | `DefaultKeysRepository.consumeUserKey` exists (supersedes "no decrement") | `07_STORAGE_AND_SYNC/49` |
| DSL closures | `NUMBER` is dead vocabulary; selections are single-answer (no `multiple` attribute) — both closed by corpus evidence over 1,030 documents | `04_DSL_PARSER_RENDERER/28` |

## II. The 50 required explanations (condensed, one paragraph each; details in the referenced files)

1. **Architecture** — five layers (presentation / interaction-domain / data / infrastructure / content-data), hand-wired DI, two lesson engines. `02_ARCHITECTURE_AND_DI/14`
2. **Startup** — `bin.ghost.YRF` → `com.getmimo.App` → `ae.m` (127 eager arms) → SDK init → `MainActivity`. `02/12`
3. **DI** — 127 cases, field-ordered, no scoping annotations, one graph per process, no defensive branch. `02/09`,`11`
4. **Packages/modules** — 1,563 app + 1,570 anonymous + 13,113 obfuscated app classes + 19 modified-base + 10,351 library. `01/01`
5. **Dynamic modules** — `content_de/es/fr/id/it`(+); contents not in the APK; base DEX owns all parsers/renderers. `03/16`
6. **Content hierarchy** — Track→Section→Tutorial(ids)→Chapter→Lesson→LessonContent→Module→Interaction. `03/18`
7. **Content delivery** — bundled English assets, Play modules per locale, zip preview endpoint, no content DB. `03/17`
8. **Content versioning** — `publishSetVersion` + `trackVersion` inside the 5-part lesson key, progress keyed on 2 parts. `03/19`
9. **DSL grammar** — 29 ordinals, 25 used tags, HTML-shaped names, full attribute set. `04/21`
10. **Parser architecture** — cursor-recursive per-module parsers, string-compare dispatch, hard structural vs soft semantic errors. `04/23`
11. **AST** — six module kinds, typed gap spans vs style spans, character offsets into `<content>`. `04/24`
12. **Rendering** — one scrollable lesson page, span composition + `PartiallyEditableEditText`, WebView modules, separate editor palette. `05/29`, `12/75`
13. **Lesson runtime** — init→render→act→submit→verdict→write→feedback→analytics→proceed→push. `05/31`
14. **Interaction engine** — exactly four kinds, no drag/order/multi-select. `06/36`
15. **Grading** — client-side for interactives (option identity; exact→normalised for free text), server-side for code runs. `06/37`,`38`
16. **Feedback** — authored `visible-if` paragraphs, canonical-answer overwrite on near-miss, no reveal on failure. `06/42`
17. **Executable lessons** — payload includes `solvedContent`; REST `runfiles` + WSS run socket; `hasPassed` drives verdict. `05/34`
18. **Learner model** — server profile/economy + local progress rows; nothing else. `07/44`
19. **Learning paths** — authored order, chapter difficulty tiers, hard mode, server pacing; no adaptation engine. `07/46`
20. **Progress calculations** — counters only; first-try is derived; completion separated from correctness. `07/45`,`47`
21. **Gamification** — coins, keys (consumable), daily goal, streaks, leagues/sparks/freeze, boards; **no XP**. `07/49`
22. **Local database** — 3 tables, no migrations, insert-not-update. `07/52`
23. **Persistence** — progress + prefs + SDK stores; no content/profile cache. `07/51`,`53`
24. **Synchronisation** — per-tutorial batch push, delete-on-2xx, no idempotency, no scheduler. `07/55`
25. **Networking** — OkHttp 20/30 s with three interceptors, Retrofit, `d70.b` envelope, no retry/pinning/cache. `08/58`
26. **Authentication** — Bearer from `ri.*`; no refresh, no 401 handling; login payload unrecovered. `08/62`,`13/89`
27. **WebSocket** — single listener `pg.a`, subprotocol auth, message schema unrecovered. `09/70`
28. **SSE** — POST + `Accept: text/event-stream`, `AiTutorConversationMessage`, `FinishReason`. `09/69`
29. **Pusher** — client + channel auth recovered; channels/events unrecovered. `09/71`
30. **AI Tutor** — typed context, quota display, no local transcript. `09/66`,`67`,`68`
31. **Navigation** — one deep-link activity, 17-fragment onboarding, lesson flow reachable from lists. `12/73`
32. **UI components** — 4 lesson fragments, 2 custom views, Compose components, span copier. `12/74`
33. **Resources** — 21 type tables decoded incl. 1,531 layouts and 1,728 styles (counts only). `12/76`
34. **Design system** — Aeonik triad, two palettes, semantic+palette token layers with config variants. `12/77`
35. **Rive** — 59 assets, JNI runtime, **binding to state not recovered**. `12/80`
36. **Localization** — UI locale (resources) ≠ content locale (modules); ASCII-only normaliser is locale-blind. `14/98`,`100`
37. **Accessibility** — span-based gaps are the risk; no a11y config recovered. `12/81`
38. **Subscriptions** — RevenueCat → `isPremium`; coins as consumables; remote discount themes. `13/90`,`91`
39. **Remote configuration** — 3 defaults + AB groups, log-and-continue on failure. `10/84`
40. **Analytics** — singleton dispatcher, typed events, 14 verified events, Adjust/Sentry alongside. `10/82`,`83`
41. **Notifications** — FCM service + token in analytics init; routing unrecovered. `09/72`
42. **Background jobs** — **none app-owned**; outbox is foreground-only. `10/86`
43. **Native code** — 4 libs, 2 ABIs, JNI only for Rive/Adjust; no disassembly possible here. `11/93`,`95`
44. **External SDKs** — 10 SDK groups catalogued with integration point each. `11/96`
45. **Error handling** — `NoConnectionException` gate, envelope failures, Sentry, `AdjustTokenNotAvailableException`, log facade. `10/87`
46. **Offline behaviour** — lessons/grading/outbox work; economy/tutor/code runs fail; deterministic fast failure. `15/102`
47. **Complete data flow** — 11 typed flows (document→AST→verdict→row→push→response). `16/108`
48. **Complete call graph** — curated cross-domain edges + method-level graph over the decompiled subset. `16/106`,`107`
49. **End-to-end behaviour** — 35 flows reconstructed, hints/XP closed as absent. `17/113`,`114`
50. **Remaining limitations** — 11 unknown behaviours, 7 blocked investigations, 4 backend-only classes. `18/118`,`119`

## III. Open-question closure (inherited 39 items)
| Status | Count |
|---|---|
| `CLOSED_STATIC` | 17 |
| `PARTIALLY_CLOSED` | 12 |
| `BACKEND_ONLY` | 4 |
| `BLOCKED_BY_ENVIRONMENT` | 3 |
| `NOT_RECOVERED` | 3 |
| `GENUINELY_UNKNOWN` | 2 |

Full table with answers and evidence: `18_CLOSURE/116_MASTER_OPEN_QUESTION_CLOSURE.csv`;
narrative: `18_CLOSURE/117_CLOSED_FINDINGS.md`.

## IV. Corrections to earlier missions (recorded, never retro-edited)
1. **Q-102 was not blocked** — a manual ARSC parser recovers token values.
2. **Keys are consumable** — Mission 6's "no decrement path" is superseded.
3. **Analytics emitters are reachable** — `U-20` is partially closed, not unrecoverable.
4. **Tutor context exists as typed objects** — Mission 6's "two authored strings only" was a DTO-level view.
5. **`Q-42` multi-select** — no `multiple` attribute; single-answer selections.
6. **`Q-31` `NUMBER`** — dead vocabulary, corpus-confirmed.

## V. Read order
`00_BASELINE/CURRENT_WORKSPACE_STATUS.md` → `00_BASELINE/MISSION_04_05_06_RECONCILIATION.md` →
`02_ARCHITECTURE_AND_DI/14` → `04_DSL_PARSER_RENDERER/21` → `06_LEARNER_AND_GRADING/38` →
`07_STORAGE_AND_SYNC/55` → `16_CROSS_DOMAIN/105` → `17_END_TO_END/113` →
`21_AUDIT/135_FINAL_COMPLETENESS_REPORT.md` → `18_CLOSURE/118`, `119`.
