# پروندهٔ لایه — `res/layout/base_modal_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/base_modal_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/base_modal_fragment.xml`](../../SOURCE/res/layout/base_modal_fragment.xml) |
| SHA-256 دیکد | `a6bcd327b67a64085f4fb82d5e2c52752a02b10482750c331ba30419b7c466bd` |
| ریشه | `FrameLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 1 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/layout_base_modal
   └─ include  #@id/base_modal_card
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `FrameLayout` | `android:id` | `@id/layout_base_modal` |
| 3 | `FrameLayout` | `android:background` | `@color/transparent` |
| 4 | `FrameLayout` | `android:clipChildren` | `false` |
| 5 | `FrameLayout` | `android:clipToPadding` | `false` |
| 6 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 7 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 8 | `include` | `android:id` | `@id/base_modal_card` |
| 9 | `include` | `layout` | `@layout/base_modal_card` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/transparent` | `#00000000` |

## ۴. شناسه‌های `@id`

```text
@id/base_modal_card
@id/layout_base_modal
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/base_modal_card
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000011" android:id="@id/layout_base_modal" android:background="@color/transparent" android:clipChildren="false" android:clipToPadding="false" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <include android:id="@id/base_modal_card" layout="@layout/base_modal_card"/>
</FrameLayout>
```
