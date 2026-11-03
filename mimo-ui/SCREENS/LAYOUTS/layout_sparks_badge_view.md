# پروندهٔ لایه — `res/layout/sparks_badge_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/sparks_badge_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/sparks_badge_view.xml`](../../SOURCE/res/layout/sparks_badge_view.xml) |
| SHA-256 دیکد | `7940c212725f4a1bff9f8b24a5b4899f0be495042d32a42902ee6989d99c5432` |
| ریشه | `LinearLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/root_sparks_badge_view
   ├─ TextView
   ├─ TextView  #@id/tv_sparks_badge_view_amount
   └─ TextView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:id` | `@id/root_sparks_badge_view` |
| 3 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 4 | `LinearLayout` | `android:layout_height` | `24.000000dip` |
| 5 | `TextView` | `android:textColor` | `@color/text_primary` |
| 6 | `TextView` | `android:gravity` | `0x00000011` |
| 7 | `TextView` | `android:layout_width` | `wrap_content` |
| 8 | `TextView` | `android:layout_height` | `match_parent` |
| 9 | `TextView` | `android:text` | `@string/plus` |
| 10 | `TextView` | `android:layout_marginStart` | `8.000000dip` |
| 11 | `TextView` | `android:layout_marginEnd` | `4.000000dip` |
| 12 | `TextView` | `style` | `@style/TextH4` |
| 13 | `TextView` | `android:textColor` | `@color/text_primary` |
| 14 | `TextView` | `android:gravity` | `0x00000011` |
| 15 | `TextView` | `android:id` | `@id/tv_sparks_badge_view_amount` |
| 16 | `TextView` | `android:layout_width` | `wrap_content` |
| 17 | `TextView` | `android:layout_height` | `match_parent` |
| 18 | `TextView` | `android:layout_marginEnd` | `4.000000dip` |
| 19 | `TextView` | `style` | `@style/TextH4` |
| 20 | `TextView` | `android:textColor` | `@color/text_primary` |
| 21 | `TextView` | `android:gravity` | `0x00000011` |
| 22 | `TextView` | `android:layout_width` | `wrap_content` |
| 23 | `TextView` | `android:layout_height` | `match_parent` |
| 24 | `TextView` | `android:text` | `@string/xp` |
| 25 | `TextView` | `android:layout_marginEnd` | `8.000000dip` |
| 26 | `TextView` | `style` | `@style/TextH4` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@string/plus` | `+` / `+` (de) / `+` (es) / `+` (fr) / `+` (in) / `+` (it) / `+` (pl) / `+` (pt-rBR) / `+` (ru) / `+` (tr) |
| `@string/xp` | `XP` / `XP` (de) / `XP` (es) / `XP` (fr) / `XP` (in) / `XP` (it) / `XP` (pl) / `XP` (pt-rBR) / `XP` (ru) / `XP` (tr) |
| `@style/TextH4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '11.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/root_sparks_badge_view
@id/tv_sparks_badge_view_amount
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:id="@id/root_sparks_badge_view" android:layout_width="wrap_content" android:layout_height="24.000000dip">
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:layout_width="wrap_content" android:layout_height="match_parent" android:text="@string/plus" android:layout_marginStart="8.000000dip" android:layout_marginEnd="4.000000dip" style="@style/TextH4"/>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_sparks_badge_view_amount" android:layout_width="wrap_content" android:layout_height="match_parent" android:layout_marginEnd="4.000000dip" style="@style/TextH4"/>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:layout_width="wrap_content" android:layout_height="match_parent" android:text="@string/xp" android:layout_marginEnd="8.000000dip" style="@style/TextH4"/>
</LinearLayout>
```
