# پروندهٔ لایه — `res/layout/leaderboard_introduction_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/leaderboard_introduction_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/leaderboard_introduction_fragment.xml`](../../SOURCE/res/layout/leaderboard_introduction_fragment.xml) |
| SHA-256 دیکد | `1bc889ccf17c24c5de784cb1322581062ce8833f76be72570b033f1ca7664642` |
| ریشه | `FrameLayout` |
| تعداد گره | 13 |
| تعداد شناسه | 10 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 35 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ ImageView  #@id/iv_leaderboard_intro_image
      ├─ TextView  #@id/iv_leaderboard_intro_title
      ├─ TextView  #@id/iv_leaderboard_intro_subtitle
      ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/cl_leaderboard_intro_details_container
      │  ├─ ImageView  #@id/iv_leaderboard_into_league_image
      │  ├─ TextView  #@id/tv_leaderboard_into_league_title
      │  ├─ TextView  #@id/tv_leaderboard_into_league_subtitle
      │  ├─ ImageView  #@id/iv_leaderboard_into_time_image
      │  ├─ TextView  #@id/tv_leaderboard_into_time_title
      │  └─ TextView
      └─ androidx.compose.ui.platform.ComposeView  #@id/mb_leaderboard_into_got_it
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 2 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000001` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:padding` | `@dimen/spacing_m_expandable` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 7 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 8 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:maxWidth` | `@dimen/content_max_width` |
| 9 | `ImageView` | `android:id` | `@id/iv_leaderboard_intro_image` |
| 10 | `ImageView` | `android:layout_width` | `0.000000dip` |
| 11 | `ImageView` | `android:layout_height` | `100.000000dip` |
| 12 | `ImageView` | `android:layout_marginBottom` | `@dimen/spacing_l_expandable` |
| 13 | `ImageView` | `android:src` | `@drawable/ic_leaderboard_introduction` |
| 14 | `ImageView` | `android:adjustViewBounds` | `true` |
| 15 | `ImageView` | `app:layout_constraintBottom_toTopOf` | `@id/iv_leaderboard_intro_title` |
| 16 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `@id/iv_leaderboard_intro_title` |
| 17 | `ImageView` | `app:layout_constraintStart_toStartOf` | `@id/iv_leaderboard_intro_title` |
| 18 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 19 | `ImageView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 20 | `TextView` | `android:textAppearance` | `@style/TextH1` |
| 21 | `TextView` | `android:textColor` | `@color/text_primary` |
| 22 | `TextView` | `android:gravity` | `0x00000011` |
| 23 | `TextView` | `android:id` | `@id/iv_leaderboard_intro_title` |
| 24 | `TextView` | `android:layout_width` | `wrap_content` |
| 25 | `TextView` | `android:layout_height` | `wrap_content` |
| 26 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_xs_expandable` |
| 27 | `TextView` | `android:text` | `@string/leaderboard_into_title` |
| 28 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/iv_leaderboard_intro_subtitle` |
| 29 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 30 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 31 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_leaderboard_intro_image` |
| 32 | `TextView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 33 | `TextView` | `android:textAppearance` | `@style/TextP1` |
| 34 | `TextView` | `android:textColor` | `@color/text_weak` |
| 35 | `TextView` | `android:gravity` | `0x00000011` |
| 36 | `TextView` | `android:id` | `@id/iv_leaderboard_intro_subtitle` |
| 37 | `TextView` | `android:layout_width` | `0.000000dip` |
| 38 | `TextView` | `android:layout_height` | `wrap_content` |
| 39 | `TextView` | `android:text` | `@string/leaderboard_into_subtitle` |
| 40 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 41 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/cl_leaderboard_intro_details_container` |
| 42 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 43 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 44 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_leaderboard_intro_title` |
| 45 | `TextView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 46 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/cl_leaderboard_intro_details_container` |
| 47 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@drawable/rounded_background` |
| 48 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:padding` | `@dimen/spacing_l_expandable` |
| 49 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `0.000000dip` |
| 50 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 51 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginBottom` | `@dimen/spacing_l_expandable` |
| 52 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintBottom_toTopOf` | `@id/mb_leaderboard_into_got_it` |
| 53 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 54 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 55 | `ImageView` | `android:id` | `@id/iv_leaderboard_into_league_image` |
| 56 | `ImageView` | `android:layout_width` | `@dimen/icon_size_large_expandable` |
| 57 | `ImageView` | `android:layout_height` | `@dimen/icon_size_large_expandable` |
| 58 | `ImageView` | `android:src` | `@drawable/ic_trophy` |
| 59 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 60 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 61 | `ImageView` | `app:tint` | `@color/primary_default` |
| 62 | `TextView` | `android:textAppearance` | `@style/TextH4` |
| 63 | `TextView` | `android:textColor` | `@color/text_primary` |
| 64 | `TextView` | `android:gravity` | `0x00000010` |
| 65 | `TextView` | `android:id` | `@id/tv_leaderboard_into_league_title` |
| 66 | `TextView` | `android:layout_width` | `0.000000dip` |
| 67 | `TextView` | `android:layout_height` | `wrap_content` |
| 68 | `TextView` | `android:text` | `@string/leaderboard_into_league_title` |
| 69 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_xs_expandable` |
| 70 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_leaderboard_into_league_image` |
| 71 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 72 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_leaderboard_into_league_image` |
| 73 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/iv_leaderboard_into_league_image` |
| 74 | `TextView` | `android:textAppearance` | `@style/TextP3` |
| 75 | `TextView` | `android:textColor` | `@color/text_weak` |
| 76 | `TextView` | `android:id` | `@id/tv_leaderboard_into_league_subtitle` |
| 77 | `TextView` | `android:layout_width` | `0.000000dip` |
| 78 | `TextView` | `android:layout_height` | `wrap_content` |
| 79 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs_expandable` |
| 80 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 81 | `TextView` | `android:text` | `@string/leaderboard_into_league_subtitle` |
| 82 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 83 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/iv_leaderboard_into_league_image` |
| 84 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_leaderboard_into_league_title` |
| 85 | `ImageView` | `android:id` | `@id/iv_leaderboard_into_time_image` |
| 86 | `ImageView` | `android:layout_width` | `@dimen/icon_size_large_expandable` |
| 87 | `ImageView` | `android:layout_height` | `@dimen/icon_size_large_expandable` |
| 88 | `ImageView` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 89 | `ImageView` | `android:src` | `@drawable/ic_timer` |
| 90 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 91 | `ImageView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_leaderboard_into_league_subtitle` |
| 92 | `ImageView` | `app:tint` | `@color/primary_default` |
| 93 | `TextView` | `android:textAppearance` | `@style/TextH4` |
| 94 | `TextView` | `android:textColor` | `@color/text_primary` |
| 95 | `TextView` | `android:gravity` | `0x00000010` |
| 96 | `TextView` | `android:id` | `@id/tv_leaderboard_into_time_title` |
| 97 | `TextView` | `android:layout_width` | `0.000000dip` |
| 98 | `TextView` | `android:layout_height` | `wrap_content` |
| 99 | `TextView` | `android:text` | `@string/leaderboard_into_time_title` |
| 100 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_xs_expandable` |
| 101 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_leaderboard_into_time_image` |
| 102 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 103 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_leaderboard_into_time_image` |
| 104 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/iv_leaderboard_into_time_image` |
| 105 | `TextView` | `android:textAppearance` | `@style/TextP3` |
| 106 | `TextView` | `android:textColor` | `@color/text_weak` |
| 107 | `TextView` | `android:layout_width` | `0.000000dip` |
| 108 | `TextView` | `android:layout_height` | `wrap_content` |
| 109 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs_expandable` |
| 110 | `TextView` | `android:text` | `@string/leaderboard_into_time_subtitle` |
| 111 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 112 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/iv_leaderboard_into_time_image` |
| 113 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_leaderboard_into_time_title` |
| 114 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/mb_leaderboard_into_got_it` |
| 115 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 116 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 117 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/primary_default` | `#FF7E4BDE` / `#FF885BDE` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/content_max_width` | `608.000000dip` |
| `@dimen/icon_size_large_expandable` | `24.000000dip` / `32.000000dip` (sw600dp) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_l_expandable` | `24.000000dip` / `36.000000dip` (sw600dp) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_xs_expandable` | `8.000000dip` / `12.000000dip` (sw600dp) |
| `@string/leaderboard_into_league_subtitle` | `Finish in the top 15 to advance to a higher league.` / `Schließe in den Top 15 ab, um in eine höhere Liga aufzusteigen.` (de) / `Termina en el top 15 para ascender a la siguiente liga.` (es) / `Termine parmi les 15 premiers pour accéder à une Ligue supérieure.` (fr) / `Finis di 15 teratas untuk naik ke liga yang lebih tinggi.` (in) / `Chiudi tra i primi 15 per salire di lega.` (it) / `Zakończ w top 15, aby awansować do wyższej ligi.` (pl) / `Termine no top 15 para avançar para uma liga superior.` (pt-rBR) / `Закончи в топ 15 и перейди в лигу выше.` (ru) / `Bir üst lige yükselmek için ilk 15 içinde bitir.` (tr) |
| `@string/leaderboard_into_league_title` | `Conquer your League` / `Erobere deine Liga` (de) / `Conquista tu liga` (es) / `Remporter ta Ligue` (fr) / `Taklukkan ligamu` (in) / `Conquista la tua lega` (it) / `Zdobądź swoją ligę` (pl) / `Conquiste sua Liga` (pt-rBR) / `Победи в своей Лиге` (ru) / `Ligini fethet` (tr) |
| `@string/leaderboard_into_subtitle` | `Compete with learners around the world for most weekly XP.` / `Wetteifere mit anderen Lernenden auf der Welt für die meisten wöchentlichen XP.` (de) / `Compite con estudiantes de todo el mundo por la mayor XP semanal.` (es) / `Rivalise avec les apprenants du monde entier pour le plus grand nombre de XP hebdomadaires.` (fr) / `Bersaing dengan pelajar di seluruh dunia untuk XP mingguan terbanyak.` (in) / `Competi con studenti di tutto il mondo per gli XP settimanali.` (it) / `Rywalizuj z uczącymi się z całego świata o najwięcej XP w tygodniu.` (pl) / `Dispute com alunos do mundo inteiro.` (pt-rBR) / `Соревнуйся с пользователями по всему миру каждую неделю за максимальные очки (XP).` (ru) / `Haftalık en yüksek XP için dünyanın dört bir yanındaki öğrenenlerle yarış.` (tr) |
| `@string/leaderboard_into_time_subtitle` | `You have limited time to get to the top. Results will be ready once the time runs out.` / `Deine Zeit, um an die Spitze zu kommen, ist begrenzt. Die Ergebnisse stehen bereit, sobald die Zeit abgelaufen ist.` (de) / `Tienes tiempo limitado para llegar al top. Los resultados aparecerán cuando se acabe el tiempo.` (es) / `Tu as un temps limité pour arriver au sommet. Les résultats seront prêts une fois le temps écoulé.` (fr) / `Waktumu terbatas untuk sampai ke puncak. Hasil akan siap begitu waktu habis.` (in) / `Hai un tempo limitato per arrivare in cima. I risultati arrivano allo scadere del tempo.` (it) / `Masz ograniczony czas, aby dotrzeć na szczyt. Wyniki poznasz, gdy czas się skończy.` (pl) / `Você tem tempo limitado para chegar ao topo. Os resultados estarão prontos assim que o tempo acabar.` (pt-rBR) / `У тебя истекает время, чтобы добраться до вершины рейтинга. Как только оно истечёт, результаты будут окончательными.` (ru) / `Zirveye çıkmak için sınırlı zamanın var. Süre dolduğunda sonuçlar hazır olacak.` (tr) |
| `@string/leaderboard_into_time_title` | `Time is running` / `Die Zeit läuft` (de) / `El tiempo corre` (es) / `Le temps presse` (fr) / `Waktu terus berjalan` (in) / `Il tempo corre` (it) / `Czas leci` (pl) / `O tempo está passando` (pt-rBR) / `Время истекает` (ru) / `Süre işliyor` (tr) |
| `@string/leaderboard_into_title` | `Weekly Leaderboard` / `Wöchentliches Leaderboard` (de) / `Clasificación Semanal` (es) / `Classement Hebdomadaire` (fr) / `Papan Peringkat Mingguan` (in) / `Classifica settimanale` (it) / `Ranking tygodnia` (pl) / `Leaderboard Semanal` (pt-rBR) / `Еженедельный Рейтинг` (ru) / `Haftalık Liderlik Tablosu` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextH4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '11.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/cl_leaderboard_intro_details_container
@id/iv_leaderboard_into_league_image
@id/iv_leaderboard_into_time_image
@id/iv_leaderboard_intro_image
@id/iv_leaderboard_intro_subtitle
@id/iv_leaderboard_intro_title
@id/mb_leaderboard_into_got_it
@id/tv_leaderboard_into_league_subtitle
@id/tv_leaderboard_into_league_title
@id/tv_leaderboard_into_time_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.leaderboard.LeaderboardFragment$observeViewModelEvents$1$1$1
com.getmimo.ui.onboarding.step1.IntroductionFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.constraintlayout.widget.ConstraintLayout android:layout_gravity="0x00000001" android:background="@color/background_primary" android:padding="@dimen/spacing_m_expandable" android:layout_width="match_parent" android:layout_height="match_parent" android:maxWidth="@dimen/content_max_width">
    <ImageView android:id="@id/iv_leaderboard_intro_image" android:layout_width="0.000000dip" android:layout_height="100.000000dip" android:layout_marginBottom="@dimen/spacing_l_expandable" android:src="@drawable/ic_leaderboard_introduction" android:adjustViewBounds="true" app:layout_constraintBottom_toTopOf="@id/iv_leaderboard_intro_title" app:layout_constraintEnd_toEndOf="@id/iv_leaderboard_intro_title" app:layout_constraintStart_toStartOf="@id/iv_leaderboard_intro_title" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_chainStyle="2"/>
    <TextView android:textAppearance="@style/TextH1" android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/iv_leaderboard_intro_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_xs_expandable" android:text="@string/leaderboard_into_title" app:layout_constraintBottom_toTopOf="@id/iv_leaderboard_intro_subtitle" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_leaderboard_intro_image" app:layout_constraintVertical_chainStyle="2"/>
    <TextView android:textAppearance="@style/TextP1" android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/iv_leaderboard_intro_subtitle" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:text="@string/leaderboard_into_subtitle" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constraintBottom_toTopOf="@id/cl_leaderboard_intro_details_container" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_leaderboard_intro_title" app:layout_constraintVertical_chainStyle="2"/>
    <androidx.constraintlayout.widget.ConstraintLayout android:id="@id/cl_leaderboard_intro_details_container" android:background="@drawable/rounded_background" android:padding="@dimen/spacing_l_expandable" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_l_expandable" app:layout_constraintBottom_toTopOf="@id/mb_leaderboard_into_got_it" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0">
      <ImageView android:id="@id/iv_leaderboard_into_league_image" android:layout_width="@dimen/icon_size_large_expandable" android:layout_height="@dimen/icon_size_large_expandable" android:src="@drawable/ic_trophy" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:tint="@color/primary_default"/>
      <TextView android:textAppearance="@style/TextH4" android:textColor="@color/text_primary" android:gravity="0x00000010" android:id="@id/tv_leaderboard_into_league_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:text="@string/leaderboard_into_league_title" android:layout_marginStart="@dimen/spacing_xs_expandable" app:layout_constraintBottom_toBottomOf="@id/iv_leaderboard_into_league_image" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/iv_leaderboard_into_league_image" app:layout_constraintTop_toTopOf="@id/iv_leaderboard_into_league_image"/>
      <TextView android:textAppearance="@style/TextP3" android:textColor="@color/text_weak" android:id="@id/tv_leaderboard_into_league_subtitle" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs_expandable" android:layout_marginBottom="@dimen/spacing_m" android:text="@string/leaderboard_into_league_subtitle" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="@id/iv_leaderboard_into_league_image" app:layout_constraintTop_toBottomOf="@id/tv_leaderboard_into_league_title"/>
      <ImageView android:id="@id/iv_leaderboard_into_time_image" android:layout_width="@dimen/icon_size_large_expandable" android:layout_height="@dimen/icon_size_large_expandable" android:layout_marginTop="@dimen/spacing_m_expandable" android:src="@drawable/ic_timer" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_leaderboard_into_league_subtitle" app:tint="@color/primary_default"/>
      <TextView android:textAppearance="@style/TextH4" android:textColor="@color/text_primary" android:gravity="0x00000010" android:id="@id/tv_leaderboard_into_time_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:text="@string/leaderboard_into_time_title" android:layout_marginStart="@dimen/spacing_xs_expandable" app:layout_constraintBottom_toBottomOf="@id/iv_leaderboard_into_time_image" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/iv_leaderboard_into_time_image" app:layout_constraintTop_toTopOf="@id/iv_leaderboard_into_time_image"/>
      <TextView android:textAppearance="@style/TextP3" android:textColor="@color/text_weak" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs_expandable" android:text="@string/leaderboard_into_time_subtitle" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="@id/iv_leaderboard_into_time_image" app:layout_constraintTop_toBottomOf="@id/tv_leaderboard_into_time_title"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
    <androidx.compose.ui.platform.ComposeView android:id="@id/mb_leaderboard_into_got_it" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</FrameLayout>
```
