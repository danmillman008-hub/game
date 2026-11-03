# پروندهٔ لایه — `res/layout/leaderboard_fragment_locked.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_fragment_locked.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_fragment_locked.xml`](../../SOURCE/res/layout/leaderboard_fragment_locked.xml) |
| SHA-256 دیکد | `2206bccf3b8d1acc8e1a2b1ca32436f07b8e615cc92442ee8bd92d59d604d883` |
| ریشه | `LinearLayout` |
| تعداد گره | 8 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 15 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ com.getmimo.ui.leaderboard.LeaderboardLeagueHeaderView  #@id/leaderboard_league_header_view_locked
   ├─ Space
   ├─ ImageView  #@id/iv_leaderboard_fragment_locked_illustration
   ├─ TextView  #@id/tv_leaderboard_fragment_locked_header
   ├─ TextView  #@id/tv_leaderboard_fragment_locked_message
   ├─ Space
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_leaderboard_fragment_locked_jump_into_lesson
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:background` | `@color/background_primary` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 5 | `com.getmimo.ui.leaderboard.LeaderboardLeagueHeaderView` | `android:id` | `@id/leaderboard_league_header_view_locked` |
| 6 | `com.getmimo.ui.leaderboard.LeaderboardLeagueHeaderView` | `android:layout_width` | `match_parent` |
| 7 | `com.getmimo.ui.leaderboard.LeaderboardLeagueHeaderView` | `android:layout_height` | `wrap_content` |
| 8 | `Space` | `android:layout_width` | `wrap_content` |
| 9 | `Space` | `android:layout_height` | `0.000000dip` |
| 10 | `Space` | `android:layout_weight` | `1.000000` |
| 11 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 12 | `ImageView` | `android:id` | `@id/iv_leaderboard_fragment_locked_illustration` |
| 13 | `ImageView` | `android:layout_width` | `wrap_content` |
| 14 | `ImageView` | `android:layout_height` | `120.000000dip` |
| 15 | `ImageView` | `android:adjustViewBounds` | `true` |
| 16 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 17 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 18 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 19 | `ImageView` | `app:srcCompat` | `@drawable/ic_leaderboard_locked` |
| 20 | `TextView` | `android:textColor` | `@color/text_primary` |
| 21 | `TextView` | `android:layout_gravity` | `0x00000011` |
| 22 | `TextView` | `android:id` | `@id/tv_leaderboard_fragment_locked_header` |
| 23 | `TextView` | `android:layout_width` | `wrap_content` |
| 24 | `TextView` | `android:layout_height` | `wrap_content` |
| 25 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 26 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 27 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 28 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_leaderboard_fragment_locked_illustration` |
| 29 | `TextView` | `style` | `@style/TextH1` |
| 30 | `TextView` | `android:textColor` | `@color/text_weak` |
| 31 | `TextView` | `android:gravity` | `0x00000011` |
| 32 | `TextView` | `android:id` | `@id/tv_leaderboard_fragment_locked_message` |
| 33 | `TextView` | `android:layout_width` | `match_parent` |
| 34 | `TextView` | `android:layout_height` | `wrap_content` |
| 35 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 36 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 37 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 38 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 39 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_leaderboard_fragment_locked_header` |
| 40 | `TextView` | `style` | `@style/TextP1` |
| 41 | `Space` | `android:layout_width` | `wrap_content` |
| 42 | `Space` | `android:layout_height` | `0.000000dip` |
| 43 | `Space` | `android:layout_weight` | `1.000000` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_leaderboard_fragment_locked_jump_into_lesson` |
| 45 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 47 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 48 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_leaderboard_fragment_locked_jump_into_lesson
@id/iv_leaderboard_fragment_locked_illustration
@id/leaderboard_league_header_view_locked
@id/tv_leaderboard_fragment_locked_header
@id/tv_leaderboard_fragment_locked_message
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
<LinearLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.getmimo.ui.leaderboard.LeaderboardLeagueHeaderView android:id="@id/leaderboard_league_header_view_locked" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  <Space android:layout_width="wrap_content" android:layout_height="0.000000dip" android:layout_weight="1.000000"/>
  <ImageView android:layout_gravity="0x00000011" android:id="@id/iv_leaderboard_fragment_locked_illustration" android:layout_width="wrap_content" android:layout_height="120.000000dip" android:adjustViewBounds="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_leaderboard_locked"/>
  <TextView android:textColor="@color/text_primary" android:layout_gravity="0x00000011" android:id="@id/tv_leaderboard_fragment_locked_header" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_leaderboard_fragment_locked_illustration" style="@style/TextH1"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_leaderboard_fragment_locked_message" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_leaderboard_fragment_locked_header" style="@style/TextP1"/>
  <Space android:layout_width="wrap_content" android:layout_height="0.000000dip" android:layout_weight="1.000000"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_leaderboard_fragment_locked_jump_into_lesson" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m" android:layout_marginHorizontal="@dimen/spacing_m_expandable"/>
</LinearLayout>
```
