# Mission 7 — Outbox and Sync (complete)

```
lesson event ──► LessonProgress row (in_queue=1)  [Room]
                        │
                        │ trigger (push cycle; exact trigger UNKNOWN, Q-70)
                        ▼
        SELECT WHERE in_queue=1 ──► PostProgressRequestBody{progressList}
                        │
                        ├─ 2xx ──► delete rows, read {reachedGoal, dailyGoalCoinReward}
                        └─ failure ──► rows retained unchanged (no retry counter, no backoff)
```

## Properties
| Property | Value | Evidence |
|---|---|---|
| batching | per tutorial (id in path) | endpoint |
| idempotency | none client-side (no client id/nonce) | DTO fields |
| retry | implicit only (row stays dirty) | `in_queue` |
| duplicate prevention | by row key, not by request | schema |
| process restart | rows survive; push resumes | Room |
| ordering | not enforced | no sequence column |
| acknowledgement | row deletion | repository |

## New in Mission 7
No WorkManager worker and no scheduler was recovered for progress push → the push is **not** guaranteed in the
background; it happens in a live process (trigger unknown, `Q-70` remains).
