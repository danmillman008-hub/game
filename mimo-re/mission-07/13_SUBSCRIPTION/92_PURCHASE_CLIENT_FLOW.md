# Mission 7 — Purchase Client Flow

```
learner opens paywall
  → paywall reads product/discount configuration
      (RevenueCat offering + LocalDiscountTheme from the API)
  → learner taps purchase
      → RevenueCat purchase flow → Play Billing sheet
      → CustomerInfo updated
      → app reads entitlement (isPremium)
      → UI unlocks + analytics event (paywall_shown/… family exists as event names)
  → failure/cancel → paywall remains, no local state change
  → restore → RevenueCat restore → entitlement refresh
```

## Facts vs inference
- RevenueCat in the chain, `isPremium` as the flag: **VERIFIED_STATIC**.
- The exact call order and error branches: **INFERRED** (paywall VM not decompiled).
- Server-side receipt verification: **BACKEND_ONLY** (RevenueCat's servers).
