# Mission 7 — `bin.ghost` Base-Application Architecture

## Inventory (VERIFIED_STATIC, structure only)
19 classes in `bin.ghost.*`, decompiled; entry point `bin.ghost.YRF`, subclassed by `com.getmimo.App`.
`libyrf.so` ships alongside.

## Role in the target build
- Provides the `Application` base class that `com.getmimo.App` extends.
- Sits between process start and Mimo's own Application code.

## What was and was not determined
| Aspect | Status |
|---|---|
| class list | VERIFIED_STATIC |
| hierarchy (`com.getmimo.App extends bin.ghost.yrf`) | VERIFIED_STATIC |
| Application lifecycle participation | VERIFIED_STATIC (it is the base class) |
| dialogs / callbacks / event handling | NOT_RECOVERED (bodies not analysed in depth) |
| native integration (`libyrf.so`) | UNKNOWN |
| interaction with DI/startup | INFERRED: it runs before Mimo's Application code, so anything it does is pre-graph |

## Scope note
Per the mission's scope decision, no provenance investigation is performed. This document describes the classes
as part of the target codebase and stops where evidence stops.
