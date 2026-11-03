# پروندهٔ لایه — `res/layout/wrapper_fragment_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/wrapper_fragment_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/wrapper_fragment_activity.xml`](../../SOURCE/res/layout/wrapper_fragment_activity.xml) |
| SHA-256 دیکد | `94fc0ae88852ac5096210f16fb7a7528e7b183f5ac671011ed87af074001df28` |
| ریشه | `androidx.fragment.app.FragmentContainerView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 1 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.fragment.app.FragmentContainerView  #@id/fragment_container_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.fragment.app.FragmentContainerView` | `android:id` | `@id/fragment_container_view` |
| 2 | `androidx.fragment.app.FragmentContainerView` | `android:layout_width` | `match_parent` |
| 3 | `androidx.fragment.app.FragmentContainerView` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/fragment_container_view
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.base.WrapperFragmentActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.fragment.app.FragmentContainerView xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/fragment_container_view" android:layout_width="match_parent" android:layout_height="match_parent"/>
```
