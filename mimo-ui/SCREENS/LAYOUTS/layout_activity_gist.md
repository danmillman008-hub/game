# پروندهٔ لایه — `res/layout/activity_gist.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/activity_gist.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/activity_gist.xml`](../../SOURCE/res/layout/activity_gist.xml) |
| SHA-256 دیکد | `f4251b55684aaac5637c0c00b85ff16ca53b388b2abe2239fdd822891cfd6fad` |
| ریشه | `RelativeLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RelativeLayout  #@id/modalGistViewLayout
   └─ io.customer.messaginginapp.ui.ModalInAppMessageView  #@id/gistView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `RelativeLayout` | `android:id` | `@id/modalGistViewLayout` |
| 2 | `RelativeLayout` | `android:visibility` | `gone` |
| 3 | `RelativeLayout` | `android:layout_width` | `match_parent` |
| 4 | `RelativeLayout` | `android:layout_height` | `match_parent` |
| 5 | `RelativeLayout` | `android:alpha` | `0.000000` |
| 6 | `io.customer.messaginginapp.ui.ModalInAppMessageView` | `android:id` | `@id/gistView` |
| 7 | `io.customer.messaginginapp.ui.ModalInAppMessageView` | `android:layout_width` | `match_parent` |
| 8 | `io.customer.messaginginapp.ui.ModalInAppMessageView` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/gistView
@id/modalGistViewLayout
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
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/modalGistViewLayout" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent" android:alpha="0.000000">
  <io.customer.messaginginapp.ui.ModalInAppMessageView android:id="@id/gistView" android:layout_width="match_parent" android:layout_height="match_parent"/>
</RelativeLayout>
```
