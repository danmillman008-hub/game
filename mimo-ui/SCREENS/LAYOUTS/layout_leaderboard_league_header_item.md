# پروندهٔ لایه — `res/layout/leaderboard_league_header_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_league_header_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_league_header_item.xml`](../../SOURCE/res/layout/leaderboard_league_header_item.xml) |
| SHA-256 دیکد | `01e0a2c44205ea34e2ba7ac621734b681a07117067eb00bac69c92cc9656d12d` |
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
   └─ ImageView  #@id/iv_leaderboard_league_header_item
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `@dimen/leaderboard_league_header_item_width` |
| 2 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 3 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 4 | `ImageView` | `android:id` | `@id/iv_leaderboard_league_header_item` |
| 5 | `ImageView` | `android:layout_width` | `match_parent` |
| 6 | `ImageView` | `android:layout_height` | `@dimen/leaderboard_league_header_item_height` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/leaderboard_league_header_item_height` | `50.000000dip` / `66.000000dip` (sw600dp) |
| `@dimen/leaderboard_league_header_item_width` | `52.000000dip` / `68.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_leaderboard_league_header_item
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
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="@dimen/leaderboard_league_header_item_width" android:layout_height="match_parent">
  <ImageView android:layout_gravity="0x00000011" android:id="@id/iv_leaderboard_league_header_item" android:layout_width="match_parent" android:layout_height="@dimen/leaderboard_league_header_item_height"/>
</FrameLayout>
```
