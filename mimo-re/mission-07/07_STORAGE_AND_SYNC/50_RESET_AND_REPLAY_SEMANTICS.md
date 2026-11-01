# Mission 7 — Reset and Replay

| Reset kind | Exists? | Implementation | Persistence effect |
|---|---|---|---|
| exercise retry | yes | re-submit, `attempts++` | row updated |
| lesson restart | yes | `a0()` clears state, emits `lesson_reset` | **UNKNOWN** for the existing row (`Q-08`) |
| lesson replay after completion | yes (open again) | normal init writes `H(tries,attempts)` | row overwritten (schema has no version key) |
| topic/chapter restart | not found | — | — |
| track restart | not found | — | — |
| account-level progress reset | not found | — | — |
| local cache purge | not found (no cache exists) | — | — |
| logout | token dropped (mechanism not recovered) | — | UNKNOWN whether rows are cleared (`Q-124`) |

## Reading
Replay is **non-destructive to counters by design**: because the row is keyed without version/time, a replay
overwrites rather than accumulates. There is no "best attempt" concept.
