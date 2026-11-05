#!/usr/bin/env python3
"""MISSION 07 / STAGE 3 — deterministic navigation to a live lesson + a
controlled WRONG/CORRECT answer experiment with before/after DB snapshots.

Every tap target comes from a measured uiautomator XML dump. Correct/wrong
labels come verbatim from shipped `interactiveContent` (see m07_lesson_plan.py).
No guessed answers, no server calls, no APK modification.
"""
import subprocess, pathlib, json, time, sys, hashlib, re
R = pathlib.Path('ANALYSIS/RUNTIME/MISSION_07')
UI = R/'UI'; EXP = R/'EXPERIMENTS'; LOG = EXP/'STAGE3_ANSWER_LOG.jsonl'
for d in (UI, EXP, R/'DB'): d.mkdir(parents=True, exist_ok=True)
LOG.write_text('', encoding='utf-8')

def rec(o):
    o['ts'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    with LOG.open('a', encoding='utf-8') as f: f.write(json.dumps(o, ensure_ascii=False)+'\n')
    print('[m07]', json.dumps(o, ensure_ascii=False)[:260], flush=True)

def adb(*a, timeout=45):
    try:
        return subprocess.run(['adb']+list(a), capture_output=True, timeout=timeout).stdout.decode(errors='replace').strip()
    except Exception as e:
        return 'ADB_ERROR %s' % e

def dump(name):
    p = UI/(name+'.xml')
    adb('shell','uiautomator','dump','/sdcard/m07_ads.xml')
    adb('pull','/sdcard/m07_ads.xml',str(p))
    if not p.exists(): return None
    s = p.read_text(errors='replace')
    texts = [t for t in re.findall(r'text="([^"]+)"', s) if t.strip()]
    return {'path':str(p),'texts':texts[:40],'sha':hashlib.sha256(s.encode()).hexdigest()[:16]}

def tap(x,y,label):
    rec({'event':'tap','x':x,'y':y,'label':label})
    adb('shell','input','tap',str(x),str(y))
    time.sleep(4)

def plan(xml):
    try:
        out = subprocess.check_output([sys.executable,str(R/'m07_lesson_plan.py'),xml],timeout=20).decode()
        return json.loads(out)
    except Exception as e:
        return {'type':'PLAN_ERROR','error':str(e)}

def choose(xml, prefer, avoid):
    out = subprocess.check_output([sys.executable,str(R/'m07_tap_target.py'),xml,'',
                                   ';'.join(avoid), '|'.join(prefer)],timeout=25).decode().strip().splitlines()
    if not out or out[0].startswith('NONE'): return None, out[0] if out else 'NONE'
    p = out[0].split(None,3)
    return (int(p[0]),int(p[1]),p[2] if len(p)>2 else '',p[3] if len(p)>3 else ''), out[0]

def snap(label, state):
    subprocess.run(['bash',str(R/'m07_snapshot.sh'),label],capture_output=True,timeout=180)
    rec({'event':'snapshot','label':label,'state':state})

# Preferred onboarding answers: choose the WEB/HTML path when that question is
# shown; otherwise accept the shipped default. Never tap auth/purchase actions.
PREFER = ['Web apps','Web Development','HTML','How things look (appearance)',
          'Build something useful','Do better at work or school','Employed',
          'Software, IT & data','Casual','Mostly on the computer','Skip']
AVOID = set(); STATE = pathlib.Path(str(LOG)+'.state'); STATE.write_text('\n0\n')
lesson = None; lxml = None
for i in range(1, 36):
    name = 'S3NAV-%02d' % i
    st = dump(name)
    if not st: rec({'event':'dump_failed','step':name}); time.sleep(3); continue
    p = plan(st['path'])
    if p.get('type') in ('WEBVIEW_LETTER_151403','SELECTION_123420'):
        lesson, lxml = p, st['path']; rec({'event':'lesson_detected','step':name,'plan':p}); break
    c, raw = choose(st['path'], PREFER, AVOID)
    rec({'event':'nav','step':name,'texts':st['texts'][:14],'choice':raw})
    if not c: time.sleep(4); continue
    x,y,lab,mode = c
    tap(x,y,lab); AVOID.add('%d,%d'%(x,y))
    nt = dump(name+'b')
    if nt and nt['sha'] == st['sha']:
        n = int(STATE.read_text().splitlines()[-1] or 0) + 1
    else:
        n = 0; AVOID.clear()
    STATE.write_text('%s\n%d\n'%(nt['sha'] if nt else '', n))
    if n >= 4: rec({'event':'nav_stop','reason':'four_identical_hierarchies'}); break

if not lesson:
    rec({'event':'ABORT','reason':'no classified lesson reached'})
    sys.exit(0)

# ---------------- controlled answer experiment -----------------------------
snap('S3_C_BEFORE_ANSWER', {'phase':'C','lesson':lesson['type'],'shipped_ref':lesson.get('shipped_ref')})
rec({'event':'experiment_start','hypothesis':'wrong then correct answer executes distinct runtime paths and writes lesson_progress',
     'prepared_state':'fresh install, lesson opened, no prior answer','operation':'one wrong tap then one correct tap'})

# 1) WRONG option
w = lesson['wrong']
tap(w['x'],w['y'],'WRONG:'+w['label'])
st = dump('S3_D1_AFTER_WRONG_OPTION'); rec({'event':'ui','label':'D1_AFTER_WRONG_OPTION','texts':st['texts'][:20] if st else []})
snap('S3_D1_AFTER_WRONG_OPTION', {'phase':'D1','operation':'tap wrong option'})

# 2) Submit/Continue CTA after wrong (if enabled)
p2 = plan(UI/'S3_D1_AFTER_WRONG_OPTION.xml')
c2 = p2.get('cta')
if c2 and c2.get('enabled'):
    tap(c2['x'],c2['y'],'CTA_AFTER_WRONG')
    st = dump('S3_D2_AFTER_WRONG_SUBMIT'); rec({'event':'ui','label':'D2_AFTER_WRONG_SUBMIT','texts':st['texts'][:20] if st else []})
    snap('S3_D2_AFTER_WRONG_SUBMIT', {'phase':'D2','operation':'submit wrong answer'})
else:
    rec({'event':'cta_skipped','reason':'no enabled CTA after wrong option','cta':c2})

# 3) CORRECT option — re-read the current UI so coordinates are measured, not assumed
cur = dump('S3_E0_BEFORE_CORRECT')
p3 = plan(cur['path']) if cur else {'type':'PLAN_ERROR'}
co = p3.get('correct') if p3.get('type') == lesson['type'] else None
if not co:
    rec({'event':'correct_option_unresolved','reason':'current UI is not the same lesson',
         'current_plan_type':p3.get('type')})
if co:
    tap(co['x'],co['y'],'CORRECT:'+co['label'])
    st = dump('S3_E1_AFTER_CORRECT_OPTION'); rec({'event':'ui','label':'E1_AFTER_CORRECT_OPTION','texts':st['texts'][:20] if st else []})
    snap('S3_E1_AFTER_CORRECT_OPTION', {'phase':'E1','operation':'tap correct option'})
    p4 = plan(UI/'S3_E1_AFTER_CORRECT_OPTION.xml')
    c4 = p4.get('cta')
    if c4 and c4.get('enabled'):
        tap(c4['x'],c4['y'],'CTA_AFTER_CORRECT')
        st = dump('S3_F_AFTER_CORRECT_SUBMIT'); rec({'event':'ui','label':'F_AFTER_CORRECT_SUBMIT','texts':st['texts'][:20] if st else []})
        snap('S3_F_AFTER_CORRECT_SUBMIT', {'phase':'F','operation':'submit correct answer'})
    else:
        rec({'event':'cta_skipped','reason':'no enabled CTA after correct option','cta':c4})
rec({'event':'experiment_complete','lesson':lesson['type']})
