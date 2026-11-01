# Mission 7 — Localization Architecture

## Two independent axes
| Axis | Mechanism | Evidence |
|---|---|---|
| UI language | Android resource qualifiers (`values-<lang>`) — the ARSC string pool holds copy in ~12+ languages | ARSC decode |
| Content language | Play dynamic modules `content_<locale>` + bundled English assets | manifest meta-data, asset tree |

## Resolution
- UI text resolves through `Resources` (standard Android).
- Content resolves by choosing the module/asset tree; `ContentLocale` (IT, PL, PT, RU, TR) is a **fallback enum**,
  not the full list.
- No code was found that forces content locale = UI locale.

## Consequences
- A learner can have German UI and English lessons.
- The normaliser (`qm.i`) is locale-independent ⇒ non-Latin answers cannot match via the normalised path.
- RTL: no RTL-specific layout logic recovered; Arabic/Hebrew content is not in the shipped assets.
