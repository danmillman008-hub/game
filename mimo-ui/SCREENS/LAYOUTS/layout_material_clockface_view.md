# پروندهٔ لایه — `res/layout/material_clockface_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/material_clockface_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/material_clockface_view.xml`](../../SOURCE/res/layout/material_clockface_view.xml) |
| SHA-256 دیکد | `31088733d81783956b2071a2fccbca49b403535c6ac8f52de0235c79b7fed9c9` |
| ریشه | `merge` |
| تعداد گره | 2 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 2 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge  #@id/material_clock_face
   └─ com.google.android.material.timepicker.ClockHandView  #@id/material_clock_hand
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `merge` | `android:layout_gravity` | `0x00000011` |
| 2 | `merge` | `android:id` | `@id/material_clock_face` |
| 3 | `merge` | `android:layout_width` | `256.000000dip` |
| 4 | `merge` | `android:layout_height` | `256.000000dip` |
| 5 | `com.google.android.material.timepicker.ClockHandView` | `android:id` | `@id/material_clock_hand` |
| 6 | `com.google.android.material.timepicker.ClockHandView` | `android:tag` | `skip` |
| 7 | `com.google.android.material.timepicker.ClockHandView` | `android:layout_width` | `match_parent` |
| 8 | `com.google.android.material.timepicker.ClockHandView` | `android:layout_height` | `match_parent` |
| 9 | `com.google.android.material.timepicker.ClockHandView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 10 | `com.google.android.material.timepicker.ClockHandView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 11 | `com.google.android.material.timepicker.ClockHandView` | `app:layout_constraintStart_toStartOf` | `0` |
| 12 | `com.google.android.material.timepicker.ClockHandView` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `com.google.android.material.timepicker.ClockHandView` | `app:selectorSize` | `24.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/material_clock_face
@id/material_clock_hand
```

## ۵. ارجاع به لایه‌های دیگر

```text
0x00000011
256.000000dip
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000011" android:id="@id/material_clock_face" android:layout_width="256.000000dip" android:layout_height="256.000000dip">
  <com.google.android.material.timepicker.ClockHandView android:id="@id/material_clock_hand" android:tag="skip" android:layout_width="match_parent" android:layout_height="match_parent" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:selectorSize="24.000000dip"/>
</merge>
```
