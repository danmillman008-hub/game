# پروندهٔ لایه — `res/layout/abtest_config_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abtest_config_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abtest_config_activity.xml`](../../SOURCE/res/layout/abtest_config_activity.xml) |
| SHA-256 دیکد | `c561084bf3f1062a96db8cd75b228ce8871ad18f269b544c9721d10418628bf0` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_abtest__config
   │  └─ include  #@id/layout_toolbar
   └─ androidx.recyclerview.widget.RecyclerView  #@id/rv_abtest_config
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:fitsSystemWindows` | `true` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_abtest__config` |
| 5 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/navbar_background` |
| 6 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 7 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 8 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 9 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 10 | `com.google.android.material.appbar.AppBarLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `include` | `android:id` | `@id/layout_toolbar` |
| 12 | `include` | `android:layout_width` | `match_parent` |
| 13 | `include` | `android:layout_height` | `wrap_content` |
| 14 | `include` | `android:title` | `@string/app_name` |
| 15 | `include` | `layout` | `@layout/toolbar` |
| 16 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_abtest_config` |
| 17 | `androidx.recyclerview.widget.RecyclerView` | `android:padding` | `16.000000dip` |
| 18 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `match_parent` |
| 19 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `0.000000dip` |
| 20 | `androidx.recyclerview.widget.RecyclerView` | `app:layoutManager` | `androidx.recyclerview.widget.LinearLayoutManager` |
| 21 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 22 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 23 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintStart_toStartOf` | `0` |
| 24 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintTop_toBottomOf` | `@id/appbar_abtest__config` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@string/app_name` | `Mimo` / `Mimo` (de) / `Mimo` (es) / `Mimo` (fr) / `Mimo` (in) / `Mimo` (it) / `Mimo` (pl) / `Mimo` (pt-rBR) / `Mimo` (ru) / `Mimo` (tr) |

## ۴. شناسه‌های `@id`

```text
@id/appbar_abtest__config
@id/layout_toolbar
@id/rv_abtest_config
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/toolbar
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.developermenu.abtest.ABTestConfigActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_abtest__config" android:background="@color/navbar_background" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="wrap_content" android:title="@string/app_name" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <androidx.recyclerview.widget.RecyclerView android:id="@id/rv_abtest_config" android:padding="16.000000dip" android:layout_width="match_parent" android:layout_height="0.000000dip" app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/appbar_abtest__config"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
