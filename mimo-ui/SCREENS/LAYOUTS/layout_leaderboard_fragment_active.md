# پروندهٔ لایه — `res/layout/leaderboard_fragment_active.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_fragment_active.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_fragment_active.xml`](../../SOURCE/res/layout/leaderboard_fragment_active.xml) |
| SHA-256 دیکد | `4128c519086e16ecc8dc2eedbe6d0a36143a20df9ecd447b0be2784fcc2b6372` |
| ریشه | `LinearLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ com.getmimo.ui.leaderboard.LeaderboardLeagueHeaderView  #@id/leaderboard_league_header_view
   └─ androidx.swiperefreshlayout.widget.SwipeRefreshLayout  #@id/srl_leaderboard_refresh_layout
      └─ androidx.recyclerview.widget.RecyclerView  #@id/rv_leaderboard
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 4 | `com.getmimo.ui.leaderboard.LeaderboardLeagueHeaderView` | `android:id` | `@id/leaderboard_league_header_view` |
| 5 | `com.getmimo.ui.leaderboard.LeaderboardLeagueHeaderView` | `android:layout_width` | `match_parent` |
| 6 | `com.getmimo.ui.leaderboard.LeaderboardLeagueHeaderView` | `android:layout_height` | `wrap_content` |
| 7 | `androidx.swiperefreshlayout.widget.SwipeRefreshLayout` | `android:id` | `@id/srl_leaderboard_refresh_layout` |
| 8 | `androidx.swiperefreshlayout.widget.SwipeRefreshLayout` | `android:layout_width` | `match_parent` |
| 9 | `androidx.swiperefreshlayout.widget.SwipeRefreshLayout` | `android:layout_height` | `match_parent` |
| 10 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_leaderboard` |
| 11 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `match_parent` |
| 12 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `match_parent` |
| 13 | `androidx.recyclerview.widget.RecyclerView` | `app:layoutManager` | `androidx.recyclerview.widget.LinearLayoutManager` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/leaderboard_league_header_view
@id/rv_leaderboard
@id/srl_leaderboard_refresh_layout
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

```text
res/layout/leaderboard_fragment.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.getmimo.ui.leaderboard.LeaderboardLeagueHeaderView android:id="@id/leaderboard_league_header_view" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  <androidx.swiperefreshlayout.widget.SwipeRefreshLayout android:id="@id/srl_leaderboard_refresh_layout" android:layout_width="match_parent" android:layout_height="match_parent">
    <androidx.recyclerview.widget.RecyclerView android:id="@id/rv_leaderboard" android:layout_width="match_parent" android:layout_height="match_parent" app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager"/>
  </androidx.swiperefreshlayout.widget.SwipeRefreshLayout>
</LinearLayout>
```
