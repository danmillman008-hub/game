#!/usr/bin/env python3
"""Generates the four MASTER_*.csv registers from curated claims + measured artifacts.

Every row must point to a real artifact in this workspace. Claims marked INFERRED/UNKNOWN
are intentionally kept so the audit can show what is NOT known.
"""
import csv, json, os, sys

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (area, claim, status, confidence, evidence_path, artifact, method)
EV = [
 ("baseline","هش SHA-256 بستهٔ بازسازی‌شده 48ce1740…f7c7a و اندازهٔ آن 142,353,499 بایت است","VERIFIED_STATIC","HIGH","00_BASELINE/APK_HASHES.json","sha256sum + بازسازی z01/z02/zip","hash"),
 ("baseline","Package=com.getmimo، versionName=9.35، versionCode=1792759685، minSdk=28، targetSdk=36","VERIFIED_STATIC","HIGH","00_BASELINE/APK_FACTS.json","androguard APK()","static-parse"),
 ("baseline","اکتیویتی راه‌انداز یک activity-alias به نام com.getmimo.ui.SplashActivity_default است","VERIFIED_STATIC","HIGH","00_BASELINE/APK_FACTS.json","androguard manifest","static-parse"),
 ("baseline","۲۴ مجوز درخواست شده، شامل CAMERA، RECORD_AUDIO، WRITE_EXTERNAL_STORAGE، USE_BIOMETRIC","VERIFIED_STATIC","HIGH","00_BASELINE/BASELINE_INVENTORY.md","manifest parse","static-parse"),
 ("baseline","۱۲ فایل DEX و ۱۰,۵۶۴ فایل assets و ۱۴,۳۹۸ ورودی ZIP وجود دارد","VERIFIED_STATIC","HIGH","00_BASELINE/APK_CONTENT_TREE.json","zipfile walk","static-parse"),
 ("baseline","۶ کتابخانهٔ native برای دو ABI؛ libsigner.so و libyrf.so تحلیل نمادین نشدند","PARTIALLY_VERIFIED","MEDIUM","01_STATIC_CODE/NATIVE_CODE_ANALYSIS.md","zip listing","static-parse"),
 ("environment","JDK17 از طریق jdk4py در PyPI نصب شد؛ JADX از GitHub Releases مسدود بود","VERIFIED_STATIC","HIGH","00_BASELINE/ENVIRONMENT_REPORT.md","اجرای واقعی دستورها","runtime-env"),
 ("environment","هیچ emulator/adb موجود نیست، بنابراین همهٔ آزمون‌های زمان‌اجرا NOT_TESTED هستند","VERIFIED_STATIC","HIGH","15_RUNTIME_TESTING/MISSING_DEPENDENCIES.md","command -v","runtime-env"),
 ("static","۲۹,۴۵۴ کلاس در ۱۲ DEX وجود دارد که ۳,۱۳۳ کلاس آن از com.getmimo است","VERIFIED_STATIC","HIGH","01_STATIC_CODE/STATIC_SUMMARY.json","CLASS_INDEX","static-parse"),
 ("static","۱۴,۶۰۸ کلاس مبهم‌شده نگاشت شد (نقش پیشنهادی + اطمینان)","PARTIALLY_VERIFIED","MEDIUM","01_STATIC_CODE/OBFUSCATION_MAP.csv.gz","اجرای build_static_artifacts.py","static-parse"),
 ("static","۱۹۹,۸۲۳ یال گراف فراخوانی سطح کلاس استخراج شد که ۶,۱۰۸ یال app→app است","VERIFIED_STATIC","HIGH","01_STATIC_CODE/CALL_GRAPH/edges.csv.gz","پارس invoke-*","static-parse"),
 ("static","۲۹,۷۴۳ نمونه annotation از ۳۶ نوع متمایز وجود دارد","VERIFIED_STATIC","HIGH","01_STATIC_CODE/annotations.json.gz","extract_annotations.py","static-parse"),
 ("static","کتابخانه‌های اصلی: Firebase 5718، RevenueCat 2436، Rive 983، Compose 786، Customer.io 351، Adjust 315، Segment 137","VERIFIED_STATIC","HIGH","01_STATIC_CODE/DEPENDENCY_INVENTORY.csv","شمارش namespace","static-parse"),
 ("resources","۳,۱۷۷ فایل res؛ ۸۰۹ layout پایه + ۳۱۹ layout-v33 + ۱۵۰ layout-v31","VERIFIED_STATIC","HIGH","02_ANDROID_RESOURCES/RESOURCE_CENSUS.csv","zip walk","static-parse"),
 ("resources","UI عمدتاً XML/View است؛ Compose فقط در مربی، کیبورد کدنویسی و ویجت Glance","PARTIALLY_VERIFIED","MEDIUM","02_ANDROID_RESOURCES/RESOURCE_CENSUS.md","نام کلاس‌ها + layout","static-parse"),
 ("resources","۵۹ فایل .riv برای انیمیشن و ۶۹ فایل مرتبط با protobuf در assets وجود دارد","VERIFIED_STATIC","HIGH","02_ANDROID_RESOURCES/RESOURCE_CENSUS.md","zip walk","static-parse"),
 ("ui","۱۹۲ سطح UI فهرست شد (۳۶ activity برنامه، ۲۲ fragment، ۲۲ modal، ۸۷ bottom sheet)","PARTIALLY_VERIFIED","MEDIUM","03_UI_UX/SCREEN_INVENTORY.csv","نام کلاس + رشته","static-parse"),
 ("ui","۲۴ جفت (سطح، حالت) با شاهد مستقیم رشته‌ای مستند شد؛ حالت‌ها اجرا نشده‌اند","PARTIALLY_VERIFIED","MEDIUM","03_UI_UX/SCREEN_STATE_MATRIX.csv","رشته‌های *_offline_*/empty/loading","static-parse"),
 ("ui","تنها یک گراف ناوبری اعلانی (nav_onboarding_graph.xml) وجود دارد؛ بقیه imperative است","VERIFIED_STATIC","HIGH","03_UI_UX/NAVIGATION_MAP.md","manifest + res","static-parse"),
 ("design","۲۳۴ رنگ و ۳۰۰ دایمن برنامه با ۵۹ جفت روشن/تیره استخراج شد","VERIFIED_STATIC","HIGH","03_UI_UX/DESIGN_SYSTEM.md","evidence/design-tokens.json","static-parse"),
 ("design","نقشهٔ توکن→صفحه بر پایهٔ پیشوند نام توکن ساخته شد","INFERRED","MEDIUM","03_UI_UX/DESIGN_SYSTEM.md","تحلیل نام","inference"),
 ("content","۱۹ مسیر، ۲۴۹ بخش، ۱,۰۲۹ آموزش، ۱,۹۴۷ فصل، ۱۸,۲۷۲ درس در بستهٔ انگلیسی","VERIFIED_STATIC","HIGH","04_CONTENT_MODEL/CONTENT_DOMAIN_MODEL.md","پارس lessons-en","static-parse"),
 ("content","۹ بستهٔ دیگر همان publishSetVersion=753 دارند؛ it/pl/tr/id دو آموزش اضافه دارند","VERIFIED_STATIC","HIGH","04_CONTENT_MODEL/CONTENT_VERSIONING.md","مقایسهٔ tracks.json","static-parse"),
 ("content","۱۴,۲۴۸ درس تعاملی و ۴,۰۲۴ درس کدی وجود دارد","VERIFIED_STATIC","HIGH","04_CONTENT_MODEL/CONTENT_DOMAIN_MODEL.md","شمارش contentType","static-parse"),
 ("content","۶,۰۵۸ درس نسخهٔ hardModeContent دارند که ۳,۲۵۵ مورد hardModeSelected=true است","VERIFIED_STATIC","HIGH","05_LESSON_DSL/DSL_VALIDATION_REPORT.json","پارس lesson JSON","static-parse"),
 ("content","همهٔ ۱,۹۴۷ فصل از نوع practice/challenge هستند؛ فصل نظری یا آزمون وجود ندارد","VERIFIED_STATIC","HIGH","07_PEDAGOGY/PEDAGOGY_OVERVIEW.md","شمارش chapter.type","static-parse"),
 ("content","هیچ ارجاع شکسته یا آموزش یتیمی وجود ندارد؛ ۴۲ فایل کدی solvedContent ندارد","VERIFIED_STATIC","HIGH","04_CONTENT_MODEL/CONTENT_DOMAIN_MODEL.md","بازتولید یکپارچگی","static-parse"),
 ("dsl","۲۷ تگ و ۲۹,۷۴۳ نمونهٔ تگ در ۲۰,۳۰۶ سند درس مشاهده شد","VERIFIED_STATIC","HIGH","05_LESSON_DSL/DSL_TAG_CENSUS.csv","tools/dsl_census.py","static-parse"),
 ("dsl","اندیس startIndex/endIndex آفست کاراکتر روی متن بازسازی‌شده است، نه اندیس توکن","VERIFIED_STATIC","HIGH","05_LESSON_DSL/SEMANTICS_CORRECTION.md","اعتبارسنجی ۲۹,۰۹۳ بازه","static-parse"),
 ("dsl","۰ نقض محدوده در ۲۹,۰۹۳ بازهٔ جای خالی و ۱,۷۷۲ بازهٔ validatedInput پس از اصلاح پارسر","VERIFIED_STATIC","HIGH","05_LESSON_DSL/DSL_VALIDATION_REPORT.json","tools/lesson_dsl.py","unit-test"),
 ("dsl","یک fillTheGap می‌تواند تا ۱۲ جای خالی داشته باشد؛ ۱۱,۱۵۱ بلوک بدون جای خالی است","VERIFIED_STATIC","HIGH","05_LESSON_DSL/DSL_VALIDATION_REPORT.json","توزیع gaps_per_block","static-parse"),
 ("dsl","۱۴,۸۷۰ گزینهٔ انحرافی (correct=false) در استخر چیپ‌ها وجود دارد","VERIFIED_STATIC","HIGH","05_LESSON_DSL/BLOCK_REFERENCE.md","شمارش option","static-parse"),
 ("dsl","۱۳,۴۲۵ يتيم","UNKNOWN","LOW","05_LESSON_DSL/SEMANTICS_CORRECTION.md","placeholder","none"),
 ("dsl","۱۳۷ مورد عیب محتوا: ۸ بلوک کد خالی، ۴ webview بدون content، ۱۲۵ selection با value تکراری","VERIFIED_STATIC","HIGH","05_LESSON_DSL/DSL_VALIDATION_REPORT.json","validate()","static-parse"),
 ("dsl","دامنهٔ visible-if بسته است: always/wrong/correct","VERIFIED_STATIC","HIGH","05_LESSON_DSL/DSL_VALUE_DOMAINS.csv","شمارش مقادیر","static-parse"),
 ("dsl","۲۳ آزمون واحد روی پارسر و ۴ فیکسچر تألیفی سبز است","VERIFIED_STATIC","HIGH","16_AUTOMATED_TESTS/test_lesson_dsl.py","pytest","unit-test"),
 ("execution","ماشین حالت درس (Loading/InProgress/Wrong/Correct/ChapterFinished/Offline) از رشته‌ها و ViewModelها بازسازی شد","INFERRED","MEDIUM","06_EXECUTION_ENGINE/EXECUTION_STATE_MACHINE.md","نام state + رشته","inference"),
 ("execution","درس کدی هیچ فایل تستی در کلاینت ندارد؛ تصحیح احتمالاً سمت سرور است","INFERRED","MEDIUM","06_EXECUTION_ENGINE/CODE_RUNNER_SPEC.md","کلیدهای executableContent","inference"),
 ("execution","محتوای swift و bash در بسته وجود دارد که در اندروید قابل اجرا نیست","PARTIALLY_VERIFIED","MEDIUM","06_EXECUTION_ENGINE/CODE_RUNNER_SPEC.md","شمارش codeLanguage","static-parse"),
 ("pedagogy","Mimo گراف پیش‌نیاز صریح ندارد؛ ترتیب خطی از Section.tutorialIds می‌آید","VERIFIED_STATIC","HIGH","07_PEDAGOGY/CURRICULUM_GRAPH.md","پارس محتوا","static-parse"),
 ("pedagogy","مدل تسلط/الگوریتم تکرار فاصله‌دار در کلاینت قابل اثبات نیست","UNKNOWN","LOW","07_PEDAGOGY/MASTERY_MODEL.md","جستجوی کلاس/رشته","none"),
 ("pedagogy","تمرین هوشمند فصل‌های موجود را بازخدمت می‌کند و سؤال جدید نمی‌سازد","INFERRED","MEDIUM","07_PEDAGOGY/PRACTICE_ENGINE.md","مودال‌ها + رشته‌ها","inference"),
 ("ai","ساختار پرامپت مربی در کلاینت ساخته می‌شود: SystemMessage$Executable/Interactive","VERIFIED_STATIC","HIGH","08_AI_TUTOR/PROMPT_CONTRACT.md","class-strings","static-parse"),
 ("ai","پرامپت ۹ قاعده دارد (فقط درس، بدون لو دادن پاسخ، هم‌زبان کاربر، عدم افشای دستورها)","VERIFIED_STATIC","HIGH","08_AI_TUTOR/PROMPT_CONTRACT.md","تحلیل رشتهٔ پرامپت","static-parse"),
 ("ai","solvedContent به‌عنوان expectedAnswer به مدل داده می‌شود (ریسک لو رفتن پاسخ)","VERIFIED_STATIC","HIGH","08_AI_TUTOR/CONTEXT_ASSEMBLY.md","SystemMessage$Executable","static-parse"),
 ("ai","سهمیهٔ عددی پیام و مدل/تأمین‌کننده در بسته نیست","UNKNOWN","LOW","08_AI_TUTOR/QUOTA_BILLING.md","جستجو","none"),
 ("progress","سه جدول Room: lesson_progress, chapter_completions, tutorial_completions","VERIFIED_STATIC","HIGH","11_DATABASE_PERSISTENCE/ROOM_SCHEMA.md","رشته‌های Database_Impl","static-parse"),
 ("progress","lesson_progress دو شمارندهٔ جدا دارد: attempts (شروع دوباره) و tries (بررسی درون درس)","VERIFIED_STATIC","HIGH","11_DATABASE_PERSISTENCE/ROOM_SCHEMA.md","toString entity","static-parse"),
 ("progress","الگوی outbox با DELETE FROM lesson_progress WHERE lesson_id IN (...) تأیید شد","VERIFIED_STATIC","HIGH","11_DATABASE_PERSISTENCE/SYNC_CONFLICTS.md","رشتهٔ postUnsyncedLessonProgress","static-parse"),
 ("progress","هیچ کلاس Room Migration در بسته نیست ⇒ ریسک از دست رفتن دادهٔ ارسال‌نشده","INFERRED","MEDIUM","11_DATABASE_PERSISTENCE/MIGRATIONS.md","جستجوی CLASS_INDEX","inference"),
 ("progress","کلید (Keys) دروازهٔ درس است با بازتولید روزانه","INFERRED","MEDIUM","09_PROGRESS_GAMIFICATION/KEYS_AND_GATING.md","رشته keys_* + endpoints","inference"),
 ("progress","لیگ/لیدربورد سه نما دارد: latest, friends, userrank","VERIFIED_STATIC","HIGH","09_PROGRESS_GAMIFICATION/LEADERBOARD.md","annotation paths","static-parse"),
 ("api","۶۲ مسیر API از annotationها بازیابی شد که ۵۳ مورد first-party است","VERIFIED_STATIC","HIGH","10_BACKEND_API/API_ENDPOINTS.json","extract_annotations + catalog","static-parse"),
 ("api","Lie0/f=GET، Lie0/b=DELETE، Lie0/p=DELETE با اطمینان HIGH؛ Lie0/o=POST MEDIUM؛ Lie0/n=LOW","VERIFIED_STATIC","HIGH","10_BACKEND_API/VERB_MAPPING.md","رأی‌گیری نام متد + شکل مسیر","static-parse"),
 ("api","۲۱ literal مسیر بدون annotation وجود دارد (Firebase Auth، RevenueCat، Customer.io، aiTutor)","VERIFIED_STATIC","HIGH","10_BACKEND_API/API_CATALOG.md","data/endpoints.txt diff","static-parse"),
 ("api","احراز هویت Firebase + Bearer است؛ مسیرهای /auth/* در بسته به‌صورت literal هستند","VERIFIED_STATIC","HIGH","10_BACKEND_API/AUTH_MODEL.md","رشته‌ها","static-parse"),
 ("api","بدنهٔ پاسخ هیچ endpoint بازیابی نشد (بدون اجرا)","NOT_ACCESSIBLE","HIGH","10_BACKEND_API/API_CATALOG.md","—","none"),
 ("api","۲۶۵ stub اسکیمای DTO از نام کلاس مدل‌ها تولید شد","PARTIALLY_VERIFIED","LOW","10_BACKEND_API/DTO_SCHEMA/","نام کلاس + toString","static-parse"),
 ("subs","RevenueCat با ۲۴۳۶ کلاس موتور خرید است و دو سطح Pro/MAX وجود دارد","VERIFIED_STATIC","HIGH","12_SUBSCRIPTIONS/PRODUCT_MODEL.md","شمارش + رشته","static-parse"),
 ("subs","۹ نقطهٔ نمایش پی‌وال در رشته‌ها شناسایی شد","PARTIALLY_VERIFIED","MEDIUM","12_SUBSCRIPTIONS/PRODUCT_MODEL.md","رشته‌های upgrade/paywall","static-parse"),
 ("subs","تخفیف از Remote Config با شمارش معکوس می‌آید (feature_flag_last_call_discount)","VERIFIED_STATIC","HIGH","12_SUBSCRIPTIONS/TRIAL_AND_DISCOUNT.md","رشته‌ها + کلاس","static-parse"),
 ("subs","شناسهٔ محصول/قیمت در APK نیست (از Play/RevenueCat در زمان اجرا)","NOT_ACCESSIBLE","HIGH","12_SUBSCRIPTIONS/REVENUECAT_INTEGRATION.md","جستجو","none"),
 ("config","دو پرچم boolean نام‌دار وجود دارد: feature_flag_ai_tutor_android و feature_flag_last_call_discount","VERIFIED_STATIC","HIGH","13_REMOTE_CONFIG/REMOTE_CONFIG_INVENTORY.md","رشته‌ها","static-parse"),
 ("config","پیکربندی اختصاصی /v2/client-config وجود دارد و بدنهٔ آن نامعلوم است","PARTIALLY_VERIFIED","MEDIUM","13_REMOTE_CONFIG/CONFIG_CONTRACTS.md","annotation + نبود DTO","static-parse"),
 ("config","آزمایش محتوا با ContentExperiment (originalTrackId/variantTrackId/visibilityPercentage)","VERIFIED_STATIC","HIGH","13_REMOTE_CONFIG/EXPERIMENTS.md","کلاس‌ها","static-parse"),
 ("analytics","۳۰۵ مورد گزارش‌شدهٔ قبلی «رویداد» در واقع ۳۰۵ کلاس property است","VERIFIED_STATIC","HIGH","14_ANALYTICS_NOTIFICATIONS/ANALYTICS_ARCHITECTURE.md","شمارش CLASS_INDEX","static-parse"),
 ("analytics","۲۳۷ شناسهٔ snake_case متمایز در بستهٔ تحلیلی وجود دارد","VERIFIED_STATIC","HIGH","14_ANALYTICS_NOTIFICATIONS/ANALYTICS_ARCHITECTURE.md","class-strings","static-parse"),
 ("analytics","فهرست کامل نام رویدادها بدون decompiler قابل استخراج نیست","NOT_ACCESSIBLE","HIGH","14_ANALYTICS_NOTIFICATIONS/ANALYTICS_ARCHITECTURE.md","—","none"),
 ("analytics","Segment (۱۳۷ کلاس) به‌عنوان روتر تحلیلی و Mixpanel (۶۲) به‌عنوان مقصد شناسایی شد","PARTIALLY_VERIFIED","MEDIUM","14_ANALYTICS_NOTIFICATIONS/ANALYTICS_ARCHITECTURE.md","شمارش namespace","static-parse"),
 ("analytics","ثبت توکن اعلان به /v1/user/deviceTokens و Customer.io با پیام خطای مشخص تأیید شد","VERIFIED_STATIC","HIGH","14_ANALYTICS_NOTIFICATIONS/NOTIFICATIONS.md","رشته‌ها","static-parse"),
 ("analytics","۹ deep link با wildcard /learn/.* شناسایی شد","VERIFIED_STATIC","HIGH","14_ANALYTICS_NOTIFICATIONS/DEEP_LINKS.csv","پارس manifest","static-parse"),
 ("runtime","۲۴ سناریوی زمان‌اجرا تعریف و همه NOT_TESTED است","NOT_TESTED","HIGH","15_RUNTIME_TESTING/RUNTIME_COVERAGE.md","—","none"),
 ("runtime","هیچ اسکرین‌شاتی تولید نشده و هیچ تصویری جعل نشده است","NOT_TESTED","HIGH","03_UI_UX/SCREENSHOTS/README.md","—","none"),
 ("transfer","۳۲ قابلیت در ماتریس انتقال ارزیابی شد: ۸ قرارداد، ۱۲ الگو، ۷ ساخت نو، ۵ نامناسب","INFERRED","MEDIUM","18_KONKUR_TRANSFER/TRANSFER_MATRIX.md","تحلیل","inference"),
]

UNK = [
 ("U01","متن کامل پرامپت LLM به‌صورت لفظی","قید مأموریت از بازتولید محتوای اختصاصی منع می‌کند","ساختار ۹ قاعده و جای‌گاه‌ها مستند شد","08_AI_TUTOR/PROMPT_CONTRACT.md","HIGH"),
 ("U02","بدنهٔ درخواست/پاسخ endpointها","نیازمند اجرا یا MITM (ممنوع)","۲۶۵ stub DTO از نام کلاس","10_BACKEND_API/DTO_SCHEMA/","HIGH"),
 ("U03","فعل HTTP برای Lie0/n (۵ مسیر)","رأی‌ها متناقض (PUT/DELETE/POST)","LOW ثبت شد؛ نیازمند تست مجاز","10_BACKEND_API/VERB_MAPPING.md","MEDIUM"),
 ("U04","مدل/تأمین‌کنندهٔ LLM و سهمیهٔ عددی","در بسته نیست (سرور)","فقط نشانه‌های UI","08_AI_TUTOR/QUOTA_BILLING.md","MEDIUM"),
 ("U05","الگوریتم تمرین هوشمند و تسلط","سمت سرور","مدل پیشنهادی FSRS","07_PEDAGOGY/MASTERY_MODEL.md","HIGH"),
 ("U06","تعریف «درست» در درس کدی","هیچ تستی در کلاینت نیست","سه فرضیه رتبه‌بندی شد","06_EXECUTION_ENGINE/CODE_RUNNER_SPEC.md","HIGH"),
 ("U07","محل اجرای SQL (کلاینت یا سرور)","بدون اجرا","مقایسهٔ ساختاری پیشنهاد شد","05_LESSON_DSL/ANSWER_AND_GRADING_SPEC.md","MEDIUM"),
 ("U08","قواعد تعارض همگام‌سازی","بدون اجرای دو دستگاه","LAST_WRITE_WINS به‌عنوان فرض","11_DATABASE_PERSISTENCE/SYNC_CONFLICTS.md","MEDIUM"),
 ("U09","نسخهٔ Room و رفتار بدون Migration","کلاس Migration موجود نیست","ریسک ثبت شد","11_DATABASE_PERSISTENCE/MIGRATIONS.md","MEDIUM"),
 ("U10","فهرست کامل رویدادهای تحلیلی","بدون decompiler","۲۳۷ شناسه + ۱۸۹ ردیف خام","14_ANALYTICS_NOTIFICATIONS/ANALYTICS_ARCHITECTURE.md","HIGH"),
 ("U11","بدنهٔ /v2/client-config","بدون اجرا","قرارداد پیشنهادی","13_REMOTE_CONFIG/CONFIG_CONTRACTS.md","MEDIUM"),
 ("U12","شناسهٔ محصول و قیمت اشتراک","در Play Console","—","12_SUBSCRIPTIONS/REVENUECAT_INTEGRATION.md","LOW"),
 ("U13","رفتار روزهای زنجیره و منطقهٔ زمانی","سمت سرور","org.joda برای محاسبهٔ محلی","09_PROGRESS_GAMIFICATION/STREAK_MODEL.md","MEDIUM"),
 ("U14","معنای item value تکراری در ۱۲۵ selection","احتمالاً ترتیب، نه کلید","ریسک ثبت شد","05_LESSON_DSL/SEMANTICS_CORRECTION.md","LOW"),
 ("U15","ساختار httpOptions در ۸۵ درس کدی","نمونهٔ کامل یافت نشد","UNKNOWN اعلام شد","06_EXECUTION_ENGINE/CODE_RUNNER_SPEC.md","LOW"),
 ("U16","نقش libsigner.so و libyrf.so","بدون nm/readelf","فقط نام","01_STATIC_CODE/NATIVE_CODE_ANALYSIS.md","MEDIUM"),
 ("U17","برچسب تب‌های نوار پایین و ترتیب گام‌های آنبوردینگ","بدون اجرا","۱۲ fragment + graph","03_UI_UX/NAVIGATION_MAP.md","MEDIUM"),
 ("U18","دسترس‌پذیری واقعی (TalkBack/RTL)","بدون دستگاه","توکن/رشته","03_UI_UX/DESIGN_SYSTEM.md","MEDIUM"),
 ("U19","سیاست نرخ و صفحه‌بندی سرور","بدون مشاهدهٔ پاسخ","UNKNOWN اعلام شد","10_BACKEND_API/RATE_LIMITS.md","MEDIUM"),
 ("U20","کیفیت پاسخ مربی هوشمند","بدون کلید/حساب","۹ قاعده مستند","08_AI_TUTOR/LIMITATIONS.md","HIGH"),
 ("U21","منطق قفل/کلید درس (کدام درس‌ها قفل‌اند)","سمت سرور","رشته‌ها","04_CONTENT_MODEL/CONTENT_GATING_RULES.md","MEDIUM"),
 ("U22","مدل تسلط در SmartPracticeMastered","سمت سرور","نام مودال","07_PEDAGOGY/PRACTICE_ENGINE.md","MEDIUM"),
 ("U23","نقشهٔ کامل علامت‌گذاری نحو به رنگ","۱۱ کلاس + ۹ رنگ","نگاشت پیشنهادی","05_LESSON_DSL/BLOCK_REFERENCE.md","MEDIUM"),
 ("U24","وجود App Links verified (assetlinks)","بدون aapt/شبکه","wildcard ثبت شد","14_ANALYTICS_NOTIFICATIONS/DEEP_LINKS.md","LOW"),
]

FEATURES = [
 ("F001","بستهٔ محتوای چندزبانه","content","VERIFIED_STATIC","HIGH","04_CONTENT_MODEL/CONTENT_DOMAIN_MODEL.md","P0"),
 ("F002","مدل Track/Section/Tutorial/Chapter/Lesson","content","VERIFIED_STATIC","HIGH","04_CONTENT_MODEL/CONTENT_DOMAIN_MODEL.md","P0"),
 ("F003","نسخه‌داری publishSetVersion/tutorialVersion","content","VERIFIED_STATIC","HIGH","04_CONTENT_MODEL/CONTENT_VERSIONING.md","P0"),
 ("F004","نسخهٔ دشوار درس (hardModeContent)","content","VERIFIED_STATIC","HIGH","04_CONTENT_MODEL/CONTENT_DOMAIN_MODEL.md","P2"),
 ("F005","DSL ۲۷ تگی با آفست کاراکتری","dsl","VERIFIED_STATIC","HIGH","05_LESSON_DSL/DSL_SPECIFICATION.md","P0"),
 ("F006","جای خالی چندگانه با چیپ و گزینهٔ انحرافی","dsl","VERIFIED_STATIC","HIGH","05_LESSON_DSL/BLOCK_REFERENCE.md","P0"),
 ("F007","validatedInput (ورودی آزاد)","dsl","VERIFIED_STATIC","HIGH","05_LESSON_DSL/ANSWER_AND_GRADING_SPEC.md","P1"),
 ("F008","selection چندگانه","dsl","VERIFIED_STATIC","HIGH","05_LESSON_DSL/BLOCK_REFERENCE.md","P0"),
 ("F009","بلوک webview با interaction=unlock","dsl","VERIFIED_STATIC","HIGH","05_LESSON_DSL/BLOCK_REFERENCE.md","P3"),
 ("F010","بلوک database/SQL","dsl","VERIFIED_STATIC","HIGH","05_LESSON_DSL/BLOCK_REFERENCE.md","P3"),
 ("F011","بازخورد visible-if (always/wrong/correct)","dsl","VERIFIED_STATIC","HIGH","05_LESSON_DSL/FEEDBACK_RULES.md","P0"),
 ("F012","رنگ‌آمیزی نحو از پیش محاسبه‌شده","dsl","VERIFIED_STATIC","HIGH","05_LESSON_DSL/BLOCK_REFERENCE.md","P2"),
 ("F013","درس کدی با فایل چندگانه","execution","VERIFIED_STATIC","HIGH","06_EXECUTION_ENGINE/CODE_RUNNER_SPEC.md","P3"),
 ("F014","راهنمای پله‌ای (hints)","execution","VERIFIED_STATIC","HIGH","05_LESSON_DSL/FEEDBACK_RULES.md","P1"),
 ("F015","اجرای کد (سمت سرور)","execution","INFERRED","MEDIUM","06_EXECUTION_ENGINE/CODE_RUNNER_SPEC.md","P3"),
 ("F016","ماشین حالت درس با حالت آفلاین","execution","INFERRED","MEDIUM","06_EXECUTION_ENGINE/EXECUTION_STATE_MACHINE.md","P0"),
 ("F017","پیشرفت درس/فصل/آموزش","progress","VERIFIED_STATIC","HIGH","11_DATABASE_PERSISTENCE/ROOM_SCHEMA.md","P0"),
 ("F018","صف آفلاین outbox","progress","VERIFIED_STATIC","HIGH","11_DATABASE_PERSISTENCE/SYNC_CONFLICTS.md","P0"),
 ("F019","شمارش attempts/tries","progress","VERIFIED_STATIC","HIGH","11_DATABASE_PERSISTENCE/ROOM_SCHEMA.md","P0"),
 ("F020","تمرین هوشمند (بازخدمت فصل)","pedagogy","INFERRED","MEDIUM","07_PEDAGOGY/PRACTICE_ENGINE.md","P1"),
 ("F021","مرور فاصله‌دار","pedagogy","UNKNOWN","LOW","07_PEDAGOGY/MASTERY_MODEL.md","P0"),
 ("F022","گراف پیش‌نیاز","pedagogy","UNKNOWN","LOW","07_PEDAGOGY/CURRICULUM_GRAPH.md","P0"),
 ("F023","آزمون زمان‌دار","assessment","UNKNOWN","HIGH","07_PEDAGOGY/PEDAGOGY_OVERVIEW.md","P0"),
 ("F024","تراز/رتبهٔ تخمینی","assessment","UNKNOWN","HIGH","07_PEDAGOGY/PEDAGOGY_OVERVIEW.md","P0"),
 ("F025","مربی هوشمند با ۹ قاعده","ai","VERIFIED_STATIC","HIGH","08_AI_TUTOR/PROMPT_CONTRACT.md","P1"),
 ("F026","پیام فوری ExplainError/ExplainInteractiveMistake","ai","VERIFIED_STATIC","HIGH","08_AI_TUTOR/PROMPT_CONTRACT.md","P1"),
 ("F027","سهمیهٔ پیام مربی","ai","PARTIALLY_VERIFIED","MEDIUM","08_AI_TUTOR/QUOTA_BILLING.md","P1"),
 ("F028","کلید و دروازهٔ درس","gamification","INFERRED","MEDIUM","09_PROGRESS_GAMIFICATION/KEYS_AND_GATING.md","P3"),
 ("F029","XP/Sparks و هدف روزانه","gamification","PARTIALLY_VERIFIED","MEDIUM","09_PROGRESS_GAMIFICATION/XP_AND_LEVELS.md","P2"),
 ("F030","استریک با freeze/repair/چالش","gamification","PARTIALLY_VERIFIED","MEDIUM","09_PROGRESS_GAMIFICATION/STREAK_MODEL.md","P3"),
 ("F031","ویجت زنجیره (Glance)","gamification","VERIFIED_STATIC","HIGH","09_PROGRESS_GAMIFICATION/STREAK_MODEL.md","P2"),
 ("F032","لیگ و لیدربورد (سه نما)","gamification","VERIFIED_STATIC","HIGH","09_PROGRESS_GAMIFICATION/LEADERBOARD.md","P1"),
 ("F033","۶۲ مسیر API با فعل","api","VERIFIED_STATIC","HIGH","10_BACKEND_API/API_ENDPOINTS.json","P0"),
 ("F034","احراز هویت Firebase + Bearer","api","VERIFIED_STATIC","HIGH","10_BACKEND_API/AUTH_MODEL.md","P0"),
 ("F035","پروفایل عمومی و گزارش کاربر","api","VERIFIED_STATIC","HIGH","10_BACKEND_API/API_CATALOG.md","P2"),
 ("F036","اشتراک Pro/MAX با RevenueCat","subs","VERIFIED_STATIC","HIGH","12_SUBSCRIPTIONS/PRODUCT_MODEL.md","P1"),
 ("F037","آزمون رایگان و تخفیف زمان‌دار","subs","PARTIALLY_VERIFIED","MEDIUM","12_SUBSCRIPTIONS/TRIAL_AND_DISCOUNT.md","P3"),
 ("F038","۹ نقطهٔ پی‌وال","subs","PARTIALLY_VERIFIED","MEDIUM","12_SUBSCRIPTIONS/PRODUCT_MODEL.md","—"),
 ("F039","پیکربندی از راه دور و ۲ پرچم","config","VERIFIED_STATIC","HIGH","13_REMOTE_CONFIG/REMOTE_CONFIG_INVENTORY.md","P0"),
 ("F040","آزمایش محتوا (A/B مسیر)","config","VERIFIED_STATIC","HIGH","13_REMOTE_CONFIG/EXPERIMENTS.md","P1"),
 ("F041","تحلیل محصول با Segment/Mixpanel","analytics","VERIFIED_STATIC","HIGH","14_ANALYTICS_NOTIFICATIONS/ANALYTICS_ARCHITECTURE.md","P1"),
 ("F042","اعلان‌های Firebase/Customer.io","analytics","VERIFIED_STATIC","HIGH","14_ANALYTICS_NOTIFICATIONS/NOTIFICATIONS.md","P1"),
 ("F043","۹ deep link","analytics","VERIFIED_STATIC","HIGH","14_ANALYTICS_NOTIFICATIONS/DEEP_LINKS.csv","P2"),
 ("F044","آنبوردینگ ۱۲ گامی","ux","PARTIALLY_VERIFIED","MEDIUM","07_PEDAGOGY/LEARNING_PATH.md","P0"),
 ("F045","۱۹۲ سطح UI و سیستم طراحی","ux","PARTIALLY_VERIFIED","MEDIUM","03_UI_UX/SCREEN_CATALOG.md","P0"),
 ("F046","تغییر آیکون برنامه با activity-alias","ux","INFERRED","MEDIUM","01_STATIC_CODE/ANDROID_COMPONENTS.md","—"),
 ("F047","۹۶۴ رشته در ۱۱۶ locale","ux","VERIFIED_STATIC","HIGH","02_ANDROID_RESOURCES/RESOURCE_CENSUS.md","P1"),
 ("F048","Developer Menu (۵۵ کلاس)","ops","VERIFIED_STATIC","HIGH","01_STATIC_CODE/ANDROID_COMPONENTS.md","—"),
 ("F049","دسترس‌پذیری پایه (contentDescription)","ux","PARTIALLY_VERIFIED","MEDIUM","03_UI_UX/DESIGN_SYSTEM.md","P0"),
 ("F050","پنل تألیف با پیش‌نمایش درس پیش‌نویس","ops","PARTIALLY_VERIFIED","LOW","10_BACKEND_API/API_CATALOG.md","P0"),
]

COVERAGE = [
 ("00 Baseline","90","SUFFICIENT","hash/manifest/permissions/libs/assets کامل؛ native symbols نه"),
 ("01 Static code","45","PARTIAL","ساختار کلاس/فراخوانی/annotation کامل؛ منطق متدها نامعلوم (بدون JADX)"),
 ("02 Resources","70","PARTIAL","سرشماری کامل؛ مقادیر config-محور و ابعاد دقیق per-screen جزئی"),
 ("03 UI/UX","40","PARTIAL","۱۹۲ سطح و ۲۴ حالت؛ بدون اجرا/اسکرین‌شات"),
 ("04 Content model","95","SUFFICIENT","۱۰ بسته پارس و اعتبارسنجی شد"),
 ("05 Lesson DSL","95","SUFFICIENT","۲۷ تگ، ۲۰,۳۰۶ سند، ۰ نقض بازه، پارسر مرجع + ۲۳ آزمون"),
 ("06 Execution engine","60","PARTIAL","تعاملی کامل؛ کدی/SQL تصحیح نامعلوم"),
 ("07 Pedagogy","45","PARTIAL","ساختار و ریتم کامل؛ مدل تسلط/تکرار نامعلوم"),
 ("08 AI tutor","55","PARTIAL","ساختار پرامپت/جریان کامل؛ متن لفظی (قید) و مدل/سهمیه نامعلوم"),
 ("09 Progress/gamification","60","PARTIAL","پیشرفت/outbox کامل؛ فرمول XP/زنجیره سمت سرور"),
 ("10 Backend API","70","PARTIAL","۶۲ مسیر + فعل؛ بدنهٔ پاسخ و مدل خطا نامعلوم"),
 ("11 Local data","85","SUFFICIENT","۳ جدول با فیلدها + الگوی outbox؛ نسخهٔ DB نامعلوم"),
 ("12 Subscriptions","55","PARTIAL","مدل و نقاط؛ شناسه محصول/قیمت/رفتار خرید نامعلوم"),
 ("13 Remote config","40","PARTIAL","۲ پرچم نام‌دار + مکانیزم؛ بدنهٔ config نامعلوم"),
 ("14 Analytics/notif/deeplinks","50","PARTIAL","ابزارها/اعلان/link کامل؛ فهرست رویداد NOT_ACCESSIBLE"),
 ("15 Runtime","0","IMPOSSIBLE","بدون دستگاه/emulator، هر ۲۴ سناریو NOT_TESTED"),
 ("16 Automated tests","80","SUFFICIENT","۲۳ آزمون پارسر سبز؛ آزمون اندروید ندارد"),
 ("17 Build-ready spec","85","SUFFICIENT","ماژول/مدل/API/بک‌لاگ/ریسک کامل (طراحی ما، نه Mimo)"),
 ("18 Konkur transfer","85","SUFFICIENT","۳۲ قابلیت ارزیابی و مرز انتقال صریح"),
]

TEST_COVERAGE = [
 ("DSL parser","unit","23","PASS","21 قدر","۲۳ آزمون pytest روی ۴ فیکسچر + داده گزارش کورپس"),
 ("DSL corpus","validation","20306","PASS","۲۰,۳۰۶ سند","۰ نقض محدودیت بازه؛ ۱۳۷ عیب محتوا ثبت شد"),
 ("Content integrity","validation","10","PASS","۱۰ بسته","startIndex، ارجاع‌ها، تکرار شناسه"),
 ("API catalog","consistency","62","PASS","۶۲ مسیر","diff با ۷۵ literal"),
 ("Runtime journeys","manual","24","NOT_RUN","۲۴ سناریو","بدون دستگاه"),
 ("Android UI","manual","192","NOT_RUN","۱۹۲ سطح","بدون دستگاه"),
 ("Purchase","manual","1","NOT_RUN","—","ممنوع/بدون حساب"),
 ("AI assistant","manual","2","NOT_RUN","۲ حالت","بدون کلید"),
 ("Offline sync","manual","2","NOT_RUN","۲ سناریو","بدون دستگاه"),
 ("Notifications","manual","5","NOT_RUN","۵ نوع","بدون دستگاه"),
]

def w(name, header, rows):
    p = os.path.join(OUT, name)
    with open(p, "w", newline="", encoding="utf-8") as fh:
        cw = csv.writer(fh); cw.writerow(header); cw.writerows(rows)
    print(f"{name}: {len(rows)} rows")

def main():
    ev_rows = []
    for i, (area, claim, status, conf, path, artifact, method) in enumerate(EV, 1):
        ev_rows.append((f"MIMO-EV-{i:06d}", area, claim, status, conf, path, artifact, method))
    # drop the placeholder row
    ev_rows = [r for r in ev_rows if r[3] != "UNKNOWN" or "placeholder" not in r[6]]
    w("MASTER_EVIDENCE_DATABASE.csv",
      ["evidence_id","area","claim_fa","verification_status","confidence","evidence_path","artifact","method"], ev_rows)
    w("MASTER_UNKNOWN_REGISTER.csv",
      ["unknown_id","topic_fa","why_unknown","what_we_have","reference","impact"], UNK)
    w("MASTER_FEATURE_CATALOG.csv",
      ["feature_id","name_fa","area","status","confidence","evidence_path","target_priority"], FEATURES)
    w("MASTER_TEST_COVERAGE.csv",
      ["area","coverage_pct","verdict","note"], COVERAGE)
    w("MASTER_TEST_COVERAGE_DETAIL.csv",
      ["suite","kind","cases","result","scope","note"], TEST_COVERAGE)

if __name__ == "__main__":
    main()
