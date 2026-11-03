# پروندهٔ لایه — `res/layout/public_profile_code_header_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/public_profile_code_header_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/public_profile_code_header_view.xml`](../../SOURCE/res/layout/public_profile_code_header_view.xml) |
| SHA-256 دیکد | `d1dc07d8d1bf901de2ef00b17e3c4f2a19d88fe36b3b81a03742554f9b8d517e` |
| ریشه | `TextView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ TextView  #@id/tv_playgrounds_header
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:textColor` | `@color/text_primary` |
| 2 | `TextView` | `android:id` | `@id/tv_playgrounds_header` |
| 3 | `TextView` | `android:layout_width` | `match_parent` |
| 4 | `TextView` | `android:layout_height` | `wrap_content` |
| 5 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_s_expandable` |
| 6 | `TextView` | `android:text` | `@string/playgrounds` |
| 7 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 8 | `TextView` | `style` | `@style/TextH3` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_s_expandable` | `12.000000dip` / `16.000000dip` (sw600dp) |
| `@string/playgrounds` | `Playgrounds` / `Spielplätze` (de) / `Playgrounds` (es) / `Aires de Jeux` (fr) / `Playgrounds` (in) / `Playground` (it) / `Playgroundy` (pl) / `Playgrounds` (pt-rBR) / `Код` (ru) / `Playground'lar` (tr) |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/tv_playgrounds_header
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.profile.main.ProfileFragment
com.getmimo.ui.publicprofile.PublicProfileActivity
com.getmimo.ui.publicprofile.PublicProfileFragment$collectData$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<TextView xmlns:android="http://schemas.android.com/apk/res/android" android:textColor="@color/text_primary" android:id="@id/tv_playgrounds_header" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_s_expandable" android:text="@string/playgrounds" android:layout_marginHorizontal="@dimen/spacing_m_expandable" style="@style/TextH3"/>
```
