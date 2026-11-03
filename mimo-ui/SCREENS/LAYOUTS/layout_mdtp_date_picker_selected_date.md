# پروندهٔ لایه — `res/layout/mdtp_date_picker_selected_date.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mdtp_date_picker_selected_date.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mdtp_date_picker_selected_date.xml`](../../SOURCE/res/layout/mdtp_date_picker_selected_date.xml) |
| SHA-256 دیکد | `b8cc3d9e6bef616719121a9226f6be5b5536d9043207e97016bcaf86052e5f20` |
| ریشه | `LinearLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/mdtp_day_picker_selected_date_layout
   ├─ com.wdullaer.materialdatetimepicker.AccessibleLinearLayout  #@id/mdtp_date_picker_month_and_day
   │  ├─ TextView  #@id/mdtp_date_picker_month
   │  └─ TextView  #@id/mdtp_date_picker_day
   └─ com.wdullaer.materialdatetimepicker.AccessibleTextView  #@id/mdtp_date_picker_year
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 2 | `LinearLayout` | `android:orientation` | `vertical` |
| 3 | `LinearLayout` | `android:id` | `@id/mdtp_day_picker_selected_date_layout` |
| 4 | `LinearLayout` | `android:background` | `@color/mdtp_accent_color` |
| 5 | `LinearLayout` | `android:layout_width` | `@dimen/mdtp_date_picker_component_width` |
| 6 | `LinearLayout` | `android:layout_height` | `@dimen/mdtp_selected_date_height` |
| 7 | `LinearLayout` | `android:layout_weight` | `1.000000` |
| 8 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:textColor` | `@color/mdtp_date_picker_selector` |
| 9 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:layout_gravity` | `0x00000011` |
| 10 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:orientation` | `vertical` |
| 11 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:id` | `@id/mdtp_date_picker_month_and_day` |
| 12 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:background` | `@0x0106000D` |
| 13 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:clickable` | `true` |
| 14 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:layout_width` | `match_parent` |
| 15 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:layout_height` | `wrap_content` |
| 16 | `TextView` | `android:textSize` | `@dimen/mdtp_selected_date_month_size` |
| 17 | `TextView` | `android:textColor` | `@color/mdtp_date_picker_selector` |
| 18 | `TextView` | `android:gravity` | `0x00000051` |
| 19 | `TextView` | `android:id` | `@id/mdtp_date_picker_month` |
| 20 | `TextView` | `android:background` | `@0x0106000D` |
| 21 | `TextView` | `android:duplicateParentState` | `true` |
| 22 | `TextView` | `android:layout_width` | `match_parent` |
| 23 | `TextView` | `android:layout_height` | `wrap_content` |
| 24 | `TextView` | `android:includeFontPadding` | `false` |
| 25 | `TextView` | `android:textAllCaps` | `true` |
| 26 | `TextView` | `android:textSize` | `@dimen/mdtp_selected_date_day_size` |
| 27 | `TextView` | `android:textColor` | `@color/mdtp_date_picker_selector` |
| 28 | `TextView` | `android:gravity` | `0x00000011` |
| 29 | `TextView` | `android:layout_gravity` | `0x00000011` |
| 30 | `TextView` | `android:id` | `@id/mdtp_date_picker_day` |
| 31 | `TextView` | `android:background` | `@0x0106000D` |
| 32 | `TextView` | `android:duplicateParentState` | `true` |
| 33 | `TextView` | `android:layout_width` | `match_parent` |
| 34 | `TextView` | `android:layout_height` | `wrap_content` |
| 35 | `TextView` | `android:layout_marginTop` | `16777206.000000dip` |
| 36 | `TextView` | `android:layout_marginBottom` | `16777206.000000dip` |
| 37 | `TextView` | `android:includeFontPadding` | `false` |
| 38 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:textSize` | `@dimen/mdtp_selected_date_year_size` |
| 39 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:textColor` | `@color/mdtp_date_picker_selector` |
| 40 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:gravity` | `0x00000031` |
| 41 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_gravity` | `0x00000011` |
| 42 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:id` | `@id/mdtp_date_picker_year` |
| 43 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:background` | `@0x0106000D` |
| 44 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_width` | `match_parent` |
| 45 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_height` | `wrap_content` |
| 46 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:includeFontPadding` | `false` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/mdtp_accent_color` | `#FF009688` |
| `@color/mdtp_date_picker_selector` | `res/color/mdtp_date_picker_selector.xml` |
| `@dimen/mdtp_date_picker_component_width` | `270.000000dip` / `220.000000dip` (land) / `400.000000dip` (sw600dp) / `270.000000dip` (w560dp-land) |
| `@dimen/mdtp_selected_date_day_size` | `70.000000dip` / `100.000000dip` (land) / `150.000000dip` (sw600dp) / `100.000000dip` (w270dp-h560dp) |
| `@dimen/mdtp_selected_date_height` | `140.000000dip` / `190.000000dip` (w270dp-h560dp) |
| `@dimen/mdtp_selected_date_month_size` | `25.000000dip` / `30.000000dip` (land) / `45.000000dip` (sw600dp) / `30.000000dip` (w270dp-h560dp) |
| `@dimen/mdtp_selected_date_year_size` | `25.000000dip` / `30.000000dip` (land) / `45.000000dip` (sw600dp) / `30.000000dip` (w270dp-h560dp) |

## ۴. شناسه‌های `@id`

```text
@id/mdtp_date_picker_day
@id/mdtp_date_picker_month
@id/mdtp_date_picker_month_and_day
@id/mdtp_date_picker_year
@id/mdtp_day_picker_selected_date_layout
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout-land/mdtp_date_picker_dialog.xml
res/layout-sw600dp-land-v13/mdtp_date_picker_dialog.xml
res/layout-sw600dp-v13/mdtp_date_picker_dialog.xml
res/layout-w270dp-h560dp-v13/mdtp_date_picker_dialog.xml
res/layout/mdtp_date_picker_dialog.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000011" android:orientation="vertical" android:id="@id/mdtp_day_picker_selected_date_layout" android:background="@color/mdtp_accent_color" android:layout_width="@dimen/mdtp_date_picker_component_width" android:layout_height="@dimen/mdtp_selected_date_height" android:layout_weight="1.000000">
  <com.wdullaer.materialdatetimepicker.AccessibleLinearLayout android:textColor="@color/mdtp_date_picker_selector" android:layout_gravity="0x00000011" android:orientation="vertical" android:id="@id/mdtp_date_picker_month_and_day" android:background="@0x0106000D" android:clickable="true" android:layout_width="match_parent" android:layout_height="wrap_content">
    <TextView android:textSize="@dimen/mdtp_selected_date_month_size" android:textColor="@color/mdtp_date_picker_selector" android:gravity="0x00000051" android:id="@id/mdtp_date_picker_month" android:background="@0x0106000D" android:duplicateParentState="true" android:layout_width="match_parent" android:layout_height="wrap_content" android:includeFontPadding="false" android:textAllCaps="true"/>
    <TextView android:textSize="@dimen/mdtp_selected_date_day_size" android:textColor="@color/mdtp_date_picker_selector" android:gravity="0x00000011" android:layout_gravity="0x00000011" android:id="@id/mdtp_date_picker_day" android:background="@0x0106000D" android:duplicateParentState="true" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="16777206.000000dip" android:layout_marginBottom="16777206.000000dip" android:includeFontPadding="false"/>
  </com.wdullaer.materialdatetimepicker.AccessibleLinearLayout>
  <com.wdullaer.materialdatetimepicker.AccessibleTextView android:textSize="@dimen/mdtp_selected_date_year_size" android:textColor="@color/mdtp_date_picker_selector" android:gravity="0x00000031" android:layout_gravity="0x00000011" android:id="@id/mdtp_date_picker_year" android:background="@0x0106000D" android:layout_width="match_parent" android:layout_height="wrap_content" android:includeFontPadding="false"/>
</LinearLayout>
```
