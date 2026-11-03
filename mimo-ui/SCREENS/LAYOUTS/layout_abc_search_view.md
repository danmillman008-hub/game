# پروندهٔ لایه — `res/layout/abc_search_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_search_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_search_view.xml`](../../SOURCE/res/layout/abc_search_view.xml) |
| SHA-256 دیکد | `f8e8806cd5d9bc23c876eeb61fde7f88fed0536330ad85878fef75b18ada1695` |
| ریشه | `LinearLayout` |
| تعداد گره | 11 |
| تعداد شناسه | 11 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 24 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/search_bar
   ├─ TextView  #@id/search_badge
   ├─ ImageView  #@id/search_button
   └─ LinearLayout  #@id/search_edit_frame
      ├─ ImageView  #@id/search_mag_icon
      ├─ LinearLayout  #@id/search_plate
      │  ├─ view  #@id/search_src_text
      │  └─ ImageView  #@id/search_close_btn
      └─ LinearLayout  #@id/submit_area
         ├─ ImageView  #@id/search_go_btn
         └─ ImageView  #@id/search_voice_btn
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:id` | `@id/search_bar` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 5 | `TextView` | `android:textAppearance` | `?0x01010041` |
| 6 | `TextView` | `android:textColor` | `?0x01010036` |
| 7 | `TextView` | `android:gravity` | `0x00000010` |
| 8 | `TextView` | `android:id` | `@id/search_badge` |
| 9 | `TextView` | `android:visibility` | `gone` |
| 10 | `TextView` | `android:layout_width` | `wrap_content` |
| 11 | `TextView` | `android:layout_height` | `match_parent` |
| 12 | `TextView` | `android:layout_marginBottom` | `2.000000dip` |
| 13 | `TextView` | `android:drawablePadding` | `0.000000dip` |
| 14 | `ImageView` | `android:layout_gravity` | `0x00000010` |
| 15 | `ImageView` | `android:id` | `@id/search_button` |
| 16 | `ImageView` | `android:focusable` | `true` |
| 17 | `ImageView` | `android:layout_width` | `wrap_content` |
| 18 | `ImageView` | `android:layout_height` | `match_parent` |
| 19 | `ImageView` | `android:contentDescription` | `@string/abc_searchview_description_search` |
| 20 | `ImageView` | `style` | `?attr/actionButtonStyle` |
| 21 | `LinearLayout` | `android:orientation` | `horizontal` |
| 22 | `LinearLayout` | `android:id` | `@id/search_edit_frame` |
| 23 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 24 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 25 | `LinearLayout` | `android:layout_marginLeft` | `8.000000dip` |
| 26 | `LinearLayout` | `android:layout_marginRight` | `8.000000dip` |
| 27 | `LinearLayout` | `android:layout_weight` | `1.000000` |
| 28 | `LinearLayout` | `android:layoutDirection` | `locale` |
| 29 | `ImageView` | `android:layout_gravity` | `0x00000010` |
| 30 | `ImageView` | `android:id` | `@id/search_mag_icon` |
| 31 | `ImageView` | `android:visibility` | `gone` |
| 32 | `ImageView` | `android:layout_width` | `@dimen/abc_dropdownitem_icon_width` |
| 33 | `ImageView` | `android:layout_height` | `wrap_content` |
| 34 | `ImageView` | `android:scaleType` | `centerInside` |
| 35 | `ImageView` | `style` | `@style/RtlOverlay.Widget.AppCompat.SearchView.MagIcon` |
| 36 | `LinearLayout` | `android:layout_gravity` | `0x00000010` |
| 37 | `LinearLayout` | `android:orientation` | `horizontal` |
| 38 | `LinearLayout` | `android:id` | `@id/search_plate` |
| 39 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 40 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 41 | `LinearLayout` | `android:layout_weight` | `1.000000` |
| 42 | `view` | `android:ellipsize` | `end` |
| 43 | `view` | `android:layout_gravity` | `0x00000010` |
| 44 | `view` | `android:id` | `@id/search_src_text` |
| 45 | `view` | `android:background` | `@null` |
| 46 | `view` | `android:paddingLeft` | `@dimen/abc_dropdownitem_text_padding_left` |
| 47 | `view` | `android:paddingRight` | `@dimen/abc_dropdownitem_text_padding_right` |
| 48 | `view` | `android:layout_width` | `0.000000dip` |
| 49 | `view` | `android:layout_height` | `36.000000dip` |
| 50 | `view` | `android:singleLine` | `true` |
| 51 | `view` | `android:layout_weight` | `1.000000` |
| 52 | `view` | `android:inputType` | `0x00090001` |
| 53 | `view` | `android:dropDownAnchor` | `@id/search_edit_frame` |
| 54 | `view` | `android:imeOptions` | `0x00000003` |
| 55 | `view` | `android:dropDownHeight` | `-2` |
| 56 | `view` | `android:dropDownHorizontalOffset` | `0.000000dip` |
| 57 | `view` | `android:dropDownVerticalOffset` | `0.000000dip` |
| 58 | `view` | `class` | `androidx.appcompat.widget.SearchView$SearchAutoComplete` |
| 59 | `ImageView` | `android:layout_gravity` | `0x00000010` |
| 60 | `ImageView` | `android:id` | `@id/search_close_btn` |
| 61 | `ImageView` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 62 | `ImageView` | `android:paddingLeft` | `8.000000dip` |
| 63 | `ImageView` | `android:paddingRight` | `8.000000dip` |
| 64 | `ImageView` | `android:focusable` | `true` |
| 65 | `ImageView` | `android:layout_width` | `wrap_content` |
| 66 | `ImageView` | `android:layout_height` | `match_parent` |
| 67 | `ImageView` | `android:contentDescription` | `@string/abc_searchview_description_clear` |
| 68 | `LinearLayout` | `android:orientation` | `horizontal` |
| 69 | `LinearLayout` | `android:id` | `@id/submit_area` |
| 70 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 71 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 72 | `ImageView` | `android:layout_gravity` | `0x00000010` |
| 73 | `ImageView` | `android:id` | `@id/search_go_btn` |
| 74 | `ImageView` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 75 | `ImageView` | `android:paddingLeft` | `16.000000dip` |
| 76 | `ImageView` | `android:paddingRight` | `16.000000dip` |
| 77 | `ImageView` | `android:focusable` | `true` |
| 78 | `ImageView` | `android:visibility` | `gone` |
| 79 | `ImageView` | `android:layout_width` | `wrap_content` |
| 80 | `ImageView` | `android:layout_height` | `match_parent` |
| 81 | `ImageView` | `android:contentDescription` | `@string/abc_searchview_description_submit` |
| 82 | `ImageView` | `android:layout_gravity` | `0x00000010` |
| 83 | `ImageView` | `android:id` | `@id/search_voice_btn` |
| 84 | `ImageView` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 85 | `ImageView` | `android:paddingLeft` | `16.000000dip` |
| 86 | `ImageView` | `android:paddingRight` | `16.000000dip` |
| 87 | `ImageView` | `android:focusable` | `true` |
| 88 | `ImageView` | `android:visibility` | `gone` |
| 89 | `ImageView` | `android:layout_width` | `wrap_content` |
| 90 | `ImageView` | `android:layout_height` | `match_parent` |
| 91 | `ImageView` | `android:contentDescription` | `@string/abc_searchview_description_voice` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/abc_dropdownitem_icon_width` | `32.000000dip` |
| `@dimen/abc_dropdownitem_text_padding_left` | `8.000000dip` |
| `@dimen/abc_dropdownitem_text_padding_right` | `8.000000dip` |
| `@string/abc_searchview_description_clear` | `Clear query` / `Vee navraag uit` (af) / `መጠይቅ አጽዳ` (am) / `محو طلب البحث` (ar) / `সন্ধান কৰা প্ৰশ্ন মচক` (as) / `Sorğunu silin` (az) / `Выдаліць запыт` (be) / `Изчистване на заявката` (bg) / `কোয়েরি মুছে ফেলুন` (bn) / `Obriši upit` (bs) / `Esborra la consulta` (ca) / `Smazat dotaz` (cs) / `Ryd forespørgsel` (da) / `Suchanfrage löschen` (de) / `Διαγραφή ερωτήματος` (el) / `Clear query` (en-rAU) / `Clear query` (en-rCA) / `Clear query` (en-rGB) / `Clear query` (en-rIN) / `‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‏‎‏‏‎‎‏‏‏‏‏‎‏‎‏‏‎‏‎‏‎‎‎‏‎‎‏‏‏‏‎‎‎‏‎‏‎‎‎‎‎‏‏‎‏‏‎‎‏‎‏‏‎‎‎‏‎‏‏‏‎‎‏‏‎Clear query‎‏‎‎‏‎` (en-rXC) / `Borrar consulta` (es) / `Borrar consulta` (es-rUS) / `Päringu tühistamine` (et) / `Garbitu kontsulta` (eu) / `پاک کردن پُرسمان` (fa) / `Tyhjennä kysely` (fi) / `Effacer la requête` (fr) / `Effacer la requête` (fr-rCA) / `Borra a consulta` (gl) / `ક્વેરી સાફ કરો` (gu) / `क्‍वेरी हटाएं` (hi) / `Izbriši upit` (hr) / `Lekérdezés törlése` (hu) / `Ջնջել հարցումը` (hy) / `Hapus kueri` (in) / `Hreinsa fyrirspurn` (is) / `Cancella query` (it) / `מחיקת השאילתה` (iw) / `検索キーワードを削除` (ja) / `მოთხოვნის გასუფთავება` (ka) / `Сұрауды өшіру` (kk) / `សម្អាត​សំណួរ` (km) / `ಪ್ರಶ್ನೆಯನ್ನು ತೆರವುಗೊಳಿಸಿ` (kn) / `검색어 삭제` (ko) / `Сурамды өчүрүү` (ky) / `ລຶບຂໍ້ຄວາມຊອກຫາ` (lo) / `Išvalyti užklausą` (lt) / `Notīrīt vaicājumu` (lv) / `Исчисти барање` (mk) / `ചോദ്യം മായ്‌ക്കുക` (ml) / `Асуулга арилгах` (mn) / `क्‍वेरी साफ करा` (mr) / `Kosongkan pertanyaan` (ms) / `ရှာဖွေမှုကို ဖယ်ရှားရန်` (my) / `Slett søket` (nb) / `क्वेरी खाली गर्नुहोस्` (ne) / `Zoekopdracht wissen` (nl) / `କ୍ୱେରୀ ଖାଲି କରନ୍ତୁ` (or) / `ਪੁੱਛਗਿੱਛ ਕਲੀਅਰ ਕਰੋ` (pa) / `Wyczyść zapytanie` (pl) / `Limpar consulta` (pt) / `Limpar consulta` (pt-rBR) / `Limpar consulta` (pt-rPT) / `Șterge interogarea` (ro) / `Удалить запрос` (ru) / `විමසුම හිස් කරන්න` (si) / `Vymazať dopyt` (sk) / `Izbris poizvedbe` (sl) / `Pastro pyetjen` (sq) / `Обришите упит` (sr) / `Ta bort frågan` (sv) / `Futa hoja` (sw) / `வினவலை அழிக்கும்` (ta) / `ప్రశ్నను తీసివేస్తుంది` (te) / `ล้างคำค้นหา` (th) / `I-clear ang query` (tl) / `Sorguyu temizle` (tr) / `Очистити запит` (uk) / `استفسار صاف کریں` (ur) / `So‘rovni o‘chirish` (uz) / `Xóa truy vấn` (vi) / `清除查询` (zh-rCN) / `清除查詢` (zh-rHK) / `清除查詢` (zh-rTW) / `Sula inkinga` (zu) |
| `@string/abc_searchview_description_search` | `Search` / `Soek` (af) / `ፍለጋ` (am) / `البحث` (ar) / `সন্ধান কৰক` (as) / `Axtarın` (az) / `Пошук` (be) / `Търсене` (bg) / `সার্চ করুন` (bn) / `Pretraživanje` (bs) / `Cerca` (ca) / `Hledat` (cs) / `Søg` (da) / `Suche` (de) / `Αναζήτηση` (el) / `Search` (en-rAU) / `Search` (en-rCA) / `Search` (en-rGB) / `Search` (en-rIN) / `‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‏‎‏‎‏‏‏‏‎‏‏‎‏‏‎‏‏‏‏‏‏‎‏‎‎‏‎‏‎‎‏‏‎‎‎‎‎‎‎‎‎‏‏‎‏‎‏‏‏‎‎‏‏‏‏‏‎‎‏‏‏‎‎‎‎Search‎‏‎‎‏‎` (en-rXC) / `Buscar` (es) / `Buscar` (es-rUS) / `Otsing` (et) / `Bilatu` (eu) / `جستجو` (fa) / `Haku` (fi) / `Rechercher` (fr) / `Rechercher` (fr-rCA) / `Realiza buscas` (gl) / `શોધો` (gu) / `खोजें` (hi) / `Pretraži` (hr) / `Keresés` (hu) / `Որոնել` (hy) / `Telusuri` (in) / `Leit` (is) / `Cerca` (it) / `חיפוש` (iw) / `検索` (ja) / `ძიება` (ka) / `Іздеу` (kk) / `ស្វែងរក` (km) / `ಹುಡುಕಿ` (kn) / `검색` (ko) / `Издөө` (ky) / `ຊອກຫາ` (lo) / `Ieškoti` (lt) / `Meklēt` (lv) / `Пребарај` (mk) / `തിരയുക` (ml) / `Хайх` (mn) / `शोधा` (mr) / `Cari` (ms) / `ရှာရန်` (my) / `Søk` (nb) / `खोज्नुहोस्` (ne) / `Zoeken` (nl) / `ସର୍ଚ୍ଚ କରନ୍ତୁ` (or) / `ਖੋਜ` (pa) / `Szukaj` (pl) / `Pesquisar` (pt) / `Pesquisar` (pt-rBR) / `Pesquisar` (pt-rPT) / `Caută` (ro) / `Поиск` (ru) / `සෙවීම` (si) / `Hľadať` (sk) / `Iskanje` (sl) / `Kërko` (sq) / `Претражите` (sr) / `Sök` (sv) / `Tafuta` (sw) / `தேடும்` (ta) / `సెర్చ్` (te) / `ค้นหา` (th) / `Maghanap` (tl) / `Ara` (tr) / `Пошук` (uk) / `تلاش کریں` (ur) / `Qidiruv` (uz) / `Tìm kiếm` (vi) / `搜索` (zh-rCN) / `搜尋` (zh-rHK) / `搜尋` (zh-rTW) / `Sesha` (zu) |
| `@string/abc_searchview_description_submit` | `Submit query` / `Dien navraag in` (af) / `መጠይቅ አስገባ` (am) / `إرسال طلب البحث` (ar) / `প্ৰশ্ন দাখিল কৰক` (as) / `Sorğunu göndərin` (az) / `Адправіць запыт` (be) / `Изпращане на заявката` (bg) / `কোয়েরি জমা দিন` (bn) / `Pošalji upit` (bs) / `Envia la consulta` (ca) / `Odeslat dotaz` (cs) / `Indsend forespørgsel` (da) / `Anfrage senden` (de) / `Υποβολή ερωτήματος` (el) / `Submit query` (en-rAU) / `Submit query` (en-rCA) / `Submit query` (en-rGB) / `Submit query` (en-rIN) / `‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‎‏‏‎‏‎‎‏‎‏‎‎‎‎‏‎‎‏‏‏‏‎‎‎‎‏‎‏‏‎‏‎‏‎‏‎‏‏‎‏‏‏‎‎‎‏‏‏‏‏‎‏‏‎‎‏‏‎‏‏‏‏‏‎Submit query‎‏‎‎‏‎` (en-rXC) / `Enviar consulta` (es) / `Enviar consulta` (es-rUS) / `Päringu esitamine` (et) / `Bidali kontsulta` (eu) / `ارسال پُرسمان` (fa) / `Lähetä kysely` (fi) / `Envoyer la requête` (fr) / `Envoyer la requête` (fr-rCA) / `Envía a consulta` (gl) / `ક્વેરી સબમિટ કરો` (gu) / `क्वेरी सबमिट करें` (hi) / `Pošalji upit` (hr) / `Lekérdezés küldése` (hu) / `Ուղարկել հարցումը` (hy) / `Kirim kueri` (in) / `Senda fyrirspurn` (is) / `Invia query` (it) / `שליחת שאילתה` (iw) / `検索キーワードを送信` (ja) / `მოთხოვნის გადაგზავნა` (ka) / `Сұрауды жіберу` (kk) / `ដាក់បញ្ជូន​សំណួរ` (km) / `ಪ್ರಶ್ನೆಯನ್ನು ಸಲ್ಲಿಸಿ` (kn) / `검색어 보내기` (ko) / `Сурам тапшыруу` (ky) / `ສົ່ງຂໍ້ມູນ` (lo) / `Pateikti užklausą` (lt) / `Iesniegt vaicājumu` (lv) / `Испрати барање` (mk) / `ചോദ്യം സമർപ്പിക്കുക` (ml) / `Асуулга илгээх` (mn) / `क्वेरी सबमिट करा` (mr) / `Serah pertanyaan` (ms) / `ရှာဖွေစရာ အချက်အလက်ကို ပေးပို့ရန်` (my) / `Utfør søket` (nb) / `क्वेरी पेस गर्नुहोस्` (ne) / `Zoekopdracht verzenden` (nl) / `କ୍ୱେରୀ ଦାଖଲ କରନ୍ତୁ` (or) / `ਪੁੱਛਗਿੱਛ ਸਪੁਰਦ ਕਰੋ` (pa) / `Wyślij zapytanie` (pl) / `Enviar consulta` (pt) / `Enviar consulta` (pt-rBR) / `Enviar consulta` (pt-rPT) / `Trimite interogarea` (ro) / `Отправить запрос` (ru) / `විමසුම යොමු කරන්න` (si) / `Odoslať dopyt` (sk) / `Pošiljanje poizvedbe` (sl) / `Dërgo pyetjen` (sq) / `Пошаљите упит` (sr) / `Skicka fråga` (sv) / `Wasilisha hoja` (sw) / `வினவலைச் சமர்ப்பிக்கும்` (ta) / `ప్రశ్నని సమర్పిస్తుంది` (te) / `ส่งคำค้นหา` (th) / `Isumite ang query` (tl) / `Sorguyu gönder` (tr) / `Наіслати запит` (uk) / `استفسار جمع کرائیں` (ur) / `So‘rov yaratish` (uz) / `Gửi truy vấn` (vi) / `提交查询` (zh-rCN) / `提交查詢` (zh-rHK) / `提交查詢` (zh-rTW) / `Thumela umbuzo` (zu) |
| `@string/abc_searchview_description_voice` | `Voice search` / `Stemsoektog` (af) / `የድምጽ ፍለጋ` (am) / `بحث صوتي` (ar) / `কণ্ঠধ্বনিৰ দ্বাৰা সন্ধান` (as) / `Səsli axtarış` (az) / `Галасавы пошук` (be) / `Гласово търсене` (bg) / `ভয়েস সার্চ করুন` (bn) / `Glasovno pretraživanje` (bs) / `Cerca per veu` (ca) / `Hlasové vyhledávání` (cs) / `Talesøgning` (da) / `Sprachsuche` (de) / `Φωνητική αναζήτηση` (el) / `Voice search` (en-rAU) / `Voice search` (en-rCA) / `Voice search` (en-rGB) / `Voice search` (en-rIN) / `‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‎‏‏‏‏‏‏‏‏‎‏‎‏‎‎‎‏‏‎‏‏‎‏‏‎‎‎‏‎‏‏‏‏‏‎‏‏‎‎‎‏‏‎‏‏‎‏‎‎‎‎‏‎‎‎‏‎‎‏‎‏‏‏‎Voice search‎‏‎‎‏‎` (en-rXC) / `Búsqueda por voz` (es) / `Búsqueda por voz` (es-rUS) / `Häälotsing` (et) / `Ahozko bilaketa` (eu) / `جستجوی گفتاری` (fa) / `Puhehaku` (fi) / `Recherche vocale` (fr) / `Recherche vocale` (fr-rCA) / `Busca por voz` (gl) / `વૉઇસ શોધ` (gu) / `बोलकर खोजें` (hi) / `Glasovno pretraživanje` (hr) / `Hangalapú keresés` (hu) / `Ձայնային որոնում` (hy) / `Penelusuran suara` (in) / `Raddleit` (is) / `Ricerca vocale` (it) / `חיפוש קולי` (iw) / `音声検索` (ja) / `ხმოვანი ძიება` (ka) / `Дауыспен іздеу` (kk) / `ស្វែងរក​តាម​សំឡេង` (km) / `ಧ್ವನಿ ಹುಡುಕಾಟ` (kn) / `음성 검색` (ko) / `Айтып издөө` (ky) / `ຊອກຫາດ້ວຍສຽງ` (lo) / `Paieška balsu` (lt) / `Meklēt ar balsi` (lv) / `Гласовно пребарување` (mk) / `സംസാരത്തിലൂടെ തിരയുക` (ml) / `Дуут хайлт` (mn) / `व्हॉइस शोध` (mr) / `Carian suara` (ms) / `အသံဖြင့် ရှာရန်` (my) / `Talesøk` (nb) / `आवाजमा आधारित खोजी` (ne) / `Gesproken zoekopdracht` (nl) / `ଭଏସ ସର୍ଚ୍ଚ` (or) / `ਅਵਾਜ਼ੀ ਖੋਜ` (pa) / `Wyszukiwanie głosowe` (pl) / `Pesquisa por voz` (pt) / `Pesquisa por voz` (pt-rBR) / `Pesquisa por voz` (pt-rPT) / `Căutare vocală` (ro) / `Голосовой поиск` (ru) / `හඬ සෙවීම` (si) / `Hlasové vyhľadávanie` (sk) / `Glasovno iskanje` (sl) / `Kërkim me zë` (sq) / `Гласовна претрага` (sr) / `Röstsökning` (sv) / `Kutafuta kwa kutamka` (sw) / `குரல் தேடல்` (ta) / `వాయిస్ సెర్చ్` (te) / `ค้นหาด้วยเสียง` (th) / `Paghahanap gamit ang boses` (tl) / `Sesli arama` (tr) / `Голосовий пошук` (uk) / `صوتی تلاش` (ur) / `Ovozli qidiruv` (uz) / `Tìm kiếm bằng giọng nói` (vi) / `语音搜索` (zh-rCN) / `語音搜尋` (zh-rHK) / `語音搜尋` (zh-rTW) / `Ukusesha ngezwi` (zu) |
| `@style/RtlOverlay.Widget.AppCompat.SearchView.MagIcon` | `[{'attr': 'android:layout_marginStart', 'attr_id': '0x010103B5', 'value': '@dimen/abc_dropdownitem_text_padding_left', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/search_badge
@id/search_bar
@id/search_button
@id/search_close_btn
@id/search_edit_frame
@id/search_go_btn
@id/search_mag_icon
@id/search_plate
@id/search_src_text
@id/search_voice_btn
@id/submit_area
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:id="@id/search_bar" android:layout_width="match_parent" android:layout_height="match_parent">
  <TextView android:textAppearance="?0x01010041" android:textColor="?0x01010036" android:gravity="0x00000010" android:id="@id/search_badge" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="match_parent" android:layout_marginBottom="2.000000dip" android:drawablePadding="0.000000dip"/>
  <ImageView android:layout_gravity="0x00000010" android:id="@id/search_button" android:focusable="true" android:layout_width="wrap_content" android:layout_height="match_parent" android:contentDescription="@string/abc_searchview_description_search" style="?attr/actionButtonStyle"/>
  <LinearLayout android:orientation="horizontal" android:id="@id/search_edit_frame" android:layout_width="wrap_content" android:layout_height="match_parent" android:layout_marginLeft="8.000000dip" android:layout_marginRight="8.000000dip" android:layout_weight="1.000000" android:layoutDirection="locale">
    <ImageView android:layout_gravity="0x00000010" android:id="@id/search_mag_icon" android:visibility="gone" android:layout_width="@dimen/abc_dropdownitem_icon_width" android:layout_height="wrap_content" android:scaleType="centerInside" style="@style/RtlOverlay.Widget.AppCompat.SearchView.MagIcon"/>
    <LinearLayout android:layout_gravity="0x00000010" android:orientation="horizontal" android:id="@id/search_plate" android:layout_width="wrap_content" android:layout_height="match_parent" android:layout_weight="1.000000">
      <view android:ellipsize="end" android:layout_gravity="0x00000010" android:id="@id/search_src_text" android:background="@null" android:paddingLeft="@dimen/abc_dropdownitem_text_padding_left" android:paddingRight="@dimen/abc_dropdownitem_text_padding_right" android:layout_width="0.000000dip" android:layout_height="36.000000dip" android:singleLine="true" android:layout_weight="1.000000" android:inputType="0x00090001" android:dropDownAnchor="@id/search_edit_frame" android:imeOptions="0x00000003" android:dropDownHeight="-2" android:dropDownHorizontalOffset="0.000000dip" android:dropDownVerticalOffset="0.000000dip" class="androidx.appcompat.widget.SearchView$SearchAutoComplete"/>
      <ImageView android:layout_gravity="0x00000010" android:id="@id/search_close_btn" android:background="?attr/selectableItemBackgroundBorderless" android:paddingLeft="8.000000dip" android:paddingRight="8.000000dip" android:focusable="true" android:layout_width="wrap_content" android:layout_height="match_parent" android:contentDescription="@string/abc_searchview_description_clear"/>
    </LinearLayout>
    <LinearLayout android:orientation="horizontal" android:id="@id/submit_area" android:layout_width="wrap_content" android:layout_height="match_parent">
      <ImageView android:layout_gravity="0x00000010" android:id="@id/search_go_btn" android:background="?attr/selectableItemBackgroundBorderless" android:paddingLeft="16.000000dip" android:paddingRight="16.000000dip" android:focusable="true" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="match_parent" android:contentDescription="@string/abc_searchview_description_submit"/>
      <ImageView android:layout_gravity="0x00000010" android:id="@id/search_voice_btn" android:background="?attr/selectableItemBackgroundBorderless" android:paddingLeft="16.000000dip" android:paddingRight="16.000000dip" android:focusable="true" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="match_parent" android:contentDescription="@string/abc_searchview_description_voice"/>
    </LinearLayout>
  </LinearLayout>
</LinearLayout>
```
