# پروندهٔ لایه — `res/layout/md_dialog_stub_message.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/md_dialog_stub_message.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/md_dialog_stub_message.xml`](../../SOURCE/res/layout/md_dialog_stub_message.xml) |
| SHA-256 دیکد | `f82ce351a2b88f35feda3b64571419543936bacc3104a69c6e793d9eb100d5c4` |
| ریشه | `com.afollestad.materialdialogs.internal.rtl.RtlTextView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.afollestad.materialdialogs.internal.rtl.RtlTextView  #@id/md_text_message
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.afollestad.materialdialogs.internal.rtl.RtlTextView` | `android:id` | `@id/md_text_message` |
| 2 | `com.afollestad.materialdialogs.internal.rtl.RtlTextView` | `style` | `@style/MD_Dialog_Message` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/MD_Dialog_Message` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/md_message_textsize', 'value_type': 'reference'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '?android:01010038', 'value_type': 'attribute'}, {'attr': 'android:layout_gravity', 'attr_id': '0x010100B3', 'value': '0x00000011', 'value_type': 'int_hex'}, {'attr': 'android:paddingLeft', 'attr_id': '0x010100D6', 'value': '@dimen/md_dialog_frame_margin_horizontal', 'value_type': 'reference'}, {'attr': 'android:paddingRight', 'attr_id': '0x010100D8', 'value': '@dimen/md_dialog_frame_margin_horizontal', 'value_type': 'reference'}, {'attr': 'android:layout_width', 'attr_id': '0x010100F4', 'value': '-1', 'value_type': 'int_dec'}, {'attr': 'android:layout_height', 'attr_id': '0x010100F5', 'value': '-2', 'value_type': 'int_dec'}]` |

## ۴. شناسه‌های `@id`

```text
@id/md_text_message
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
<com.afollestad.materialdialogs.internal.rtl.RtlTextView xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/md_text_message" style="@style/MD_Dialog_Message"/>
```
