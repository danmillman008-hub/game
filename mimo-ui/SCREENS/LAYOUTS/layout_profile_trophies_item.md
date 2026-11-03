# پروندهٔ لایه — `res/layout/profile_trophies_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_trophies_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_trophies_item.xml`](../../SOURCE/res/layout/profile_trophies_item.xml) |
| SHA-256 دیکد | `da0a7db4cdc24a9203b6f82b7a91f2ba093b76b57d7bbd4a3ab128c82b87e745` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_trophies_title
   └─ LinearLayout  #@id/layout_trophies_rows
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingBottom` | `@dimen/spacing_m_expandable` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 5 | `TextView` | `android:textAppearance` | `@style/TextH3` |
| 6 | `TextView` | `android:textColor` | `@color/text_primary` |
| 7 | `TextView` | `android:id` | `@id/tv_trophies_title` |
| 8 | `TextView` | `android:layout_width` | `wrap_content` |
| 9 | `TextView` | `android:layout_height` | `wrap_content` |
| 10 | `TextView` | `android:text` | `@string/leaderboard_trophies_title` |
| 11 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m_expandable` |
| 12 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `LinearLayout` | `android:orientation` | `vertical` |
| 15 | `LinearLayout` | `android:id` | `@id/layout_trophies_rows` |
| 16 | `LinearLayout` | `android:background` | `@drawable/rounded_background` |
| 17 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 18 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 19 | `LinearLayout` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 20 | `LinearLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 21 | `LinearLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 22 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 23 | `LinearLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_trophies_title` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@string/leaderboard_trophies_title` | `Leaderboard Trophies` / `Leaderboard-Trophäen` (de) / `Trofeos de Clasificación` (es) / `Trophées de Classement` (fr) / `Trofi Papan Peringkat` (in) / `Trofei della classifica` (it) / `Trofea rankingowe` (pl) / `Troféus da Leaderboard` (pt-rBR) / `Награды за рейтинг` (ru) / `Liderlik Kupaları` (tr) |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/layout_trophies_rows
@id/tv_trophies_title
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:paddingBottom="@dimen/spacing_m_expandable" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable">
  <TextView android:textAppearance="@style/TextH3" android:textColor="@color/text_primary" android:id="@id/tv_trophies_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/leaderboard_trophies_title" android:layout_marginStart="@dimen/spacing_m_expandable" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <LinearLayout android:orientation="vertical" android:id="@id/layout_trophies_rows" android:background="@drawable/rounded_background" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable" android:foreground="?attr/selectableItemBackground" android:layout_marginHorizontal="@dimen/spacing_m_expandable" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_trophies_title"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
