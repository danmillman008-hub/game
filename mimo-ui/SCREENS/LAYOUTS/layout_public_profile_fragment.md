# پروندهٔ لایه — `res/layout/public_profile_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/public_profile_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/public_profile_fragment.xml`](../../SOURCE/res/layout/public_profile_fragment.xml) |
| SHA-256 دیکد | `675b4a7181cdc9cfe95f1c004becca711b9ecfa2fb91058867a520b8839e1820` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_profile_root
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_profile
   │  └─ include  #@id/layout_toolbar
   ├─ androidx.recyclerview.widget.RecyclerView  #@id/rv_profile
   └─ com.getmimo.ui.components.common.OfflineView  #@id/profile_offline_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_profile_root` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/navbar_background` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:fitsSystemWindows` | `true` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 6 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_profile` |
| 7 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/navbar_background` |
| 8 | `com.google.android.material.appbar.AppBarLayout` | `android:fitsSystemWindows` | `true` |
| 9 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 10 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 11 | `com.google.android.material.appbar.AppBarLayout` | `app:elevation` | `0.000000dip` |
| 12 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 13 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 14 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 15 | `include` | `android:id` | `@id/layout_toolbar` |
| 16 | `include` | `android:layout_width` | `match_parent` |
| 17 | `include` | `android:layout_height` | `@dimen/toolbar_height` |
| 18 | `include` | `layout` | `@layout/toolbar` |
| 19 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_profile` |
| 20 | `androidx.recyclerview.widget.RecyclerView` | `android:background` | `@color/background_primary` |
| 21 | `androidx.recyclerview.widget.RecyclerView` | `android:clipToPadding` | `false` |
| 22 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `0.000000dip` |
| 23 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `0.000000dip` |
| 24 | `androidx.recyclerview.widget.RecyclerView` | `app:layoutManager` | `androidx.recyclerview.widget.LinearLayoutManager` |
| 25 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 26 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 27 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintStart_toStartOf` | `0` |
| 28 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintTop_toBottomOf` | `@id/appbar_profile` |
| 29 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintWidth_max` | `@dimen/content_max_width` |
| 30 | `com.getmimo.ui.components.common.OfflineView` | `android:id` | `@id/profile_offline_view` |
| 31 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_width` | `wrap_content` |
| 32 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_height` | `wrap_content` |
| 33 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 34 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 35 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintStart_toStartOf` | `0` |
| 36 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintTop_toBottomOf` | `@id/appbar_profile` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@dimen/content_max_width` | `608.000000dip` |
| `@dimen/toolbar_height` | `56.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/appbar_profile
@id/layout_profile_root
@id/layout_toolbar
@id/profile_offline_view
@id/rv_profile
```

## ۵. ارجاع به لایه‌های دیگر

```text
@dimen/toolbar_height
@layout/toolbar
match_parent
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.profile.main.ProfileFragment
com.getmimo.ui.publicprofile.PublicProfileActivity
com.getmimo.ui.publicprofile.PublicProfileFragment$collectData$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/layout_profile_root" android:background="@color/navbar_background" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_profile" android:background="@color/navbar_background" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="wrap_content" app:elevation="0.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="@dimen/toolbar_height" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <androidx.recyclerview.widget.RecyclerView android:id="@id/rv_profile" android:background="@color/background_primary" android:clipToPadding="false" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/appbar_profile" app:layout_constraintWidth_max="@dimen/content_max_width"/>
  <com.getmimo.ui.components.common.OfflineView android:id="@id/profile_offline_view" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/appbar_profile"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
