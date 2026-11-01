# Mission 7 — End-to-End Behavioural Reconstruction

Format per flow: **entry → caller → method → data → callee → state change → side effect → output → persistence →
result**, with unresolved links marked `[UNRESOLVED]`.

## 1. Application startup
process → `bin.ghost.YRF` → `com.getmimo.App` → `ae.m.<init>` (127 arms) → analytics singleton (Firebase/Adjust/
FCM/AB groups) → OkHttp (case 20) → HttpUrl (case 22) → Room → `MainActivity` → onboarding or home.
State: graph built. Side effects: SDK init, network token fetch, attribution. Result: app usable. **[VERIFIED_STATIC]**

## 2–3. Authentication
UI → auth repository **[UNRESOLVED: payload]** → endpoint among the 9 unauthenticated → token stored in `ri.*`.
Later calls carry `Authorization: Bearer`. No refresh. **[PARTIALLY_CLOSED]**

## 4–6. Home / path loading
home VM → content repository → `TracksJson` from assets/module + `GET /v1/tracks/{id}/completion` →
`lastInteractedTutorialId` positions the learner. **[VERIFIED_STATIC for shapes]**

## 7. Locale module installation
content UI → Play SplitInstall **[trigger UNRESOLVED]** → module assets → lessons available. **[PARTIAL]**

## 8–10. Lesson open → parse → render
fragment → `te.c.b` (dispatch on tag) → `te.a/d/e/f/g/b` → `LessonModule*` models → `base.c` state → renderer
(spans / `PartiallyEditableEditText` / WebView). During init `H(0,0)` writes an empty progress row.
**[VERIFIED_STATIC]**

## 11–13. Interactions
- multiple-choice = `SELECTION` items or `FILL_THE_GAP` options → tap → `base.c.Z` → verdict by option identity.
- fill-the-gap = same path, options rendered as chips with style spans.
- free text = `VALIDATED_INPUT` → 300 ms delay → `qm.i` two-phase compare.
**[VERIFIED_STATIC]**

## 14. Code execution
editor → `POST /v1/code/runfiles` (or WSS) → `ExecuteFilesResponse` → console + `hasPassed` → progress write.
**[VERIFIED_STATIC for contract; UI binding INFERRED]**

## 15–17. Verdicts
incorrect → `X()` → wrong paragraph; correct → `V()` → proceed; normalised → `W()` → input overwritten.
**[VERIFIED_STATIC]**

## 18. Hint request
**Does not exist.** No hint state, field, event, or endpoint. **[CLOSED_STATIC — absence]**

## 19. Retry
re-submit, `attempts++`, unlimited. **[VERIFIED_STATIC]**

## 20. Lesson completion
`U()` → `tries` computed → progress row written → navigation to next lesson **[UNRESOLVED: navigation call]**.

## 21. Progress sync
dirty rows → batch POST → delete on 2xx → `reachedGoal` displayed. **[VERIFIED_STATIC]**

## 22. XP update
**Does not exist** — no XP model. **[CLOSED_STATIC — absence]**

## 23. Streak update
server-side; client displays `activeStreak`/`longestStreak`. **[VERIFIED_STATIC for display; BACKEND_ONLY for logic]**

## 24. League update
server reports `league`/`newLeague`/`usedLeagueFreeze` in the leaderboard payload. **[VERIFIED_STATIC for payload]**

## 25–26. AI tutor question and streaming
interactor builds `SystemMessage`/`UserMessage` (prompt text from `Resources`) → `POST /v1/aiTutor/conversations`
with `Accept: text/event-stream` → frames append content → `finishReason` ends. No local persistence.
**[VERIFIED_STATIC]**

## 27. Code-run WebSocket
`wss://api.mimo.org/v1/run/socket` + `Sec-WebSocket-Protocol: authorization.bearer.<token>`; frames consumed by
`pg.a` **[message schema UNRESOLVED]**.

## 28–30. Subscription check → paywall → restore
RevenueCat `CustomerInfo` → `PublicUser.isPremium` → paywall surfaces; restore via RevenueCat. Coin products and
remote discount themes are separate. **[VERIFIED_STATIC for chain; INFERRED for call order]**

## 31. Remote configuration update
analytics init: `fetchAndActivate()` → AB-test groups held in the singleton; failure logged, defaults used.
Consumers **[UNRESOLVED]**.

## 32. Notification reception
FCM service → `MainActivity` intent → route **[UNRESOLVED: mapping]**.

## 33. Offline lesson attempt
`hg.e` throws before dialling; lesson still parses/renders/grades; progress queued. **[VERIFIED_STATIC]**

## 34. Sync recovery
next live push cycle sends queued rows; no scheduler exists. **[VERIFIED_STATIC for mechanism; trigger UNRESOLVED]**

## 35. App restart / state restoration
Room rows survive; lesson VM state is lost; reopening a lesson writes `H(0,0)` again. **[VERIFIED_STATIC]**
