# پروندهٔ لایه — `res/layout/md_listitem.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/md_listitem.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/md_listitem.xml`](../../SOURCE/res/layout/md_listitem.xml) |
| SHA-256 دیکد | `d1fdc9e76dbe31aa5bb4dd492a4b1d7e79eb61ddb70b9b1b6eac764253fed128` |
| ریشه | `LinearLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   └─ com.afollestad.materialdialogs.internal.rtl.RtlTextView  #@id/md_title
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `style` | `@style/MD_ListItem` |
| 2 | `com.afollestad.materialdialogs.internal.rtl.RtlTextView` | `android:id` | `@id/md_title` |
| 3 | `com.afollestad.materialdialogs.internal.rtl.RtlTextView` | `style` | `@style/MD_ListItemText` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/MD_ListItem` | `[{'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00800013', 'value_type': 'int_hex'}, {'attr': 'android:orientation', 'attr_id': '0x010100C4', 'value': '1', 'value_type': 'int_dec'}, {'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@null', 'value_type': 'reference'}, {'attr': 'android:focusable', 'attr_id': '0x010100DA', 'value': 'true', 'value_type': 'int_boolean'}, {'attr': 'android:clickable', 'attr_id': '0x010100E5', 'value': 'true', 'value_type': 'int_boolean'}, {'attr': 'android:layout_width', 'attr_id': '0x010100F4', 'value': '-1', 'value_type': 'int_dec'}, {'attr': 'android:layout_height', 'attr_id': '0x010100F5', 'value': '-2', 'value_type': 'int_dec'}, {'attr': 'android:minHeight', 'attr_id': '0x01010140', 'value': '@dimen/md_listitem_height', 'value_type': 'reference'}]` |
| `@style/MD_ListItemText` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/md_listitem_textsize', 'value_type': 'reference'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/md_list_item_textcolor', 'value_type': 'reference'}, {'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00800013', 'value_type': 'int_hex'}, {'attr': 'android:layout_gravity', 'attr_id': '0x010100B3', 'value': '0x00800013', 'value_type': 'int_hex'}, {'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@null', 'value_type': 'reference'}, {'attr': 'android:layout_width', 'attr_id': '0x010100F4', 'value': '-2', 'value_type': 'int_dec'}, {'attr': 'android:layout_height', 'attr_id': '0x010100F5', 'value': '-2', 'value_type': 'int_dec'}, {'attr': 'android:layout_marginLeft', 'attr_id': '0x010100F7', 'value': '@dimen/md_listitem_margin_left', 'value_type': 'reference'}, {'attr': 'android:layout_marginTop', 'attr_id': '0x010100F8', 'value': '@dimen/md_listitem_vertical_margin', 'value_type': 'reference'}, {'attr': 'android:layout_marginRight', 'attr_id': '0x010100F9', 'value': '@dimen/md_dialog_frame_margin_horizontal', 'value_type': 'reference'}, {'attr': 'android:layout_marginBottom', 'attr_id': '0x010100FA', 'value': '@dimen/md_listitem_vertical_margin', 'value_type': 'reference'}, {'attr': 'android:layout_marginStart', 'attr_id': '0x010103B5', 'value': '@dimen/md_listitem_margin_left', 'value_type': 'reference'}, {'attr': 'android:layout_marginEnd', 'attr_id': '0x010103B6', 'value': '@dimen/md_dialog_frame_margin_horizontal', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/md_title
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" style="@style/MD_ListItem">
  <com.afollestad.materialdialogs.internal.rtl.RtlTextView android:id="@id/md_title" style="@style/MD_ListItemText"/>
</LinearLayout>
```
