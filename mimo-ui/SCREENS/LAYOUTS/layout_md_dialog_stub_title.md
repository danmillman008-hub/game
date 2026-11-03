# پروندهٔ لایه — `res/layout/md_dialog_stub_title.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/md_dialog_stub_title.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/md_dialog_stub_title.xml`](../../SOURCE/res/layout/md_dialog_stub_title.xml) |
| SHA-256 دیکد | `ad22d8ee5c5e7c572c2f09dc7aa55385d8cf3f3b6ce77283c66631bbb0c178e3` |
| ریشه | `com.afollestad.materialdialogs.internal.main.DialogTitleLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.afollestad.materialdialogs.internal.main.DialogTitleLayout  #@id/md_title_layout
   ├─ ImageView  #@id/md_icon_title
   └─ com.afollestad.materialdialogs.internal.rtl.RtlTextView  #@id/md_text_title
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.afollestad.materialdialogs.internal.main.DialogTitleLayout` | `android:id` | `@id/md_title_layout` |
| 2 | `com.afollestad.materialdialogs.internal.main.DialogTitleLayout` | `android:layout_width` | `match_parent` |
| 3 | `com.afollestad.materialdialogs.internal.main.DialogTitleLayout` | `android:layout_height` | `wrap_content` |
| 4 | `ImageView` | `android:id` | `@id/md_icon_title` |
| 5 | `ImageView` | `style` | `@style/MD_Dialog_Icon` |
| 6 | `com.afollestad.materialdialogs.internal.rtl.RtlTextView` | `android:id` | `@id/md_text_title` |
| 7 | `com.afollestad.materialdialogs.internal.rtl.RtlTextView` | `android:visibility` | `gone` |
| 8 | `com.afollestad.materialdialogs.internal.rtl.RtlTextView` | `android:layout_width` | `wrap_content` |
| 9 | `com.afollestad.materialdialogs.internal.rtl.RtlTextView` | `android:layout_height` | `wrap_content` |
| 10 | `com.afollestad.materialdialogs.internal.rtl.RtlTextView` | `style` | `@style/MD_Dialog_Title_Text` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/MD_Dialog_Icon` | `[{'attr': 'android:visibility', 'attr_id': '0x010100DC', 'value': '2', 'value_type': 'int_dec'}, {'attr': 'android:layout_width', 'attr_id': '0x010100F4', 'value': '56.000000dip', 'value_type': 'dimension'}, {'attr': 'android:layout_height', 'attr_id': '0x010100F5', 'value': '56.000000dip', 'value_type': 'dimension'}, {'attr': 'android:scaleType', 'attr_id': '0x0101011D', 'value': '3', 'value_type': 'int_dec'}]` |
| `@style/MD_Dialog_Title_Text` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/md_title_textsize', 'value_type': 'reference'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '?android:01010036', 'value_type': 'attribute'}, {'attr': 'android:fontFamily', 'attr_id': '0x010103AC', 'value': 'sans-serif-medium', 'value_type': 'string'}]` |

## ۴. شناسه‌های `@id`

```text
@id/md_icon_title
@id/md_text_title
@id/md_title_layout
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
<com.afollestad.materialdialogs.internal.main.DialogTitleLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/md_title_layout" android:layout_width="match_parent" android:layout_height="wrap_content">
  <ImageView android:id="@id/md_icon_title" style="@style/MD_Dialog_Icon"/>
  <com.afollestad.materialdialogs.internal.rtl.RtlTextView android:id="@id/md_text_title" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/MD_Dialog_Title_Text"/>
</com.afollestad.materialdialogs.internal.main.DialogTitleLayout>
```
