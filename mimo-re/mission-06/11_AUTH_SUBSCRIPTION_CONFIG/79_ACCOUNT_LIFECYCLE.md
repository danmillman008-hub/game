# Mission 6 — Account Lifecycle

## Scope
Sign-out, delete-account, reinstall and multi-device consequences visible to the client.

## Method
Endpoint catalogue (delete/account paths), Room schema, sync design (Phase 6.45).

## Findings
1. The catalogue contains account-related endpoints among the 62 (2 DELETE + others); the exact
   delete-account contract is **INFERRED_HIGH** from the path, not proven by a traced UI flow (`Q-123`).
2. On sign-out, local progress rows are the only learner data that could survive; whether they are cleared
   was not traced (`Q-124`).
3. Reinstall loses queued rows (no backup: `allowBackup=false`) — **VERIFIED_STATIC** consequence.
4. Multi-device conflicts are server-resolved, invisible to the client (Phase 6.45).

## Evidence labels
As marked.

## Open questions
`Q-123`, `Q-124`.

## Reproduction
`grep -iE 'delete|account|logout' ../mission-05/evidence/API_CATALOG_V2.csv | head`
