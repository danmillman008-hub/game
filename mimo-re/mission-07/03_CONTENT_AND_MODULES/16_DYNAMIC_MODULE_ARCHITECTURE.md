# Mission 7 — Dynamic Feature Module Architecture

## Inventory (VERIFIED_STATIC)
Fused modules: `base` + `content_de`, `content_es`, `content_fr`, `content_id`, `content_it`, and further
`content_*` names in the same manifest meta-data value.

## Layout question
The modules are **not** in the APK. Their internal split (assets vs dex vs resources) is therefore
NOT_RECOVERED. What the base build constrains: all parsers (`te.*`), renderers (`ui.lesson.*`) and models live
in the base DEX, so a content module can only contribute *data* (lesson documents, images) — it cannot change
behaviour without a base release.

## Delivery
Play Feature Delivery. No `SplitInstallManager`/`SplitInstallRequest` usage was found in the decompiled subset,
so the install trigger is UNKNOWN; the naming and fused-module list prove the mechanism exists.

## Offline consequence
Once installed, module assets are on device → lessons work offline (**INFERRED_HIGH**). Before installation,
that locale's lessons are unavailable while English remains available (bundled).

## Locale ↔ module matrix
`99_LOCALE_MODULE_MATRIX.csv`.
