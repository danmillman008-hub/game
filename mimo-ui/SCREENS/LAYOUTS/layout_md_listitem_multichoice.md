# پروندهٔ لایه — `res/layout/md_listitem_multichoice.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/md_listitem_multichoice.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/md_listitem_multichoice.xml`](../../SOURCE/res/layout/md_listitem_multichoice.xml) |
| SHA-256 دیکد | `5a02b1a4377a9ea66f9641fcbad2cc3462ace9346870975e18d24009e2e10cd8` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ androidx.appcompat.widget.AppCompatCheckBox  #@id/md_control
   └─ com.afollestad.materialdialogs.internal.rtl.RtlTextView  #@id/md_title
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `style` | `@style/MD_ListItem.Choice` |
| 2 | `androidx.appcompat.widget.AppCompatCheckBox` | `android:id` | `@id/md_control` |
| 3 | `androidx.appcompat.widget.AppCompatCheckBox` | `style` | `@style/MD_ListItem_Control` |
| 4 | `com.afollestad.materialdialogs.internal.rtl.RtlTextView` | `android:id` | `@id/md_title` |
| 5 | `com.afollestad.materialdialogs.internal.rtl.RtlTextView` | `style` | `@style/MD_ListItemText.Choice` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/MD_ListItem.Choice` | `[{'attr': 'android:orientation', 'attr_id': '0x010100C4', 'value': '0', 'value_type': 'int_dec'}, {'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@null', 'value_type': 'reference'}, {'attr': 'android:paddingLeft', 'attr_id': '0x010100D6', 'value': '@dimen/md_dialog_frame_margin_horizontal', 'value_type': 'reference'}, {'attr': 'android:paddingRight', 'attr_id': '0x010100D8', 'value': '@dimen/md_dialog_frame_margin_horizontal', 'value_type': 'reference'}, {'attr': 'android:focusable', 'attr_id': '0x010100DA', 'value': 'true', 'value_type': 'int_boolean'}, {'attr': 'android:descendantFocusability', 'attr_id': '0x010100F1', 'value': '2', 'value_type': 'int_dec'}, {'attr': 'android:minHeight', 'attr_id': '0x01010140', 'value': '@dimen/md_listitem_height', 'value_type': 'reference'}]` |
| `@style/MD_ListItemText.Choice` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/md_listitem_textsize', 'value_type': 'reference'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/md_list_item_textcolor', 'value_type': 'reference'}, {'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00800013', 'value_type': 'int_hex'}, {'attr': 'android:layout_gravity', 'attr_id': '0x010100B3', 'value': '0x00800013', 'value_type': 'int_hex'}, {'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@null', 'value_type': 'reference'}, {'attr': 'android:paddingLeft', 'attr_id': '0x010100D6', 'value': '@dimen/md_listitem_control_margin', 'value_type': 'reference'}, {'attr': 'android:paddingTop', 'attr_id': '0x010100D7', 'value': '@dimen/md_listitem_vertical_margin_choice', 'value_type': 'reference'}, {'attr': 'android:paddingBottom', 'attr_id': '0x010100D9', 'value': '@dimen/md_listitem_vertical_margin_choice', 'value_type': 'reference'}, {'attr': 'android:layout_width', 'attr_id': '0x010100F4', 'value': '-2', 'value_type': 'int_dec'}, {'attr': 'android:layout_height', 'attr_id': '0x010100F5', 'value': '-2', 'value_type': 'int_dec'}, {'attr': 'android:layout_marginLeft', 'attr_id': '0x010100F7', 'value': '@dimen/md_listitem_margin_left_choice', 'value_type': 'reference'}, {'attr': 'android:layout_marginTop', 'attr_id': '0x010100F8', 'value': '0.000000dip', 'value_type': 'dimension'}, {'attr': 'android:layout_marginBottom', 'attr_id': '0x010100FA', 'value': '0.000000dip', 'value_type': 'dimension'}, {'attr': 'android:minHeight', 'attr_id': '0x01010140', 'value': '@dimen/md_listitem_height', 'value_type': 'reference'}, {'attr': 'android:paddingStart', 'attr_id': '0x010103B3', 'value': '@dimen/md_listitem_control_margin', 'value_type': 'reference'}, {'attr': 'android:layout_marginStart', 'attr_id': '0x010103B5', 'value': '@dimen/md_listitem_margin_left_choice', 'value_type': 'reference'}]` |
| `@style/MD_ListItem_Control` | `[{'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00800013', 'value_type': 'int_hex'}, {'attr': 'android:layout_gravity', 'attr_id': '0x010100B3', 'value': '0x00800013', 'value_type': 'int_hex'}, {'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@null', 'value_type': 'reference'}, {'attr': 'android:focusable', 'attr_id': '0x010100DA', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'android:clickable', 'attr_id': '0x010100E5', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'android:layout_width', 'attr_id': '0x010100F4', 'value': '-2', 'value_type': 'int_dec'}, {'attr': 'android:layout_height', 'attr_id': '0x010100F5', 'value': '-2', 'value_type': 'int_dec'}]` |

## ۴. شناسه‌های `@id`

```text
@id/md_control
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" style="@style/MD_ListItem.Choice">
  <androidx.appcompat.widget.AppCompatCheckBox android:id="@id/md_control" style="@style/MD_ListItem_Control"/>
  <com.afollestad.materialdialogs.internal.rtl.RtlTextView android:id="@id/md_title" style="@style/MD_ListItemText.Choice"/>
</LinearLayout>
```
