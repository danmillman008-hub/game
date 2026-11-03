# پروندهٔ لایه — `res/layout-watch-v20/abc_alert_dialog_title_material.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-watch-v20/abc_alert_dialog_title_material.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-watch-v20/abc_alert_dialog_title_material.xml`](../../SOURCE/res/layout-watch-v20/abc_alert_dialog_title_material.xml) |
| SHA-256 دیکد | `87a4aa1d19acafcd6c3dd0ec59836f210a8beb0fb6345a94a869280654719723` |
| ریشه | `LinearLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/topPanel
   ├─ LinearLayout  #@id/title_template
   │  ├─ ImageView  #@0x01020006
   │  └─ androidx.appcompat.widget.DialogTitle  #@id/alertTitle
   └─ android.widget.Space  #@id/titleDividerNoCustom
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000031` |
| 2 | `LinearLayout` | `android:orientation` | `vertical` |
| 3 | `LinearLayout` | `android:id` | `@id/topPanel` |
| 4 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 5 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 6 | `LinearLayout` | `android:gravity` | `0x00000001` |
| 7 | `LinearLayout` | `android:orientation` | `vertical` |
| 8 | `LinearLayout` | `android:id` | `@id/title_template` |
| 9 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 10 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 11 | `LinearLayout` | `android:layout_marginTop` | `24.000000dip` |
| 12 | `ImageView` | `android:layout_gravity` | `0x00000001` |
| 13 | `ImageView` | `android:id` | `@0x01020006` |
| 14 | `ImageView` | `android:layout_width` | `wrap_content` |
| 15 | `ImageView` | `android:layout_height` | `wrap_content` |
| 16 | `ImageView` | `android:adjustViewBounds` | `true` |
| 17 | `ImageView` | `android:maxWidth` | `24.000000dip` |
| 18 | `ImageView` | `android:maxHeight` | `24.000000dip` |
| 19 | `androidx.appcompat.widget.DialogTitle` | `android:gravity` | `0x00000011` |
| 20 | `androidx.appcompat.widget.DialogTitle` | `android:id` | `@id/alertTitle` |
| 21 | `androidx.appcompat.widget.DialogTitle` | `android:layout_width` | `match_parent` |
| 22 | `androidx.appcompat.widget.DialogTitle` | `android:layout_height` | `wrap_content` |
| 23 | `androidx.appcompat.widget.DialogTitle` | `style` | `?0x0101005B` |
| 24 | `android.widget.Space` | `android:id` | `@id/titleDividerNoCustom` |
| 25 | `android.widget.Space` | `android:visibility` | `gone` |
| 26 | `android.widget.Space` | `android:layout_width` | `match_parent` |
| 27 | `android.widget.Space` | `android:layout_height` | `@dimen/abc_dialog_title_divider_material` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/abc_dialog_title_divider_material` | `8.000000dip` |

## ۴. شناسه‌های `@id`

```text
@0x01020006
@id/alertTitle
@id/titleDividerNoCustom
@id/title_template
@id/topPanel
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/abc_alert_dialog_material.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000031" android:orientation="vertical" android:id="@id/topPanel" android:layout_width="match_parent" android:layout_height="wrap_content">
  <LinearLayout android:gravity="0x00000001" android:orientation="vertical" android:id="@id/title_template" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="24.000000dip">
    <ImageView android:layout_gravity="0x00000001" android:id="@0x01020006" android:layout_width="wrap_content" android:layout_height="wrap_content" android:adjustViewBounds="true" android:maxWidth="24.000000dip" android:maxHeight="24.000000dip"/>
    <androidx.appcompat.widget.DialogTitle android:gravity="0x00000011" android:id="@id/alertTitle" android:layout_width="match_parent" android:layout_height="wrap_content" style="?0x0101005B"/>
  </LinearLayout>
  <android.widget.Space android:id="@id/titleDividerNoCustom" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/abc_dialog_title_divider_material"/>
</LinearLayout>
```
