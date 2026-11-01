# Mission 6 — Security Threat Model (analysis of the client, defensive framing)

## Scope
What the *client* trusts, where that trust is misplaced, and what that means for a reconstruction and for
an owner of the app. No exploitation is described or performed.

## Method
Trust-boundary reading: token handling, offline guard, progress assertions, content parsing, dynamic code
loading, WebView usage.

## Findings (VERIFIED_STATIC unless marked)
| Boundary | Client behaviour | Risk framing |
|---|---|---|
| content → parser | XML from bundled assets or downloaded zips is parsed with no schema validation | malformed content is a hard parse failure; a signed/verified pack path was not found |
| client → server | progress is an **assertion** (no signature, no nonce) | server must validate; client cannot prove completion |
| server → client | `publishSetVersion`, coins, streaks trusted as returned | no client-side verification of economy state |
| token → device | bearer token stored client-side; storage mechanism not recovered | standard mobile risk (`Q-121`) |
| WebView modules | `<webview>` DSL tag with `interaction`/`content` attributes | content-controlled web content inside the app; URL allowlist behaviour **UNKNOWN** (`Q-140`) |
| dynamic modules | Play-delivered content packs | standard |
| APK integrity | this artifact is third-party re-signed | **any** integrity/injection claim is void for this APK |

## Explicit non-goals
No bypass of auth/payment/licensing, no attempts against the backend, no key extraction. Findings above
are properties of the client contract, not instructions.

## Evidence labels
As marked; WebView allowlist and token storage are open questions.

## Reproduction
`grep -rn 'loadUrl\|WebView' /tmp/dad/com.getmimo.ui.webview*.java | head`
