# پروندهٔ لایه — `res/layout/material_clock_period_toggle.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/material_clock_period_toggle.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/material_clock_period_toggle.xml`](../../SOURCE/res/layout/material_clock_period_toggle.xml) |
| SHA-256 دیکد | `bdea73544a70651cd0a716f3a0db1c21bec332b31026159b17e36ab1df3e8147` |
| ریشه | `com.google.android.material.button.MaterialButtonToggleGroup` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 9 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.google.android.material.button.MaterialButtonToggleGroup  #@id/material_clock_period_toggle
   ├─ com.google.android.material.button.MaterialButton  #@id/material_clock_period_am_button
   └─ com.google.android.material.button.MaterialButton  #@id/material_clock_period_pm_button
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.google.android.material.button.MaterialButtonToggleGroup` | `android:orientation` | `vertical` |
| 2 | `com.google.android.material.button.MaterialButtonToggleGroup` | `android:id` | `@id/material_clock_period_toggle` |
| 3 | `com.google.android.material.button.MaterialButtonToggleGroup` | `android:visibility` | `gone` |
| 4 | `com.google.android.material.button.MaterialButtonToggleGroup` | `android:layout_width` | `@dimen/material_clock_period_toggle_width` |
| 5 | `com.google.android.material.button.MaterialButtonToggleGroup` | `android:layout_height` | `@dimen/material_clock_period_toggle_height` |
| 6 | `com.google.android.material.button.MaterialButtonToggleGroup` | `android:contentDescription` | `@string/material_clock_toggle_content_description` |
| 7 | `com.google.android.material.button.MaterialButtonToggleGroup` | `app:checkedButton` | `@id/material_clock_period_am_button` |
| 8 | `com.google.android.material.button.MaterialButtonToggleGroup` | `app:selectionRequired` | `true` |
| 9 | `com.google.android.material.button.MaterialButtonToggleGroup` | `app:singleSelection` | `true` |
| 10 | `com.google.android.material.button.MaterialButton` | `android:id` | `@id/material_clock_period_am_button` |
| 11 | `com.google.android.material.button.MaterialButton` | `android:layout_width` | `wrap_content` |
| 12 | `com.google.android.material.button.MaterialButton` | `android:layout_height` | `48.000000dip` |
| 13 | `com.google.android.material.button.MaterialButton` | `android:text` | `@string/material_timepicker_am` |
| 14 | `com.google.android.material.button.MaterialButton` | `android:insetTop` | `8.000000dip` |
| 15 | `com.google.android.material.button.MaterialButton` | `style` | `?attr/materialButtonOutlinedStyle` |
| 16 | `com.google.android.material.button.MaterialButton` | `android:id` | `@id/material_clock_period_pm_button` |
| 17 | `com.google.android.material.button.MaterialButton` | `android:layout_width` | `wrap_content` |
| 18 | `com.google.android.material.button.MaterialButton` | `android:layout_height` | `48.000000dip` |
| 19 | `com.google.android.material.button.MaterialButton` | `android:text` | `@string/material_timepicker_pm` |
| 20 | `com.google.android.material.button.MaterialButton` | `android:insetBottom` | `8.000000dip` |
| 21 | `com.google.android.material.button.MaterialButton` | `style` | `?attr/materialButtonOutlinedStyle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/material_clock_period_toggle_height` | `98.000000dip` |
| `@dimen/material_clock_period_toggle_width` | `52.000000dip` |
| `@string/material_clock_toggle_content_description` | `Select AM or PM` / `Kies vm. of nm.` (af) / `AM ወይም PM ይምረጡ` (am) / `يُرجى اختيار صباحًا أو مساءً.` (ar) / `Select AM or PM` (as) / `Gündüz və ya axşam seçin` (az) / `Выберыце AM (да паўдня) або PM (пасля паўдня)` (be) / `Изберете AM или PM` (bg) / `AM অথবা PM বেছে নিন` (bn) / `Odaberite prijepodne ili poslijepodne` (bs) / `Selecciona a. m. o p. m.` (ca) / `Vyberte AM nebo PM` (cs) / `Vælg AM eller PM` (da) / `Vormittags oder Nachmittags auswählen` (de) / `Επιλέξτε π.μ. ή μ.μ.` (el) / `Select a.m. or p.m.` (en-rGB) / `Selecciona AM o PM` (es) / `Selecciona a.m. o p.m.` (es-r419) / `Selecciona a.m. o p.m.` (es-rUS) / `Valige AM või PM` (et) / `Hautatu AM edo PM` (eu) / `انتخاب .ق.ظ. یا ب.ظ.` (fa) / `Valitse AP tai IP` (fi) / `Sélectionner le format AM ou PM` (fr) / `Sélectionner AM ou PM` (fr-rCA) / `Seleccionar a.m. ou p.m.` (gl) / `AM અથવા PM પસંદ કરો` (gu) / `AM या PM चुनें` (hi) / `Odaberite prijepodne ili poslijepodne` (hr) / `Válassza ki, hogy délelőtt vagy délután` (hu) / `Ընտրել AM կամ PM` (hy) / `Pilih AM atau PM` (in) / `Velja f.h. eða e.h.` (is) / `Seleziona AM o PM` (it) / `יש לבחור ב-AM או ב-PM` (iw) / `午前または午後を選択` (ja) / `აირჩიეთ AM ან PM` (ka) / `"AM" немесе "PM" форматын таңдау` (kk) / `ជ្រើសរើស AM ឬ PM` (km) / `ಬೆಳಿಗ್ಗೆ ಅಥವಾ ಮಧ್ಯಾಹ್ನ ಆಯ್ಕೆಮಾಡಿ` (kn) / `오전 또는 오후를 선택하세요.` (ko) / `Тандоо: AM же PM` (ky) / `ເລືອກຕອນເຊົ້າ ຫຼື ຕອນແລງ` (lo) / `Pasirinkite „iki pietų“ arba „po pietų“` (lt) / `Atlasiet “AM” (priekšpusdienā) vai “PM” (pēcpusdienā).` (lv) / `Изберете претпладне или попладне` (mk) / `AM അല്ലെങ്കിൽ PM തിരഞ്ഞെടുക്കുക` (ml) / `ҮӨ эсвэл ҮХ сонгоно уу` (mn) / `AM किंवा PM निवडा` (mr) / `Pilih AM atau PM` (ms) / `AM (သို့) PM ရွေးရန်` (my) / `Velg AM eller PM` (nb) / `AM वा PM चयन गर्नुहोस्` (ne) / `Selecteer a.m. of p.m.` (nl) / `Select AM or PM` (or) / `AM ਜਾਂ PM ਚੁਣੋ` (pa) / `Wybierz: przed południem czy po południu` (pl) / `Selecionar AM ou PM` (pt-rBR) / `Selecionar AM ou PM` (pt-rPT) / `Selectați ora` (ro) / `Выберите AM (до полудня) или PM (после полудня)` (ru) / `පෙරවරු හෝ පස්වරු තෝරන්න` (si) / `Vyberte AM alebo PM` (sk) / `Izberite dopoldanski ali popoldanski čas.` (sl) / `Zgjidh paradite ose pasdite` (sq) / `Изаберите пре подне или по подне` (sr) / `Välj mellan FM och EM` (sv) / `Chagua AM au PM` (sw) / `AM அல்லது PMமைத் தேர்ந்தெடுக்க உதவும்` (ta) / `AM లేదా PMను ఎంచుకోండి` (te) / `เลือก AM หรือ PM` (th) / `Piliin ang AM o PM` (tl) / `ÖÖ veya ÖS'yi seçin` (tr) / `Виберіть ДП чи ПП` (uk) / `AM یا PM منتخب کریں` (ur) / `Tushdan oldin yoki keyinligini tanlang` (uz) / `Chọn SA hoặc CH` (vi) / `选择上午或下午` (zh-rCN) / `選擇上午或下午` (zh-rHK) / `選取上午或下午` (zh-rTW) / `Khetha u-AM noma u-PM` (zu) |
| `@string/material_timepicker_am` | `AM` / `VM.` (af) / `ጥዋት` (am) / `صباحًا` (ar) / `AM` (as) / `AM` (az) / `AM` (be) / `AM` (bg) / `AM` (bn) / `AM` (bs) / `a. m.` (ca) / `AM` (cs) / `AM` (da) / `AM` (de) / `ΠΜ` (el) / `a.m.` (en-rGB) / `a. m.` (es) / `a.m.` (es-r419) / `a.m.` (es-rUS) / `AM` (et) / `AM` (eu) / `ق.ظ` (fa) / `ap` (fi) / `AM` (fr) / `AM` (fr-rCA) / `a.m.` (gl) / `AM` (gu) / `पूर्वाह्न` (hi) / `AM` (hr) / `de.` (hu) / `AM` (hy) / `AM` (in) / `fh` (is) / `AM` (it) / `AM` (iw) / `午前` (ja) / `AM` (ka) / `AM` (kk) / `ព្រឹក` (km) / `AM` (kn) / `오전` (ko) / `AM` (ky) / `ໂມງເຊົ້າ` (lo) / `AM` (lt) / `AM` (lv) / `пр.` (mk) / `AM` (ml) / `AM` (mn) / `AM` (mr) / `PG` (ms) / `နံနက်` (my) / `AM` (nb) / `AM` (ne) / `a.m.` (nl) / `AM` (or) / `AM` (pa) / `AM` (pl) / `AM` (pt-rBR) / `AM` (pt-rPT) / `a.m.` (ro) / `AM` (ru) / `පෙව` (si) / `AM` (sk) / `dop.` (sl) / `PD` (sq) / `AM` (sr) / `FM` (sv) / `AM` (sw) / `AM` (ta) / `AM` (te) / `AM` (th) / `AM` (tl) / `AM` (tr) / `дп` (uk) / `قبل از دوپہر` (ur) / `AM` (uz) / `SA` (vi) / `上午` (zh-rCN) / `AM` (zh-rHK) / `AM` (zh-rTW) / `AM` (zu) |
| `@string/material_timepicker_pm` | `PM` / `NM.` (af) / `ከሰዓት` (am) / `مساءً` (ar) / `PM` (as) / `GƏ` (az) / `PM` (be) / `PM` (bg) / `PM` (bn) / `PM` (bs) / `p. m.` (ca) / `PM` (cs) / `e.m.` (da) / `PM` (de) / `ΜΜ` (el) / `p.m.` (en-rGB) / `p. m.` (es) / `p.m.` (es-r419) / `p.m.` (es-rUS) / `PM` (et) / `PM` (eu) / `ب.ظ` (fa) / `ip` (fi) / `PM` (fr) / `PM` (fr-rCA) / `p.m.` (gl) / `PM` (gu) / `अपराह्न` (hi) / `PM` (hr) / `du.` (hu) / `PM` (hy) / `PM` (in) / `eh` (is) / `PM` (it) / `PM` (iw) / `午後` (ja) / `PM` (ka) / `PM` (kk) / `ល្ងាច` (km) / `PM` (kn) / `오후` (ko) / `PM` (ky) / `ໂມງແລງ` (lo) / `PM` (lt) / `PM` (lv) / `по.` (mk) / `PM` (ml) / `PM` (mn) / `PM` (mr) / `P/M` (ms) / `ညနေ` (my) / `PM` (nb) / `PM` (ne) / `p.m.` (nl) / `PM` (or) / `PM` (pa) / `PM` (pl) / `PM` (pt-rBR) / `PM` (pt-rPT) / `p.m.` (ro) / `PM` (ru) / `පව` (si) / `PM` (sk) / `pop.` (sl) / `PD` (sq) / `PM` (sr) / `EM` (sv) / `PM` (sw) / `PM` (ta) / `PM` (te) / `PM` (th) / `PM` (tl) / `PM` (tr) / `пп` (uk) / `رات` (ur) / `PM` (uz) / `CH` (vi) / `下午` (zh-rCN) / `PM` (zh-rHK) / `PM` (zh-rTW) / `PM` (zu) |

## ۴. شناسه‌های `@id`

```text
@id/material_clock_period_am_button
@id/material_clock_period_pm_button
@id/material_clock_period_toggle
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/material_textinput_timepicker.xml
res/layout/material_timepicker.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<com.google.android.material.button.MaterialButtonToggleGroup xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:id="@id/material_clock_period_toggle" android:visibility="gone" android:layout_width="@dimen/material_clock_period_toggle_width" android:layout_height="@dimen/material_clock_period_toggle_height" android:contentDescription="@string/material_clock_toggle_content_description" app:checkedButton="@id/material_clock_period_am_button" app:selectionRequired="true" app:singleSelection="true">
  <com.google.android.material.button.MaterialButton android:id="@id/material_clock_period_am_button" android:layout_width="wrap_content" android:layout_height="48.000000dip" android:text="@string/material_timepicker_am" android:insetTop="8.000000dip" style="?attr/materialButtonOutlinedStyle"/>
  <com.google.android.material.button.MaterialButton android:id="@id/material_clock_period_pm_button" android:layout_width="wrap_content" android:layout_height="48.000000dip" android:text="@string/material_timepicker_pm" android:insetBottom="8.000000dip" style="?attr/materialButtonOutlinedStyle"/>
</com.google.android.material.button.MaterialButtonToggleGroup>
```
