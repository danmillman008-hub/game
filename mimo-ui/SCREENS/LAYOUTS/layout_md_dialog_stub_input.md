# پروندهٔ لایه — `res/layout/md_dialog_stub_input.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/md_dialog_stub_input.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/md_dialog_stub_input.xml`](../../SOURCE/res/layout/md_dialog_stub_input.xml) |
| SHA-256 دیکد | `737d2fd62de19497b7748ee29b3dd9d4a099dbcf6ac593378ae9bb212a1bf2ab` |
| ریشه | `FrameLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   └─ com.google.android.material.textfield.TextInputLayout  #@id/md_input_layout
      └─ com.google.android.material.textfield.TextInputEditText  #@id/md_input_message
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:paddingLeft` | `@dimen/md_dialog_frame_margin_horizontal` |
| 2 | `FrameLayout` | `android:paddingRight` | `@dimen/md_dialog_frame_margin_horizontal` |
| 3 | `FrameLayout` | `android:paddingBottom` | `@dimen/md_dialog_frame_margin_vertical_less` |
| 4 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 5 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 6 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/md_input_layout` |
| 7 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `match_parent` |
| 8 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 9 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/md_input_message` |
| 10 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 11 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/md_dialog_frame_margin_horizontal` | `24.000000dip` |
| `@dimen/md_dialog_frame_margin_vertical_less` | `16.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/md_input_layout
@id/md_input_message
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
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:paddingLeft="@dimen/md_dialog_frame_margin_horizontal" android:paddingRight="@dimen/md_dialog_frame_margin_horizontal" android:paddingBottom="@dimen/md_dialog_frame_margin_vertical_less" android:layout_width="match_parent" android:layout_height="wrap_content">
  <com.google.android.material.textfield.TextInputLayout android:id="@id/md_input_layout" android:layout_width="match_parent" android:layout_height="wrap_content">
    <com.google.android.material.textfield.TextInputEditText android:id="@id/md_input_message" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  </com.google.android.material.textfield.TextInputLayout>
</FrameLayout>
```
