# Mission 7 — Rive Runtime Architecture

## Inventory (VERIFIED_STATIC)
**59** `.riv` assets are packaged, plus `librive-android.so` (JNI) and `app.rive.*` Java classes.

First assets:
- `19695  1981-01-01 01:01`
- `14443  1981-01-01 01:01`
- `5826  1981-01-01 01:01`
- `27202  1981-01-01 01:01`
- `22436  1981-01-01 01:01`
- `10828  1981-01-01 01:01`
- `11931  1981-01-01 01:01`
- `18029  1981-01-01 01:01`
- `21255  1981-01-01 01:01`
- `11053  1981-01-01 01:01`
- `8640  1981-01-01 01:01`
- `5180  1981-01-01 01:01`

## What is known
- The runtime is the official Rive Android library (JNI into `librive-android.so`).
- Assets are bundled, so animations are offline-capable.
- The app also uses `ui.sonar.*` (59 classes) for UI effects, which is separate from Rive.

## What is *not* recovered
| Question | Status |
|---|---|
| which class loads which `.riv` | NOT_RECOVERED — no `RiveAnimationView` reference in the decompiled subset |
| state machine / input names | NOT_RECOVERED |
| trigger conditions (correct answer, streak, level) | NOT_RECOVERED |
| fallback behaviour | UNKNOWN |

## Honest position
Mission 6 and 7 both fail at the same point: the binding layer is UI code that was not in any decompiled batch
and cannot be inferred from asset names. `79_RIVE_COMPONENT_MAPPING.csv` lists every asset with
`NOT_RECOVERED` rather than a guess.
