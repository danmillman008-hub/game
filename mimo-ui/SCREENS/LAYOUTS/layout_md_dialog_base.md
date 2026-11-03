# پروندهٔ لایه — `res/layout/md_dialog_base.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/md_dialog_base.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/md_dialog_base.xml`](../../SOURCE/res/layout/md_dialog_base.xml) |
| SHA-256 دیکد | `7ebf2fb16896bebe919cc961018f86949c088cab60d8b66aba943f38d2769e9d` |
| ریشه | `com.afollestad.materialdialogs.internal.main.DialogLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 2 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.afollestad.materialdialogs.internal.main.DialogLayout  #@id/md_root
   ├─ include
   ├─ com.afollestad.materialdialogs.internal.message.DialogContentLayout  #@id/md_content_layout
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.afollestad.materialdialogs.internal.main.DialogLayout` | `android:id` | `@id/md_root` |
| 2 | `com.afollestad.materialdialogs.internal.main.DialogLayout` | `android:clipChildren` | `true` |
| 3 | `com.afollestad.materialdialogs.internal.main.DialogLayout` | `android:layout_width` | `match_parent` |
| 4 | `com.afollestad.materialdialogs.internal.main.DialogLayout` | `android:layout_height` | `wrap_content` |
| 5 | `include` | `layout` | `@layout/md_dialog_stub_title` |
| 6 | `com.afollestad.materialdialogs.internal.message.DialogContentLayout` | `android:id` | `@id/md_content_layout` |
| 7 | `com.afollestad.materialdialogs.internal.message.DialogContentLayout` | `android:layout_width` | `match_parent` |
| 8 | `com.afollestad.materialdialogs.internal.message.DialogContentLayout` | `android:layout_height` | `wrap_content` |
| 9 | `include` | `layout` | `@layout/md_dialog_stub_buttons` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/md_content_layout
@id/md_root
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/md_dialog_stub_buttons
@layout/md_dialog_stub_title
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<com.afollestad.materialdialogs.internal.main.DialogLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/md_root" android:clipChildren="true" android:layout_width="match_parent" android:layout_height="wrap_content">
  <include layout="@layout/md_dialog_stub_title"/>
  <com.afollestad.materialdialogs.internal.message.DialogContentLayout android:id="@id/md_content_layout" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  <include layout="@layout/md_dialog_stub_buttons"/>
</com.afollestad.materialdialogs.internal.main.DialogLayout>
```
