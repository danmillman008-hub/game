# پروندهٔ لایه — `res/layout-land/mdtp_time_picker_dialog_v2.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-land/mdtp_time_picker_dialog_v2.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-land/mdtp_time_picker_dialog_v2.xml`](../../SOURCE/res/layout-land/mdtp_time_picker_dialog_v2.xml) |
| SHA-256 دیکد | `62fc5ea2a004569015e29ca106863b7dd42d3249f7e313a1247a06642b86b2db` |
| ریشه | `LinearLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 7 |
| ارجاع به منابع | 12 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/mdtp_time_picker_dialog
   ├─ include
   ├─ FrameLayout  #@id/mdtp_time_display_background
   │  └─ include
   └─ LinearLayout
      ├─ com.wdullaer.materialdatetimepicker.time.RadialPickerLayout  #@id/mdtp_time_picker
      └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:id` | `@id/mdtp_time_picker_dialog` |
| 3 | `LinearLayout` | `android:background` | `@color/mdtp_background_color` |
| 4 | `LinearLayout` | `android:focusable` | `true` |
| 5 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 6 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 7 | `include` | `layout` | `@layout/mdtp_time_title_view_v2` |
| 8 | `FrameLayout` | `android:id` | `@id/mdtp_time_display_background` |
| 9 | `FrameLayout` | `android:background` | `@color/mdtp_accent_color` |
| 10 | `FrameLayout` | `android:layout_width` | `@dimen/mdtp_date_picker_header_width` |
| 11 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 12 | `include` | `android:layout_gravity` | `0x00000011` |
| 13 | `include` | `android:layout_width` | `match_parent` |
| 14 | `include` | `android:layout_height` | `match_parent` |
| 15 | `include` | `layout` | `@layout/mdtp_time_header_label` |
| 16 | `LinearLayout` | `android:orientation` | `vertical` |
| 17 | `LinearLayout` | `android:background` | `@0x0106000D` |
| 18 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 19 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 20 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:layout_gravity` | `0x00000011` |
| 21 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:id` | `@id/mdtp_time_picker` |
| 22 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:background` | `@color/mdtp_circle_background` |
| 23 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:focusable` | `true` |
| 24 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:focusableInTouchMode` | `true` |
| 25 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:layout_width` | `@dimen/mdtp_picker_dimen` |
| 26 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:layout_height` | `@dimen/mdtp_picker_dimen` |
| 27 | `include` | `android:layout_width` | `match_parent` |
| 28 | `include` | `android:layout_height` | `wrap_content` |
| 29 | `include` | `android:layout_marginTop` | `16777200.000000dip` |
| 30 | `include` | `layout` | `@layout/mdtp_done_button` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/mdtp_accent_color` | `#FF009688` |
| `@color/mdtp_background_color` | `@color/mdtp_white` |
| `@color/mdtp_circle_background` | `@color/mdtp_background_color` |
| `@dimen/mdtp_date_picker_header_width` | `@dimen/mdtp_date_picker_component_width` / `170.000000dip` (land) / `220.000000dip` (sw600dp-land) |
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
16777200.000000dip
@layout/mdtp_done_button
@layout/mdtp_time_header_label
@layout/mdtp_time_title_view_v2
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:id="@id/mdtp_time_picker_dialog" android:background="@color/mdtp_background_color" android:focusable="true" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <include layout="@layout/mdtp_time_title_view_v2"/>
  <FrameLayout android:id="@id/mdtp_time_display_background" android:background="@color/mdtp_accent_color" android:layout_width="@dimen/mdtp_date_picker_header_width" android:layout_height="match_parent">
    <include android:layout_gravity="0x00000011" android:layout_width="match_parent" android:layout_height="match_parent" layout="@layout/mdtp_time_header_label"/>
  </FrameLayout>
  <LinearLayout android:orientation="vertical" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="wrap_content">
    <com.wdullaer.materialdatetimepicker.time.RadialPickerLayout android:layout_gravity="0x00000011" android:id="@id/mdtp_time_picker" android:background="@color/mdtp_circle_background" android:focusable="true" android:focusableInTouchMode="true" android:layout_width="@dimen/mdtp_picker_dimen" android:layout_height="@dimen/mdtp_picker_dimen"/>
    <include android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="16777200.000000dip" layout="@layout/mdtp_done_button"/>
  </LinearLayout>
</LinearLayout>
```
