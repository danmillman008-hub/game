# پروندهٔ لایه — `res/layout/generic_compose_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/generic_compose_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/generic_compose_view.xml`](../../SOURCE/res/layout/generic_compose_view.xml) |
| SHA-256 دیکد | `12bbac14570091c945eba516da2dd1ccfa63ee5ece9baee27a03a1104bdfb1f2` |
| ریشه | `androidx.compose.ui.platform.ComposeView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 2 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/compose_content` |
| 2 | `androidx.compose.ui.platform.ComposeView` | `android:background` | `@color/background_primary` |
| 3 | `androidx.compose.ui.platform.ComposeView` | `android:fitsSystemWindows` | `false` |
| 4 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 5 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |

## ۴. شناسه‌های `@id`

```text
@id/compose_content
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
<androidx.compose.ui.platform.ComposeView xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/compose_content" android:background="@color/background_primary" android:fitsSystemWindows="false" android:layout_width="match_parent" android:layout_height="match_parent"/>
```
