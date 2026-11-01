# 08 — SPEC: streaming (SSE) and the AI tutor (partially recovered)

Sources: `mimo-re/mission-07/09_STREAMING/{69,70,71}*`, `mimo-re/mission-08/07_NETWORKING/`.
Status: **PARTIAL** — client-side framing recovered, WebSocket surface and server semantics not recovered.

## 1. SSE (Server-Sent Events)

Recovered:
* the client uses a streaming call with an `Accept: text/event-stream`-style contract and parses `data:` frames;
* the stream is tied to the AI tutor feature (category `ai_tutor`, 1 endpoint);
* cancellation is handled through the call's cancellation handle; the parser tolerates empty keep-alive frames.

Not recovered: exact endpoint path/verb per-row annotation confidence, reconnect/`Last-Event-ID` behaviour, and any
server framing beyond `data:`.

## 2. WebSocket

A WebSocket client object exists in the network stack. **Frames, handshake headers, and message schema were not
recovered** (`Q-96`). Do not invent them.

## 3. WebView ↔ native bridge

`<webview>` blocks render third-party HTML with `interaction="feedback|unlock"`. The JavaScript interface names and the
URL allowlist were **not recovered** (`Q-140`). Mimo's `unlock` interaction implies the embedded page can influence
progress through a native callback; the callback surface is unknown.

## 4. Tutor (conversational help)

What is certain: an AI tutor endpoint exists and is streamed; the app shows tutor candidates in the incorrect-feedback
state (`jm.o` flags, `04` §5). Model names, prompt handling and moderation are **BACKEND_ONLY**.

## 5. Why this section exists in an offline brief

So that nobody re-derives it, and so that any agent tempted to "add AI" knows: the client half is known, the server half
is not, and the offline engine deliberately excludes it. If you implement streaming in `mimo/`, treat it as **new
work**, not as recovery, and label it accordingly.
