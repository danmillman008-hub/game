# پروندهٔ لایه — `res/layout/mtrl_picker_header_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_picker_header_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_picker_header_dialog.xml`](../../SOURCE/res/layout/mtrl_picker_header_dialog.xml) |
| SHA-256 دیکد | `b706ca14b417bdeb7b54f87ecee4de4f01f7e02b45fde979d70b2b22e2297612` |
| ریشه | `merge` |
| تعداد گره | 7 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 5 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ LinearLayout  #@id/mtrl_picker_header
   │  ├─ FrameLayout  #@id/mtrl_picker_header_title_and_selection
   │  │  ├─ include
   │  │  └─ include
   │  └─ include
   └─ View
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `merge` | `android:layout_width` | `match_parent` |
| 2 | `merge` | `android:layout_height` | `wrap_content` |
| 3 | `LinearLayout` | `android:layout_gravity` | `0x00000030` |
| 4 | `LinearLayout` | `android:orientation` | `horizontal` |
| 5 | `LinearLayout` | `android:id` | `@id/mtrl_picker_header` |
| 6 | `LinearLayout` | `android:paddingLeft` | `@dimen/mtrl_calendar_header_content_padding` |
| 7 | `LinearLayout` | `android:paddingRight` | `@dimen/mtrl_calendar_header_content_padding` |
| 8 | `LinearLayout` | `android:baselineAligned` | `false` |
| 9 | `LinearLayout` | `android:paddingStart` | `@dimen/mtrl_calendar_header_content_padding` |
| 10 | `LinearLayout` | `android:paddingEnd` | `@dimen/mtrl_calendar_header_content_padding` |
| 11 | `LinearLayout` | `style` | `?attr/materialCalendarHeaderLayout` |
| 12 | `FrameLayout` | `android:id` | `@id/mtrl_picker_header_title_and_selection` |
| 13 | `FrameLayout` | `android:paddingLeft` | `@dimen/mtrl_calendar_header_text_padding` |
| 14 | `FrameLayout` | `android:focusable` | `false` |
| 15 | `FrameLayout` | `android:focusableInTouchMode` | `false` |
| 16 | `FrameLayout` | `android:layout_width` | `0.000000dip` |
| 17 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 18 | `FrameLayout` | `android:layout_weight` | `1.000000` |
| 19 | `FrameLayout` | `android:importantForAccessibility` | `yes` |
| 20 | `FrameLayout` | `android:paddingStart` | `@dimen/mtrl_calendar_header_text_padding` |
| 21 | `include` | `layout` | `@layout/mtrl_picker_header_title_text` |
| 22 | `include` | `layout` | `@layout/mtrl_picker_header_selection_text` |
| 23 | `include` | `layout` | `@layout/mtrl_picker_header_toggle` |
| 24 | `View` | `android:layout_gravity` | `0x00000050` |
| 25 | `View` | `android:layout_width` | `match_parent` |
| 26 | `View` | `android:layout_height` | `@dimen/mtrl_calendar_header_divider_thickness` |
| 27 | `View` | `style` | `?attr/materialCalendarHeaderDivider` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_header_content_padding` | `12.000000dip` / `4.000000dip` (land) |
| `@dimen/mtrl_calendar_header_divider_thickness` | `1.000000dip` |
| `@dimen/mtrl_calendar_header_text_padding` | `12.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/mtrl_picker_header
@id/mtrl_picker_header_title_and_selection
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/mtrl_picker_header_selection_text
@layout/mtrl_picker_header_title_text
@layout/mtrl_picker_header_toggle
match_parent
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/mtrl_picker_dialog.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="wrap_content">
  <LinearLayout android:layout_gravity="0x00000030" android:orientation="horizontal" android:id="@id/mtrl_picker_header" android:paddingLeft="@dimen/mtrl_calendar_header_content_padding" android:paddingRight="@dimen/mtrl_calendar_header_content_padding" android:baselineAligned="false" android:paddingStart="@dimen/mtrl_calendar_header_content_padding" android:paddingEnd="@dimen/mtrl_calendar_header_content_padding" style="?attr/materialCalendarHeaderLayout">
    <FrameLayout android:id="@id/mtrl_picker_header_title_and_selection" android:paddingLeft="@dimen/mtrl_calendar_header_text_padding" android:focusable="false" android:focusableInTouchMode="false" android:layout_width="0.000000dip" android:layout_height="match_parent" android:layout_weight="1.000000" android:importantForAccessibility="yes" android:paddingStart="@dimen/mtrl_calendar_header_text_padding">
      <include layout="@layout/mtrl_picker_header_title_text"/>
      <include layout="@layout/mtrl_picker_header_selection_text"/>
    </FrameLayout>
    <include layout="@layout/mtrl_picker_header_toggle"/>
  </LinearLayout>
  <View android:layout_gravity="0x00000050" android:layout_width="match_parent" android:layout_height="@dimen/mtrl_calendar_header_divider_thickness" style="?attr/materialCalendarHeaderDivider"/>
</merge>
```
