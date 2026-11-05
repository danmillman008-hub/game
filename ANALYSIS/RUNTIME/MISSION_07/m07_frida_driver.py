#!/usr/bin/env python3
"""Attach Frida to the ORIGINAL com.getmimo process, run a JS probe, keep the
session alive for DURATION seconds while ADB experiments execute, and write
every message verbatim as JSONL runtime trace evidence."""
import frida, json, sys, time, pathlib

js_path, out_path, duration = sys.argv[1], sys.argv[2], float(sys.argv[3])
out = pathlib.Path(out_path); out.parent.mkdir(parents=True, exist_ok=True)
fh = out.open('w', encoding='utf-8')
lines = []
def on_message(message, data):
    rec = {'ts_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
           'type': message.get('type'), 'payload': message.get('payload')}
    if message.get('type') == 'error':
        rec['stack'] = message.get('stack'); rec['description'] = message.get('description')
    lines.append(rec); fh.write(json.dumps(rec, ensure_ascii=False) + '\n'); fh.flush()
    if rec['type'] == 'send':
        try:
            o = json.loads(message['payload'])
            print('[frida] %s %s %s' % (o.get('kind'), o.get('experiment',''), o.get('tag','')), flush=True)
        except Exception: print('[frida] %s' % message['payload'], flush=True)
    else:
        print('[frida:error] %s' % message.get('description'), flush=True)

dev = frida.get_usb_device(timeout=60)
try:
    proc = dev.get_process('com.getmimo')
    pid = proc.pid
    print('[driver] attaching to existing pid=%d' % pid, flush=True)
    session = dev.attach(pid)
    spawned = False
except Exception as e:
    print('[driver] no process (%s); spawning' % e, flush=True)
    pid = dev.spawn(['com.getmimo'])
    session = dev.attach(pid)
    spawned = True
script = session.create_script(pathlib.Path(js_path).read_text())
script.on('message', on_message)
script.load()
if spawned:
    dev.resume(pid)
print('[driver] script loaded, collecting for %.0fs' % duration, flush=True)
end = time.time() + duration
while time.time() < end:
    time.sleep(0.5)
try: script.unload()
except Exception: pass
try: session.detach()
except Exception: pass
fh.close()
print('[driver] messages=%d output=%s' % (len(lines), out_path), flush=True)
