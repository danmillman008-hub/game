#!/usr/bin/env python3
"""Compare fresh direct startup with the application's own offline Skip route."""
import hashlib, os, re, subprocess, time, xml.etree.ElementTree as ET
from pathlib import Path
root=Path(os.environ['RUNNER_TEMP']); out=root/'guest-profile';out.mkdir(exist_ok=True)
def run(*args):
 r=subprocess.run(['adb',*args],capture_output=True,text=True);return r.stdout
def snap(name):
 run('shell','uiautomator','dump','/sdcard/guest.xml')
 raw=subprocess.run(['adb','exec-out','cat','/sdcard/guest.xml'],capture_output=True).stdout
 (out/(name+'.xml')).write_bytes(raw)
 (out/(name+'.png')).write_bytes(subprocess.run(['adb','exec-out','screencap','-p'],capture_output=True).stdout)
 try: tree=ET.fromstring(raw)
 except ET.ParseError: return []
 nodes=[]
 for n in tree.iter('node'):
  text=(n.get('text') or n.get('content-desc') or '').strip();m=re.fullmatch(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]',n.get('bounds',''))
  if text and m:
   a,b,c,d=map(int,m.groups());nodes.append((text,(a+c)//2,(b+d)//2))
 log.append(name+': '+' | '.join(x[0] for x in nodes));return nodes
log=['variant='+os.environ['VARIANT'],'sha256='+hashlib.file_digest(open(root/'candidate.apk','rb'),'sha256').hexdigest()]
run('root');run('wait-for-device');run('shell','svc','wifi','disable');run('shell','svc','data','disable')
r=subprocess.run(['adb','install',str(root/'candidate.apk')],capture_output=True,text=True);log.append('install='+r.stdout.strip());assert r.returncode==0 and 'Success' in r.stdout
run('shell','monkey','-p','com.getmimo','-c','android.intent.category.LAUNCHER','1');time.sleep(15)
for i in range(30):
 nodes=snap('step%02d'%i)
 if any(t=='Profile' for t,_,_ in nodes): break
 choice=subprocess.run(['python3','ANALYSIS/RUNTIME/MISSION_05/choose_tap.py',str(out/('step%02d.xml'%i))],capture_output=True,text=True).stdout.strip().split()
 if len(choice)<2 or not choice[0].isdigit(): log.append('STOP onboarding '+repr(choice));break
 log.append('tap '+ ' '.join(choice[:3]));run('shell','input','tap',choice[0],choice[1]);time.sleep(4)
else: log.append('STOP onboarding limit')
profile=next((p for p in nodes if p[0]=='Profile'),None)
if profile:
 run('shell','input','tap',str(profile[1]),str(profile[2]));time.sleep(10);snap('profile')
run('shell','am','force-stop','com.getmimo');run('shell','monkey','-p','com.getmimo','-c','android.intent.category.LAUNCHER','1');time.sleep(15);snap('restart')
(out/'summary.txt').write_text('\n'.join(log)+'\n');print('\n'.join(log))
