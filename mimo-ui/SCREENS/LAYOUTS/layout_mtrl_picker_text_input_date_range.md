# پروندهٔ لایه — `res/layout/mtrl_picker_text_input_date_range.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_picker_text_input_date_range.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_picker_text_input_date_range.xml`](../../SOURCE/res/layout/mtrl_picker_text_input_date_range.xml) |
| SHA-256 دیکد | `0baa0df4b2d0d0473f50403417d36d5da8e53cc299c2a4371e14e0d7c8faa7a3` |
| ریشه | `ScrollView` |
| تعداد گره | 7 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ ScrollView
   └─ LinearLayout
      ├─ com.google.android.material.textfield.TextInputLayout  #@id/mtrl_picker_text_input_range_start
      │  └─ com.google.android.material.textfield.TextInputEditText  #@id/mtrl_picker_edit_text_range_start
      ├─ Space
      └─ com.google.android.material.textfield.TextInputLayout  #@id/mtrl_picker_text_input_range_end
         └─ com.google.android.material.textfield.TextInputEditText  #@id/mtrl_picker_edit_text_range_end
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ScrollView` | `android:layout_width` | `match_parent` |
| 2 | `ScrollView` | `android:layout_height` | `wrap_content` |
| 3 | `LinearLayout` | `android:orientation` | `vertical` |
| 4 | `LinearLayout` | `android:paddingLeft` | `@dimen/mtrl_calendar_content_padding` |
| 5 | `LinearLayout` | `android:paddingTop` | `@dimen/mtrl_calendar_text_input_padding_top` |
| 6 | `LinearLayout` | `android:paddingRight` | `@dimen/mtrl_calendar_content_padding` |
| 7 | `LinearLayout` | `android:paddingBottom` | `16.000000dip` |
| 8 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 9 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 10 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_gravity` | `0x00000001` |
| 11 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/mtrl_picker_text_input_range_start` |
| 12 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `match_parent` |
| 13 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 14 | `com.google.android.material.textfield.TextInputLayout` | `android:maxWidth` | `@dimen/material_textinput_max_width` |
| 15 | `com.google.android.material.textfield.TextInputLayout` | `android:minWidth` | `@dimen/material_textinput_min_width_with_label` |
| 16 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/mtrl_picker_edit_text_range_start` |
| 17 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 18 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 19 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `@string/mtrl_picker_text_input_date_range_start_hint` |
| 20 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000014` |
| 21 | `com.google.android.material.textfield.TextInputEditText` | `android:imeOptions` | `0x10000000` |
| 22 | `Space` | `android:layout_width` | `0.000000dip` |
| 23 | `Space` | `android:layout_height` | `8.000000dip` |
| 24 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_gravity` | `0x00000001` |
| 25 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/mtrl_picker_text_input_range_end` |
| 26 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `match_parent` |
| 27 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 28 | `com.google.android.material.textfield.TextInputLayout` | `android:maxWidth` | `@dimen/material_textinput_max_width` |
| 29 | `com.google.android.material.textfield.TextInputLayout` | `android:minWidth` | `@dimen/material_textinput_min_width_with_label` |
| 30 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/mtrl_picker_edit_text_range_end` |
| 31 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 32 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 33 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `@string/mtrl_picker_text_input_date_range_end_hint` |
| 34 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000014` |
| 35 | `com.google.android.material.textfield.TextInputEditText` | `android:imeOptions` | `0x10000000` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/material_textinput_max_width` | `488.000000dip` |
| `@dimen/material_textinput_min_width_with_label` | `88.000000dip` |
| `@dimen/mtrl_calendar_content_padding` | `12.000000dip` |
| `@dimen/mtrl_calendar_text_input_padding_top` | `16.000000dip` / `32.000000dip` (land) |
| `@string/mtrl_picker_text_input_date_range_end_hint` | `End date` / `Einddatum` (af) / `የማብቂያ ቀን` (am) / `تاريخ الانتهاء` (ar) / `End date` (as) / `Bitmə tarixi` (az) / `Дата заканчэння` (be) / `Крайна дата` (bg) / `সমাপ্তির তারিখ` (bn) / `Datum završetka` (bs) / `Data de finalització` (ca) / `Datum ukončení` (cs) / `Slutdato` (da) / `Enddatum` (de) / `Ημερομηνία λήξης` (el) / `End date` (en-rGB) / `Fecha de finalización` (es) / `Fecha de finalización` (es-r419) / `Fecha de finalización` (es-rUS) / `Lõppkuupäev` (et) / `Amaiera-data` (eu) / `تاریخ پایان` (fa) / `Päättymispäivä` (fi) / `Date de fin` (fr) / `Date de fin` (fr-rCA) / `Data de finalización` (gl) / `સમાપ્તિની તારીખ` (gu) / `खत्म होने की तारीख` (hi) / `Datum završetka` (hr) / `Befejezés dátuma` (hu) / `Ավարտի ամսաթիվը` (hy) / `Tanggal akhir` (in) / `Lokadagur` (is) / `Data di fine` (it) / `תאריך סיום` (iw) / `終了日` (ja) / `დასრულების თარიღი` (ka) / `Аяқталу күні` (kk) / `កាល​បរិច្ឆេទ​បញ្ចប់` (km) / `ಮುಕ್ತಾಯ ದಿನಾಂಕ` (kn) / `종료일` (ko) / `Качан аяктайт` (ky) / `ວັນທີສິ້ນສຸດ` (lo) / `Pabaigos data` (lt) / `Beigu datums` (lv) / `Краен датум` (mk) / `അവസാനിക്കുന്ന തീയതി` (ml) / `Дуусах огноо` (mn) / `संपण्याची तारीख` (mr) / `Tarikh tamat` (ms) / `ပြီးဆုံးရက်` (my) / `Sluttdato` (nb) / `अन्त्य हुने मिति` (ne) / `Einddatum` (nl) / `End date` (or) / `ਸਮਾਪਤੀ ਤਾਰੀਖ` (pa) / `Data zakończenia` (pl) / `Data de término` (pt-rBR) / `Data de fim` (pt-rPT) / `Data de încheiere` (ro) / `Дата окончания` (ru) / `නිමා වන දිනය` (si) / `Dátum ukončenia` (sk) / `Končni datum` (sl) / `Data e përfundimit` (sq) / `Датум завршетка` (sr) / `Slutdatum` (sv) / `Tarehe ya mwisho` (sw) / `முடிவுத் தேதி` (ta) / `ముగింపు తేదీ` (te) / `วันที่สิ้นสุด` (th) / `Petsa ng pagtatapos` (tl) / `Bitiş tarihi` (tr) / `Дата завершення` (uk) / `تاریخ اختتام` (ur) / `Tugash sanasi` (uz) / `Ngày kết thúc` (vi) / `结束日期` (zh-rCN) / `結束日期` (zh-rHK) / `結束日期` (zh-rTW) / `Idethi yokuphela` (zu) |
| `@string/mtrl_picker_text_input_date_range_start_hint` | `Start date` / `Begindatum` (af) / `መጀመሪያ ቀን` (am) / `تاريخ البدء` (ar) / `Start date` (as) / `Başlama tarixi` (az) / `Дата пачатку` (be) / `Начална дата` (bg) / `শুরুর তারিখ` (bn) / `Datum početka` (bs) / `Data d'inici` (ca) / `Datum zahájení` (cs) / `Startdato` (da) / `Startdatum` (de) / `Ημερομηνία έναρξης` (el) / `Start date` (en-rGB) / `Fecha de inicio` (es) / `Fecha de inicio` (es-r419) / `Fecha de inicio` (es-rUS) / `Alguskuupäev` (et) / `Hasiera-data` (eu) / `تاریخ شروع` (fa) / `Alkamispäivä` (fi) / `Date de début` (fr) / `Date de début` (fr-rCA) / `Data de inicio` (gl) / `શરૂ કરવાની તારીખ` (gu) / `शुरू होने की तारीख` (hi) / `Datum početka` (hr) / `Kezdés dátuma` (hu) / `Մեկնարկի ամսաթիվը` (hy) / `Tanggal mulai` (in) / `Upphafsdagur` (is) / `Data di inizio` (it) / `תאריך התחלה` (iw) / `開始日` (ja) / `დაწყების თარიღი` (ka) / `Басталу күні` (kk) / `កាល​បរិច្ឆេទ​ចាប់ផ្ដើម` (km) / `ಪ್ರಾರಂಭ ದಿನಾಂಕ` (kn) / `시작일` (ko) / `Баштоо күнү` (ky) / `ວັນທີເລີ່ມ` (lo) / `Pradžios data` (lt) / `Sākuma datums` (lv) / `Почетен датум` (mk) / `ആരംഭിക്കുന്ന തീയതി` (ml) / `Эхлэх огноо` (mn) / `सुरू होण्याची तारीख` (mr) / `Tarikh mula` (ms) / `စတင်ရက်` (my) / `Startdato` (nb) / `सुरु हुने मिति` (ne) / `Startdatum` (nl) / `Start date` (or) / `ਸ਼ੁਰੂਆਤੀ ਤਾਰੀਖ` (pa) / `Data rozpoczęcia` (pl) / `Data de início` (pt-rBR) / `Data de início` (pt-rPT) / `Data de începere` (ro) / `Дата начала` (ru) / `ආරම්භක දිනය` (si) / `Dátum začatia` (sk) / `Začetni datum` (sl) / `Data e fillimit` (sq) / `Датум почетка` (sr) / `Startdatum` (sv) / `Tarehe ya kuanza` (sw) / `தொடக்கத் தேதி` (ta) / `ప్రారంభ తేదీ` (te) / `วันที่เริ่มต้น` (th) / `Petsa ng pagsisimula` (tl) / `Başlangıç tarihi` (tr) / `Дата початку` (uk) / `تاریخ آغاز` (ur) / `Boshlanish sanasi` (uz) / `Ngày bắt đầu` (vi) / `开始日期` (zh-rCN) / `開始日期` (zh-rHK) / `開始日期` (zh-rTW) / `Idethi yokuqala` (zu) |

## ۴. شناسه‌های `@id`

```text
@id/mtrl_picker_edit_text_range_end
@id/mtrl_picker_edit_text_range_start
@id/mtrl_picker_text_input_range_end
@id/mtrl_picker_text_input_range_start
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="wrap_content">
  <LinearLayout android:orientation="vertical" android:paddingLeft="@dimen/mtrl_calendar_content_padding" android:paddingTop="@dimen/mtrl_calendar_text_input_padding_top" android:paddingRight="@dimen/mtrl_calendar_content_padding" android:paddingBottom="16.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content">
    <com.google.android.material.textfield.TextInputLayout android:layout_gravity="0x00000001" android:id="@id/mtrl_picker_text_input_range_start" android:layout_width="match_parent" android:layout_height="wrap_content" android:maxWidth="@dimen/material_textinput_max_width" android:minWidth="@dimen/material_textinput_min_width_with_label">
      <com.google.android.material.textfield.TextInputEditText android:id="@id/mtrl_picker_edit_text_range_start" android:layout_width="match_parent" android:layout_height="wrap_content" android:hint="@string/mtrl_picker_text_input_date_range_start_hint" android:inputType="0x00000014" android:imeOptions="0x10000000"/>
    </com.google.android.material.textfield.TextInputLayout>
    <Space android:layout_width="0.000000dip" android:layout_height="8.000000dip"/>
    <com.google.android.material.textfield.TextInputLayout android:layout_gravity="0x00000001" android:id="@id/mtrl_picker_text_input_range_end" android:layout_width="match_parent" android:layout_height="wrap_content" android:maxWidth="@dimen/material_textinput_max_width" android:minWidth="@dimen/material_textinput_min_width_with_label">
      <com.google.android.material.textfield.TextInputEditText android:id="@id/mtrl_picker_edit_text_range_end" android:layout_width="match_parent" android:layout_height="wrap_content" android:hint="@string/mtrl_picker_text_input_date_range_end_hint" android:inputType="0x00000014" android:imeOptions="0x10000000"/>
    </com.google.android.material.textfield.TextInputLayout>
  </LinearLayout>
</ScrollView>
```
