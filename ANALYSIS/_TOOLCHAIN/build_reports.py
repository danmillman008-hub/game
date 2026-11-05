"""Generate four evidence-driven Persian reports from verified JSON artifacts.

Only writes ANALYSIS/*.fa.md. Script lives in ANALYSIS/_TOOLCHAIN.
"""

import os
import json
import collections
import re

A = '/home/user/game/ANALYSIS'
I = json.load(open(A + '/APK_COMPLETE_INVENTORY.json'))
G = json.load(open(A + '/COMPONENT_GRAPH.json'))
M = json.load(open(A + '/COVERAGE_METRICS.json'))
E = json.load(open(A + '/EVIDENCE_INDEX.json'))
S = json.load(open(A + '/SUBSYSTEM_EVIDENCE.json'))['subsystems']
EPS = json.load(open(A + '/MIMO_RETROFIT_ENDPOINTS.json'))
SCHEMA = json.load(open(A + '/MIMO_CONTENT_SCHEMA.json'))
CORO = json.load(open(A + '/COROUTINE_STATE_MACHINES.json'))

HDR = """**REVIEW — گزارش فنی، بدون ادعای تأیید نهایی.** منبع حقیقت: APK اصلی Mimo 9.35
(`sha256 = {sha}`). وضعیتها: `OBSERVED` | `STATICALLY INFERRED` | `RUNTIME VERIFIED` | `SERVER CONFIRMED` | `UNKNOWN`.
هیچ شبیهساز/ADB/لاگ/اسکرینشات/پاسخ سرور در این جلسه وجود ندارد؛ `RUNTIME VERIFIED` و `SERVER CONFIRMED` = **۰**.

""".format(sha=I['apk']['sha256'])


def tbl(headers, rows):
    out = '| ' + ' | '.join(headers) + ' |\n'
    out += '|' + '|'.join(['---'] * len(headers)) + '|\n'
    for r in rows:
        cells = [str(c).replace('|', '\\|').replace('\n', ' ')[:220] for c in r]
        out += '| ' + ' | '.join(cells) + ' |\n'
    return out + '\n'


def li(items):
    return ''.join('- ' + str(x).replace('\n', ' ') + '\n' for x in items) + '\n'


def write(name, text):
    p = os.path.join(A, name)
    open(p, 'w').write(HDR + text)
    print('wrote', name, os.path.getsize(p), 'bytes')


def ev_ids(substr):
    return [e['id'] for e in E['evidence'] if substr.lower() in e['claim'].lower()][:6]


# ===========================================================================
# 2. COMPONENT_CATALOG.fa.md
# ===========================================================================
layer_names_fa = {
    'ui': 'رابط/کامپوزابلها', 'viewmodel': 'ViewModel', 'usecase_interactor': 'UseCase/Interactor',
    'repository_remote': 'Repository/منبع راهدور', 'repository_local': 'Repository/محلی',
    'repository': 'Repository (سایر)', 'network_client': 'کلاینت شبکه', 'model': 'مدل داده',
    'analytics': 'Analytics/Properties', 'dependency_injection': 'تزریق وابستگی',
    'entry_point': 'Activity/Fragment نقطه ورود', 'application': 'Application',
    'background_worker': 'Worker/پسزمینه', 'navigation': 'Navigation', 'data_other': 'سایر data/core',
    'other_mimo': 'سایر com.getmimo',
}
cat = G['catalog']
by_layer = collections.defaultdict(list)
for c in cat:
    by_layer[c['layer']].append(c)

t = """# COMPONENT_CATALOG — کاتالوگ مؤلفهها

## ۱. دامنه و روش

کاتالوگ از **class_def های واقعی `Lcom/getmimo/`** در ۱۲ DEX ساخته شد
(**{n} کلاس** از {allc} class_def کل)؛ طبقهبندی لایها بر اساس مسیر بسته و نام کلاس است و
`STATICALLY INFERRED` محسوب میشود، نه مشاهدهٔ اجرا. لبهها و شمارشها در
`COMPONENT_GRAPH.json` و شناسهها در `EVIDENCE_INDEX.json` هستند.
لایهبندی **ادعای معماری سراسری نیست**؛ فقط توزیع نامها است.

""".format(n=G['totals']['mimo_class_defs_catalogued'], allc=G['totals']['all_class_defs'])

t += '## ۲. توزیع لایهها \n\n'
t += tbl(['لایه', 'عنوان فارسی', 'تعداد', '`OBSERVED` / `STATICALLY INFERRED`', 'نمونه کلاسها'],
         [[k, layer_names_fa.get(k, k), len(v), 'OBSERVED (تعداد) / STATICALLY INFERRED (نقش)',
           ', '.join(x['descriptor'] for x in v[:3])] for k, v in
          sorted(by_layer.items(), key=lambda x: -len(x[1]))])
t += """⚠️ تعداد لایه `ui` شامل کلاسهای لامبدای کاتلین (`PathMapScreenKt$...`) نیز هست؛
پس «تعداد کامپوزابل» نیست. `analytics` عمدتاً enum/propertyهای ردیابی است.

## ۳. توزیع زیرسیستمها (A…P)

"""
sub_fa = {
    'A_launch_init': 'A — راهاندازی/Init', 'B_auth_session': 'B — احراز هویت/نشست',
    'C_onboarding': 'C — Onboarding', 'D_home_dashboard': 'D — خانه/داشبورد',
    'E_learning_path': 'E — مسیر یادگیری', 'F_lesson_execution': 'F — اجرای درس',
    'G_lesson_progress': 'G — پیشرفت درس', 'H_practice_challenges': 'H — تمرین/چالش',
    'I_chapter_scoring': 'I — پایان چپتر/نمره', 'J_rewards_currency': 'J — پاداش/ارزها',
    'K_goals_streaks': 'K — هدف روزانه/Streak', 'L_leaderboard_league': 'L — لیدربورد/لیگ',
    'M_ai_tutor': 'M — AI Tutor', 'N_settings': 'N — تنظیمات',
    'O_client_config_flags': 'O — پیکربندی/Feature flags', 'P_subscription': 'P — اشتراک/پرداخت',
    'U_unclassified': 'بدون طبقهبندی',
}
t += tbl(['زیرسیستم', 'کلاس', 'لایه غالب', 'نمونه کلاس (عنوان ستون اصلاحشده)'],
         [[sub_fa.get(k, k), v['class_count'],
           ', '.join('%s:%d' % (a, b) for a, b in list(v['layer_distribution'].items())[:3]),
           ', '.join(v['sample_classes'][:2])] for k, v in S.items()])

t += """## ۴. مؤلفههای کلیدی (برگزیده از نامهای بازیابیشده)

### ۴٫۱ نقطههای ورود و Application
"""
acts = I['manifest']['components']['activity']
t += tbl(['نقش', 'کلاس', '`OBSERVED` در', 'سند'],
         [['Application', I['manifest']['application']['name'], 'AndroidManifest.xml', 'EV-0030..']] +
         [['Activity', x['name'], 'AndroidManifest.xml', 'APK_COMPLETE_INVENTORY.json'] for x in acts[:14]])
t += """### ۴٫۲ ViewModelها، Interactorها و Repositoryها (نمونه مستند)

"""
for layer, title in [('viewmodel', 'ViewModel'), ('usecase_interactor', 'UseCase/Interactor'),
                     ('repository', 'Repository'), ('repository_remote', 'Remote repository/API'),
                     ('repository_local', 'Local repository / DataStore'),
                     ('background_worker', 'Worker')]:
    xs = [c for c in by_layer[layer] if '$' not in c['descriptor']][:14]
    t += '**%s** (%d کلاس در لایه)\n\n' % (title, len(by_layer[layer]))
    t += li([x['descriptor'] for x in xs] or ['(فقط کلاسهای داخلی/لامبدا یافت شد)'])

t += """### ۴٫۳ سرویسها، گیرندهها و Providerها (از Manifest)

"""
for comp, title in [('service', 'Service'), ('receiver', 'BroadcastReceiver'), ('provider', 'ContentProvider')]:
    t += '**%s** (%d):\n\n' % (title, len(I['manifest']['components'][comp]))
    t += li([x['name'] for x in I['manifest']['components'][comp]])

t += """### ۴٫۴ وابستگیهای بومی و کتابخانهای

"""
t += tbl(['نوع', 'مورد', 'وضعیت'],
         [['native .so', '%d کتابخانه در ۲ ABI' % len(I['native_libraries']), 'OBSERVED'],
          ['native', 'libandroidx.graphics.path.so', 'OBSERVED — مرتبط با رسم Path در Compose (نقش دقیق INFERRED)'],
          ['native', 'librive-android.so / libdatastore_shared_counter.so / libsigner.so / libyrf.so', 'OBSERVED'],
          ['Compose', 'androidx.compose 1.12.1 / material3 1.4.0 / adaptive 1.3.0',
           'OBSERVED (META-INF/*.version)']] +
         [[v['path'].split('/')[-1], v['content'], 'OBSERVED'] for v in I['embedded_dependency_version_files'][:16]])

t += """## ۵. نگاشت نامهای R8

"""
r8 = G['r8']
t += tbl(['مورد', 'مقدار', 'وضعیت'],
         [['R8 map-id', ', '.join(r8['map_id'].keys()) or '(none)', 'OBSERVED در source_file_idx'],
          ['فایل mapping در APK', 'خیر', 'OBSERVED (عدم وجود)'],
          ['نگاشت کلاس کوتاه → نام منطقی', r8['mapped_obfuscated_classes_sample'].__len__() and G['totals']['obfuscated_to_logical_mappings'], 'OBSERVED (بخشی)'],
          ['نام فایلهای منبع کاتلین بازیافته', G['totals']['kotlin_source_file_names_recovered'], 'OBSERVED'],
          ['دیابسکیشن کامل کلاسهای کوتاهنام', 'انجامنشده', 'UNKNOWN']])
t += """نمونهای از نگاشتهای قابل اتکا (از `DebugMetadata.c`):

"""
t += li(['`%s` ← `%s`' % (k, v) for k, v in list(sorted(r8['mapped_obfuscated_classes_sample'].items()))[:10]])

t += """## ۶. شناسههای شاهد مرتبط

"""
t += li([', '.join(ev_ids(x)) or '(none)' for x in
         ['Application class is', 'Component catalog', 'native .so', 'r8-map-id', 'DebugMetadata annotations']])
write('COMPONENT_CATALOG.fa.md', t)


# ===========================================================================
# 3. APPLICATION_FLOWS.fa.md
# ===========================================================================
flow_notes = {
    'A_launch_init': 'ترتیب دقیق initializerها و زمانبندی DI مشاهده نشده است.',
    'B_auth_session': 'جریان توکن، تازهسازی نشست و ذخیرهٔ امن آن مشاهده نشده است.',
    'C_onboarding': 'شرطهای انتقال بین صفحات و ترتیب آنها نامشخص است.',
    'D_home_dashboard': 'تقریباً هیچ کلاس `home/dashboard`ای با نام صریح پیدا نشد؛ صفحهٔ اصلی احتمالاً در `MainActivity` + کامپوزابلهای `ui/*` است (INFERRED).',
    'E_learning_path': 'فرمول هندسی گرهها، dp فواصل، تابع منحنی و اسکرول بازیابی نشده است.',
    'F_lesson_execution': 'منطق ارزیابی پاسخ و انواع تعاملات بهصورت جزئی بازسازی نشده است.',
    'G_lesson_progress': 'ترتیب دقیق آفلاین→آنلاین و خطاهای همگامسازی مشاهده نشد.',
    'H_practice_challenges': 'قواعد انتخاب تمرین و چالش نامشخص است.',
    'I_chapter_scoring': 'ضرایب عددی امتیاز و ترتیب صفحههای پایان نامشخص است.',
    'J_rewards_currency': 'مقادیر پاداش و تأیید سرور فقط استنتاجشدهاند.',
    'K_goals_streaks': 'قواعد شکستن/ترمیم Streak و محاسبهٔ هدف روزانه مشاهده نشد.',
    'L_leaderboard_league': 'قواعد صعود/سقوط لیگ و بازهٔ هفتگی مشاهده نشد.',
    'M_ai_tutor': 'پروتکل SSE، مدل پیامها و محدودیت نرخ مشاهده نشد.',
    'N_settings': 'فهرست کامل کلیدهای DataStore و مقادیر پیشفرض مشاهده نشد.',
    'O_client_config_flags': 'کدام فلگها فعالاند و مقادیر سرور مشاهده نشد.',
    'P_subscription': 'جریان خرید/ entitlement فقط از نام کلاسها استنتاج میشود؛ هیچ تراکنش مشاهدهای ثبت نشد.',
}

t = """# APPLICATION_FLOWS — جریانهای سرتاسری زیرسیستمها

## روش و هشدار

هر ردیف زیر بر **شواهد استاتیک** (`SUBSYSTEM_EVIDENCE.json`) بنا شده است. ستونها فقط جایی پر شدهاند که
مرجع واقعی وجود دارد؛ در غیر این صورت صریحاً `UNKNOWN` نوشته شده است. **هیچ جریانی RUNTIME VERIFIED نیست**.
(`OBSERVED` = رشته/کلاس/کلید SQL در APK؛ `STATICALLY INFERRED` = نقش از روی نام/مرجع؛ `UNKNOWN` = شاهد کافی نیست.)

## نمای کلی جریان اصلی (`STATICALLY INFERRED` از لبههای مشاهدهشده)

```mermaid
flowchart TD
  A[AndroidManifest: SplashActivity / MainActivity] --> B[App.onCreate]
  B --> C{Onboarding / Auth}
  C --> D[MainActivity Compose root]
  D --> E[Learning Path: PathMapScreen]
  E --> F[Lesson / ChapterActivity]
  F --> G[LessonProgress + Room]
  G --> H[LessonProgressQueue -> POST progress]
  H --> I[ChapterFinished* UI]
  I --> J[Rewards / Streak / Leaderboard]
  K[WorkManager / Services / Receivers] -.-> G
  L[DataStore / RemoteConfig] -.-> D
```

## جدول ۱۶ زیرسیستم (ده مؤلفهٔ درخواستی)

"""
for key, v in S.items():
    t += '### %s\n\n' % sub_fa.get(key, key)
    cls = ', '.join('`%s`' % x for x in v['sample_classes'][:5]) or 'UNKNOWN'
    good_methods = [x for x in v['distinct_method_names']
                    if len(x) > 2 and not x.startswith('<') and not x.startswith('access$')]
    methods = ', '.join('`%s`' % x for x in good_methods[:10]) or 'UNKNOWN (فقط نامهای R8شده/سازنده)'
    eps = ', '.join('%s `%s`' % (x['verb_inferred'], x['path']) for x in v['retrofit_endpoints'][:8]) or 'UNKNOWN'
    sql = ', '.join('`%s`' % x[:110] for x in v['sql_statements'][:4]) or 'UNKNOWN'
    model_cls = [c['descriptor'].split('/')[-1].rstrip(';') for c in cat
                 if c['layer'] == 'model' and re.search(v['keyword_pattern'], c['descriptor'])]
    models = (', '.join('`%s`' % x for x in sorted(set(model_cls))[:7]) or
              ', '.join('`%s`' % x[:80] for x in v['dex_string_evidence'][:5]) or 'UNKNOWN')
    kt = ', '.join('`%s`' % x for x in v['kotlin_source_files'][:6]) or 'UNKNOWN'
    gf = ', '.join('`%s@%s`' % (x['name'].split('::')[-1], x['address']) for x in v['ghidra_target_functions'][:4]) or 'UNKNOWN'
    layers = ', '.join('%s:%d' % (a, b) for a, b in list(v['layer_distribution'].items())[:4])
    t += tbl(['#', 'مؤلفه', 'یافته', 'وضعیت'], [
        ['۱', 'نقطهٔ ورود', cls, 'OBSERVED (نام کلاس) / UNKNOWN (ترتیب اجرا)'],
        ['۲', 'کلاسهای اصلی', '%d کلاس؛ لایهها: %s' % (v['class_count'], layers), 'OBSERVED'],
        ['۳', 'مدلهای داده', models, 'OBSERVED (رشتهها) / STATICALLY INFERRED (نسبت به کلاس)'],
        ['۴', 'متدهای اصلی', methods, 'OBSERVED (نام) / UNKNOWN (بدنهٔ کامل)'],
        ['۵', 'وابستگیها', layers, 'STATICALLY INFERRED'],
        ['۶', 'تعاملات شبکه', eps, 'STATICALLY INFERRED (مسیر) / UNKNOWN (فعل HTTP و بدنهٔ پاسخ)'],
        ['۷', 'پایداری محلی', sql, 'OBSERVED (عبارت SQL)' if v['sql_statements'] else 'UNKNOWN'],
        ['۸', 'گذار وضعیت', gf + '؛ ماشین حالت coroutine: %d کلاس' % CORO['counts']['suspend_classes'],
         'OBSERVED (دستورالعمل) / UNKNOWN (نمای کامل گذارها)'],
        ['۹', 'خروجی UI', kt, 'STATICALLY INFERRED'],
        ['۱۰', 'وابستگی به زیرسیستمهای دیگر', eps or sql, 'STATICALLY INFERRED'],
    ])
    t += '**بخشهای ناشناخته:** %s\n\n' % flow_notes.get(key, 'UNKNOWN')

t += """## آنچه در هیچ زیرسیستمی RUNTIME VERIFIED نشده است

"""
t += li([
    'ترتیب واقعی فراخوانیها، زمانبندی coroutineها و خطاهای شبکه.',
    'مقادیر واقعی پاسخ سرور و تغییر حالت پس از آن (`SERVER CONFIRMED` = ۰).',
    'ناوبری واقعی بین صفحات، انیمیشنها و اسکرول (هیچ ADB UI hierarchy / logcat / screenshot تولید نشد).',
    'نقشهٔ کامل routeهای `NavHost`؛ فقط ۹ deep-link filter و ۳۰۰ رشتهٔ routeمانند یافت شد (`COMPONENT_GRAPH.json`).',
])
t += '## شناسههای شاهد\n\n' + li([', '.join(ev_ids(x)) or '(none)' for x in
                               ['Manifest declares', 'Retrofit endpoint', 'Room/SQLite statement', 'DebugMetadata']])
write('APPLICATION_FLOWS.fa.md', t)


# ===========================================================================
# 4. DATA_AND_API_MAP.fa.md
# ===========================================================================
sql = I['database']['sql_statements']
mimo_sql = [s for s in sql if any(k in s for k in
            ('chapter_completions', 'tutorial_completions', 'lesson_progress', 'room_master_table'))]
other_sql = [s for s in sql if s not in mimo_sql]

t = """# DATA_AND_API_MAP — شبکه، پایگاهداده، مدلها و مالکیت وضعیت

> نوشتهٔ «مالکیت وضعیت» یعنی تعیین اینکه یک مقدار محلی ذخیره میشود، از سرور گرفته میشود، یا سرور مرجع نهایی آن است.
> در غیاب پاسخ سرور، **هیچ موردی `SERVER CONFIRMED` نیست**.

## ۱. مالکیت وضعیت (خلاصه)

"""
t += tbl(['داده', 'محل', 'مالک', 'شاهد', 'وضعیت'], [
    ['پیشرفت درس `lesson_progress`', 'Room `mimo.db`', 'محلی + صف ارسال (`in_queue`)',
     '`CREATE TABLE IF NOT EXISTS lesson_progress ...` / `SELECT * FROM lesson_progress WHERE in_queue = 1`', 'OBSERVED'],
    ['اتمام tutorial/chapter', 'Room `tutorial_completions` / `chapter_completions`', 'محلی',
     'دو `CREATE TABLE` + `SELECT COUNT(DISTINCT chapter_id)`', 'OBSERVED'],
    ['وضعیت «آخرین مسیر تعاملشده»', 'سرور + کش محلی', 'نا مشخص',
     '`GET /v1/tracks/completion/lastInteracted` + `CompletionRepository.fetchLastInteractedTrackId`', 'STATICALLY INFERRED'],
    ['پاداش سکّهٔ هدف روزانه', 'پاسخ سرور', 'سرور (استنتاجی)',
     '`PostProgressResponse::getDailyGoalCoinReward` + `POST /v1/user/rewards/{rewardId}/confirm`', 'STATICALLY INFERRED / نه SERVER CONFIRMED'],
    ['محتوای درس/مسیر', 'Assets shipped (v753)', 'داخل APK',
     '`assets/lessons-en/tracks/tracks.json` publishSetVersion=753', 'OBSERVED'],
    ['تنظیمات/ترجیحات', 'DataStore', 'محلی',
     '`Lcom/getmimo/data/local/DataStoreUserPreferences;` + `libdatastore_shared_counter.so`', 'OBSERVED'],
    ['پیکربندی کلاینت/فلگها', 'Remote Config / سرور', 'سرور (استنتاجی)',
     '`RemoteConfigManager.kt` / `/v2/client-config`', 'STATICALLY INFERRED'],
    ['نشست/احراز هویت', 'نا مشخص', 'نا مشخص', 'کلاسهای `ui/authentication/*`', 'UNKNOWN'],
])

t += """## ۲. طرحوارهٔ پایگاهداده (Room / SQLite)

نام پایگاهداده در رشتههای DEX: **{dbs}**.
تعداد عبارتهای SQL یافتشده: **{n}** (شامل WorkManager، Firebase و Room).

### ۲٫۱ جداول Mimo

""".format(dbs=', '.join(I['database']['database_names']), n=len(sql))
t += tbl(['#', 'عبارت SQL (OBSERVED)'], [[i + 1, '`%s`' % s.replace('\n', ' ')] for i, s in enumerate(mimo_sql)])
t += """### ۲٫۲ طرحوارهٔ `lesson_progress` (تطبیق دقیق)

ستونها از `CREATE TABLE` و `INSERT INTO`: `lesson_id, completed_at, started_at, tries,
tutorial_id, tutorial_version, track_id, publish_set_version, attempts,
is_practice_progress, in_queue` = **۱۱ ستون**. Ghidra دقیقاً **۱۱ متد `component1..component11`**
و getterهای متناظر برای `Lcom/getmimo/data/model/room/LessonProgress;` استخراج کرده است.
این تطبیق `OBSERVED` / `HIGH` است (`CONTROL_FLOW.txt`).

### ۲٫۳ سایر عبارتها (WorkManager / Firebase / migrations)

"""
t += li(['`%s`' % s[:170].replace('\n', ' ') for s in other_sql[:22]])

t += """## ۳. نقاط API

دو مجموعهٔ مستقل داریم: **{a} تعریف Retrofit حاشیهگذاریشده** (`MIMO_RETROFIT_ENDPOINTS.json`)
و **{b} رشتهٔ مسیر `/v...` در جدول رشتههای DEX** (`APK_COMPLETE_INVENTORY.json`).
تفاوت این دو به معنی نقاط اضافیِ تأییدنشده است، نه لیست کامل API.

### ۳٫۱ افعال HTTP — هشدار

اعلانهای Retrofit توسط R8 به کلاسهای کوتاه `@f/@o/@n/@p/@b` تغییر نام یافتهاند.
**هیچ فعل HTTP از روی نام متد استنتاج نشده است** و چنین استنتاجی صریحاً رد میشود.
برچسبهای GET/POST/PUT/DELETE در جدول زیر **فقط حدس `LOW`** از روی الگوی اعلانها هستند؛
هویت واقعی `@f`/`@o`/`@n`/`@p`/`@b` **UNKNOWN** است. تعیین قطعی نیازمند ردیابی
دستورالعملهای `retrofit2.RequestFactory$Builder` در Ghidra **یا** ثبت درخواست/پاسخ در محیط تست مجاز است
(هیچکدام انجام نشده؛ `SERVER CONFIRMED` = ۰).

""".format(a=EPS['count'], b=len(I['network']['endpoint_like_paths']))
t += tbl(['فعل استنتاجی', 'تعداد'], sorted(collections.Counter(e['verb_inferred'] for e in EPS['endpoints']).items()))

t += """### ۳٫۲ فهرست {n} تعریف Retrofit

""".format(n=EPS['count'])
t += tbl(['#', 'برچسب حدسی (LOW؛ فعل واقعی UNKNOWN)', 'مسیر', 'فایل کلاس', 'امضا'],
         [[i + 1, e['verb_inferred'], '`%s`' % e['path'], '`%s`' % e['source_file'],
           '`%s`' % e['signature'][:130]] for i, e in enumerate(EPS['endpoints'])])

t += """### ۳٫۳ مدل درخواست/پاسخ، Repository فراخوان، تغییروضعیت

"""
t += tbl(['مؤلفه', 'یافته', 'وضعیت'], [
    ['مدل درخواست/پاسخ', 'امضاها در جدول بالا؛ بدنهٔ مدلها عمدتاً JADX-stub یا R8شده', 'OBSERVED (امضا) / UNKNOWN (فیلدهای کامل)'],
    ['Repository فراخوان', '`DefaultRewardRepository`, `DefaultCoinsRepository`, `DefaultStreakRepository`, `DefaultLeaderboardRepository`, `CompletionRepository`, `LessonProgressRepository`, `SettingsRepository`', 'OBSERVED (نام کلاس)'],
    ['ViewModel/UseCase فراخوان', '`GetChapterEndSuccessState`, `GetPathMapState`, `GetChapterEndProgressWithEtaScreenData`, `CreateChapterEndScreens`', 'OBSERVED (نام) / STATICALLY INFERRED (نقش)'],
    ['تغییروضعیت پس از پاسخ موفق', '`INSERT/UPDATE lesson_progress`, `DELETE ... WHERE in_queue = 1`, `Confirmed reward with id`', 'OBSERVED (عبارت/رشته) / UNKNOWN (ترتیب اجرا)'],
    ['ارتباط موجودیت محلی با پاسخ', 'همبستگی مستقیم ستون→فیلد پاسخ برقرار نشده', 'UNKNOWN'],
])

t += """## ۴. سایر ذخیرهسازیها و منابع

"""
t += tbl(['منبع', 'مقدار', 'وضعیت'], [
    ['resources.arsc', '%d پکیج، %d ورودی در ۱۱۷ پیکربندی محلی' % (
        len(I['resources']['packages']), I['resources']['total_resource_entries']), 'OBSERVED'],
    ['انواع منبع پیشفرض', ', '.join('%s=%s' % (k, v) for k, v in
                                    I['resources']['packages'][0]['default_locale_types'].items() if v), 'OBSERVED'],
    ['Assets', '%d فایل / %d JSON / بستههای محلی %s' % (
        I['assets']['count'], I['assets']['json_files'], I['assets']['locale_bundles']), 'OBSERVED'],
    ['بومی', '%d کتابخانه .so' % len(I['native_libraries']), 'OBSERVED'],
    ['DataStore/SharedPreferences', '`DataStoreUserPreferences`، migrationـهای RevenueCat', 'OBSERVED (رشتهها) / UNKNOWN (فهرست کامل کلیدها)'],
])
t += '## شناسههای شاهد\n\n' + li([', '.join(ev_ids(x)) or '(none)' for x in
                               ['Room/SQLite statement', 'Retrofit endpoint', 'resources.arsc', 'mimo.db']])
write('DATA_AND_API_MAP.fa.md', t)


# ===========================================================================
# 9. COVERAGE_REPORT.fa.md
# ===========================================================================
cov = M['coverage']
t = """# COVERAGE_REPORT — پوشش، بازیافتها، شکستها و ناشناختهها

> **مأموریت «کامل» اعلام نمیشود.** معیار تکمیل، بازسازی و تأیید رفتار است، نه تولید فایل.

## ۱. مخرجهای اندازهگیری شده (`COVERAGE_METRICS.json`)

"""
t += tbl(['کمیت', 'مقدار', 'وضعیت'], [[k, v, 'OBSERVED'] for k, v in M['denominators'].items()])
t += """### ۱٫۱ باز reconcile مستقل اعداد قبلی

"""
t += tbl(['ادعای قبلی', 'منبع مستقل', 'نتیجه'],
         [['۱۲۲٬۵۴۶ تابع Ghidra', 'جمع `code_item` در map_list هر ۱۲ DEX = ۱۲۲٬۵۴۶؛ `defined_methods_with_code` = ۱۲۲٬۵۴۶',
           '✅ تطابق دقیق، تکتک DEXها (`OBSERVED/HIGH`)'],
          ['۱٬۲۸۴٬۵۴۲ نماد Ghidra', 'جمع ۱۲ سربرگ `=== PROGRAM ... symbols=` = ۱٬۲۸۴٬۵۴۲',
           '✅ تطابق حسابی؛ **ترکیب نمادها UNKNOWN**'],
          ['۱۲۹٬۰۷۱ متد (JADX MCP)', 'جمع `defined_methods_from_class_data` = ۱۲۹٬۰۷۱',
           '✅ تطابق دقیق (cross-check اضافی)']])
p = I['ghidra_reconciliation']['symbol_composition_probe']
t += """ترکیب نمادها:پایه ساختاری DEX **{b}** آیتم، باقیماندهٔ **{r}** برچسب تولیدشده توسط Ghidra
(`string_data::`، `EXTERNAL.dex-N::`، برچسبهای کلاس/متد/داده). فرمول دقیق تولید نماد
از سرآیند DEX قابل استخراج نیست ← `UNKNOWN`.

""".format(b=p['dex_structural_id_baseline'], r=p['residual_generated_labels'])

t += '## ۲. درصد پوشش (مخرج واقعی)\n\n'
rows = []
for k, v in cov.items():
    rows.append([k, v['count'], v['denominator'], v['pct'] if v['pct'] is not None else 'UNKNOWN',
                 v.get('note', '')])
t += tbl(['معیار', 'صورت', 'مخرج', 'درصد', 'یادداشت'], rows)

t += """## ۳. آنچه بازیابی شد

"""
t += li([
    'همهٔ ۱۲ DEX: هدر، Adler32، SHA-1، map_list، string/type/proto/field/method id، class_def، class_data، code_item (`OBSERVED`).',
    'Manifest باینری: ۶۱ activity + ۶ alias + ۱۹ service + ۲۰ receiver + ۸ provider + ۲۴ permission + ۵۱ meta-data + ۹ deep-link filter (`OBSERVED`).',
    'resources.arsc: ۱ پکیج، ۹۴٬۴۰۱ ورودی، ۱۱۷ پیکربندی محلی، ۱۴٬۰۲۳ آیتم public، ۱٬۷۲۱ رشته، ۱٬۶۳۱ dimen، ۲٬۲۳۳ id (`OBSERVED`).',
    '۱۲ کتابخانهٔ بومی، ۱۰٬۵۶۴ asset، ۱۰٬۳۱۷ JSON، ۱۱ بستهٔ زبانی محتوا، ۱۰۵٬۶۱۱ رشتهٔ یکتای DEX (`OBSERVED`).',
    'طرحوارهٔ Room: `lesson_progress` (۱۱ ستون)، `chapter_completions`، `tutorial_completions` + ۶۸ عبارت SQL (`OBSERVED`).',
    '۵۳ تعریف Retrofit + ۶۸ رشتهٔ مسیر، ۳٬۱۳۳ توصیفگر `com.getmimo`، ۴٬۱۹۹ لبهٔ ساختاری و ۱۶۱٬۹۴۶ لبهٔ Smali (`OBSERVED`/`STATICALLY INFERRED`).',
    '۵۳۹ `DebugMetadata`، ۸۴ فیلد ماشین حالت، ۶۵۲ کلاس suspend، ۱۲۲ تابع هدف با دستورالعمل Dalvik (`OBSERVED`).',
    'دادهٔ shipped v753: ۱۹ مسیر / ۱۴۴ section / ۲٬۰۰۲ ارجاع tutorial / ۶ نوع گره / ۰ نقض پیوستگی (`OBSERVED`).',
])

t += """## ۴. شکستها و عناصر ازدسترفته

"""
f = I['analysis_failures']
t += tbl(['مورد', 'مقدار', 'توضیح'], [
    ['شکست Smali', '%d کلاس (%s%% از class_def)' % (f['smali_failed_classes'], cov['smali_failures_vs_class_defs']['pct']),
     'همه در `classes.dex`؛ `Invalid element width` ۳/۵/…/۱۹. یکسان در baksmali ۲.۳.۴ و smali ۳.x → ساختار payload DEX، نه نسخهٔ ابزار.'],
    ['Smali تولیدشده', '%d فایل (%s%%)' % (f['smali_files_produced'], cov['smali_class_files_vs_class_defs']['pct']), 'پوشش کامل Smali ادعا نمیشود.'],
    ['JADX ۱.۵.۶', '%d فایل Java / %d فایل دارای stub (%s%%)' % (
        f['jadx_1_5_6_java_files'], f['jadx_1_5_6_stub_files'], cov['jadx_1_5_6_stub_file_rate']['pct']),
     '%d خطای گزارششده؛ بدنهٔ متدها بازسازی نشده است.' % f['jadx_1_5_6_reported_total_errors']],
    ['xref رشته→تابع Ghidra', '۰', 'آنالایزر Reference در PSPEC لودر DEX غیرفعال است؛ نسبت قطعی فیلد به کلاس باز است.'],
    ['R8 mapping', 'فایل وجود ندارد', 'فقط ۴۹۱ نگاشت از `DebugMetadata.c`؛ دیابسکیشن کامل UNKNOWN.'],
    ['متدهای بدون بدنه', M['denominators']['methods_without_code'],
     'abstract/interface/native طبق `code_off=0`؛ **اینها «عملکرد گمشده» نیستند** (قید ۷ پروژه).'],
])

t += """## ۵. وضعیت نهایی چهارگانه

### WHAT WE KNOW — `OBSERVED`
"""
t += li(['ساختار باینری APK و ۱۲ DEX، هشها، شمارشها و تطابق کامل ۱۲۲٬۵۴۶ تابع Ghidra با `code_item`.',
         'فهرست مؤلفههای Manifest، منابع، کتابخانههای بومی، assetها و طرحوارهٔ Room.',
         'نام کلاسها، امضاها، رشتههای وضعیت، نقاط API حاشیهگذاریشده و دستورالعملهای ۱۲۲ تابع هدف.',
         'مدل دادهٔ v753 و اینکه مختصات گرهها در assetها وجود ندارد.'])
t += '### WHAT WE INFER — `STATICALLY INFERRED`\n\n'
t += li(['لایهبندی SCREEN→VIEWMODEL→USECASE→REPOSITORY تنها در بخشی از گراف دیده شد (لبههای ui→viewmodel ۱۸، viewmodel→usecase ۳۴، usecase→repository ۷۹ مرجع نوعی)؛ **سراسری نیست**.',
         'فعل HTTP (فقط حدس LOW؛ استنتاج از نام متد رد شده است)؛ مالکیت سروری پاداش؛ نقش کامپوزابلها و routeها.',
         'معنای فیلدهای `toString()` کاتلین در غیاب xref.'])
t += '### WHAT WE VERIFIED AT RUNTIME — `RUNTIME VERIFIED` / `SERVER CONFIRMED`\n\n'
t += li(['**۰ مورد.** نه شبیهساز/ADB تأییدشده، نه اسکرینشات، نه UI hierarchy، نه logcat، نه پاسخ سرور.',
         'هیچ استنتاج استاتیکی بهعنوان مشاهدهٔ اجرا جلوه داده نشده است.'])
t += '### WHAT WE STILL DO NOT KNOW — `UNKNOWN`\n\n'
t += li(['اعداد `dp` فاصلهٔ عمودی/افقی، تابع منحنی، X/Y گرهها، مقدار `scrollPositionX`/`scrollPositionY` و انیمیشنها.',
         'ضرایب عددی `rewardMultiplier` / `rewardedSparksForCorrectAnswer`، وزن «درست از بار اول»، آستانههای ETA و ترتیب صفحههای پایان چپتر.',
         'ترکیب دقیق ۱٬۲۸۴٬۵۴۲ نماد Ghidra، نگاشت کامل R8، نقشهٔ routeهای `NavHost`، نشست/توکن، قواعد لیگ و Streak.',
         'بدنهٔ پاسخهای سرور و تغییروضعیت پس از آنها، و کلیهٔ رفتارهای runtime.'])

t += """## ۶. معیارهای تکمیل (مادهٔ ۱۲) — ارزیابی صادقانه

"""
t += tbl(['معیار', 'وضعیت'], [
    ['همهٔ ۱۲ DEX محاسبه شدند', '✅ بله (`OBSERVED`)'],
    ['مؤلفههای اصلی اپ شناسایی شدند', '✅ بله، **تا سطح نام/لایه**؛ نقش کامل UNKNOWN'],
    ['روابط زیرسیستمها نگاشت شدند', '⚠️ جزئی (لبههای نوعی + لبههای Smali)، نه گراف کامل'],
    ['ناوبری و جریان داده بازسازی شدند', '⚠️ جزئی؛ مسیر کامل routeها UNKNOWN'],
    ['حالت محلی و راهدور مهم شناسایی شد', '✅ بله (Room/DataStore/API)، مالکیت برخی UNKNOWN'],
    ['منطق Learning Path تحلیل شد', '⚠️ مدل داده بله، **هندسه خیر**'],
    ['منطق درس و امتیاز تحلیل شد', '⚠️ چرخهٔ ذخیره/همگامسازی بله، **فرمول عددی خیر**'],
    ['ماشینهای حالت coroutine مهم نگاشت شدند', '⚠️ فیلدها و ۱۲۲ بدنهٔ دستورالعملی؛ نمای کامل گذارها خیر'],
    ['شاهد به نتایج مهم پیوست شد', '✅ %d ورودی در `EVIDENCE_INDEX.json`' % E['counts']['total']],
    ['وضعیت تأیید runtime افشا شد', '✅ بله (۰ مورد)'],
    ['ناشناختهها صریحاً مستند شدند', '✅ بله'],
    ['بازیابی کامل سورس', '❌ خیر، و ادعا نمیشود'],
])
t += """## ۷. شمارش شواهد

"""
t += tbl(['وضعیت', 'تعداد'], sorted(E['counts']['by_status'].items()))
t += tbl(['سطح اطمینان', 'تعداد'], sorted(E['counts']['by_confidence'].items()))
t += '\n`RUNTIME VERIFIED` = ۰، `SERVER CONFIRMED` = ۰ (ستونها خالیاند، حذف نشدهاند).\n'
write('COVERAGE_REPORT.fa.md', t)
