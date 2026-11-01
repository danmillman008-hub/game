# Mission 7 — Remaining Unknown Behaviours

| # | Behaviour | Why it is still unknown | What would close it |
|---|---|---|---|
| 1 | exact login/registration payload | auth repository not decompiled | targeted decompile of auth package |
| 2 | token storage backend (plain vs encrypted prefs) | `ri.*` bodies not recovered | decompile `ri.a/ri.c` bodies |
| 3 | websocket run message schema | `pg.a.onMessage` not readable | decompile message classes |
| 4 | Rive ↔ state binding | UI layer not in any batch | decompile `.riv` consumers |
| 5 | Pusher channels/events | constructed at runtime | decompile channel classes |
| 6 | notification → route mapping | route grammar not recovered | decompile MainActivity URI handling |
| 7 | unknown-tag behaviour in the parser | else-branch unreadable | bytecode-level inspection of `te.c.b` |
| 8 | progress push trigger | no worker/scheduler found | lifecycle trace or runtime |
| 9 | `a0()` effect on persisted row | repository call arguments unreadable | decompile repository |
| 10 | webview allowlist / bridge | webview consumer not recovered | decompile webview UI |
| 11 | AB-group → feature effect | consumers unknown | decompile flag readers |
| 12 | quota threshold / reset | server-side | server contract |
| 13 | leaderboard gating matrix | paywall VM not decompiled | decompile paywall |
