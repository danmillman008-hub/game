# پروندهٔ لایه — `res/layout/mdtp_time_picker_dialog_v2.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mdtp_time_picker_dialog_v2.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mdtp_time_picker_dialog_v2.xml`](../../SOURCE/res/layout/mdtp_time_picker_dialog_v2.xml) |
| SHA-256 دیکد | `d05517161eac136567217b9ba911b65f4ad19f5dc22ed1d032af852af3edb62b` |
| ریشه | `LinearLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 6 |
| ارجاع به منابع | 11 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/mdtp_time_picker_dialog
   ├─ LinearLayout  #@id/mdtp_time_display_background
   │  ├─ include
   │  ├─ include
   │  └─ com.wdullaer.materialdatetimepicker.time.RadialPickerLayout  #@id/mdtp_time_picker
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 2 | `LinearLayout` | `android:orientation` | `vertical` |
| 3 | `LinearLayout` | `android:id` | `@id/mdtp_time_picker_dialog` |
| 4 | `LinearLayout` | `android:background` | `@color/mdtp_background_color` |
| 5 | `LinearLayout` | `android:focusable` | `true` |
| 6 | `LinearLayout` | `android:layout_width` | `@dimen/mdtp_picker_dimen` |
| 7 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 8 | `LinearLayout` | `android:orientation` | `vertical` |
| 9 | `LinearLayout` | `android:id` | `@id/mdtp_time_display_background` |
| 10 | `LinearLayout` | `android:background` | `@color/mdtp_accent_color` |
| 11 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 12 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 13 | `include` | `layout` | `@layout/mdtp_time_title_view_v2` |
| 14 | `include` | `android:layout_gravity` | `0x00000011` |
| 15 | `include` | `android:layout_width` | `match_parent` |
| 16 | `include` | `android:layout_height` | `@dimen/mdtp_header_height` |
| 17 | `include` | `layout` | `@layout/mdtp_time_header_label` |
| 18 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:layout_gravity` | `0x00000011` |
| 19 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:id` | `@id/mdtp_time_picker` |
| 20 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:background` | `@color/mdtp_circle_background` |
| 21 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:focusable` | `true` |
| 22 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:focusableInTouchMode` | `true` |
| 23 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:layout_width` | `@dimen/mdtp_picker_dimen` |
| 24 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:layout_height` | `@dimen/mdtp_picker_dimen` |
| 25 | `include` | `layout` | `@layout/mdtp_done_button` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/mdtp_accent_color` | `#FF009688` |
| `@color/mdtp_background_color` | `@color/mdtp_white` |
| `@color/mdtp_circle_background` | `@color/mdtp_background_color` |
| `@dimen/mdtp_header_height` | `96.000000dip` / `120.000000dip` (sw600dp) / `96.000000dip` (sw600dp-land) |
| `@dimen/mdtp_picker_dimen` | `270.000000dip` / `220.000000dip` (land) / `400.000000dip` (sw600dp) / `270.000000dip` (w560dp-land) |

## ۴. شناسه‌های `@id`

```text
@id/mdtp_time_display_background
@id/mdtp_time_picker
@id/mdtp_time_picker_dialog
```

## ۵. ارجاع به لایه‌های دیگر

```text
0x00000011
@dimen/mdtp_header_height
@layout/mdtp_done_button
@layout/mdtp_time_header_label
@layout/mdtp_time_title_view_v2
match_parent
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000011" android:orientation="vertical" android:id="@id/mdtp_time_picker_dialog" android:background="@color/mdtp_background_color" android:focusable="true" android:layout_width="@dimen/mdtp_picker_dimen" android:layout_height="wrap_content">
  <LinearLayout android:orientation="vertical" android:id="@id/mdtp_time_display_background" android:background="@color/mdtp_accent_color" android:layout_width="wrap_content" android:layout_height="wrap_content">
    <include layout="@layout/mdtp_time_title_view_v2"/>
    <include android:layout_gravity="0x00000011" android:layout_width="match_parent" android:layout_height="@dimen/mdtp_header_height" layout="@layout/mdtp_time_header_label"/>
    <com.wdullaer.materialdatetimepicker.time.RadialPickerLayout android:layout_gravity="0x00000011" android:id="@id/mdtp_time_picker" android:background="@color/mdtp_circle_background" android:focusable="true" android:focusableInTouchMode="true" android:layout_width="@dimen/mdtp_picker_dimen" android:layout_height="@dimen/mdtp_picker_dimen"/>
  </LinearLayout>
  <include layout="@layout/mdtp_done_button"/>
</LinearLayout>
```
