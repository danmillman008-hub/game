# پروندهٔ لایه — `res/layout/reward_tablet_dialog_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/reward_tablet_dialog_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/reward_tablet_dialog_fragment.xml`](../../SOURCE/res/layout/reward_tablet_dialog_fragment.xml) |
| SHA-256 دیکد | `f3e360dd40e6f61b5cc3a5c0bbbe7479722b1715a893563a0b05a09ddda79c31` |
| ریشه | `FrameLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/root_reward_tablet_dialog_fragment
   └─ androidx.cardview.widget.CardView
      └─ FrameLayout  #@id/container_reward_tablet_dialog_fragment
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:orientation` | `vertical` |
| 2 | `FrameLayout` | `android:id` | `@id/root_reward_tablet_dialog_fragment` |
| 3 | `FrameLayout` | `android:background` | `@color/generic_backdrop_color` |
| 4 | `FrameLayout` | `android:focusable` | `true` |
| 5 | `FrameLayout` | `android:clickable` | `true` |
| 6 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 7 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 8 | `androidx.cardview.widget.CardView` | `android:layout_gravity` | `0x00000011` |
| 9 | `androidx.cardview.widget.CardView` | `android:layout_width` | `wrap_content` |
| 10 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 11 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/card_enabled` |
| 12 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius_large` |
| 13 | `FrameLayout` | `android:id` | `@id/container_reward_tablet_dialog_fragment` |
| 14 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 15 | `FrameLayout` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/card_enabled` | `#FFFFFFFF` / `#FF3F4273` (night) |
| `@color/generic_backdrop_color` | `#88000000` |
| `@dimen/cardview_corner_radius_large` | `12.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/container_reward_tablet_dialog_fragment
@id/root_reward_tablet_dialog_fragment
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.reward.RewardFragment$loadUserName$1
com.getmimo.ui.reward.RewardTabletDialogFragment$onViewCreated$2
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:id="@id/root_reward_tablet_dialog_fragment" android:background="@color/generic_backdrop_color" android:focusable="true" android:clickable="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.cardview.widget.CardView android:layout_gravity="0x00000011" android:layout_width="wrap_content" android:layout_height="wrap_content" app:cardBackgroundColor="@color/card_enabled" app:cardCornerRadius="@dimen/cardview_corner_radius_large">
    <FrameLayout android:id="@id/container_reward_tablet_dialog_fragment" android:layout_width="match_parent" android:layout_height="match_parent"/>
  </androidx.cardview.widget.CardView>
</FrameLayout>
```
