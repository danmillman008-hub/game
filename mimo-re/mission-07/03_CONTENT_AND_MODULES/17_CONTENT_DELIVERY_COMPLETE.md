# Mission 7 — Content Delivery (complete)

| Channel | Payload | Evidence | Label |
|---|---|---|---|
| bundled assets | English lesson JSON ({10327:,} files) | asset census | VERIFIED_STATIC |
| Play dynamic module | locale content packs | manifest meta-data | VERIFIED_STATIC (names) |
| HTTP zip | `GET /v1/package/preview` (`application/zip`) | API catalogue | VERIFIED_STATIC |
| HTTP structure | track completion / ETA / tutorial content | API catalogue | VERIFIED_STATIC |
| local content cache | **absent** (Room = 3 progress tables) | schema | VERIFIED_STATIC |

## Runtime sequence
```
tracks list   ← TracksJson (assets or module) + GET /v1/tracks/{id}/completion
lesson open   ← lesson document → te.c.b dispatch → AST → renderer
lesson finish ← POST /v1/tutorials/{tutorialId}/progress
```

## Trust boundary
No signature/checksum verification of content was recovered; content is trusted once delivered
(defensive observation, not an exploit).
