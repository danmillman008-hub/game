# پروندهٔ لایه — `res/layout/anonymous_feature_locked_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/anonymous_feature_locked_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/anonymous_feature_locked_view.xml`](../../SOURCE/res/layout/anonymous_feature_locked_view.xml) |
| SHA-256 دیکد | `cd17571a40c4043d62ff2119bbc4f90d7888baf6de8c48646077c2afecff2a72` |
| ریشه | `merge` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 1 |
| ارجاع به منابع | 1 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `merge` | `android:layout_width` | `match_parent` |
| 2 | `merge` | `android:layout_height` | `match_parent` |
| 3 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/compose_view` |
| 4 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 5 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/compose_view
```

## ۵. ارجاع به لایه‌های دیگر

```text
match_parent
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.compose.ui.platform.ComposeView android:id="@id/compose_view" android:layout_width="match_parent" android:layout_height="match_parent"/>
</merge>
```
