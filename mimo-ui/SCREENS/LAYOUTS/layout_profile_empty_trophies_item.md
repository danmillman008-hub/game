# پروندهٔ لایه — `res/layout/profile_empty_trophies_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_empty_trophies_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_empty_trophies_item.xml`](../../SOURCE/res/layout/profile_empty_trophies_item.xml) |
| SHA-256 دیکد | `fc99f5cf5f3a96c1e448d31d8ce6cfbbe22eba9e7030c19784c57898eabe583e` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 15 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_trophies_title
   └─ LinearLayout  #@id/layout_no_trophies
      ├─ ImageView
      ├─ TextView
      └─ TextView
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
| 14 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 15 | `LinearLayout` | `android:orientation` | `vertical` |
| 16 | `LinearLayout` | `android:id` | `@id/layout_no_trophies` |
| 17 | `LinearLayout` | `android:background` | `@drawable/border_dashed` |
| 18 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 19 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 20 | `LinearLayout` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 21 | `LinearLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 22 | `LinearLayout` | `android:paddingVertical` | `@dimen/spacing_xl` |
| 23 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 24 | `LinearLayout` | `app:layout_constraintTop_toBottomOf` | `@id/tv_trophies_title` |
| 25 | `ImageView` | `android:layout_width` | `80.000000dip` |
| 26 | `ImageView` | `android:layout_height` | `80.000000dip` |
| 27 | `ImageView` | `android:src` | `@drawable/ic_leaderboard_locked` |
| 28 | `TextView` | `android:textColor` | `@color/text_primary` |
| 29 | `TextView` | `android:layout_width` | `wrap_content` |
| 30 | `TextView` | `android:layout_height` | `wrap_content` |
| 31 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 32 | `TextView` | `android:text` | `@string/no_trophies_yet_title` |
| 33 | `TextView` | `style` | `@style/TextH3` |
| 34 | `TextView` | `android:textColor` | `@color/text_weak` |
| 35 | `TextView` | `android:gravity` | `0x00000011` |
| 36 | `TextView` | `android:layout_width` | `wrap_content` |
| 37 | `TextView` | `android:layout_height` | `wrap_content` |
| 38 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 39 | `TextView` | `android:text` | `@string/no_trophies_yet_desc` |
| 40 | `TextView` | `android:layout_marginStart` | `60.000000dip` |
| 41 | `TextView` | `android:layout_marginEnd` | `60.000000dip` |
| 42 | `TextView` | `style` | `@style/TextP2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@string/leaderboard_trophies_title` | `Leaderboard Trophies` / `Leaderboard-Trophäen` (de) / `Trofeos de Clasificación` (es) / `Trophées de Classement` (fr) / `Trofi Papan Peringkat` (in) / `Trofei della classifica` (it) / `Trofea rankingowe` (pl) / `Troféus da Leaderboard` (pt-rBR) / `Награды за рейтинг` (ru) / `Liderlik Kupaları` (tr) |
| `@string/no_trophies_yet_desc` | `Get to the top of your Leaderboard and win a trophy` / `Gelange an die Spitze deines Leaderboards und gewinne eine Trophäe` (de) / `Llega a las primeras posiciones de tu Clasificaicón y gana un trofeo` (es) / `Termine en tête de ton classement et gagne un trophée.` (fr) / `Naik ke puncak Papan Peringkat dan menangkan trofi` (in) / `Arriva in cima alla tua classifica e vinci un trofeo` (it) / `Wskocz na szczyt rankingu i zdobądź trofeum` (pl) / `Chegue ao topo da sua Leaderboard e ganhe um troféu` (pt-rBR) / `Доберись до вершины рейтинга и получай награды` (ru) / `Liderlik tablonda zirveye çık ve kupa kazan` (tr) |
| `@string/no_trophies_yet_title` | `No trophies yet` / `Noch keine Trophäen` (de) / `Sin trofeos todavía` (es) / `Aucun trophée pour l'instant` (fr) / `Belum ada trofi` (in) / `Ancora nessun trofeo` (it) / `Brak trofeów` (pl) / `Ainda sem troféus` (pt-rBR) / `У тебя пока нет наград` (ru) / `Henüz kupa yok` (tr) |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/layout_no_trophies
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:paddingBottom="@dimen/spacing_m_expandable" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable">
  <TextView android:textAppearance="@style/TextH3" android:textColor="@color/text_primary" android:id="@id/tv_trophies_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/leaderboard_trophies_title" android:layout_marginStart="@dimen/spacing_m_expandable" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <LinearLayout android:gravity="0x00000011" android:orientation="vertical" android:id="@id/layout_no_trophies" android:background="@drawable/border_dashed" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable" android:layout_marginHorizontal="@dimen/spacing_m_expandable" android:paddingVertical="@dimen/spacing_xl" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_trophies_title">
    <ImageView android:layout_width="80.000000dip" android:layout_height="80.000000dip" android:src="@drawable/ic_leaderboard_locked"/>
    <TextView android:textColor="@color/text_primary" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:text="@string/no_trophies_yet_title" style="@style/TextH3"/>
    <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:text="@string/no_trophies_yet_desc" android:layout_marginStart="60.000000dip" android:layout_marginEnd="60.000000dip" style="@style/TextP2"/>
  </LinearLayout>
</androidx.constraintlayout.widget.ConstraintLayout>
```
