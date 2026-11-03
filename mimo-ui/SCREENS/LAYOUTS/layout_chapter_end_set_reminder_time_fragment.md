# پروندهٔ لایه — `res/layout/chapter_end_set_reminder_time_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/chapter_end_set_reminder_time_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/chapter_end_set_reminder_time_fragment.xml`](../../SOURCE/res/layout/chapter_end_set_reminder_time_fragment.xml) |
| SHA-256 دیکد | `c1ba4a01dafe6587594ad8c37b60f277e3755d0114227a9116d13447f3b6abf6` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 28 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_reminder_time_title
   ├─ TextView  #@id/tv_set_reminder_time
   ├─ TextView  #@id/tv_onboarding_step_header
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/iv_set_reminder_time
   ├─ TextView  #@id/tv_reminder_time
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_footer_content
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 4 | `TextView` | `android:textColor` | `@color/text_primary` |
| 5 | `TextView` | `android:gravity` | `0x00000011` |
| 6 | `TextView` | `android:id` | `@id/tv_set_reminder_time_title` |
| 7 | `TextView` | `android:layout_width` | `0.000000dip` |
| 8 | `TextView` | `android:layout_height` | `wrap_content` |
| 9 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 10 | `TextView` | `android:text` | `@string/start_a_coding_habit` |
| 11 | `TextView` | `android:minLines` | `2` |
| 12 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 13 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_set_reminder_time` |
| 14 | `TextView` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 15 | `TextView` | `app:layout_constraintRight_toRightOf` | `0` |
| 16 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 17 | `TextView` | `style` | `@style/TextH1` |
| 18 | `TextView` | `android:textColor` | `@color/text_weak` |
| 19 | `TextView` | `android:gravity` | `0x00000031` |
| 20 | `TextView` | `android:id` | `@id/tv_set_reminder_time` |
| 21 | `TextView` | `android:layout_width` | `0.000000dip` |
| 22 | `TextView` | `android:layout_height` | `wrap_content` |
| 23 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 24 | `TextView` | `android:text` | `@string/you_can_change_time_later` |
| 25 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_xxl` |
| 26 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xxl` |
| 27 | `TextView` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 28 | `TextView` | `app:layout_constraintRight_toRightOf` | `0` |
| 29 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_set_reminder_time_title` |
| 30 | `TextView` | `style` | `@style/TextP1` |
| 31 | `TextView` | `android:textAppearance` | `@style/TextLabel1` |
| 32 | `TextView` | `android:textColor` | `@color/support_purple` |
| 33 | `TextView` | `android:gravity` | `0x00000011` |
| 34 | `TextView` | `android:id` | `@id/tv_onboarding_step_header` |
| 35 | `TextView` | `android:layout_width` | `match_parent` |
| 36 | `TextView` | `android:layout_height` | `wrap_content` |
| 37 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 38 | `TextView` | `android:text` | `@string/reminder` |
| 39 | `TextView` | `android:textAllCaps` | `true` |
| 40 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/iv_set_reminder_time` |
| 41 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_set_reminder_time` |
| 42 | `TextView` | `app:layout_constraintVertical_chainStyle` | `2` |
| 43 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:id` | `@id/iv_set_reminder_time` |
| 44 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_width` | `wrap_content` |
| 45 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_height` | `220.000000dip` |
| 46 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_marginBottom` | `@dimen/spacing_s` |
| 47 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintBottom_toTopOf` | `@id/tv_reminder_time` |
| 48 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 49 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintStart_toStartOf` | `0` |
| 50 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_onboarding_step_header` |
| 51 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveAutoPlay` | `true` |
| 52 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveFit` | `1` |
| 53 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveLoop` | `1` |
| 54 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveResource` | `@raw/notification` |
| 55 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveStateMachine` | `default` |
| 56 | `TextView` | `android:gravity` | `0x00000031` |
| 57 | `TextView` | `android:id` | `@id/tv_reminder_time` |
| 58 | `TextView` | `android:background` | `@drawable/set_reminder_time_background` |
| 59 | `TextView` | `android:paddingTop` | `@dimen/spacing_m` |
| 60 | `TextView` | `android:paddingBottom` | `14.000000dip` |
| 61 | `TextView` | `android:layout_width` | `wrap_content` |
| 62 | `TextView` | `android:layout_height` | `wrap_content` |
| 63 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 64 | `TextView` | `android:layout_marginBottom` | `82.000000dip` |
| 65 | `TextView` | `android:foreground` | `?attr/selectableItemBackgroundBorderless` |
| 66 | `TextView` | `android:paddingStart` | `@dimen/spacing_l` |
| 67 | `TextView` | `android:paddingEnd` | `@dimen/spacing_l` |
| 68 | `TextView` | `android:elevation` | `2.000000dip` |
| 69 | `TextView` | `app:drawableEndCompat` | `@drawable/ic_chevron_down_small` |
| 70 | `TextView` | `app:drawableTint` | `@color/text_primary` |
| 71 | `TextView` | `app:layout_constraintBottom_toTopOf` | `@id/compose_footer_content` |
| 72 | `TextView` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 73 | `TextView` | `app:layout_constraintRight_toRightOf` | `0` |
| 74 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_set_reminder_time` |
| 75 | `TextView` | `style` | `@style/TextViewOnBoardingReminderTime` |
| 76 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/compose_footer_content` |
| 77 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 78 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 79 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 80 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 81 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/support_purple` | `#FF7E4BDE` / `#FFB99AF4` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxl` | `40.000000dip` |
| `@string/reminder` | `Reminder` / `Erinnerung` (de) / `Recordatorio` (es) / `Rappel` (fr) / `Pengingat` (in) / `Promemoria` (it) / `Przypomnienie` (pl) / `Lembrete` (pt-rBR) / `Напоминание` (ru) / `Hatırlatıcı` (tr) |
| `@string/start_a_coding_habit` | `Start a coding habit, set a daily reminder` / `Mach Coding zu einer Gewohnheit, stelle eine tägliche Erinnerung ein` (de) / `Empieza un hábito para programar, establece un recordatorio diario` (es) / `Démarre une habitude de codage, définis un rappel quotidien` (fr) / `Mulai kebiasaan koding, atur pengingat harian` (in) / `Crea l'abitudine di programmare: imposta un promemoria giornaliero` (it) / `Zbuduj nawyk kodowania, ustaw codzienne przypomnienie` (pl) / `Adquira o hábito de programar, defina um lembrete diário` (pt-rBR) / `Заведи привычку кодировать, установи ежедневное напоминание` (ru) / `Kodlama alışkanlığı başlat, günlük hatırlatıcı kur` (tr) |
| `@string/you_can_change_time_later` | `You can always change the time later` / `Du kannst später jederzeit die Uhrzeit ändern` (de) / `Siempre puedes cambiar la hora después` (es) / `Tu peux toujours changer l'heure plus tard` (fr) / `Kamu selalu bisa mengubah waktunya nanti` (in) / `Puoi cambiare l'orario quando vuoi` (it) / `Godzinę zmienisz w każdej chwili` (pl) / `Você pode mudar a hora a qualquer momento` (pt-rBR) / `Ты всегда можешь изменить время позже` (ru) / `Saati istediğin zaman değiştirebilirsin` (tr) |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextViewOnBoardingReminderTime` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:textAllCaps', 'attr_id': '0x0101038C', 'value': 'true', 'value_type': 'int_boolean'}]` |

## ۴. شناسه‌های `@id`

```text
@id/compose_footer_content
@id/iv_set_reminder_time
@id/tv_onboarding_step_header
@id/tv_reminder_time
@id/tv_set_reminder_time
@id/tv_set_reminder_time_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.chapter.ChapterActivity
com.getmimo.ui.chapter.remindertime.SetReminderTimeFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_set_reminder_time_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/start_a_coding_habit" android:minLines="2" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/tv_set_reminder_time" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextH1"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000031" android:id="@id/tv_set_reminder_time" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:text="@string/you_can_change_time_later" android:layout_marginStart="@dimen/spacing_xxl" android:layout_marginEnd="@dimen/spacing_xxl" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toBottomOf="@id/tv_set_reminder_time_title" style="@style/TextP1"/>
  <TextView android:textAppearance="@style/TextLabel1" android:textColor="@color/support_purple" android:gravity="0x00000011" android:id="@id/tv_onboarding_step_header" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable" android:text="@string/reminder" android:textAllCaps="true" app:layout_constraintBottom_toTopOf="@id/iv_set_reminder_time" app:layout_constraintTop_toBottomOf="@id/tv_set_reminder_time" app:layout_constraintVertical_chainStyle="2"/>
  <app.rive.runtime.kotlin.RiveAnimationView android:id="@id/iv_set_reminder_time" android:layout_width="wrap_content" android:layout_height="220.000000dip" android:layout_marginBottom="@dimen/spacing_s" app:layout_constraintBottom_toTopOf="@id/tv_reminder_time" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_onboarding_step_header" app:riveAutoPlay="true" app:riveFit="1" app:riveLoop="1" app:riveResource="@raw/notification" app:riveStateMachine="default"/>
  <TextView android:gravity="0x00000031" android:id="@id/tv_reminder_time" android:background="@drawable/set_reminder_time_background" android:paddingTop="@dimen/spacing_m" android:paddingBottom="14.000000dip" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginBottom="82.000000dip" android:foreground="?attr/selectableItemBackgroundBorderless" android:paddingStart="@dimen/spacing_l" android:paddingEnd="@dimen/spacing_l" android:elevation="2.000000dip" app:drawableEndCompat="@drawable/ic_chevron_down_small" app:drawableTint="@color/text_primary" app:layout_constraintBottom_toTopOf="@id/compose_footer_content" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toBottomOf="@id/iv_set_reminder_time" style="@style/TextViewOnBoardingReminderTime"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/compose_footer_content" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
