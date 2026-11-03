# پروندهٔ لایه — `res/layout/material_timepicker.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/material_timepicker.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/material_timepicker.xml`](../../SOURCE/res/layout/material_timepicker.xml) |
| SHA-256 دیکد | `5db76a228125ed2905c9a853df29df5199e482b6cfd7747d41f5bec89c6655ba` |
| ریشه | `merge` |
| تعداد گره | 5 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
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
| 4 | `androidx.constraintlayout.helper.widget.Flow` | `android:orientation` | `horizontal` |
| 5 | `androidx.constraintlayout.helper.widget.Flow` | `android:id` | `@id/material_clock_display_and_toggle` |
| 6 | `androidx.constraintlayout.helper.widget.Flow` | `android:layout_width` | `0.000000dip` |
| 7 | `androidx.constraintlayout.helper.widget.Flow` | `android:layout_height` | `@dimen/material_clock_period_toggle_height` |
| 8 | `androidx.constraintlayout.helper.widget.Flow` | `app:constraint_referenced_ids` | `material_clock_display,material_clock_period_toggle` |
| 9 | `androidx.constraintlayout.helper.widget.Flow` | `app:flow_horizontalGap` | `@dimen/material_clock_period_toggle_horizontal_gap` |
| 10 | `androidx.constraintlayout.helper.widget.Flow` | `app:layout_constraintEnd_toEndOf` | `0` |
| 11 | `androidx.constraintlayout.helper.widget.Flow` | `app:layout_constraintStart_toStartOf` | `0` |
| 12 | `androidx.constraintlayout.helper.widget.Flow` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `include` | `android:id` | `@id/material_clock_display` |
| 14 | `include` | `layout` | `@layout/material_clock_display` |
| 15 | `include` | `android:id` | `@id/material_clock_period_toggle` |
| 16 | `include` | `layout` | `@layout/material_clock_period_toggle` |
| 17 | `com.google.android.material.timepicker.ClockFaceView` | `android:theme` | `@style/ThemeOverlay.ClockFaceView` |
| 18 | `com.google.android.material.timepicker.ClockFaceView` | `android:layout_gravity` | `0x00000011` |
| 19 | `com.google.android.material.timepicker.ClockFaceView` | `android:id` | `@id/material_clock_face` |
| 20 | `com.google.android.material.timepicker.ClockFaceView` | `android:layout_width` | `wrap_content` |
| 21 | `com.google.android.material.timepicker.ClockFaceView` | `android:layout_height` | `wrap_content` |
| 22 | `com.google.android.material.timepicker.ClockFaceView` | `android:layout_marginTop` | `28.000000dip` |
| 23 | `com.google.android.material.timepicker.ClockFaceView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 24 | `com.google.android.material.timepicker.ClockFaceView` | `app:layout_constraintStart_toStartOf` | `0` |
| 25 | `com.google.android.material.timepicker.ClockFaceView` | `app:layout_constraintTop_toBottomOf` | `@id/material_clock_display_and_toggle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/material_clock_period_toggle_height` | `98.000000dip` |
| `@dimen/material_clock_period_toggle_horizontal_gap` | `12.000000dip` |
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
@layout/material_clock_display
@layout/material_clock_period_toggle
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
  <androidx.constraintlayout.helper.widget.Flow android:orientation="horizontal" android:id="@id/material_clock_display_and_toggle" android:layout_width="0.000000dip" android:layout_height="@dimen/material_clock_period_toggle_height" app:constraint_referenced_ids="material_clock_display,material_clock_period_toggle" app:flow_horizontalGap="@dimen/material_clock_period_toggle_horizontal_gap" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <include android:id="@id/material_clock_display" layout="@layout/material_clock_display"/>
  <include android:id="@id/material_clock_period_toggle" layout="@layout/material_clock_period_toggle"/>
  <com.google.android.material.timepicker.ClockFaceView android:theme="@style/ThemeOverlay.ClockFaceView" android:layout_gravity="0x00000011" android:id="@id/material_clock_face" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="28.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/material_clock_display_and_toggle"/>
</merge>
```
