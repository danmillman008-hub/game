# پروندهٔ لایه — `res/layout/material_timepicker_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/material_timepicker_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/material_timepicker_dialog.xml`](../../SOURCE/res/layout/material_timepicker_dialog.xml) |
| SHA-256 دیکد | `0c8c576efaaacf6a31640d565df740759924c7c8f28db1103dd74bc45ba8a981` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 7 |
| ارجاع به منابع | 15 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/header_title
   ├─ com.google.android.material.timepicker.TimePickerView  #@id/material_timepicker_view
   ├─ ViewStub  #@id/material_textinput_timepicker
   ├─ com.google.android.material.button.MaterialButton  #@id/material_timepicker_mode_button
   ├─ Button  #@id/material_timepicker_cancel_button
   └─ Button  #@id/material_timepicker_ok_button
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingBottom` | `2.000000dip` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `wrap_content` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:accessibilityPaneTitle` | `@string/material_timepicker_select_time` |
| 5 | `TextView` | `android:id` | `@id/header_title` |
| 6 | `TextView` | `android:layout_width` | `wrap_content` |
| 7 | `TextView` | `android:layout_height` | `wrap_content` |
| 8 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 9 | `TextView` | `android:text` | `@string/material_timepicker_select_time` |
| 10 | `TextView` | `android:importantForAccessibility` | `yes` |
| 11 | `TextView` | `android:layout_marginStart` | `24.000000dip` |
| 12 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 13 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 14 | `TextView` | `style` | `?attr/materialTimePickerTitleStyle` |
| 15 | `com.google.android.material.timepicker.TimePickerView` | `android:id` | `@id/material_timepicker_view` |
| 16 | `com.google.android.material.timepicker.TimePickerView` | `android:visibility` | `gone` |
| 17 | `com.google.android.material.timepicker.TimePickerView` | `android:layout_width` | `wrap_content` |
| 18 | `com.google.android.material.timepicker.TimePickerView` | `android:layout_height` | `wrap_content` |
| 19 | `com.google.android.material.timepicker.TimePickerView` | `android:layout_marginLeft` | `24.000000dip` |
| 20 | `com.google.android.material.timepicker.TimePickerView` | `android:layout_marginTop` | `@dimen/material_clock_face_margin_top` |
| 21 | `com.google.android.material.timepicker.TimePickerView` | `android:layout_marginRight` | `24.000000dip` |
| 22 | `com.google.android.material.timepicker.TimePickerView` | `android:layout_marginBottom` | `@dimen/material_clock_face_margin_bottom` |
| 23 | `com.google.android.material.timepicker.TimePickerView` | `app:layout_constraintBottom_toTopOf` | `@id/material_timepicker_mode_button` |
| 24 | `com.google.android.material.timepicker.TimePickerView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 25 | `com.google.android.material.timepicker.TimePickerView` | `app:layout_constraintStart_toStartOf` | `0` |
| 26 | `com.google.android.material.timepicker.TimePickerView` | `app:layout_constraintTop_toTopOf` | `0` |
| 27 | `ViewStub` | `android:id` | `@id/material_textinput_timepicker` |
| 28 | `ViewStub` | `android:layout` | `@layout/material_textinput_timepicker` |
| 29 | `ViewStub` | `android:inflatedId` | `@id/material_textinput_timepicker` |
| 30 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 31 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 32 | `ViewStub` | `android:layout_marginLeft` | `24.000000dip` |
| 33 | `ViewStub` | `android:layout_marginTop` | `44.000000dip` |
| 34 | `ViewStub` | `android:layout_marginRight` | `24.000000dip` |
| 35 | `ViewStub` | `android:layout_marginBottom` | `@dimen/material_clock_face_margin_bottom` |
| 36 | `ViewStub` | `app:layout_constraintBottom_toTopOf` | `@id/material_timepicker_mode_button` |
| 37 | `ViewStub` | `app:layout_constraintEnd_toEndOf` | `0` |
| 38 | `ViewStub` | `app:layout_constraintStart_toStartOf` | `0` |
| 39 | `ViewStub` | `app:layout_constraintTop_toTopOf` | `0` |
| 40 | `com.google.android.material.button.MaterialButton` | `android:id` | `@id/material_timepicker_mode_button` |
| 41 | `com.google.android.material.button.MaterialButton` | `android:layout_width` | `wrap_content` |
| 42 | `com.google.android.material.button.MaterialButton` | `android:layout_height` | `wrap_content` |
| 43 | `com.google.android.material.button.MaterialButton` | `android:layout_marginStart` | `12.000000dip` |
| 44 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 45 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintStart_toStartOf` | `0` |
| 46 | `com.google.android.material.button.MaterialButton` | `style` | `?attr/imageButtonStyle` |
| 47 | `Button` | `android:id` | `@id/material_timepicker_cancel_button` |
| 48 | `Button` | `android:layout_width` | `wrap_content` |
| 49 | `Button` | `android:layout_height` | `wrap_content` |
| 50 | `Button` | `android:layout_marginTop` | `2.000000dip` |
| 51 | `Button` | `android:minWidth` | `72.000000dip` |
| 52 | `Button` | `android:text` | `@string/mtrl_timepicker_cancel` |
| 53 | `Button` | `android:layout_marginEnd` | `8.000000dip` |
| 54 | `Button` | `app:layout_constraintEnd_toStartOf` | `@id/material_timepicker_ok_button` |
| 55 | `Button` | `app:layout_constraintTop_toTopOf` | `@id/material_timepicker_mode_button` |
| 56 | `Button` | `style` | `?attr/borderlessButtonStyle` |
| 57 | `Button` | `android:id` | `@id/material_timepicker_ok_button` |
| 58 | `Button` | `android:layout_width` | `wrap_content` |
| 59 | `Button` | `android:layout_height` | `wrap_content` |
| 60 | `Button` | `android:layout_marginTop` | `2.000000dip` |
| 61 | `Button` | `android:minWidth` | `64.000000dip` |
| 62 | `Button` | `android:text` | `@string/mtrl_timepicker_confirm` |
| 63 | `Button` | `android:layout_marginEnd` | `8.000000dip` |
| 64 | `Button` | `app:layout_constraintEnd_toEndOf` | `0` |
| 65 | `Button` | `app:layout_constraintTop_toTopOf` | `@id/material_timepicker_mode_button` |
| 66 | `Button` | `style` | `?attr/borderlessButtonStyle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/material_clock_face_margin_bottom` | `24.000000dip` / `8.000000dip` (h320dp-port) / `24.000000dip` (h550dp-port) |
| `@dimen/material_clock_face_margin_top` | `44.000000dip` / `36.000000dip` (w320dp-land) |
| `@string/material_timepicker_select_time` | `Select time` / `Kies tyd` (af) / `ጊዜ ምረጥ` (am) / `اختيار الوقت` (ar) / `Select time` (as) / `Vaxt seçin` (az) / `Выберыце час` (be) / `Избор на час` (bg) / `সময় বেছে নিন` (bn) / `Odabir vremena` (bs) / `Selecció de l'hora` (ca) / `Vyberte čas` (cs) / `Vælg tidspunkt` (da) / `Uhrzeit auswählen` (de) / `Επιλέξτε ώρα` (el) / `Select time` (en-rGB) / `Seleccionar la hora` (es) / `Selecciona una hora` (es-r419) / `Selecciona una hora` (es-rUS) / `Aja valimine` (et) / `Hautatu ordua` (eu) / `انتخاب زمان` (fa) / `Valitse aika` (fi) / `Sélectionner l'heure` (fr) / `Sélectionner l'heure` (fr-rCA) / `Seleccionar hora` (gl) / `સમય પસંદ કરો` (gu) / `समय चुनें` (hi) / `Odabir vremena` (hr) / `Időpont kiválasztása` (hu) / `Ժամանակի ընտրություն` (hy) / `Pilih waktu` (in) / `Veldu tíma` (is) / `Seleziona l'ora` (it) / `בחר שעה` (iw) / `時刻を選択` (ja) / `აირჩიეთ დრო` (ka) / `Уақытты таңдау` (kk) / `ជ្រើស​ម៉ោង` (km) / `ಸಮಯವನ್ನು ಆಯ್ಕೆಮಾಡಿ` (kn) / `시간 선택` (ko) / `Убакыт тандоо` (ky) / `ເລືອກເວ​ລາ` (lo) / `Pasirinkite laiką` (lt) / `Laika atlasīšana` (lv) / `Изберете време` (mk) / `സമയം തിരഞ്ഞെടുക്കുക` (ml) / `Цаг сонгох` (mn) / `वेळ निवडा` (mr) / `Pilih masa` (ms) / `အချိန်ရွေးပါ` (my) / `Velg tidspunkt` (nb) / `समय चयन गर्नुहोस्` (ne) / `Tijd selecteren` (nl) / `Select time` (or) / `ਸਮਾਂ ਚੁਣੋ` (pa) / `Określ czas` (pl) / `Selecionar horário` (pt-rBR) / `Selecionar hora` (pt-rPT) / `Selectați ora` (ro) / `Выбор времени` (ru) / `වේලාව තෝරන්න` (si) / `Vyberte čas` (sk) / `Izberite uro` (sl) / `Zgjidh orën` (sq) / `Изаберите време` (sr) / `Välj tid` (sv) / `Chagua wakati` (sw) / `நேரத்தைத் தேர்ந்தெடுக்கவும்` (ta) / `సమయాన్ని ఎంచుకోండి` (te) / `เลือกเวลา` (th) / `Pumili ng oras` (tl) / `Zamanı seçin` (tr) / `Виберіть час` (uk) / `وقت منتخب کریں` (ur) / `Vaqtni tanlang` (uz) / `Chọn thời gian` (vi) / `选择时间` (zh-rCN) / `選取時間` (zh-rHK) / `選取時間` (zh-rTW) / `Khetha isikhathi` (zu) |
| `@string/mtrl_timepicker_cancel` | `Cancel` / `Kanselleer` (af) / `ይቅር` (am) / `إلغاء` (ar) / `Cancel` (as) / `Ləğv edin` (az) / `Скасаваць` (be) / `Отказ` (bg) / `বাতিল করুন` (bn) / `Otkaži` (bs) / `Cancel·la` (ca) / `Zrušit` (cs) / `Annuller` (da) / `Abbrechen` (de) / `Ακύρωση` (el) / `Cancel` (en-rGB) / `Cancelar` (es) / `Cancelar` (es-r419) / `Cancelar` (es-rUS) / `Tühista` (et) / `Utzi` (eu) / `لغو` (fa) / `Peru` (fi) / `Annuler` (fr) / `Annuler` (fr-rCA) / `Cancelar` (gl) / `રદ કરો` (gu) / `रद्द करें` (hi) / `Odustani` (hr) / `Mégse` (hu) / `Չեղարկել` (hy) / `Batal` (in) / `Hætta við` (is) / `Annulla` (it) / `ביטול` (iw) / `キャンセル` (ja) / `გაუქმება` (ka) / `Бас тарту` (kk) / `បោះបង់` (km) / `ರದ್ದುಮಾಡಿ` (kn) / `취소` (ko) / `Жокко чыгаруу` (ky) / `ຍົກເລີກ` (lo) / `Atšaukti` (lt) / `Atcelt` (lv) / `Откажи` (mk) / `റദ്ദാക്കുക` (ml) / `Цуцлах` (mn) / `रद्द करा` (mr) / `Batal` (ms) / `မလုပ်တော့` (my) / `Avbryt` (nb) / `रद्द गर्नुहोस्` (ne) / `Annuleren` (nl) / `Cancel` (or) / `ਰੱਦ ਕਰੋ` (pa) / `Anuluj` (pl) / `Cancelar` (pt-rBR) / `Cancelar` (pt-rPT) / `Anulați` (ro) / `Отмена` (ru) / `අවලංගු කරන්න` (si) / `Zrušiť` (sk) / `Prekliči` (sl) / `Anulo` (sq) / `Откажи` (sr) / `Avbryt` (sv) / `Ghairi` (sw) / `ரத்துசெய்` (ta) / `రద్దు చేయండి` (te) / `ยกเลิก` (th) / `Kanselahin` (tl) / `İptal` (tr) / `Скасувати` (uk) / `منسوخ کریں` (ur) / `Bekor qilish` (uz) / `Huỷ` (vi) / `取消` (zh-rCN) / `取消` (zh-rHK) / `取消` (zh-rTW) / `Khansela` (zu) |
| `@string/mtrl_timepicker_confirm` | `OK` / `OK` (af) / `እሺ` (am) / `حسنًا` (ar) / `OK` (as) / `OK` (az) / `ОК` (be) / `OK` (bg) / `ঠিক আছে` (bn) / `Uredu` (bs) / `D’acord` (ca) / `OK` (cs) / `OK` (da) / `OK` (de) / `ΟΚ` (el) / `OK` (en-rGB) / `Aceptar` (es) / `Aceptar` (es-r419) / `Aceptar` (es-rUS) / `OK` (et) / `Ados` (eu) / `تأیید` (fa) / `OK` (fi) / `OK` (fr) / `OK` (fr-rCA) / `Aceptar` (gl) / `ઓકે` (gu) / `ठीक है` (hi) / `U redu` (hr) / `OK` (hu) / `Եղավ` (hy) / `Oke` (in) / `Í lagi` (is) / `OK` (it) / `אישור` (iw) / `OK` (ja) / `კარგი` (ka) / `Жарайды` (kk) / `យល់ព្រម` (km) / `ಸರಿ` (kn) / `확인` (ko) / `Жарайт` (ky) / `ຕົກລົງ` (lo) / `Gerai` (lt) / `Labi` (lv) / `Во ред` (mk) / `ശരി` (ml) / `OK` (mn) / `ओके` (mr) / `OK` (ms) / `OK` (my) / `OK` (nb) / `ठिक छ` (ne) / `OK` (nl) / `OK` (or) / `ਠੀਕ ਹੈ` (pa) / `OK` (pl) / `OK` (pt-rBR) / `OK` (pt-rPT) / `OK` (ro) / `ОК` (ru) / `හරි` (si) / `OK` (sk) / `V redu` (sl) / `Në rregull` (sq) / `Потврди` (sr) / `OK` (sv) / `Sawa` (sw) / `சரி` (ta) / `సరే` (te) / `ตกลง` (th) / `OK` (tl) / `Tamam` (tr) / `OK` (uk) / `ٹھیک ہے` (ur) / `OK` (uz) / `OK` (vi) / `确定` (zh-rCN) / `確定` (zh-rHK) / `確定` (zh-rTW) / `KULUNGILE` (zu) |

## ۴. شناسه‌های `@id`

```text
@id/header_title
@id/material_textinput_timepicker
@id/material_timepicker_cancel_button
@id/material_timepicker_mode_button
@id/material_timepicker_ok_button
@id/material_timepicker_view
```

## ۵. ارجاع به لایه‌های دیگر

```text
0
24.000000dip
44.000000dip
@dimen/material_clock_face_margin_bottom
@id/material_timepicker_mode_button
@layout/material_textinput_timepicker
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:paddingBottom="2.000000dip" android:layout_width="wrap_content" android:layout_height="wrap_content" android:accessibilityPaneTitle="@string/material_timepicker_select_time">
  <TextView android:id="@id/header_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:text="@string/material_timepicker_select_time" android:importantForAccessibility="yes" android:layout_marginStart="24.000000dip" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="?attr/materialTimePickerTitleStyle"/>
  <com.google.android.material.timepicker.TimePickerView android:id="@id/material_timepicker_view" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginLeft="24.000000dip" android:layout_marginTop="@dimen/material_clock_face_margin_top" android:layout_marginRight="24.000000dip" android:layout_marginBottom="@dimen/material_clock_face_margin_bottom" app:layout_constraintBottom_toTopOf="@id/material_timepicker_mode_button" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <ViewStub android:id="@id/material_textinput_timepicker" android:layout="@layout/material_textinput_timepicker" android:inflatedId="@id/material_textinput_timepicker" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginLeft="24.000000dip" android:layout_marginTop="44.000000dip" android:layout_marginRight="24.000000dip" android:layout_marginBottom="@dimen/material_clock_face_margin_bottom" app:layout_constraintBottom_toTopOf="@id/material_timepicker_mode_button" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <com.google.android.material.button.MaterialButton android:id="@id/material_timepicker_mode_button" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginStart="12.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" style="?attr/imageButtonStyle"/>
  <Button android:id="@id/material_timepicker_cancel_button" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="2.000000dip" android:minWidth="72.000000dip" android:text="@string/mtrl_timepicker_cancel" android:layout_marginEnd="8.000000dip" app:layout_constraintEnd_toStartOf="@id/material_timepicker_ok_button" app:layout_constraintTop_toTopOf="@id/material_timepicker_mode_button" style="?attr/borderlessButtonStyle"/>
  <Button android:id="@id/material_timepicker_ok_button" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="2.000000dip" android:minWidth="64.000000dip" android:text="@string/mtrl_timepicker_confirm" android:layout_marginEnd="8.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="@id/material_timepicker_mode_button" style="?attr/borderlessButtonStyle"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
