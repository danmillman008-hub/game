# پروندهٔ لایه — `res/layout/chapter_finished_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/chapter_finished_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/chapter_finished_fragment.xml`](../../SOURCE/res/layout/chapter_finished_fragment.xml) |
| SHA-256 دیکد | `f2cfd5bea652aa22a4adccda93634f3ecad0fd5d432765499727da78f7cc4675` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 20 |
| تعداد شناسه | 18 |
| تگ‌های استفاده‌شده | 9 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 42 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_chapter_finished_fragment
   ├─ androidx.constraintlayout.widget.Group  #@id/group_chapter_finished_success_state
   ├─ androidx.compose.ui.platform.ComposeView  #@id/rav_chapter_finished
   ├─ TextView  #@id/tv_chapter_finished_success_title
   ├─ TextView  #@id/tv_chapter_finished_success_subtitle
   ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_chapter_finished_stats
   ├─ androidx.cardview.widget.CardView  #@id/cv_double_gain
   │  └─ TextView  #@id/tv_profile_card_value
   ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_chapter_finished_daily_goal_progress
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_chapter_finished_continue
   ├─ LinearLayout  #@id/layout_chapter_finished_loading_state
   │  ├─ app.rive.runtime.kotlin.RiveAnimationView
   │  └─ TextView
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_chapter_finished_offline_state
   │  ├─ ImageView  #@id/iv_connection_error
   │  ├─ TextView  #@id/tv_offline_state_headline
   │  ├─ TextView  #@id/tv_offline_state_description
   │  └─ androidx.compose.ui.platform.ComposeView  #@id/btn_chapter_finished_offline_state_continue
   ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_coins
   └─ androidx.fragment.app.FragmentContainerView  #@id/fcv_chapter_finished_fragment_container
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_chapter_finished_fragment` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.Group` | `android:id` | `@id/group_chapter_finished_success_state` |
| 6 | `androidx.constraintlayout.widget.Group` | `android:visibility` | `invisible` |
| 7 | `androidx.constraintlayout.widget.Group` | `android:layout_width` | `match_parent` |
| 8 | `androidx.constraintlayout.widget.Group` | `android:layout_height` | `match_parent` |
| 9 | `androidx.constraintlayout.widget.Group` | `app:constraint_referenced_ids` | `rav_chapter_finished,tv_chapter_finished_success_title,tv_chapter_finished_success_subtitle,btn_chapter_finished_continue` |
| 10 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/rav_chapter_finished` |
| 11 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 12 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 13 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 14 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 15 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_chapter_finished_success_title` |
| 16 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 17 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 18 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toTopOf` | `0` |
| 19 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 20 | `TextView` | `android:textAppearance` | `@style/TextH1` |
| 21 | `TextView` | `android:textColor` | `@color/text_primary` |
| 22 | `TextView` | `android:gravity` | `0x00000011` |
| 23 | `TextView` | `android:id` | `@id/tv_chapter_finished_success_title` |
| 24 | `TextView` | `android:layout_width` | `0.000000dip` |
| 25 | `TextView` | `android:layout_height` | `wrap_content` |
| 26 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l_expandable` |
| 27 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 28 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_chapter_finished_success_subtitle` |
| 29 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 30 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 31 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/rav_chapter_finished` |
| 32 | `TextView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 33 | `TextView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 34 | `TextView` | `android:textAppearance` | `@style/TextP1` |
| 35 | `TextView` | `android:textColor` | `@color/text_weak` |
| 36 | `TextView` | `android:gravity` | `0x00000011` |
| 37 | `TextView` | `android:id` | `@id/tv_chapter_finished_success_subtitle` |
| 38 | `TextView` | `android:layout_width` | `0.000000dip` |
| 39 | `TextView` | `android:layout_height` | `wrap_content` |
| 40 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs_expandable` |
| 41 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 42 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/cv_chapter_finished_stats` |
| 43 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 44 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 45 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_chapter_finished_success_title` |
| 46 | `TextView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 47 | `TextView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 48 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cv_chapter_finished_stats` |
| 49 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 50 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 51 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 52 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_l_expandable` |
| 53 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 54 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/cv_chapter_finished_daily_goal_progress` |
| 55 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 56 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 57 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 58 | `androidx.compose.ui.platform.ComposeView` | `app:layout_goneMarginBottom` | `@dimen/spacing_xl_expandable` |
| 59 | `androidx.cardview.widget.CardView` | `android:id` | `@id/cv_double_gain` |
| 60 | `androidx.cardview.widget.CardView` | `android:visibility` | `gone` |
| 61 | `androidx.cardview.widget.CardView` | `android:layout_width` | `wrap_content` |
| 62 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 63 | `androidx.cardview.widget.CardView` | `android:layout_marginBottom` | `16777212.000000dip` |
| 64 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/support_yellow` |
| 65 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `8.000000dip` |
| 66 | `androidx.cardview.widget.CardView` | `app:cardElevation` | `0.000000dip` |
| 67 | `androidx.cardview.widget.CardView` | `app:contentPaddingBottom` | `@dimen/spacing_xxs_expandable` |
| 68 | `androidx.cardview.widget.CardView` | `app:contentPaddingLeft` | `@dimen/spacing_s_expandable` |
| 69 | `androidx.cardview.widget.CardView` | `app:contentPaddingRight` | `@dimen/spacing_s_expandable` |
| 70 | `androidx.cardview.widget.CardView` | `app:contentPaddingTop` | `@dimen/spacing_xxs_expandable` |
| 71 | `androidx.cardview.widget.CardView` | `app:layout_constraintBottom_toTopOf` | `@id/cv_chapter_finished_stats` |
| 72 | `androidx.cardview.widget.CardView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 73 | `androidx.cardview.widget.CardView` | `app:layout_constraintStart_toStartOf` | `0` |
| 74 | `TextView` | `android:textColor` | `#FF252746` |
| 75 | `TextView` | `android:id` | `@id/tv_profile_card_value` |
| 76 | `TextView` | `android:layout_width` | `wrap_content` |
| 77 | `TextView` | `android:layout_height` | `wrap_content` |
| 78 | `TextView` | `android:text` | `@string/sparks_double_gain` |
| 79 | `TextView` | `android:textAllCaps` | `true` |
| 80 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 81 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 82 | `TextView` | `style` | `@style/TextLabel3` |
| 83 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cv_chapter_finished_daily_goal_progress` |
| 84 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 85 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 86 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 87 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_l_expandable` |
| 88 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 89 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_chapter_finished_continue` |
| 90 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 91 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 92 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 93 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_chapter_finished_continue` |
| 94 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 95 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 96 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/chapter_end_continue_button_margin_bottom` |
| 97 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 98 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 99 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 100 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 101 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 102 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 103 | `LinearLayout` | `android:orientation` | `vertical` |
| 104 | `LinearLayout` | `android:id` | `@id/layout_chapter_finished_loading_state` |
| 105 | `LinearLayout` | `android:visibility` | `gone` |
| 106 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 107 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 108 | `LinearLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 109 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 110 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 111 | `LinearLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 112 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_width` | `@dimen/chapter_end_animation_width` |
| 113 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_height` | `wrap_content` |
| 114 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveLoop` | `1` |
| 115 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveResource` | `@raw/intro` |
| 116 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveStateMachine` | `default` |
| 117 | `TextView` | `android:textColor` | `@color/text_weak` |
| 118 | `TextView` | `android:layout_width` | `wrap_content` |
| 119 | `TextView` | `android:layout_height` | `wrap_content` |
| 120 | `TextView` | `android:text` | `@string/chapter_finished_loading` |
| 121 | `TextView` | `style` | `@style/TextP1` |
| 122 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:orientation` | `vertical` |
| 123 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_chapter_finished_offline_state` |
| 124 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:visibility` | `gone` |
| 125 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `0.000000dip` |
| 126 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 127 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 128 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 129 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 130 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 131 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 132 | `ImageView` | `android:id` | `@id/iv_connection_error` |
| 133 | `ImageView` | `android:layout_width` | `wrap_content` |
| 134 | `ImageView` | `android:layout_height` | `wrap_content` |
| 135 | `ImageView` | `android:layout_marginBottom` | `36.000000dip` |
| 136 | `ImageView` | `android:src` | `@drawable/ic_state_offline` |
| 137 | `ImageView` | `android:elevation` | `2.000000dip` |
| 138 | `ImageView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_offline_state_headline` |
| 139 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 140 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 141 | `TextView` | `android:gravity` | `0x00000011` |
| 142 | `TextView` | `android:layout_gravity` | `0x00000011` |
| 143 | `TextView` | `android:id` | `@id/tv_offline_state_headline` |
| 144 | `TextView` | `android:layout_width` | `wrap_content` |
| 145 | `TextView` | `android:layout_height` | `wrap_content` |
| 146 | `TextView` | `android:text` | `@string/offline_message` |
| 147 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 148 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 149 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 150 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 151 | `TextView` | `style` | `@style/TextChapterFinishedOfflineStateHeadline` |
| 152 | `TextView` | `android:gravity` | `0x00000011` |
| 153 | `TextView` | `android:layout_gravity` | `0x00000011` |
| 154 | `TextView` | `android:id` | `@id/tv_offline_state_description` |
| 155 | `TextView` | `android:layout_width` | `wrap_content` |
| 156 | `TextView` | `android:layout_height` | `wrap_content` |
| 157 | `TextView` | `android:layout_marginTop` | `12.000000dip` |
| 158 | `TextView` | `android:text` | `@string/chapter_finished_offline_state_description` |
| 159 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 160 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 161 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_offline_state_headline` |
| 162 | `TextView` | `style` | `@style/TextChapterFinishedOfflineStateDescription` |
| 163 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_chapter_finished_offline_state_continue` |
| 164 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 165 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 166 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/chapter_end_continue_button_margin_bottom` |
| 167 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 168 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 169 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 170 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 171 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 172 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cv_coins` |
| 173 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 174 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 175 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 176 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 177 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 178 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 179 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toTopOf` | `0` |
| 180 | `androidx.fragment.app.FragmentContainerView` | `android:id` | `@id/fcv_chapter_finished_fragment_container` |
| 181 | `androidx.fragment.app.FragmentContainerView` | `android:layout_width` | `match_parent` |
| 182 | `androidx.fragment.app.FragmentContainerView` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/support_yellow` | `#FFF4D055` / `#FFFBDF83` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/chapter_end_animation_width` | `200.000000dip` / `260.000000dip` (sw600dp) |
| `@dimen/chapter_end_continue_button_margin_bottom` | `16.000000dip` / `36.000000dip` (sw600dp) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l_expandable` | `24.000000dip` / `36.000000dip` (sw600dp) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s_expandable` | `12.000000dip` / `16.000000dip` (sw600dp) |
| `@dimen/spacing_xl_expandable` | `32.000000dip` / `48.000000dip` (sw600dp) |
| `@dimen/spacing_xs_expandable` | `8.000000dip` / `12.000000dip` (sw600dp) |
| `@dimen/spacing_xxs_expandable` | `4.000000dip` / `6.000000dip` (sw600dp) |
| `@string/chapter_finished_loading` | `Calculating your progress…` / `Dein Fortschritt wird berechnet…` (de) / `Calculando tu progreso…` (es) / `Calcul de ta progression…` (fr) / `Menghitung progresmu…` (in) / `Calcolo dei progressi in corso…` (it) / `Obliczamy twoje postępy…` (pl) / `Calculando seu progresso…` (pt-rBR) / `Подсчёт твоего прогресса…` (ru) / `İlerlemen hesaplanıyor…` (tr) |
| `@string/chapter_finished_offline_state_description` | `Make sure you’re online to make your 
Sparks count towards your daily goal` / `Stelle sicher, dass du online bist, damit deine 
Sparks auf dein Tagesziel angerechnet werden` (de) / `Asegúrate de que tienes conexión a internet para obtener tus bonificaciones para tu objetivo diario.` (es) / `Assure-toi d'être en ligne pour que tes 
Étincelles soient ajoutées à ton objectif quotidien` (fr) / `Pastikan kamu online agar 
Sparks-mu dihitung untuk target harianmu` (in) / `Assicurati di essere online per far contare i tuoi 
Sparks nell'obiettivo giornaliero` (it) / `Sprawdź połączenie, aby twoje 
Sparks liczyły się do celu dziennego` (pl) / `Verifique se você está on-line para fazer com que suas Sparks contem para sua meta diária` (pt-rBR) / `Убедись, что ты онлайн, чтобы твои 
Очки засчитались в` (ru) / `Sparks'ların günlük hedefine sayılması için 
çevrimiçi olduğundan emin ol` (tr) |
| `@string/offline_message` | `Looks like you're offline` / `Sieht so aus, als wärst du offline` (de) / `Parece que estás offline` (es) / `Il semble que tu sois hors ligne` (fr) / `Sepertinya kamu sedang offline` (in) / `Sembra che tu sia offline` (it) / `Wygląda na to, że jesteś offline` (pl) / `Parece que você está off-line` (pt-rBR) / `Кажется, ты оффлайн` (ru) / `Görünüşe göre çevrimdışısın` (tr) |
| `@string/sparks_double_gain` | `Double gain` / `Doppelter Gewinn` (de) / `Doble ganancia` (es) / `Double gain` (fr) / `Perolehan ganda` (in) / `Guadagno doppio` (it) / `Podwójny zysk` (pl) / `Ganho duplo` (pt-rBR) / `Двойной бонус` (ru) / `Çift kazanç` (tr) |
| `@style/TextChapterFinishedOfflineStateDescription` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_weak', 'value_type': 'reference'}]` |
| `@style/TextChapterFinishedOfflineStateHeadline` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}]` |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_chapter_finished_continue
@id/btn_chapter_finished_offline_state_continue
@id/cv_chapter_finished_daily_goal_progress
@id/cv_chapter_finished_stats
@id/cv_coins
@id/cv_double_gain
@id/fcv_chapter_finished_fragment_container
@id/group_chapter_finished_success_state
@id/iv_connection_error
@id/layout_chapter_finished_fragment
@id/layout_chapter_finished_loading_state
@id/layout_chapter_finished_offline_state
@id/rav_chapter_finished
@id/tv_chapter_finished_success_subtitle
@id/tv_chapter_finished_success_title
@id/tv_offline_state_description
@id/tv_offline_state_headline
@id/tv_profile_card_value
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.chapter.ChapterActivity
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$onChapterFinishedContinue$1
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$1$1
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$2
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/layout_chapter_finished_fragment" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.constraintlayout.widget.Group android:id="@id/group_chapter_finished_success_state" android:visibility="invisible" android:layout_width="match_parent" android:layout_height="match_parent" app:constraint_referenced_ids="rav_chapter_finished,tv_chapter_finished_success_title,tv_chapter_finished_success_subtitle,btn_chapter_finished_continue"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/rav_chapter_finished" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/tv_chapter_finished_success_title" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintVertical_chainStyle="2"/>
  <TextView android:textAppearance="@style/TextH1" android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_chapter_finished_success_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l_expandable" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/tv_chapter_finished_success_subtitle" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/rav_chapter_finished" app:layout_constraintVertical_chainStyle="2" app:layout_constraintWidth_max="@dimen/general_max_width"/>
  <TextView android:textAppearance="@style/TextP1" android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_chapter_finished_success_subtitle" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs_expandable" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/cv_chapter_finished_stats" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_chapter_finished_success_title" app:layout_constraintVertical_chainStyle="2" app:layout_constraintWidth_max="@dimen/general_max_width"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/cv_chapter_finished_stats" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_l_expandable" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/cv_chapter_finished_daily_goal_progress" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="@dimen/general_max_width" app:layout_goneMarginBottom="@dimen/spacing_xl_expandable"/>
  <androidx.cardview.widget.CardView android:id="@id/cv_double_gain" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="16777212.000000dip" app:cardBackgroundColor="@color/support_yellow" app:cardCornerRadius="8.000000dip" app:cardElevation="0.000000dip" app:contentPaddingBottom="@dimen/spacing_xxs_expandable" app:contentPaddingLeft="@dimen/spacing_s_expandable" app:contentPaddingRight="@dimen/spacing_s_expandable" app:contentPaddingTop="@dimen/spacing_xxs_expandable" app:layout_constraintBottom_toTopOf="@id/cv_chapter_finished_stats" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0">
    <TextView android:textColor="#FF252746" android:id="@id/tv_profile_card_value" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/sparks_double_gain" android:textAllCaps="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" style="@style/TextLabel3"/>
  </androidx.cardview.widget.CardView>
  <androidx.compose.ui.platform.ComposeView android:id="@id/cv_chapter_finished_daily_goal_progress" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_l_expandable" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/btn_chapter_finished_continue" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="@dimen/general_max_width"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_chapter_finished_continue" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/chapter_end_continue_button_margin_bottom" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="@dimen/general_max_width"/>
  <LinearLayout android:gravity="0x00000011" android:orientation="vertical" android:id="@id/layout_chapter_finished_loading_state" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <app.rive.runtime.kotlin.RiveAnimationView android:layout_width="@dimen/chapter_end_animation_width" android:layout_height="wrap_content" app:riveLoop="1" app:riveResource="@raw/intro" app:riveStateMachine="default"/>
    <TextView android:textColor="@color/text_weak" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/chapter_finished_loading" style="@style/TextP1"/>
  </LinearLayout>
  <androidx.constraintlayout.widget.ConstraintLayout android:orientation="vertical" android:id="@id/layout_chapter_finished_offline_state" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="match_parent" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <ImageView android:layout_gravity="0x00000011" android:id="@id/iv_connection_error" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="36.000000dip" android:src="@drawable/ic_state_offline" android:elevation="2.000000dip" app:layout_constraintBottom_toTopOf="@id/tv_offline_state_headline" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
    <TextView android:gravity="0x00000011" android:layout_gravity="0x00000011" android:id="@id/tv_offline_state_headline" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/offline_message" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextChapterFinishedOfflineStateHeadline"/>
    <TextView android:gravity="0x00000011" android:layout_gravity="0x00000011" android:id="@id/tv_offline_state_description" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="12.000000dip" android:text="@string/chapter_finished_offline_state_description" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_offline_state_headline" style="@style/TextChapterFinishedOfflineStateDescription"/>
    <androidx.compose.ui.platform.ComposeView android:id="@id/btn_chapter_finished_offline_state_continue" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/chapter_end_continue_button_margin_bottom" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintWidth_max="@dimen/general_max_width"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
  <androidx.compose.ui.platform.ComposeView android:id="@id/cv_coins" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0"/>
  <androidx.fragment.app.FragmentContainerView android:id="@id/fcv_chapter_finished_fragment_container" android:layout_width="match_parent" android:layout_height="match_parent"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
