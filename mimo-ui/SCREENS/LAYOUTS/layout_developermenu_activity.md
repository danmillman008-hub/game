# پروندهٔ لایه — `res/layout/developermenu_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/developermenu_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/developermenu_activity.xml`](../../SOURCE/res/layout/developermenu_activity.xml) |
| SHA-256 دیکد | `8753ecaee70526b106aaecc2fc7aeb66ac5fa32cb17cac43be7fa43e230a6153` |
| ریشه | `androidx.coordinatorlayout.widget.CoordinatorLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.coordinatorlayout.widget.CoordinatorLayout  #@id/developer_menu_root
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_developermenu
   │  └─ include  #@id/layout_toolbar
   └─ fragment  #@id/fragment_developermenu
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:id` | `@id/developer_menu_root` |
| 2 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:fitsSystemWindows` | `true` |
| 3 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_height` | `match_parent` |
| 5 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_developermenu` |
| 6 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/background_secondary` |
| 7 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 8 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 9 | `include` | `android:id` | `@id/layout_toolbar` |
| 10 | `include` | `android:layout_width` | `match_parent` |
| 11 | `include` | `android:layout_height` | `wrap_content` |
| 12 | `include` | `android:title` | `@string/app_name` |
| 13 | `include` | `layout` | `@layout/toolbar` |
| 14 | `fragment` | `android:name` | `com.getmimo.ui.developermenu.DeveloperMenuFragment` |
| 15 | `fragment` | `android:id` | `@id/fragment_developermenu` |
| 16 | `fragment` | `android:layout_width` | `match_parent` |
| 17 | `fragment` | `android:layout_height` | `match_parent` |
| 18 | `fragment` | `app:layout_behavior` | `@string/appbar_scrolling_view_behavior` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@string/app_name` | `Mimo` / `Mimo` (de) / `Mimo` (es) / `Mimo` (fr) / `Mimo` (in) / `Mimo` (it) / `Mimo` (pl) / `Mimo` (pt-rBR) / `Mimo` (ru) / `Mimo` (tr) |
| `@string/appbar_scrolling_view_behavior` | `com.google.android.material.appbar.AppBarLayout$ScrollingViewBehavior` |

## ۴. شناسه‌های `@id`

```text
@id/appbar_developermenu
@id/developer_menu_root
@id/fragment_developermenu
@id/layout_toolbar
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/toolbar
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.developermenu.DeveloperMenuActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/developer_menu_root" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_developermenu" android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="wrap_content">
    <include android:id="@id/layout_toolbar" android:layout_width="match_parent" android:layout_height="wrap_content" android:title="@string/app_name" layout="@layout/toolbar"/>
  </com.google.android.material.appbar.AppBarLayout>
  <fragment android:name="com.getmimo.ui.developermenu.DeveloperMenuFragment" android:id="@id/fragment_developermenu" android:layout_width="match_parent" android:layout_height="match_parent" app:layout_behavior="@string/appbar_scrolling_view_behavior"/>
</androidx.coordinatorlayout.widget.CoordinatorLayout>
```
