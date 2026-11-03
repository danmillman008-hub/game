# پروندهٔ لایه — `res/layout/complex_wrap_expand.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/complex_wrap_expand.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/complex_wrap_expand.xml`](../../SOURCE/res/layout/complex_wrap_expand.xml) |
| SHA-256 دیکد | `c22c5b190f7c247df1a1c971dec2cdf6038c24c7eac4c66250c46851dfef893e` |
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
| 3 | `RelativeLayout` | `android:layout_width` | `wrap_content` |
| 4 | `RelativeLayout` | `android:layout_height` | `0.000000dip` |
| 5 | `RelativeLayout` | `android:layout_weight` | `1.000000` |
| 6 | `ViewStub` | `android:id` | `@id/glanceViewStub` |
| 7 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 8 | `ViewStub` | `android:layout_height` | `match_parent` |

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
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/relativeLayout" android:tag="glanceComplexLayout" android:layout_width="wrap_content" android:layout_height="0.000000dip" android:layout_weight="1.000000">
  <ViewStub android:id="@id/glanceViewStub" android:layout_width="wrap_content" android:layout_height="match_parent"/>
</RelativeLayout>
```
