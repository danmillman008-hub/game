# Mission 6 — Subscription and Entitlements

## Scope
Plans, purchase path, entitlement checks and paywall logic.

## Method
`ui.upgrade.*`, `ui.iap.*`, RevenueCat classes, `PublicUser.isPremium`, `RawPurchasedProduct`, discount
themes.

## Findings (VERIFIED_STATIC)
1. Purchases go through **RevenueCat** (`libsigner.so` + RevenueCat SDK classes): the app does not talk to
   a Mimo payment endpoint.
2. Entitlement surface on the user object is a single boolean `isPremium`; the plan tiers Free/Pro/Max are
   present in the product configuration data (mission-05 finding, frozen).
3. `RawPurchasedProduct { id, productType, coinPrice, boughtAt }` shows **coin-priced products** exist as a
   second economy beside subscriptions.
4. `LocalDiscountTheme`/`LocalDiscountThemeRepository.fetch` show **personalised discount offers** delivered
   remotely and rendered locally.
5. The paywall is a first-class feature (`ui.paywall`, `ui.upgrade`, `ui.iap.modal`), and the AI tutor
   references upgrade UI (Phase 8.60).

## Evidence labels
RevenueCat, `isPremium`, coin products, discount fetch: **VERIFIED_STATIC**. Which features are gated:
**INFERRED_HIGH** (`Q-115`).

## Open questions
`Q-115` feature gating matrix; `Q-116` restore/refund handling; `Q-117` discount eligibility source.

## Reproduction
`grep -rl 'revenuecat' /tmp/dad | head -3; grep -n 'coinPrice' /tmp/dad/com.getmimo.data.model.iap.RawPurchasedProduct.java`
