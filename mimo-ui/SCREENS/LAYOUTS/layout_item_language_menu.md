# پروندهٔ لایه — `res/layout/item_language_menu.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/item_language_menu.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/item_language_menu.xml`](../../SOURCE/res/layout/item_language_menu.xml) |
| SHA-256 دیکد | `7a80ce2a63cc045eb8ed54d7d5a3af35b3b499472496eea2732be471cf49b55e` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ TextView  #@id/tv_language_name
   └─ ImageView  #@id/iv_download_icon
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000010` |
| 2 | `LinearLayout` | `android:orientation` | `horizontal` |
| 3 | `LinearLayout` | `android:background` | `?attr/selectableItemBackground` |
| 4 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 5 | `LinearLayout` | `android:layout_height` | `48.000000dip` |
| 6 | `LinearLayout` | `android:paddingHorizontal` | `@dimen/general_margin_16dp` |
| 7 | `TextView` | `android:textColor` | `@color/text_primary` |
| 8 | `TextView` | `android:id` | `@id/tv_language_name` |
| 9 | `TextView` | `android:layout_width` | `0.000000dip` |
| 10 | `TextView` | `android:layout_height` | `wrap_content` |
| 11 | `TextView` | `android:layout_weight` | `1.000000` |
| 12 | `TextView` | `android:layout_marginEnd` | `24.000000dip` |
| 13 | `TextView` | `style` | `@style/TextP1` |
| 14 | `ImageView` | `android:id` | `@id/iv_download_icon` |
| 15 | `ImageView` | `android:visibility` | `gone` |
| 16 | `ImageView` | `android:layout_width` | `24.000000dip` |
| 17 | `ImageView` | `android:layout_height` | `24.000000dip` |
| 18 | `ImageView` | `android:src` | `@drawable/ic_download` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/general_margin_16dp` | `16.000000dip` / `20.000000dip` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_download_icon
@id/tv_language_name
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000010" android:orientation="horizontal" android:background="?attr/selectableItemBackground" android:layout_width="match_parent" android:layout_height="48.000000dip" android:paddingHorizontal="@dimen/general_margin_16dp">
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_language_name" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000" android:layout_marginEnd="24.000000dip" style="@style/TextP1"/>
  <ImageView android:id="@id/iv_download_icon" android:visibility="gone" android:layout_width="24.000000dip" android:layout_height="24.000000dip" android:src="@drawable/ic_download"/>
</LinearLayout>
```
