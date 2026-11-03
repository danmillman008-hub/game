# پروندهٔ لایه — `res/layout/leaderboard_league_header_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_league_header_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_league_header_view.xml`](../../SOURCE/res/layout/leaderboard_league_header_view.xml) |
| SHA-256 دیکد | `01f77bafc4de7050e5888204897f4afe92c561886bb734aa1585cbf6569bb9ab` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ FrameLayout  #@id/frameLayout
   │  └─ androidx.recyclerview.widget.RecyclerView  #@id/rv_leaderboard_result_leagues
   ├─ TextView  #@id/tv_leaderboard_results_league_label
   └─ TextView  #@id/tv_leaderboard_header_results_available_timer
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/navbar_background` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:elevation` | `4.000000dip` |
| 5 | `FrameLayout` | `android:id` | `@id/frameLayout` |
| 6 | `FrameLayout` | `android:layout_width` | `0.000000dip` |
| 7 | `FrameLayout` | `android:layout_height` | `@dimen/leaderboard_league_header_height` |
| 8 | `FrameLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 9 | `FrameLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 10 | `FrameLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_gravity` | `0x00000011` |
| 12 | `androidx.recyclerview.widget.RecyclerView` | `android:orientation` | `horizontal` |
| 13 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_leaderboard_result_leagues` |
| 14 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `wrap_content` |
| 15 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `match_parent` |
| 16 | `androidx.recyclerview.widget.RecyclerView` | `android:overScrollMode` | `2` |
| 17 | `androidx.recyclerview.widget.RecyclerView` | `app:layoutManager` | `androidx.recyclerview.widget.LinearLayoutManager` |
| 18 | `TextView` | `android:textColor` | `@color/navbar_text` |
| 19 | `TextView` | `android:id` | `@id/tv_leaderboard_results_league_label` |
| 20 | `TextView` | `android:layout_width` | `wrap_content` |
| 21 | `TextView` | `android:layout_height` | `wrap_content` |
| 22 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 23 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 24 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 25 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 26 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/frameLayout` |
| 27 | `TextView` | `style` | `@style/TextLeaderboardLeagueHeader` |
| 28 | `TextView` | `android:textColor` | `@color/navbar_text` |
| 29 | `TextView` | `android:id` | `@id/tv_leaderboard_header_results_available_timer` |
| 30 | `TextView` | `android:layout_width` | `wrap_content` |
| 31 | `TextView` | `android:layout_height` | `wrap_content` |
| 32 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 33 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 34 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 35 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 36 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/frameLayout` |
| 37 | `TextView` | `style` | `@style/TextP1` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/navbar_text` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/leaderboard_league_header_height` | `100.000000dip` / `144.000000dip` (sw600dp) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@style/TextLeaderboardLeagueHeader` | `[]` / `[]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/frameLayout
@id/rv_leaderboard_result_leagues
@id/tv_leaderboard_header_results_available_timer
@id/tv_leaderboard_results_league_label
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:background="@color/navbar_background" android:layout_width="match_parent" android:layout_height="wrap_content" android:elevation="4.000000dip">
  <FrameLayout android:id="@id/frameLayout" android:layout_width="0.000000dip" android:layout_height="@dimen/leaderboard_league_header_height" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <androidx.recyclerview.widget.RecyclerView android:layout_gravity="0x00000011" android:orientation="horizontal" android:id="@id/rv_leaderboard_result_leagues" android:layout_width="wrap_content" android:layout_height="match_parent" android:overScrollMode="2" app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager"/>
  </FrameLayout>
  <TextView android:textColor="@color/navbar_text" android:id="@id/tv_leaderboard_results_league_label" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/frameLayout" style="@style/TextLeaderboardLeagueHeader"/>
  <TextView android:textColor="@color/navbar_text" android:id="@id/tv_leaderboard_header_results_available_timer" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toBottomOf="@id/frameLayout" style="@style/TextP1"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
