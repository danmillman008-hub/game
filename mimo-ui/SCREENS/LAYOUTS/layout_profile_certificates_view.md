# پروندهٔ لایه — `res/layout/profile_certificates_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_certificates_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_certificates_view.xml`](../../SOURCE/res/layout/profile_certificates_view.xml) |
| SHA-256 دیکد | `275366e8aba771f03d19239a037f6a57233bb754acf9fef4f4298214e0ec5767` |
| ریشه | `merge` |
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
└─ merge
   └─ LinearLayout  #@id/profile_paths_container
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:id` | `@id/profile_paths_container` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/profile_paths_container
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.certificates.CertificateActivity
com.getmimo.ui.profile.main.ProfileFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android">
  <LinearLayout android:orientation="vertical" android:id="@id/profile_paths_container" android:layout_width="match_parent" android:layout_height="wrap_content"/>
</merge>
```
