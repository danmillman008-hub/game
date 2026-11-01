# Mission 6 — Business Logic and Monetisation

## Scope
How the product makes money and what the client must therefore implement.

## Method
IAP/RevenueCat findings, coin economy, discount themes, paywall surfaces, keys/hearts, AI gating.

## Findings (VERIFIED_STATIC unless marked)
1. **Subscription** (RevenueCat; Free/Pro/Max tiers in product config) — primary revenue.
2. **Coin purchases** (`RawPurchasedProduct.coinPrice`) — consumables priced in coins, bought via IAP.
3. **Coins earned**: `PostProgressResponse.dailyGoalCoinReward` (daily goal) and league `sparks` (a
   separate currency) — **earning is server-granted**, the client only displays.
4. **Keys** (`UserKeys.currentKeys`) — a limited-resource model whose consumption path is not in the
   recovered lesson code (`Q-57`).
5. **Discount themes** fetched remotely — price personalisation/promotions.
6. **AI tutor** sits behind the upgrade surface (`INFERRED_HIGH`).
7. No ads SDK was found in the recovered classes (`VERIFIED_STATIC` for the batch; `Q-125` for the whole
   DEX).

## Evidence labels
As marked.

## Open questions
`Q-57`, `Q-115`, `Q-125`.

## Reproduction
`grep -ci 'admob\|applovin\|unityads' <(ls /tmp/dad)`
