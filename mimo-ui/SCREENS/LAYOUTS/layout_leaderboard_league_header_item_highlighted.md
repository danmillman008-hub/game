# پروندهٔ لایه — `res/layout/leaderboard_league_header_item_highlighted.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_league_header_item_highlighted.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_league_header_item_highlighted.xml`](../../SOURCE/res/layout/leaderboard_league_header_item_highlighted.xml) |
| SHA-256 دیکد | `c03479109904b43d5bf7b5f3262205219ff7dbec0f8c1e54a9fa4c3a7a745ee9` |
| ریشه | `FrameLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   └─ ImageView  #@id/iv_leaderboard_league_header_item_highlighted
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `@dimen/leaderboard_league_header_item_selected_width` |
| 2 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 3 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 4 | `ImageView` | `android:id` | `@id/iv_leaderboard_league_header_item_highlighted` |
| 5 | `ImageView` | `android:layout_width` | `match_parent` |
| 6 | `ImageView` | `android:layout_height` | `@dimen/leaderboard_league_header_item_selected_height` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/leaderboard_league_header_item_selected_height` | `60.000000dip` / `78.000000dip` (sw600dp) |
| `@dimen/leaderboard_league_header_item_selected_width` | `62.000000dip` / `80.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_leaderboard_league_header_item_highlighted
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.leaderboard.LeaderboardFragment$observeViewModelEvents$1$1$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="@dimen/leaderboard_league_header_item_selected_width" android:layout_height="match_parent">
  <ImageView android:layout_gravity="0x00000011" android:id="@id/iv_leaderboard_league_header_item_highlighted" android:layout_width="match_parent" android:layout_height="@dimen/leaderboard_league_header_item_selected_height"/>
</FrameLayout>
```
