# پروندهٔ لایه — `res/layout/mtrl_picker_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_picker_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_picker_dialog.xml`](../../SOURCE/res/layout/mtrl_picker_dialog.xml) |
| SHA-256 دیکد | `5dc0bea52ce3286c9dbe838a60b45c9e44d071cb2955fc02c5cf676f514ae7f3` |
| ریشه | `LinearLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ include
   └─ LinearLayout  #@id/mtrl_calendar_main_pane
      ├─ androidx.fragment.app.FragmentContainerView  #@id/mtrl_calendar_frame
      └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `@integer/mtrl_calendar_header_orientation` |
| 2 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 3 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 4 | `include` | `layout` | `@layout/mtrl_picker_header_dialog` |
| 5 | `LinearLayout` | `android:orientation` | `vertical` |
| 6 | `LinearLayout` | `android:id` | `@id/mtrl_calendar_main_pane` |
| 7 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 8 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 9 | `androidx.fragment.app.FragmentContainerView` | `android:id` | `@id/mtrl_calendar_frame` |
| 10 | `androidx.fragment.app.FragmentContainerView` | `android:paddingLeft` | `@dimen/mtrl_calendar_content_padding` |
| 11 | `androidx.fragment.app.FragmentContainerView` | `android:paddingRight` | `@dimen/mtrl_calendar_content_padding` |
| 12 | `androidx.fragment.app.FragmentContainerView` | `android:paddingBottom` | `@dimen/mtrl_calendar_bottom_padding` |
| 13 | `androidx.fragment.app.FragmentContainerView` | `android:layout_width` | `match_parent` |
| 14 | `androidx.fragment.app.FragmentContainerView` | `android:layout_height` | `0.000000dip` |
| 15 | `androidx.fragment.app.FragmentContainerView` | `android:layout_weight` | `1.000000` |
| 16 | `androidx.fragment.app.FragmentContainerView` | `android:paddingStart` | `@dimen/mtrl_calendar_content_padding` |
| 17 | `androidx.fragment.app.FragmentContainerView` | `android:paddingEnd` | `@dimen/mtrl_calendar_content_padding` |
| 18 | `include` | `android:layout_width` | `match_parent` |
| 19 | `include` | `android:layout_height` | `@dimen/mtrl_calendar_action_height` |
| 20 | `include` | `layout` | `@layout/mtrl_picker_actions` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_action_height` | `52.000000dip` |
| `@dimen/mtrl_calendar_bottom_padding` | `0.000000dip` / `4.000000dip` (h360dp-land) / `0.000000dip` (h480dp-land) / `4.000000dip` (w360dp-port) / `0.000000dip` (w400dp-port) |
| `@dimen/mtrl_calendar_content_padding` | `12.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/mtrl_calendar_frame
@id/mtrl_calendar_main_pane
```

## ۵. ارجاع به لایه‌های دیگر

```text
@dimen/mtrl_calendar_action_height
@layout/mtrl_picker_actions
@layout/mtrl_picker_header_dialog
match_parent
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="@integer/mtrl_calendar_header_orientation" android:layout_width="wrap_content" android:layout_height="match_parent">
  <include layout="@layout/mtrl_picker_header_dialog"/>
  <LinearLayout android:orientation="vertical" android:id="@id/mtrl_calendar_main_pane" android:layout_width="wrap_content" android:layout_height="match_parent">
    <androidx.fragment.app.FragmentContainerView android:id="@id/mtrl_calendar_frame" android:paddingLeft="@dimen/mtrl_calendar_content_padding" android:paddingRight="@dimen/mtrl_calendar_content_padding" android:paddingBottom="@dimen/mtrl_calendar_bottom_padding" android:layout_width="match_parent" android:layout_height="0.000000dip" android:layout_weight="1.000000" android:paddingStart="@dimen/mtrl_calendar_content_padding" android:paddingEnd="@dimen/mtrl_calendar_content_padding"/>
    <include android:layout_width="match_parent" android:layout_height="@dimen/mtrl_calendar_action_height" layout="@layout/mtrl_picker_actions"/>
  </LinearLayout>
</LinearLayout>
```
