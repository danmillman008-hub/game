# پروندهٔ لایه — `res/layout/m3_side_sheet_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/m3_side_sheet_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/m3_side_sheet_dialog.xml`](../../SOURCE/res/layout/m3_side_sheet_dialog.xml) |
| SHA-256 دیکد | `f0e71bd4217e9137c4a0ff1739b1cf5e1cddb9f70b3efb11146d53df1cc9653b` |
| ریشه | `FrameLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/container
   └─ androidx.coordinatorlayout.widget.CoordinatorLayout  #@id/coordinator
      ├─ View  #@id/touch_outside
      └─ FrameLayout  #@id/m3_side_sheet
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:id` | `@id/container` |
| 2 | `FrameLayout` | `android:fitsSystemWindows` | `true` |
| 3 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 4 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 5 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:id` | `@id/coordinator` |
| 6 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:fitsSystemWindows` | `true` |
| 7 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_width` | `match_parent` |
| 8 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_height` | `match_parent` |
| 9 | `View` | `android:id` | `@id/touch_outside` |
| 10 | `View` | `android:focusable` | `false` |
| 11 | `View` | `android:layout_width` | `match_parent` |
| 12 | `View` | `android:layout_height` | `match_parent` |
| 13 | `View` | `android:soundEffectsEnabled` | `false` |
| 14 | `View` | `android:importantForAccessibility` | `no` |
| 15 | `FrameLayout` | `android:id` | `@id/m3_side_sheet` |
| 16 | `FrameLayout` | `app:layout_behavior` | `@string/side_sheet_behavior` |
| 17 | `FrameLayout` | `style` | `?attr/sideSheetModalStyle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@string/side_sheet_behavior` | `com.google.android.material.sidesheet.SideSheetBehavior` |

## ۴. شناسه‌های `@id`

```text
@id/container
@id/coordinator
@id/m3_side_sheet
@id/touch_outside
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/container" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.coordinatorlayout.widget.CoordinatorLayout android:id="@id/coordinator" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
    <View android:id="@id/touch_outside" android:focusable="false" android:layout_width="match_parent" android:layout_height="match_parent" android:soundEffectsEnabled="false" android:importantForAccessibility="no"/>
    <FrameLayout android:id="@id/m3_side_sheet" app:layout_behavior="@string/side_sheet_behavior" style="?attr/sideSheetModalStyle"/>
  </androidx.coordinatorlayout.widget.CoordinatorLayout>
</FrameLayout>
```
