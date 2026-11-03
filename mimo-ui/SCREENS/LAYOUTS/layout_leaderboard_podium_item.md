# پروندهٔ لایه — `res/layout/leaderboard_podium_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_podium_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_podium_item.xml`](../../SOURCE/res/layout/leaderboard_podium_item.xml) |
| SHA-256 دیکد | `2c87839098616eaba21b6b6465355559764c4255966e9e33d5a0ce55e4ce96b4` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 15 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/root_leaderboard_podium_item
   ├─ ImageView  #@id/iv_medal_leaderboard_podium_item
   ├─ ImageView  #@id/iv_avatar_leaderboard_podium_item
   ├─ TextView  #@id/tv_username_leaderboard_podium_item
   ├─ TextView  #@id/tv_sparks_leaderboard_podium_item
   └─ ImageView  #@id/iv_sparks_leaderboard_podium_item
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/root_leaderboard_podium_item` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `60.000000dip` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 5 | `ImageView` | `android:id` | `@id/iv_medal_leaderboard_podium_item` |
| 6 | `ImageView` | `android:layout_width` | `24.000000dip` |
| 7 | `ImageView` | `android:layout_height` | `24.000000dip` |
| 8 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 9 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 10 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 11 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 12 | `ImageView` | `app:srcCompat` | `@drawable/ic_award_leaderboard_first` |
| 13 | `ImageView` | `android:id` | `@id/iv_avatar_leaderboard_podium_item` |
| 14 | `ImageView` | `android:layout_width` | `40.000000dip` |
| 15 | `ImageView` | `android:layout_height` | `40.000000dip` |
| 16 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_s` |
| 17 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 18 | `ImageView` | `app:layout_constraintStart_toEndOf` | `@id/iv_medal_leaderboard_podium_item` |
| 19 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 20 | `ImageView` | `app:srcCompat` | `@drawable/avatar_fallback_6` |
| 21 | `TextView` | `android:id` | `@id/tv_username_leaderboard_podium_item` |
| 22 | `TextView` | `android:layout_width` | `0.000000dip` |
| 23 | `TextView` | `android:layout_height` | `wrap_content` |
| 24 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_s` |
| 25 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xxs` |
| 26 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 27 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/iv_sparks_leaderboard_podium_item` |
| 28 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_avatar_leaderboard_podium_item` |
| 29 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 30 | `TextView` | `style` | `@style/TextLeaderboardItemTitle` |
| 31 | `TextView` | `android:id` | `@id/tv_sparks_leaderboard_podium_item` |
| 32 | `TextView` | `android:layout_width` | `wrap_content` |
| 33 | `TextView` | `android:layout_height` | `wrap_content` |
| 34 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 35 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 36 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 37 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 38 | `TextView` | `style` | `@style/TextLeaderboardItemTitle` |
| 39 | `ImageView` | `android:id` | `@id/iv_sparks_leaderboard_podium_item` |
| 40 | `ImageView` | `android:layout_width` | `wrap_content` |
| 41 | `ImageView` | `android:layout_height` | `0.000000dip` |
| 42 | `ImageView` | `android:adjustViewBounds` | `true` |
| 43 | `ImageView` | `android:layout_marginEnd` | `@dimen/spacing_xxs` |
| 44 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/tv_sparks_leaderboard_podium_item` |
| 45 | `ImageView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_sparks_leaderboard_podium_item` |
| 46 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_sparks_leaderboard_podium_item` |
| 47 | `ImageView` | `app:srcCompat` | `@drawable/ic_flash_filled` |
| 48 | `ImageView` | `app:tint` | `@color/support_yellow` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/support_yellow` | `#FFF4D055` / `#FFFBDF83` (night) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@style/TextLeaderboardItemTitle` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/iv_avatar_leaderboard_podium_item
@id/iv_medal_leaderboard_podium_item
@id/iv_sparks_leaderboard_podium_item
@id/root_leaderboard_podium_item
@id/tv_sparks_leaderboard_podium_item
@id/tv_username_leaderboard_podium_item
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/root_leaderboard_podium_item" android:layout_width="match_parent" android:layout_height="60.000000dip" android:foreground="?attr/selectableItemBackground">
  <ImageView android:id="@id/iv_medal_leaderboard_podium_item" android:layout_width="24.000000dip" android:layout_height="24.000000dip" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_award_leaderboard_first"/>
  <ImageView android:id="@id/iv_avatar_leaderboard_podium_item" android:layout_width="40.000000dip" android:layout_height="40.000000dip" android:layout_marginStart="@dimen/spacing_s" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toEndOf="@id/iv_medal_leaderboard_podium_item" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/avatar_fallback_6"/>
  <TextView android:id="@id/tv_username_leaderboard_podium_item" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginStart="@dimen/spacing_s" android:layout_marginEnd="@dimen/spacing_xxs" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/iv_sparks_leaderboard_podium_item" app:layout_constraintStart_toEndOf="@id/iv_avatar_leaderboard_podium_item" app:layout_constraintTop_toTopOf="0" style="@style/TextLeaderboardItemTitle"/>
  <TextView android:id="@id/tv_sparks_leaderboard_podium_item" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextLeaderboardItemTitle"/>
  <ImageView android:id="@id/iv_sparks_leaderboard_podium_item" android:layout_width="wrap_content" android:layout_height="0.000000dip" android:adjustViewBounds="true" android:layout_marginEnd="@dimen/spacing_xxs" app:layout_constraintBottom_toBottomOf="@id/tv_sparks_leaderboard_podium_item" app:layout_constraintEnd_toStartOf="@id/tv_sparks_leaderboard_podium_item" app:layout_constraintTop_toTopOf="@id/tv_sparks_leaderboard_podium_item" app:srcCompat="@drawable/ic_flash_filled" app:tint="@color/support_yellow"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
