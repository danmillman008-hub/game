# 01 — What Mimo is (one page, no prior knowledge assumed)

Mimo is a mobile app that teaches programming through short interactive lessons. Everything in this document is
recovered from the shipped APK and is `VERIFIED_STATIC` unless marked otherwise.

## 1. The product in numbers

| Quantity | Value |
|---|---|
| Tracks / tutorials / chapters / lessons | 19 / 1,029 / 1,947 / **18,272** |
| Locales shipped | 10 (`en` base + 9) |
| Content documents | 10,317 JSON + 20,306 lesson HTML-documents |
| Content version | `publishSetVersion = 753` |
| Endpoints | 62 (29 Retrofit interfaces) over 5 hosts |
| Local tables | 3 (`lesson_progress`, `tutorial_completions`, `chapter_completions`) |
| HTTP clients | 6 objects, 3 interceptors |
| Analytics events bound to code | 14 |

## 2. Layered view

```text
UI (Compose) → ViewModel → use case/interactor → repository → { assets | Room | OkHttp/Retrofit | Firebase }
```

* **Content is not downloaded.** Lessons come from `assets/lessons-<locale>/tracks/tutorial-<id>.json`.
* **Grading is local.** The device decides correct/partial/wrong.
* **Completion is remote.** The device posts solved lessons, then asks the server what is complete.
* **Identity is Firebase.** The token is fetched per request and injected only into annotated endpoints.

## 3. The lesson pipeline

```text
tutorial JSON → Track/Section/Tutorial/Chapter/Lesson model
   → dispatcher te.c → one of seven parsers te.a..te.g → AST
   → renderer (HTML custom elements + native interaction surfaces)
   → user answers → normaliser qm.i.a → verdict (CORRECT | PARTIAL | INCORRECT)
   → feedback state jm.m/jm.n/jm.o → visibility gating (ALWAYS | CORRECT | WRONG)
   → lesson solved → progress row → outbox → POST → delete
```

## 4. The five things that surprise people

1. **`tries` is not a counter.** It is 0/1: "was this lesson solved". `attempts` is the session counter and is never
   restored from storage. There is no lifetime history locally.
2. **Nothing client-side computes completion or unlocking.** The server answers, the client caches.
3. **`in_queue` is an outbox flag**, and a successful upload *deletes* the rows it posted.
4. **The token header is annotation-driven**, so REST, SSE and WebSocket each authenticate differently.
5. **The app is offline for content and lesson work, online for progression.** Both halves are evidenced; calling it
   simply "offline-capable" is wrong either way.

## 5. What was reverse-engineered, and how far

| Layer | Status |
|---|---|
| content model, corpus, locales, versioning | complete |
| DSL grammar, parsers, AST, renderer contract | complete |
| interactions, grading, feedback | complete (algorithm recovered) |
| learner model, outbox, completion boundary | complete |
| Room schema, DAO statements | complete (except 25 lambda ids) |
| network stack, endpoints, auth lifecycle | complete (except the per-endpoint annotation table) |
| SSE | complete (client side) |
| WebSocket frames, WebView JS surface, sign-out bodies | not recovered |
| server behaviour (completion rules, ETA, coins) | out of reach by definition |

Runtime verification: **none**. The APK is no longer available in the analysis environment, so every claim rests on
bytecode read while it was.

## 6. Where to look next

* to build the engine: `10_BUILD_THE_MIMO_PROJECT.md`;
* to copy the grading rules exactly: `04_SPEC_INTERACTION_AND_GRADING.md`;
* to know what to keep and what to drop: `12_DELTA_REGISTER.md`;
* to see the dark corners: `13_KNOWN_UNKNOWNS.md`.
