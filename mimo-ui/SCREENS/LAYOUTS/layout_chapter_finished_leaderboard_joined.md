# پروندهٔ لایه — `res/layout/chapter_finished_leaderboard_joined.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/chapter_finished_leaderboard_joined.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/chapter_finished_leaderboard_joined.xml`](../../SOURCE/res/layout/chapter_finished_leaderboard_joined.xml) |
| SHA-256 دیکد | `b78d2da62ef67f8fd8f206d575c2def8229524c20c616b1923e9dc9206f74488` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 17 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_later
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/iv_chapter_finished_leaderboard_joined_icon
   ├─ TextView  #@id/tv_chapter_finished_leaderboard_joined_title
   └─ TextView  #@id/tv_chapter_finished_leaderboard_joined_description
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 3 | `TextView` | `android:textColor` | `@color/text_weak` |
| 4 | `TextView` | `android:id` | `@id/tv_later` |
| 5 | `TextView` | `android:visibility` | `gone` |
| 6 | `TextView` | `android:layout_width` | `wrap_content` |
| 7 | `TextView` | `android:layout_height` | `wrap_content` |
| 8 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xxl` |
| 9 | `TextView` | `android:text` | `@string/later` |
| 10 | `TextView` | `android:layout_marginEnd` | `20.000000dip` |
| 11 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 12 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `TextView` | `style` | `@style/MaterialButton.TextButton` |
| 14 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:id` | `@id/iv_chapter_finished_leaderboard_joined_icon` |
| 15 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_width` | `@dimen/chapter_end_animation_width` |
| 16 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_height` | `wrap_content` |
| 17 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_chapter_finished_leaderboard_joined_title` |
| 18 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 19 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintStart_toStartOf` | `0` |
| 20 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintTop_toTopOf` | `0` |
| 21 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 22 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveResource` | `@raw/leaderboard` |
| 23 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveStateMachine` | `default` |
| 24 | `TextView` | `android:textAppearance` | `@style/TextH1` |
| 25 | `TextView` | `android:textColor` | `@color/text_primary` |
| 26 | `TextView` | `android:gravity` | `0x00000001` |
| 27 | `TextView` | `android:id` | `@id/tv_chapter_finished_leaderboard_joined_title` |
| 28 | `TextView` | `android:layout_width` | `match_parent` |
| 29 | `TextView` | `android:layout_height` | `wrap_content` |
| 30 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 31 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_xs` |
| 32 | `TextView` | `android:text` | `@string/chapter_end_screen_leaderboard_joined_title` |
| 33 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_xxl` |
| 34 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xxl` |
| 35 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_chapter_finished_leaderboard_joined_description` |
| 36 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_chapter_finished_leaderboard_joined_icon` |
| 37 | `TextView` | `android:textAppearance` | `@style/TextP1` |
| 38 | `TextView` | `android:textColor` | `@color/text_weak` |
| 39 | `TextView` | `android:gravity` | `0x00000001` |
| 40 | `TextView` | `android:id` | `@id/tv_chapter_finished_leaderboard_joined_description` |
| 41 | `TextView` | `android:layout_width` | `match_parent` |
| 42 | `TextView` | `android:layout_height` | `wrap_content` |
| 43 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 44 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_xs` |
| 45 | `TextView` | `android:text` | `@string/chapter_end_screen_leaderboard_joined_description` |
| 46 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_xxl` |
| 47 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xxl` |
| 48 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 49 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_chapter_finished_leaderboard_joined_title` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/chapter_end_animation_width` | `200.000000dip` / `260.000000dip` (sw600dp) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxl` | `40.000000dip` |
| `@string/chapter_end_screen_leaderboard_joined_description` | `Compete with learners around the world for most weekly XP. The more you learn, the more XP you earn!` / `Wetteifere mit Lernenden aus aller Welt für die meisten wöchentlichen XP. Je mehr du lernst, desto mehr XP verdienst du!` (de) / `Compite con estudiantes de todo el mundo por la mayor XP semanal. ¡Cuanto más aprendas, más XP ganas!` (es) / `Rivalise avec les apprenants du monde entier pour obtenir le plus d'XP hebdomadaire. Plus tu apprends, plus tu gagnes d'XP!` (fr) / `Bersaing dengan pelajar dari seluruh dunia untuk XP mingguan terbanyak. Makin banyak kamu belajar, makin banyak XP yang kamu dapat!` (in) / `Competi con altri studenti in tutto il mondo per gli XP settimanali. Più impari, più XP guadagni!` (it) / `Rywalizuj z uczącymi się z całego świata o najwięcej XP w tygodniu. Im więcej się uczysz, tym więcej XP zdobywasz!` (pl) / `Dispute com alunos do mundo inteiro. Quanto mais você aprende, mais XP você ganha!` (pt-rBR) / `Соревнуйся с пользователями по всему миру по количеству опыта в неделю (XP). Чем больше ты учишься, тем больше XP зарабатываешь!` (ru) / `Haftalık en yüksek XP için dünyanın dört bir yanındaki öğrenenlerle yarış. Ne kadar çok öğrenirsen o kadar çok XP kazanırsın!` (tr) |
| `@string/chapter_end_screen_leaderboard_joined_title` | `You’ve joined a Leaderboard!` / `Du hast es auf ein Leaderboard geschafft!` (de) / `¡Te has unido a una clasificación!` (es) / `Tu as rejoint un Classement!` (fr) / `Kamu masuk Papan Peringkat!` (in) / `Sei in una classifica!` (it) / `Dołączasz do rankingu!` (pl) / `Você se juntou a uma Leaderboard!` (pt-rBR) / `Ты попал(а) в рейтинг!` (ru) / `Bir liderlik tablosuna katıldın!` (tr) |
| `@string/later` | `Later` / `Später` (de) / `Más tarde` (es) / `Plus tard` (fr) / `Nanti` (in) / `Più tardi` (it) / `Później` (pl) / `Mais tarde` (pt-rBR) / `Потом` (ru) / `Sonra` (tr) |
| `@style/MaterialButton.TextButton` | `[{'attr': 'android:textAppearance', 'attr_id': '0x01010034', 'value': '@style/TextButton1', 'value_type': 'reference'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/material_button_text_state', 'value_type': 'reference'}, {'attr': 'attr.drawableTint', 'attr_id': '0x7F040218', 'value': '@color/material_button_text_state', 'value_type': 'reference'}, {'attr': 'attr.iconTint', 'attr_id': '0x7F0402FA', 'value': '@color/material_button_text_state', 'value_type': 'reference'}, {'attr': 'attr.rippleColor', 'attr_id': '0x7F0404F0', 'value': '@color/support_snow_light', 'value_type': 'reference'}]` |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_chapter_finished_leaderboard_joined_icon
@id/tv_chapter_finished_leaderboard_joined_description
@id/tv_chapter_finished_leaderboard_joined_title
@id/tv_later
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.chapter.ChapterActivity
com.getmimo.ui.chapter.chapterendview.leaderboard.ChapterFinishedLeaderboardFragment$setupAuthenticationObservers$2
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$onChapterFinishedContinue$1
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$1$1
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$2
com.getmimo.ui.leaderboard.LeaderboardFragment$observeViewModelEvents$1$1$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent">
  <TextView android:textColor="@color/text_weak" android:id="@id/tv_later" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xxl" android:text="@string/later" android:layout_marginEnd="20.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" style="@style/MaterialButton.TextButton"/>
  <app.rive.runtime.kotlin.RiveAnimationView android:id="@id/iv_chapter_finished_leaderboard_joined_icon" android:layout_width="@dimen/chapter_end_animation_width" android:layout_height="wrap_content" app:layout_constraintBottom_toTopOf="@id/tv_chapter_finished_leaderboard_joined_title" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_chainStyle="2" app:riveResource="@raw/leaderboard" app:riveStateMachine="default"/>
  <TextView android:textAppearance="@style/TextH1" android:textColor="@color/text_primary" android:gravity="0x00000001" android:id="@id/tv_chapter_finished_leaderboard_joined_title" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginBottom="@dimen/spacing_xs" android:text="@string/chapter_end_screen_leaderboard_joined_title" android:layout_marginStart="@dimen/spacing_xxl" android:layout_marginEnd="@dimen/spacing_xxl" app:layout_constraintBottom_toTopOf="@id/tv_chapter_finished_leaderboard_joined_description" app:layout_constraintTop_toBottomOf="@id/iv_chapter_finished_leaderboard_joined_icon"/>
  <TextView android:textAppearance="@style/TextP1" android:textColor="@color/text_weak" android:gravity="0x00000001" android:id="@id/tv_chapter_finished_leaderboard_joined_description" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginBottom="@dimen/spacing_xs" android:text="@string/chapter_end_screen_leaderboard_joined_description" android:layout_marginStart="@dimen/spacing_xxl" android:layout_marginEnd="@dimen/spacing_xxl" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintTop_toBottomOf="@id/tv_chapter_finished_leaderboard_joined_title"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
