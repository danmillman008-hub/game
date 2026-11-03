# پروندهٔ لایه — `res/layout/upgrade_modal_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/upgrade_modal_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/upgrade_modal_activity.xml`](../../SOURCE/res/layout/upgrade_modal_activity.xml) |
| SHA-256 دیکد | `33bdf227417db0daf765609ffb0b971033a305f180a925fe9658e3ee2e8d09d3` |
| ریشه | `FrameLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 2 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 14 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/fl_main
   └─ com.google.android.material.card.MaterialCardView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ ImageButton  #@id/iv_upgrade_modal_close
         ├─ androidx.viewpager2.widget.ViewPager2  #@id/vp_in_app
         ├─ com.getmimo.ui.common.ViewPagerIndicator  #@id/vpi_in_app
         └─ com.getmimo.ui.upgrade.UpgradeModalBottomView  #@id/upgrade_modal_bottom_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:id` | `@id/fl_main` |
| 2 | `FrameLayout` | `android:background` | `@color/generic_backdrop_color` |
| 3 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 4 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 5 | `com.google.android.material.card.MaterialCardView` | `android:layout_gravity` | `0x00000011` |
| 6 | `com.google.android.material.card.MaterialCardView` | `android:layout_width` | `@dimen/modal_default_width` |
| 7 | `com.google.android.material.card.MaterialCardView` | `android:layout_height` | `wrap_content` |
| 8 | `com.google.android.material.card.MaterialCardView` | `app:cardCornerRadius` | `@dimen/cardview_corner_radius_large` |
| 9 | `com.google.android.material.card.MaterialCardView` | `app:cardUseCompatPadding` | `true` |
| 10 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_secondary` |
| 11 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 12 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 13 | `ImageButton` | `android:id` | `@id/iv_upgrade_modal_close` |
| 14 | `ImageButton` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 15 | `ImageButton` | `android:padding` | `@dimen/modal_default_close_button_padding` |
| 16 | `ImageButton` | `android:layout_width` | `wrap_content` |
| 17 | `ImageButton` | `android:layout_height` | `wrap_content` |
| 18 | `ImageButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 19 | `ImageButton` | `app:layout_constraintTop_toTopOf` | `0` |
| 20 | `ImageButton` | `app:srcCompat` | `@drawable/ic_close` |
| 21 | `ImageButton` | `app:tint` | `@color/icon_weak` |
| 22 | `androidx.viewpager2.widget.ViewPager2` | `android:id` | `@id/vp_in_app` |
| 23 | `androidx.viewpager2.widget.ViewPager2` | `android:clipToPadding` | `false` |
| 24 | `androidx.viewpager2.widget.ViewPager2` | `android:layout_width` | `match_parent` |
| 25 | `androidx.viewpager2.widget.ViewPager2` | `android:layout_height` | `wrap_content` |
| 26 | `androidx.viewpager2.widget.ViewPager2` | `android:layout_marginTop` | `40.000000dip` |
| 27 | `androidx.viewpager2.widget.ViewPager2` | `app:layout_constraintBottom_toTopOf` | `@id/vpi_in_app` |
| 28 | `androidx.viewpager2.widget.ViewPager2` | `app:layout_constraintTop_toTopOf` | `0` |
| 29 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:id` | `@id/vpi_in_app` |
| 30 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:layout_width` | `wrap_content` |
| 31 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:layout_height` | `wrap_content` |
| 32 | `com.getmimo.ui.common.ViewPagerIndicator` | `android:layout_marginTop` | `@dimen/modal_upgrade_description_margin_bottom` |
| 33 | `com.getmimo.ui.common.ViewPagerIndicator` | `app:layout_constraintEnd_toEndOf` | `0` |
| 34 | `com.getmimo.ui.common.ViewPagerIndicator` | `app:layout_constraintStart_toStartOf` | `0` |
| 35 | `com.getmimo.ui.common.ViewPagerIndicator` | `app:layout_constraintTop_toBottomOf` | `@id/vp_in_app` |
| 36 | `com.getmimo.ui.upgrade.UpgradeModalBottomView` | `android:id` | `@id/upgrade_modal_bottom_view` |
| 37 | `com.getmimo.ui.upgrade.UpgradeModalBottomView` | `android:layout_width` | `match_parent` |
| 38 | `com.getmimo.ui.upgrade.UpgradeModalBottomView` | `android:layout_height` | `wrap_content` |
| 39 | `com.getmimo.ui.upgrade.UpgradeModalBottomView` | `app:layout_constraintTop_toBottomOf` | `@id/vpi_in_app` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/generic_backdrop_color` | `#88000000` |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@dimen/cardview_corner_radius_large` | `12.000000dip` |
| `@dimen/modal_default_close_button_padding` | `12.000000dip` |
| `@dimen/modal_default_width` | `296.000000dip` / `360.000000dip` (sw600dp) |
| `@dimen/modal_upgrade_description_margin_bottom` | `16.000000dip` / `20.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/fl_main
@id/iv_upgrade_modal_close
@id/upgrade_modal_bottom_view
@id/vp_in_app
@id/vpi_in_app
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.upgrade.UpgradeModalActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/fl_main" android:background="@color/generic_backdrop_color" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.card.MaterialCardView android:layout_gravity="0x00000011" android:layout_width="@dimen/modal_default_width" android:layout_height="wrap_content" app:cardCornerRadius="@dimen/cardview_corner_radius_large" app:cardUseCompatPadding="true">
    <androidx.constraintlayout.widget.ConstraintLayout android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="wrap_content">
      <ImageButton android:id="@id/iv_upgrade_modal_close" android:background="?attr/selectableItemBackgroundBorderless" android:padding="@dimen/modal_default_close_button_padding" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_close" app:tint="@color/icon_weak"/>
      <androidx.viewpager2.widget.ViewPager2 android:id="@id/vp_in_app" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="40.000000dip" app:layout_constraintBottom_toTopOf="@id/vpi_in_app" app:layout_constraintTop_toTopOf="0"/>
      <com.getmimo.ui.common.ViewPagerIndicator android:id="@id/vpi_in_app" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/modal_upgrade_description_margin_bottom" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/vp_in_app"/>
      <com.getmimo.ui.upgrade.UpgradeModalBottomView android:id="@id/upgrade_modal_bottom_view" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintTop_toBottomOf="@id/vpi_in_app"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </com.google.android.material.card.MaterialCardView>
</FrameLayout>
```
