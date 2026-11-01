# 10 — Gamification and the reward economy

Mimo runs **five distinct currencies** with separate authorities, separate sinks and separate
psychological jobs. Interleaving them is the product's biggest design asset and its biggest
transfer risk.

## 1. The five currencies

| Currency | Contract (V) | Source | Sink | Authority |
|---|---|---|---|---|
| **Sparks (XP)** | `sparks_daily_goal = %1$d/%2$d XP`, `DailySparksGoalProgressView`, dimens 42/32 sp | every correct answer / lesson | daily goal ring only — **XP is not spendable** | server-validated, client-displayed |
| **Coins** | `Coins(coins)`, `/v1/user/coins`, `sparks_goal_reached_coins` | daily-goal completion, streak challenges, rewards | **Mimo Store**: cosmetic app icons, streak freeze, fun rewards (`store_*`, 39 strings) | server (`/v1/user/coins`) |
| **Keys** | `UserKeys(currentKeys)`, `/v1/user/keys`, `/v1/user/keys/consume`, `keys_left_today = %d keys left today`, `keys_zero_subtitle = "New keys arrive tomorrow"` | daily refill (tomorrow) + Pro ("unlimited keys") | **unlocking lessons** (`keys_left_today_subtitle = "Use keys to unlock lessons"`) | server, consume is an explicit POST |
| **Streak** | `Streak(start)`, streak challenge/freeze/repair, widget | daily completion | risk of loss; repair costs | server |
| **League** | `Leaderboard(leaderboardId, startDate, endDate, isInProgress, hasActiveLeagueFreeze, currentUserIndex, promotionThreshold, demotionThreshold, users, league)`, `LeaderboardLeague(name, shortName, iconRes)` | weekly XP | promotion/demotion | server |

Additionally RevenueCat exposes **virtual currency** (`/v1/subscribers/%s/virtual_currencies`) —
evidence that at least part of the coin balance is projected through the purchase system rather
than (only) the game service.

## 2. The reward ritual (chapter end)

```
chapter complete
   → chapter_end_* screen (52 strings): progress, ETA, streak goal, native-ad fallback
   → reward sheet: reward_choose_box → reward_tap_to_open → Rive animation
                    reward_header_with_name ("Well done, %s!"), reward_drag_to_dismiss
   → reward content: Reward(id, description, rewardAmount, rewardId, rewardMultiplier)
                    confirm via /v1/user/rewards/{rewardId}/confirm
   → sparks credited → daily goal may complete → coins credited
                    ("You earned %1$d coins!", "exchange your coins for fun rewards in the Mimo Store")
```
`rewardMultiplier` + `sparks_double_gain` prove **multiplier mechanics** (streak length or Pro
status), and `/v1/user/rewards/next` proves the reward is **server-chosen**, not random on the
client.

## 3. Risk mechanics — the part most people miss

`streak_challenge_prompt_*` (V):
> "Up for a challenge?" / "Maintain your streak for 7 days and we'll double your investment" /
> **"Accept for %d"** (a cost) → on success "You've maintained a 7 day streak and earned %1$s
> coins"; on failure "You lost your challenge streak".

This is a **wager**: the learner stakes coins on their own consistency. It is the strongest
retention device in the app because it converts a passive streak into an active commitment.
`StreakRepairModal` + `store_product_streak_freeze_*` add the loss-aversion sink.

## 4. League structure (V)

Five named leagues (`leaderboard_league_name_1..5`, `…_short_name_1..5`), weekly windows
(`startDate`/`endDate`/`isInProgress`), explicit **promotion and demotion thresholds**
integers in the model, `hasActiveLeagueFreeze` (a paid protection — you can buy a week of not
being demoted), `currentUserIndex` + `users[]` for rendering around the user, and
`/v1/leaderboards/friends` for a social variant. `leaderboard_offline_message` shows the
degraded state.

## 5. Event pipeline

| Stage | Implementation (V) |
|---|---|
| Typed event catalogue | **305** `analytics.properties.*Property` classes, each with a snake_case `event`/`property` literal |
| Transport | `/v1/events` (own collector) + Mixpanel SDK + Adjust (attribution) + Firebase Analytics |
| Super properties | `SuperProperty` literals (track, tutorial, lesson, experiment, publishSetVersion) |
| Experiment tagging | `ContentExperiment(originalTrackId, variantTrackId, useTheVariant)` attached to events |
| Tutor/monetisation funnels | `AiTutorInteraction*`, `PaywallTrackingSource*` (13+ variants incl. `LastCall$Drawer`, `PathBanner`) |
| Lifecycle | Customer.io (351 classes) + Firebase In-App Messaging modals |

The event catalogue is the real asset: an enum-like schema of 305 product questions, each with a
stable snake_case name. For Konkur this is a **specification of the analytics you must have**,
not just code.

## 6. Economy balance observations (from copy, not from numbers)

* Keys are the only **hard gate** and they regenerate daily → the monetisation is
  *impatience*, not content.
* Coins have **no power** (cosmetics + protection) → the paid economy and the game economy are
  decoupled, which is why a Pro subscriber still plays the same loops.
* Sparks are a **display currency** — they measure progress and drive the daily ring, never
  unlock.
* Streak is the only currency that can be **lost**, and loss is the only thing that triggers
  repair purchases.
* No prices appear in resources (RevenueCat `offerings`/`products` are server-side, V endpoints
  `/v1/offerings`, `/v1/package/preview`, `/v2/purchase`) — **all economics are remote**.

## 7. Konkur transfer

| Element | Verdict | Reason |
|---|---|---|
| Sparks/XP + daily goal ring | **Reuse** | Universally motivating, no economy risk |
| Coins + store (cosmetics) | **Adapt** | Iran: cosmetics sell poorly; use coins for exam simulations/PDF exports |
| Keys (daily refill gate) | **Adapt** | Excellent monetisation model for Konkur's content depth, but must not gate *exam* content |
| Streak (daily) | **Adapt** | Study streaks work; add "days to Konkur" framing |
| Streak wager ("Accept for %d") | **Reuse with care** | Powerful, but gambling-adjacent framing needs legal review |
| League with promotion/demotion + freeze | **Exclude** | Needs a large active cohort per league; Konkur users study in isolation — use cohort/class rankings instead |
| Friends leaderboard | **Adapt** | Class/school ranking is culturally stronger |
| Reward box ritual | **Adapt** | Keep the moment, drop the animation; reward with *insight* ("you fixed 3 weak topics") |
| 305-event catalogue | **Reuse as spec** | Rebuild with Persian product questions |

**One hard warning:** Mimo's economy works because content is effectively infinite (1,029
tutorials, 19 tracks). A Konkur app with a fixed exam syllabus must not gate lessons with keys
— it will read as extortion. Gate *simulations* and *analytics depth* instead.
