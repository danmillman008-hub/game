# Mission 7 — Complete Storage Map

| Store | Technology | Content | Lifetime | Evidence |
|---|---|---|---|---|
| `lesson_progress` | Room | 11 columns per (lesson,tutorial) | until push | entity + SQL |
| `chapter_completions` | Room | chapter markers | persistent | SQL literals |
| `tutorial_completions` | Room | tutorial markers | persistent | SQL literals |
| preferences | SharedPreferences | token, onboarding flags, FCM token, config cache | persistent | usage sites |
| encrypted storage | **not identified** | — | — | no EncryptedSharedPreferences call recovered |
| files / cache | OkHttp/asset cache only | assets, no content writes | process | absence of file APIs for content |
| WebView storage | platform default | webview module data | platform | `<webview>` module |
| native/SDK storage | Adjust/Firebase/RevenueCat own stores | SDK state | SDK | SDK presence |

## Key structural fact
There is **no content cache and no learner-profile cache**: everything the client must remember across launches
lives in three tables plus preferences. That is why offline lessons work (assets) but offline economy data does
not exist.
