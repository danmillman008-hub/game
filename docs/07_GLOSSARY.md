# ۷ · واژهنامه (جلوگیری از سوءتفاهمهای پرهزینه)

| واژه | معنای دقیق در این پروژه |
|---|---|
| **Mimo / میمو** | اپ `com.getmimo` نسخهٔ ۹٫۳۵، منبع مهندسی معکوس. |
| **M09 / MISSION_09** | آخرین مأموریت رانتایم؛ ۱۹ تحویلی نهایی در `ANALYSIS/MISSION_09/`. مرجع اول معماری. |
| **v12.5-fa** | آخرین دور طراحی تأییدشدهٔ کاربر؛ `mimo-ui/UPGRADE/DESIGN/index.html` با SHA `c356068…`. |
| **پروتوتایپ** | همان فایل `DESIGN/index.html` (۱۵ صفحه، توکنها، یادداشتها). کپیاش در `app/assets/phone.html` بایتبهبایت است. |
| **درسنامه** | `tutorial` در میمو / کتاب در کنکور. **نه** متن دموی چیدمان خط. |
| **فصل / chapter** | زیرمجموعهٔ درسنامه؛ در بستهٔ فعلی ۲۰ فصل، هر کدام ۶ ریزدرس. |
| **ریزدرس / micro-lesson** | کوچکترین واحد قابلحل (در میمو `LessonProgress` میسازد). ۱۲۰ عدد فعلی. |
| **نقش پداگوژیک** | `hook → check → feedback → explain → practice → recap` (enum رسمی شامل `challenge`, `example` هم هست). |
| **بلوک / block** | یک قطعه با `renderer` مشخص و `trace.sourceRef`؛ ۱۶۰ عدد فعلی. |
| **DSL** | زبان نشانهگذاری درس میمو: `p/code/selection/img/webview/interaction/database/output`. تگ ناشناخته حذف میشود؛ XML خراب → اسلاید خالی. |
| **A6–A11** | شش ولیدیتور پاسخ (ترتیب `fillTheGap`، `all{selected==isCorrect}`، `validatedInput` نرمالشده، `solvedContent`). |
| **`LessonProgress`** | ردیف ۱۱فیلدی Room/SQLite؛ `isSolvedCorrectly ≡ tries>=1`، `publishSetVersion`, `inQueue`, `queued`. |
| **پاسخبرگ** | برگهای که گزینههای زدهشدهٔ آزمون را نشان میدهد. **با پاسخنامه فرق دارد.** |
| **پاسخنامه** | فهرست پاسخهای صحیح + توضیح گزینهها؛ دکمهای جداگانه در هاب آزمون. |
| **KONKUR** | دادهٔ محلی ۱۲ درس کنکور در `learning-path.js`؛ منبع محتوای نهایی **نیست** (placeholder). |
| **QRAW / QBANK** | ۲۰ پرسش/پاسخ موجود در `proto-ui.js`؛ تنها منبع جملات عینی `STRUCTURED_PACKAGE.json`. `QBANK` سمت آزمون همچنان placeholder است. |
| **STARTER_PACKAGE** | همان ۲۰ پرسش در قالب فرم، `contentStatus:'placeholder'`. |
| **STRUCTURED_PACKAGE** | بستهٔ فعلی: همان جملهها ولی در سلسلهمراتب بومی میمو، `structured` / `unreviewed`. |
| **PROCESSED_DRAFT** | خروجی `process_book.py` از word boxes کتاب؛ noisy، `unreviewed`، خارج از گیت و اپ. |
| **LearnHarness** | «بخش هوش مصنوعی» محلی: سنجش / برنامه / آموزش / تمرین. بدون LLM، بدون کلید، بدون شبکه. |
| **سه ساختار توکن** | (۱) توکنهای طراحی CSS، (۲) اقتصاد محلی و دفتر توکنها، (۳) زمینه/هزینه/گامهای AI. |
| **SOURCE_SLOT** | `'__MIMO' + '_SOURCE_B64_SLOT__'` در `output-kit.js`؛ محل تزریق بستهٔ داخل `<head>`. دقیقاً یکبار. |
| **SERVER CONFIRMED=0** | هیچ رفتار سروری در کل پروژه تأیید نشده؛ بالاترین پرچم صداقت. |
| **VERIFIED_STATIC / RUNTIME / ASSET / UNKNOWN / SERVER_DEPENDENT** | واژگان اعتبار `FINAL_UNKNOWN_REGISTER.md` ← `06_EVIDENCE_INDEX.md`. |
| **F10…F47** | شمارهٔ یادداشتها/قواعد در `02_UI_FIDELITY_CONTRACT.md` و `CATALOGS/*.csv`. |
| **ARSC** | منابع اندروید APK؛ منبع رنگها، dimens و وکتورها. |
| **`chapterRefFor()`** | نگاشت فصل → محتوا؛ فعلاً **هشپایه** است (R2 در roadmap). |
| **superseded** | بنر اسناد `mimo-ui/UPGRADE/*`: دور طراحی قدیمی، حکم امروز نیست. |
| **بازسازی ۱ / ۲** | `2042db0d` ناوبری بومی / `9179b8c4` لایهٔ محتوا. |

بعدی: [`08_HANDOFF_PROMPT.md`](08_HANDOFF_PROMPT.md)
