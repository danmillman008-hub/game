# Mission 7 — Subscriptions

## Provider chain (VERIFIED_STATIC)
```
ui.paywall / ui.upgrade / ui.iap.modal
   → RevenueCat SDK (product catalogue, purchase, restore)
      → Google Play Billing
   → entitlement surfaced as PublicUser.isPremium (boolean)
```
- Tiers observed in product configuration: Free / Pro / Max (mission-05 finding, not re-derived).
- `RawPurchasedProduct{id, productType, coinPrice, boughtAt}` shows coin-priced consumables beside subscriptions.
- `LocalDiscountTheme` + `LocalDiscountThemeRepository.fetch` deliver **remote offers**, rendered locally.
- No Mimo endpoint performs purchases: the app never verifies receipts against `api.mimo.org` in recovered code
  (RevenueCat handles server-side validation out of band) — an INFERRED property of the provider model.

## Not attempted
No purchase was executed, no store account was used, no receipt or entitlement was spoofed.
