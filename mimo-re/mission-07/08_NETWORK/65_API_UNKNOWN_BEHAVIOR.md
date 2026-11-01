# Mission 7 — API Unknown Behaviour

| # | Question | Status | What would close it |
|---|---|---|---|
| 1 | pagination for any list endpoint | UNKNOWN (no cursor/page DTO) | server contract or a large-list runtime test |
| 2 | error DTO shape | NOT_RECOVERED (no error type) | decompile the envelope consumer |
| 3 | 4xx semantics per endpoint | UNKNOWN | server contract |
| 4 | whether `progressList` can span tutorials | UNKNOWN (`tutorialId` is in the path) | runtime capture |
| 5 | live vs test host switch flag | PARTIALLY (case 22 branch; flag source unknown) | decompile the flag provider |
| 6 | rate limiting / retry-after | NOT_RECOVERED | runtime |
| 7 | keys endpoint verbs | PARTIALLY (repository exists, interface not read) | decompile keys interface |
| 8 | AI tutor continuation semantics without conversationId | UNKNOWN | runtime |
