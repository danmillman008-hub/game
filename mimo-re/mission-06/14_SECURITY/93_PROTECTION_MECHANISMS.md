# Mission 6 — Protection Mechanisms

## Scope
Anti-tamper/obfuscation posture of the *Mimo* code (excluding foreign injections).

## Findings
1. **Obfuscation**: R8/ProGuard-style renaming — package names for app code are preserved
   (`com.getmimo.*`) while most classes/methods are single letters (`ae.m`, `qm.i`, `te.c`). Kotlin
   metadata is largely stripped from renamed classes. (VERIFIED_STATIC)
2. **String obfuscation**: none systematic — literals such as `api.mimo.org`, DSL tags and endpoint paths
   survive in the DEX constant pool, which is what made this mission possible. (VERIFIED_STATIC)
3. **No certificate pinning recovered** (Phase 11.78) — unusual for a subscription app; possibly added via
   config elsewhere (`Q-120`).
4. **No client-side encryption of progress or content** found. (VERIFIED_STATIC for the batch)
5. Play Integrity absent in the recovered batch (`Q-141`).

## Assessment (INFERRED)
Protection is aimed at **code readability**, not at traffic or integrity. A reconstruction should therefore
expect to rely on documented contracts, not on security-by-obscurity claims.

## Evidence labels
1–4 **VERIFIED_STATIC**; 5 **NOT_RECOVERED**; assessment **INFERRED**.
