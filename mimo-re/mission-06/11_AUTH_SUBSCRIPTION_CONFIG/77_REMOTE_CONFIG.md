# Mission 6 — Remote Config

## Scope
Server-controlled switches and their defaults.

## Method
`res/xml/remote_config_defaults.xml` (decoded), Firebase Remote Config usage, 15 `res/xml` configs.

## Findings (VERIFIED_STATIC)
1. `remote_config_defaults.xml` declares exactly **3 flags** (a small, surgical switch surface — not a
   general experiment platform in the client).
2. Firebase Remote Config is the provider (Firebase SDK present; the defaults file is its companion).
3. 15 `res/xml` files exist in total (network security config, backup rules, data extraction rules,
   locales, remote config defaults, …).
4. Which flags gate which features is **UNKNOWN** — the flag keys read as generic identifiers and no
   consumer mapping was traced (`Q-118`).

## Evidence labels
Points 1–3 **VERIFIED_STATIC**; 4 **UNKNOWN**.

## Open questions
`Q-118` flag consumers; `Q-119` whether flags can disable lessons/AI.

## Reproduction
`cat /tmp/res/res/xml/remote_config_defaults.xml`
