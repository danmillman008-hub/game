# پروندهٔ لایه — `res/layout/intro_slides_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/intro_slides_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/intro_slides_activity.xml`](../../SOURCE/res/layout/intro_slides_activity.xml) |
| SHA-256 دیکد | `6e7640e73fa9c3b4cfcbb6e1573688f05b4d3f2ec1b4b10fc351107b3d30a6ca` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ androidx.viewpager.widget.ViewPager  #@id/vp_intro_slides
   ├─ com.getmimo.ui.common.ViewPagerIndicator  #@id/vp_indicator
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:fitsSystemWindows` | `true` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 6 | `androidx.viewpager.widget.ViewPager` | `android:id` | `@id/vp_intro_slides` |
| 7 | `androidx.viewpager.widget.ViewPager` | `android:layout_width` | `match_parent` |
| 8 | `androidx.viewpager.widget.ViewPager` | `android:layout_height` | `0.000000dip` |
| 9 | `androidx.viewpager.widget.ViewPager` | `app:layout_constraintBottom_toTopOf` | `@id/vp_indicator` |
| 10 | `androidx.viewpager.widget.ViewPager` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:gravity` | `0x00000010` |
| 12 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:id` | `@id/vp_indicator` |
| 13 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:layout_width` | `wrap_content` |
| 14 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:layout_height` | `wrap_content` |
| 15 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:layout_marginVertical` | `@dimen/onboarding_container_intro_slides_dots_margin_vertical` |
| 16 | `com.getmimo.ui.common.ViewPagerIndicator` | `app:layout_constraintBottom_toTopOf` | `@id/compose_content` |
| 17 | `com.getmimo.ui.common.ViewPagerIndicator` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 18 | `com.getmimo.ui.common.ViewPagerIndicator` | `app:layout_constraintRight_toRightOf` | `0` |
| 19 | `com.getmimo.ui.common.ViewPagerIndicator` | `app:layout_constraintTop_toBottomOf` | `@id/vp_intro_slides` |
| 20 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/compose_content` |
| 21 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 22 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 23 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 24 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 25 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@dimen/onboarding_container_intro_slides_dots_margin_vertical` | `24.000000dip` / `24.000000dip` (sw320dp-xhdpi) / `32.000000dip` (sw320dp-xxhdpi) / `32.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/compose_content
@id/vp_indicator
@id/vp_intro_slides
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.onboarding.intro.IntroSlidesActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000011" android:background="@color/background_primary" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.viewpager.widget.ViewPager android:id="@id/vp_intro_slides" android:layout_width="match_parent" android:layout_height="0.000000dip" app:layout_constraintBottom_toTopOf="@id/vp_indicator" app:layout_constraintTop_toTopOf="0"/>
  <com.getmimo.ui.common.ViewPagerIndicator android:gravity="0x00000010" android:id="@id/vp_indicator" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginVertical="@dimen/onboarding_container_intro_slides_dots_margin_vertical" app:layout_constraintBottom_toTopOf="@id/compose_content" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toBottomOf="@id/vp_intro_slides"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/compose_content" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
