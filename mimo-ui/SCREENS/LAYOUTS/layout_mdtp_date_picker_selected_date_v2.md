# پروندهٔ لایه — `res/layout/mdtp_date_picker_selected_date_v2.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mdtp_date_picker_selected_date_v2.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mdtp_date_picker_selected_date_v2.xml`](../../SOURCE/res/layout/mdtp_date_picker_selected_date_v2.xml) |
| SHA-256 دیکد | `82b61bd09f3b421547996db6edd9ab8a0e42e8ba9c93b985445a54950d942559` |
| ریشه | `LinearLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/mdtp_day_picker_selected_date_layout
   ├─ com.wdullaer.materialdatetimepicker.AccessibleTextView  #@id/mdtp_date_picker_year
   └─ com.wdullaer.materialdatetimepicker.AccessibleLinearLayout  #@id/mdtp_date_picker_month_and_day
      └─ TextView  #@id/mdtp_date_picker_day
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000030` |
| 2 | `LinearLayout` | `android:orientation` | `vertical` |
| 3 | `LinearLayout` | `android:id` | `@id/mdtp_day_picker_selected_date_layout` |
| 4 | `LinearLayout` | `android:background` | `@color/mdtp_accent_color` |
| 5 | `LinearLayout` | `android:padding` | `16.000000dip` |
| 6 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 7 | `LinearLayout` | `android:layout_height` | `@dimen/mdtp_date_picker_header_height` |
| 8 | `LinearLayout` | `android:layout_weight` | `1.000000` |
| 9 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:textSize` | `@dimen/mdtp_datepicker_year_selection_text_size` |
| 10 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:textColor` | `@color/mdtp_date_picker_selector` |
| 11 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:gravity` | `0x00000010` |
| 12 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_gravity` | `0x00000011` |
| 13 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:id` | `@id/mdtp_date_picker_year` |
| 14 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:background` | `@0x0106000D` |
| 15 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_width` | `match_parent` |
| 16 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_height` | `wrap_content` |
| 17 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_marginBottom` | `4.000000dip` |
| 18 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:includeFontPadding` | `false` |
| 19 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:textColor` | `@color/mdtp_date_picker_selector` |
| 20 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:layout_gravity` | `0x00000011` |
| 21 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:orientation` | `horizontal` |
| 22 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:id` | `@id/mdtp_date_picker_month_and_day` |
| 23 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:background` | `@0x0106000D` |
| 24 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:clickable` | `true` |
| 25 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:layout_width` | `match_parent` |
| 26 | `com.wdullaer.materialdatetimepicker.AccessibleLinearLayout` | `android:layout_height` | `wrap_content` |
| 27 | `TextView` | `android:textSize` | `@dimen/mdtp_datepicker_selection_text_size` |
| 28 | `TextView` | `android:textColor` | `@color/mdtp_date_picker_selector` |
| 29 | `TextView` | `android:gravity` | `0x00000003` |
| 30 | `TextView` | `android:layout_gravity` | `0x00000010` |
| 31 | `TextView` | `android:id` | `@id/mdtp_date_picker_day` |
| 32 | `TextView` | `android:background` | `@0x0106000D` |
| 33 | `TextView` | `android:duplicateParentState` | `true` |
| 34 | `TextView` | `android:layout_width` | `wrap_content` |
| 35 | `TextView` | `android:layout_height` | `wrap_content` |
| 36 | `TextView` | `android:includeFontPadding` | `false` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/mdtp_accent_color` | `#FF009688` |
| `@color/mdtp_date_picker_selector` | `res/color/mdtp_date_picker_selector.xml` |
| `@dimen/mdtp_date_picker_header_height` | `16777214.000000dip` / `308.000000dip` (land) / `456.000000dip` (sw600dp-land) |
| `@dimen/mdtp_datepicker_selection_text_size` | `30.000000sp` |
| `@dimen/mdtp_datepicker_year_selection_text_size` | `16.000000sp` |

## ۴. شناسه‌های `@id`

```text
@id/mdtp_date_picker_day
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
res/layout-land/mdtp_date_picker_dialog_v2.xml
res/layout/mdtp_date_picker_dialog_v2.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000030" android:orientation="vertical" android:id="@id/mdtp_day_picker_selected_date_layout" android:background="@color/mdtp_accent_color" android:padding="16.000000dip" android:layout_width="match_parent" android:layout_height="@dimen/mdtp_date_picker_header_height" android:layout_weight="1.000000">
  <com.wdullaer.materialdatetimepicker.AccessibleTextView android:textSize="@dimen/mdtp_datepicker_year_selection_text_size" android:textColor="@color/mdtp_date_picker_selector" android:gravity="0x00000010" android:layout_gravity="0x00000011" android:id="@id/mdtp_date_picker_year" android:background="@0x0106000D" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="4.000000dip" android:includeFontPadding="false"/>
  <com.wdullaer.materialdatetimepicker.AccessibleLinearLayout android:textColor="@color/mdtp_date_picker_selector" android:layout_gravity="0x00000011" android:orientation="horizontal" android:id="@id/mdtp_date_picker_month_and_day" android:background="@0x0106000D" android:clickable="true" android:layout_width="match_parent" android:layout_height="wrap_content">
    <TextView android:textSize="@dimen/mdtp_datepicker_selection_text_size" android:textColor="@color/mdtp_date_picker_selector" android:gravity="0x00000003" android:layout_gravity="0x00000010" android:id="@id/mdtp_date_picker_day" android:background="@0x0106000D" android:duplicateParentState="true" android:layout_width="wrap_content" android:layout_height="wrap_content" android:includeFontPadding="false"/>
  </com.wdullaer.materialdatetimepicker.AccessibleLinearLayout>
</LinearLayout>
```
