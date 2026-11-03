# پروندهٔ لایه — `res/layout/feature_introduction_modal_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/feature_introduction_modal_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/feature_introduction_modal_fragment.xml`](../../SOURCE/res/layout/feature_introduction_modal_fragment.xml) |
| SHA-256 دیکد | `99ea0e2278ae3ef4c52dba6de61b05f03a3052b0d2cf468923795a5c58281843` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 1 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_feature_introduction_modal
   ├─ include  #@id/base_modal_card
   └─ com.getmimo.ui.common.CutoutBackgroundView  #@id/cutout_view_feature_intro
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_feature_introduction_modal` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:fitsSystemWindows` | `true` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 5 | `include` | `android:id` | `@id/base_modal_card` |
| 6 | `include` | `layout` | `@layout/base_modal_card` |
| 7 | `com.getmimo.ui.common.CutoutBackgroundView` | `android:id` | `@id/cutout_view_feature_intro` |
| 8 | `com.getmimo.ui.common.CutoutBackgroundView` | `android:fitsSystemWindows` | `true` |
| 9 | `com.getmimo.ui.common.CutoutBackgroundView` | `android:layout_width` | `0.000000dip` |
| 10 | `com.getmimo.ui.common.CutoutBackgroundView` | `android:layout_height` | `0.000000dip` |
| 11 | `com.getmimo.ui.common.CutoutBackgroundView` | `app:bg_color` | `@color/cutout_view_default_background` |
| 12 | `com.getmimo.ui.common.CutoutBackgroundView` | `app:cutout_color` | `@color/white` |
| 13 | `com.getmimo.ui.common.CutoutBackgroundView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 14 | `com.getmimo.ui.common.CutoutBackgroundView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 15 | `com.getmimo.ui.common.CutoutBackgroundView` | `app:layout_constraintStart_toStartOf` | `0` |
| 16 | `com.getmimo.ui.common.CutoutBackgroundView` | `app:layout_constraintTop_toTopOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/cutout_view_default_background` | `#66000000` |
| `@color/white` | `#FFFFFFFF` |

## ۴. شناسه‌های `@id`

```text
@id/base_modal_card
@id/cutout_view_feature_intro
@id/layout_feature_introduction_modal
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/base_modal_card
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.onboarding.step1.IntroductionFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/layout_feature_introduction_modal" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <include android:id="@id/base_modal_card" layout="@layout/base_modal_card"/>
  <com.getmimo.ui.common.CutoutBackgroundView android:id="@id/cutout_view_feature_intro" android:fitsSystemWindows="true" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:bg_color="@color/cutout_view_default_background" app:cutout_color="@color/white" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
