# Mission 7 — Complete Local Persistence

## Write paths (VERIFIED_STATIC)
1. **Lesson open/verdict** → `base.c.H(tries,attempts)` → ProgressRepository → `lesson_progress` upsert with
   `in_queue=1`.
2. **Chapter/tutorial completion** → marker insert.
3. **Onboarding/remote config/FCM** → preferences.

## Read paths
1. Progress lookup by `(lesson_id, tutorial_id)`.
2. Pending batch `WHERE in_queue=1` before a push.
3. Onboarding flags at startup.

## Acknowledgements
Only one: the progress push. On 2xx the pushed rows are deleted; there is no other two-phase protocol in local
storage (no outbox for analytics — the SDK owns that queue).

## Nothing else
No user table, no content table, no session table, no analytics table, no migration table.
