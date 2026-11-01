# 02 — SPEC: content model (normative)

Sources: `data/content_schema.json` (JSON-Schema), `mimo-re/complete-extraction/04_CONTENT_MODEL/`,
`mimo-re/mission-06/evidence/CONTENT_MODEL_FIELDS.json`, `mimo-re/mission-08/02_CONTENT_DELIVERY/`.
Confidence: `VERIFIED_STATIC` for every field below (structure read from the model classes and the shipped corpus).

## 1. Layout on disk

```text
assets/lessons-<locale>/tracks/tracks.json          pack manifest
assets/lessons-<locale>/tracks/tutorial-<id>.json   one tutorial per file
assets/lessons-<locale>/<other assets>              images, webview html, etc.
```

`<locale>` ∈ {en, ru, pt, fr, es, id, it, pl, tr, +1}. Documents per pack: 1,030 (four packs carry 1,032).

## 2. Manifest — `TracksJson`

| Field | Type | Meaning |
|---|---|---|
| `publishSetVersion` | int | content baseline; **753** in the shipped pack |
| `tracks` | `Track[]` | the catalogue |

## 3. Track

| Field | Type | Notes |
|---|---|---|
| `id` | int | track identity |
| `version` | int | sent to the completion endpoint |
| `title` / `name` | string | display |
| `sections` | `Section[]` | ordered |

## 4. Section → Tutorial → Chapter → Lesson

| Entity | Key fields | Notes |
|---|---|---|
| `Section` | `index` (int), `name`, `description`, `tutorials[]`, `hasProgress` (lazy) | client renders **document order**; `index` is carried but not re-sorted (Q-27 closed) |
| `Tutorial` | `id` (int), `version` (int), `type` (`course` \| `practice` …), `chapters[]` | one JSON file per tutorial |
| `Chapter` | `id` (int), `type`, `lessons[]` | ordered |
| `Lesson` | `id` (int), `contentType` (`interactive` \| `executableFiles`), `interactiveContent` \| `executableContent` | body is a lesson document (§03) |

## 5. Identity

```text
LessonIdentifier = (trackId, trackVersion, tutorialId, chapterId, lessonId)   // 5 longs, navigation payload only
```

**The persisted learner key is different:** `(lessonId, tutorialId)` — `chapterId` is never stored (correction C-16).
An implementation that persists the five-part id will diverge from Mimo; see `12` (D-14 `KEEP_WITH_CHANGES`).

## 6. Versioning

* `publishSetVersion` is written into every progress row and sent in uploads; **no comparison exists anywhere**
  (A11 closed negative). A content update never invalidates local state in Mimo.
* `tutorialVersion` is per tutorial and travels in the upload payload.
* The API host is unrelated to content versions.

## 7. Locales and fallback

Ten packs ship in the APK; the in-code `ContentLocale` enum has five values, i.e. the enum is a subset (Q-14 closed).
The asset path is `"lessons-" + locale`; **no fallback branch to `en` was ever observed** (A12 partially closed).
→ For your implementation: `ADD-07` requires an explicit fallback chain.

## 8. Conformance rules for a content pack fed to the engine

1. `tracks.json` must carry `publishSetVersion` and a non-empty `tracks` array.
2. Every `tutorial.id` referenced by a section must have `tutorial-<id>.json`.
3. `section.index` must be unique within a track; rendering order is array order.
4. Lesson bodies must validate against `data/dsl_grammar.ebnf` (§03).
5. Unknown JSON keys: Mimo tolerates or rejects them depending on the `Json` configuration, which was **not**
   recovered (A-05). Your engine must choose and document one policy.
