# Phase 6 — Request/response models

## 1. Serialization

`he0.a.c(jx.d)` is the converter factory used by every app Retrofit instance; `jx.d` is the **kotlinx.serialization**
`Json`-backed converter (the same provider feeds all five Retrofit instances). Consequences:

* models are Kotlin `@Serializable` data classes with `$$serializer` companions (present in the class census);
* unknown keys are handled by the Json configuration in `jx.d`, which was **not** read → strictness is `UNKNOWN`
  (A-05);
* no Gson, Moshi, Jackson, or manual `JsonAdapter` in the recovered paths;
* there is **no** global `Result`/`Envelope<T>` wrapper: `d70.b` in signatures is `kotlin.coroutines.Continuation`
  (correction C-20). A failed call is an exception, not a value.

## 2. Request bodies (by endpoint family)

| Family | DTO | Notes |
|---|---|---|
| progress | `PostProgressRequestBody{ progressList: List<Progress> }` | `Progress` = 9 fields, **no** `tutorialId` (grouped per request) |
| code execution | `ExecuteFilesBody` → `ExecuteFilesResponse` | sync REST counterpart of the socket |
| saved code | `SavedCode…` request/response pairs (`Lmh/c;`, `Lih/a;`) | 5 endpoints |
| settings | `Settings…`, `ChangeEmailRequestBody`, avatar upload body | 4 endpoints |
| lessons | `SaveLesson…`, `LessonReport…` (`Ldh/a;`, `Lkh/a;`) | save + report |
| iap | `Product` request, `RawPurchasedProduct` response | 2 endpoints |
| customer.io | `CustomerIoData`, `AnalyticsEvent` | C4/C5 |
| preview | `ExecuteFiles`-shaped body on C3 | request type is shared with execution |

Full field-level schemas already exist and are not duplicated here:
`mission-07/08_NETWORK/61_REQUEST_RESPONSE_COMPLETE_SCHEMAS/` (10 JSON Schemas, e.g. `PostProgressRequestBody`,
`ExecuteFilesResponse`, `LastInteractedTrackResponse`, `Coins`, `LeaderboardUserResult`, `PublicUser`) and
`mission-06/50_REQUEST_RESPONSE_SCHEMAS/`.

## 3. Response shapes

| Shape | Where | Meaning |
|---|---|---|
| `Lz60/q;` | 20+ rows | Unit-like acknowledgement (`Unit`) |
| `Lge0/o0<…>` | 12 rows | `retrofit2.Response<T>` — callers inspect the status themselves |
| concrete DTO | the rest | direct body |
| `Lokhttp3/ResponseBody;` | 2 rows (`eh/a`, `og/a`) | raw stream (package preview, certificate download) |

The `Response<T>` rows are important: those call sites **do not** get exception-based error handling, they get an
inspectable status. Two error styles therefore coexist in the app (see `07_ERROR_RETRY_OFFLINE.md`).

## 4. Field-level conventions observed in the DTOs

* timestamps: ISO-8601 strings in DTOs, converted to `org.joda.time.Instant` at the Room boundary (Stage 5);
* ids: `Long` everywhere (`lessonId`, `tutorialId`, `trackId`, `userId`), never strings for entity ids;
* enums: serialized as strings, with a distinct enum per domain — no shared enum type;
* nullability: response DTOs mix nullable and non-null fields; Room adapters treat `Instant` as non-null
  (`"Expected NON-NULL 'org.joda.time.Instant', but it was NULL."`), so a null timestamp from the server would fail at
  the persistence boundary, not at deserialization (A-06).

## 5. Not recovered

* error body schema for any endpoint (no error DTO type found in the census);
* pagination envelopes (`mission-07` Q-list #1);
* the `Accept`/`Content-Type` negotiation rules for the C3 download;
* whether `j`/`UnknownKey` policies tolerate added server fields.
