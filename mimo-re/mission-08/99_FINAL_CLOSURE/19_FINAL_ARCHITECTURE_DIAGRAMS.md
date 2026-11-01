# 19 — Final architecture diagrams

All diagrams are derived from recovered evidence; no box exists that is not backed by a record in `16`.

## 1. Application architecture

```mermaid
graph TD
  A[MainActivity<br/>12 deep links + mimo://] --> NAV[Navigation graph]
  NAV --> VM[ViewModels]
  VM --> UC[use cases / interactors]
  UC --> REPO[repositories]
  REPO --> CONTENT[ContentRepository<br/>assets/lessons-*]
  REPO --> PROG[LessonProgressRepository + Queue]
  REPO --> COMP[CompletionRepository]
  REPO --> REMOTE[remote.* 29 interfaces]
  PROG --> DB[(mimo.db v2)]
  COMP --> DB
  COMP --> PREFS[mimo_prefs]
  REMOTE --> C1[OkHttp C1] --> SRV[api.mimo.org]
  VM --> TUTOR[aitutor.a SSE] --> SRV
  VM --> SOCK[pg.a WebSocket] --> WSS[wss api.mimo.org]
  VM --> ANA[analytics.a] --> CIO[track.customer.io]
```

## 2. Dependency injection (network arm)

```mermaid
graph LR
  U[ri.d connectivity] --> HE[hg.e]
  B[ku.a token] --> FA[fh.a]
  HE --> C1[case 20 client]
  FB[fh.b UA] --> C1
  FA --> C1
  C1 --> C2[case 19 Retrofit]
  W[case 22 host] --> C2
  E[jx.d converter] --> C2
  C2 --> IF[25 interfaces]
  C1 --> C4[track.customer.io] & C5[mimoauth] & C6[email]
  C1 --> C3[case 108 10s/120s]
  B --> C7[tutor] & C8[socket]
```

## 3. Content delivery

```mermaid
sequenceDiagram
  participant UI as Lesson UI
  participant CR as ContentRepository (ye.b)
  participant AS as assets/lessons-<locale>
  participant TE as te.c → te.a..te.g
  participant RD as renderer
  UI->>CR: open(tutorialId)
  CR->>AS: tracks/tutorial-<id>.json
  AS-->>CR: document
  CR->>TE: parse blocks
  TE-->>RD: AST
  RD-->>UI: custom elements + composables
```

## 4. Lesson + grading + feedback

```mermaid
stateDiagram-v2
  [*] --> Open: K (initialiseCodeBlocks)
  Open --> Graded: submit
  Graded --> Correct: V (tries=!(C==TRUE), jm.m)
  Graded --> Partial: W (jm.n)
  Graded --> Wrong: X (tries=0, jm.o)
  Correct --> Stored: e0 → outbox (in_queue=1)
  Partial --> Stored
  Wrong --> Stored
  Stored --> Next: U (tries=(C==TRUE), emit next lesson)
```

## 5. Learner progress lifecycle

```mermaid
sequenceDiagram
  participant VM as Lesson VM
  participant R as LessonProgressRepository
  participant DB as lesson_progress
  participant API as POST /v1/tutorials/{id}/progress
  participant C as CompletionRepository
  VM->>R: create + store (in_queue=1)
  R->>DB: upsert
  Note over R,DB: chapter end or app start
  R->>DB: UPDATE in_queue=0 WHERE in_queue=1
  R->>DB: SELECT *
  R->>API: grouped by tutorialId
  API-->>R: reachedGoal, dailyGoalCoinReward
  R->>DB: DELETE WHERE lesson_id IN (...)
  VM->>C: fetchTrackCompletion(trackId, version)
  C->>C: tutorial_completions + chapter_completions + prefs pointer
```

## 6. Database schema

```mermaid
erDiagram
  lesson_progress {
    long lesson_id PK
    long tutorial_id PK
    long track_id
    int tries
    int attempts
    boolean in_queue
  }
  tutorial_completions {
    long tutorial_id PK
    long track_id PK
    boolean is_completed
  }
  chapter_completions {
    long chapter_id PK
    long track_id PK
    long tutorial_id
  }
```

## 7. Authentication lifecycle

```mermaid
sequenceDiagram
  participant REQ as authorized request
  participant FA as fh.a
  participant K as ku.a
  participant F as FirebaseAuth
  REQ->>FA: header present? annotated?
  FA->>K: d(false)
  K->>F: currentUser / getAccessToken(false)
  alt exp < now
    K->>F: getAccessToken(true)
  end
  K-->>FA: token
  FA-->>REQ: Authorization: Bearer <token>
```

## 8. Network topology

```mermaid
graph LR
  APP[app code] --> C2[shared Retrofit] --> API[api.mimo.org]
  APP --> C4[Customer.io] --> T[track.customer.io]
  APP --> C5[mimo-auth relay] --> M[mimoauth.getmimo.com]
  APP --> C6[email] --> E[email.getmimo.com]
  APP --> C7[SSE] --> API
  APP --> C8[WS] --> WSS[wss api.mimo.org]
  APP --> SDK[Firebase / RevenueCat / Adjust / Sentry]
```

## 9. Offline boundary

```mermaid
graph TD
  subgraph OFFLINE_OK
    L[lessons] --> G[grading] --> P[progress row]
  end
  subgraph NEEDS_NETWORK
    CMP[completion] ; COINS[coins] ; TUT[ai tutor] ; EXE[execution] ; SOC[social]
  end
  P -->|outbox flush| SRV[server]
  SRV --> CMP
```

## 10. Domain map

45 domains, statuses in `15_FINAL_COVERAGE_MATRIX.csv`: 25 COMPLETE, 15 SUBSTANTIALLY, 5 PARTIALLY, 0 unclassified.
