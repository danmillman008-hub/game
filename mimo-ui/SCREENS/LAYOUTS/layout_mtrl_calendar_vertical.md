# پروندهٔ لایه — `res/layout/mtrl_calendar_vertical.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_calendar_vertical.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_calendar_vertical.xml`](../../SOURCE/res/layout/mtrl_calendar_vertical.xml) |
| SHA-256 دیکد | `4317844c6089605a8ed63ddc75ef809667ef057e7005b89320972bb73418735f` |
| ریشه | `LinearLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 2 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ include
   ├─ View
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 2 | `LinearLayout` | `android:orientation` | `vertical` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 5 | `include` | `layout` | `@layout/mtrl_calendar_days_of_week` |
| 6 | `View` | `android:background` | `?attr/colorOnSurface` |
| 7 | `View` | `android:layout_width` | `match_parent` |
| 8 | `View` | `android:layout_height` | `1.000000dip` |
| 9 | `include` | `layout` | `@layout/mtrl_calendar_months` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
(none)
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/mtrl_calendar_days_of_week
@layout/mtrl_calendar_months
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000011" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="match_parent">
  <include layout="@layout/mtrl_calendar_days_of_week"/>
  <View android:background="?attr/colorOnSurface" android:layout_width="match_parent" android:layout_height="1.000000dip"/>
  <include layout="@layout/mtrl_calendar_months"/>
</LinearLayout>
```
