# پروندهٔ لایه — `res/layout/abc_action_bar_title_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_action_bar_title_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_action_bar_title_item.xml`](../../SOURCE/res/layout/abc_action_bar_title_item.xml) |
| SHA-256 دیکد | `dfb5faf75f0a9aae1e093b44d3a8f9018d026e68429277361356789de855a240` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ TextView  #@id/action_bar_title
   └─ TextView  #@id/action_bar_subtitle
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `LinearLayout` | `style` | `@style/RtlOverlay.Widget.AppCompat.ActionBar.TitleItem` |
| 5 | `TextView` | `android:ellipsize` | `end` |
| 6 | `TextView` | `android:id` | `@id/action_bar_title` |
| 7 | `TextView` | `android:layout_width` | `wrap_content` |
| 8 | `TextView` | `android:layout_height` | `wrap_content` |
| 9 | `TextView` | `android:singleLine` | `true` |
| 10 | `TextView` | `android:ellipsize` | `end` |
| 11 | `TextView` | `android:id` | `@id/action_bar_subtitle` |
| 12 | `TextView` | `android:visibility` | `gone` |
| 13 | `TextView` | `android:layout_width` | `wrap_content` |
| 14 | `TextView` | `android:layout_height` | `wrap_content` |
| 15 | `TextView` | `android:layout_marginTop` | `@dimen/abc_action_bar_subtitle_top_margin_material` |
| 16 | `TextView` | `android:singleLine` | `true` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/abc_action_bar_subtitle_top_margin_material` | `16777213.000000dip` |
| `@style/RtlOverlay.Widget.AppCompat.ActionBar.TitleItem` | `[{'attr': 'android:layout_gravity', 'attr_id': '0x010100B3', 'value': '0x00800013', 'value_type': 'int_hex'}, {'attr': 'android:paddingEnd', 'attr_id': '0x010103B4', 'value': '8.000000dip', 'value_type': 'dimension'}]` |

## ۴. شناسه‌های `@id`

```text
@id/action_bar_subtitle
@id/action_bar_title
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/RtlOverlay.Widget.AppCompat.ActionBar.TitleItem">
  <TextView android:ellipsize="end" android:id="@id/action_bar_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true"/>
  <TextView android:ellipsize="end" android:id="@id/action_bar_subtitle" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/abc_action_bar_subtitle_top_margin_material" android:singleLine="true"/>
</LinearLayout>
```
