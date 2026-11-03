# پروندهٔ لایه — `res/layout/set_daily_goal_card.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/set_daily_goal_card.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/set_daily_goal_card.xml`](../../SOURCE/res/layout/set_daily_goal_card.xml) |
| SHA-256 دیکد | `10e45d097cdf20d3d8d9c7a16f60b7d4dc2d10853c54c4543688f0f411193740` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.getmimo.ui.profile.view.SetDailyGoalCardItem  #@id/daily_goal_level_1
   ├─ View  #@id/line_daily_goal_level_1
   ├─ com.getmimo.ui.profile.view.SetDailyGoalCardItem  #@id/daily_goal_level_2
   ├─ View  #@id/line_daily_goal_level_2
   └─ com.getmimo.ui.profile.view.SetDailyGoalCardItem  #@id/daily_goal_level_3
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 3 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `android:id` | `@id/daily_goal_level_1` |
| 4 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `android:layout_width` | `0.000000dip` |
| 5 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `android:layout_height` | `@dimen/onboarding_set_goal_item_height` |
| 6 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `app:layout_constraintBottom_toTopOf` | `@id/line_daily_goal_level_1` |
| 7 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 8 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `app:layout_constraintRight_toRightOf` | `0` |
| 9 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `app:layout_constraintTop_toTopOf` | `0` |
| 10 | `View` | `android:id` | `@id/line_daily_goal_level_1` |
| 11 | `View` | `android:background` | `@color/line_primary` |
| 12 | `View` | `android:layout_width` | `0.000000dip` |
| 13 | `View` | `android:layout_height` | `1.000000dip` |
| 14 | `View` | `app:layout_constraintBottom_toTopOf` | `@id/daily_goal_level_2` |
| 15 | `View` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 16 | `View` | `app:layout_constraintRight_toRightOf` | `0` |
| 17 | `View` | `app:layout_constraintTop_toBottomOf` | `@id/daily_goal_level_1` |
| 18 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `android:id` | `@id/daily_goal_level_2` |
| 19 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `android:layout_width` | `0.000000dip` |
| 20 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `android:layout_height` | `@dimen/onboarding_set_goal_item_height` |
| 21 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `app:layout_constraintBottom_toTopOf` | `@id/line_daily_goal_level_2` |
| 22 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 23 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `app:layout_constraintRight_toRightOf` | `0` |
| 24 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `app:layout_constraintTop_toBottomOf` | `@id/line_daily_goal_level_1` |
| 25 | `View` | `android:id` | `@id/line_daily_goal_level_2` |
| 26 | `View` | `android:background` | `@color/line_primary` |
| 27 | `View` | `android:layout_width` | `0.000000dip` |
| 28 | `View` | `android:layout_height` | `1.000000dip` |
| 29 | `View` | `app:layout_constraintBottom_toTopOf` | `@id/daily_goal_level_3` |
| 30 | `View` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 31 | `View` | `app:layout_constraintRight_toRightOf` | `0` |
| 32 | `View` | `app:layout_constraintTop_toBottomOf` | `@id/daily_goal_level_2` |
| 33 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `android:id` | `@id/daily_goal_level_3` |
| 34 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `android:layout_width` | `0.000000dip` |
| 35 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `android:layout_height` | `@dimen/onboarding_set_goal_item_height` |
| 36 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 37 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `app:layout_constraintRight_toRightOf` | `0` |
| 38 | `com.getmimo.ui.profile.view.SetDailyGoalCardItem` | `app:layout_constraintTop_toBottomOf` | `@id/line_daily_goal_level_2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@dimen/onboarding_set_goal_item_height` | `56.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/daily_goal_level_1
@id/daily_goal_level_2
@id/daily_goal_level_3
@id/line_daily_goal_level_1
@id/line_daily_goal_level_2
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_width="match_parent" android:layout_height="wrap_content">
  <com.getmimo.ui.profile.view.SetDailyGoalCardItem android:id="@id/daily_goal_level_1" android:layout_width="0.000000dip" android:layout_height="@dimen/onboarding_set_goal_item_height" app:layout_constraintBottom_toTopOf="@id/line_daily_goal_level_1" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toTopOf="0"/>
  <View android:id="@id/line_daily_goal_level_1" android:background="@color/line_primary" android:layout_width="0.000000dip" android:layout_height="1.000000dip" app:layout_constraintBottom_toTopOf="@id/daily_goal_level_2" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toBottomOf="@id/daily_goal_level_1"/>
  <com.getmimo.ui.profile.view.SetDailyGoalCardItem android:id="@id/daily_goal_level_2" android:layout_width="0.000000dip" android:layout_height="@dimen/onboarding_set_goal_item_height" app:layout_constraintBottom_toTopOf="@id/line_daily_goal_level_2" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toBottomOf="@id/line_daily_goal_level_1"/>
  <View android:id="@id/line_daily_goal_level_2" android:background="@color/line_primary" android:layout_width="0.000000dip" android:layout_height="1.000000dip" app:layout_constraintBottom_toTopOf="@id/daily_goal_level_3" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toBottomOf="@id/daily_goal_level_2"/>
  <com.getmimo.ui.profile.view.SetDailyGoalCardItem android:id="@id/daily_goal_level_3" android:layout_width="0.000000dip" android:layout_height="@dimen/onboarding_set_goal_item_height" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toBottomOf="@id/line_daily_goal_level_2"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
