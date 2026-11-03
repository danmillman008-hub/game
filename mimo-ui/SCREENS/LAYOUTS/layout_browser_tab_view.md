# پروندهٔ لایه — `res/layout/browser_tab_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/browser_tab_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/browser_tab_view.xml`](../../SOURCE/res/layout/browser_tab_view.xml) |
| SHA-256 دیکد | `89ab4b4eb13b4304a27101feacc3ebeaf8aa710e97883659ceb3f1365773be31` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 2 |
| `ComposeView` | 0 |
| `WebView` | 1 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/container_browser_tab_view
   ├─ com.getmimo.ui.lesson.view.code.BrowserBar  #@id/browserbar_browsertabview
   └─ com.getmimo.ui.components.common.NestedWebView  #@id/webview_browsertabview
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:id` | `@id/container_browser_tab_view` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `LinearLayout` | `android:minHeight` | `320.000000dip` |
| 6 | `com.getmimo.ui.lesson.view.code.BrowserBar` | `android:id` | `@id/browserbar_browsertabview` |
| 7 | `com.getmimo.ui.lesson.view.code.BrowserBar` | `android:layout_width` | `match_parent` |
| 8 | `com.getmimo.ui.lesson.view.code.BrowserBar` | `android:layout_height` | `wrap_content` |
| 9 | `com.getmimo.ui.components.common.NestedWebView` | `android:id` | `@id/webview_browsertabview` |
| 10 | `com.getmimo.ui.components.common.NestedWebView` | `android:layout_width` | `match_parent` |
| 11 | `com.getmimo.ui.components.common.NestedWebView` | `android:layout_height` | `wrap_content` |
| 12 | `com.getmimo.ui.components.common.NestedWebView` | `android:minHeight` | `150.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/browserbar_browsertabview
@id/container_browser_tab_view
@id/webview_browsertabview
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:id="@id/container_browser_tab_view" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="320.000000dip">
  <com.getmimo.ui.lesson.view.code.BrowserBar android:id="@id/browserbar_browsertabview" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  <com.getmimo.ui.components.common.NestedWebView android:id="@id/webview_browsertabview" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="150.000000dip"/>
</LinearLayout>
```
