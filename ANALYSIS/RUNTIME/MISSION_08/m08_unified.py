#!/usr/bin/env python3
"""MISSION 08 — the ONLY new orchestrator.

It controls proven M07 tools; it does not reimplement them:
  * m07_frida_driver.py  -> Frida 17 attach + Java bridge (reused VERBATIM)
  * m07_db_snapshot.py   -> SQLite schema/row snapshots (reused VERBATIM)
  * m07_tap_target.py    -> measured XML tap targets (reused VERBATIM)
  * m07_lesson_plan.py   -> shipped-answer lesson classifier (reused VERBATIM)

Responsibilities: (1) find the real app PID with `ps -A`, (2) restart the M07
Frida driver whenever the process changes so the bridge is loaded in EVERY new
process, (3) state-aware UI exploration, (4) before/after state snapshots,
(5) merge UI / navigation / Frida / DB / network events into ONE correlated
JSONL timeline with experiment + action identifiers.

No framework, no static analyser, no separate observers.
"""
import argparse, hashlib, json, os, pathlib, re, subprocess, sys, threading, time
import xml.etree.ElementTree as ET

R = pathlib.Path('ANALYSIS/RUNTIME/MISSION_08')
M7 = pathlib.Path('ANALYSIS/RUNTIME/MISSION_07')
TL = R / 'TIMELINE' / 'MIMO_RUNTIME_TIMELINE.jsonl'
for d in ('TRACES', 'TIMELINE', 'STATE', 'UI', 'EXPERIMENTS', 'LOGS', 'ENV'):
    (R / d).mkdir(parents=True, exist_ok=True)
TL.write_text('', encoding='utf-8')

_lock = threading.Lock()
_seq = 0
_t0 = time.time()
_exp = 'EXP-R1-000'
_act = 'ACT-0000'
_last_screen = None
_edges = []
_screens = {}
_exp_history = [(_t0, 'EXP-R1-000')]
_prev_db = None


def emit(source, event, **fields):
    global _seq
    with _lock:
        _seq += 1
        o = {
            'seq': _seq,
            'ts_mono_ms': round((time.time() - _t0) * 1000, 3),
            'ts_utc': time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime()) + '.%03dZ' % int((time.time() % 1) * 1000),
            'experiment_id': _exp,
            'action_id': _act,
            'source': source,
            'event': event,
        }
        o.update(fields)
        with TL.open('a', encoding='utf-8') as f:
            f.write(json.dumps(o, ensure_ascii=False) + '\n')


def experiment(eid, title, **meta):
    global _exp
    if _exp != 'EXP-R1-000':
        emit('orchestrator', 'experiment_end', experiment_id_end=_exp)
    _exp = eid
    _exp_history.append((time.time(), eid))
    emit('orchestrator', 'experiment_start', title=title, **meta)


def action(label):
    global _act
    _act = 'ACT-%04d' % (int(_act.split('-')[1]) + 1)
    return _act


def adb(*a, timeout=45):
    try:
        return subprocess.run(['adb'] + list(a), capture_output=True, timeout=timeout).stdout.decode(errors='replace').strip()
    except Exception as e:
        return 'ADB_ERROR %s' % e


# ---------------------------------------------------------------------------
# PID detection: measured M07 process NAME is `Mimo`; do not assume pidof.
# ---------------------------------------------------------------------------
def ps_pid():
    out = adb('shell', 'ps -A')
    for line in out.splitlines():
        if re.search(r'\b(Mimo|com\.getmimo)\s*$', line.strip()) or re.search(r'\s(Mimo|com\.getmimo)\b', line):
            parts = line.split()
            # ps -A columns: USER PID PPID VSZ RSS WCHAN ADDR S NAME
            for i, p in enumerate(parts):
                if p.isdigit() and i >= 1 and 100 < int(p) < 100000:
                    return int(p)
    return None


def pidof_pid():
    try:
        s = adb('shell', 'pidof', 'com.getmimo')
        return int(s.split()[0])
    except Exception:
        return None


def frida_pid():
    try:
        out = subprocess.check_output(['frida-ps', '-U'], stderr=subprocess.DEVNULL, timeout=25).decode(errors='replace')
        for line in out.splitlines():
            if re.search(r'\bMimo\b', line):
                return int(line.split()[0])
    except Exception:
        pass
    return None


def real_pid():
    a, b, c = ps_pid(), pidof_pid(), frida_pid()
    pid = a or b or c
    return pid, {'ps_A': a, 'pidof': b, 'frida_ps': c, 'chosen': pid}


# ---------------------------------------------------------------------------
# Frida driver supervision (reuses m07_frida_driver.py, bridge loaded each time)
# ---------------------------------------------------------------------------
class FridaSupervisor:
    def __init__(self, agent, duration):
        self.agent = str(agent)
        self.deadline = time.time() + duration
        self.proc = None
        self.cur_pid = None
        self.generation = 0
        self.offsets = {}
        self.stop = False
        self.thread = threading.Thread(target=self._tail, daemon=True)
        self.thread.start()

    def trace_path(self, gen):
        return R / 'TRACES' / ('M08_R1_%02d.jsonl' % gen)

    def start(self, pid, pids):
        self.generation += 1
        tp = self.trace_path(self.generation)
        tp.write_text('', encoding='utf-8')
        remaining = max(30, min(240, int(self.deadline - time.time())))
        env = dict(os.environ, M08_TARGET_PID=str(pid))
        self.proc = subprocess.Popen(
            [sys.executable, str(M7 / 'm07_frida_driver.py'), self.agent, str(tp), str(remaining)],
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env)
        self.cur_pid = pid
        self.offsets[str(tp)] = 0
        emit('orchestrator', 'frida_attach', pid=pid, generation=self.generation,
             trace=str(tp), seconds=remaining, pid_detection=pids,
             note='m07_frida_driver.py reused verbatim; Java bridge loaded in this process')

    def stop_proc(self):
        if self.proc and self.proc.poll() is None:
            self.proc.terminate()
            try:
                self.proc.wait(timeout=8)
            except Exception:
                self.proc.kill()
        self.proc = None

    def _tail(self):
        """Merge every M07-driver trace line into the ONE shared timeline."""
        while not self.stop:
            for p in sorted((R / 'TRACES').glob('M08_R1_*.jsonl')):
                k = str(p)
                off = self.offsets.get(k, 0)
                try:
                    with p.open('rb') as f:
                        f.seek(off)
                        chunk = f.read()
                    self.offsets[k] = off + len(chunk)
                    for line in chunk.decode(errors='replace').splitlines():
                        if not line.strip():
                            continue
                        try:
                            o = json.loads(line)
                        except Exception:
                            continue
                        if o.get('kind') in ('driver_start', 'driver_done', 'bridge_loaded',
                                             'attached', 'ready', 'attach_retry'):
                            src = 'orchestrator'
                        else:
                            src = 'frida'
                        # assign experiment by wall-clock boundary (tail lag < 0.5 s)
                        e = _exp_history[0][1]
                        for t, eid in _exp_history:
                            if t <= time.time():
                                e = eid
                            else:
                                break
                        emit(src, o.get('kind', 'frida_event'),
                             experiment_id=e, **{kk: vv for kk, vv in o.items() if kk != 'kind'})
                except Exception:
                    pass
            time.sleep(0.4)

    def run(self):
        last = None
        try:
            while time.time() < self.deadline:
                pid, pids = real_pid()
                if pid is None:
                    emit('orchestrator', 'waiting_for_process', pid_detection=pids)
                    time.sleep(2)
                    continue
                if pid != last or self.proc is None or self.proc.poll() is not None:
                    if last is not None:
                        emit('orchestrator', 'process_change', old_pid=last, new_pid=pid,
                             pid_detection=pids, note='restarting M07 Frida driver -> bridge reloaded')
                    self.stop_proc()
                    self.start(pid, pids)
                    last = pid
                time.sleep(1.5)
        finally:
            self.stop_proc()
            self.stop = True
            emit('orchestrator', 'frida_supervisor_done', generations=self.generation)


# ---------------------------------------------------------------------------
# UI explorer (state-aware; reuses m07_tap_target.py for measured coordinates)
# ---------------------------------------------------------------------------
def dump_ui(label):
    name = 'S%03d_%s' % (_seq, re.sub(r'[^A-Za-z0-9]', '_', label))
    p = R / 'UI' / (name + '.xml')
    adb('shell', 'uiautomator', 'dump', '/sdcard/m08_ui.xml')
    adb('pull', '/sdcard/m08_ui.xml', str(p))
    if not p.exists():
        return None
    raw = p.read_text(errors='replace')
    texts = [t for t in re.findall(r'text="([^"]*)"', raw) if t.strip()]
    nodes = []
    try:
        root = ET.parse(p).getroot()
        for n in root.iter('node'):
            m = re.match(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', n.get('bounds') or '')
            if not m:
                continue
            x1, y1, x2, y2 = map(int, m.groups())
            own = (n.get('text') or '').strip()
            desc = (n.get('content-desc') or '').strip()
            rid = (n.get('resource-id') or '').strip()
            kids = [(d.get('text') or '').strip() for d in n.iter('node')
                    if d is not n and (d.get('text') or '').strip()]
            lab = own or desc or (kids[0] if kids else '') or rid
            nodes.append({'x': (x1 + x2) // 2, 'y': (y1 + y2) // 2, 'label': lab,
                          'rid': rid, 'clickable': n.get('clickable') == 'true',
                          'enabled': n.get('enabled') == 'true',
                          'y1': y1, 'x1': x1, 'x2': x2})
    except Exception:
        pass
    resumed = ''
    d = adb('shell', 'dumpsys', 'activity', 'activities')
    for line in d.splitlines():
        if 'topResumedActivity' in line or 'mResumedActivity' in line:
            resumed = line.strip()
            break
    fragments = []
    top = adb('shell', 'dumpsys', 'activity', 'top')
    for line in top.splitlines():
        if re.search(r'#\d+:|Added Fragments|Fragment\{', line):
            fragments.append(line.strip()[:220])
    sid = hashlib.sha1((resumed + '|' + '|'.join(sorted(set(texts)))).encode()).hexdigest()[:12]
    _screens[sid] = {'activity': resumed, 'texts': texts[:30],
                     'clickable': len([n for n in nodes if n['clickable']]),
                     'fragments': fragments[:12]}
    emit('ui', 'screen', screen_id=sid, label=label, xml=str(p), texts=texts[:30],
         clickable_nodes=len([n for n in nodes if n['clickable']]),
         resumed_activity=resumed, fragments=fragments[:12])
    return {'id': sid, 'nodes': nodes, 'texts': texts, 'activity': resumed, 'xml': str(p),
            'path': p}


def find_node(s, label):
    t = label.lower()
    cands = [n for n in s['nodes'] if n['clickable'] and n['enabled']]
    for n in cands:
        if n['label'].lower().strip() == t or t in n['label'].lower():
            return n
    for n in cands:
        if t in n['rid'].lower():
            return n
    return None


def m07_choose(s, prefer, avoid):
    """Reuse the proven M07 tap chooser (measured bounds, no blind tapping)."""
    try:
        out = subprocess.check_output(
            [sys.executable, str(M7 / 'm07_tap_target.py'), s['xml'], '',
             ';'.join(avoid), '|'.join(prefer)], timeout=25).decode().strip().splitlines()
        if out and not out[0].startswith('NONE'):
            p = out[0].split()
            return int(p[0]), int(p[1]), out[0]
    except Exception:
        pass
    return None


def tap(n, label, s=None):
    global _last_screen
    a = action(label)
    emit('ui', 'ui_action', action=a, kind='tap', x=n['x'], y=n['y'],
         label=label, from_screen=_last_screen)
    adb('shell', 'input', 'tap', str(n['x']), str(n['y']))
    time.sleep(2.4)
    ns = dump_ui(label + '_after')
    if ns:
        if _last_screen and _last_screen != ns['id']:
            _edges.append({'from': _last_screen, 'to': ns['id'], 'action': label,
                           'x': n['x'], 'y': n['y'], 'experiment': _exp})
        _last_screen = ns['id']
    return ns


def key(keycode, label):
    action(label)
    emit('ui', 'ui_action', kind='key', keycode=keycode, label=label, from_screen=_last_screen)
    adb('shell', 'input', 'keyevent', str(keycode))
    time.sleep(2.2)
    s = dump_ui(label + '_after')
    return s


# ---------------------------------------------------------------------------
# State observer (reuses m07_db_snapshot.py; only row-level diffs are emitted)
# ---------------------------------------------------------------------------
def state(label, synthetic=False):
    global _prev_db
    root = R / 'STATE' / label
    root.mkdir(parents=True, exist_ok=True)
    adb('shell', 'rm -rf /sdcard/m08_state; mkdir -p /sdcard/m08_state; '
        'for d in databases shared_prefs files/datastore no_backup; do '
        'if [ -e /data/data/com.getmimo/$d ]; then mkdir -p /sdcard/m08_state/$(dirname $d); cp -a /data/data/com.getmimo/$d /sdcard/m08_state/$d 2>/dev/null; fi; done')
    adb('pull', '/sdcard/m08_state', str(root / 'private'))
    for fn in (adb('shell', 'ls /data/data/com.getmimo/databases/') or '').split():
        fn = fn.strip()
        if fn.endswith(('-wal', '-shm', '-journal')):
            continue
        adb('shell', 'sqlite3 /data/data/com.getmimo/databases/%s ".backup /sdcard/m08_consistent.db"' % fn)
        adb('pull', '/sdcard/m08_consistent.db', str(root / ('consistent_' + fn)))
    out = R / 'STATE' / ('SNAPSHOT_' + label + '.json')
    subprocess.run([sys.executable, str(M7 / 'm07_db_snapshot.py'), str(root), label, str(out)],
                   capture_output=True, timeout=180)
    if not out.exists():
        emit('db', 'snapshot_error', label=label)
        return None
    d = json.loads(out.read_text())
    counts = {}
    rows = {}
    for db in d.get('databases', []):
        if 'mimo.db' not in db.get('path', ''):
            continue
        for t in db.get('tables', []):
            counts[t['name']] = t.get('row_count')
            rows[t['name']] = t.get('rows') or []
    emit('db', 'db_state', label=label, synthetic=synthetic, files=len(d.get('files', [])),
         tables=counts, snapshot_json=str(out))
    if _prev_db:
        diffs = {}
        for t in set(list(counts) + list(_prev_db['counts'])):
            a, b = _prev_db['counts'].get(t, 0), counts.get(t, 0)
            if a != b:
                diffs[t] = {'before': a, 'after': b, 'delta': b - a}
        before = set(map(tuple, _prev_db['rows'].get('lesson_progress', [])))
        after = set(map(tuple, rows.get('lesson_progress', [])))
        added = [list(x) for x in (after - before)][:20]
        removed = [list(x) for x in (before - after)][:20]
        emit('db', 'db_diff', label=label, from_label=_prev_db['label'],
             count_changes=diffs, lesson_progress_inserted=added,
             lesson_progress_deleted=removed)
    _prev_db = {'label': label, 'counts': counts, 'rows': rows}
    return d


def seed_synthetic(rows_sql):
    """Controlled state seeding — only when it exposes a decision algorithm."""
    for q in rows_sql:
        adb('shell', 'sqlite3 /data/data/com.getmimo/databases/mimo.db "%s"' % q)
    emit('db', 'state_seeded', synthetic=True, statements=rows_sql)


# ---------------------------------------------------------------------------
# Phase 1: ONE broad controlled investigation.
# ---------------------------------------------------------------------------
ONBOARD_PREFER = ['Skip', 'Continue', 'Get started', "Let's go", 'Set later',
                  'Casual', 'Mostly on the computer', 'No thanks', "Don't allow", 'Back']
ROUTES = ['Practice', 'Leaderboard', 'Profile', 'Learn', 'Settings', 'Goals', 'Streak']


def explore(steps, prefer, label, avoid_repeat=2):
    global _last_screen
    s = dump_ui(label + '_start')
    if s:
        _last_screen = s['id']
    avoid, seen, stagnant = set(), {}, 0
    for i in range(steps):
        s = dump_ui('%s_%02d' % (label, i))
        if not s:
            time.sleep(2)
            continue
        key = (s['id'], tuple(s['texts'][:6]))
        if seen.get(key, 0) >= avoid_repeat:
            break
        seen[key] = seen.get(key, 0) + 1
        r = m07_choose(s, prefer, avoid)
        if not r:
            emit('ui', 'exploration_stop', reason='no meaningful clickable target', step=i)
            break
        x, y, raw = r
        avoid.add('%d,%d' % (x, y))
        n = {'x': x, 'y': y, 'label': raw}
        before = s['id']
        ns = tap(n, '%s_%02d' % (label, i))
        if ns and ns['id'] == before:
            stagnant += 1
        else:
            stagnant = 0
            avoid.clear()
        if stagnant >= 4:
            emit('ui', 'exploration_stop', reason='four identical hierarchies', step=i)
            break
    return s


def route_tour():
    """State-aware: only tap labelled, meaningful application routes."""
    global _last_screen
    for route in ROUTES:
        s = dump_ui('route_' + route + '_before')
        if not s:
            continue
        n = find_node(s, route)
        if not n:
            emit('ui', 'route_not_found', route=route, screen=s['id'])
            continue
        emit('orchestrator', 'route_target', route=route, node=n)
        tap(n, 'route_' + route)
        state('S_ROUTE_' + route.upper())
        key(4, 'back_from_' + route)
        s2 = dump_ui('route_' + route + '_resumed')
        if s2:
            _last_screen = s2['id']


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--duration', type=int, default=720)
    ap.add_argument('--agent', default=str(R / 'm08_agent.js'))
    args = ap.parse_args()

    pid, pids = real_pid()
    emit('orchestrator', 'run_start', run_id=os.environ.get('GITHUB_RUN_ID', 'local'),
         apk_sha256='48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a',
         pid_detection=pids,
         tool_selection={'frida': 'M07 m07_frida_driver.py + Java bridge (reused)',
                         'db': 'M07 m07_db_snapshot.py (reused)',
                         'ui': 'M07 m07_tap_target.py + adb uiautomator (reused)',
                         'static': 'M06 METHOD_CATALOG_MIMO.json / CLASS_CATALOG_MIMO.json',
                         'rejected': 'Fastbot/Kea2/DroidBot/DarkRide/uiautomator2: no demonstrated advantage on API 36'})

    sup = FridaSupervisor(args.agent, args.duration)
    threading.Thread(target=sup.run, daemon=True).start()
    time.sleep(6)  # let attach + bridge + hooks settle

    # EXP 1 — startup / application architecture (relaunch while hooks are live)
    experiment('EXP-R1-001', 'Application startup, DI and activity creation',
               hypothesis='App.onCreate / Activity lifecycle / MainViewModel startup chain')
    adb('shell', 'am', 'force-stop', 'com.getmimo')
    time.sleep(2)
    emit('orchestrator', 'adb_command', cmd='am start -n com.getmimo/.ui.SplashActivity_default')
    adb('shell', 'am', 'start', '-n', 'com.getmimo/.ui.SplashActivity_default')
    time.sleep(14)
    dump_ui('startup_home')
    state('S0_STARTUP')

    # EXP 2 — onboarding / navigation graph discovery
    experiment('EXP-R1-002', 'State-aware onboarding exploration and screen transitions',
               hypothesis='real navigation graph + rendering/controller per screen')
    explore(26, ONBOARD_PREFER, 'onboard')
    state('S1_POST_ONBOARDING')

    # EXP 3 — guided route tour (ViewModel / Repository plumbing)
    experiment('EXP-R1-003', 'Main application routes: tabs, profile, goals, resume',
               hypothesis='Activity/Fragment -> ViewModel -> Repository chain per screen')
    route_tour()
    state('S2_POST_ROUTES')

    # EXP 4 — lesson engine + scoring + learner state in ONE correlated chain
    experiment('EXP-R1-004', 'Lesson path: answer -> feedback -> progress -> scoring',
               hypothesis='native V/W/X dispatch, correct/first-try counters, streak and reward triggers')
    s = dump_ui('lesson_entry_before')
    # Prefer "Continue"/"Start practicing"/"Learn" to enter a lesson; bounded.
    explore(12, ['Continue', 'Start practicing', 'Start', 'Learn', 'Practice'], 'to_lesson')
    state('S3_LESSON_BEFORE')
    # One controlled wrong then correct tap when a shipped classified lesson appears.
    try:
        p = subprocess.check_output(
            [sys.executable, str(M7 / 'm07_lesson_plan.py'),
             str(sorted((R / 'UI').glob('to_lesson_*.xml'))[-1])], timeout=20).decode()
        plan = json.loads(p)
    except Exception as e:
        plan = {'type': 'PLAN_ERROR', 'error': str(e)}
    emit('lesson', 'lesson_classification', plan=plan)
    if plan.get('wrong') and plan.get('correct'):
        emit('orchestrator', 'controlled_answer_start', plan_type=plan['type'],
             shipped_ref=plan.get('shipped_ref'))
        w, c = plan['wrong'], plan['correct']
        tap({'x': w['x'], 'y': w['y'], 'label': 'WRONG'}, 'answer_wrong')
        state('S4_AFTER_WRONG')
        tap({'x': c['x'], 'y': c['y'], 'label': 'CORRECT'}, 'answer_correct')
        state('S5_AFTER_CORRECT')
        cta = plan.get('cta')
        if cta and cta.get('enabled'):
            tap({'x': cta['x'], 'y': cta['y'], 'label': 'CTA'}, 'answer_submit')
            state('S6_AFTER_SUBMIT')
    else:
        emit('lesson', 'no_classified_lesson', note='recorded as UNKNOWN, not guessed')

    # EXP 5 — back / resume restoration
    experiment('EXP-R1-005', 'Back navigation and resume behaviour',
               hypothesis='learner state survives back/resume; canonical structures')
    key(4, 'back_from_lesson')
    state('S7_AFTER_BACK')
    explore(8, ['Continue', 'Resume', 'Learn', 'Start practicing'], 'resume')
    state('S8_AFTER_RESUME')

    # EXP 6 — network boundary snapshot (no forced offline: M07 already proved it)
    experiment('EXP-R1-006', 'Client/server responsibilities and event processing',
               hypothesis='which subsystems require a response vs work locally')
    emit('orchestrator', 'network_state', cmd='dumpsys connectivity')
    conn = adb('shell', 'dumpsys', 'connectivity')
    active = [l.strip()[:180] for l in conn.splitlines() if 'Active default network' in l][:2]
    emit('net', 'connectivity', active_default_network=active)
    time.sleep(12)

    emit('orchestrator', 'phase_complete', phase=1,
         note='second run decided only after inspecting this evidence')
    graph = {'screens': _screens, 'edges': _edges,
             'experiment': 'EXP-R1-001..006',
             'method': 'uiautomator hierarchy + dumpsys resumed activity + Frida ActivityLifecycleCallbacks'}
    (R / 'EXPERIMENTS' / 'NAV_GRAPH.json').write_text(json.dumps(graph, indent=1, ensure_ascii=False), encoding='utf-8')
    emit('orchestrator', 'navigation_graph_written', screens=len(_screens), edges=len(_edges))

    # allow supervisor to finish naturally, then stop
    time.sleep(min(20, max(0, args.duration - (time.time() - _t0))))
    sup.stop = True
    emit('orchestrator', 'timeline_done', events=_seq, path=str(TL))


if __name__ == '__main__':
    main()
