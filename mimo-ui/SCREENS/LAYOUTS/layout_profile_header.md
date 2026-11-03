# پروندهٔ لایه — `res/layout/profile_header.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_header.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_header.xml`](../../SOURCE/res/layout/profile_header.xml) |
| SHA-256 دیکد | `3444f5226f47787121965e6073abe812c78d66e62cc323b913b8e6b75d1b99ca` |
| ریشه | `FrameLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   └─ com.getmimo.ui.profile.view.ProfileHeaderView  #@id/profile_header_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 2 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 3 | `com.getmimo.ui.profile.view.ProfileHeaderView` | `android:id` | `@id/profile_header_view` |
| 4 | `com.getmimo.ui.profile.view.ProfileHeaderView` | `android:layout_width` | `match_parent` |
| 5 | `com.getmimo.ui.profile.view.ProfileHeaderView` | `android:layout_height` | `wrap_content` |
| 6 | `com.getmimo.ui.profile.view.ProfileHeaderView` | `android:layout_marginBottom` | `@dimen/spacing_s_expandable` |
| 7 | `com.getmimo.ui.profile.view.ProfileHeaderView` | `style` | `@style/ProfileHeaderView` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/spacing_s_expandable` | `12.000000dip` / `16.000000dip` (sw600dp) |
| `@style/ProfileHeaderView` | `[{'attr': 'android:layout_gravity', 'attr_id': '0x010100B3', 'value': '0x00000011', 'value_type': 'int_hex'}, {'attr': 'android:layout_width', 'attr_id': '0x010100F4', 'value': '-1', 'value_type': 'int_dec'}]` / `[{'attr': 'android:layout_gravity', 'attr_id': '0x010100B3', 'value': '0x00000011', 'value_type': 'int_hex'}, {'attr': 'android:layout_width', 'attr_id': '0x010100F4', 'value': '-2', 'value_type': 'int_dec'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/profile_header_view
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.profile.main.ProfileFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="wrap_content">
  <com.getmimo.ui.profile.view.ProfileHeaderView android:id="@id/profile_header_view" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_s_expandable" style="@style/ProfileHeaderView"/>
</FrameLayout>
```
