# پروندهٔ لایه — `res/layout-v33/glance_radio_button_backport_wrapwidth_expandheight.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v33/glance_radio_button_backport_wrapwidth_expandheight.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v33/glance_radio_button_backport_wrapwidth_expandheight.xml`](../../SOURCE/res/layout-v33/glance_radio_button_backport_wrapwidth_expandheight.xml) |
| SHA-256 دیکد | `dba906af62319b60f03d5730c9ed1d75f42c920f8099e33ee9f11ea60a478835` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 6 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/glanceView
   ├─ ViewStub  #@id/radioIcon
   └─ ViewStub  #@id/radioText
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 2 | `LinearLayout` | `android:orientation` | `horizontal` |
| 3 | `LinearLayout` | `android:id` | `@id/glanceView` |
| 4 | `LinearLayout` | `android:tag` | `glanceCompoundButton` |
| 5 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 6 | `LinearLayout` | `android:layout_height` | `0.000000dip` |
| 7 | `LinearLayout` | `android:layout_weight` | `1.000000` |
| 8 | `LinearLayout` | `android:layoutDirection` | `locale` |
| 9 | `LinearLayout` | `app:glance_isTopLevelLayout` | `true` |
| 10 | `LinearLayout` | `style` | `@style/Glance.AppWidget.RadioButton` |
| 11 | `ViewStub` | `android:id` | `@id/radioIcon` |
| 12 | `ViewStub` | `android:layout` | `@layout/glance_radio_icon` |
| 13 | `ViewStub` | `android:layout_width` | `32.000000dip` |
| 14 | `ViewStub` | `android:layout_height` | `32.000000dip` |
| 15 | `ViewStub` | `android:id` | `@id/radioText` |
| 16 | `ViewStub` | `android:layout` | `@layout/glance_radio_text` |
| 17 | `ViewStub` | `android:layout_width` | `0.000000dip` |
| 18 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 19 | `ViewStub` | `android:layout_weight` | `1.000000` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.RadioButton` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/glanceView
@id/radioIcon
@id/radioText
```

## ۵. ارجاع به لایه‌های دیگر

```text
0.000000dip
1.000000
32.000000dip
@layout/glance_radio_icon
@layout/glance_radio_text
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:gravity="0x00000011" android:orientation="horizontal" android:id="@id/glanceView" android:tag="glanceCompoundButton" android:layout_width="wrap_content" android:layout_height="0.000000dip" android:layout_weight="1.000000" android:layoutDirection="locale" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.RadioButton">
  <ViewStub android:id="@id/radioIcon" android:layout="@layout/glance_radio_icon" android:layout_width="32.000000dip" android:layout_height="32.000000dip"/>
  <ViewStub android:id="@id/radioText" android:layout="@layout/glance_radio_text" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000"/>
</LinearLayout>
```
