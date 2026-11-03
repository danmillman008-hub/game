# پروندهٔ لایه — `res/layout/custom_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/custom_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/custom_dialog.xml`](../../SOURCE/res/layout/custom_dialog.xml) |
| SHA-256 دیکد | `e0238fed00bcbab4eeddc7561cde1fb4f0367078d049cb46ee24b5c80bf895cb` |
| ریشه | `RelativeLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 1 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RelativeLayout
   └─ Button  #@id/dialog_button
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `RelativeLayout` | `android:layout_width` | `match_parent` |
| 2 | `RelativeLayout` | `android:layout_height` | `match_parent` |
| 3 | `Button` | `android:id` | `@id/dialog_button` |
| 4 | `Button` | `android:layout_width` | `100.000000px` |
| 5 | `Button` | `android:layout_height` | `wrap_content` |
| 6 | `Button` | `android:layout_marginTop` | `5.000000dip` |
| 7 | `Button` | `android:layout_marginRight` | `5.000000dip` |
| 8 | `Button` | `android:text` | ` Ok ` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/dialog_button
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
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent">
  <Button android:id="@id/dialog_button" android:layout_width="100.000000px" android:layout_height="wrap_content" android:layout_marginTop="5.000000dip" android:layout_marginRight="5.000000dip" android:text=" Ok "/>
</RelativeLayout>
```
