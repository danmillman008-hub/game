# پروندهٔ لایه — `res/layout/mdtp_date_picker_dialog_v2.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mdtp_date_picker_dialog_v2.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mdtp_date_picker_dialog_v2.xml`](../../SOURCE/res/layout/mdtp_date_picker_dialog_v2.xml) |
| SHA-256 دیکد | `8601232957c5a21b08078e5ecb6fe06e102db67359fb3d69d551aa0a990024dd` |
| ریشه | `LinearLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 5 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ LinearLayout
   │  ├─ include
   │  ├─ include
   │  └─ include
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 2 | `LinearLayout` | `android:orientation` | `vertical` |
| 3 | `LinearLayout` | `android:background` | `@color/mdtp_date_picker_view_animator` |
| 4 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 5 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 6 | `LinearLayout` | `android:orientation` | `vertical` |
| 7 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 8 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 9 | `include` | `layout` | `@layout/mdtp_date_picker_header_view_v2` |
| 10 | `include` | `layout` | `@layout/mdtp_date_picker_selected_date_v2` |
| 11 | `include` | `layout` | `@layout/mdtp_date_picker_view_animator_v2` |
| 12 | `include` | `layout` | `@layout/mdtp_done_button` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/mdtp_date_picker_view_animator` | `@android:0106000B` |

## ۴. شناسه‌های `@id`

```text
(none)
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/mdtp_date_picker_header_view_v2
@layout/mdtp_date_picker_selected_date_v2
@layout/mdtp_date_picker_view_animator_v2
@layout/mdtp_done_button
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000011" android:orientation="vertical" android:background="@color/mdtp_date_picker_view_animator" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <LinearLayout android:orientation="vertical" android:layout_width="wrap_content" android:layout_height="wrap_content">
    <include layout="@layout/mdtp_date_picker_header_view_v2"/>
    <include layout="@layout/mdtp_date_picker_selected_date_v2"/>
    <include layout="@layout/mdtp_date_picker_view_animator_v2"/>
  </LinearLayout>
  <include layout="@layout/mdtp_done_button"/>
</LinearLayout>
```
