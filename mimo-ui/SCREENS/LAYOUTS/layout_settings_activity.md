# پروندهٔ لایه — `res/layout/settings_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/settings_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/settings_activity.xml`](../../SOURCE/res/layout/settings_activity.xml) |
| SHA-256 دیکد | `a3bffedb8399dcad7972236eeb017d6dc4728879def37ec94edbffc74c6cc05d` |
| ریشه | `androidx.coordinatorlayout.widget.CoordinatorLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.coordinatorlayout.widget.CoordinatorLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_settings
   │  └─ include  #@id/layout_toolbar
   └─ fragment  #@id/fragment_settings
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_height` | `match_parent` |
| 3 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_settings` |
| 4 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/navbar_background` |
| 5 | `com.google.android.material.appbar.AppBarLayout` | `android:fitsSystemWindows` | `true` |
| 6 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 7 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 8 | `com.google.android.material.appbar.AppBarLayout` | `app:elevation` | `0.000000dip` |
| 9 | `include` | `android:id` | `@id/layout_toolbar` |
| 10 | `include` | `android:layout_width` | `match_parent` |
| 11 | `include` | `android:layout_height` | `@dimen/toolbar_height` |
| 12 | `include` | `layout` | `@layout/toolbar` |
| 13 | `fragment` | `android:name` | `com.getmimo.ui.settings.SettingsFragment` |
| 14 | `fragment` | `android:id` | `@id/fragment_settings` |
| 15 | `fragment` | `android:layout_width` | `match_parent` |
| 16 | `fragment` | `android:layout_height` | `match_parent` |
| 17 | `fragment` | `app:layout_behavior` | `@string/appbar_scrolling_view_behavior` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@dimen/toolbar_height` | `56.000000dip` |
| `@string/appbar_scrolling_view_behavior` | `com.google.android.material.appbar.AppBarLayout$ScrollingViewBehavior` |

## ۴. شناسه‌های `@id`

```text
@id/appbar_settings
@id/fragment_settings
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
com.getmimo.ui.settings.SettingsActivity
com.getmimo.ui.settings.SettingsFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_settings" android:background="@color/navbar_background" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="wrap_content" app:elevation="0.000000dip">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="@dimen/toolbar_height" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <fragment android:name="com.getmimo.ui.settings.SettingsFragment" android:id="@id/fragment_settings" android:layout_width="match_parent" android:layout_height="match_parent" app:layout_behavior="@string/appbar_scrolling_view_behavior"/>
</androidx.coordinatorlayout.widget.CoordinatorLayout>
```
