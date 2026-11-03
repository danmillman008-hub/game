# پروندهٔ لایه — `res/layout/root_match_match.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/root_match_match.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/root_match_match.xml`](../../SOURCE/res/layout/root_match_match.xml) |
| SHA-256 دیکد | `29c3a0ab074c405c1cd0e0ab317b05720ee0d80436521b7cb4c982753a019490` |
| ریشه | `FrameLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 1 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/rootView
   └─ ViewStub  #@id/rootStubId
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:theme` | `@style/Glance.AppWidget.Theme` |
| 2 | `FrameLayout` | `android:id` | `@id/rootView` |
| 3 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 4 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 5 | `ViewStub` | `android:id` | `@id/rootStubId` |
| 6 | `ViewStub` | `android:layout_width` | `match_parent` |
| 7 | `ViewStub` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.Theme` | `[]` / `[]` (v29) |

## ۴. شناسه‌های `@id`

```text
@id/rootStubId
@id/rootView
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
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:theme="@style/Glance.AppWidget.Theme" android:id="@id/rootView" android:layout_width="match_parent" android:layout_height="match_parent">
  <ViewStub android:id="@id/rootStubId" android:layout_width="match_parent" android:layout_height="match_parent"/>
</FrameLayout>
```
