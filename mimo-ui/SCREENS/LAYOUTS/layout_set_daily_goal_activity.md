# پروندهٔ لایه — `res/layout/set_daily_goal_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/set_daily_goal_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/set_daily_goal_activity.xml`](../../SOURCE/res/layout/set_daily_goal_activity.xml) |
| SHA-256 دیکد | `61ea36a7df507d2a0d4667a4caf45c31f3349d2b6db38b07ac9c301b527fcfa4` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 2 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_daily_goal_settings
   │  └─ include  #@id/layout_toolbar
   ├─ com.getmimo.ui.streaks.DailySparksGoalProgressView  #@id/pb_set_daily_goal
   ├─ com.getmimo.ui.profile.view.SetDailyGoalCard  #@id/layout_daily_goal_card
   └─ androidx.compose.ui.platform.ComposeView  #@id/button_daily_goal_continue
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:fitsSystemWindows` | `false` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 5 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_daily_goal_settings` |
| 6 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/navbar_background` |
| 7 | `com.google.android.material.appbar.AppBarLayout` | `android:fitsSystemWindows` | `true` |
| 8 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 9 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 10 | `com.google.android.material.appbar.AppBarLayout` | `app:elevation` | `0.000000dip` |
| 11 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 12 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `include` | `android:id` | `@id/layout_toolbar` |
| 15 | `include` | `android:layout_width` | `match_parent` |
| 16 | `include` | `android:layout_height` | `wrap_content` |
| 17 | `include` | `layout` | `@layout/toolbar` |
| 18 | `com.getmimo.ui.streaks.DailySparksGoalProgressView` | `android:id` | `@id/pb_set_daily_goal` |
| 19 | `com.getmimo.ui.streaks.DailySparksGoalProgressView` | `android:layout_width` | `200.000000dip` |
| 20 | `com.getmimo.ui.streaks.DailySparksGoalProgressView` | `android:layout_height` | `200.000000dip` |
| 21 | `com.getmimo.ui.streaks.DailySparksGoalProgressView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 22 | `com.getmimo.ui.streaks.DailySparksGoalProgressView` | `app:layout_constraintBottom_toTopOf` | `@id/layout_daily_goal_card` |
| 23 | `com.getmimo.ui.streaks.DailySparksGoalProgressView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 24 | `com.getmimo.ui.streaks.DailySparksGoalProgressView` | `app:layout_constraintStart_toStartOf` | `0` |
| 25 | `com.getmimo.ui.streaks.DailySparksGoalProgressView` | `app:layout_constraintTop_toBottomOf` | `@id/appbar_daily_goal_settings` |
| 26 | `com.getmimo.ui.streaks.DailySparksGoalProgressView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 27 | `com.getmimo.ui.streaks.DailySparksGoalProgressView` | `app:text_style` | `1` |
| 28 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:id` | `@id/layout_daily_goal_card` |
| 29 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:background` | `@drawable/rounded_background_secondary` |
| 30 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:layout_width` | `0.000000dip` |
| 31 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:layout_height` | `wrap_content` |
| 32 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:elevation` | `1.000000dip` |
| 33 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:layout_marginHorizontal` | `@dimen/spacing_s` |
| 34 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `android:layout_marginVertical` | `@dimen/spacing_l` |
| 35 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `app:layout_constraintBottom_toTopOf` | `@id/button_daily_goal_continue` |
| 36 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `app:layout_constraintEnd_toEndOf` | `0` |
| 37 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `app:layout_constraintStart_toStartOf` | `0` |
| 38 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `app:layout_constraintTop_toBottomOf` | `@id/pb_set_daily_goal` |
| 39 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `app:layout_constraintVertical_chainStyle` | `2` |
| 40 | `com.getmimo.ui.profile.view.SetDailyGoalCard` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 41 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/button_daily_goal_continue` |
| 42 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 43 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 44 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_s` |
| 45 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginVertical` | `@dimen/spacing_m` |
| 46 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 47 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 48 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 49 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `360.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/appbar_daily_goal_settings
@id/button_daily_goal_continue
@id/layout_daily_goal_card
@id/layout_toolbar
@id/pb_set_daily_goal
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/toolbar
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.profile.SetDailyGoalActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:background="@color/background_primary" android:fitsSystemWindows="false" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_daily_goal_settings" android:background="@color/navbar_background" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="wrap_content" app:elevation="0.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="wrap_content" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <com.getmimo.ui.streaks.DailySparksGoalProgressView android:id="@id/pb_set_daily_goal" android:layout_width="200.000000dip" android:layout_height="200.000000dip" android:layout_marginTop="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/layout_daily_goal_card" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/appbar_daily_goal_settings" app:layout_constraintVertical_chainStyle="2" app:text_style="1"/>
  <com.getmimo.ui.profile.view.SetDailyGoalCard android:id="@id/layout_daily_goal_card" android:background="@drawable/rounded_background_secondary" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:elevation="1.000000dip" android:layout_marginHorizontal="@dimen/spacing_s" android:layout_marginVertical="@dimen/spacing_l" app:layout_constraintBottom_toTopOf="@id/button_daily_goal_continue" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/pb_set_daily_goal" app:layout_constraintVertical_chainStyle="2" app:layout_constraintWidth_max="@dimen/general_max_width"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/button_daily_goal_continue" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_s" android:layout_marginVertical="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="360.000000dip"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
