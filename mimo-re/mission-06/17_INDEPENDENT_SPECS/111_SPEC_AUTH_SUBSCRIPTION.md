# Spec 111 — Auth, Subscription, Remote Config

## MUST
1. Bearer-token auth on all non-bootstrap calls; token held client-side.
2. Subscriptions via RevenueCat; entitlement exposed as `isPremium`.
3. Coin-priced consumables and remotely delivered discount themes.
4. Firebase Remote Config with exactly 3 default flags.
5. `allowBackup=false`.

## MUST NOT
- Implement login payloads (NOT_RECOVERED), refresh flows, or entitlement matrices.
- Bypass or emulate the payment provider.

## GIVEN EVIDENCE
`11_AUTH_SUBSCRIPTION_CONFIG/75..81`.
