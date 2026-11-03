# پروندهٔ لایه — `res/layout-land/mdtp_time_header_label.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-land/mdtp_time_header_label.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-land/mdtp_time_header_label.xml`](../../SOURCE/res/layout-land/mdtp_time_header_label.xml) |
| SHA-256 دیکد | `04f26f5ace98c2ebc45fd0cd7c6a5e429ff85dfb98f6b0d55de18ee741c64de0` |
| ریشه | `RelativeLayout` |
| تعداد گره | 16 |
| تعداد شناسه | 13 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 27 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RelativeLayout  #@id/mdtp_time_display
   ├─ View  #@id/mdtp_center_view
   ├─ TextView  #@id/mdtp_hour_space
   ├─ FrameLayout
   │  └─ com.wdullaer.materialdatetimepicker.AccessibleTextView  #@id/mdtp_hours
   ├─ TextView  #@id/mdtp_separator
   ├─ TextView  #@id/mdtp_minutes_space
   ├─ FrameLayout
   │  └─ com.wdullaer.materialdatetimepicker.AccessibleTextView  #@id/mdtp_minutes
   ├─ TextView  #@id/mdtp_separator_seconds
   ├─ TextView  #@id/mdtp_seconds_space
   ├─ FrameLayout
   │  └─ com.wdullaer.materialdatetimepicker.AccessibleTextView  #@id/mdtp_seconds
   └─ LinearLayout  #@id/mdtp_ampm_layout
      ├─ TextView  #@id/mdtp_am_label
      └─ TextView  #@id/mdtp_pm_label
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `RelativeLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `RelativeLayout` | `android:id` | `@id/mdtp_time_display` |
| 3 | `RelativeLayout` | `android:background` | `@color/mdtp_accent_color` |
| 4 | `RelativeLayout` | `android:padding` | `16.000000dip` |
| 5 | `RelativeLayout` | `android:clipChildren` | `false` |
| 6 | `RelativeLayout` | `android:layout_width` | `match_parent` |
| 7 | `RelativeLayout` | `android:layout_height` | `match_parent` |
| 8 | `View` | `android:id` | `@id/mdtp_center_view` |
| 9 | `View` | `android:background` | `#00000000` |
| 10 | `View` | `android:visibility` | `invisible` |
| 11 | `View` | `android:layout_width` | `1.000000dip` |
| 12 | `View` | `android:layout_height` | `1.000000dip` |
| 13 | `View` | `android:layout_centerInParent` | `true` |
| 14 | `View` | `android:importantForAccessibility` | `no` |
| 15 | `TextView` | `android:id` | `@id/mdtp_hour_space` |
| 16 | `TextView` | `android:visibility` | `invisible` |
| 17 | `TextView` | `android:layout_width` | `wrap_content` |
| 18 | `TextView` | `android:layout_height` | `wrap_content` |
| 19 | `TextView` | `android:text` | `@string/mdtp_time_placeholder` |
| 20 | `TextView` | `android:layout_toLeftOf` | `@id/mdtp_separator` |
| 21 | `TextView` | `android:layout_alignBaseline` | `@id/mdtp_separator` |
| 22 | `TextView` | `android:importantForAccessibility` | `no` |
| 23 | `TextView` | `style` | `@style/mdtp_time_label` |
| 24 | `FrameLayout` | `android:background` | `@0x0106000D` |
| 25 | `FrameLayout` | `android:clipChildren` | `false` |
| 26 | `FrameLayout` | `android:layout_width` | `0.000000dip` |
| 27 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 28 | `FrameLayout` | `android:layout_marginLeft` | `@dimen/mdtp_extra_time_label_margin` |
| 29 | `FrameLayout` | `android:layout_marginRight` | `@dimen/mdtp_extra_time_label_margin` |
| 30 | `FrameLayout` | `android:layout_alignLeft` | `@id/mdtp_hour_space` |
| 31 | `FrameLayout` | `android:layout_alignRight` | `@id/mdtp_hour_space` |
| 32 | `FrameLayout` | `android:layout_alignBottom` | `@id/mdtp_separator` |
| 33 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:textColor` | `@color/mdtp_white` |
| 34 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:gravity` | `0x00000001` |
| 35 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_gravity` | `0x00000011` |
| 36 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:id` | `@id/mdtp_hours` |
| 37 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:background` | `@0x0106000D` |
| 38 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_width` | `wrap_content` |
| 39 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_height` | `wrap_content` |
| 40 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:text` | `@string/mdtp_time_placeholder` |
| 41 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `style` | `@style/mdtp_time_label` |
| 42 | `TextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 43 | `TextView` | `android:id` | `@id/mdtp_separator` |
| 44 | `TextView` | `android:background` | `@0x0106000D` |
| 45 | `TextView` | `android:paddingLeft` | `@dimen/mdtp_separator_padding` |
| 46 | `TextView` | `android:paddingRight` | `@dimen/mdtp_separator_padding` |
| 47 | `TextView` | `android:layout_width` | `wrap_content` |
| 48 | `TextView` | `android:layout_height` | `wrap_content` |
| 49 | `TextView` | `android:text` | `@string/mdtp_time_separator` |
| 50 | `TextView` | `android:layout_above` | `@id/mdtp_seconds_space` |
| 51 | `TextView` | `android:layout_centerHorizontal` | `true` |
| 52 | `TextView` | `android:importantForAccessibility` | `no` |
| 53 | `TextView` | `style` | `@style/mdtp_time_label` |
| 54 | `TextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 55 | `TextView` | `android:id` | `@id/mdtp_minutes_space` |
| 56 | `TextView` | `android:visibility` | `invisible` |
| 57 | `TextView` | `android:layout_width` | `wrap_content` |
| 58 | `TextView` | `android:layout_height` | `wrap_content` |
| 59 | `TextView` | `android:text` | `@string/mdtp_time_placeholder` |
| 60 | `TextView` | `android:layout_toRightOf` | `@id/mdtp_separator` |
| 61 | `TextView` | `android:layout_alignBaseline` | `@id/mdtp_separator` |
| 62 | `TextView` | `android:importantForAccessibility` | `no` |
| 63 | `TextView` | `style` | `@style/mdtp_time_label` |
| 64 | `FrameLayout` | `android:background` | `@0x0106000D` |
| 65 | `FrameLayout` | `android:layout_width` | `0.000000dip` |
| 66 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 67 | `FrameLayout` | `android:layout_marginLeft` | `@dimen/mdtp_extra_time_label_margin` |
| 68 | `FrameLayout` | `android:layout_marginRight` | `@dimen/mdtp_extra_time_label_margin` |
| 69 | `FrameLayout` | `android:layout_alignLeft` | `@id/mdtp_minutes_space` |
| 70 | `FrameLayout` | `android:layout_alignRight` | `@id/mdtp_minutes_space` |
| 71 | `FrameLayout` | `android:layout_alignBottom` | `@id/mdtp_separator` |
| 72 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 73 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:gravity` | `0x00000001` |
| 74 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_gravity` | `0x00000011` |
| 75 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:id` | `@id/mdtp_minutes` |
| 76 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:background` | `@0x0106000D` |
| 77 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_width` | `wrap_content` |
| 78 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_height` | `wrap_content` |
| 79 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:text` | `@string/mdtp_time_placeholder` |
| 80 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `style` | `@style/mdtp_time_label` |
| 81 | `TextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 82 | `TextView` | `android:id` | `@id/mdtp_separator_seconds` |
| 83 | `TextView` | `android:background` | `@0x0106000D` |
| 84 | `TextView` | `android:paddingLeft` | `@dimen/mdtp_separator_padding` |
| 85 | `TextView` | `android:paddingRight` | `@dimen/mdtp_separator_padding` |
| 86 | `TextView` | `android:visibility` | `gone` |
| 87 | `TextView` | `android:layout_width` | `wrap_content` |
| 88 | `TextView` | `android:layout_height` | `wrap_content` |
| 89 | `TextView` | `android:text` | `@string/mdtp_time_separator` |
| 90 | `TextView` | `android:layout_toRightOf` | `@id/mdtp_minutes_space` |
| 91 | `TextView` | `android:importantForAccessibility` | `no` |
| 92 | `TextView` | `style` | `@style/mdtp_time_label` |
| 93 | `TextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 94 | `TextView` | `android:id` | `@id/mdtp_seconds_space` |
| 95 | `TextView` | `android:background` | `@0x0106000D` |
| 96 | `TextView` | `android:visibility` | `invisible` |
| 97 | `TextView` | `android:layout_width` | `wrap_content` |
| 98 | `TextView` | `android:layout_height` | `wrap_content` |
| 99 | `TextView` | `android:text` | `@string/mdtp_time_placeholder` |
| 100 | `TextView` | `android:layout_alignBottom` | `@id/mdtp_center_view` |
| 101 | `TextView` | `android:layout_centerInParent` | `true` |
| 102 | `TextView` | `android:importantForAccessibility` | `no` |
| 103 | `TextView` | `style` | `@style/mdtp_time_label_small` |
| 104 | `FrameLayout` | `android:background` | `@0x0106000D` |
| 105 | `FrameLayout` | `android:layout_width` | `0.000000dip` |
| 106 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 107 | `FrameLayout` | `android:layout_marginLeft` | `@dimen/mdtp_extra_time_label_margin` |
| 108 | `FrameLayout` | `android:layout_marginRight` | `@dimen/mdtp_extra_time_label_margin` |
| 109 | `FrameLayout` | `android:layout_alignLeft` | `@id/mdtp_seconds_space` |
| 110 | `FrameLayout` | `android:layout_alignRight` | `@id/mdtp_seconds_space` |
| 111 | `FrameLayout` | `android:layout_alignBottom` | `@id/mdtp_center_view` |
| 112 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 113 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:gravity` | `0x00000001` |
| 114 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_gravity` | `0x00000011` |
| 115 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:id` | `@id/mdtp_seconds` |
| 116 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:background` | `@0x0106000D` |
| 117 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_width` | `wrap_content` |
| 118 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_height` | `wrap_content` |
| 119 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:text` | `@string/mdtp_time_placeholder` |
| 120 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `style` | `@style/mdtp_time_label_small` |
| 121 | `LinearLayout` | `android:orientation` | `vertical` |
| 122 | `LinearLayout` | `android:id` | `@id/mdtp_ampm_layout` |
| 123 | `LinearLayout` | `android:background` | `@0x0106000D` |
| 124 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 125 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 126 | `LinearLayout` | `android:layout_marginTop` | `20.000000dip` |
| 127 | `LinearLayout` | `android:layout_below` | `@id/mdtp_seconds_space` |
| 128 | `LinearLayout` | `android:layout_centerHorizontal` | `true` |
| 129 | `TextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 130 | `TextView` | `android:id` | `@id/mdtp_am_label` |
| 131 | `TextView` | `android:background` | `@0x0106000D` |
| 132 | `TextView` | `android:paddingLeft` | `@dimen/mdtp_ampm_left_padding` |
| 133 | `TextView` | `android:paddingRight` | `@dimen/mdtp_ampm_left_padding` |
| 134 | `TextView` | `android:layout_width` | `wrap_content` |
| 135 | `TextView` | `android:layout_height` | `wrap_content` |
| 136 | `TextView` | `android:text` | `@string/mdtp_am` |
| 137 | `TextView` | `android:importantForAccessibility` | `no` |
| 138 | `TextView` | `style` | `@style/mdtp_ampm_label` |
| 139 | `TextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 140 | `TextView` | `android:id` | `@id/mdtp_pm_label` |
| 141 | `TextView` | `android:background` | `@0x0106000D` |
| 142 | `TextView` | `android:paddingLeft` | `@dimen/mdtp_ampm_left_padding` |
| 143 | `TextView` | `android:paddingRight` | `@dimen/mdtp_ampm_left_padding` |
| 144 | `TextView` | `android:layout_width` | `wrap_content` |
| 145 | `TextView` | `android:layout_height` | `wrap_content` |
| 146 | `TextView` | `android:layout_marginTop` | `6.000000dip` |
| 147 | `TextView` | `android:text` | `@string/mdtp_pm` |
| 148 | `TextView` | `android:importantForAccessibility` | `no` |
| 149 | `TextView` | `style` | `@style/mdtp_ampm_label` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/mdtp_accent_color` | `#FF009688` |
| `@color/mdtp_accent_color_focused` | `#76FFFFFF` |
| `@color/mdtp_white` | `#FFFFFFFF` |
| `@dimen/mdtp_ampm_left_padding` | `6.000000dip` |
| `@dimen/mdtp_extra_time_label_margin` | `16777186.000000dip` / `16777166.000000dip` (sw600dp) |
| `@dimen/mdtp_separator_padding` | `4.000000dip` / `5.000000dip` (sw600dp) |
| `@string/mdtp_am` | `am` |
| `@string/mdtp_pm` | `pm` |
| `@string/mdtp_time_placeholder` | `00` |
| `@string/mdtp_time_separator` | `:` |
| `@style/mdtp_ampm_label` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/mdtp_ampm_label_size', 'value_type': 'reference'}, {'attr': 'android:textStyle', 'attr_id': '0x01010097', 'value': '0x00000001', 'value_type': 'int_hex'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/mdtp_ampm_text_color', 'value_type': 'reference'}, {'attr': 'android:textAllCaps', 'attr_id': '0x0101038C', 'value': 'true', 'value_type': 'int_boolean'}]` |
| `@style/mdtp_time_label` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/mdtp_time_label_size', 'value_type': 'reference'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/mdtp_numbers_text_color', 'value_type': 'reference'}]` |
| `@style/mdtp_time_label_small` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/mdtp_time_label_subscript_size', 'value_type': 'reference'}, {'attr': 'android:layout_marginBottom', 'attr_id': '0x010100FA', 'value': '@dimen/mdtp_time_label_shift', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/mdtp_am_label
@id/mdtp_ampm_layout
@id/mdtp_center_view
@id/mdtp_hour_space
@id/mdtp_hours
@id/mdtp_minutes
@id/mdtp_minutes_space
@id/mdtp_pm_label
@id/mdtp_seconds
@id/mdtp_seconds_space
@id/mdtp_separator
@id/mdtp_separator_seconds
@id/mdtp_time_display
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout-land/mdtp_time_picker_dialog.xml
res/layout-land/mdtp_time_picker_dialog_v2.xml
res/layout/mdtp_time_picker_dialog.xml
res/layout/mdtp_time_picker_dialog_v2.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000011" android:id="@id/mdtp_time_display" android:background="@color/mdtp_accent_color" android:padding="16.000000dip" android:clipChildren="false" android:layout_width="match_parent" android:layout_height="match_parent">
  <View android:id="@id/mdtp_center_view" android:background="#00000000" android:visibility="invisible" android:layout_width="1.000000dip" android:layout_height="1.000000dip" android:layout_centerInParent="true" android:importantForAccessibility="no"/>
  <TextView android:id="@id/mdtp_hour_space" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_placeholder" android:layout_toLeftOf="@id/mdtp_separator" android:layout_alignBaseline="@id/mdtp_separator" android:importantForAccessibility="no" style="@style/mdtp_time_label"/>
  <FrameLayout android:background="@0x0106000D" android:clipChildren="false" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/mdtp_extra_time_label_margin" android:layout_marginRight="@dimen/mdtp_extra_time_label_margin" android:layout_alignLeft="@id/mdtp_hour_space" android:layout_alignRight="@id/mdtp_hour_space" android:layout_alignBottom="@id/mdtp_separator">
    <com.wdullaer.materialdatetimepicker.AccessibleTextView android:textColor="@color/mdtp_white" android:gravity="0x00000001" android:layout_gravity="0x00000011" android:id="@id/mdtp_hours" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_placeholder" style="@style/mdtp_time_label"/>
  </FrameLayout>
  <TextView android:textColor="@color/mdtp_accent_color_focused" android:id="@id/mdtp_separator" android:background="@0x0106000D" android:paddingLeft="@dimen/mdtp_separator_padding" android:paddingRight="@dimen/mdtp_separator_padding" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_separator" android:layout_above="@id/mdtp_seconds_space" android:layout_centerHorizontal="true" android:importantForAccessibility="no" style="@style/mdtp_time_label"/>
  <TextView android:textColor="@color/mdtp_accent_color_focused" android:id="@id/mdtp_minutes_space" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_placeholder" android:layout_toRightOf="@id/mdtp_separator" android:layout_alignBaseline="@id/mdtp_separator" android:importantForAccessibility="no" style="@style/mdtp_time_label"/>
  <FrameLayout android:background="@0x0106000D" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/mdtp_extra_time_label_margin" android:layout_marginRight="@dimen/mdtp_extra_time_label_margin" android:layout_alignLeft="@id/mdtp_minutes_space" android:layout_alignRight="@id/mdtp_minutes_space" android:layout_alignBottom="@id/mdtp_separator">
    <com.wdullaer.materialdatetimepicker.AccessibleTextView android:textColor="@color/mdtp_accent_color_focused" android:gravity="0x00000001" android:layout_gravity="0x00000011" android:id="@id/mdtp_minutes" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_placeholder" style="@style/mdtp_time_label"/>
  </FrameLayout>
  <TextView android:textColor="@color/mdtp_accent_color_focused" android:id="@id/mdtp_separator_seconds" android:background="@0x0106000D" android:paddingLeft="@dimen/mdtp_separator_padding" android:paddingRight="@dimen/mdtp_separator_padding" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_separator" android:layout_toRightOf="@id/mdtp_minutes_space" android:importantForAccessibility="no" style="@style/mdtp_time_label"/>
  <TextView android:textColor="@color/mdtp_accent_color_focused" android:id="@id/mdtp_seconds_space" android:background="@0x0106000D" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_placeholder" android:layout_alignBottom="@id/mdtp_center_view" android:layout_centerInParent="true" android:importantForAccessibility="no" style="@style/mdtp_time_label_small"/>
  <FrameLayout android:background="@0x0106000D" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/mdtp_extra_time_label_margin" android:layout_marginRight="@dimen/mdtp_extra_time_label_margin" android:layout_alignLeft="@id/mdtp_seconds_space" android:layout_alignRight="@id/mdtp_seconds_space" android:layout_alignBottom="@id/mdtp_center_view">
    <com.wdullaer.materialdatetimepicker.AccessibleTextView android:textColor="@color/mdtp_accent_color_focused" android:gravity="0x00000001" android:layout_gravity="0x00000011" android:id="@id/mdtp_seconds" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_placeholder" style="@style/mdtp_time_label_small"/>
  </FrameLayout>
  <LinearLayout android:orientation="vertical" android:id="@id/mdtp_ampm_layout" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="20.000000dip" android:layout_below="@id/mdtp_seconds_space" android:layout_centerHorizontal="true">
    <TextView android:textColor="@color/mdtp_accent_color_focused" android:id="@id/mdtp_am_label" android:background="@0x0106000D" android:paddingLeft="@dimen/mdtp_ampm_left_padding" android:paddingRight="@dimen/mdtp_ampm_left_padding" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_am" android:importantForAccessibility="no" style="@style/mdtp_ampm_label"/>
    <TextView android:textColor="@color/mdtp_accent_color_focused" android:id="@id/mdtp_pm_label" android:background="@0x0106000D" android:paddingLeft="@dimen/mdtp_ampm_left_padding" android:paddingRight="@dimen/mdtp_ampm_left_padding" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="6.000000dip" android:text="@string/mdtp_pm" android:importantForAccessibility="no" style="@style/mdtp_ampm_label"/>
  </LinearLayout>
</RelativeLayout>
```
