# پروندهٔ لایه — `res/layout/design_bottom_sheet_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/design_bottom_sheet_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/design_bottom_sheet_dialog.xml`](../../SOURCE/res/layout/design_bottom_sheet_dialog.xml) |
| SHA-256 دیکد | `2f8489f2597173d8f03245c9fae29def1430105b967caf3801636d3a12bc22d9` |
| ریشه | `FrameLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/container
   ├─ androidx.coordinatorlayout.widget.CoordinatorLayout  #@id/coordinator
   │  ├─ View  #@id/touch_outside
   │  └─ FrameLayout  #@id/design_bottom_sheet
   └─ androidx.core.view.insets.ProtectionLayout  #@id/protection_layout
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
| 15 | `FrameLayout` | `android:layout_gravity` | `0x00000031` |
| 16 | `FrameLayout` | `android:id` | `@id/design_bottom_sheet` |
| 17 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 18 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 19 | `FrameLayout` | `app:layout_behavior` | `@string/bottom_sheet_behavior` |
| 20 | `FrameLayout` | `style` | `?attr/bottomSheetStyle` |
| 21 | `androidx.core.view.insets.ProtectionLayout` | `android:id` | `@id/protection_layout` |
| 22 | `androidx.core.view.insets.ProtectionLayout` | `android:visibility` | `gone` |
| 23 | `androidx.core.view.insets.ProtectionLayout` | `android:layout_width` | `match_parent` |
| 24 | `androidx.core.view.insets.ProtectionLayout` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@string/bottom_sheet_behavior` | `com.google.android.material.bottomsheet.BottomSheetBehavior` |

## ۴. شناسه‌های `@id`

```text
@id/container
@id/coordinator
@id/design_bottom_sheet
@id/protection_layout
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
    <FrameLayout android:layout_gravity="0x00000031" android:id="@id/design_bottom_sheet" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_behavior="@string/bottom_sheet_behavior" style="?attr/bottomSheetStyle"/>
  </androidx.coordinatorlayout.widget.CoordinatorLayout>
  <androidx.core.view.insets.ProtectionLayout android:id="@id/protection_layout" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent"/>
</FrameLayout>
```
