# پروندهٔ لایه — `res/layout/md_dialog_stub_buttons.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/md_dialog_stub_buttons.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/md_dialog_stub_buttons.xml`](../../SOURCE/res/layout/md_dialog_stub_buttons.xml) |
| SHA-256 دیکد | `b4a40f57480213150597eedad7d5b0c22d387bde49b93c30ccbc8affe506b5dd` |
| ریشه | `com.afollestad.materialdialogs.internal.button.DialogActionButtonLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.afollestad.materialdialogs.internal.button.DialogActionButtonLayout  #@id/md_button_layout
   ├─ androidx.appcompat.widget.AppCompatCheckBox  #@id/md_checkbox_prompt
   ├─ com.afollestad.materialdialogs.internal.button.DialogActionButton  #@id/md_button_positive
   ├─ com.afollestad.materialdialogs.internal.button.DialogActionButton  #@id/md_button_negative
   └─ com.afollestad.materialdialogs.internal.button.DialogActionButton  #@id/md_button_neutral
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.afollestad.materialdialogs.internal.button.DialogActionButtonLayout` | `android:id` | `@id/md_button_layout` |
| 2 | `com.afollestad.materialdialogs.internal.button.DialogActionButtonLayout` | `android:layout_width` | `match_parent` |
| 3 | `com.afollestad.materialdialogs.internal.button.DialogActionButtonLayout` | `android:layout_height` | `wrap_content` |
| 4 | `androidx.appcompat.widget.AppCompatCheckBox` | `android:id` | `@id/md_checkbox_prompt` |
| 5 | `androidx.appcompat.widget.AppCompatCheckBox` | `android:layout_width` | `wrap_content` |
| 6 | `androidx.appcompat.widget.AppCompatCheckBox` | `android:layout_height` | `wrap_content` |
| 7 | `androidx.appcompat.widget.AppCompatCheckBox` | `style` | `@style/MD_Dialog_CheckPrompt` |
| 8 | `com.afollestad.materialdialogs.internal.button.DialogActionButton` | `android:id` | `@id/md_button_positive` |
| 9 | `com.afollestad.materialdialogs.internal.button.DialogActionButton` | `style` | `@style/MD_ActionButton` |
| 10 | `com.afollestad.materialdialogs.internal.button.DialogActionButton` | `android:id` | `@id/md_button_negative` |
| 11 | `com.afollestad.materialdialogs.internal.button.DialogActionButton` | `style` | `@style/MD_ActionButton` |
| 12 | `com.afollestad.materialdialogs.internal.button.DialogActionButton` | `android:id` | `@id/md_button_neutral` |
| 13 | `com.afollestad.materialdialogs.internal.button.DialogActionButton` | `style` | `@style/MD_ActionButton` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/MD_ActionButton` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/md_action_button_textsize', 'value_type': 'reference'}, {'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00000011', 'value_type': 'int_hex'}, {'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@null', 'value_type': 'reference'}, {'attr': 'android:paddingLeft', 'attr_id': '0x010100D6', 'value': '@dimen/md_action_button_padding_horizontal', 'value_type': 'reference'}, {'attr': 'android:paddingRight', 'attr_id': '0x010100D8', 'value': '@dimen/md_action_button_padding_horizontal', 'value_type': 'reference'}, {'attr': 'android:layout_width', 'attr_id': '0x010100F4', 'value': '-2', 'value_type': 'int_dec'}, {'attr': 'android:layout_height', 'attr_id': '0x010100F5', 'value': '-1', 'value_type': 'int_dec'}, {'attr': 'android:minWidth', 'attr_id': '0x0101013F', 'value': '@dimen/md_action_button_min_width', 'value_type': 'reference'}, {'attr': 'android:singleLine', 'attr_id': '0x0101015D', 'value': 'true', 'value_type': 'int_boolean'}, {'attr': 'android:textAllCaps', 'attr_id': '0x0101038C', 'value': 'false', 'value_type': 'int_boolean'}]` |
| `@style/MD_Dialog_CheckPrompt` | `[{'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00800013', 'value_type': 'int_hex'}, {'attr': 'android:visibility', 'attr_id': '0x010100DC', 'value': '2', 'value_type': 'int_dec'}, {'attr': 'android:minHeight', 'attr_id': '0x01010140', 'value': '@dimen/md_checkbox_prompt_height', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/md_button_layout
@id/md_button_negative
@id/md_button_neutral
@id/md_button_positive
@id/md_checkbox_prompt
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/md_dialog_base.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<com.afollestad.materialdialogs.internal.button.DialogActionButtonLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/md_button_layout" android:layout_width="match_parent" android:layout_height="wrap_content">
  <androidx.appcompat.widget.AppCompatCheckBox android:id="@id/md_checkbox_prompt" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/MD_Dialog_CheckPrompt"/>
  <com.afollestad.materialdialogs.internal.button.DialogActionButton android:id="@id/md_button_positive" style="@style/MD_ActionButton"/>
  <com.afollestad.materialdialogs.internal.button.DialogActionButton android:id="@id/md_button_negative" style="@style/MD_ActionButton"/>
  <com.afollestad.materialdialogs.internal.button.DialogActionButton android:id="@id/md_button_neutral" style="@style/MD_ActionButton"/>
</com.afollestad.materialdialogs.internal.button.DialogActionButtonLayout>
```
