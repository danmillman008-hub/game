# Mission 7 — Pusher Architecture

## Presence (VERIFIED_STATIC)
`f9.j` constructs a Pusher client reading the API host and performing channel authorisation through the API.
`com.pusher.client.*` (16 classes) is decompiled and available.

## Unknowns
| Item | Status |
|---|---|
| channel names | NOT_RECOVERED (constructed at runtime) |
| event names | NOT_RECOVERED |
| payload schema | NOT_RECOVERED |
| subscribing UI component | NOT_RECOVERED |
| reconnect policy | SDK default (Pusher client) |
| why realtime is needed at all | UNKNOWN — no product feature recovered that requires push-driven state |

## Assessment (INFERRED)
Because nothing in the lesson/progress path consumes realtime events, Pusher most plausibly serves
social/notification-ish updates (leaderboard or streak changes). This is **not** asserted as fact; it is recorded
as an open question with a hypothesis.
