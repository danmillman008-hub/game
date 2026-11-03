# پروندهٔ لایه — `res/layout/practice_tab_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/practice_tab_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/practice_tab_fragment.xml`](../../SOURCE/res/layout/practice_tab_fragment.xml) |
| SHA-256 دیکد | `8efac79ed4678f59e78e7a71be48f41cfe403ece21443af5dff377c7e674ed5d` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_practice_tab
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_practice
   │  └─ include  #@id/layout_toolbar
   └─ com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView  #@id/anonymous_user_lock_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 3 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cv_practice_tab` |
| 4 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `visible` |
| 5 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 6 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `0.000000dip` |
| 7 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 8 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 9 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 10 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/appbar_practice` |
| 11 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_practice` |
| 12 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/navbar_background` |
| 13 | `com.google.android.material.appbar.AppBarLayout` | `android:visibility` | `gone` |
| 14 | `com.google.android.material.appbar.AppBarLayout` | `android:fitsSystemWindows` | `true` |
| 15 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `0.000000dip` |
| 16 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 17 | `com.google.android.material.appbar.AppBarLayout` | `app:elevation` | `0.000000dip` |
| 18 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 19 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 20 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 21 | `include` | `android:id` | `@id/layout_toolbar` |
| 22 | `include` | `android:layout_width` | `match_parent` |
| 23 | `include` | `android:layout_height` | `@dimen/toolbar_height` |
| 24 | `include` | `layout` | `@layout/toolbar` |
| 25 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:id` | `@id/anonymous_user_lock_view` |
| 26 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:visibility` | `gone` |
| 27 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:layout_width` | `0.000000dip` |
| 28 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:layout_height` | `0.000000dip` |
| 29 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 30 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 31 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintStart_toStartOf` | `0` |
| 32 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintTop_toBottomOf` | `@id/appbar_practice` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@dimen/toolbar_height` | `56.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/anonymous_user_lock_view
@id/appbar_practice
@id/cv_practice_tab
@id/layout_toolbar
```

## ۵. ارجاع به لایه‌های دیگر

```text
@dimen/toolbar_height
@layout/toolbar
match_parent
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.practice.PracticeTabFragment$onViewCreated$5$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.compose.ui.platform.ComposeView android:id="@id/cv_practice_tab" android:visibility="visible" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/appbar_practice"/>
  <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_practice" android:background="@color/navbar_background" android:visibility="gone" android:fitsSystemWindows="true" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:elevation="0.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="@dimen/toolbar_height" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView android:id="@id/anonymous_user_lock_view" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/appbar_practice"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
