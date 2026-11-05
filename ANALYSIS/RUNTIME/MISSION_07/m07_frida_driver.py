#!/usr/bin/env python3
"""MISSION 07 — attach Frida to the ORIGINAL com.getmimo process and collect
a JSONL trace. On this emulator the process NAME is 'Mimo', not the package
name (measured: frida-ps -U -> 3407 Mimo; adb shell pidof com.getmimo -> 3407).
Therefore attach by PID, never by get_process('com.getmimo'). Android is
'jailed' for Frida so spawn() is unsupported; attach is the correct mode.
"""
import sys, json, time, subprocess, pathlib
import frida

if len(sys.argv) < 4:
    print('usage: m07_frida_driver.py <script.js> <trace.jsonl> <seconds>'); sys.exit(2)
js_path, trace_path, duration = sys.argv[1], sys.argv[2], float(sys.argv[3])
out = pathlib.Path(trace_path); out.parent.mkdir(parents=True, exist_ok=True)
f = out.open('w', encoding='utf-8')

def write(o):
    f.write(json.dumps(o, ensure_ascii=False) + '\n'); f.flush()

def host_env():
    try:
        s = subprocess.check_output(['frida-ps', '-U'], stderr=subprocess.STDOUT, timeout=30).decode(errors='replace')
        return [l for l in s.splitlines() if 'Mimo' in l][:5]
    except Exception as e:
        return ['frida-ps failed: %s' % e]

def device_pid():
    try:
        return int(subprocess.check_output(['adb', 'shell', 'pidof', 'com.getmimo'],
                                          stderr=subprocess.DEVNULL, timeout=20).decode().strip().split()[0])
    except Exception:
        return None

dev = frida.get_usb_device(timeout=30)
write({'kind': 'driver_start', 'frida': frida.__version__, 'pidof_com.getmimo': device_pid(),
       'frida_ps_mimo': host_env(), 'timestamp_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())})
pid = device_pid()
proc = None
for p in dev.enumerate_processes():
    if (pid is not None and p.pid == pid) or p.name in ('Mimo', 'com.getmimo'):
        proc = p; break
if proc is None:
    print('[driver] process not found; aborting (no spawn on jailed Android)'); sys.exit(3)
print('[driver] attaching to pid=%d name=%s' % (proc.pid, proc.name))
session = None
for attempt in range(3):
    try:
        session = dev.attach(proc.pid)
        break
    except Exception as e:
        write({'kind':'attach_retry','attempt':attempt+1,'pid':proc.pid,'error':str(e)})
        print('[driver] attach attempt %d failed: %s; restarting frida-server' % (attempt+1, e))
        # A host-side `adb shell` keeps the server alive; restart it if reaped.
        try:
            subprocess.Popen(['adb','shell','/data/local/tmp/frida-server'],
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e2:
            write({'kind':'attach_restart_error','error':str(e2)})
        time.sleep(6)
        try: dev = frida.get_usb_device(timeout=30)
        except Exception: pass
if session is None:
    write({'kind':'driver_abort','reason':'frida-server not reachable after 3 attempts'})
    print('[driver] aborting: frida-server not reachable'); sys.exit(4)
write({'kind': 'attached', 'pid': proc.pid, 'name': proc.name})
js = pathlib.Path(js_path).read_text(encoding='utf-8')
# Frida 17 removed the built-in Java/ObjC bridges (frida 17.0.0 release notes;
# frida/frida#3473). frida-tools 14.11.0 ships the compiled bridge as
# frida_tools/bridges/java.js: `var bridge = function(){...}();`. We commit an
# exact copy and bind it as globalThis.Java before our agent code runs.
bridge_path = pathlib.Path(__file__).with_name('FRIDA') / 'java_bridge_frida17.js'
bridge_src = None
if bridge_path.exists():
    bridge_src = bridge_path.read_text(encoding='utf-8')
else:
    try:
        import frida_tools, os
        candidate = os.path.join(os.path.dirname(frida_tools.__file__), 'bridges', 'java.js')
        bridge_src = pathlib.Path(candidate).read_text(encoding='utf-8')
    except Exception as e:
        write({'kind':'bridge_error','error':str(e)})
if bridge_src:
    js = '(function(){\n' + bridge_src + '\nObject.defineProperty(globalThis,"Java",{value:bridge,configurable:true});\n})();\n' + js
    write({'kind':'bridge_loaded','bytes':len(bridge_src),'source':str(bridge_path)})
else:
    write({'kind':'bridge_missing','note':'script will fail if it uses Java'})
script = session.create_script(js)

def on_message(message, data):
    if message.get('type') == 'send':
        p = message.get('payload')
        if isinstance(p, str):
            try: o = json.loads(p)
            except Exception: o = {'kind': 'raw', 'text': p}
        else: o = p if isinstance(p, dict) else {'kind': 'raw', 'value': str(p)}
        o['_ts'] = time.strftime('%Y-%m-%dT%H:%M:%S', time.gmtime())
        write(o)
        if o.get('kind') in ('call_error', 'experiment_error', 'hook_error', 'emit_error'):
            print('[warn]', json.dumps(o, ensure_ascii=False)[:300])
    elif message.get('type') == 'error':
        write({'kind': 'script_error', 'description': message.get('description'),
               'stack': message.get('stack')})
        print('[error]', message.get('description'))
    else:
        write({'kind': 'frida_message', 'message': str(message)})

script.on('message', on_message)
script.load()
print('[driver] script loaded; collecting for %.0fs' % duration)
time.sleep(duration)
write({'kind': 'driver_done', 'elapsed_seconds': duration})
try: session.detach()
except Exception: pass
f.close()
print('[driver] done, messages=%d' % sum(1 for _ in out.open(encoding='utf-8')))
