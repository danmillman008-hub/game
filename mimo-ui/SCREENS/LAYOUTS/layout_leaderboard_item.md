# پروندهٔ لایه — `res/layout/leaderboard_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_item.xml`](../../SOURCE/res/layout/leaderboard_item.xml) |
| SHA-256 دیکد | `a9a0214899903a49116de5efb9b4165a1bb2dbe183f332db16860dd7115fac80` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 16 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/root_leaderboard_podium_item
   ├─ TextView  #@id/tv_rank_leaderboard_item
   ├─ ImageView  #@id/iv_avatar_leaderboard_item
   ├─ TextView  #@id/tv_username_leaderboard_item
   ├─ TextView  #@id/tv_sparks_leaderboard_item
   └─ ImageView  #@id/iv_sparks_leaderboard_item
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/root_leaderboard_podium_item` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `60.000000dip` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 5 | `TextView` | `android:textColor` | `@color/text_primary` |
| 6 | `TextView` | `android:gravity` | `0x00000011` |
| 7 | `TextView` | `android:id` | `@id/tv_rank_leaderboard_item` |
| 8 | `TextView` | `android:layout_width` | `24.000000dip` |
| 9 | `TextView` | `android:layout_height` | `wrap_content` |
| 10 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 11 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 12 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `TextView` | `style` | `@style/TextSubtitle` |
| 15 | `ImageView` | `android:id` | `@id/iv_avatar_leaderboard_item` |
| 16 | `ImageView` | `android:layout_width` | `40.000000dip` |
| 17 | `ImageView` | `android:layout_height` | `40.000000dip` |
| 18 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_s` |
| 19 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 20 | `ImageView` | `app:layout_constraintStart_toEndOf` | `@id/tv_rank_leaderboard_item` |
| 21 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 22 | `ImageView` | `app:srcCompat` | `@drawable/mimo_gravatar` |
| 23 | `TextView` | `android:id` | `@id/tv_username_leaderboard_item` |
| 24 | `TextView` | `android:layout_width` | `0.000000dip` |
| 25 | `TextView` | `android:layout_height` | `wrap_content` |
| 26 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_s` |
| 27 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xxs` |
| 28 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 29 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/iv_sparks_leaderboard_item` |
| 30 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_avatar_leaderboard_item` |
| 31 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 32 | `TextView` | `style` | `@style/TextLeaderboardItemTitle` |
| 33 | `TextView` | `android:id` | `@id/tv_sparks_leaderboard_item` |
| 34 | `TextView` | `android:layout_width` | `wrap_content` |
| 35 | `TextView` | `android:layout_height` | `wrap_content` |
| 36 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 37 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 38 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 39 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 40 | `TextView` | `style` | `@style/TextLeaderboardItemTitle` |
| 41 | `ImageView` | `android:id` | `@id/iv_sparks_leaderboard_item` |
| 42 | `ImageView` | `android:layout_width` | `wrap_content` |
| 43 | `ImageView` | `android:layout_height` | `0.000000dip` |
| 44 | `ImageView` | `android:adjustViewBounds` | `true` |
| 45 | `ImageView` | `android:layout_marginEnd` | `@dimen/spacing_xxs` |
| 46 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/tv_sparks_leaderboard_item` |
| 47 | `ImageView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_sparks_leaderboard_item` |
| 48 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_sparks_leaderboard_item` |
| 49 | `ImageView` | `app:srcCompat` | `@drawable/ic_flash_filled` |
| 50 | `ImageView` | `app:tint` | `@color/support_yellow` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/support_yellow` | `#FFF4D055` / `#FFFBDF83` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@style/TextLeaderboardItemTitle` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}]` |
| `@style/TextSubtitle` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_avatar_leaderboard_item
@id/iv_sparks_leaderboard_item
@id/root_leaderboard_podium_item
@id/tv_rank_leaderboard_item
@id/tv_sparks_leaderboard_item
@id/tv_username_leaderboard_item
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
res/layout/chapter_finished_leaderboard_status.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/root_leaderboard_podium_item" android:layout_width="match_parent" android:layout_height="60.000000dip" android:foreground="?attr/selectableItemBackground">
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_rank_leaderboard_item" android:layout_width="24.000000dip" android:layout_height="wrap_content" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextSubtitle"/>
  <ImageView android:id="@id/iv_avatar_leaderboard_item" android:layout_width="40.000000dip" android:layout_height="40.000000dip" android:layout_marginStart="@dimen/spacing_s" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toEndOf="@id/tv_rank_leaderboard_item" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/mimo_gravatar"/>
  <TextView android:id="@id/tv_username_leaderboard_item" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginStart="@dimen/spacing_s" android:layout_marginEnd="@dimen/spacing_xxs" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/iv_sparks_leaderboard_item" app:layout_constraintStart_toEndOf="@id/iv_avatar_leaderboard_item" app:layout_constraintTop_toTopOf="0" style="@style/TextLeaderboardItemTitle"/>
  <TextView android:id="@id/tv_sparks_leaderboard_item" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextLeaderboardItemTitle"/>
  <ImageView android:id="@id/iv_sparks_leaderboard_item" android:layout_width="wrap_content" android:layout_height="0.000000dip" android:adjustViewBounds="true" android:layout_marginEnd="@dimen/spacing_xxs" app:layout_constraintBottom_toBottomOf="@id/tv_sparks_leaderboard_item" app:layout_constraintEnd_toStartOf="@id/tv_sparks_leaderboard_item" app:layout_constraintTop_toTopOf="@id/tv_sparks_leaderboard_item" app:srcCompat="@drawable/ic_flash_filled" app:tint="@color/support_yellow"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
