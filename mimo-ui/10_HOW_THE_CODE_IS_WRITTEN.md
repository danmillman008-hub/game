# ۱۰ — کد دقیقاً چطور نوشته شده (پاسخ به اصل درخواست)

## خلاصهٔ پاسخ

رابط Mimo 9.35 **عمدتاً XML View است، نه Compose خالص**: ۱٬۲۹۹ لایهٔ کامپایلشده،
که ۷۱ تای آنها یک `ComposeView` برای بخشهای پویا دارند و ۶ تای آنها `WebView` برای درس.
کد UI در سه زبان نوشته شده: **XML** (چیدمان/استایل/حرکت)، **Kotlin** (Activity/Fragment/
ViewModel/Compose)، **JavaScript/CSS** (رندرر درس). منابع در `resources.arsc` کامپایل شدهاند
و کد از طریق شناسههای `0x7F…` به آنها وصل میشود.

## ۱. الگوی اتصال کد به لایه (شاهد مستقیم از DEX)

در `ChapterActivity.onCreate` بایتکد واقعی چنین است (دیکامپایل نشده، operandها خوانده شدهاند):

```
invoke-virtual  Activity.getLayoutInflater()
const           v1, 2131558662        // 0x7F0D0106 = R.layout.chapter_activity
invoke-virtual  LayoutInflater.inflate(I, ViewGroup, Z)
const           v1, 2131362108        // 0x7F0A013C = R.id.chapter_appbarlayout
invoke-static   Lwc/h;->k(View, I)View  // findViewById-like helper (ViewBinding)
check-cast      AppBarLayout / ChapterToolbar / ComposeView
```

یعنی: `setContentView`/`inflate` با **عدد ثابت شناسهٔ منبع**، سپس resolve ویوها با همان
اعداد. `tools/extract_ui.py` این operandها را خوانده و ۱۰۹ نگاشت قطعی
`کلاس → R.layout.*` ساخته (`SOURCE/dex/LAYOUT_XREFS.csv`).

## ۲. اسکلت بازسازیشده (۱۰۹ فایل)

`RECONSTRUCTION/kotlin/*.kt` برای هر یک از آن ۱۰۹ کلاس ساخته شده:
package و superclass واقعی، آنوتیشنها، `setContentView(R.layout.X)`، فهرست `R.id.*`
استخراجشده از operandها، و **فهرست کامل متدها** از جدول DEX. مثال:

```kotlin
// RECONSTRUCTED SKELETON — not decompiled source.
package com.getmimo.ui.chapter
class ChapterActivity : aj.f {              // superclass از DEX
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.chapter_activity)   // از const 0x7F0D0106
    }
    // R.id.compose_view, R.id.vp_lessons, R.id.chapter_toolbar, …
    // DEX: onCreate(Landroid/os/Bundle;)V  … (۳۲ متد)
}
```

> برچسب صادقانه: اینها **سورس دیکامپایلشده نیستند**؛ JADX/Java در محیط موجود نبود.
> چیزی که واقعی است: نام کلاس، superclass، interfaces، نام/امضای همهٔ متدها، آنوتیشنها،
> لیترالها، و شناسههای منبع مصرفشده. فقط قالب `Kotlin` بازسازی شده تا خواندنی باشد.

## ۳. قرارداد نامگذاری (از ۱٬۲۹۹ نام فایل)

| الگو | مثال | معنی |
|---|---|---|
| `<screen>_activity.xml` | `chapter_activity.xml` | ریشهٔ اکتیویتی |
| `<screen>_fragment.xml` | `chapter_finished_fragment.xml` | صفحهٔ Fragment |
| `<screen>_bottomsheet_dialog.xml` | `fake_streak_bottomsheet_dialog.xml` | BottomSheet |
| `<feature>_item_layout.xml` | `lesson_interaction_selection_item_layout.xml` | آیتم RecyclerView |
| `<feature>_view.xml` | `lesson_description_textview.xml` | قطعهٔ قابل include |
| `abc_*` / `m3_*` / `design_*` | `abc_screen_simple.xml` | لایههای AndroidX/Material |
| `layout-v31`, `layout-v33` | ۱۵۰ + ۳۱۹ فایل | Splash/Material You و API 33 |
| `layout-land`, `layout-sw600dp-v13` | ۱۱ + ۳ فایل | چرخش / تبلت |

## ۴. XML چگونه نوشته شده (از جدول ویژگیها)

- `android:id="@+id/..."` → در AXML به `@id/...` (حلشده توسط ما).
- اندازهها `-1`/`-2` به جای `match_parent`/`wrap_content` (ما رمزگشایی کردیم).
- `@color/...`, `@dimen/...`, `@string/...`, `@drawable/...`, `@style/...` همه از ARSC.
- ویژگیهای سفارشی با namespace `app:` (مثلاً `app:elevation` روی AppBarLayout).
- ۲٬۷۷۱ `<include>`/`<ViewStub>` ⇒ کامپوننتسازی با `merge` (۳۳۰ لایه ریشه `merge`اند).
- ۵۳ ویوی سفارشی مثل `com.getmimo.ui.lesson.view.code.CodeBodyView` مستقیم در XML.

## ۵. مقادیر و تم

`resources.arsc` شامل ۱۲٬۹۱۵ شناسه و ۵۰٬۴۷۷ ردیف پیکربندی است. تم روشن/تیره با
همان **نام** و دو مقدار (`default` / `night`) کار میکند؛ مثلاً `background_primary`
`#FFF6F7FB` ↔ `#FF252746`. استایلها (`1٬728` نام) با `<item name="android:...">` ارجاع
میدهند. `SOURCE/values/` این جدول را دوباره به شکل `values.xml` قابل خواندن درآورده.

## ۶. رندرر درس

محتوای درس (۱۰٬۳۰۸ JSON) توسط DSL به HTML تبدیل و در `MimoWebView` نمایش داده میشود؛
`lesson-webview.js` ژست/فوکوس/ارتفاع/نتیجه را به نیتیو پس میفرستد (کامل در `07`).

## ۷. آبفوسکیشن و دستکاری بسته

- بیشتر کلاسهای غیر `ui` نامهای کوتاه R8 دارند (`La/a;`, `Lo70/s;`) — به همین دلیل
  فهرست `CLASS_INDEX` دور قبل پر از «ObfuscatedUnresolved» است.
- رشتهٔ `Smob - Mod obfuscation tool v4.6 by Kirlif'` و ۸ DEX پوچ ⇒ بسته repack شده.
- بنابراین این استخراج **سورس اصلی شرکت نیست**، بلکه توصیف دقیق و کامل همان بینریای است
  که در Drive گذاشتهاید. این تمایز در تمام مستندات حفظ شده.
