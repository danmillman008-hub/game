# Mission 6 — AI Tutor Persistence

## Scope
Where conversations live between sessions.

## Method
Room schema (3 tables), local data source for tutor (`data.source.local.aitutor.a`), search for message
tables/preferences.

## Findings (VERIFIED_STATIC)
1. **No tutor table exists in Room.** The local source class `data.source.local.aitutor.a` does not touch a
   DAO — it wraps the network/repository.
2. Conversations therefore persist **server-side only**, keyed by `conversationId`.
3. No transcript cache in preferences was found.
4. Consequence: opening the tutor offline yields nothing; there is no local history.

## Evidence labels
1, 2 **VERIFIED_STATIC**; 4 **INFERRED_HIGH**.

## Open questions
`Q-101` whether a "resume conversation" GET exists (none in the catalogue).

## Reproduction
`sed -n '1,60p' /tmp/dad/com.getmimo.data.source.local.aitutor.a.java`
