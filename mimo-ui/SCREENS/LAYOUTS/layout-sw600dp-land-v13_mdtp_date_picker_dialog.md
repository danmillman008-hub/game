# پروندهٔ لایه — `res/layout-sw600dp-land-v13/mdtp_date_picker_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-sw600dp-land-v13/mdtp_date_picker_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-sw600dp-land-v13/mdtp_date_picker_dialog.xml`](../../SOURCE/res/layout-sw600dp-land-v13/mdtp_date_picker_dialog.xml) |
| SHA-256 دیکد | `befcb5e9c9d32a3b3f527239771b3aede1a03a315ea2c68de28e30425d016fef` |
| ریشه | `LinearLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ LinearLayout
   │  ├─ LinearLayout
   │  │  ├─ include
   │  │  └─ include
   │  └─ include
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:background` | `@color/mdtp_background_color` |
| 3 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 6 | `LinearLayout` | `android:orientation` | `horizontal` |
| 7 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 8 | `LinearLayout` | `android:layout_height` | `@dimen/mdtp_date_picker_view_animator_height` |
| 9 | `LinearLayout` | `android:layout_gravity` | `0x00000011` |
| 10 | `LinearLayout` | `android:orientation` | `vertical` |
| 11 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 12 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 13 | `include` | `layout` | `@layout/mdtp_date_picker_header_view` |
| 14 | `include` | `layout` | `@layout/mdtp_date_picker_selected_date` |
| 15 | `include` | `layout` | `@layout/mdtp_date_picker_view_animator` |
| 16 | `include` | `layout` | `@layout/mdtp_done_button` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/mdtp_background_color` | `@color/mdtp_white` |
| `@dimen/mdtp_date_picker_view_animator_height` | `252.000000dip` / `220.000000dip` (land) / `400.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
(none)
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/mdtp_date_picker_header_view
@layout/mdtp_date_picker_selected_date
@layout/mdtp_date_picker_view_animator
@layout/mdtp_done_button
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:background="@color/mdtp_background_color" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <LinearLayout android:gravity="0x00000011" android:orientation="horizontal" android:layout_width="match_parent" android:layout_height="@dimen/mdtp_date_picker_view_animator_height">
    <LinearLayout android:layout_gravity="0x00000011" android:orientation="vertical" android:layout_width="wrap_content" android:layout_height="match_parent">
      <include layout="@layout/mdtp_date_picker_header_view"/>
      <include layout="@layout/mdtp_date_picker_selected_date"/>
    </LinearLayout>
    <include layout="@layout/mdtp_date_picker_view_animator"/>
  </LinearLayout>
  <include layout="@layout/mdtp_done_button"/>
</LinearLayout>
```
