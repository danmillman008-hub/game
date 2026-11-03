# پروندهٔ لایه — `res/layout/complex_match_fixed.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/complex_match_fixed.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/complex_match_fixed.xml`](../../SOURCE/res/layout/complex_match_fixed.xml) |
| SHA-256 دیکد | `6b55c3f0076a41863f9e56cfa60cc063af3b936af858d47ef621adce9fceb417` |
| ریشه | `RelativeLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RelativeLayout  #@id/relativeLayout
   ├─ FrameLayout  #@id/sizeView
   │  └─ ViewStub  #@id/sizeViewStub
   └─ ViewStub  #@id/glanceViewStub
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `RelativeLayout` | `android:id` | `@id/relativeLayout` |
| 2 | `RelativeLayout` | `android:tag` | `glanceComplexLayout` |
| 3 | `RelativeLayout` | `android:layout_width` | `match_parent` |
| 4 | `RelativeLayout` | `android:layout_height` | `wrap_content` |
| 5 | `FrameLayout` | `android:id` | `@id/sizeView` |
| 6 | `FrameLayout` | `android:visibility` | `invisible` |
| 7 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 8 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 9 | `ViewStub` | `android:id` | `@id/sizeViewStub` |
| 10 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 11 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 12 | `ViewStub` | `android:id` | `@id/glanceViewStub` |
| 13 | `ViewStub` | `android:layout_width` | `match_parent` |
| 14 | `ViewStub` | `android:layout_height` | `0.000000dip` |
| 15 | `ViewStub` | `android:layout_alignTop` | `@id/sizeView` |
| 16 | `ViewStub` | `android:layout_alignBottom` | `@id/sizeView` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/glanceViewStub
@id/relativeLayout
@id/sizeView
@id/sizeViewStub
```

## ۵. ارجاع به لایه‌های دیگر

```text
0.000000dip
@id/sizeView
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
  <FrameLayout android:id="@id/sizeView" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content">
    <ViewStub android:id="@id/sizeViewStub" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
  </FrameLayout>
  <ViewStub android:id="@id/glanceViewStub" android:layout_width="match_parent" android:layout_height="0.000000dip" android:layout_alignTop="@id/sizeView" android:layout_alignBottom="@id/sizeView"/>
</RelativeLayout>
```
