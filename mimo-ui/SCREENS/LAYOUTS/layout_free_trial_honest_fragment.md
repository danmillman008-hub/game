# پروندهٔ لایه — `res/layout/free_trial_honest_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/free_trial_honest_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/free_trial_honest_fragment.xml`](../../SOURCE/res/layout/free_trial_honest_fragment.xml) |
| SHA-256 دیکد | `96b52f384269aae360287658a6b492a138ec46e40b2f24a24bb56b111e4aad42` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 24 |
| تعداد شناسه | 23 |
| تگ‌های استفاده‌شده | 10 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 7 |
| ارجاع به منابع | 57 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/cl_main
   ├─ ImageButton  #@id/ib_upgrade_modal_close
   ├─ TextView  #@id/tv_mimo_pro
   ├─ TextView  #@id/tv_title
   ├─ ScrollView  #@id/sv_main
   │  └─ androidx.constraintlayout.widget.ConstraintLayout  #@id/sv_honest_trial
   │     ├─ View
   │     ├─ ImageView  #@id/iv_arrow
   │     ├─ ImageView  #@id/iv_today
   │     ├─ TextView  #@id/tv_today
   │     ├─ ImageView  #@id/iv_unlock
   │     ├─ TextView  #@id/tv_now
   │     ├─ include  #@id/tv_now_description
   │     ├─ ImageView  #@id/iv_trial_reminder
   │     ├─ TextView  #@id/tv_trial_reminder
   │     ├─ ImageView  #@id/iv_trial_ends
   │     └─ TextView  #@id/tv_trial_ends
   ├─ ImageView  #@id/iv_one_time_offer
   ├─ LinearLayout  #@id/ll_pricing
   │  ├─ TextView  #@id/tv_yearly_price
   │  ├─ androidx.compose.ui.platform.ComposeView  #@id/mb_upgrade_modal_upgrade
   │  └─ TextView  #@id/tv_cancel_anytime
   ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_paywall
   └─ androidx.constraintlayout.widget.Group  #@id/group_content
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/cl_main` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_secondary` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:maxWidth` | `@dimen/general_max_width` |
| 7 | `ImageButton` | `android:id` | `@id/ib_upgrade_modal_close` |
| 8 | `ImageButton` | `android:background` | `?attr/selectableItemBackground` |
| 9 | `ImageButton` | `android:layout_width` | `48.000000dip` |
| 10 | `ImageButton` | `android:layout_height` | `48.000000dip` |
| 11 | `ImageButton` | `android:elevation` | `2.000000dip` |
| 12 | `ImageButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 13 | `ImageButton` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `ImageButton` | `app:srcCompat` | `@drawable/ic_close` |
| 15 | `ImageButton` | `app:tint` | `@color/icon_weak` |
| 16 | `TextView` | `android:textColor` | `@color/support_purple` |
| 17 | `TextView` | `android:id` | `@id/tv_mimo_pro` |
| 18 | `TextView` | `android:layout_width` | `wrap_content` |
| 19 | `TextView` | `android:layout_height` | `wrap_content` |
| 20 | `TextView` | `android:text` | `@string/mimo_pro` |
| 21 | `TextView` | `android:textAllCaps` | `true` |
| 22 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/ib_upgrade_modal_close` |
| 23 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 24 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 25 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/ib_upgrade_modal_close` |
| 26 | `TextView` | `style` | `@style/TextTitle` |
| 27 | `TextView` | `android:textAppearance` | `@style/TextH1` |
| 28 | `TextView` | `android:textColor` | `@color/text_primary` |
| 29 | `TextView` | `android:gravity` | `0x00000011` |
| 30 | `TextView` | `android:id` | `@id/tv_title` |
| 31 | `TextView` | `android:layout_width` | `match_parent` |
| 32 | `TextView` | `android:layout_height` | `wrap_content` |
| 33 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 34 | `TextView` | `android:text` | `@string/honest_free_trial_title` |
| 35 | `TextView` | `android:layout_marginHorizontal` | `72.000000dip` |
| 36 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/ib_upgrade_modal_close` |
| 37 | `ScrollView` | `android:id` | `@id/sv_main` |
| 38 | `ScrollView` | `android:layout_width` | `0.000000dip` |
| 39 | `ScrollView` | `android:layout_height` | `0.000000dip` |
| 40 | `ScrollView` | `android:maxWidth` | `@dimen/general_max_width` |
| 41 | `ScrollView` | `app:layout_constraintBottom_toTopOf` | `@id/iv_one_time_offer` |
| 42 | `ScrollView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 43 | `ScrollView` | `app:layout_constraintStart_toStartOf` | `0` |
| 44 | `ScrollView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_title` |
| 45 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/sv_honest_trial` |
| 46 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 47 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 48 | `View` | `android:background` | `@color/line_secondary` |
| 49 | `View` | `android:layout_width` | `4.000000dip` |
| 50 | `View` | `android:layout_height` | `0.000000dip` |
| 51 | `View` | `android:layout_marginBottom` | `2.000000dip` |
| 52 | `View` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_arrow` |
| 53 | `View` | `app:layout_constraintEnd_toEndOf` | `@id/iv_today` |
| 54 | `View` | `app:layout_constraintStart_toStartOf` | `@id/iv_today` |
| 55 | `View` | `app:layout_constraintTop_toBottomOf` | `@id/iv_today` |
| 56 | `ImageView` | `android:id` | `@id/iv_arrow` |
| 57 | `ImageView` | `android:layout_width` | `wrap_content` |
| 58 | `ImageView` | `android:layout_height` | `wrap_content` |
| 59 | `ImageView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 60 | `ImageView` | `android:src` | `@drawable/honest_free_trial_arrow` |
| 61 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `@id/iv_today` |
| 62 | `ImageView` | `app:layout_constraintStart_toStartOf` | `@id/iv_today` |
| 63 | `ImageView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_trial_ends` |
| 64 | `ImageView` | `app:tint` | `@color/line_secondary` |
| 65 | `ImageView` | `android:id` | `@id/iv_today` |
| 66 | `ImageView` | `android:layout_width` | `48.000000dip` |
| 67 | `ImageView` | `android:layout_height` | `48.000000dip` |
| 68 | `ImageView` | `android:src` | `@drawable/honest_free_trial_today` |
| 69 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_xl` |
| 70 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/tv_today` |
| 71 | `ImageView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_today` |
| 72 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 73 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_today` |
| 74 | `TextView` | `android:textAppearance` | `@style/TextH4` |
| 75 | `TextView` | `android:textStyle` | `0x00000000` |
| 76 | `TextView` | `android:textColor` | `@color/text_primary` |
| 77 | `TextView` | `android:id` | `@id/tv_today` |
| 78 | `TextView` | `android:layout_width` | `0.000000dip` |
| 79 | `TextView` | `android:layout_height` | `wrap_content` |
| 80 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 81 | `TextView` | `android:text` | `@string/honest_free_trial_first_step` |
| 82 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 83 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xl` |
| 84 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 85 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_today` |
| 86 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 87 | `ImageView` | `android:id` | `@id/iv_unlock` |
| 88 | `ImageView` | `android:layout_width` | `48.000000dip` |
| 89 | `ImageView` | `android:layout_height` | `48.000000dip` |
| 90 | `ImageView` | `android:src` | `@drawable/honest_free_trial_unlock` |
| 91 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_xl` |
| 92 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/tv_now` |
| 93 | `ImageView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_now` |
| 94 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 95 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_now` |
| 96 | `TextView` | `android:textAppearance` | `@style/TextH4` |
| 97 | `TextView` | `android:textColor` | `@color/text_primary` |
| 98 | `TextView` | `android:id` | `@id/tv_now` |
| 99 | `TextView` | `android:layout_width` | `0.000000dip` |
| 100 | `TextView` | `android:layout_height` | `wrap_content` |
| 101 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xxl` |
| 102 | `TextView` | `android:text` | `@string/honest_free_trial_now` |
| 103 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 104 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xl` |
| 105 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 106 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_unlock` |
| 107 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_today` |
| 108 | `include` | `android:id` | `@id/tv_now_description` |
| 109 | `include` | `android:layout_width` | `0.000000dip` |
| 110 | `include` | `android:layout_height` | `wrap_content` |
| 111 | `include` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 112 | `include` | `android:layout_marginEnd` | `@dimen/spacing_xl` |
| 113 | `include` | `app:layout_constraintEnd_toEndOf` | `0` |
| 114 | `include` | `app:layout_constraintStart_toStartOf` | `@id/tv_now` |
| 115 | `include` | `app:layout_constraintTop_toBottomOf` | `@id/tv_now` |
| 116 | `include` | `layout` | `@layout/differences_between_free_and_pro_layout` |
| 117 | `ImageView` | `android:id` | `@id/iv_trial_reminder` |
| 118 | `ImageView` | `android:layout_width` | `48.000000dip` |
| 119 | `ImageView` | `android:layout_height` | `48.000000dip` |
| 120 | `ImageView` | `android:src` | `@drawable/honest_free_trial_bell` |
| 121 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_xl` |
| 122 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/tv_trial_reminder` |
| 123 | `ImageView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_trial_reminder` |
| 124 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 125 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_trial_reminder` |
| 126 | `TextView` | `android:textAppearance` | `@style/TextH4` |
| 127 | `TextView` | `android:textColor` | `@color/text_primary` |
| 128 | `TextView` | `android:id` | `@id/tv_trial_reminder` |
| 129 | `TextView` | `android:layout_width` | `0.000000dip` |
| 130 | `TextView` | `android:layout_height` | `wrap_content` |
| 131 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xxl` |
| 132 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 133 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xl` |
| 134 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 135 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_trial_reminder` |
| 136 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_now_description` |
| 137 | `ImageView` | `android:id` | `@id/iv_trial_ends` |
| 138 | `ImageView` | `android:layout_width` | `48.000000dip` |
| 139 | `ImageView` | `android:layout_height` | `48.000000dip` |
| 140 | `ImageView` | `android:src` | `@drawable/honest_free_trial_rocket` |
| 141 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_xl` |
| 142 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/tv_trial_ends` |
| 143 | `ImageView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_trial_ends` |
| 144 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 145 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/tv_trial_ends` |
| 146 | `TextView` | `android:textAppearance` | `@style/TextH4` |
| 147 | `TextView` | `android:textColor` | `@color/text_primary` |
| 148 | `TextView` | `android:id` | `@id/tv_trial_ends` |
| 149 | `TextView` | `android:layout_width` | `0.000000dip` |
| 150 | `TextView` | `android:layout_height` | `wrap_content` |
| 151 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xxl` |
| 152 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 153 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xl` |
| 154 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 155 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_trial_ends` |
| 156 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_trial_reminder` |
| 157 | `ImageView` | `android:id` | `@id/iv_one_time_offer` |
| 158 | `ImageView` | `android:layout_width` | `177.000000dip` |
| 159 | `ImageView` | `android:layout_height` | `43.000000dip` |
| 160 | `ImageView` | `android:src` | `@drawable/one_time_offer` |
| 161 | `ImageView` | `android:elevation` | `2.000000dip` |
| 162 | `ImageView` | `app:layout_constraintBottom_toTopOf` | `@id/ll_pricing` |
| 163 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 164 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 165 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/ll_pricing` |
| 166 | `LinearLayout` | `android:orientation` | `vertical` |
| 167 | `LinearLayout` | `android:id` | `@id/ll_pricing` |
| 168 | `LinearLayout` | `android:background` | `@color/background_primary` |
| 169 | `LinearLayout` | `android:layout_width` | `0.000000dip` |
| 170 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 171 | `LinearLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 172 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 173 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 174 | `TextView` | `android:textColor` | `@color/text_primary` |
| 175 | `TextView` | `android:gravity` | `0x00000011` |
| 176 | `TextView` | `android:id` | `@id/tv_yearly_price` |
| 177 | `TextView` | `android:layout_width` | `match_parent` |
| 178 | `TextView` | `android:layout_height` | `wrap_content` |
| 179 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 180 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 181 | `TextView` | `style` | `@style/TextP1` |
| 182 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/mb_upgrade_modal_upgrade` |
| 183 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 184 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 185 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 186 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_s` |
| 187 | `TextView` | `android:textAppearance` | `@style/TextP2` |
| 188 | `TextView` | `android:textColor` | `@color/text_weak` |
| 189 | `TextView` | `android:gravity` | `0x00000011` |
| 190 | `TextView` | `android:id` | `@id/tv_cancel_anytime` |
| 191 | `TextView` | `android:layout_width` | `match_parent` |
| 192 | `TextView` | `android:layout_height` | `wrap_content` |
| 193 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 194 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_s` |
| 195 | `TextView` | `android:text` | `@string/free_trial_bottom_cancel_anytime` |
| 196 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cv_paywall` |
| 197 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 198 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 199 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `0.000000dip` |
| 200 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 201 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 202 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 203 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toTopOf` | `0` |
| 204 | `androidx.constraintlayout.widget.Group` | `android:id` | `@id/group_content` |
| 205 | `androidx.constraintlayout.widget.Group` | `android:visibility` | `visible` |
| 206 | `androidx.constraintlayout.widget.Group` | `android:layout_width` | `@dimen/general_margin_10dp` |
| 207 | `androidx.constraintlayout.widget.Group` | `android:layout_height` | `wrap_content` |
| 208 | `androidx.constraintlayout.widget.Group` | `app:constraint_referenced_ids` | `ll_pricing,iv_one_time_offer,sv_main,tv_title,tv_mimo_pro,ib_upgrade_modal_close,` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/line_secondary` | `#FFE4E6F1` / `#FF4A4D85` (night) |
| `@color/support_purple` | `#FF7E4BDE` / `#FFB99AF4` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/general_margin_10dp` | `10.000000dip` / `12.500001dip` (sw600dp) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxl` | `40.000000dip` |
| `@string/free_trial_bottom_cancel_anytime` | `Cancel anytime in the Play Store` / `Kündige jederzeit im Play Store` (de) / `Cancela en cualquier momento en Play Store` (es) / `Annuler à tout moment sur Play Store` (fr) / `Batalkan kapan saja di Play Store` (in) / `Disdici quando vuoi nel Play Store` (it) / `Anuluj w każdej chwili w Play Store` (pl) / `Cancele a qualquer momento na Play Store` (pt-rBR) / `Отмени в любой момент в Play Store` (ru) / `Play Store'dan istediğin zaman iptal et` (tr) |
| `@string/honest_free_trial_first_step` | `You’ve taken the first step` / `Du hast den ersten Schritt gemacht` (de) / `Has hecho el primer paso` (es) / `Tu as fait le premier pas` (fr) / `Kamu sudah ambil langkah pertama` (in) / `Hai fatto il primo passo` (it) / `Pierwszy krok masz za sobą` (pl) / `Você deu o primeiro passo` (pt-rBR) / `Ты сделал(а) первый шаг` (ru) / `İlk adımı attın` (tr) |
| `@string/honest_free_trial_now` | `Now: Start %d days free trial` / `Starte deine %d-tägige Testphase jetzt` (de) / `Ahora: Empieza %d días de prueba gratis` (es) / `Maintenant : Commence ton essai gratuit de %d jours` (fr) / `Sekarang: Mulai uji coba gratis %d hari` (in) / `Ora: inizia la prova gratuita di %d giorni` (it) / `Teraz: start %d-dniowego okresu próbnego` (pl) / `Agora: Comece seus %d dias de teste gratuito` (pt-rBR) / `Теперь: Начни %d-дневную бесплатную пробную версию` (ru) / `Şimdi: %d günlük ücretsiz denemeyi başlat` (tr) |
| `@string/honest_free_trial_title` | `How the trial works` / `Wie die Probephase funktioniert` (de) / `Cómo funciona el período grautito` (es) / `Comment fonctionne l'essai` (fr) / `Cara kerja uji coba` (in) / `Come funziona la prova` (it) / `Jak działa okres próbny` (pl) / `Como funciona seu teste gratuito` (pt-rBR) / `Как работает пробный период` (ru) / `Deneme nasıl işliyor` (tr) |
| `@string/mimo_pro` | `Mimo Pro` / `Mimo Pro` (de) / `Mimo Pro` (es) / `Mimo Pro` (fr) / `Mimo Pro` (in) / `Mimo Pro` (it) / `Mimo Pro` (pl) / `Mimo Pro` (pt-rBR) / `Mimo Pro` (ru) / `Mimo Pro` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextH4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '11.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '17.500002sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'android:textAllCaps', 'attr_id': '0x0101038C', 'value': 'true', 'value_type': 'int_boolean'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/cl_main
@id/cv_paywall
@id/group_content
@id/ib_upgrade_modal_close
@id/iv_arrow
@id/iv_one_time_offer
@id/iv_today
@id/iv_trial_ends
@id/iv_trial_reminder
@id/iv_unlock
@id/ll_pricing
@id/mb_upgrade_modal_upgrade
@id/sv_honest_trial
@id/sv_main
@id/tv_cancel_anytime
@id/tv_mimo_pro
@id/tv_now
@id/tv_now_description
@id/tv_title
@id/tv_today
@id/tv_trial_ends
@id/tv_trial_reminder
@id/tv_yearly_price
```

## ۵. ارجاع به لایه‌های دیگر

```text
0
0.000000dip
@dimen/spacing_xl
@dimen/spacing_xs
@id/tv_now
@layout/differences_between_free_and_pro_layout
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.iap.freetrial.HonestFreeTrialFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000011" android:id="@id/cl_main" android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="match_parent" android:maxWidth="@dimen/general_max_width">
  <ImageButton android:id="@id/ib_upgrade_modal_close" android:background="?attr/selectableItemBackground" android:layout_width="48.000000dip" android:layout_height="48.000000dip" android:elevation="2.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_close" app:tint="@color/icon_weak"/>
  <TextView android:textColor="@color/support_purple" android:id="@id/tv_mimo_pro" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/mimo_pro" android:textAllCaps="true" app:layout_constraintBottom_toBottomOf="@id/ib_upgrade_modal_close" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/ib_upgrade_modal_close" style="@style/TextTitle"/>
  <TextView android:textAppearance="@style/TextH1" android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_title" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/honest_free_trial_title" android:layout_marginHorizontal="72.000000dip" app:layout_constraintTop_toBottomOf="@id/ib_upgrade_modal_close"/>
  <ScrollView android:id="@id/sv_main" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:maxWidth="@dimen/general_max_width" app:layout_constraintBottom_toTopOf="@id/iv_one_time_offer" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_title">
    <androidx.constraintlayout.widget.ConstraintLayout android:id="@id/sv_honest_trial" android:layout_width="match_parent" android:layout_height="wrap_content">
      <View android:background="@color/line_secondary" android:layout_width="4.000000dip" android:layout_height="0.000000dip" android:layout_marginBottom="2.000000dip" app:layout_constraintBottom_toBottomOf="@id/iv_arrow" app:layout_constraintEnd_toEndOf="@id/iv_today" app:layout_constraintStart_toStartOf="@id/iv_today" app:layout_constraintTop_toBottomOf="@id/iv_today"/>
      <ImageView android:id="@id/iv_arrow" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:src="@drawable/honest_free_trial_arrow" app:layout_constraintEnd_toEndOf="@id/iv_today" app:layout_constraintStart_toStartOf="@id/iv_today" app:layout_constraintTop_toBottomOf="@id/tv_trial_ends" app:tint="@color/line_secondary"/>
      <ImageView android:id="@id/iv_today" android:layout_width="48.000000dip" android:layout_height="48.000000dip" android:src="@drawable/honest_free_trial_today" android:layout_marginStart="@dimen/spacing_xl" app:layout_constraintBottom_toBottomOf="@id/tv_today" app:layout_constraintEnd_toStartOf="@id/tv_today" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/tv_today"/>
      <TextView android:textAppearance="@style/TextH4" android:textStyle="0x00000000" android:textColor="@color/text_primary" android:id="@id/tv_today" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/honest_free_trial_first_step" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_xl" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/iv_today" app:layout_constraintTop_toTopOf="0"/>
      <ImageView android:id="@id/iv_unlock" android:layout_width="48.000000dip" android:layout_height="48.000000dip" android:src="@drawable/honest_free_trial_unlock" android:layout_marginStart="@dimen/spacing_xl" app:layout_constraintBottom_toBottomOf="@id/tv_now" app:layout_constraintEnd_toStartOf="@id/tv_now" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/tv_now"/>
      <TextView android:textAppearance="@style/TextH4" android:textColor="@color/text_primary" android:id="@id/tv_now" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xxl" android:text="@string/honest_free_trial_now" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_xl" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/iv_unlock" app:layout_constraintTop_toBottomOf="@id/tv_today"/>
      <include android:id="@id/tv_now_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginEnd="@dimen/spacing_xl" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="@id/tv_now" app:layout_constraintTop_toBottomOf="@id/tv_now" layout="@layout/differences_between_free_and_pro_layout"/>
      <ImageView android:id="@id/iv_trial_reminder" android:layout_width="48.000000dip" android:layout_height="48.000000dip" android:src="@drawable/honest_free_trial_bell" android:layout_marginStart="@dimen/spacing_xl" app:layout_constraintBottom_toBottomOf="@id/tv_trial_reminder" app:layout_constraintEnd_toStartOf="@id/tv_trial_reminder" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/tv_trial_reminder"/>
      <TextView android:textAppearance="@style/TextH4" android:textColor="@color/text_primary" android:id="@id/tv_trial_reminder" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xxl" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_xl" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/iv_trial_reminder" app:layout_constraintTop_toBottomOf="@id/tv_now_description"/>
      <ImageView android:id="@id/iv_trial_ends" android:layout_width="48.000000dip" android:layout_height="48.000000dip" android:src="@drawable/honest_free_trial_rocket" android:layout_marginStart="@dimen/spacing_xl" app:layout_constraintBottom_toBottomOf="@id/tv_trial_ends" app:layout_constraintEnd_toStartOf="@id/tv_trial_ends" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/tv_trial_ends"/>
      <TextView android:textAppearance="@style/TextH4" android:textColor="@color/text_primary" android:id="@id/tv_trial_ends" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xxl" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_xl" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/iv_trial_ends" app:layout_constraintTop_toBottomOf="@id/tv_trial_reminder"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </ScrollView>
  <ImageView android:id="@id/iv_one_time_offer" android:layout_width="177.000000dip" android:layout_height="43.000000dip" android:src="@drawable/one_time_offer" android:elevation="2.000000dip" app:layout_constraintBottom_toTopOf="@id/ll_pricing" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/ll_pricing"/>
  <LinearLayout android:orientation="vertical" android:id="@id/ll_pricing" android:background="@color/background_primary" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0">
    <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_yearly_price" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:layout_marginHorizontal="@dimen/spacing_l" style="@style/TextP1"/>
    <androidx.compose.ui.platform.ComposeView android:id="@id/mb_upgrade_modal_upgrade" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_marginHorizontal="@dimen/spacing_s"/>
    <TextView android:textAppearance="@style/TextP2" android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_cancel_anytime" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_marginBottom="@dimen/spacing_s" android:text="@string/free_trial_bottom_cancel_anytime"/>
  </LinearLayout>
  <androidx.compose.ui.platform.ComposeView android:id="@id/cv_paywall" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <androidx.constraintlayout.widget.Group android:id="@id/group_content" android:visibility="visible" android:layout_width="@dimen/general_margin_10dp" android:layout_height="wrap_content" app:constraint_referenced_ids="ll_pricing,iv_one_time_offer,sv_main,tv_title,tv_mimo_pro,ib_upgrade_modal_close,"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
