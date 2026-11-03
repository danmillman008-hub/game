# پروندهٔ لایه — `res/layout/mtrl_picker_fullscreen.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_picker_fullscreen.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_picker_fullscreen.xml`](../../SOURCE/res/layout/mtrl_picker_fullscreen.xml) |
| SHA-256 دیکد | `515dca095e4abdb08e470f3647b179cc04d42f62a36211fe856c0ff28a048d0d` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 1 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/mtrl_picker_fullscreen
   ├─ include
   └─ androidx.fragment.app.FragmentContainerView  #@id/mtrl_calendar_frame
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:gravity` | `0x00000001` |
| 2 | `LinearLayout` | `android:orientation` | `vertical` |
| 3 | `LinearLayout` | `android:id` | `@id/mtrl_picker_fullscreen` |
| 4 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 5 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 6 | `include` | `layout` | `@layout/mtrl_picker_header_fullscreen` |
| 7 | `androidx.fragment.app.FragmentContainerView` | `android:id` | `@id/mtrl_calendar_frame` |
| 8 | `androidx.fragment.app.FragmentContainerView` | `android:paddingLeft` | `@dimen/mtrl_calendar_content_padding` |
| 9 | `androidx.fragment.app.FragmentContainerView` | `android:paddingRight` | `@dimen/mtrl_calendar_content_padding` |
| 10 | `androidx.fragment.app.FragmentContainerView` | `android:layout_width` | `match_parent` |
| 11 | `androidx.fragment.app.FragmentContainerView` | `android:layout_height` | `wrap_content` |
| 12 | `androidx.fragment.app.FragmentContainerView` | `android:paddingStart` | `@dimen/mtrl_calendar_content_padding` |
| 13 | `androidx.fragment.app.FragmentContainerView` | `android:paddingEnd` | `@dimen/mtrl_calendar_content_padding` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_content_padding` | `12.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/mtrl_calendar_frame
@id/mtrl_picker_fullscreen
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/mtrl_picker_header_fullscreen
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000001" android:orientation="vertical" android:id="@id/mtrl_picker_fullscreen" android:layout_width="match_parent" android:layout_height="match_parent">
  <include layout="@layout/mtrl_picker_header_fullscreen"/>
  <androidx.fragment.app.FragmentContainerView android:id="@id/mtrl_calendar_frame" android:paddingLeft="@dimen/mtrl_calendar_content_padding" android:paddingRight="@dimen/mtrl_calendar_content_padding" android:layout_width="match_parent" android:layout_height="wrap_content" android:paddingStart="@dimen/mtrl_calendar_content_padding" android:paddingEnd="@dimen/mtrl_calendar_content_padding"/>
</LinearLayout>
```
