# پروندهٔ لایه — `res/layout-land/mdtp_time_picker_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-land/mdtp_time_picker_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-land/mdtp_time_picker_dialog.xml`](../../SOURCE/res/layout-land/mdtp_time_picker_dialog.xml) |
| SHA-256 دیکد | `bd2304ac058d6c2330c0e3977ae86a19333c94155dfbe4d9694557fd5996de6b` |
| ریشه | `LinearLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 5 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/mdtp_time_picker_dialog
   ├─ com.wdullaer.materialdatetimepicker.time.RadialPickerLayout  #@id/mdtp_time_picker
   └─ LinearLayout
      ├─ include
      ├─ FrameLayout  #@id/mdtp_time_display_background
      │  └─ include
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
| 7 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:layout_gravity` | `0x00000011` |
| 8 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:id` | `@id/mdtp_time_picker` |
| 9 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:background` | `@color/mdtp_circle_background` |
| 10 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:focusable` | `true` |
| 11 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:focusableInTouchMode` | `true` |
| 12 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:layout_width` | `@dimen/mdtp_picker_dimen` |
| 13 | `com.wdullaer.materialdatetimepicker.time.RadialPickerLayout` | `android:layout_height` | `@dimen/mdtp_time_picker_height` |
| 14 | `LinearLayout` | `android:orientation` | `vertical` |
| 15 | `LinearLayout` | `android:background` | `@0x0106000D` |
| 16 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 17 | `LinearLayout` | `android:layout_height` | `@dimen/mdtp_time_picker_height` |
| 18 | `include` | `layout` | `@layout/mdtp_time_title_view` |
| 19 | `FrameLayout` | `android:id` | `@id/mdtp_time_display_background` |
| 20 | `FrameLayout` | `android:background` | `@color/mdtp_accent_color` |
| 21 | `FrameLayout` | `android:layout_width` | `@dimen/mdtp_left_side_width` |
| 22 | `FrameLayout` | `android:layout_height` | `0.000000dip` |
| 23 | `FrameLayout` | `android:layout_weight` | `1.000000` |
| 24 | `include` | `android:layout_gravity` | `0x00000011` |
| 25 | `include` | `android:layout_width` | `match_parent` |
| 26 | `include` | `android:layout_height` | `match_parent` |
| 27 | `include` | `layout` | `@layout/mdtp_time_header_label` |
| 28 | `include` | `layout` | `@layout/mdtp_done_button` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/mdtp_accent_color` | `#FF009688` |
| `@color/mdtp_background_color` | `@color/mdtp_white` |
| `@color/mdtp_circle_background` | `@color/mdtp_background_color` |
| `@dimen/mdtp_left_side_width` | `240.000000dip` (land) / `400.000000dip` (sw600dp-land) / `270.000000dip` (w560dp-land) |
| `@dimen/mdtp_picker_dimen` | `270.000000dip` / `220.000000dip` (land) / `400.000000dip` (sw600dp) / `270.000000dip` (w560dp-land) |
| `@dimen/mdtp_time_picker_height` | `300.000000dip` / `450.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/mdtp_time_display_background
@id/mdtp_time_picker
@id/mdtp_time_picker_dialog
```

## ۵. ارجاع به لایه‌های دیگر

```text
0x00000011
@layout/mdtp_done_button
@layout/mdtp_time_header_label
@layout/mdtp_time_title_view
match_parent
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:id="@id/mdtp_time_picker_dialog" android:background="@color/mdtp_background_color" android:focusable="true" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <com.wdullaer.materialdatetimepicker.time.RadialPickerLayout android:layout_gravity="0x00000011" android:id="@id/mdtp_time_picker" android:background="@color/mdtp_circle_background" android:focusable="true" android:focusableInTouchMode="true" android:layout_width="@dimen/mdtp_picker_dimen" android:layout_height="@dimen/mdtp_time_picker_height"/>
  <LinearLayout android:orientation="vertical" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="@dimen/mdtp_time_picker_height">
    <include layout="@layout/mdtp_time_title_view"/>
    <FrameLayout android:id="@id/mdtp_time_display_background" android:background="@color/mdtp_accent_color" android:layout_width="@dimen/mdtp_left_side_width" android:layout_height="0.000000dip" android:layout_weight="1.000000">
      <include android:layout_gravity="0x00000011" android:layout_width="match_parent" android:layout_height="match_parent" layout="@layout/mdtp_time_header_label"/>
    </FrameLayout>
    <include layout="@layout/mdtp_done_button"/>
  </LinearLayout>
</LinearLayout>
```
