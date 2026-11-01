# Mission 7 — Offline Behaviour (complete)

| Capability | Offline | Evidence |
|---|---|---|
| bundled lessons | works (parse + render + grade local) | assets + `te.*` + `qm.*` |
| installed locale module lessons | works | module assets |
| progress recording | works (Room, `in_queue=1`) | repository |
| progress push | deferred | outbox |
| executable lessons | **fail** (no interpreter, needs server) | no native runtime |
| AI tutor | fail | SSE |
| coins/keys/streaks/leaderboard | unavailable (nothing cached) | storage map |
| subscription state | depends on cached session/entitlement; no entitlement store | INFERRED_HIGH |
| analytics | SDK-buffered | SDK |
| animations | work (bundled) | assets |
| webview modules | work if content is inline; external links fail | `<webview content>` |

## Entry point of the offline path
`hg.e` throws `NoConnectionException` **before** DNS/socket, so every network call fails fast and deterministically;
the UI sees a normal failure envelope, not a timeout.
