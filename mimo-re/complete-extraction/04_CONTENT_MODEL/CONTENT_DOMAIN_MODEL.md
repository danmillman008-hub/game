# ۰۴ — مدل دامنهٔ محتوا

**شواهد:** VERIFIED_STATIC روی کل بستهٔ انگلیسی (۱۹ مسیر، ۱,۰۲۹ آموزش، ۱,۹۴۷ فصل، ۱۸,۲۷۲ درس)
و تطبیق با ۹ بستهٔ دیگر.

## ۱. موجودیت‌ها و روابط

```
PublishSet (publishSetVersion = 753, per language pack)
└── Track           19      id, version(3..501), title, onboardingCategory(build|none), isNew, sections[]
    └── Section     249     name, startIndex, endIndex, tutorialIds[]
        └── Tutorial 1,029  id, version(1..161), type(6), codeLanguage(11), chapters[], isNew, showInTrack
            └── Chapter 1,947  id, type(6: practiceLevel1..3 | challengeLevel0..2), lessons[]
                └── Lesson 18,272  id, contentType(interactive|executableFiles),
                                     interactiveContent?, hardModeContent?, executableContent?
```

**تفکیک مفاهیم (چیزی که در گزارش‌های عمومی اشتباه گرفته می‌شود):**

| مفهوم | در Mimo چیست | نیست |
|---|---|---|
| Track | «مسیر» = لیست پخش آموزش‌ها | دورهٔ یکپارچه با سیلابس |
| Section | برش مسیر + اندیس شروع | فصل محتوا |
| Tutorial | واحد انتشار و نسخه‌دهی (فایل JSON) | درس |
| Chapter | واحد نمایش در `ChapterActivity` + واحد سختی | آزمون |
| Lesson | واحد سنجش (تعاملی یا کدی) | مفهوم آموزشی |
| Practice | **بازخدمت** فصل‌های موجود | محتوای جدید |
| Challenge | برچسب فصل (`challengeLevel*`) | سیستم جدا |
| Project | نوع آموزش (`guidedProject*`) | محیط پروژه |

## ۲. آمار کلیدی (اندازه‌گیری‌شده)

| سنجه | مقدار |
|---|---|
| آموزش بر حسب نوع | course 507 · practiceRequired 157 · practiceOptional 134 · guidedProjectOptional 117 · guidedProject 74 · challenges 40 |
| زبان کد | javascript 283 · python 195 · css 169 · html 139 · sql 64 · node 47 · jsx 46 · swift 43 · typescript 23 · none 19 · bash 1 |
| فصل بر حسب تعداد درس | ۱ درس: ۶۷۰ · ۲: ۱۶۳ · ۳: ۱۱۹ · ۴: ۳۸ · ۵: ۵ · ۱۰: ۶ |
| درس بر فصل | میانگین ۹.۳۸ · میانه ۱۰ · بیشینه ۲۸ |
| درس تعاملی / کدی | ۱۴,۲۴۸ / ۴,۰۲۴ |
| درس با `hardModeContent` | ۶,۰۵۸ (۴۲.۵٪ از تعاملی‌ها) |
| بلوک سنجش | ۱۳,۰۲۷ (۸,۲۷۶ interaction + ۴,۷۵۱ selection) |

## ۳. یکپارچگی (بازتولیدشده در این فاز)

| بررسی | نتیجه |
|---|---|
| `sections[].startIndex` = مجموع طول بخش‌های قبل | ۲۴۹/۲۴۹ ✅ |
| ارجاع `tutorialIds[]` به فایل موجود | ۰ ارجاع شکسته ✅ |
| آموزش‌های بی‌استفاده (orphan) | ۰ ✅ |
| شناسهٔ تکراری (آموزش/فصل/درس) | ۰ ✅ |
| درس کدی بدون `solvedContent` | ۴۲ (تنها انحراف) ⚠️ |
| کلاس درس کدی بدون فایل | ۰ ✅ |

## ۴. تفاوت بسته‌ها

۹ بسته: ۱۹ مسیر / ۱,۰۲۹ آموزش / ۱۸,۲۷۲ درس؛ **it, pl, tr, id**: ۱,۰۳۱ آموزش / ۱۸,۲۸۹ درس
(+۲ آموزش، +۱۷ درس) با همان `publishSetVersion = 753`.
⇒ نسخهٔ انتشار، «قرارداد» است نه هش محتوا؛ CMS می‌تواند محتوای بومی را مستقل اضافه کند.
