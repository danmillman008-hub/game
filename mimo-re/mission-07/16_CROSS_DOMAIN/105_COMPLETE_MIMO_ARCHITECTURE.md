# Mission 7 — Complete Mimo Architecture (integrated model)

This is the single model that connects every subsystem Mission 4–7 recovered. Every edge below is backed by a
file in this mission or in Mission 6 (`112_END_TO_END_EXECUTION_PATHS.md` names the evidence per flow).

```
PROCESS
 └─ bin.ghost.YRF (base Application) → com.getmimo.App
     └─ DI graph ae.m (127 eager arms)
         ├─ analytics singleton (case 1): FirebaseAnalytics · Adjust · FCM token · Remote Config AB groups
         ├─ OkHttp clients (case 20): hg.e → fh.b → fh.a [+ Bearer]
         ├─ HttpUrl (case 22): api.mimo.org | api-testing.mimo.org
         ├─ Room (3 tables: lesson_progress, chapter_completions, tutorial_completions)
         └─ repositories / interactors
             ├─ auth/token holder (ri.*)
             ├─ content repos (bundled assets + Play modules)
             ├─ progress repo (outbox)
             ├─ AI tutor repo (SSE)
             ├─ code repo (REST runfiles + WSS run socket)
             ├─ keys repo (consumeUserKey)
             ├─ leaderboard/streak/coins repos (display-only)
             └─ purchase (RevenueCat)
     └─ MainActivity (12 deep links) → onboarding (17 fragments) → home/learning path
         └─ track → section → tutorial → chapter → lesson
             ├─ INTERACTIVE: lesson doc → te.* parsers → AST → base.c state
             │     → fragment render (span composition / PartiallyEditableEditText)
             │     → user input → qm.d verdict (qm.i grader) → feedback paragraphs
             │     → H(tries,attempts) → Room(in_queue=1) → batch push POST /v1/tutorials/{id}/progress
             │     → analytics ge.j events → com.getmimo.analytics.a → Firebase/Adjust
             └─ EXECUTABLE: payload(files, solvedContent) → editor → POST /v1/code/runfiles | WSS
                   → ExecuteFilesResponse{consoleOutput,error,hasPassed,hostedProjectUrl,tests} → verdict
```

## The seven load-bearing conclusions
1. **Content is data.** No content code, no content table: 7 parsers + 6 module kinds + 4 interactions.
2. **Grading is client-side except for code runs.** Two-phase string comparison with an ASCII-only normaliser.
3. **Progress is a local outbox asserted upward.** No merge, no idempotency key, no scheduler.
4. **The economy is server-authoritative.** Coins/keys/streaks/leagues/ETA are displayed, never computed.
5. **DI is a hand-written 127-arm switch** — architecture, not framework.
6. **Analytics is a typed subsystem** with a full payload recovered for `lesson_reset` and 13 more events.
7. **Failure handling is deliberately minimal**: fail fast offline, retry only the outbox, log-and-continue for
   remote config.

## Cross-domain coupling points (evidence-backed)
| Coupling | Direction | Evidence |
|---|---|---|
| content version → progress row | write | `publish_set_version` column |
| progress → economy reward | server response | `PostProgressResponse{reachedGoal,dailyGoalCoinReward}` |
| lesson → analytics | per verdict | `f0`, `a0` |
| lesson → AI tutor | context objects | `SystemMessage$*`, `UserMessage$*` |
| session token → HTTP + WSS + Pusher | auth | `fh.a`, `pg.a`, `f9.j` |
| AB groups → feature behaviour | indirect | analytics singleton holds them (`Q-118` open) |
