# پروندهٔ لایه — `res/layout/profile_friends_header.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_friends_header.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_friends_header.xml`](../../SOURCE/res/layout/profile_friends_header.xml) |
| SHA-256 دیکد | `bfead4ad15a1cc6cad4acf151a5d1dab4db1474575c1f33987888238cb60be47` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_friends_title
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_add_friends
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 3 | `TextView` | `android:textAppearance` | `@style/TextH3` |
| 4 | `TextView` | `android:textColor` | `@color/text_primary` |
| 5 | `TextView` | `android:id` | `@id/tv_friends_title` |
| 6 | `TextView` | `android:layout_width` | `wrap_content` |
| 7 | `TextView` | `android:layout_height` | `wrap_content` |
| 8 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_s_expandable` |
| 9 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 10 | `TextView` | `android:text` | `@string/friends_title` |
| 11 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m_expandable` |
| 12 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 13 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 14 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 15 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_add_friends` |
| 16 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 17 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 18 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginEnd` | `@dimen/spacing_m_expandable` |
| 19 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 20 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 21 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toTopOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_s_expandable` | `12.000000dip` / `16.000000dip` (sw600dp) |
| `@string/friends_title` | `Friends` / `Freunde` (de) / `Círculo` (es) / `Amis` (fr) / `Teman` (in) / `Amici` (it) / `Znajomi` (pl) / `Amigos` (pt-rBR) / `Друзья` (ru) / `Arkadaşlar` (tr) |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_add_friends
@id/tv_friends_title
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="wrap_content">
  <TextView android:textAppearance="@style/TextH3" android:textColor="@color/text_primary" android:id="@id/tv_friends_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s_expandable" android:layout_marginBottom="@dimen/spacing_m_expandable" android:text="@string/friends_title" android:layout_marginStart="@dimen/spacing_m_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_add_friends" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginEnd="@dimen/spacing_m_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
