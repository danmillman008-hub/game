# پروندهٔ لایه — `res/layout/complex_match_wrap.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/complex_match_wrap.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/complex_match_wrap.xml`](../../SOURCE/res/layout/complex_match_wrap.xml) |
| SHA-256 دیکد | `fb7717e3c279e4d3ebd02441e3331aaf69398b1d5c2a04c626443c796ac1edaa` |
| ریشه | `RelativeLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 2 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RelativeLayout  #@id/relativeLayout
   └─ ViewStub  #@id/glanceViewStub
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `RelativeLayout` | `android:id` | `@id/relativeLayout` |
| 2 | `RelativeLayout` | `android:tag` | `glanceComplexLayout` |
| 3 | `RelativeLayout` | `android:layout_width` | `match_parent` |
| 4 | `RelativeLayout` | `android:layout_height` | `wrap_content` |
| 5 | `ViewStub` | `android:id` | `@id/glanceViewStub` |
| 6 | `ViewStub` | `android:layout_width` | `match_parent` |
| 7 | `ViewStub` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/glanceViewStub
@id/relativeLayout
```

## ۵. ارجاع به لایه‌های دیگر

```text
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/relativeLayout" android:tag="glanceComplexLayout" android:layout_width="match_parent" android:layout_height="wrap_content">
  <ViewStub android:id="@id/glanceViewStub" android:layout_width="match_parent" android:layout_height="wrap_content"/>
</RelativeLayout>
```
