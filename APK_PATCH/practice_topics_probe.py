#!/usr/bin/env python3
"""Compare previous and stats-fallback APK on a fresh, offline Android emulator."""
import hashlib, os, re, subprocess, time, xml.etree.ElementTree as ET
from pathlib import Path
root = Path(os.environ['RUNNER_TEMP']); out = root / 'practice-topics'; out.mkdir(exist_ok=True)

def adb(*args):
    r = subprocess.run(['adb', *args], capture_output=True, text=True)
    return r.stdout

def snap(name):
    adb('shell','uiautomator','dump','/sdcard/state.xml')
    xml=subprocess.run(['adb','exec-out','cat','/sdcard/state.xml'],capture_output=True).stdout
    (out/(name+'.xml')).write_bytes(xml)
    (out/(name+'.png')).write_bytes(subprocess.run(['adb','exec-out','screencap','-p'],capture_output=True).stdout)
    nodes=[]
    for n in ET.fromstring(xml).iter('node'):
        text=(n.get('text') or n.get('content-desc') or '').strip()
        m=re.fullmatch(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]', n.get('bounds',''))
        if text and m:
            a,b,c,d=map(int,m.groups());nodes.append((text,(a+c)//2,(b+d)//2))
    log.append(name+': '+' | '.join(t for t,_,_ in nodes)); return nodes

def click(nodes, predicate):
    target=next((x for x in nodes if predicate(x[0])),None)
    if target:
        log.append('tap '+repr(target));adb('shell','input','tap',str(target[1]),str(target[2]));time.sleep(8)
    else:log.append('target missing')
    return bool(target)

log=[]
adb('root');adb('wait-for-device');adb('shell','svc','wifi','disable');adb('shell','svc','data','disable')
log.append('network='+adb('shell','dumpsys','connectivity').split('Active default network:')[1].split('\n')[0].strip() if 'Active default network:' in adb('shell','dumpsys','connectivity') else 'network state unavailable')
for version in ('fallback','topics'):
    apk=root/version/'candidate.apk'
    log.append(version+' sha256='+hashlib.sha256(apk.read_bytes()).hexdigest())
    adb('uninstall','com.getmimo');result=adb('install',str(apk));log.append('install='+result.strip())
    if 'Success' not in result:continue
    adb('logcat','-c');adb('shell','monkey','-p','com.getmimo','-c','android.intent.category.LAUNCHER','1');time.sleep(15)
    n=snap(version+'_map')
    if click(n,lambda t:t.startswith('Practice')):
        n=snap(version+'_practice')
        if any(t=='Retry' for t,_,_ in n):
            click(n,lambda t:t=='Retry');snap(version+'_retry')
        elif version == 'topics':
            adb('shell','input','swipe','160','535','160','190','550');time.sleep(3);n=snap(version+'_scrolled')
            if any(t in ('Continue','Got it','Start','Get started') for t,_,_ in n):
                click(n,lambda t:t in ('Continue','Got it','Start','Get started'));n=snap(version+'_after_intro')
            candidates=[x for x in n if x[0] not in ('Practice','Playgrounds','Learn','Leaderboard','Profile','Start lesson','Lock in your learning','Progress in the path to unlock practice content') and 'image' not in x[0].lower()]
            log.append('practice_candidates='+repr(candidates))
            if any(t=='Start now' for t,_,_ in n):
                click(n,lambda t:t=='Start now');n=snap(version+'_opened')
                if any(t in ('Start lesson','Start learning','Start') for t,_,_ in n):
                    click(n,lambda t:t in ('Start lesson','Start learning','Start'));snap(version+'_exercise')
            elif any(t=='See all' for t,_,_ in n):
                click(n,lambda t:t=='See all');snap(version+'_opened')
    full=adb('logcat','-d','-v','brief')
    # Fresh emulator only; keep bounded relevant failures, not tokens or request bodies.
    relevant=[]
    for line in full.splitlines():
        if re.search(r'Error loading practice|AccessTokenUnavailable|NoConnectionException|FATAL EXCEPTION|AndroidRuntime|UnknownHostException|Exception in coroutine',line,re.I):
            line=re.sub(r'https?://\S+', '<url>',line)
            relevant.append(line)
    (out/(version+'_errors.txt')).write_text('\n'.join(relevant[-200:])+'\n')
    adb('shell','am','force-stop','com.getmimo')
(out/'summary.txt').write_text('\n'.join(log)+'\n'); print('\n'.join(log))
