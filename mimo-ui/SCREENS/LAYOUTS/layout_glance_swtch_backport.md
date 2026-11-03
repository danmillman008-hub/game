# پروندهٔ لایه — `res/layout/glance_swtch_backport.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/glance_swtch_backport.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/glance_swtch_backport.xml`](../../SOURCE/res/layout/glance_swtch_backport.xml) |
| SHA-256 دیکد | `b89bb6bbb8e7954b1453880e76da7625216368ed2d44afd7480d258a9322c0d5` |
| ریشه | `LinearLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 8 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ ViewStub  #@id/switchText
   └─ FrameLayout
      ├─ ViewStub  #@id/switchTrack
      └─ ViewStub  #@id/switchThumb
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 2 | `LinearLayout` | `android:orientation` | `horizontal` |
| 3 | `LinearLayout` | `android:tag` | `glanceCompoundButton` |
| 4 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 5 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 6 | `LinearLayout` | `app:glance_isTopLevelLayout` | `true` |
| 7 | `LinearLayout` | `style` | `@style/Glance.AppWidget.SwitchBackport` |
| 8 | `ViewStub` | `android:id` | `@id/switchText` |
| 9 | `ViewStub` | `android:layout` | `@layout/glance_switch_text` |
| 10 | `ViewStub` | `android:layout_width` | `0.000000dip` |
| 11 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 12 | `ViewStub` | `android:layout_weight` | `1.000000` |
| 13 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 14 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 15 | `FrameLayout` | `style` | `@style/Glance.AppWidget.SwitchBackport` |
| 16 | `ViewStub` | `android:id` | `@id/switchTrack` |
| 17 | `ViewStub` | `android:layout` | `@layout/glance_switch_track` |
| 18 | `ViewStub` | `android:layout_width` | `42.000000dip` |
| 19 | `ViewStub` | `android:layout_height` | `28.000000dip` |
| 20 | `ViewStub` | `android:id` | `@id/switchThumb` |
| 21 | `ViewStub` | `android:layout` | `@layout/glance_switch_thumb` |
| 22 | `ViewStub` | `android:layout_width` | `42.000000dip` |
| 23 | `ViewStub` | `android:layout_height` | `28.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.SwitchBackport` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/switchText
@id/switchThumb
@id/switchTrack
```

## ۵. ارجاع به لایه‌های دیگر

```text
0.000000dip
1.000000
28.000000dip
42.000000dip
@layout/glance_switch_text
@layout/glance_switch_thumb
@layout/glance_switch_track
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:gravity="0x00000011" android:orientation="horizontal" android:tag="glanceCompoundButton" android:layout_width="wrap_content" android:layout_height="wrap_content" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.SwitchBackport">
  <ViewStub android:id="@id/switchText" android:layout="@layout/glance_switch_text" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000"/>
  <FrameLayout android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/Glance.AppWidget.SwitchBackport">
    <ViewStub android:id="@id/switchTrack" android:layout="@layout/glance_switch_track" android:layout_width="42.000000dip" android:layout_height="28.000000dip"/>
    <ViewStub android:id="@id/switchThumb" android:layout="@layout/glance_switch_thumb" android:layout_width="42.000000dip" android:layout_height="28.000000dip"/>
  </FrameLayout>
</LinearLayout>
```
