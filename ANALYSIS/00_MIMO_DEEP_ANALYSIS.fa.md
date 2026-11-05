# تحلیل عمیقِ Mimo 9.35 — گام «شناخت»، نه «ساخت»

> **REVIEW / سند تحلیلی.** این سند **هیچ ساختار تازهای نمیسازد**؛ فقط حاصل رمزگشایی ایستای نرمافزار اورجینال و ممیزی «کلاف سردرگم» ریپو است تا برنامه ریختنِ مرحلهٔ بعد ساده شود. پروتوتایپ v12.5‑fa، MANIFEST، ZIP، کاتالوگها و فایلهای درایو **دستنخورده** ماندند. هیچ ادعای تأیید نهایی، اجرای زنده، یا ساخت محصول در کار نیست.

- منبع واحد: `Mimo_9.35 (1).apk` · ۱۴۲٬۳۵۳٬۴۹۹ بایت · `com.getmimo` · `versionName=9.35` · `versionCode=1792759685`
- SHA‑256: `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`
- تاریخ: ۲۰۲۶‑۱۱‑۰۵ · شاخهٔ کار: `arena/aebb90b7-game`
- کاتالوگهای ماشینخوان همراه: `MIMO_API_SURFACE.json` · `MIMO_CONTENT_SCHEMA.json` · `MIMO_SCORING_MODEL.json` · `REPO_EVIDENCE_MAP.json` · `TOOLCHAIN_TEMP.fa.md`

---

## ۰. خلاصهٔ اجرایی (آنچه امروز واقعاً دست آمد)

| پرسش شما | پاسخ مستند |
|---|---|
| «نرمافزار اورجینال دقیقاً چیه، جز به جز» | یک اپ **دوپوسته** (View/Fragment + Jetpack Compose)، MVVM با Flow، ۱۲ فایل DEX، ۱۰۵٬۶۱۱ رشتهٔ یکتا، ۳۲٬۶۸۴ تایپ، **۶۱ activity + ۶ activity‑alias** / ۱۹ service / ۲۰ receiver / ۸ provider، ۲۴ مجوز، ۱۲ کتابخانهٔ بومی، و **۱۰٬۳۱۷ فایل JSON محتوا** در `assets/`. |
| «سیستم امتیازدهی و نحوهٔ کارکرد» | **چهار لایهٔ ارز** (XP / Sparks / Coins / Keys) + **هدف روزانه** (Casual/Regular/Serious) + **Streak** (freeze/repair/challenge) + **Leaderboard هفتگی** با ۵ لیگ (Wooden→Golden)، صعود top‑15، محافظت لیگ + **Rewards سرورمحور**. فرمولهای عددی هنوز کشف نشدهاند. |
| «قالب فرمها/درسها/درسنامهها/آزمونها بدون هاردکد» | میمو **از قبل کاملاً دادهپیشران** است: `tracks.json` (v753، ۱۹ track / ۱۴۴ section / ۲٬۰۰۲ ارجاع tutorial) ← `tutorial-*.json` (۱٬۰۲۹ فایل انگلیسی / ۱٬۹۴۷ فصل / ۱۸٬۲۷۲ درس) ← یک **DSL اچتیامالگوی درس** با ~۶۰ تگ و ۲ نوع تعامل. پروتوتایپ فعلی برعکس، همهچیز را هاردکد کرده است. |
| «گرههای بخش یادگیری هنوز خوب نشده» | **علت ریشهای پیدا شد**: `PathMapFragment` **۱۰۰٪ Compose است و صفر لایهٔ XML دارد**؛ هندسهٔ پروتوتایپ از `assets/testdata/test-tracks.json` (**v52، یک fixture تست**) و **چک بصری اسکرینشات** گرفته شده، درحالیکه محتوای shipped **v753** است. ۶ گرهٔ ثابت نمیتواند مسیر ۱۹ ترک/۱۴۴ بخش را نمایش دهد. |
| «این کلاف سردرگمِ توی ریپو» | ۷٬۴۳۰ فایل در ۸ ناحیه، ۱٬۵۷۷ داسیهٔ صفحه، ۱٬۲۹۹ لایهٔ دیکدشده، ۵۰٬۴۷۷ ردیف منبع، ۱۲ دور طراحی، ۳۳ اسکریپت build/finalize، ۲٬۸۰۳ مسیر ارجاعشده (۲٬۷۲۵ موجود / **۷۸ گم**). موجودی **کامل** است، آنچه کم است **ترکیب (synthesis)** است. |

---

## ۱. نصب موقت دو ابزار (بهروزشده بعد از تصحیح شما)

> **تصحیح پذیرفته شد**: «بیرون خط لولهٔ اصلی» بهمعنی «نصب نکردن» نبود. صورت وضعیت کامل در
> `TOOLCHAIN_TEMP.fa.md` و §۱۲ همین سند. خلاصهٔ بهروزشده:

| ابزار | وضعیت | نتیجهٔ واقعی |
|---|---|---|
| `morluto/rea` | ✅ **کامل** در `TOOLS/rea/` (submodule پینشده + ۵ سابماژول تو در تو) | `./TOOLS/install.sh` اجرا شد: ۱۱٬۸۵۷ فایل سورس + `rea-agents@6.7.0`. `rea inspect-artifact` روی APK یک **Evidence رسمی** ساخت: `ev_cbbbefbf1ed8230551034c3f9d5ab72b9f19ad938841639ec19fe0a9ceef11b2` با ۱۴٬۰۶۳ گره / ۱۴٬۳۹۹ occurrence / ۱۴٬۳۹۸ یال / **۰ تناقض یکپارچگی**. `rea doctor` همچنان بهدلیل نبود `jdk.compiler` در بیلد PyPI ناسالم است (بند ۴ سند ابزار). |
| `NationalSecurityAgency/ghidra` | ✅ **کامل نصب و اجرا شد** (هم سورس در `TOOLS/ghidra/`، هم باینری رسمی روی رانر گیتهاب) | run `41936300913`: ریلیز `ghidra_12.2_PUBLIC_20261016.zip` (SHA `2c2cd776…`) دانلود، **۵٬۳۲۴ فایل / ۸۸۵M** نصب، `analyzeHeadless` روی ۳ DEX اورجینال اجرا → ۳ برنامهٔ `Dalvik:LE:32:DEX_KitKat` با **۹۰٬۲۴۸ نماد**. شواهد در `ANALYSIS/GHIDRA/`. |
| JADX / REA Android class tools | ✅ موتور دیکامپایل **اجرا شد** | `jadx-mcp.jar` (۴۳٫۸ MB، از npm registry مجاز) روی APK: **۲۴٬۰۲۲ کلاس / ۱۲۹٬۰۷۱ متد / ۷٬۴۲۶٬۴۵۰ دستورالعمل**، خطای سطحکلاس ۰. JADX 1.5.6 از طریق رانر گیتهاب: **۲٬۲۱۱ فایل Java / ۳۸۱٬۴۵۵ خط** در `ANALYSIS/DECOMPILED/`. JAR رسمی `jadx-headless-mcp 0.7.1` هم دانلود و هششد (`6e5eacf5…ff75` = هش مستند REA). |
| موتور جایگزین (همچنان موقت) | ✅ | `androguard 4.1.4` + پارسر مستقیم `string_ids`/`type_ids` DEX + `string.xml` ریپو. تمام اعداد DEX با `CATALOGS/DEX_CENSUS.json` **تکبهدقت جور درآمد** (۵۳٬۷۳۰ / ۵۰٬۲۱۵ / ۱۶٬۷۱۸ رشته). |

**محدودیت بنیادی (سر جای خود باقی است):** با وجود نصب کامل ابزارها، **هیچ اجرای زندهای** (adb/امولاتور/اسکرینشات رانتایم) انجام نشد و بدنهٔ بسیاری از متدهای کروتین Kotlin توسط JADX قابل decode نیست (بند ۵ سند ابزار). پس **همهٔ نتایج، مشاهدهٔ ایستا (static observed) است**؛ رفتار واقعی، ترتیب فراخوانیها و مقادیر سروری «ناشناخته»اند نه «تأییدشده».

---

## ۲. معماری نرمافزار اورجینال (جز به جز)

### ۲٫۱ لایهبندی باینری

| لایه | اندازه / تعداد | نکتهٔ کلیدی |
|---|---|---|
| ZIP entries | ۱۴٬۳۹۸ | ۱۰٬۳۲۷ فایل `.json`، ۲٬۸۶۲ `.xml`، ۲۱۵ `.svg`، ۱۱۷ `.png`، ۱۱۲ `.webp`، ۶۹ `.proto`، ۵۹ `.riv`، ۱۲ `.dex`، ۱۲ `.so` |
| `assets/` | ۱۰٬۵۶۴ فایل | **۱۰ باندل زبانه** `lessons-{de,en,es,fr,id,it,pl,pt,ru,tr}` (هرکدام ~۱٬۰۳۰ فایل، ~۶۰ MB)، ۲۱۵ بنر SVG مشترک، `testdata/`, `mock/`, `spieglein/`, `prettier/`, `beautify/`, `snippets/`, `dexopt/` |
| DEX | ۱۲ فایل | `classes.dex` ۱۶٫۲ MB / ۵۳٬۷۳۰ رشته، `classes2.dex` ۹٫۸ MB / ۵۰٬۲۱۵، `classes3.dex` ۲٫۸ MB / ۱۶٬۷۱۸؛ ۹ تای کوچک ۱٬۰۹۶ بایتی (placeholder). **۱۰۵٬۶۱۱ رشتهٔ یکتا، ۳۲٬۶۸۴ تایپ** |
| منابع | `resources.arsc` | ۵۰٬۴۷۷ ردیف کانفیگ در ریپو، ۱٬۷۲۱ رشته در `values/values/string.xml`، ۱٬۲۹۹ لایهٔ XML دیکدشده |
| Manifest | ۳۹٬۶۲۸ بایت دیکدشده | ۶۱ activity + ۶ activity‑alias، ۱۹ service، ۲۰ receiver، ۸ provider، ۲۴ مجوز، deep link `https://getmimo.com/*` + `mimo://` (مطابق `73_COMPLETE_NAVIGATION_GRAPH.json`) |

### ۲٫۲ نقشهٔ پکیجها (از `type_ids` تمام DEXها)

| پکیج | تایپها | معنا |
|---|---|---|
| `com/getmimo/ui/*` | ۱٬۹۲۳ | `ui/lesson` ۳۱۵ · `ui/chapter` ۱۱۸ · `ui/path` ۱۰۴ · `ui/iap` ۱۲۶ · `ui/onboarding` ۹۵ · `ui/leaderboard` ۵۱ · `ui/profile` ۴۹ · `ui/aitutor` ۳۴ · `ui/streaks` ۲۶ · `ui/practice` ۶۹ · `ui/codeplayground` ۶۵ |
| `com/getmimo/data/*` | ۶۴۹ | `data/source` ۲۰۰ (remote/local) · `data/content` ۱۴۵ · `data/model` ۱۴۰ · `data/local` ۷۱ · `data/settings` ۴۰ |
| `com/getmimo/analytics/*` | ۳۳۷ | عمدتاً `properties` (۳۰۵) — تقریباً هر اقدام کاربر یک رویداد نامگذاریشده دارد |
| `com/getmimo/interactors/*` | ۱۶۰ | `path` ۵۱ · `chapter` ۲۰ · `streak` ۹ · `playgrounds` ۹ · `practice` ۷ · `chapterend` ۶ |
| `com/revenuecat/purchases` | ۲٬۴۳۶ | اشتراک/پرداخت (**طبق دستور شما از دامنهٔ طراحی خارج است**، ولی در باینری وجود دارد) |
| Jetpack Compose / Rive / Customer.io / Adjust / Mixpanel / Segment / Firebase | — | پوستهٔ ترکیبی، انیمیشن Rive، پیامرسانی in‑app، انتساب و تلمتری |

### ۲٫۳ الگوی معماری (تأیید با داسیههای ریپو)

- **دو فناوری رندر همزیست**: درس/آنبوردینگ/ویرایشگر کد = View + Fragment + ViewPager2؛ سطوح جدیدتر (مسیر یادگیری، لیدربورد، انتهای فصل) = **Compose**. داسیهٔ `PathMapFragment.md` صراحتاً «هیچ لایهٔ XML متصل نیست — صفحه Compose یا کتابخانهای» میگوید.
- **MVVM + Coroutines/Flow**؛ VMهای درس «کنترلر imperative»اند، بقیه `StateFlow`. مدلها `PathMapState`, `PathToolbarState`, `TutorialProgress`, `ChapterCompletion`, `RemoteLeaderboardState`.
- **رندر درس**: سند درس ← پارسرهای `te.*` ← مدل بلوکی ← `SpannableStringBuilder` / `PartiallyEditableEditText` / **WebView** ← رویداد کاربر ← verdict ← bind مجدد. یعنی **یک صفحهٔ اسکرولشونده بهازای هر درس**، نه RecyclerView؛ ارزان ولی سقف اندازهٔ درس را محدود میکند.
- **پل WebView** (`assets/lesson-webview.js`): `MimoLesson.postMessage(...)` با پیامهای `gesture` (تشخیص مالکیت لمس بین صفحه و وبویو)، `activity` (`mimo.activity.correct|wrong|completed`)، `focus`، `height`، `ready`. پس **درست/غلط شدن تمرین از داخل JS وبویو به نیتیو گزارش میشود** — نقطهٔ اتصال پداگوژی به سیستم امتیاز.
- **کددارایی محلی**: Room (`chapter_completions`, `tutorial_completions`) + DataStore (`onboarding_user_daily_goal`, `streak_freeze`, `league_freeze`, …) + WorkManager (همگامسازی پیشرفت/ویجت).

---

## ۳. سطح بکاند / کششهای API

فهرست کامل در `MIMO_API_SURFACE.json`: **۸۳ مسیر تمیزشده** (۹۹ رشتهٔ خام شامل توصیفگرهای Kotlin)، ۱۲۳ رشتهٔ `https://`، بیسها `https://api.mimo.org` و `https://api-testing.mimo.org`، موتور اجرای کد `code.gist.build` / `engine.api.gist.build` / `queue.api.local.gist.build:86`.

گروهبندی:

| گروه | نمونه | نقش حدسی (ایستا) |
|---|---|---|
| محتوا/پیشرفت (۱۱) | `/v1/tracks/{trackId}/completion`, `/v1/tutorials/{tutorialId}/progress`, `/v1/tracks/{trackId}/eta`, `/v1/tracks/completion/lastInteracted`, `/v1/practice/statistics` | وضعیت مسیر، ETA، آخرین تعامل، آمار تمرین |
| فایلهای درس (۳) | `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` و `savefiles`، `/v1/tutorials/drafts/.../render` | اجرا/ذخیرهٔ فایلهای `executableFiles` و رندر پیشنویس |
| کاربر (۲۰) | `/v1/user/settings`, `/v1/user/coins`, `/v1/user/keys`, `/v1/user/keys/consume`, `/v1/user/rewards/next`, `/v1/user/rewards/{rewardId}/confirm`, `/v1/user/activity`, `/v1/user/visits`, `/v1/user/favorites/tracks`, `/v1/user/following/{userId}` | تنظیمات، ارزها، پاداشها، تقویم streak، علاقهمندیها |
| لیدربورد (۳) | `/v1/leaderboards/latest`, `/friends`, `/{leaderboardId}/userrank` | جدول هفتگی، دوستان، رتبهٔ من |
| کد / AI (۸) | `/v1/code/runfiles`, `/v1/code/{savedCodeId}/remixes`, `/v1/aiTutor/conversations`, `/v1/aiTutor/conversations/messages/count` | اجرای کد، playgroundها، چت درس |
| گزارش/تشخیص | `/v1/tutorials/{tutorialId}/lessons/{lessonIdentityId}/report`, `/v1/diagnostics`, `/v1/health/connectivity`, `/v1/events`, `/v2/client-config` | گزارش محتوا، سلامت، پیکربندی از دور |
| شخص ثالث | Revenuecat، Adjust، Mixpanel، Customer.io/Gist، Firebase، Segment، AdMob | پرداخت/انتساب/تلمتری/پیام درونبرنامهای |

> ⚠️ **ناشناختههای صریح**: فعل HTTP هر مسیر، اسکیمای درخواست/پاسخ، جریان توکن، سیاست باطلسازی کش آفلاین، و اینکه دقیقاً کدام مسیرها هنگام نمایش یک درس صدا زده میشوند. REA/Ghidra برای همین لایه لازم بودند و در این محیط اجرا نشدند — این **اولویت اول** مرحلهٔ بعد است.

---

## ۴. پداگوژی و قالب محتوا (مهمترین کشف برای «عدم هاردکد»)

### ۴٫۱ سلسلهمراتب واقعی (از `assets/lessons-en/tracks/tracks.json`, `publishSetVersion=753`)

```
publishSet (v753, versioning سراسری)
└── Track           19 تا؛ id, version, title, descriptionContent, onboardingCategory,
│                   isNew, isHidden, iconBanner, sections[], tutorials[]
└── Section         144 تا؛ name, description, startIndex, endIndex, tutorialIds[]
└── Tutorial        2,002 ارجاع / 1,029 فایل انگلیسی (10,298 فایل در ۱۰ زبان)
│                   id, version, type, codeLanguage, title, descriptionContent,
│                   shortDescriptionContent, showInTrack, iconBanner, chapters[]
└── Chapter         1,947 تا؛ id, title, type, lessons[]
└── Lesson          18,272 تا؛ title, id, contentType, images[],
                    interactiveContent | executableContent,
                    hardModeSelected, hardModeContent
```

**enumهای دقیق (شمارش روی کل ۱٬۰۲۹ فایل انگلیسی):**

| سطح | مقادیر | تعداد |
|---|---|---|
| `tutorial.type` | `course`, `practiceRequired`, `practiceOptional`, `guidedProject`, `guidedProjectOptional`, `challenges` | ۵۰۷ / ۱۵۷ / ۱۳۴ / ۷۴ / ۱۱۷ / ۴۰ |
| `codeLanguage` | javascript, python, css, html, sql, node, jsx, swift, typescript, none, bash | ۲۸۳ / ۱۹۵ / ۱۶۹ / ۱۳۹ / ۶۴ / ۴۷ / ۴۶ / ۴۳ / ۲۳ / ۱۹ / ۱ |
| `chapter.type` | `practiceLevel1/2/3`, `challengeLevel0/1/2` | ۸۱۰ / ۱۷۴ / ۵۲۲ / ۴۵ / ۱۴ / ۳۸۲ |
| `lesson.contentType` | `interactive`, `executableFiles` | ۱۴٬۲۴۸ / ۴٬۰۲۴ |
| `interaction.type` | `fillTheGap`, `validatedInput` | ۹٬۹۵۷ / ۱٬۷۷۲ |
| `visible-if` | `always`, `wrong`, `correct` | ۱۸٬۸۶۹ / ۱۹٬۱۰۱ / ۱۷۳ |
| `<code codelang>` | html, javascript, python, jsx, css, sql, swift, typescript, bash, none | ۵٬۲۴۵ / ۵٬۰۳۷ / ۳٬۵۷۵ / … |

### ۴٫۲ DSL درس (قالب قابلتعمیمی که میمو خودش دارد)

`interactiveContent` یک اچتیامال با تگهای سفارشی است. پرتکرارها: `<text value=… type="break" class="keyword|string|number|type|built_in">` (۳۷۱٬۰۸۸)، `<code version="2" codelang name visible-if>` (۸۰٬۸۰۰)، `<content>`, `<interactions>`, `<interaction type isDefault startIndex endIndex>`, `<options>/<option startIndex endIndex correct>`, `<selection multiple iscode>`, `<item value correct>`, `<data content>`, `<header content>`, `<webview version="2" content visible-if>`, `<database bootstrapScript>`, `<tables>/<table>/<row>/<output>`, `<p visible-if="wrong|correct|always">`, `<testimonial>`, `<scoreview>`.

چهار ویژگی ساختاری که برای «قالب گسترش یابنده» حیاتیاند:
1. **نسخهبندی در هر سطح** (`publishSetVersion`, `track.version`, `tutorial.version`, `code.version="2"`, `webview version="2"`) → مهاجرت شما نمیتواند بدون `schemaVersion` باشد.
2. **شرط نمایش بهجای شاخهسازی در کد** (`visible-if=always|correct|wrong`).
3. **حالت سخت** (`hardModeSelected`, `hardModeContent`) بهعنوان جایگزین محتوا، نه منطق جدا.
4. **جدایی محتوا از ارائه**: ۱۰ باندل زبانه با همان `id`ها؛ `lessons-common/icons/` بنرها؛ `testdata/` و `mock/` نمونهها.

> ⚠️ **نسلهای اسکیمای متفاوت همزمان در APK وجود دارند**: `assets/mock/tracks.json` (v44، فیلدهای `difficulty/color/icon/slug`)، `assets/testdata/test-tracks.json` (**v52**، `Make a Website` با ۱۵ بخش / ۲۲۳ tutorialId)، و `assets/lessons-*/tracks/tracks.json` (**v753**، ۱۹ ترک). هر طراحی قالب باید **چندنسلی** باشد.

---

## ۵. سیستم امتیازدهی و نحوهٔ کارکرد (گام دوم شما)

کاتالوگ کامل: `MIMO_SCORING_MODEL.json`. نکتهٔ کلیدی: **XP همان چیزی است که کاربر میبیند؛ Sparks نام داخلی همان افزایش امتیاز است.**

| لایه | واحد | شواهد | نقش |
|---|---|---|---|
| **XP** | `%1$d/%2$d XP` | `xp`, `total_xp`, `xp_earned`, `sparks_daily_goal`, `streak_drawer_daily_xp`, «Compete … for most **weekly XP**», `UserXpInformation(xpFormatted=`, `DOUBLE_XP_GAIN`, `xpHelper` | هدف روزانه + جدول هفتگی + مجموع عمر |
| **Sparks** | ⚡ (نام داخلی) | `rewardedSparksForCorrectAnswer`, `earnedSparks`, `dailySparksGoal`, `DailySparksProgress`, `ChapterFinishedStats(earnedSparks=`, `double_sparks_24h`, `getDailySparksGoal` | پاداش بهازای پاسخ درست/درس؛ پیشرفت هدف روزانه |
| **Coins** | سکه | `/v1/user/coins`, `dailyGoalCoinReward`, `missedCoins`, `userCoins`, «You earned %1$d coins!», «exchange your coins … in the Mimo Store» | ارز فروشگاه؛ با رسیدن به هدف روزانه داده میشود |
| **Keys** | کلید | `/v1/user/keys`, `/v1/user/keys/consume`, `PathToolbarKt$RowWithKeys`, `refreshKeysFlow` | ارز سوم در نوار ابزار مسیر؛ **معنایش هنوز ناشناخته** |

**هدف روزانه**: ۳ سطح `Casual / Regular / Serious` (`daily_goal_level_1..3`)، تنظیم در آنبوردینگ (`OnboardingSetDailyGoalFragment`, `setDailyGoal`, `getUserDailyGoal`)، سه وضعیت `DAILY_GOAL_REACHED / NOT_REACHED / ALREADY_REACHED_EARLIER_TODAY`، نمایش در `DailySparksGoalProgressView` و `ChapterFinishedDailyGoalProgressView`. بلافاصله بعد از فصل: «Make sure you’re online to make your Sparks count towards your daily goal» یعنی **همگامسازی سروری**.

**Streak**: `activeStreakLength`, `longestStreakLength`, `bestStreak`, `userCurrentStreak`, `streakType`, `streakChainType`؛ مکانیزمها `STREAK_FREEZE` / `WEEKEND_FREEZE` / `STREAK_REPAIR` / `FREE_STREAK_REPAIR` / چالشهای `streak_challenge_{3d,5d,7d}`؛ ویجتهای small/medium/large با `WorkManager`؛ صفحات انتهای فصل multi‑day (`chapter_end_streak_*`).

**Leaderboard**: ۵ لیگ دقیق `Wooden → Stone → Bronze → Silver → Golden` (از `string.xml`)؛ «Finish in the **top 15** to advance»؛ ناحیهٔ خطر / سقوط / «league protection» / `hasActiveLeagueFreeze`؛ `RemoteLeaderboardState{Active,NotEnrolled,Error,Result}`؛ `/v1/leaderboards/{latest,friends,{id}/userrank}`؛ `ProfileTrophy(league=…)`؛ انیمیشنهای Lottie `trophy_icon`, `streak_icon`, `streak_animation`.

**Rewards**: کاملاً **سرورمحور** — `/v1/user/rewards/next` ← `/v1/user/rewards/{rewardId}/confirm`، فیلدها `rewardId, rewardAmount, rewardMultiplier, rewardType, rewardEntitlementId, rewardVerificationEnabled, rewardVirtualCurrencyAmount/Code`؛ «Choose a box / Tap to open it» و سه Lottie `reward_mini/medium/maxi`. یعنی کلاینت **نمیتواند خودش امتیاز بدهد**.

**فروشگاه (۱۷ محصول)**: Streak Freeze، Streak Repair (ماهی یکبار رایگان)، League Protection، Double XP Gain (2x / 24h)، Double Sparks و… (طبق تصمیم شما، **پرداخت/اشتراک/Pro وارد طراحی نمیشود**؛ اینجا صرفاً برای فهم مکانیک امتیاز ثبت شد).

> 📌 **یادداشت تطابق با تصمیمهای قبلی شما**: حذف «Wooden League / ردیف رقبا / منطقهٔ صعود» از لیدربورد پروتوتایپ (دور یازدهم) یک **تصمیم طراحی** بود، نه خطای استخراج. اپ اورجینال واقعاً ۵ لیگ و رقابت هفتگی دارد. این سند فقط واقعیت باینری را ثبت میکند و **هیچ تغییری در آن تصمیم نمیدهد**؛ صرفاً مشخص میکند اگر بعداً خواستیم «شبیه اپ واقعی» باشیم، کدام مکانیزمها وجود داشتهاند.

**چرخهٔ واقعی یک درس (ترکیب شواهد)**:
`PathMap → Chapter (ViewPager2 از Lessonها) → WebView/PartiallyEditableEditText → mimo.activity.correct/wrong → Sparks/XP → progress → ChapterFinished (DailyGoal + Streak + Leaderboard + Reward + ETA + Widget) → همگامسازی /v1/tracks/…/completion, /v1/user/activity, /v1/user/rewards/…`.

> ⚠️ **ناشناختههای عددی**: XP دقیق بهازای پاسخ درست/درس/فصل، آستانههای عددی Casual/Regular/Serious، زمان ریست هفتگی و اندازهٔ گروه لیدربورد، قیمت سکهای هر محصول، و فرمول تبدیل `sparks → XP → rank`. اینها یا در بایتکد **`const` operands**اند (نیازمند دیکامپایل JADX/Ghidra) یا **از `/v2/client-config` / Remote Config سرور** میآیند.

---

## ۶. چرا گرههای «یادگیری» هنوز درست نیست (گزارش ریشهای)

| لایه | آنچه پروتوتایپ v12.5‑fa دارد | آنچه APK 9.35 دارد | نتیجه |
|---|---|---|---|
| منبع هندسه | `NODE_CODE_GEOMETRY.json` بر پایهٔ `assets/testdata/test-tracks.json` (**v52**) | `assets/lessons-en/tracks/tracks.json` (**v753**) | ** fixture تست بهجای محتوای shipped ** |
| تعداد گره | ۶ گرهٔ ثابت `l10n1..l10n6` با `left/top` هاردکد در CSS | ۱۹ ترک، ۱۴۴ بخش، ۲٬۰۰۲ ارجاع tutorial | نمایش ۶ گره نمیتواند مدل واقعی را بازنمایی کند |
| فناوری | SVG ایستا با ۲ مسیر `Q` و ۳ لاین (center/right/left) | `PathMapScreenKt` **Compose خالص**، `PathMapFragment` **صفر لایهٔ XML** | خط لولهٔ دیکد AXML ریپو (۱٬۲۹۹ لایه) **اساساً به این صفحه نمیرسد** |
| پارامترها | `node 92dp`، `corner 26dp`، `stroke 10dp`، `gap 24dp`، `elbow 32dp` | `Connector(width=…)`, `ConnectorStyle(width=…)`, `PathItem(fill=…)`, `PathMapState(track=…, sections, tutorialStates, sectionStates, connector, connectorStyle, spotlightType)`, `snapRadius`, `verticalEllipseRadius`, `ringInnerCornerRadiusPx`, `ringOuterCornerRadiusPx`, `sectionHeaderHeight/Radius/BorderWidth`, `offsetXPx/offsetYPx`, `dotRadius`, `touchRadius`, `cropCornerRadius`, `cellHighlightRadius`, `blurRadius`, `circularProgressStrokeWidth` | مدل واقعی **وضعیتمحور و محاسباتی** است، نه چند عدد ثابت |
| درجهٔ اطمینان | خود سند میگوید `26dp is VISUAL_CROSSCHECK_ONLY`، `stroke 10dp` از اسکرینشات، `code_basis` صرفاً ۹۲ کلاس + `test-tracks.json` | ۹۲ کلاس `PathMap*`, `GetPathMapState.kt`, `ObservePathToolbarState`, `PracticeOptionalIntroKt`, `ChapterSpotlightType` | اعداد «حدس بصری تأییدشده با کد» نیستند؛ **هندسهٔ دقیق هنوز استخراج نشده** |

**تشخیص نهایی**: مشکل «خوب نشدن گرهها» یک مشکل CSS نیست؛ **مشکل منبع证据 و مدل داده است**. تا وقتی (۱) بایتکد `PathMapScreenKt` دیکامپایل نشود، (۲) `tracks.json` v753 بهجای fixture جایگزین نشود، و (۳) گرهها از `sectionStates/tutorialStates` تولید نشوند، هر بار فقط ۶ دایرهٔ زیباتر خواهیم ساخت. این دقیقاً همان کاری است که «تحلیل قبل از ساخت» باید جلویش را بگیرد.

---

## ۷. ممیزی «کلاف سردرگم» ریپو

| ناحیه | فایلها | حجم | محتوا |
|---|---:|---:|---|
| `SOURCE/` | ۳٬۷۳۲ | ۳۹٫۴ MB | ۳٬۱۵۶ XML منابع، ۱٬۲۹۹ لایهٔ دیکدشده، ARSC، manifest، DEX census |
| `SCREENS/` | ۱٬۵۷۷ | ۷٫۲ MB | داسیهٔ هر صفحه/کلاس + `LAYOUTS/` (درخت مؤلفهها، رشتهها، رنگها) |
| `UPGRADE/` | ۱٬۹۵۵ | ۲۵٫۶ MB | ۲۵ سند طراحی، ۲۱ کاتالوگ، پروتوتایپ، ۳۳ اسکریپت build/finalize، ۱۲ نسخهٔ HTML |
| `RECONSTRUCTION/` | ۱۰۹ | ۱۴۸ KB | اسکلتهای Kotlin بازساخته از DEX (صریحاً «not decompiled source») |
| `CATALOGS/` | ۱۴ | ۱۸٫۶ MB | `APK_ENTRY_CENSUS`, `RESOURCE_INDEX` (۵۰٬۹۹۴ ردیف داده), `UI_CLASS_INDEX` (۳٬۲۵۵), `DEX_CENSUS`, `LAYOUT_INDEX`, `SCREEN_INDEX`, `COVERAGE_BY_AREA` |
| `ATLAS/` | ۴ | ۲۴٫۷ MB | `index.html` ۱۹ MB، توکنها، `data.json.gz` |
| `REFERENCE/` | ۱۷ | ۱٫۶ MB | `PRIOR_WORK/` (ناوبری، دیزاین سیستم، Rive، دسترسپذیری) + `REA_EVIDENCE/JS_EVIDENCE.json` |
| `tools/` | ۵ | ۱۵۳ KB | ابزارهای استخراج نسل اول |
| **جمع** | **۷٬۴۳۰** | — | ۸ ناحیه، ۱٬۶۴۱ سند `.md` |

**اعتبارسنجی متقابل (انجام شد)**: سرشماری تازهٔ APK دقیقاً ۱۴٬۳۹۸ entry داد و با ۱۴٬۳۹۸ ردیف `APK_ENTRY_CENSUS.csv` **بدون حتی یک اختلاف** جور شد؛ شمارش رشتههای DEX هم با `DEX_CENSUS.json` یکی بود. `COVERAGE_BY_AREA.csv` همهٔ ۲۳ ناحیه را `COMPLETE` اعلام میکند. پس **موجودی کم نیست**.

**آنچه کم است = ترکیب و صحت ارجاع**:

- ۲٬۸۰۳ مسیر در اسناد ارجاع شده؛ ۲٬۷۲۵ موجود، **۷۸ مسیر واقعاً گم** (عمدتاً `mimo/HANDOFF/docs/dsl.md`, `mimo/learn/dsl.js`, `mimo/learn/grade.js`, `mimo/engines/pins.json`, `18_KONKUR_TRANSFER/`, `DESIGN/HABITICA_SCORING.json`, `spieglein/index.html`, اسناد `CRAFT_ANYTHING/upstream_docs/*`). یعنی `07_LESSON_STRUCTURE_AND_QUESTIONS.md` به «۲۷ تگ / ۱۲ ویژگی DSL» و `09_DATA_MODEL_AND_BACKEND.md` به پینهای LearnHarness/EPM ارجاع میدهند **بدون اینکه آن زیرساخت در این چکاوت وجود داشته باشد**.
- `73_COMPLETE_NAVIGATION_GRAPH.json` خودش اعتراف میکند **بازیابی نشده**: `exact route ids`, `bottom-navigation destinations`, `modal/back-stack semantics`, `deep-link path grammar`.
- ۱۲ دور طراحی (v5…v12.5‑fa) + ۴۸ فایل در `UPGRADE/tools` (۳۳ اسکریپت + ۱۵ قالب HTML) + ۴ لایهٔ بنر «superseded» بالای هر سند → خواندن ترتیب حاکم دشوار است.
- **هیچ ایندکس واحدی** وجود ندارد که «صفحه ← لایه ← کلاس DEX ← رشتهٔ ARSC ← endpoint بکاند ← مدل داده ← قانون امتیاز» را بههم وصل کند.

**نتیجهٔ ممیزی**: ریپو یک **آرشیو شواهد درجهیک** است، نه یک **مدل**. اختلاف «طرح» و «واقعیت» از همینجا میآید: مثلاً لیدربورد طراحی ما `XP total / Weekly XP` دارد، درحالیکه اپ واقعی ۴ ارز، ۵ لیگ، و پاداش سرورمحور دارد؛ یا مسیر یادگیری ما ۶ گرهٔ ثابت دارد درحالیکه اپ ۱۹ ترک/۱۴۴ بخش دارد.

---

## ۸. هاردکدهای پروتوتایپ فعلی (چرا «گسترش یابنده» ضروری است)

شمارش روی `UPGRADE/DESIGN/index.html` (۴۳۷٬۹۷۲ بایت): ۱۹ `data-screen`، ۱۳ `<section`، ۱۴ دکمهٔ `data-go`، ۵ `data-tab`، ۶۳ `data-code`، ۷ `data-lh`، ۳ `p.note`، ۶ preset زمان. در JS آن (~۴۰ KB) این ثابتها **داخل کد**اند: `POLICY`, `EXAM_KIND`, `QTOTAL=20`, `QRAW`, `WRONG`, `HIST`, `V11_PROGRAMS`, `V11_COURSES`, `P_FA`, `P_STEMS`, `tabMap`, `tabScreen`, `tabFa`, `ANSWERS/CHECKED/SAVED` و چهار payload عظیم `GEO/LEARN/NODE/KONKUR` (درون `<script>`)، بعلاوهٔ CSS موقعیت `l10n1..l10n6`.

هیچ `schema`، `registry`، `form template`، `lesson template`، `exam template` یا `renderer` عمومی وجود ندارد؛ اضافهکردن یک درس/آزمون/تب = ویرایش HTML. در مقابل، میمو **همهٔ اینها را از JSON میخواند**. این تضاد، صورت مسئلهٔ سوم شماست — و پاسخش در §۴ مستند شد. (`SAVED` همچنان فقط در حافظه است، بدون localStorage؛ محدودیت اعلامشدهٔ قبل پابرجاست.)

---

## ۹. آنچه هنوز نمیدانیم (باید صادقانه پرچم بزنیم)

1. فعل/بدنهٔ HTTP، اسکیمای پاسخ، جریان توکن، سیاست آفلاین (نیازمند JADX/Ghidra یا مشاهدهٔ رانتایم).
2. فرمولهای عددی امتیاز، آستانههای هدف روزانه، ریست هفتگی، قیمتهای فروشگاه، نگاشت `sparks→XP→rank`.
3. هندسهٔ دقیق Compose مسیر (محاسبهٔ `Connector`, لاینها، `spotlight`, `snapRadius`) و قواعد state machine گرهها.
4. معنای دقیق `Keys` و برخی تگهای DSL (`scoreview`, `testimonial`, `database`, `tables`).
5. Back‑stack مودالها، route idها، مقصدهای ناوبری پایین، گرامر deep linkها.
6. ترتیب fall‑back باندلهای ۱۰ زبانه و قواعد انتشار/نسخهبندی سرور محتوا.
7. **عمداً خارج از دامنه (طبق دستور شما)**: اشتراک/Pro/پرداخت، مشاوره، و تحلیل کامل دو اپ ایرانی و پلتفرم LearnHarness/EPM — فقط موجودی آنها ثبت شد: `hamdars` ۸۳۱ فایل / ۱۳٫۴ MB (Flutter)، `hadaf_plus` ۹۷۵ فایل / ۳٫۶ MB، و ارجاعات LearnHarness در ۱۹ فایل اسناد/کاتالوگ (بدون سورس پینشده در چکاوت).

---

## ۱۰. نقشهٔ مرحلهٔ بعد (فقط ترتیب کار؛ **هیچ ساختار/کدی ساخته نشد**)

| گام | کار | معیار پذیرش (برای آن مرحله) |
|---|---|---|
| A | فراهم کردن دیکامپایلر (JADX/Ghidra) در محیطی با دسترسی به ریلیزها، یا افزودن JAR به مخزن | `PathMapScreenKt`, `ChapterFinishedViewModel`, `DefaultLeaderboardRepository`, `DefaultStreakRepository`, `DefaultRewardRepository` به پسودوکد خوانا |
| B | «دفترچهٔ رفتار» هر صفحه: صفحه ← لایه/Compose ← VM ← endpoint ← مدل ← قانون امتیاز | یک جدول واحد برای ۲۷۶ صفحهٔ ثبتشده، جایگزین ۱٬۵۷۷ داسیهٔ پراکنده |
| C | بستن ۷۸ ارجاع گمشده (یا حذف صریحشان) + تعیین «حاکم» میان ۱۲ دور طراحی | `reference integrity = 100%` و یک `CURRENT_DESIGN` مشخص |
| D | استخراج کامل `tracks.json` v753 و مهاجرت از fixture v52؛ استخراج enumها/DSL به **یک اسکیمای نسخهدار** (بدون پیادهسازی) | تمام ۱۹ ترک / ۱۴۴ بخش / ۱٬۰۲۹ tutorial / ۱۸٬۲۷۲ lesson قابلآدرسدهی با شناسه، نه رشتهٔ هاردکد |
| E | مدلسازی کامل امتیازدهی (اعداد + ترتیب رویدادها + نقش سرور) و مستندسازی چرخهٔ درس | هیچ قانون امتیازی بدون شاهد DEX/ARSC/API نماند |
| F | **آنوقت** طراحی قالبهای گسترش یابنده (فرم/درسنامه/آزمون/پروتوتایپ) و پلن پیادهسازی | قالبها از همان اسکیمای D تغذیه شوند و افزودن محتوا = افزودن داده، نه ویرایش کد |

ترتیب **عمدی** است: تا A و B تمام نشوند، طراحی قالب (F) دوباره به همان «۶ گرهٔ ثابت» و «XP تکی» ختم میشود. امروز فقط زمینهای ساخته شد که این ترتیب قابلاجرا باشد.

---

### ۱۱. بازتولید شواهد (برای مرحلهٔ بعد؛ هیچ فایل اجرایی ساخته نشد)

شواهد خام موقتاند ولی **دقیقاً قابل بازتولید**اند. مسیر APK: `/home/user/_work/apk/Mimo_9.35 (1).apk`.

```python
# الف) جدول رشتهها/تایپهای DEX — همان فرمتی که Ghidra/FileFormats/android/dex توصیف میکند
import zipfile, struct, json
z = zipfile.ZipFile(APK)
def uleb(b,o):
    r=s=0
    while True:
        x=b[o]; o+=1; r |= (x&0x7f)<<s
        if not x&0x80: return r,o
        s+=7
def strings(b):
    n,off = struct.unpack_from('<I',b,56)[0], struct.unpack_from('<I',b,60)[0]
    out=[]
    for i in range(n):
        o=struct.unpack_from('<I',b,off+4*i)[0]; _,o=uleb(b,o)
        out.append(b[o:b.find(b'\x00',o)].decode('utf-8','replace'))
    return out
all_str = sum((strings(z.read(x)) for x in z.namelist() if x.endswith('.dex')), [])

# ب) محتوای shipped (بدون fixtureها)
tracks = json.loads(z.read('assets/lessons-en/tracks/tracks.json'))   # publishSetVersion=753
tut    = json.loads(z.read('assets/lessons-en/tracks/tutorial-1001.json'))['tutorial']

# ج) مقایسه با fixture قدیمی (علت مشکل گرهها)
fixture = json.loads(z.read('assets/testdata/test-tracks.json'))      # publishSetVersion=52
```

چهار کاتالوگ JSON کنار این سند، خروجی همین شمارشها هستند و با `mimo-ui/CATALOGS/{DEX_CENSUS.json,APK_ENTRY_CENSUS.csv,COVERAGE_BY_AREA.csv}` ریپو تطبیق داده شدند.

---

## ۱۲. بهروزرسانی بعد از تصحیح شما: پروکسی گیتهاب، نصب کامل، فایل اورجینال، دیکامپایل

> این بخش پاسخ مستقیم به «نصب نکردی چون موقتی/بیرون خط لولهای» است.
> **پذیرفته شد**؛ الان نصب کامل انجام شده ولی همچنان جدای `mimo-ui/UPGRADE` است.
> جزئیات اجرایی در `TOOLCHAIN_TEMP.fa.md`، `TOOLS/README.fa.md`، `ANALYSIS/GHIDRA/INSTALL.md`
> و `ANALYSIS/DECOMPILED/REPORT.md`.

### ۱۲٫۱ فایل اورجینال Drive، دقیقاً همان فایلی است که تحلیل شد

پوشهٔ `mimo` Drive (`1yU1PN1GhTZlDeu91H4FSS0JsOT5MjpxB`) یک **آرشیو ۳ تکهای** است:

| قطعه | بایت | SHA‑256 (جور با متاداتای Drive ✔) |
|---|---|---|
| `Mimo_9.35 (1).z01` | ۵۲٬۴۲۸٬۸۰۰ | `1e3a41159ebe531121f0b04f146791fe900605c7ac15cc9cf54b1501d3b93b18` |
| `Mimo_9.35 (1).z02` | ۵۲٬۴۲۸٬۸۰۰ | `1ac22ab2c916f302d8ba0fd42317f1cb79ea53eb6045061d0a174993a634f539` |
| `Mimo_9.35 (1).zip` | ۳۱٬۰۶۹٬۳۶۸ | `91c670864fc66d852b371ed83c1f6d260ab4075c078030f74b29620807ffa2b7` |

الحاق = ۱۳۵٬۹۲۶٬۹۶۸ B ← دقیقاً **یک عضو**: `Mimo_9.35 (1).apk`، ۱۴۲٬۳۵۳٬۴۹۹ B، `CRC32=0x94bc6bf2`.
CRC و SHA‑256 APK محلی با آن یکساناند (`48ce1740…f7c7a`). یعنی **هیچ نسخهٔ متفاوتی وجود ندارد**؛
«همهٔ پیچ و مهرهها» = ۳ قطعه + APK + ۱۲ DEX + ۱۴٬۳۹۸ entry + ۱۰٬۳۵۲ فایل `assets/` + ARSC + Manifest + ۱۰ باندل زبان.

### ۱۲٫۲ نصب کامل، در یک پوشهٔ جداگانه در گیتهاب

| پوشه | ریپو | کامیت پینشده | فایلها |
|---|---|---|---|
| `TOOLS/ghidra/` | `NationalSecurityAgency/ghidra` @ `master` | `4cfb27de…7072` | ۲۰٬۶۵۵ |
| `TOOLS/rea/` | `morluto/rea` @ `main` | `71f680d7…105f` | ۱۱٬۸۵۷ (با ۵ سابماژول تو در تو) |

`./TOOLS/install.sh` اجرا و موفق شد: `git submodule update --init --recursive` + npm + PyPI.
همهٔ خروجیهای تولیدی زیر `TOOLS/_*/`اند و توسط `.gitignore` وارد ZIP/MANIFEST نمیشوند.

### ۱۲٫۳ Ghidra واقعاً نصب و اجرا شد (GitHub Actions = پروکسی)

run `41936300913` (۹/۹ گام ✓): ریلیز رسمی `ghidra_12.2_PUBLIC_20261016.zip`
(SHA `2c2cd776db3c1f6a097ba418922378ac3649cadd5e844a6f5f088ae628a7be67`) دانلود،
**۵٬۳۲۴ فایل / ۸۸۵M** استخراج، `Temurin-25.0.5+8` نصب، و
`analyzeHeadless ... -import classes.dex classes2.dex classes3.dex -postScript MimoGhidraReport.java`
اجرا شد → ۳ برنامهٔ `Dalvik:LE:32:DEX_KitKat`، **۹۰٬۲۴۸ نماد**، `Import succeeded`.
همان رانر `jadx-headless-mcp-0.7.1-all.jar` را هم گرفت و هش آن
`6e5eacf500b64292bfb73c49797c1958f6ee44646e43e868039ae7feb573ff75` دقیقاً با مستندات REA جور شد.
پس «به VPN/فایل دستی نیاز افتاد» پیش نیامد — مسیر گیتهاب کافی بود.

### ۱۲٫۴ دیکامپایل کامل (دو کانال)

| کانال | نتیجه |
|---|---|
| npm registry → `jadx-mcp@1.4.1` (۴۳٫۸ MB JAR، JADX مدرن) | APK لود شد: **۲۴٬۰۲۲ کلاس / ۱۲۹٬۰۷۱ متد / ۷٬۴۲۶٬۴۵۰ دستورالعمل**، `errors=0` در سطح کلاس، ۲۱ ابزار MCP فعال (`get_class_source`, `search_code`, xrefs, …) |
| رانر گیتهاب → JADX 1.5.6 | `classes.dex` → **۲٬۲۱۱ فایل Java `com.getmimo` / ۳۸۱٬۴۵۵ خط**، بستهٔ `ANALYSIS/DECOMPILED/getmimo_sources.tar.gz` (SHA `ec7af3a7…c74c`) |
| JADX 1.1.0 محلی | ۱۱٬۸۴۴ فایل Java / ۱۳۵ MB؛ از این خروجی **۵۳ تعریف Retrofit** استخراج شد |

### ۱۲٫۵ کشف تازه: سطح API، این بار از کد دیکامپایلشده (نه حدس رشتهای)

`ANALYSIS/MIMO_RETROFIT_ENDPOINTS.json` شامل **۵۳ نقطهٔ پایانی** با مسیر، فایل منبع،
امضای متد و آنوتیشنها است (R8 نام کلاسهای Retrofit را Obfuscate کرده؛ فعلها از روی نام/معنای متد
استنتاج شدهاند: `f=GET` ۲۶، `o=POST` ۲۱، `n=PUT` ۳، `p=DELETE` ۲، و ۱ مورد `POST/other` — **رانتایم مشاهده نشده**).
نمونههایی که مستقیماً به پرسشهای شما مربوطاند:

| مسیر | امضای دیکامپایلشده | معنا |
|---|---|---|
| `/v1/leaderboards/latest` | `Object a(d70.b<? super o0<Leaderboard>>)` | جدول هفتگی فعلی |
| `/v1/leaderboards/{leaderboardId}/userrank` | `Object b(@s("leaderboardId") long, …)` | رتبهٔ کاربر |
| `/v1/user/rewards/next`, `/v1/user/rewards/{rewardId}/confirm` | `lh/a.java` | **پاداش سرورمحور** (§۵ تأیید شد) |
| `/v1/user/keys`, `/v1/user/keys/consume` | `bh/a.java` | ارز `Keys` |
| `/v1/user/coins`, `/v1/user/activity` | `qg/a.java`, `sh/h.java` | ارز `Coins` + تقویم Streak |
| `/v1/user/settings` | `Object a(@a Settings, …)` | هدف روزانه / تنظیمات |
| `/v1/tutorials/{tutorialId}/progress` | `postProgress(@s("tutorialId") long, @a PostProgressRequestBody, …)` | **همگامسازی پیشرفت درس** |
| `/v1/tracks/{trackId}/completion`, `/eta`, `/certificates` | `CompletionApi`, `TrackEtaApi`, `og/a.java` | وضعیت ترک، ETA، گواهی |
| `/v1/tracks/{trackId}/tutorials/{tutorialId}/chapters/{chapterId}/lessons/{lessonId}/runFiles` | `hg/c.java` | پول اجرای کد/پروژه |
| `/v1/practice/statistics`, `/v1/aiTutor/conversations/messages/count` | `hh/a.java`, `jg/a.java` | آمار تمرین + سهمیهٔ AI |
| `/v2/client-config` | `lg/a.java` | پیکربندی سمت سرور (نسخهبندی محتوا) |

این جدول §۳ و بند ۱ از §۹ («فعل/بدنهٔ HTTP») را تا سطح **تعریف اینترفیس** پر میکند؛
بدنهٔ پاسخ/توکن/سیاست آفلاین همچنان ناشناخته است.

### ۱۲٫۶ محدودیت فنی تازه (باید صادقانه بماند)

هر سه JADX روی **بدنهٔ متدهای کروتین** شکست خوردند: JADX 1.1.0 ← `bogus element_width`،
JADX مدرن ← `newPosition > limit`، JADX 1.5.6 ← `243002 errors` / ۱۱٬۶۲۸ استاب `Method not decompiled`.
هدر DEX استاندارد است (`dex\n039\0`، ۱۸ ورودی معمولی `map_list`، بدون call‑site/method‑handle/hiddenapi)؛
پس مشکل خرابی فایل نیست، بلکه ترکیب R8 + `SuspendLambda` است. Ghidra در عوض هر سه DEX را با ۹۰٬۲۴۸ نماد import کرد.
نتیجه: **امضاها، `@Metadata` کاتلین، آنوتیشنهای Retrofit، رشتهها و تمام محتوای shipped کاملاند؛
فرمول عددی امتیاز و هندسهٔ دقیق `com.getmimo.ui.path.map.k` همچنان بستهاند.**
علت ریشهای گرههای غلط (§۶: fixture v52 در برابر shipped v753) سر جای خود و بدون تغییر است.

### ۱۲٫۷ ایزولاسیون، دوباره اندازهگیری شد

- `verify_upgrade.py mimo-ui/UPGRADE` → `PASS 259/259`, `files_hashed=1954` (بعد از همهٔ کارها).
- `U/DESIGN/index.html` → `200` / ۴۳۷٬۹۷۲ B، بدون تغییر.
- `git diff -- mimo-ui/UPGRADE` خالی است؛ هیچ فایلی وارد ZIP/MANIFEST/وریفایر/پوشهٔ v12 در Drive نشد.
- **هیچ ساختار/کد/محصول تازهای ساخته نشد**؛ فقط شواهد و ابزارهای موقت. هیچ VPN واقعی، اجرای زنده،
  یا **تأیید نهایی** ادعا نشد. `SAVED` پروتوتایپ فقط در حافظه است، نه localStorage.

---

### ۱۳. اصلاح مسیر تحلیل: زنجیرهٔ واقعی بهجای ابزار بیشتر (REVIEW، تأییدنشده)

پس از اصلاحیهٔ معماری کاربر، **هیچ ابزار تازهای اضافه نشد**؛ REA/Ghidra حفظ شدند و مسیر تحلیل اصلاح گردید.
جزئیات کامل در `ANALYSIS/01_ANALYSIS_CHAIN.fa.md`؛ خلاصهٔ شواهد:

- **همهٔ ۱۲ DEX** در `ANALYSIS/_INPUT/` و `DEX_INVENTORY.json` (۲۸٬۸۳۶٬۰۸۸ بایت) موجود و توسط Ghidra import شدند
  (`DEX_COVERAGE.txt`)؛ پیش از این فقط ۳ DEX و `-noanalysis` بود.
- **Auto Analysis واقعی روی هر ۱۲ DEX**: ۵۴٬۵۳۰ + ۵۳٬۲۴۷ + ۱۴٬۷۰۴ + ۴۱ + ۳×۸ = **۱۲۲٬۵۴۶ تابع** و
  **۱٬۲۸۴٬۵۴۲ نماد** (قبلاً `functions=0`). خروجی دستورالعمل Dalvik در `ANALYSIS/GHIDRA/CONTROL_FLOW.txt`
  شامل ۶۰ تابع `ui::path::map` و ۶۲ تابع نمره/اتمام است.
- **دو JDK جدا**: Temurin ۲۵ برای Ghidra، **full Temurin ۲۱ با `jdk.compiler@21.0.13`** برای REA؛
  `rea doctor --provider jadx` → `healthy:true` ولی `environment_healthy:false` (drift نسخهٔ Ghidra ۱۲٫۲ در برابر
  انتظار ۱۲٫۱.x، و Hopper/IDA خارج از دامنه). سلامت کامل محیط REA ادعا نمیشود.
- **Smali**: baksmali ۲.۳.۴ و apktool ۲.۹.۳ (smali مدرن ۳.x) هر دو روی `classes.dex` دقیقاً ۱۱٬۸۲۸ شکست
  `Invalid element width` میدهند؛ پس مشکل نسخهٔ ابزار نیست. ۱۷٬۶۲۶ فایل smali تولید شد ولی
  **۰ فایل برای `com/getmimo/ui/path/map`**؛ پوشش کامل Smali ادعا نمیشود و جای آن را Ghidra پر کرد.
- **ماشین حالت coroutine**: ۵۳۹ آنوتیشن `@f70/c` (= `DebugMetadata`، فقط `c/f/l/m/v`؛ جدول `n/i/s` توسط R8 حذف شده)،
  ۸۴ فیلد `label/L$/I$/J$`، ۶۵۲ کلاس suspend در `COROUTINE_STATE_MACHINES.json`.
- **هدف ۱ (نقشه مسیر)**: shipped v753 = ۱۹ مسیر / ۱۴۴ section / ۲٬۰۰۲ tutorial با `startIndex/endIndex`
  کاملاً پیوسته (۰ نقض) و ۶ نوع گره؛ **هیچ `x/y`ای در JSONهای محتوا نیست** (فقط Lottie)، یعنی مختصات در کد
  Compose محاسبه میشود. نام فیلدهای هندسی/اسکرول (`chapterIndexInSection`, `columnCount`, `mainAxisSpacing`,
  `scrollPositionX`, `verticalEllipseRadius`, …) در `MIMO_COMPLETION_ENGINE.json` ثبت شد؛ ولی **۰ xref** در Ghidra
  (آنالایزر Reference در PSPEC غیرفعال است) یعنی نسبت قطعی فیلد→کلاس هنوز باز است.
- **هدف ۲ (نمره/اتمام)**: `LessonProgress` با ۱۱ مؤلفه و getterها، سازنده
  `(LessonBundle, Instant, I, I)`، `isSolvedCorrectly` → `intField >= 1`؛ `LessonProgressQueue` با ۷ متد؛
  جداول Room `chapter_completions` / `tutorial_completions` با SQL کامل؛
  `PostProgressResponse::getDailyGoalCoinReward` و `/v1/user/rewards/{rewardId}/confirm` یعنی پاداش server‑confirm است؛
  فیلدهای `rewardedSparksForCorrectAnswer` / `rewardMultiplier` / `correctLessonsFirstTry` و صفحههای
  `ChapterFinished*` / ETA ¼‑½‑«۳ درس مانده» شناسایی شدند. **ضرایب عددی و ترتیب دقیق صفحهها ناشناختهاند.**
- **محدودیت پابرجا**: بدون emulator/ADB/لاگ/اسکرینشات، **هیچ ادعای پیکسلبهپیکسل** دربارهٔ گرهها/منحنی/اسکرول
  معتبر نیست. JADX بیشتر روی کل APK اجرا نشد؛ JEB اضافه/خریداری نشد؛ رفتار runtime/سرور مشاهده نشد.
- `mimo-ui/UPGRADE`، ZIP، MANIFEST، وریفایر و طرح v12 در Drive همچنان **بدون تغییر**؛
  تأیید نهایی v12.5‑fa و این اصلاحیه هر دو **انجام نشده**اند. `SAVED` فقط در حافظه است.

---

### پیوست: اصل «شاهد» (از متدولوژی REA)

همهٔ ادعاهای این سند از یکی از این سه منبع است: **(۱)** بایتهای shipped APK (هش بالا)، **(۲)** فایلهای استخراجشدهٔ ریپو، **(۳)** جدول `string_ids` DEX. جایی که نتیجه حدسی یا ناقص است، با ⚠️ / «ناشناخته» مشخص شده. هیچ ادعایی دربارهٔ **اجرای زنده**، **رفتار سرور**، یا **تأیید کاربر** وجود ندارد.
