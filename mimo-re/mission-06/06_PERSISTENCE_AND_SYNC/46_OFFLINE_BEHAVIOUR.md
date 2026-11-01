# Mission 6 — Offline Behaviour

## Scope
What works, what fails, and what the learner sees without a connection.

## Method
Read of `hg.e` (offline interceptor), `fh.a`/`fh.b` (auth/UA), the lesson runtime, and the outbox design.

## Findings (VERIFIED_STATIC)
- Every HTTP request goes through application interceptors; `hg.e` checks connectivity first and throws
  `NoConnectionException` **before** the socket is touched.
- Lessons are bundled (Phase 2.11), so the parser and lesson runtime work offline; grading of interactive
  answers is local and therefore works offline.
- Progress accumulates in Room with `in_queue=1`.
- Executable lessons **cannot** run offline (`POST /v1/code/runfiles` / WSS) — the only lesson type that
  hard-fails.
- Coins/keys/streaks/leaderboards are unavailable offline; nothing is cached for them in Room.

## Evidence labels
Interceptor and bundling: **VERIFIED_STATIC**. "UI shows an offline banner" is **INFERRED** (string
resources for offline exist, but the screen was not traced).

## Open questions
`Q-74` offline banner screen; `Q-75` whether an offline attempt at an executable lesson is queued.

## Reproduction
`sed -n '1,80p' /tmp/dad/hg.e.java`
