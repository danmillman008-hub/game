# پروندهٔ لایه — `res/layout/layout_choice_card_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/layout_choice_card_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/layout_choice_card_item.xml`](../../SOURCE/res/layout/layout_choice_card_item.xml) |
| SHA-256 دیکد | `6ec5e78dcb910e387d064b49a2f372e54d2f71d5ff3604055faf540c27bdc420` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ com.google.android.material.radiobutton.MaterialRadioButton  #@id/radio_choice_card_item
   └─ TextView  #@id/tv_choice_card_item_name
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000010` |
| 2 | `LinearLayout` | `android:padding` | `@dimen/spacing_s` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `com.google.android.material.radiobutton.MaterialRadioButton` | `android:id` | `@id/radio_choice_card_item` |
| 6 | `com.google.android.material.radiobutton.MaterialRadioButton` | `android:focusable` | `false` |
| 7 | `com.google.android.material.radiobutton.MaterialRadioButton` | `android:clickable` | `false` |
| 8 | `com.google.android.material.radiobutton.MaterialRadioButton` | `android:layout_width` | `wrap_content` |
| 9 | `com.google.android.material.radiobutton.MaterialRadioButton` | `android:layout_height` | `wrap_content` |
| 10 | `com.google.android.material.radiobutton.MaterialRadioButton` | `style` | `@style/MaterialRadioButton` |
| 11 | `TextView` | `android:textColor` | `@color/text_primary` |
| 12 | `TextView` | `android:id` | `@id/tv_choice_card_item_name` |
| 13 | `TextView` | `android:layout_width` | `0.000000dip` |
| 14 | `TextView` | `android:layout_height` | `wrap_content` |
| 15 | `TextView` | `android:layout_weight` | `1.000000` |
| 16 | `TextView` | `style` | `@style/TextP2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_s` | `12.000000dip` |
| `@style/MaterialRadioButton` | `[{'attr': 'attr.buttonTint', 'attr_id': '0x7F0400B5', 'value': '@color/material_radiobutton', 'value_type': 'reference'}, {'attr': 'attr.useMaterialThemeColors', 'attr_id': '0x7F040680', 'value': 'false', 'value_type': 'int_boolean'}]` |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/radio_choice_card_item
@id/tv_choice_card_item_name
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000010" android:padding="@dimen/spacing_s" android:layout_width="match_parent" android:layout_height="wrap_content">
  <com.google.android.material.radiobutton.MaterialRadioButton android:id="@id/radio_choice_card_item" android:focusable="false" android:clickable="false" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/MaterialRadioButton"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_choice_card_item_name" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000" style="@style/TextP2"/>
</LinearLayout>
```
