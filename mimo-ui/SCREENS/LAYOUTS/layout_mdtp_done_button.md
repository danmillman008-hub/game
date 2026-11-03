# پروندهٔ لایه — `res/layout/mdtp_done_button.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mdtp_done_button.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mdtp_done_button.xml`](../../SOURCE/res/layout/mdtp_done_button.xml) |
| SHA-256 دیکد | `806099815de4f928abd841c64fa1291405f99245fcf8dc4ecceb4b31064f7782` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/mdtp_done_background
   ├─ Button  #@id/mdtp_cancel
   └─ Button  #@id/mdtp_ok
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00800005` |
| 2 | `LinearLayout` | `android:layout_gravity` | `0x00000010` |
| 3 | `LinearLayout` | `android:orientation` | `horizontal` |
| 4 | `LinearLayout` | `android:id` | `@id/mdtp_done_background` |
| 5 | `LinearLayout` | `android:background` | `@0x0106000D` |
| 6 | `LinearLayout` | `android:paddingBottom` | `8.000000dip` |
| 7 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 8 | `LinearLayout` | `android:layout_height` | `56.000000dip` |
| 9 | `Button` | `android:id` | `@id/mdtp_cancel` |
| 10 | `Button` | `android:layout_width` | `wrap_content` |
| 11 | `Button` | `android:layout_height` | `wrap_content` |
| 12 | `Button` | `android:layout_marginRight` | `8.000000dip` |
| 13 | `Button` | `android:text` | `@string/mdtp_cancel` |
| 14 | `Button` | `android:layout_marginEnd` | `8.000000dip` |
| 15 | `Button` | `style` | `@style/mdtp_ActionButton.Text` |
| 16 | `Button` | `android:id` | `@id/mdtp_ok` |
| 17 | `Button` | `android:layout_width` | `wrap_content` |
| 18 | `Button` | `android:layout_height` | `wrap_content` |
| 19 | `Button` | `android:layout_marginRight` | `16.000000dip` |
| 20 | `Button` | `android:text` | `@string/mdtp_ok` |
| 21 | `Button` | `android:layout_marginEnd` | `16.000000dip` |
| 22 | `Button` | `style` | `@style/mdtp_ActionButton.Text` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@string/mdtp_cancel` | `@android:01040000` / `` (et-rEE) / `` (eu-rES) |
| `@string/mdtp_ok` | `@android:0104000A` |
| `@style/mdtp_ActionButton.Text` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/mdtp_material_button_textsize', 'value_type': 'reference'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/mdtp_button_color', 'value_type': 'reference'}, {'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00000011', 'value_type': 'int_hex'}, {'attr': 'android:layout_gravity', 'attr_id': '0x010100B3', 'value': '0x00000010', 'value_type': 'int_hex'}, {'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@drawable/mdtp_material_button_background', 'value_type': 'reference'}, {'attr': 'android:paddingLeft', 'attr_id': '0x010100D6', 'value': '@dimen/mdtp_material_button_textpadding_horizontal', 'value_type': 'reference'}, {'attr': 'android:paddingRight', 'attr_id': '0x010100D8', 'value': '@dimen/mdtp_material_button_textpadding_horizontal', 'value_type': 'reference'}, {'attr': 'android:minWidth', 'attr_id': '0x0101013F', 'value': '@dimen/mdtp_material_button_minwidth', 'value_type': 'reference'}, {'attr': 'android:singleLine', 'attr_id': '0x0101015D', 'value': 'true', 'value_type': 'int_boolean'}, {'attr': 'android:textAllCaps', 'attr_id': '0x0101038C', 'value': 'true', 'value_type': 'int_boolean'}, {'attr': 'android:stateListAnimator', 'attr_id': '0x01010448', 'value': '@null', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/mdtp_cancel
@id/mdtp_done_background
@id/mdtp_ok
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
res/layout-land/mdtp_date_picker_dialog_v2.xml
res/layout-land/mdtp_time_picker_dialog.xml
res/layout-land/mdtp_time_picker_dialog_v2.xml
res/layout-sw600dp-land-v13/mdtp_date_picker_dialog.xml
res/layout-sw600dp-v13/mdtp_date_picker_dialog.xml
res/layout-w270dp-h560dp-v13/mdtp_date_picker_dialog.xml
res/layout/mdtp_date_picker_dialog.xml
res/layout/mdtp_date_picker_dialog_v2.xml
res/layout/mdtp_time_picker_dialog.xml
res/layout/mdtp_time_picker_dialog_v2.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00800005" android:layout_gravity="0x00000010" android:orientation="horizontal" android:id="@id/mdtp_done_background" android:background="@0x0106000D" android:paddingBottom="8.000000dip" android:layout_width="match_parent" android:layout_height="56.000000dip">
  <Button android:id="@id/mdtp_cancel" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginRight="8.000000dip" android:text="@string/mdtp_cancel" android:layout_marginEnd="8.000000dip" style="@style/mdtp_ActionButton.Text"/>
  <Button android:id="@id/mdtp_ok" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginRight="16.000000dip" android:text="@string/mdtp_ok" android:layout_marginEnd="16.000000dip" style="@style/mdtp_ActionButton.Text"/>
</LinearLayout>
```
