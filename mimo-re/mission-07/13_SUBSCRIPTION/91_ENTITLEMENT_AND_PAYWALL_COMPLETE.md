# Mission 7 — Entitlements and Paywall

| Element | Finding | Label |
|---|---|---|
| entitlement flag | `PublicUser.isPremium` (single boolean) | VERIFIED_STATIC |
| plan tiers | Free/Pro/Max in product config | VERIFIED_STATIC (mission-05) |
| gated features | not enumerated; upgrade UI referenced from AI tutor and guided projects | INFERRED_HIGH |
| paywall surfaces | `ui.paywall`, `ui.upgrade`, `ui.iap.modal`, reactivation/discount variants | VERIFIED_STATIC |
| promotional offers | `LocalDiscountTheme` (remote), `pro_expiration_discount_chapter_end` analytics value | VERIFIED_STATIC (existence) |
| restore purchase | RevenueCat restore; exact UI call site not decompiled | PARTIAL |
| offline entitlement | no cached entitlement store ⇒ premium state requires a successful profile/session fetch | INFERRED_HIGH |

## Open
`Q-115` gating matrix; `Q-116` restore/refund handling; `Q-117` discount eligibility.
