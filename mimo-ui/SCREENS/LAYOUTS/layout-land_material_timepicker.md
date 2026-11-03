# پروندهٔ لایه — `res/layout-land/material_timepicker.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-land/material_timepicker.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-land/material_timepicker.xml`](../../SOURCE/res/layout-land/material_timepicker.xml) |
| SHA-256 دیکد | `0567fabd1eea496753d85e64576708275dc91da2e56a05a6ad4f507e5e61f5c0` |
| ریشه | `merge` |
| تعداد گره | 5 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge  #@id/material_timepicker_container
   ├─ androidx.constraintlayout.helper.widget.Flow  #@id/material_clock_display_and_toggle
   ├─ include  #@id/material_clock_display
   ├─ include  #@id/material_clock_period_toggle
   └─ com.google.android.material.timepicker.ClockFaceView  #@id/material_clock_face
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `merge` | `android:id` | `@id/material_timepicker_container` |
| 2 | `merge` | `android:layout_width` | `wrap_content` |
| 3 | `merge` | `android:layout_height` | `wrap_content` |
| 4 | `androidx.constraintlayout.helper.widget.Flow` | `android:orientation` | `vertical` |
| 5 | `androidx.constraintlayout.helper.widget.Flow` | `android:id` | `@id/material_clock_display_and_toggle` |
| 6 | `androidx.constraintlayout.helper.widget.Flow` | `android:layout_width` | `0.000000dip` |
| 7 | `androidx.constraintlayout.helper.widget.Flow` | `android:layout_height` | `wrap_content` |
| 8 | `androidx.constraintlayout.helper.widget.Flow` | `android:layout_marginTop` | `20.000000dip` |
| 9 | `androidx.constraintlayout.helper.widget.Flow` | `app:constraint_referenced_ids` | `material_clock_display,material_clock_period_toggle` |
| 10 | `androidx.constraintlayout.helper.widget.Flow` | `app:flow_verticalGap` | `@dimen/material_clock_period_toggle_vertical_gap` |
| 11 | `androidx.constraintlayout.helper.widget.Flow` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 12 | `androidx.constraintlayout.helper.widget.Flow` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `androidx.constraintlayout.helper.widget.Flow` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `include` | `android:id` | `@id/material_clock_display` |
| 15 | `include` | `android:layout_width` | `wrap_content` |
| 16 | `include` | `android:layout_height` | `wrap_content` |
| 17 | `include` | `layout` | `@layout/material_clock_display` |
| 18 | `include` | `android:id` | `@id/material_clock_period_toggle` |
| 19 | `include` | `android:layout_width` | `0.000000dip` |
| 20 | `include` | `android:layout_height` | `wrap_content` |
| 21 | `include` | `layout` | `@layout/material_clock_period_toggle_land` |
| 22 | `com.google.android.material.timepicker.ClockFaceView` | `android:theme` | `@style/ThemeOverlay.ClockFaceView` |
| 23 | `com.google.android.material.timepicker.ClockFaceView` | `android:id` | `@id/material_clock_face` |
| 24 | `com.google.android.material.timepicker.ClockFaceView` | `android:layout_width` | `wrap_content` |
| 25 | `com.google.android.material.timepicker.ClockFaceView` | `android:layout_height` | `wrap_content` |
| 26 | `com.google.android.material.timepicker.ClockFaceView` | `android:layout_marginStart` | `@dimen/clock_face_margin_start` |
| 27 | `com.google.android.material.timepicker.ClockFaceView` | `app:layout_constrainedWidth` | `true` |
| 28 | `com.google.android.material.timepicker.ClockFaceView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 29 | `com.google.android.material.timepicker.ClockFaceView` | `app:layout_constraintStart_toEndOf` | `@id/material_clock_display_and_toggle` |
| 30 | `com.google.android.material.timepicker.ClockFaceView` | `app:layout_constraintTop_toTopOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/clock_face_margin_start` | `64.000000dip` / `24.000000dip` (w320dp-land) / `64.000000dip` (w600dp-land) |
| `@dimen/material_clock_period_toggle_vertical_gap` | `12.000000dip` |
| `@style/ThemeOverlay.ClockFaceView` | `[{'attr': 'attr.focusRingsInset', 'attr_id': '0x7F0402B1', 'value': '2.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.focusRingsShapeAppearance', 'attr_id': '0x7F0402B5', 'value': '@style/ShapeAppearance.Material3.Corner.Full', 'value_type': 'reference'}, {'attr': 'attr.shapeCornerFamily', 'attr_id': '0x7F04052E', 'value': '0', 'value_type': 'int_dec'}]` |

## ۴. شناسه‌های `@id`

```text
@id/material_clock_display
@id/material_clock_display_and_toggle
@id/material_clock_face
@id/material_clock_period_toggle
@id/material_timepicker_container
```

## ۵. ارجاع به لایه‌های دیگر

```text
0.000000dip
@layout/material_clock_display
@layout/material_clock_period_toggle_land
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/material_timepicker_container" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <androidx.constraintlayout.helper.widget.Flow android:orientation="vertical" android:id="@id/material_clock_display_and_toggle" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="20.000000dip" app:constraint_referenced_ids="material_clock_display,material_clock_period_toggle" app:flow_verticalGap="@dimen/material_clock_period_toggle_vertical_gap" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <include android:id="@id/material_clock_display" android:layout_width="wrap_content" android:layout_height="wrap_content" layout="@layout/material_clock_display"/>
  <include android:id="@id/material_clock_period_toggle" android:layout_width="0.000000dip" android:layout_height="wrap_content" layout="@layout/material_clock_period_toggle_land"/>
  <com.google.android.material.timepicker.ClockFaceView android:theme="@style/ThemeOverlay.ClockFaceView" android:id="@id/material_clock_face" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginStart="@dimen/clock_face_margin_start" app:layout_constrainedWidth="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/material_clock_display_and_toggle" app:layout_constraintTop_toTopOf="0"/>
</merge>
```
