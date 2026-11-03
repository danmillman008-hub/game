# پروندهٔ لایه — `res/layout-v33/glance_swtch_backport_expandwidth_wrapheight.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v33/glance_swtch_backport_expandwidth_wrapheight.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v33/glance_swtch_backport_expandwidth_wrapheight.xml`](../../SOURCE/res/layout-v33/glance_swtch_backport_expandwidth_wrapheight.xml) |
| SHA-256 دیکد | `d2e5e31c47b3c24f37780cbb4fb2ae29f1feb639e844d5ad0cab0f5850f0e240` |
| ریشه | `LinearLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 8 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/glanceView
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
| 3 | `LinearLayout` | `android:id` | `@id/glanceView` |
| 4 | `LinearLayout` | `android:tag` | `glanceCompoundButton` |
| 5 | `LinearLayout` | `android:layout_width` | `0.000000dip` |
| 6 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 7 | `LinearLayout` | `android:layout_weight` | `1.000000` |
| 8 | `LinearLayout` | `android:layoutDirection` | `locale` |
| 9 | `LinearLayout` | `app:glance_isTopLevelLayout` | `true` |
| 10 | `LinearLayout` | `style` | `@style/Glance.AppWidget.SwitchBackport` |
| 11 | `ViewStub` | `android:id` | `@id/switchText` |
| 12 | `ViewStub` | `android:layout` | `@layout/glance_switch_text` |
| 13 | `ViewStub` | `android:layout_width` | `0.000000dip` |
| 14 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 15 | `ViewStub` | `android:layout_weight` | `1.000000` |
| 16 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 17 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 18 | `FrameLayout` | `style` | `@style/Glance.AppWidget.SwitchBackport` |
| 19 | `ViewStub` | `android:id` | `@id/switchTrack` |
| 20 | `ViewStub` | `android:layout` | `@layout/glance_switch_track` |
| 21 | `ViewStub` | `android:layout_width` | `42.000000dip` |
| 22 | `ViewStub` | `android:layout_height` | `28.000000dip` |
| 23 | `ViewStub` | `android:id` | `@id/switchThumb` |
| 24 | `ViewStub` | `android:layout` | `@layout/glance_switch_thumb` |
| 25 | `ViewStub` | `android:layout_width` | `42.000000dip` |
| 26 | `ViewStub` | `android:layout_height` | `28.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/Glance.AppWidget.SwitchBackport` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/glanceView
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:gravity="0x00000011" android:orientation="horizontal" android:id="@id/glanceView" android:tag="glanceCompoundButton" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000" android:layoutDirection="locale" app:glance_isTopLevelLayout="true" style="@style/Glance.AppWidget.SwitchBackport">
  <ViewStub android:id="@id/switchText" android:layout="@layout/glance_switch_text" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000"/>
  <FrameLayout android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/Glance.AppWidget.SwitchBackport">
    <ViewStub android:id="@id/switchTrack" android:layout="@layout/glance_switch_track" android:layout_width="42.000000dip" android:layout_height="28.000000dip"/>
    <ViewStub android:id="@id/switchThumb" android:layout="@layout/glance_switch_thumb" android:layout_width="42.000000dip" android:layout_height="28.000000dip"/>
  </FrameLayout>
</LinearLayout>
```
