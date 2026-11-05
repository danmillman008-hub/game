#!/usr/bin/env python3
"""MISSION 07 — build 16_EVIDENCE_DATABASE.json from the workspace evidence.
Every evidence path is checked to exist; each entry carries its source file
SHA-256 prefix so the database cannot silently reference a missing artifact.
Statuses: VERIFIED_RUNTIME / VERIFIED_STATIC / VERIFIED_BOTH / INFERRED / UNKNOWN.
"""
import json, pathlib, hashlib, collections, datetime, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]          # /home/user/game
R = ROOT/'ANALYSIS/RUNTIME/MISSION_07'
M = ROOT/'ANALYSIS/MISSION_07'
OUT = M/'16_EVIDENCE_DATABASE.json'

def sha(p):
    try: return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()[:16]
    except Exception: return None

def E(status, claim, evidence, run='', notes=''):
    return {'status':status,'claim':claim,'evidence':evidence,'run':run,'notes':notes}

def add(entries, status, claim, evidence, run='', notes=''):
    ev = []
    for p in evidence:
        fp = ROOT/p
        ev.append({'path':p,'exists':fp.exists(),
                   'sha256_16':sha(fp) if fp.exists() else None,
                   'bytes':fp.stat().st_size if fp.exists() else 0})
    entries.append(E(status, claim, ev, run, notes))

def trace_counts(p):
    c = collections.Counter()
    fp = ROOT/p
    if not fp.exists(): return {}
    for l in fp.read_text(errors='replace').splitlines():
        try: c[json.loads(l).get('kind')] += 1
        except Exception: pass
    return dict(c)

def main():
    entries = []
    A = lambda s,c,e,r='',n='': add(entries,s,c,e,r,n)
    # --- environment ---
    A('VERIFIED_RUNTIME','Local sandbox has no adb/emulator/java/KVM; runtime executes on GitHub Actions',
      ['ANALYSIS/MISSION_07/00_MISSION_07_PLAN.md','ANALYSIS/MISSION_07/01_RUNTIME_ENVIRONMENT.md'],
      '42017453045','local tool inventory')
    A('VERIFIED_RUNTIME','Android 16 / API 36 sdk_gphone64_x86_64 userdebug/dev-keys, ro.debuggable=1, ro.secure=1',
      ['ANALYSIS/RUNTIME/MISSION_07/ENV/DEVICE_AND_ROOT.txt'],'42017453045')
    A('VERIFIED_RUNTIME','adb root -> uid=0(root) context=u:r:su:s0; /system/xbin/su present',
      ['ANALYSIS/RUNTIME/MISSION_07/ENV/DEVICE_AND_ROOT.txt'],'42017453045')
    A('VERIFIED_RUNTIME','SELinux Enforcing -> Permissive via setenforce 0; /system/bin/sqlite3 and strace present',
      ['ANALYSIS/RUNTIME/MISSION_07/ENV/DEVICE_AND_ROOT.txt'],'42017453045')
    A('VERIFIED_RUNTIME','Private /data/data/com.getmimo read via root; consistent sqlite3 .backup copies captured',
      ['ANALYSIS/RUNTIME/MISSION_07/DB/SNAPSHOT_C_LESSON_BEFORE_ANSWER.json'],'42019353340')
    A('VERIFIED_RUNTIME','Frida 17.25.2 server x86_64 runs; frida-ps -U lists process name Mimo',
      ['ANALYSIS/RUNTIME/MISSION_07/FRIDA/INSTALL.txt','ANALYSIS/RUNTIME/MISSION_07/FRIDA/STAGE3_SETUP.txt'],'42025423068')
    A('VERIFIED_RUNTIME','Frida attach must be by PID; get_process("com.getmimo") and spawn() both fail',
      ['ANALYSIS/RUNTIME/MISSION_07/FRIDA/DRIVER.log','ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE1_FRIDA.jsonl'],'42017453045')
    A('VERIFIED_RUNTIME','Frida 17 scripts using global Java fail ReferenceError; bundled frida-tools 14.11.0 java.js fixes it',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE2_ONLINE.jsonl','ANALYSIS/RUNTIME/MISSION_07/FRIDA/java_bridge_frida17.js',
       'ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE3_ONLINE.jsonl'],'42019353340 / 42025423068')
    A('VERIFIED_RUNTIME','36,825 loaded classes, 85 com.getmimo.* classes at attach',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE3_ONLINE.jsonl'],'42025423068')
    A('VERIFIED_RUNTIME','Offline isolation: Active default network: none + Network is unreachable + airplane_mode_on=1',
      ['ANALYSIS/RUNTIME/MISSION_07/EXPERIMENTS/G_OFFLINE_ISOLATION.txt',
       'ANALYSIS/RUNTIME/MISSION_07/EXPERIMENTS/S4_OFFLINE_ISOLATION.txt'],'42019353340 / 42028049247')
    # --- validators ---
    A('VERIFIED_BOTH','qm.i.a normalizer = lowercase(Locale.US) + keep Unicode letters/digits and < > ( ) : { } , . ; 21 runtime cases',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE3_ONLINE.jsonl','ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl',
       'ANALYSIS/MISSION_07/04_ANSWER_VALIDATION_RUNTIME.md'],'42025423068 / 42028049247')
    A('VERIFIED_BOTH','km.f.b(List) = true iff for every sm.a item selected == correct; 8 runtime cases incl. empty -> true',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl','ANALYSIS/MISSION_07/04_ANSWER_VALIDATION_RUNTIME.md'],'42028049247')
    A('VERIFIED_BOTH','LessonProgress.isSolvedCorrectly() = tries >= 1, independent of attempts; 20 constructed objects',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE3_ONLINE.jsonl','ANALYSIS/MISSION_07/04_ANSWER_VALIDATION_RUNTIME.md'],'42025423068')
    A('VERIFIED_BOTH','f0(false, isSolvedCorrectly()) — M07 correction of M06 which reported true as first arg',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl',
       'ANALYSIS/MISSION_07/RUNTIME_TRACE/STATIC_DECODE/00_STATIC_DECODE_M07.md'],'42028049247')
    A('VERIFIED_RUNTIME','network.a: online a()=true b()=false; offline a()=false b()=true',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl','ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_OFFLINE.jsonl'],'42028049247')
    A('VERIFIED_RUNTIME','te.c.b(String) parses Paragraph/Code/Selection, drops unknown tags, returns [] on malformed XML (5 cases)',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_OFFLINE.jsonl','ANALYSIS/MISSION_07/10_CODE_EDITOR_AND_WEBVIEW_BOUNDARY.md'],'42028049247')
    A('VERIFIED_RUNTIME','gm.h.a(emptyList) = None(interactionTypeName=slide)',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE3_ONLINE.jsonl'],'42025423068')
    A('VERIFIED_STATIC','c.W() @10953916 = partial-match correct path (jm/n + analytics validated_input_execution_correct_partial_match)',
      ['ANALYSIS/MISSION_07/RUNTIME_TRACE/STATIC_DECODE/00_STATIC_DECODE_M07.md',
       'ANALYSIS/MISSION_07/RUNTIME_TRACE/STATIC_DECODE/W.smali.txt'],'static decode 3735cfdf')
    A('VERIFIED_STATIC','c.d0() wrong-feedback builds jm/o with solutionFeedbackWrong and contains no XP/scoring arithmetic',
      ['ANALYSIS/MISSION_07/RUNTIME_TRACE/STATIC_DECODE/d0.smali.txt'],'static decode 3735cfdf')
    A('VERIFIED_STATIC','ds/w.c unlock key = "<long>:<long>:<long>" membership test in Set<String>',
      ['ANALYSIS/MISSION_07/RUNTIME_TRACE/STATIC_DECODE/00_STATIC_DECODE_M07.md'],'static decode 3735cfdf')
    # --- viewmodel / db ---
    A('VERIFIED_RUNTIME','Non-interactive slide 151410 solved locally: c.U() -> H() -> e0() -> queue_store -> f0(false,true) -> N()',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl','ANALYSIS/MISSION_07/03_INTERACTIVE_LESSON_VIEWMODEL_RUNTIME.md'],'42028049247')
    A('VERIFIED_RUNTIME','Live LessonBundle(lessonId=151410, tutorialId=904, trackId=219, chapterType=PRACTICE_LEVEL_1, …)',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl'],'42028049247')
    A('VERIFIED_RUNTIME','mimo.db schema exactly matches M05 ROOM_SQL.txt; journal_mode=wal; room_master hash 2b8ab6d3…',
      ['ANALYSIS/RUNTIME/MISSION_07/DB/SNAPSHOT_S4_C_BEFORE_ANSWER.json','ANALYSIS/MISSION_05/EVIDENCE/ROOM_SQL.txt'],'42028049247')
    A('VERIFIED_RUNTIME','Stage 2: lesson_progress=0, chapter_completions=0, tutorial_completions=672 in all C..I snapshots',
      ['ANALYSIS/RUNTIME/MISSION_07/LOGS/STAGE2_SUMMARY.json','ANALYSIS/MISSION_07/06_DATABASE_BEFORE_AFTER.md'],'42019353340')
    A('VERIFIED_RUNTIME','Stage 4: first real lesson_progress row 151410 tries=1 attempts=1 in_queue=1 publishSetVersion=753',
      ['ANALYSIS/RUNTIME/MISSION_07/DB/SNAPSHOT_S4_C_BEFORE_ANSWER.json','ANALYSIS/MISSION_07/06_DATABASE_BEFORE_AFTER.md'],'42028049247')
    A('VERIFIED_RUNTIME','Wrong WebView letter Q produces "Try again" + Q disabled, no lesson_progress change and no native wrong-feedback hook',
      ['ANALYSIS/RUNTIME/MISSION_07/UI/S4_D1_AFTER_WRONG_OPTION.xml',
       'ANALYSIS/RUNTIME/MISSION_07/DB/SNAPSHOT_S4_D1_AFTER_WRONG_OPTION.json',
       'ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl'],'42028049247')
    A('VERIFIED_RUNTIME','Offline cold start: postUnsyncedLessonProgress throws com.getmimo.network.NoConnectionException',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_OFFLINE.jsonl','ANALYSIS/MISSION_07/07_PERSISTENCE_RESTORATION_AND_QUEUE.md'],'42028049247')
    A('VERIFIED_RUNTIME','DELETE FROM lesson_progress WHERE in_queue = 1 removes the queued row at offline cold start (S4_G 1 -> S4_H/I 0)',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_OFFLINE.jsonl',
       'ANALYSIS/RUNTIME/MISSION_07/DB/SNAPSHOT_S4_H_OFFLINE_COLD_START.json',
       'ANALYSIS/RUNTIME/MISSION_07/DB/SNAPSHOT_S4_I_OFFLINE_RESTORED.json'],'42028049247')
    A('VERIFIED_RUNTIME','tutorial_completions rows are seeded (is_completed=0, identical updated_at), not user progress',
      ['ANALYSIS/RUNTIME/MISSION_07/DB/SNAPSHOT_C_LESSON_BEFORE_ANSWER.json',
       'ANALYSIS/RUNTIME/MISSION_07/DB/SNAPSHOT_S4_C_BEFORE_ANSWER.json'],'42019353340 / 42028049247')
    A('VERIFIED_RUNTIME','Analytics DBs (mixpanel, datatransport, google_app_measurement_local) keep writing offline',
      ['ANALYSIS/RUNTIME/MISSION_07/LOGS/STAGE2_SUMMARY.json','ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_OFFLINE.jsonl'],'42019353340 / 42028049247')
    # --- content / UI ---
    A('VERIFIED_STATIC','Shipped tutorial-904 lesson 151403 WebView JS sets correctLetter=D and shows Correct!/D O G or Try again',
      ['ANALYSIS/MISSION_05/SAMPLES/runtime_matched_lesson_151403.txt',
       'ANALYSIS/MISSION_07/RUNTIME_TRACE/SHIPPED_CONTENT/SELECTION_ANSWERS.json'],'M05 shipped content')
    A('VERIFIED_STATIC','Shipped tutorial-1103 lesson 123420 selection correct="true" item is "To store information for later use"',
      ['ANALYSIS/MISSION_07/RUNTIME_TRACE/SHIPPED_CONTENT/SELECTION_ANSWERS.json'],'M07 shipped index')
    A('VERIFIED_RUNTIME','2,855 shipped selection questions indexed with exact correct/wrong item texts',
      ['ANALYSIS/MISSION_07/RUNTIME_TRACE/SHIPPED_CONTENT/SELECTION_ANSWERS.json'],'static extraction from original APK')
    A('VERIFIED_RUNTIME','Adaptive onboarding labels measured: experience, goal, employment, interests, Web apps/Data science, daily goal, reminders, device',
      ['ANALYSIS/RUNTIME/MISSION_07/UI/NAV-11.xml','ANALYSIS/RUNTIME/MISSION_07/UI/S4NAV-12.xml',
       'ANALYSIS/MISSION_07/12_UI_STATE_MACHINE.md'],'42019353340 / 42028049247')
    A('VERIFIED_RUNTIME','Stage 4 deterministic 26-step tap chain reached the Q/R/D WebView lesson 151403',
      ['ANALYSIS/RUNTIME/MISSION_07/EXPERIMENTS/S4_ANSWER_LOG.jsonl',
       'ANALYSIS/RUNTIME/MISSION_07/UI/S4_C_BEFORE_ANSWER.xml'],'42028049247')
    A('VERIFIED_RUNTIME','LiveData m0.l/k posted Boolean true/false and AuthenticationStep AuthOverview/SignupOverview',
      ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl'],'42028049247')
    # --- unknowns ---
    A('UNKNOWN','Native correct/partial/wrong feedback (jm/m, jm/n, jm/o) at runtime after a submitted answer',
      ['ANALYSIS/MISSION_07/05_ANSWER_STATE_TRANSITIONS.md'],'pending stage 5')
    A('UNKNOWN','Absolute XP / streak / leaderboard / daily-goal scoring formulas',
      ['ANALYSIS/MISSION_07/11_SCORING_AND_REWARD_LOGIC.md'],'no local formula; remote DTOs')
    A('UNKNOWN','Live unlock boolean and the origin of the three long operands in ds/w.c',
      ['ANALYSIS/MISSION_07/08_PROGRESSION_AND_UNLOCK_LOGIC.md'],'no dev prefs / no key values observed')
    A('UNKNOWN','Code evaluation boundary (WebView JS bridge, JNI, native libs, remote executor)',
      ['ANALYSIS/MISSION_07/10_CODE_EDITOR_AND_WEBVIEW_BOUNDARY.md','ANALYSIS/MISSION_07/13_NATIVE_RUNTIME_FINDINGS.md'])
    A('UNKNOWN','Xposed/LSPosed, JVMTI, strace, heap dump and JNI tracing availability/behaviour',
      ['ANALYSIS/MISSION_07/01_RUNTIME_ENVIRONMENT.md','ANALYSIS/MISSION_07/13_NATIVE_RUNTIME_FINDINGS.md'],'not exercised, not declared unavailable')
    A('UNKNOWN','Server acknowledgement / response body for lesson progress',
      ['ANALYSIS/MISSION_07/07_PERSISTENCE_RESTORATION_AND_QUEUE.md'],'SERVER CONFIRMED=0')
    # --- stage 5 (filled if evidence exists) ---
    s5 = R/'EXPERIMENTS/S5_ANSWER_LOG.jsonl'
    if s5.exists():
        evs = []
        for l in s5.read_text(errors='replace').splitlines():
            try: o = json.loads(l)
            except Exception: continue
            if o.get('event') in ('experiment_start','experiment_complete','wrong_feedback','cta_skipped','second_lesson_detected'):
                evs.append(o)
        if evs:
            A('VERIFIED_RUNTIME','Stage 5 answer driver executed %d key events (see claim notes)' % len(evs),
              ['ANALYSIS/RUNTIME/MISSION_07/EXPERIMENTS/S5_ANSWER_LOG.jsonl'],'42030594857',
              json.dumps(evs[:12], ensure_ascii=False)[:1400])
    for f in ['STAGE5_ONLINE.jsonl','STAGE5_OFFLINE.jsonl']:
        p = 'ANALYSIS/RUNTIME/MISSION_07/TRACES/'+f
        if (ROOT/p).exists():
            A('VERIFIED_RUNTIME','Trace %s event kinds: %s' % (f, json.dumps(trace_counts(p))),
              [p],'42030594857')

    # --- auto-generated granular entries from the measured traces -----------
    def cases(trace_path, experiment, status, evidence_extra=()):
        fp = ROOT/trace_path
        if not fp.exists(): return 0
        n = 0
        for l in fp.read_text(errors='replace').splitlines():
            try: o = json.loads(l)
            except Exception: continue
            if o.get('kind') != 'call' or o.get('experiment') != experiment: continue
            key = o.get('case_name') or ('tries=%s attempts=%s' % (o.get('tries'), o.get('attempts')))
            val = o.get('ret')
            label = ('%s %s -> %s' % (experiment, key, json.dumps(val, ensure_ascii=False)[:120]))
            A(status, label, [trace_path, *evidence_extra],
              '42025423068 / 42028049247',
              json.dumps({k:o.get(k) for k in ('input','items','tries','attempts','size','tostring') if k in o}, ensure_ascii=False)[:400])
            n += 1
        return n

    cases('ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl','E1_normalizer','VERIFIED_BOTH',
          ('ANALYSIS/MISSION_07/04_ANSWER_VALIDATION_RUNTIME.md',))
    cases('ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl','E2_selection_validator','VERIFIED_BOTH')
    cases('ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl','E3_isSolvedCorrectly','VERIFIED_BOTH')
    cases('ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_OFFLINE.jsonl','E5_dsl_parser','VERIFIED_RUNTIME',
          ('ANALYSIS/MISSION_07/10_CODE_EDITOR_AND_WEBVIEW_BOUNDARY.md',))

    # one entry per installed hook
    t = ROOT/'ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl'
    if t.exists():
        for l in t.read_text(errors='replace').splitlines():
            try: o = json.loads(l)
            except Exception: continue
            if o.get('kind') != 'hook_installed': continue
            A('VERIFIED_RUNTIME', 'Hook installed: %s (%s %s, overloads=%s)' % (
                o.get('tag'), o.get('cls'), o.get('method') or '', o.get('overloads')),
              ['ANALYSIS/RUNTIME/MISSION_07/TRACES/STAGE4_ONLINE.jsonl'], '42028049247')

    # one entry per measured snapshot with room row counts
    import glob as _glob
    for f in sorted(_glob.glob(str(ROOT/'ANALYSIS/RUNTIME/MISSION_07/DB/SNAPSHOT_*.json'))):
        try: d = json.loads(pathlib.Path(f).read_text())
        except Exception: continue
        lp = cc = tc = None
        for db in d.get('databases', []):
            if 'consistent_mimo.db' not in db.get('path',''): continue
            for tb in db.get('tables', []):
                if tb['name']=='lesson_progress': lp = tb.get('row_count')
                if tb['name']=='chapter_completions': cc = tb.get('row_count')
                if tb['name']=='tutorial_completions': tc = tb.get('row_count')
        if lp is None: continue
        rel = str(pathlib.Path(f).relative_to(ROOT))
        A('VERIFIED_RUNTIME', 'Snapshot %s: lesson_progress=%s chapter_completions=%s tutorial_completions=%s files=%s' % (
            d.get('label'), lp, cc, tc, len(d.get('files',[]))),
          [rel], '42019353340 / 42028049247 / 42030594857')

    # one entry per report deliverable
    for f in sorted((M).glob('*.md')) + sorted((M).glob('*.json')):
        rel = str(f.relative_to(ROOT))
        A('VERIFIED_RUNTIME', 'MISSION 07 deliverable %s exists (%d bytes)' % (f.name, f.stat().st_size),
          [rel], 'workspace')

    counts = collections.Counter(e['status'] for e in entries)
    missing = [x['path'] for e in entries for x in e['evidence'] if not x['exists']]
    db = {
      'schema_version':'1.0',
      'mission':'07',
      'generated_utc':datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
      'branch':'arena/aebb90b7-game',
      'apk':{'sha256':'48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a',
             'bytes':142353499,'package':'com.getmimo','version_name':'9.35','version_code':1792759685,
             'unchanged':True},
      'server_confirmed':0,
      'status_counts':dict(counts),
      'total_entries':len(entries),
      'missing_evidence_paths':missing,
      'runs':[42017453045,42018369099,42019353340,42025423068,42028049247,42030594857],
      'evidence_status_vocabulary':['VERIFIED_RUNTIME','VERIFIED_STATIC','VERIFIED_BOTH','INFERRED','UNKNOWN'],
      'entries':[dict(id='M07-%03d'%(i+1), **e) for i,e in enumerate(entries)]
    }
    OUT.write_text(json.dumps(db,indent=1,ensure_ascii=False),encoding='utf-8')
    print('wrote',OUT,'entries',len(entries),'statuses',dict(counts),'missing',len(missing))

if __name__=='__main__': main()
