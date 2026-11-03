# پروندهٔ لایه — `res/layout/chapter_end_native_ads_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/chapter_end_native_ads_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/chapter_end_native_ads_fragment.xml`](../../SOURCE/res/layout/chapter_end_native_ads_fragment.xml) |
| SHA-256 دیکد | `52da6f1cbcc8d96394d4afae28dc9bcc5612ca3f88101ac79601cb395aba7b6d` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 19 |
| تعداد شناسه | 17 |
| تگ‌های استفاده‌شده | 12 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 44 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_ads_modal_title
   ├─ com.google.android.material.progressindicator.CircularProgressIndicator  #@id/cpi_countdown_timer
   ├─ TextView  #@id/tv_seconds_timer_close
   ├─ ImageButton  #@id/iv_ads_modal_close
   ├─ TextView  #@id/tv_ads_keep_mimo_free
   ├─ TextView  #@id/tv_subscribe_to_mimo_pro
   ├─ androidx.cardview.widget.CardView  #@id/card_view_ads_modal_content
   │  └─ com.google.android.gms.ads.nativead.NativeAdView  #@id/layout_adview
   │     └─ androidx.constraintlayout.widget.ConstraintLayout
   │        ├─ com.google.android.gms.ads.nativead.MediaView  #@id/mv_ads_modal_content
   │        ├─ ImageView  #@id/iv_ads_modal_content
   │        ├─ ImageView  #@id/iv_ads_modal_content_app_icon
   │        ├─ TextView  #@id/tv_ads_modal_content_title
   │        ├─ TextView  #@id/tv_ads_modal_content_description
   │        └─ com.google.android.material.button.MaterialButton  #@id/btn_cta
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_ads_modal_remove_ads
   └─ FrameLayout  #@id/layout_loading_ad
      └─ ProgressBar  #@id/progress_bar_loading_ads
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `TextView` | `android:textColor` | `@color/support_purple` |
| 5 | `TextView` | `android:gravity` | `0x00000011` |
| 6 | `TextView` | `android:id` | `@id/tv_ads_modal_title` |
| 7 | `TextView` | `android:layout_width` | `0.000000dip` |
| 8 | `TextView` | `android:layout_height` | `wrap_content` |
| 9 | `TextView` | `android:text` | `@string/chapter_end_native_ads_title` |
| 10 | `TextView` | `android:textAllCaps` | `true` |
| 11 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_ads_modal_close` |
| 12 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 13 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 14 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/iv_ads_modal_close` |
| 15 | `TextView` | `style` | `@style/TextLabel1` |
| 16 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_gravity` | `0x00000011` |
| 17 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:id` | `@id/cpi_countdown_timer` |
| 18 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_width` | `45.000000dip` |
| 19 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_height` | `45.000000dip` |
| 20 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 21 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:max` | `1000` |
| 22 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_marginEnd` | `@dimen/spacing_s` |
| 23 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:indicatorColor` | `@color/progress_primary` |
| 24 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:indicatorDirectionCircular` | `1` |
| 25 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:indicatorInset` | `0.000000dip` |
| 26 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:indicatorSize` | `45.000000dip` |
| 27 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:layout_constraintEnd_toEndOf` | `0` |
| 28 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:layout_constraintTop_toTopOf` | `0` |
| 29 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:trackColor` | `@color/transparent` |
| 30 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:trackCornerRadius` | `4.000000dip` |
| 31 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:trackThickness` | `4.000000dip` |
| 32 | `TextView` | `android:textColor` | `@color/text_primary` |
| 33 | `TextView` | `android:gravity` | `0x00000011` |
| 34 | `TextView` | `android:id` | `@id/tv_seconds_timer_close` |
| 35 | `TextView` | `android:layout_width` | `wrap_content` |
| 36 | `TextView` | `android:layout_height` | `wrap_content` |
| 37 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/cpi_countdown_timer` |
| 38 | `TextView` | `app:layout_constraintEnd_toEndOf` | `@id/cpi_countdown_timer` |
| 39 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/cpi_countdown_timer` |
| 40 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/cpi_countdown_timer` |
| 41 | `TextView` | `style` | `@style/TextH4` |
| 42 | `ImageButton` | `android:id` | `@id/iv_ads_modal_close` |
| 43 | `ImageButton` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 44 | `ImageButton` | `android:padding` | `@dimen/spacing_s` |
| 45 | `ImageButton` | `android:visibility` | `invisible` |
| 46 | `ImageButton` | `android:layout_width` | `wrap_content` |
| 47 | `ImageButton` | `android:layout_height` | `wrap_content` |
| 48 | `ImageButton` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 49 | `ImageButton` | `android:layout_marginEnd` | `@dimen/spacing_s` |
| 50 | `ImageButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 51 | `ImageButton` | `app:layout_constraintTop_toTopOf` | `0` |
| 52 | `ImageButton` | `app:srcCompat` | `@drawable/ic_close` |
| 53 | `ImageButton` | `app:tint` | `@color/icon_weak` |
| 54 | `TextView` | `android:textColor` | `@color/text_primary` |
| 55 | `TextView` | `android:gravity` | `0x00000011` |
| 56 | `TextView` | `android:id` | `@id/tv_ads_keep_mimo_free` |
| 57 | `TextView` | `android:layout_width` | `0.000000dip` |
| 58 | `TextView` | `android:layout_height` | `wrap_content` |
| 59 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 60 | `TextView` | `android:text` | `@string/ads_keep_mimo_free` |
| 61 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 62 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 63 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 64 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_ads_modal_close` |
| 65 | `TextView` | `style` | `@style/TextH1` |
| 66 | `TextView` | `android:textColor` | `@color/text_weak` |
| 67 | `TextView` | `android:gravity` | `0x00000011` |
| 68 | `TextView` | `android:id` | `@id/tv_subscribe_to_mimo_pro` |
| 69 | `TextView` | `android:layout_width` | `0.000000dip` |
| 70 | `TextView` | `android:layout_height` | `wrap_content` |
| 71 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 72 | `TextView` | `android:text` | `@string/subscribe_to_mimo_pro_remove_all_ads` |
| 73 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_l` |
| 74 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 75 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 76 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_ads_keep_mimo_free` |
| 77 | `TextView` | `style` | `@style/TextP1` |
| 78 | `androidx.cardview.widget.CardView` | `android:id` | `@id/card_view_ads_modal_content` |
| 79 | `androidx.cardview.widget.CardView` | `android:clipChildren` | `false` |
| 80 | `androidx.cardview.widget.CardView` | `android:clipToPadding` | `false` |
| 81 | `androidx.cardview.widget.CardView` | `android:layout_width` | `0.000000dip` |
| 82 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 83 | `androidx.cardview.widget.CardView` | `android:layout_margin` | `5.000000dip` |
| 84 | `androidx.cardview.widget.CardView` | `android:foreground` | `?attr/selectableItemBackground` |
| 85 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@color/card_enabled` |
| 86 | `androidx.cardview.widget.CardView` | `app:cardCornerRadius` | `12.000000dip` |
| 87 | `androidx.cardview.widget.CardView` | `app:layout_constrainedWidth` | `true` |
| 88 | `androidx.cardview.widget.CardView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_ads_modal_remove_ads` |
| 89 | `androidx.cardview.widget.CardView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 90 | `androidx.cardview.widget.CardView` | `app:layout_constraintStart_toStartOf` | `0` |
| 91 | `androidx.cardview.widget.CardView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_ads_modal_title` |
| 92 | `androidx.cardview.widget.CardView` | `app:layout_constraintWidth_max` | `328.000000dip` |
| 93 | `com.google.android.gms.ads.nativead.NativeAdView` | `android:id` | `@id/layout_adview` |
| 94 | `com.google.android.gms.ads.nativead.NativeAdView` | `android:clipChildren` | `false` |
| 95 | `com.google.android.gms.ads.nativead.NativeAdView` | `android:clipToPadding` | `false` |
| 96 | `com.google.android.gms.ads.nativead.NativeAdView` | `android:layout_width` | `match_parent` |
| 97 | `com.google.android.gms.ads.nativead.NativeAdView` | `android:layout_height` | `wrap_content` |
| 98 | `com.google.android.gms.ads.nativead.NativeAdView` | `android:foreground` | `?attr/selectableItemBackground` |
| 99 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 100 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 101 | `com.google.android.gms.ads.nativead.MediaView` | `android:id` | `@id/mv_ads_modal_content` |
| 102 | `com.google.android.gms.ads.nativead.MediaView` | `android:visibility` | `gone` |
| 103 | `com.google.android.gms.ads.nativead.MediaView` | `android:layout_width` | `match_parent` |
| 104 | `com.google.android.gms.ads.nativead.MediaView` | `android:layout_height` | `wrap_content` |
| 105 | `com.google.android.gms.ads.nativead.MediaView` | `android:adjustViewBounds` | `true` |
| 106 | `com.google.android.gms.ads.nativead.MediaView` | `app:layout_constrainedHeight` | `true` |
| 107 | `com.google.android.gms.ads.nativead.MediaView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 108 | `com.google.android.gms.ads.nativead.MediaView` | `app:layout_constraintHeight_max` | `246.000000dip` |
| 109 | `com.google.android.gms.ads.nativead.MediaView` | `app:layout_constraintStart_toStartOf` | `0` |
| 110 | `com.google.android.gms.ads.nativead.MediaView` | `app:layout_constraintTop_toTopOf` | `0` |
| 111 | `ImageView` | `android:id` | `@id/iv_ads_modal_content` |
| 112 | `ImageView` | `android:layout_width` | `match_parent` |
| 113 | `ImageView` | `android:layout_height` | `wrap_content` |
| 114 | `ImageView` | `android:adjustViewBounds` | `true` |
| 115 | `ImageView` | `app:layout_constrainedHeight` | `true` |
| 116 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 117 | `ImageView` | `app:layout_constraintHeight_max` | `246.000000dip` |
| 118 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 119 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 120 | `ImageView` | `android:id` | `@id/iv_ads_modal_content_app_icon` |
| 121 | `ImageView` | `android:visibility` | `gone` |
| 122 | `ImageView` | `android:layout_width` | `56.000000dip` |
| 123 | `ImageView` | `android:layout_height` | `56.000000dip` |
| 124 | `ImageView` | `android:layout_marginTop` | `16.000000dip` |
| 125 | `ImageView` | `android:layout_marginBottom` | `34.000000dip` |
| 126 | `ImageView` | `android:layout_marginStart` | `16.000000dip` |
| 127 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 128 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 129 | `ImageView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_ads_modal_content` |
| 130 | `ImageView` | `app:layout_constraintVertical_bias` | `0.000000` |
| 131 | `TextView` | `android:textColor` | `@color/text_primary` |
| 132 | `TextView` | `android:id` | `@id/tv_ads_modal_content_title` |
| 133 | `TextView` | `android:layout_width` | `0.000000dip` |
| 134 | `TextView` | `android:layout_height` | `wrap_content` |
| 135 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 136 | `TextView` | `android:layout_marginBottom` | `6.000000dip` |
| 137 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 138 | `TextView` | `android:layout_marginEnd` | `16.000000dip` |
| 139 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_ads_modal_content_description` |
| 140 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 141 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_ads_modal_content_app_icon` |
| 142 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_ads_modal_content` |
| 143 | `TextView` | `style` | `@style/TextH2` |
| 144 | `TextView` | `android:textColor` | `@color/text_weak` |
| 145 | `TextView` | `android:id` | `@id/tv_ads_modal_content_description` |
| 146 | `TextView` | `android:visibility` | `gone` |
| 147 | `TextView` | `android:layout_width` | `0.000000dip` |
| 148 | `TextView` | `android:layout_height` | `wrap_content` |
| 149 | `TextView` | `android:layout_marginEnd` | `16.000000dip` |
| 150 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/btn_cta` |
| 151 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 152 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/tv_ads_modal_content_title` |
| 153 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_ads_modal_content_title` |
| 154 | `TextView` | `app:layout_constraintVertical_bias` | `0.000000` |
| 155 | `TextView` | `style` | `@style/TextP2` |
| 156 | `com.google.android.material.button.MaterialButton` | `android:id` | `@id/btn_cta` |
| 157 | `com.google.android.material.button.MaterialButton` | `android:focusable` | `false` |
| 158 | `com.google.android.material.button.MaterialButton` | `android:clickable` | `false` |
| 159 | `com.google.android.material.button.MaterialButton` | `android:layout_width` | `0.000000dip` |
| 160 | `com.google.android.material.button.MaterialButton` | `android:layout_height` | `40.000000dip` |
| 161 | `com.google.android.material.button.MaterialButton` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 162 | `com.google.android.material.button.MaterialButton` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 163 | `com.google.android.material.button.MaterialButton` | `android:text` | `@string/view_components_button_primary` |
| 164 | `com.google.android.material.button.MaterialButton` | `android:layout_marginStart` | `@dimen/spacing_s` |
| 165 | `com.google.android.material.button.MaterialButton` | `android:layout_marginEnd` | `@dimen/spacing_s` |
| 166 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 167 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 168 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintStart_toStartOf` | `0` |
| 169 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintTop_toBottomOf` | `@id/tv_ads_modal_content_description` |
| 170 | `com.google.android.material.button.MaterialButton` | `style` | `@style/MaterialButton.Primary` |
| 171 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_ads_modal_remove_ads` |
| 172 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 173 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 174 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_xl` |
| 175 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_s` |
| 176 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 177 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 178 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 179 | `FrameLayout` | `android:id` | `@id/layout_loading_ad` |
| 180 | `FrameLayout` | `android:background` | `@color/background_primary` |
| 181 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 182 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 183 | `ProgressBar` | `android:layout_gravity` | `0x00000011` |
| 184 | `ProgressBar` | `android:id` | `@id/progress_bar_loading_ads` |
| 185 | `ProgressBar` | `android:layout_width` | `64.000000dip` |
| 186 | `ProgressBar` | `android:layout_height` | `64.000000dip` |
| 187 | `ProgressBar` | `android:elevation` | `2.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/card_enabled` | `#FFFFFFFF` / `#FF3F4273` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/progress_primary` | `#FF7E4BDE` / `#FFA175EA` (night) |
| `@color/support_purple` | `#FF7E4BDE` / `#FFB99AF4` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@color/transparent` | `#00000000` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@string/ads_keep_mimo_free` | `Ads help keep Mimo free` / `Werbungen helfen, Mimo gratis zu halten` (de) / `Los anuncios nos ayudan a mantener Mimo gratis` (es) / `Les pubs aident à garder Mimo gratuit` (fr) / `Iklan membantu Mimo tetap gratis` (in) / `Le pubblicità aiutano a mantenere Mimo gratuito` (it) / `Reklamy pomagają utrzymać Mimo za darmo` (pl) / `Anúncios ajudam a manter Mimo grátis` (pt-rBR) / `Реклама помогает Mimo оставаться бесплатным` (ru) / `Reklamlar Mimo'yu ücretsiz tutar` (tr) |
| `@string/chapter_end_native_ads_title` | `Advertisement` / `Werbung` (de) / `Anuncio` (es) / `Publicité` (fr) / `Iklan` (in) / `Pubblicità` (it) / `Reklama` (pl) / `Anúncio` (pt-rBR) / `Реклама` (ru) / `Reklam` (tr) |
| `@string/subscribe_to_mimo_pro_remove_all_ads` | `Subscribe to Mimo Pro to remove all ads and learn without distractions` / `Abonniere Mimo Pro, um Werbungen zu entfernen und ohne Ablenkungen zu lernen` (de) / `Suscríbete a Mimo Pro para eliminar todos los anuncios y aprender sin distracciones` (es) / `Abonne-toi à Mimo Pro pour supprimer toutes les pubs et apprendre sans distractions` (fr) / `Langganan Mimo Pro untuk menghapus semua iklan dan belajar tanpa gangguan` (in) / `Abbonati a Mimo Pro per rimuovere le pubblicità e imparare senza distrazioni` (it) / `Wykup Mimo Pro, aby usunąć wszystkie reklamy i uczyć się bez rozproszeń` (pl) / `Assine Mimo Pro para remover todos os anúncios e aprenda sem distrações` (pt-rBR) / `Купи подписку Mimo Pro, чтобы учиться, не отвлекаясь на рекламу` (ru) / `Tüm reklamları kaldırmak ve dikkatin dağılmadan öğrenmek için Mimo Pro'ya abone ol` (tr) |
| `@string/view_components_button_primary` | `Primary` |
| `@style/MaterialButton.Primary` | `[]` |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextH2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '26.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextH4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '11.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_ads_modal_remove_ads
@id/btn_cta
@id/card_view_ads_modal_content
@id/cpi_countdown_timer
@id/iv_ads_modal_close
@id/iv_ads_modal_content
@id/iv_ads_modal_content_app_icon
@id/layout_adview
@id/layout_loading_ad
@id/mv_ads_modal_content
@id/progress_bar_loading_ads
@id/tv_ads_keep_mimo_free
@id/tv_ads_modal_content_description
@id/tv_ads_modal_content_title
@id/tv_ads_modal_title
@id/tv_seconds_timer_close
@id/tv_subscribe_to_mimo_pro
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.chapter.ChapterActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <TextView android:textColor="@color/support_purple" android:gravity="0x00000011" android:id="@id/tv_ads_modal_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:text="@string/chapter_end_native_ads_title" android:textAllCaps="true" app:layout_constraintBottom_toBottomOf="@id/iv_ads_modal_close" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/iv_ads_modal_close" style="@style/TextLabel1"/>
  <com.google.android.material.progressindicator.CircularProgressIndicator android:layout_gravity="0x00000011" android:id="@id/cpi_countdown_timer" android:layout_width="45.000000dip" android:layout_height="45.000000dip" android:layout_marginTop="@dimen/spacing_m" android:max="1000" android:layout_marginEnd="@dimen/spacing_s" app:indicatorColor="@color/progress_primary" app:indicatorDirectionCircular="1" app:indicatorInset="0.000000dip" app:indicatorSize="45.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:trackColor="@color/transparent" app:trackCornerRadius="4.000000dip" app:trackThickness="4.000000dip"/>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_seconds_timer_close" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="@id/cpi_countdown_timer" app:layout_constraintEnd_toEndOf="@id/cpi_countdown_timer" app:layout_constraintStart_toStartOf="@id/cpi_countdown_timer" app:layout_constraintTop_toTopOf="@id/cpi_countdown_timer" style="@style/TextH4"/>
  <ImageButton android:id="@id/iv_ads_modal_close" android:background="?attr/selectableItemBackgroundBorderless" android:padding="@dimen/spacing_s" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_s" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_close" app:tint="@color/icon_weak"/>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_ads_keep_mimo_free" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:text="@string/ads_keep_mimo_free" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_ads_modal_close" style="@style/TextH1"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000011" android:id="@id/tv_subscribe_to_mimo_pro" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:text="@string/subscribe_to_mimo_pro_remove_all_ads" android:layout_marginHorizontal="@dimen/spacing_l" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_ads_keep_mimo_free" style="@style/TextP1"/>
  <androidx.cardview.widget.CardView android:id="@id/card_view_ads_modal_content" android:clipChildren="false" android:clipToPadding="false" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_margin="5.000000dip" android:foreground="?attr/selectableItemBackground" app:cardBackgroundColor="@color/card_enabled" app:cardCornerRadius="12.000000dip" app:layout_constrainedWidth="true" app:layout_constraintBottom_toTopOf="@id/btn_ads_modal_remove_ads" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_ads_modal_title" app:layout_constraintWidth_max="328.000000dip">
    <com.google.android.gms.ads.nativead.NativeAdView android:id="@id/layout_adview" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content" android:foreground="?attr/selectableItemBackground">
      <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content">
        <com.google.android.gms.ads.nativead.MediaView android:id="@id/mv_ads_modal_content" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content" android:adjustViewBounds="true" app:layout_constrainedHeight="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintHeight_max="246.000000dip" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
        <ImageView android:id="@id/iv_ads_modal_content" android:layout_width="match_parent" android:layout_height="wrap_content" android:adjustViewBounds="true" app:layout_constrainedHeight="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintHeight_max="246.000000dip" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
        <ImageView android:id="@id/iv_ads_modal_content_app_icon" android:visibility="gone" android:layout_width="56.000000dip" android:layout_height="56.000000dip" android:layout_marginTop="16.000000dip" android:layout_marginBottom="34.000000dip" android:layout_marginStart="16.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_ads_modal_content" app:layout_constraintVertical_bias="0.000000"/>
        <TextView android:textColor="@color/text_primary" android:id="@id/tv_ads_modal_content_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:layout_marginBottom="6.000000dip" android:layout_marginStart="16.000000dip" android:layout_marginEnd="16.000000dip" app:layout_constraintBottom_toTopOf="@id/tv_ads_modal_content_description" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/iv_ads_modal_content_app_icon" app:layout_constraintTop_toBottomOf="@id/iv_ads_modal_content" style="@style/TextH2"/>
        <TextView android:textColor="@color/text_weak" android:id="@id/tv_ads_modal_content_description" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginEnd="16.000000dip" app:layout_constraintBottom_toTopOf="@id/btn_cta" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="@id/tv_ads_modal_content_title" app:layout_constraintTop_toBottomOf="@id/tv_ads_modal_content_title" app:layout_constraintVertical_bias="0.000000" style="@style/TextP2"/>
        <com.google.android.material.button.MaterialButton android:id="@id/btn_cta" android:focusable="false" android:clickable="false" android:layout_width="0.000000dip" android:layout_height="40.000000dip" android:layout_marginTop="@dimen/spacing_m" android:layout_marginBottom="@dimen/spacing_m" android:text="@string/view_components_button_primary" android:layout_marginStart="@dimen/spacing_s" android:layout_marginEnd="@dimen/spacing_s" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_ads_modal_content_description" style="@style/MaterialButton.Primary"/>
      </androidx.constraintlayout.widget.ConstraintLayout>
    </com.google.android.gms.ads.nativead.NativeAdView>
  </androidx.cardview.widget.CardView>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_ads_modal_remove_ads" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_xl" android:layout_marginHorizontal="@dimen/spacing_s" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
  <FrameLayout android:id="@id/layout_loading_ad" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
    <ProgressBar android:layout_gravity="0x00000011" android:id="@id/progress_bar_loading_ads" android:layout_width="64.000000dip" android:layout_height="64.000000dip" android:elevation="2.000000dip"/>
  </FrameLayout>
</androidx.constraintlayout.widget.ConstraintLayout>
```
