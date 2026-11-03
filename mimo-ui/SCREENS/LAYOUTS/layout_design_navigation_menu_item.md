# پروندهٔ لایه — `res/layout/design_navigation_menu_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/design_navigation_menu_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/design_navigation_menu_item.xml`](../../SOURCE/res/layout/design_navigation_menu_item.xml) |
| SHA-256 دیکد | `72a49e9fb64ff6a43f8fcc96bd94ed63aeaacb81928598a8121fb5d933ed8bd5` |
| ریشه | `merge` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ CheckedTextView  #@id/design_menu_item_text
   └─ ViewStub  #@id/design_menu_item_action_area_stub
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `CheckedTextView` | `android:textAppearance` | `@style/TextAppearance.AppCompat.Body2` |
| 2 | `CheckedTextView` | `android:gravity` | `0x00800013` |
| 3 | `CheckedTextView` | `android:id` | `@id/design_menu_item_text` |
| 4 | `CheckedTextView` | `android:duplicateParentState` | `true` |
| 5 | `CheckedTextView` | `android:layout_width` | `0.000000dip` |
| 6 | `CheckedTextView` | `android:layout_height` | `match_parent` |
| 7 | `CheckedTextView` | `android:maxLines` | `1` |
| 8 | `CheckedTextView` | `android:drawablePadding` | `@dimen/design_navigation_icon_padding` |
| 9 | `CheckedTextView` | `android:layout_weight` | `1.000000` |
| 10 | `ViewStub` | `android:id` | `@id/design_menu_item_action_area_stub` |
| 11 | `ViewStub` | `android:layout` | `@layout/design_menu_item_action_area` |
| 12 | `ViewStub` | `android:inflatedId` | `@id/design_menu_item_action_area` |
| 13 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 14 | `ViewStub` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/design_navigation_icon_padding` | `32.000000dip` |
| `@style/TextAppearance.AppCompat.Body2` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/design_menu_item_action_area_stub
@id/design_menu_item_text
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/design_menu_item_action_area
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android">
  <CheckedTextView android:textAppearance="@style/TextAppearance.AppCompat.Body2" android:gravity="0x00800013" android:id="@id/design_menu_item_text" android:duplicateParentState="true" android:layout_width="0.000000dip" android:layout_height="match_parent" android:maxLines="1" android:drawablePadding="@dimen/design_navigation_icon_padding" android:layout_weight="1.000000"/>
  <ViewStub android:id="@id/design_menu_item_action_area_stub" android:layout="@layout/design_menu_item_action_area" android:inflatedId="@id/design_menu_item_action_area" android:layout_width="wrap_content" android:layout_height="match_parent"/>
</merge>
```
