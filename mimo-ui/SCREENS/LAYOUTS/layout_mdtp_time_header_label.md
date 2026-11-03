# پروندهٔ لایه — `res/layout/mdtp_time_header_label.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mdtp_time_header_label.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mdtp_time_header_label.xml`](../../SOURCE/res/layout/mdtp_time_header_label.xml) |
| SHA-256 دیکد | `38520a7dea7d050eda634d9808ed3233ae7d41acd3b5452d04bbd4fb9a7dc236` |
| ریشه | `RelativeLayout` |
| تعداد گره | 15 |
| تعداد شناسه | 13 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 28 |

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
   ├─ com.wdullaer.materialdatetimepicker.AccessibleTextView  #@id/mdtp_seconds
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
| 4 | `RelativeLayout` | `android:clipChildren` | `false` |
| 5 | `RelativeLayout` | `android:layout_width` | `match_parent` |
| 6 | `RelativeLayout` | `android:layout_height` | `match_parent` |
| 7 | `View` | `android:id` | `@id/mdtp_center_view` |
| 8 | `View` | `android:background` | `#00000000` |
| 9 | `View` | `android:visibility` | `invisible` |
| 10 | `View` | `android:layout_width` | `1.000000dip` |
| 11 | `View` | `android:layout_height` | `1.000000dip` |
| 12 | `View` | `android:layout_centerInParent` | `true` |
| 13 | `View` | `android:importantForAccessibility` | `no` |
| 14 | `TextView` | `android:id` | `@id/mdtp_hour_space` |
| 15 | `TextView` | `android:visibility` | `invisible` |
| 16 | `TextView` | `android:layout_width` | `wrap_content` |
| 17 | `TextView` | `android:layout_height` | `wrap_content` |
| 18 | `TextView` | `android:text` | `@string/mdtp_time_placeholder` |
| 19 | `TextView` | `android:layout_toLeftOf` | `@id/mdtp_separator` |
| 20 | `TextView` | `android:layout_centerVertical` | `true` |
| 21 | `TextView` | `android:importantForAccessibility` | `no` |
| 22 | `TextView` | `style` | `@style/mdtp_time_label` |
| 23 | `FrameLayout` | `android:background` | `@0x0106000D` |
| 24 | `FrameLayout` | `android:clipChildren` | `false` |
| 25 | `FrameLayout` | `android:layout_width` | `0.000000dip` |
| 26 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 27 | `FrameLayout` | `android:layout_marginLeft` | `@dimen/mdtp_extra_time_label_margin` |
| 28 | `FrameLayout` | `android:layout_marginRight` | `@dimen/mdtp_extra_time_label_margin` |
| 29 | `FrameLayout` | `android:layout_alignLeft` | `@id/mdtp_hour_space` |
| 30 | `FrameLayout` | `android:layout_alignRight` | `@id/mdtp_hour_space` |
| 31 | `FrameLayout` | `android:layout_centerVertical` | `true` |
| 32 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:textColor` | `@color/mdtp_white` |
| 33 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:gravity` | `0x00000001` |
| 34 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_gravity` | `0x00000011` |
| 35 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:id` | `@id/mdtp_hours` |
| 36 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:background` | `@0x0106000D` |
| 37 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_width` | `wrap_content` |
| 38 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_height` | `wrap_content` |
| 39 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:foreground` | `?attr/selectableItemBackgroundBorderless` |
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
| 50 | `TextView` | `android:layout_alignRight` | `@id/mdtp_center_view` |
| 51 | `TextView` | `android:layout_centerVertical` | `true` |
| 52 | `TextView` | `android:importantForAccessibility` | `no` |
| 53 | `TextView` | `style` | `@style/mdtp_time_label` |
| 54 | `TextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 55 | `TextView` | `android:id` | `@id/mdtp_minutes_space` |
| 56 | `TextView` | `android:visibility` | `invisible` |
| 57 | `TextView` | `android:layout_width` | `wrap_content` |
| 58 | `TextView` | `android:layout_height` | `wrap_content` |
| 59 | `TextView` | `android:text` | `@string/mdtp_time_placeholder` |
| 60 | `TextView` | `android:layout_toRightOf` | `@id/mdtp_separator` |
| 61 | `TextView` | `android:layout_centerVertical` | `true` |
| 62 | `TextView` | `android:importantForAccessibility` | `no` |
| 63 | `TextView` | `style` | `@style/mdtp_time_label` |
| 64 | `FrameLayout` | `android:background` | `@0x0106000D` |
| 65 | `FrameLayout` | `android:clipChildren` | `false` |
| 66 | `FrameLayout` | `android:layout_width` | `0.000000dip` |
| 67 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 68 | `FrameLayout` | `android:layout_marginLeft` | `@dimen/mdtp_extra_time_label_margin` |
| 69 | `FrameLayout` | `android:layout_marginRight` | `@dimen/mdtp_extra_time_label_margin` |
| 70 | `FrameLayout` | `android:layout_alignLeft` | `@id/mdtp_minutes_space` |
| 71 | `FrameLayout` | `android:layout_alignRight` | `@id/mdtp_minutes_space` |
| 72 | `FrameLayout` | `android:layout_centerVertical` | `true` |
| 73 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 74 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:gravity` | `0x00000001` |
| 75 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_gravity` | `0x00000011` |
| 76 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:id` | `@id/mdtp_minutes` |
| 77 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:background` | `@0x0106000D` |
| 78 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_width` | `wrap_content` |
| 79 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_height` | `wrap_content` |
| 80 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:foreground` | `?attr/selectableItemBackgroundBorderless` |
| 81 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:text` | `@string/mdtp_time_placeholder` |
| 82 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `style` | `@style/mdtp_time_label` |
| 83 | `TextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 84 | `TextView` | `android:id` | `@id/mdtp_separator_seconds` |
| 85 | `TextView` | `android:background` | `@0x0106000D` |
| 86 | `TextView` | `android:paddingLeft` | `@dimen/mdtp_separator_padding` |
| 87 | `TextView` | `android:paddingRight` | `@dimen/mdtp_separator_padding` |
| 88 | `TextView` | `android:layout_width` | `wrap_content` |
| 89 | `TextView` | `android:layout_height` | `wrap_content` |
| 90 | `TextView` | `android:text` | `@string/mdtp_time_separator` |
| 91 | `TextView` | `android:layout_toRightOf` | `@id/mdtp_minutes_space` |
| 92 | `TextView` | `android:layout_centerVertical` | `true` |
| 93 | `TextView` | `android:importantForAccessibility` | `no` |
| 94 | `TextView` | `style` | `@style/mdtp_time_label` |
| 95 | `TextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 96 | `TextView` | `android:id` | `@id/mdtp_seconds_space` |
| 97 | `TextView` | `android:background` | `@0x0106000D` |
| 98 | `TextView` | `android:visibility` | `invisible` |
| 99 | `TextView` | `android:layout_width` | `wrap_content` |
| 100 | `TextView` | `android:layout_height` | `wrap_content` |
| 101 | `TextView` | `android:text` | `@string/mdtp_time_placeholder` |
| 102 | `TextView` | `android:layout_toRightOf` | `@id/mdtp_separator_seconds` |
| 103 | `TextView` | `android:layout_centerVertical` | `true` |
| 104 | `TextView` | `android:importantForAccessibility` | `no` |
| 105 | `TextView` | `style` | `@style/mdtp_time_label_small` |
| 106 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 107 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:gravity` | `0x00000001` |
| 108 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_gravity` | `0x00000011` |
| 109 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:id` | `@id/mdtp_seconds` |
| 110 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:background` | `@0x0106000D` |
| 111 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_width` | `wrap_content` |
| 112 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_height` | `wrap_content` |
| 113 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:foreground` | `?attr/selectableItemBackgroundBorderless` |
| 114 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:text` | `@string/mdtp_time_placeholder` |
| 115 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_toRightOf` | `@id/mdtp_separator_seconds` |
| 116 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `android:layout_alignBaseline` | `@id/mdtp_separator` |
| 117 | `com.wdullaer.materialdatetimepicker.AccessibleTextView` | `style` | `@style/mdtp_time_label_small` |
| 118 | `LinearLayout` | `android:orientation` | `vertical` |
| 119 | `LinearLayout` | `android:id` | `@id/mdtp_ampm_layout` |
| 120 | `LinearLayout` | `android:background` | `@0x0106000D` |
| 121 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 122 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 123 | `LinearLayout` | `android:foreground` | `?attr/selectableItemBackgroundBorderless` |
| 124 | `LinearLayout` | `android:baselineAlignedChildIndex` | `1` |
| 125 | `LinearLayout` | `android:layout_toRightOf` | `@id/mdtp_seconds` |
| 126 | `LinearLayout` | `android:layout_alignBaseline` | `@id/mdtp_seconds` |
| 127 | `TextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 128 | `TextView` | `android:id` | `@id/mdtp_am_label` |
| 129 | `TextView` | `android:background` | `@0x0106000D` |
| 130 | `TextView` | `android:paddingLeft` | `@dimen/mdtp_ampm_left_padding` |
| 131 | `TextView` | `android:paddingRight` | `@dimen/mdtp_ampm_left_padding` |
| 132 | `TextView` | `android:layout_width` | `wrap_content` |
| 133 | `TextView` | `android:layout_height` | `wrap_content` |
| 134 | `TextView` | `android:text` | `@string/mdtp_am` |
| 135 | `TextView` | `android:importantForAccessibility` | `no` |
| 136 | `TextView` | `style` | `@style/mdtp_ampm_label` |
| 137 | `TextView` | `android:textColor` | `@color/mdtp_accent_color_focused` |
| 138 | `TextView` | `android:id` | `@id/mdtp_pm_label` |
| 139 | `TextView` | `android:background` | `@0x0106000D` |
| 140 | `TextView` | `android:paddingLeft` | `@dimen/mdtp_ampm_left_padding` |
| 141 | `TextView` | `android:paddingRight` | `@dimen/mdtp_ampm_left_padding` |
| 142 | `TextView` | `android:layout_width` | `wrap_content` |
| 143 | `TextView` | `android:layout_height` | `wrap_content` |
| 144 | `TextView` | `android:layout_marginTop` | `6.000000dip` |
| 145 | `TextView` | `android:text` | `@string/mdtp_pm` |
| 146 | `TextView` | `android:importantForAccessibility` | `no` |
| 147 | `TextView` | `style` | `@style/mdtp_ampm_label` |

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
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000011" android:id="@id/mdtp_time_display" android:background="@color/mdtp_accent_color" android:clipChildren="false" android:layout_width="match_parent" android:layout_height="match_parent">
  <View android:id="@id/mdtp_center_view" android:background="#00000000" android:visibility="invisible" android:layout_width="1.000000dip" android:layout_height="1.000000dip" android:layout_centerInParent="true" android:importantForAccessibility="no"/>
  <TextView android:id="@id/mdtp_hour_space" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_placeholder" android:layout_toLeftOf="@id/mdtp_separator" android:layout_centerVertical="true" android:importantForAccessibility="no" style="@style/mdtp_time_label"/>
  <FrameLayout android:background="@0x0106000D" android:clipChildren="false" android:layout_width="0.000000dip" android:layout_height="match_parent" android:layout_marginLeft="@dimen/mdtp_extra_time_label_margin" android:layout_marginRight="@dimen/mdtp_extra_time_label_margin" android:layout_alignLeft="@id/mdtp_hour_space" android:layout_alignRight="@id/mdtp_hour_space" android:layout_centerVertical="true">
    <com.wdullaer.materialdatetimepicker.AccessibleTextView android:textColor="@color/mdtp_white" android:gravity="0x00000001" android:layout_gravity="0x00000011" android:id="@id/mdtp_hours" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="wrap_content" android:foreground="?attr/selectableItemBackgroundBorderless" android:text="@string/mdtp_time_placeholder" style="@style/mdtp_time_label"/>
  </FrameLayout>
  <TextView android:textColor="@color/mdtp_accent_color_focused" android:id="@id/mdtp_separator" android:background="@0x0106000D" android:paddingLeft="@dimen/mdtp_separator_padding" android:paddingRight="@dimen/mdtp_separator_padding" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_separator" android:layout_alignRight="@id/mdtp_center_view" android:layout_centerVertical="true" android:importantForAccessibility="no" style="@style/mdtp_time_label"/>
  <TextView android:textColor="@color/mdtp_accent_color_focused" android:id="@id/mdtp_minutes_space" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_placeholder" android:layout_toRightOf="@id/mdtp_separator" android:layout_centerVertical="true" android:importantForAccessibility="no" style="@style/mdtp_time_label"/>
  <FrameLayout android:background="@0x0106000D" android:clipChildren="false" android:layout_width="0.000000dip" android:layout_height="match_parent" android:layout_marginLeft="@dimen/mdtp_extra_time_label_margin" android:layout_marginRight="@dimen/mdtp_extra_time_label_margin" android:layout_alignLeft="@id/mdtp_minutes_space" android:layout_alignRight="@id/mdtp_minutes_space" android:layout_centerVertical="true">
    <com.wdullaer.materialdatetimepicker.AccessibleTextView android:textColor="@color/mdtp_accent_color_focused" android:gravity="0x00000001" android:layout_gravity="0x00000011" android:id="@id/mdtp_minutes" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="wrap_content" android:foreground="?attr/selectableItemBackgroundBorderless" android:text="@string/mdtp_time_placeholder" style="@style/mdtp_time_label"/>
  </FrameLayout>
  <TextView android:textColor="@color/mdtp_accent_color_focused" android:id="@id/mdtp_separator_seconds" android:background="@0x0106000D" android:paddingLeft="@dimen/mdtp_separator_padding" android:paddingRight="@dimen/mdtp_separator_padding" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_separator" android:layout_toRightOf="@id/mdtp_minutes_space" android:layout_centerVertical="true" android:importantForAccessibility="no" style="@style/mdtp_time_label"/>
  <TextView android:textColor="@color/mdtp_accent_color_focused" android:id="@id/mdtp_seconds_space" android:background="@0x0106000D" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_time_placeholder" android:layout_toRightOf="@id/mdtp_separator_seconds" android:layout_centerVertical="true" android:importantForAccessibility="no" style="@style/mdtp_time_label_small"/>
  <com.wdullaer.materialdatetimepicker.AccessibleTextView android:textColor="@color/mdtp_accent_color_focused" android:gravity="0x00000001" android:layout_gravity="0x00000011" android:id="@id/mdtp_seconds" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="wrap_content" android:foreground="?attr/selectableItemBackgroundBorderless" android:text="@string/mdtp_time_placeholder" android:layout_toRightOf="@id/mdtp_separator_seconds" android:layout_alignBaseline="@id/mdtp_separator" style="@style/mdtp_time_label_small"/>
  <LinearLayout android:orientation="vertical" android:id="@id/mdtp_ampm_layout" android:background="@0x0106000D" android:layout_width="wrap_content" android:layout_height="wrap_content" android:foreground="?attr/selectableItemBackgroundBorderless" android:baselineAlignedChildIndex="1" android:layout_toRightOf="@id/mdtp_seconds" android:layout_alignBaseline="@id/mdtp_seconds">
    <TextView android:textColor="@color/mdtp_accent_color_focused" android:id="@id/mdtp_am_label" android:background="@0x0106000D" android:paddingLeft="@dimen/mdtp_ampm_left_padding" android:paddingRight="@dimen/mdtp_ampm_left_padding" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mdtp_am" android:importantForAccessibility="no" style="@style/mdtp_ampm_label"/>
    <TextView android:textColor="@color/mdtp_accent_color_focused" android:id="@id/mdtp_pm_label" android:background="@0x0106000D" android:paddingLeft="@dimen/mdtp_ampm_left_padding" android:paddingRight="@dimen/mdtp_ampm_left_padding" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="6.000000dip" android:text="@string/mdtp_pm" android:importantForAccessibility="no" style="@style/mdtp_ampm_label"/>
  </LinearLayout>
</RelativeLayout>
```
