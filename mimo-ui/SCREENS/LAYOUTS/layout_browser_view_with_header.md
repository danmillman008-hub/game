# پروندهٔ لایه — `res/layout/browser_view_with_header.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/browser_view_with_header.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/browser_view_with_header.xml`](../../SOURCE/res/layout/browser_view_with_header.xml) |
| SHA-256 دیکد | `ba5d71daa528d060caf7fa279ea294eb6416dbf4f4d1ba52850e85808042a317` |
| ریشه | `com.getmimo.ui.lesson.view.BrowserViewWithHeader` |
| تعداد گره | 4 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 2 |
| `ComposeView` | 0 |
| `WebView` | 1 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.getmimo.ui.lesson.view.BrowserViewWithHeader  #@id/browser_view_with_header
   ├─ FrameLayout
   │  └─ ImageView
   └─ com.getmimo.ui.components.common.MimoWebView  #@id/browser_tab_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.getmimo.ui.lesson.view.BrowserViewWithHeader` | `android:orientation` | `vertical` |
| 2 | `com.getmimo.ui.lesson.view.BrowserViewWithHeader` | `android:id` | `@id/browser_view_with_header` |
| 3 | `com.getmimo.ui.lesson.view.BrowserViewWithHeader` | `android:background` | `@drawable/webview_output_background` |
| 4 | `com.getmimo.ui.lesson.view.BrowserViewWithHeader` | `android:layout_width` | `match_parent` |
| 5 | `com.getmimo.ui.lesson.view.BrowserViewWithHeader` | `android:layout_height` | `wrap_content` |
| 6 | `com.getmimo.ui.lesson.view.BrowserViewWithHeader` | `android:minHeight` | `180.000000dip` |
| 7 | `FrameLayout` | `android:background` | `@drawable/browser_view_header` |
| 8 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 9 | `FrameLayout` | `android:layout_height` | `16.000000dip` |
| 10 | `ImageView` | `android:layout_gravity` | `0x00800013` |
| 11 | `ImageView` | `android:layout_width` | `wrap_content` |
| 12 | `ImageView` | `android:layout_height` | `wrap_content` |
| 13 | `ImageView` | `android:src` | `@drawable/browser_view_header_dots` |
| 14 | `ImageView` | `android:layout_marginStart` | `6.000000dip` |
| 15 | `ImageView` | `app:tint` | `@color/support_snow` |
| 16 | `com.getmimo.ui.components.common.MimoWebView` | `android:id` | `@id/browser_tab_view` |
| 17 | `com.getmimo.ui.components.common.MimoWebView` | `android:layout_width` | `match_parent` |
| 18 | `com.getmimo.ui.components.common.MimoWebView` | `android:layout_height` | `wrap_content` |
| 19 | `com.getmimo.ui.components.common.MimoWebView` | `android:minHeight` | `180.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/support_snow` | `#FFBFC1D7` / `#FF252746` (night) |

## ۴. شناسه‌های `@id`

```text
@id/browser_tab_view
@id/browser_view_with_header
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
<com.getmimo.ui.lesson.view.BrowserViewWithHeader xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:id="@id/browser_view_with_header" android:background="@drawable/webview_output_background" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="180.000000dip">
  <FrameLayout android:background="@drawable/browser_view_header" android:layout_width="match_parent" android:layout_height="16.000000dip">
    <ImageView android:layout_gravity="0x00800013" android:layout_width="wrap_content" android:layout_height="wrap_content" android:src="@drawable/browser_view_header_dots" android:layout_marginStart="6.000000dip" app:tint="@color/support_snow"/>
  </FrameLayout>
  <com.getmimo.ui.components.common.MimoWebView android:id="@id/browser_tab_view" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="180.000000dip"/>
</com.getmimo.ui.lesson.view.BrowserViewWithHeader>
```
