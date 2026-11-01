# Phase 10 — Sequence diagrams

All participants are recovered classes. Steps that are library behaviour are marked *(lib)*.

## 10.1 Authenticated REST call

```mermaid
sequenceDiagram
    participant VM as ViewModel
    participant Repo as Repository
    participant API as Retrofit interface
    participant C1 as OkHttp C1
    participant Gate as hg.e
    participant UA as fh.b
    participant Auth as fh.a
    participant Tok as ku.a
    participant Srv as api.mimo.org

    VM->>Repo: intent
    Repo->>API: suspend method(dto)
    API->>C1: newCall
    C1->>Gate: intercept
    Gate->>Gate: network.a.b() == false?
    Gate->>UA: proceed
    UA->>Auth: + User-Agent
    Auth->>Auth: header present? → pass through
    Auth->>Auth: Method.getAnnotation(marker) == null ? → pass through
    Auth->>Tok: d(false)
    Tok-->>Auth: token | null
    Auth->>Srv: Authorization: Bearer <token>
    Srv-->>Repo: DTO / HttpException
    Repo-->>VM: state
```

## 10.2 Progress flush (Stage 5 outbox over Stage 7 transport)

```mermaid
sequenceDiagram
    participant ChVM as ChapterFinishedViewModel
    participant Q as LessonProgressQueue
    participant R as LessonProgressRepository
    participant DB as mimo.db lesson_progress
    participant API as LessonProgressApi
    participant Srv as POST /v1/tutorials/{id}/progress

    ChVM->>Q: storeAndPostAllLessonProgress()
    Q->>R: moveLessonProgressFromQueue()
    R->>DB: UPDATE … SET in_queue = 0 WHERE in_queue = 1
    Q->>R: postUnsyncedLessonProgress()
    R->>R: networkUtils.a() ? else NoConnectionException
    R->>DB: SELECT * FROM lesson_progress
    loop per tutorialId
        R->>API: postProgress(tutorialId, PostProgressRequestBody)
        API->>Srv: POST (through C1, gate, UA, auth)
        Srv-->>R: PostProgressResponse{reachedGoal, dailyGoalCoinReward}
        R->>R: cg.e(reachedGoal, dailyGoalCoinReward)
    end
    R->>DB: DELETE FROM lesson_progress WHERE lesson_id IN (…)
    R-->>ChVM: sync result
    ChVM->>Srv: (next) GET /v1/tracks/{id}/completion
```

## 10.3 AI tutor SSE

```mermaid
sequenceDiagram
    participant VM as AiTutorViewModel
    participant AR as aitutor repository (C7)
    participant Tok as ku.a
    participant Srv as /v1/aiTutor/conversations
    participant L as EventSourceListener

    VM->>AR: sendMessage(system, user[, conversationId])
    AR->>Tok: d(false)
    AR->>Srv: POST + Accept: text/event-stream + Authorization
    Srv-->>L: event frames (data: {content, conversationId, finishReason})
    L->>VM: append content to last assistant message
    alt finishReason == Stop | Length
        L->>VM: complete
    else socket drops
        L->>VM: error (no resume, no retry)
    end
```

## 10.4 Code execution over the socket

```mermaid
sequenceDiagram
    participant VM as ExecutableLessonViewModel
    participant S as pg.a (C8)
    participant Srv as wss://api.mimo.org/v1/run/socket

    VM->>S: connect(runfiles)
    S->>Srv: handshake with Sec-WebSocket-Protocol: authorization.bearer.<token>
    Srv-->>S: frames (schema NOT_RECOVERED)
    S-->>VM: console output stream
    Note over S,Srv: no reconnect, no ping/pong handler recovered
```

## 10.5 Token acquisition (inside `ku.a.d`)

```mermaid
sequenceDiagram
    participant Auth as fh.a
    participant Tok as ku.a
    participant FA as FirebaseAuth
    participant G as Google identity

    Auth->>Tok: d(false)
    Tok->>FA: currentUser
    alt null
        Tok-->>Auth: null (log "There is no Firebase user!")
    else user
        Tok->>FA: getAccessToken(false) / Tasks.await (lib)
        FA-->>Tok: token + claims
        Tok->>Tok: claims["exp"] vs now
        alt expired
            Tok->>FA: getAccessToken(true) / Tasks.await
            FA->>G: refresh round-trip (lib)
        end
        Tok-->>Auth: token
    end
```
