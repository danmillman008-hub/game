**REVIEW — تحلیل موتور مسیر یادگیری. هیچ مقدار `dp`، فرمول مختصات یا ادعای پیکسلبهپیکسل ارائه نمیشود.**
منبع حقیقت: APK اصلی Mimo 9.35 (`sha256=48ce1740…`); دادهٔ shipped **v753** مقدم بر fixture قدیمی v52 است.
`RUNTIME VERIFIED` = ۰.

---

# LEARNING_PATH_ENGINE — گرهها، بخشها، هندسه، اسکرول، پیشرفت

## ۱. مدل دادهٔ shipped v753 — `OBSERVED / HIGH`

فایل `assets/lessons-en/tracks/tracks.json`، `publishSetVersion = 753`:

| کمیت | مقدار | شاهد |
|---|---|---|
| Track | ۱۹ | آرایهٔ `tracks` |
| Section | ۱۴۴ | مجموع `sections[]` |
| ارجاع Tutorial | ۲٬۰۰۲ | مجموع `tutorials[]` |
| کلید track | `id, version, title, descriptionContent, onboardingCategory, isNew, isHidden, iconBanner, sections, tutorials` | `OBSERVED` |
| کلید section | `name, description, startIndex, endIndex, tutorialIds` | `OBSERVED` |
| کلید tutorial ref | `id, version, type, title` | `OBSERVED` |
| انواع گره | `course` ۱٬۰۰۸ · `practiceRequired` ۳۲۱ · `practiceOptional` ۲۸۸ · `guidedProjectOptional` ۲۱۷ · `guidedProject` ۱۱۰ · `challenges` ۵۸ | `OBSERVED` |
| پیوستگی `startIndex/endIndex` | **۰ نقض** در تمام ۱۴۴ section | بررسی برنامهای، `OBSERVED` |

بزرگترین مسیرها: Full‑Stack Developer (id=۵۰) **۴۹۲ گره / ۲۰ section**،
Front‑End Developer ۳۷۶، Game Development ۲۱۹، Back‑End ۲۰۸، Python Developer ۱۸۰.

### نتیجهٔ کلیدی (باز هم `OBSERVED`)
در پویش **تمام ۱۰٬۳۱۷ JSON داخل APK** هیچ کلید `x`, `y`, `nodeX`, `bezier`,
`spacing`, `pathOffset` در دادههای مسیر/درس وجود ندارد. تنها `x/y`ها در انیمیشنهای Lottie هستند
(`res/raw/onboarding_curriculum.json` یک Lottie ۳۳۲×۶۳۱ با ۲۰۱ فریم است، **نه** نقشهٔ مسیر).
→ **مختصات گرهها دادهمحور نیست؛ در کد Compose محاسبه میشود.** `tracks.json` فقط
ترتیب، نوع، برچسب و مرز بخشها را میدهد.

### v52 در برابر v753
`testdata/test-tracks.json` (v52) دارای `difficulty`, `color`, `shortDescriptionContent`, `slug`, `icon`
است؛ v753 **ندارد** و بهجای آن `onboardingCategory` و `sections[].startIndex/endIndex` دارد.
v52 **هرگز** منبع حقیقت نیست.

## ۲. زنجیرهٔ بارگذاری و انتخاب (`STATICALLY INFERRED` مگر ذکر شود)

```mermaid
flowchart TD
  A[assets tracks.json v753<br/>OBSERVED] --> B[DefaultTracksRepository<br/>OBSERVED: نام کلاس]
  B --> C[GetPathMapState<br/>OBSERVED: classes.dex @0x509a8d88..0x509a9ae4]
  C --> D[PathMapViewModel<br/>OBSERVED: نام + اکشنها]
  D --> E[PathMapScreenKt / ViewsKt.PathMap<br/>OBSERVED: نام فایل .kt]
  E --> F[Compose LazyColumn + Path drawing<br/>INFERRED]
  G[CompletionRepository / LessonProgress<br/>OBSERVED: جداول Room] --> C
  H[GET /v1/tracks/{trackId}/completion<br/>OBSERVED: رشته مسیر] --> C
  I[GET /v1/tracks/completion/lastInteracted] --> D
  J[GET /v1/tracks/{trackId}/eta] --> D
```

**ترتیب Tutorial (`OBSERVED`)**: ایندکس در `tutorials[]`.
**مرز Section (`OBSERVED`)**: `startIndex` = `endIndex` بخش قبل + ۱؛ آخرین `endIndex` = `len(tutorials)-1`.
**انتخاب درس جاری**: `lastInteracted` و `sectionIndex` / `chapterIndexInSection` بهعنوان رشتههایوضعیت
دیده شدند، ولی **الگوریتم دقیق انتخاب `UNKNOWN`** است.
** وضعیت گرههای قفلشده/تمامشده**: جداول `tutorial_completions.is_completed` و `chapter_completions`
`OBSERVED`اند؛ نگاشت آنها به رنگ/آیکون/انیمیشن گره `UNKNOWN`.

## ۳. واحدهای Compose شناساییشده — `OBSERVED` (نام) / `INFERRED` (نقش)

فایلهای منبع کاتلین بازیافته از `DebugMetadata.f` و توصیفگرها:
`PathMapScreen.kt`, `PathMapViewModel.kt`, `Views.kt`, `PathToolbar.kt`,
`TutorialSpotlight.kt`, `PracticeOptionalIntro.kt`, `ResubscribeMascotOverlay.kt`,
`GetPathMapState.kt`, `GetPathMapDialogs.kt`.

| عملیات | کلاس/متد | DEX / آدرس | وضعیت |
|---|---|---|---|
| ریشهٔ صفحه | `com::getmimo::ui::path::map::PathMapFragment$onCreate$1::invokeSuspend` | `classes.dex @0x50aa5178` | `OBSERVED` (بدنهٔ ۱۶۶ بایت) |
| کامپوزابل اصلی | `ViewsKt$PathMap$...` / `PathMapScreenKt$PathMapScreen$...` | `classes.dex` (۷۵ کلاس در بسته) | `OBSERVED` (نام)، مسئولیت دقیق `INFERRED` |
| State interactor | `GetPathMapState$invoke$1..3`, `$getProBannerState$1`, `$subscriptionAndKeysFlow$1` | `@0x509a8d88 … 0x509a9ae4` | `OBSERVED` |
| Dialogها | `GetPathMapDialogs$getCertificateUpgradeDialog$1`, `$getFriendsDialog$1`, `$invoke$2` | `@0x509a85cc … 0x509a8900` | `OBSERVED` |
| ViewModel اکشنها | `refreshPathMapState`, `fetchTrackEta`, `navigateToChapter`, `onTutorialClick`, `onNextSectionShown`, `onCertificateClick`, `setHardModeEnabled`, `shouldStartChapterInHardMode`, `refreshDialogs`, `catchGenericError`, `pathOverviewTooltipState` | `classes.dex` | `OBSERVED` (نام کلاسهای لامبدا) |
| job اسکرول/انیمیشن | `PathMapScreenKt$PathMapScreen$10$1$job$1::invokeSuspend` | `@0x50aa64b8` | `OBSERVED` ۳۵ دستورالعمل؛ **معنای دقیق `UNKNOWN`** |
| رسم منحنی | `libandroidx.graphics.path.so` + `androidx.compose.ui.graphics.Path` (۱.۱۲.۱) | ۲ ABI | `OBSERVED` (وجود کتابخانه) / `INFERRED` (استفاده) |

`PathMapFragment` فاقد XML چیدمان برای نقشه است (۰ لایه) → تماماً Compose.

## ۴. هندسه — **صریحاً UNKNOWN، بدون اختراع عدد**

**منبع الف — ۳۱ قطعهٔ `toString()` کاتلین در `MIMO_COMPLETION_ENGINE.json` (`path_map_state_fields`)،
همگی `OBSERVED / HIGH` بهعنوان رشتهٔ DEX:**

| دسته | نام فیلدها (متن دقیق رشته) |
|---|---|
| ایندکس/ساختار | `activeModalNodeId`, `activeNodeIds`, `ancestorNodeIds`, `chapterIndex`, `chapterIndexInSection`, `childNodes`, `childrenByNodeId`, `columnCount`, `columnGutter`, `currentNodeId`, `sectionIndex`, `selectedSectionIndex` |
| فاصله/شعاع | `crossAxisArrangementSpacing`, `dotRadius`, `groupOffset`, `itemSpacing`, `mainAxisSpacing`, `radiusY`, `sectionHeaderRadius`, `snapRadius`, `touchRadius`, `verticalEllipseRadius` |
| منحنی/موقعیت | `borderPath`, `boxPosition`, `offsetXPx`, `offsetYPx` |
| اسکرول | `instructionsScrollOffset` |
| ETA | `currentSectionEstimatedCompletionAt`, `currentTrackTitle`, `forcePathOverviewEtaEnabled` |

**منبع ب — رشتههای تکمیلی با مکان دقیق DEX (`dexlib.py`، پارسر مستقل، `OBSERVED / HIGH`):**

| رشتهٔ دقیق | DEX | string index | `string_data` offset | وضعیت |
|---|---|---|---|---|
| `' scrollPosition='` | `classes.dex` | ۱۶۵۶ | `0x1e9081` | `OBSERVED` |
| `' scrollPositionX='` | `classes.dex` | ۱۶۵۷ | `0x1e9093` | `OBSERVED` |
| `'} scrollPositionY='` | `classes.dex` | ۵۳۷۲۰ | `0x36528c` | `OBSERVED` |
| `', instructionsScrollOffset='` | `classes.dex` | ۴۴۲۰ | `0x202266` | `OBSERVED` |
| `', panOffset='` | `classes.dex` | ۴۸۲۳ | `0x203fb9` | `OBSERVED` |
| `', boxRadius='` | `classes.dex` | ۳۸۹۱ | `0x1ffc63` | `OBSERVED` |
| `', offsetX='`, `', offsetXPx='`, `', offsetY='`, `', offsetYPx='`, `', pageSpacing='`, `', cornerRadius='` | **`classes2.dex`** | ۳۷۳۸–۳۷۴۱، ۳۸۰۳، ۳۲۰۹ | `0x712ea7…0x710728` | `OBSERVED` — احتمالاً از کتابخانههای همراه (ازجمله `revenuecatui/.../carousel/CarouselComponentState$pageSpacing$2` در همان DEX)، **انتساب به نقشهٔ Mimo قطعی نیست** |

> ⚠️ **xref رشته→تابع Ghidra برابر ۰ است** (آنالایزر Reference در PSPEC غیرفعال)، بنابراین
> **نمیتوان گفت کدام فیلد متعلق به کدام کلاس است**. برخی نامها ممکن است از کتابخانههای همراه
> (Compose / RevenueCat / CodeMirror / Rive) باشند. هیچ انتساب قطعی ادعا نمیشود.
> «وجود رشتهٔ نام فیلد» **بههیچوجه** بهمعنی «بازیابی مقدار یا فرمول» نیست.
> شناسهٔ شاهد: `EV-0186`, `EV-0187`, `EV-0188`, `EV-0189`, `EV-0190` (`EVIDENCE_INDEX.json`).

| مؤلفهٔ درخواستی | وضعیت | دلیل |
|---|---|---|
| مختصات X | `UNKNOWN` | ثابتهای `const/high16`/float بدنهٔ کامپوزابل R8شده استخراج نشد |
| مختصات Y | `UNKNOWN` | همان |
| فاصلهٔ عمودی/افقی | `UNKNOWN` | فقط نام فیلدها، بدون مقدار |
| آرایش ستونها | `UNKNOWN` | `columnCount` رشته وجود دارد، بدنهٔ محاسبه نامشخص |
| تابع منحنی | `UNKNOWN` | `verticalEllipseRadius`/`radiusY` رشتهاند، فرمولی مشاهده نشد |
| آفست اسکرول / بازیابی اسکرول | `UNKNOWN` | `scrollPosition`, `scrollPositionX`, `scrollPositionY`, `instructionsScrollOffset` رشتهاند (مکان دقیق در جدول بالا)؛ `SaveableStateRegistry` در وابستگیها `INFERRED` |
| انیمیشن | `UNKNOWN` | فقط `job$1::invokeSuspend` در سطح دستورالعمل |
| وضعیت بصری گرهها | `UNKNOWN` | ۶ نوع `type` مشاهده شد، نگاشت به ظاهر مشاهده نشد |
| انتقال بین بخشها | `UNKNOWN` | `onNextSectionShown$1$1` نام کلاس است، منطقش بازسازی نشد |

**هیچ `dp`، ضریب یا فرمولی جعل نشده است** (قید «Do not invent dp values or coordinate formulas»).

## ۵. همگامسازی پیشرفت — `OBSERVED` (رشته/جدول) / `INFERRED` (جریان)

| شاهد | منبع | وضعیت |
|---|---|---|
| `GET /v1/tracks/{trackId}/completion` | آنوتیشن Retrofit (فعل INFERRED) | `OBSERVED` |
| `GET /v1/tracks/completion/lastInteracted` | همان | `OBSERVED` |
| `GET /v1/tracks/{trackId}/eta` | همان | `OBSERVED` |
| `POST /v1/tutorials/{tutorialId}/progress` | همان | `OBSERVED` |
| `SELECT * FROM chapter_completions WHERE track_id = ?` / `SELECT COUNT(DISTINCT chapter_id) …` | رشتهٔ SQL در DEX | `OBSERVED` |
| `CompletionRepository.fetchTrackCompletion`, `fetchLastInteractedTrackId`, `getChapterCompletionCount`, `getRecentlyCompletedTutorialTitles` | Ghidra `classes.dex @0x50984214 … 0x50984750` | `OBSERVED` |
| `attachTutorialCompletionToTrack` / `attachTutorialAndChapterCompletionToTrack` | نام متد | `OBSERVED` |

ترتیب «دریافت سرور → ادغام با Room → emitوضعیت → رسم گره» **هیچکدام RUNTIME VERIFIED نشده** و
`STATICALLY INFERRED` باقی میماند.

## ۶. ماشین حالت coroutine مرتبط

`COROUTINE_STATE_MACHINES.json`: ۵۳۹ آنوتیشن `Lf70/c;` (`DebugMetadata`)،
فیلدها فقط `c/f/l/m/v` (جدول `n/i/s` حذفشده توسط R8)، ۸۴ فیلد
`label` (۴۶) / `L$0..L$4` (۳۳) / `J$0` (۳) / `I$0,I$1` (۲)، ۶۵۲ کلاس suspend.
`GetPathMapState$invoke$2` دارای `create` @`0x509a8e90`، `invoke` @`0x509a8ec8`،
`invokeSuspend` @`0x509a8f34` است و بدنهٔ `invokeSuspend` شامل `if_eqz`،
`invoke_static`, `invoke_virtual`, `move_result_object` و `return_object` است (`OBSERVED/HIGH`).
اما **نگاشت شاخهها به حالتهای `label` و ترتیب resumeها `UNKNOWN`** است؛ فقط دستورالعملها شاهدند.

## ۷. شکاف Behavior Verification

هیچ شبیهساز/ADB تأییدشده، اسکرینشات، UI hierarchy، logcat یا مشاهدهٔ network ایجاد نشد.
مواردی که بدون runtime قابل تأیید نیستند: فواصل واقعی گرهها، شکل منحنی، موقعیت اولیهٔ اسکرول،
بازیابی اسکرول پس از چرخش، انیمیشن جابهجایی بین بخشها، و ظاهر گرهها در حالتهای قفل/تمام/جاری.
→ **هیچ ادعای بازسازی پیکسلبهپیکسل** معتبر نیست. جزئیات در `RUNTIME_VERIFICATION.fa.md`.

## ۸. شناسههای شاهد

`EVIDENCE_INDEX.json`: ردیفهای مربوط به «Shipped tracks.json», «v52 testdata»,
«Ghidra disassembled PATH_MAP», «Scroll X/Y position field», «Chapter index in section field»,
«Column count field», «Vertical ellipse radius field», «Ghidra string-to-function xrefs = 0».
