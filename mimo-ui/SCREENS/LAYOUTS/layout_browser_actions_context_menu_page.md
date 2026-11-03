# پروندهٔ لایه — `res/layout/browser_actions_context_menu_page.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/browser_actions_context_menu_page.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/browser_actions_context_menu_page.xml`](../../SOURCE/res/layout/browser_actions_context_menu_page.xml) |
| SHA-256 دیکد | `124f5af226fd7d74cefddf74c8f60b06dd9f7712e2cdf2aaee9b7173dccb7e43` |
| ریشه | `androidx.browser.browseractions.BrowserActionsFallbackMenuView` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.browser.browseractions.BrowserActionsFallbackMenuView  #@id/browser_actions_menu_view
   ├─ TextView  #@id/browser_actions_header_text
   ├─ View
   └─ ListView  #@id/browser_actions_menu_items
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.browser.browseractions.BrowserActionsFallbackMenuView` | `android:layout_gravity` | `0x00000011` |
| 2 | `androidx.browser.browseractions.BrowserActionsFallbackMenuView` | `android:orientation` | `vertical` |
| 3 | `androidx.browser.browseractions.BrowserActionsFallbackMenuView` | `android:id` | `@id/browser_actions_menu_view` |
| 4 | `androidx.browser.browseractions.BrowserActionsFallbackMenuView` | `android:background` | `@color/browser_actions_bg_grey` |
| 5 | `androidx.browser.browseractions.BrowserActionsFallbackMenuView` | `android:layout_width` | `wrap_content` |
| 6 | `androidx.browser.browseractions.BrowserActionsFallbackMenuView` | `android:layout_height` | `wrap_content` |
| 7 | `androidx.browser.browseractions.BrowserActionsFallbackMenuView` | `android:minWidth` | `280.000000dip` |
| 8 | `TextView` | `android:textSize` | `13.000000sp` |
| 9 | `TextView` | `android:textStyle` | `0x00000001` |
| 10 | `TextView` | `android:textColor` | `@color/browser_actions_title_color` |
| 11 | `TextView` | `android:ellipsize` | `end` |
| 12 | `TextView` | `android:gravity` | `0x00000011` |
| 13 | `TextView` | `android:id` | `@id/browser_actions_header_text` |
| 14 | `TextView` | `android:layout_width` | `match_parent` |
| 15 | `TextView` | `android:layout_height` | `wrap_content` |
| 16 | `TextView` | `android:layout_marginTop` | `10.000000dip` |
| 17 | `TextView` | `android:layout_marginBottom` | `10.000000dip` |
| 18 | `TextView` | `android:maxLines` | `1` |
| 19 | `TextView` | `android:paddingStart` | `20.000000dip` |
| 20 | `TextView` | `android:paddingEnd` | `20.000000dip` |
| 21 | `View` | `android:background` | `@color/browser_actions_divider_color` |
| 22 | `View` | `android:layout_width` | `match_parent` |
| 23 | `View` | `android:layout_height` | `1.000000dip` |
| 24 | `ListView` | `android:id` | `@id/browser_actions_menu_items` |
| 25 | `ListView` | `android:paddingTop` | `8.000000dip` |
| 26 | `ListView` | `android:paddingBottom` | `8.000000dip` |
| 27 | `ListView` | `android:layout_width` | `match_parent` |
| 28 | `ListView` | `android:layout_height` | `wrap_content` |
| 29 | `ListView` | `android:divider` | `@null` |
| 30 | `ListView` | `android:dividerHeight` | `0.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/browser_actions_bg_grey` | `#FFF5F5F5` |
| `@color/browser_actions_divider_color` | `#1E000000` |
| `@color/browser_actions_title_color` | `#FF646464` |

## ۴. شناسه‌های `@id`

```text
@id/browser_actions_header_text
@id/browser_actions_menu_items
@id/browser_actions_menu_view
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
<androidx.browser.browseractions.BrowserActionsFallbackMenuView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000011" android:orientation="vertical" android:id="@id/browser_actions_menu_view" android:background="@color/browser_actions_bg_grey" android:layout_width="wrap_content" android:layout_height="wrap_content" android:minWidth="280.000000dip">
  <TextView android:textSize="13.000000sp" android:textStyle="0x00000001" android:textColor="@color/browser_actions_title_color" android:ellipsize="end" android:gravity="0x00000011" android:id="@id/browser_actions_header_text" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="10.000000dip" android:layout_marginBottom="10.000000dip" android:maxLines="1" android:paddingStart="20.000000dip" android:paddingEnd="20.000000dip"/>
  <View android:background="@color/browser_actions_divider_color" android:layout_width="match_parent" android:layout_height="1.000000dip"/>
  <ListView android:id="@id/browser_actions_menu_items" android:paddingTop="8.000000dip" android:paddingBottom="8.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content" android:divider="@null" android:dividerHeight="0.000000dip"/>
</androidx.browser.browseractions.BrowserActionsFallbackMenuView>
```
