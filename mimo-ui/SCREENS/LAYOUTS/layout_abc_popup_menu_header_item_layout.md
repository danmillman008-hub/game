# پروندهٔ لایه — `res/layout/abc_popup_menu_header_item_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_popup_menu_header_item_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_popup_menu_header_item_layout.xml`](../../SOURCE/res/layout/abc_popup_menu_header_item_layout.xml) |
| SHA-256 دیکد | `71d2e945a901b4a73d2ef2e2f3ec6e4079a8623f08b16ca17aa0740edc9351e5` |
| ریشه | `FrameLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   └─ TextView  #@0x01020016
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:paddingLeft` | `16.000000dip` |
| 2 | `FrameLayout` | `android:paddingRight` | `16.000000dip` |
| 3 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 4 | `FrameLayout` | `android:layout_height` | `?attr/dropdownListPreferredItemHeight` |
| 5 | `FrameLayout` | `android:minWidth` | `196.000000dip` |
| 6 | `TextView` | `android:textAppearance` | `?attr/textAppearancePopupMenuHeader` |
| 7 | `TextView` | `android:ellipsize` | `marquee` |
| 8 | `TextView` | `android:layout_gravity` | `0x00000010` |
| 9 | `TextView` | `android:id` | `@0x01020016` |
| 10 | `TextView` | `android:fadingEdge` | `0x00001000` |
| 11 | `TextView` | `android:layout_width` | `match_parent` |
| 12 | `TextView` | `android:layout_height` | `wrap_content` |
| 13 | `TextView` | `android:singleLine` | `true` |
| 14 | `TextView` | `android:textAlignment` | `viewStart` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@0x01020016
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
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:paddingLeft="16.000000dip" android:paddingRight="16.000000dip" android:layout_width="match_parent" android:layout_height="?attr/dropdownListPreferredItemHeight" android:minWidth="196.000000dip">
  <TextView android:textAppearance="?attr/textAppearancePopupMenuHeader" android:ellipsize="marquee" android:layout_gravity="0x00000010" android:id="@0x01020016" android:fadingEdge="0x00001000" android:layout_width="match_parent" android:layout_height="wrap_content" android:singleLine="true" android:textAlignment="viewStart"/>
</FrameLayout>
```
