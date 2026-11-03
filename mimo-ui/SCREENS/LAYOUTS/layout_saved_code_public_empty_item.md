# پروندهٔ لایه — `res/layout/saved_code_public_empty_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/saved_code_public_empty_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/saved_code_public_empty_item.xml`](../../SOURCE/res/layout/saved_code_public_empty_item.xml) |
| SHA-256 دیکد | `9a44253df00367e2eb684b9defe9e368852c59c6d5e4c1691f41f016e65dfa00` |
| ریشه | `FrameLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 9 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   └─ TextView  #@id/tv_empty_playgrounds
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:gravity` | `0x00000011` |
| 2 | `FrameLayout` | `android:background` | `@drawable/border_dashed` |
| 3 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 4 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 5 | `FrameLayout` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 6 | `FrameLayout` | `android:layout_marginBottom` | `@dimen/spacing_s_expandable` |
| 7 | `FrameLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_s_expandable` |
| 8 | `FrameLayout` | `android:paddingVertical` | `@dimen/spacing_xl` |
| 9 | `TextView` | `android:textColor` | `@color/text_weak` |
| 10 | `TextView` | `android:gravity` | `0x00000011` |
| 11 | `TextView` | `android:id` | `@id/tv_empty_playgrounds` |
| 12 | `TextView` | `android:layout_width` | `match_parent` |
| 13 | `TextView` | `android:layout_height` | `wrap_content` |
| 14 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 15 | `TextView` | `android:text` | `@string/saved_code_empty_state_header` |
| 16 | `TextView` | `android:layout_marginStart` | `60.000000dip` |
| 17 | `TextView` | `android:layout_marginEnd` | `60.000000dip` |
| 18 | `TextView` | `style` | `@style/TextP2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_s_expandable` | `12.000000dip` / `16.000000dip` (sw600dp) |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@string/saved_code_empty_state_header` | `No playgrounds` / `Keine Playgrounds` (de) / `Sin Playgrounds` (es) / `Aucune aires de jeux` (fr) / `Belum ada playground` (in) / `Nessun playground` (it) / `Brak Playgroundów` (pl) / `Sem playgrounds` (pt-rBR) / `Нет кода` (ru) / `Playground yok` (tr) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/tv_empty_playgrounds
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
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000011" android:background="@drawable/border_dashed" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable" android:layout_marginBottom="@dimen/spacing_s_expandable" android:layout_marginHorizontal="@dimen/spacing_s_expandable" android:paddingVertical="@dimen/spacing_xl">
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_empty_playgrounds" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:text="@string/saved_code_empty_state_header" android:layout_marginStart="60.000000dip" android:layout_marginEnd="60.000000dip" style="@style/TextP2"/>
</FrameLayout>
```
