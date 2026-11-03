# پروندهٔ لایه — `res/layout/browser_actions_context_menu_row.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/browser_actions_context_menu_row.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/browser_actions_context_menu_row.xml`](../../SOURCE/res/layout/browser_actions_context_menu_row.xml) |
| SHA-256 دیکد | `195328b2808a0f60c58dd658336b6cad3d5e2a441395446d1293e39a63250f6d` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ TextView  #@id/browser_actions_menu_item_text
   └─ ImageView  #@id/browser_actions_menu_item_icon
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `LinearLayout` | `android:minHeight` | `48.000000dip` |
| 5 | `LinearLayout` | `android:paddingStart` | `15.000000dip` |
| 6 | `LinearLayout` | `android:paddingEnd` | `15.000000dip` |
| 7 | `TextView` | `android:textSize` | `15.000000sp` |
| 8 | `TextView` | `android:textColor` | `@color/browser_actions_text_color` |
| 9 | `TextView` | `android:layout_gravity` | `0x00000010` |
| 10 | `TextView` | `android:id` | `@id/browser_actions_menu_item_text` |
| 11 | `TextView` | `android:layout_width` | `0.000000dip` |
| 12 | `TextView` | `android:layout_height` | `wrap_content` |
| 13 | `TextView` | `android:layout_marginLeft` | `10.000000dip` |
| 14 | `TextView` | `android:layout_weight` | `1.000000` |
| 15 | `TextView` | `android:layout_marginStart` | `10.000000dip` |
| 16 | `ImageView` | `android:id` | `@id/browser_actions_menu_item_icon` |
| 17 | `ImageView` | `android:paddingTop` | `8.000000dip` |
| 18 | `ImageView` | `android:paddingBottom` | `8.000000dip` |
| 19 | `ImageView` | `android:layout_width` | `20.000000dip` |
| 20 | `ImageView` | `android:layout_height` | `match_parent` |
| 21 | `ImageView` | `android:scaleType` | `centerInside` |
| 22 | `ImageView` | `android:contentDescription` | `@null` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/browser_actions_text_color` | `#DE000000` |

## ۴. شناسه‌های `@id`

```text
@id/browser_actions_menu_item_icon
@id/browser_actions_menu_item_text
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="48.000000dip" android:paddingStart="15.000000dip" android:paddingEnd="15.000000dip">
  <TextView android:textSize="15.000000sp" android:textColor="@color/browser_actions_text_color" android:layout_gravity="0x00000010" android:id="@id/browser_actions_menu_item_text" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginLeft="10.000000dip" android:layout_weight="1.000000" android:layout_marginStart="10.000000dip"/>
  <ImageView android:id="@id/browser_actions_menu_item_icon" android:paddingTop="8.000000dip" android:paddingBottom="8.000000dip" android:layout_width="20.000000dip" android:layout_height="match_parent" android:scaleType="centerInside" android:contentDescription="@null"/>
</LinearLayout>
```
