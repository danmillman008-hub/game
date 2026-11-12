#!/usr/bin/env python3
"""Bounded fresh offline UI exploration; no asserted completion without evidence."""
import os, subprocess, time, re, xml.etree.ElementTree as ET
from pathlib import Path
out=Path(os.environ['RUNNER_TEMP'])/'progress-probe';out.mkdir(exist_ok=True)
def adb(*x): return subprocess.run(['adb',*x],capture_output=True,text=True).stdout
def capture(name):
 adb('shell','uiautomator','dump','/sdcard/progress.xml')
 xml= subprocess.run(['adb','exec-out','cat','/sdcard/progress.xml'],capture_output=True).stdout
 (out/(name+'.xml')).write_bytes(xml)
 (out/(name+'.png')).write_bytes(subprocess.run(['adb','exec-out','screencap','-p'],capture_output=True).stdout)
 activity=adb('shell','dumpsys','activity','activities');a=' '.join(x.strip() for x in activity.splitlines() if 'topResumedActivity' in x)
 try:r=ET.fromstring(xml)
 except ET.ParseError:return a,[]
 nodes=[]
 for n in r.iter('node'):
  text=(n.get('text') or n.get('content-desc') or '').strip();b=n.get('bounds','');m=re.fullmatch(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]',b)
  if text and m:
   x1,y1,x2,y2=map(int,m.groups());nodes.append((text,(x1+x2)//2,(y1+y2)//2,n.get('class','')))
 return a,nodes
log=[]
def snap(name):
 a,n=capture(name);log.append(name+' '+a+' TEXT: '+' | '.join(t[:120] for t,_,_,_ in n));return n
adb('shell','svc','wifi','disable');adb('shell','svc','data','disable')
adb('uninstall','com.getmimo');adb('install','-r',os.environ['RUNNER_TEMP']+'/candidate.apk')
adb('shell','monkey','-p','com.getmimo','-c','android.intent.category.LAUNCHER','1');time.sleep(15)
n=snap('00_map');icon=next((x for x in n if x[0]=='Path Icon'),None)
if icon:adb('shell','input','tap',str(icon[1]),str(icon[2]));time.sleep(8)
last='';same=0
for i in range(1,25):
 n=snap(f'{i:02}');texts='|'.join(t for t,_,_,_ in n)
 if texts==last:same+=1
 else:same=0
 last=texts
 # Exact labels or short actionable code; no guess at answer correctness.
 target=next((x for x in n if x[0] in ('Continue','Start','Start lesson','Run code','Run','Next','Got it')),None)
 if not target:target=next((x for x in n if x[0]=='<button>Like</button>'),None)
 if not target or same>=2:log.append('STOP no actionable progression or repeated screen');break
 log.append('TAP '+repr(target));adb('shell','input','tap',str(target[1]),str(target[2]));time.sleep(5)
adb('shell','am','force-stop','com.getmimo');adb('shell','monkey','-p','com.getmimo','-c','android.intent.category.LAUNCHER','1');time.sleep(15);snap('restart')
(out/'summary.txt').write_text('\n'.join(log)+'\n',encoding='utf-8')
(out/'crash.txt').write_text(adb('logcat','-d','-b','crash','-v','brief'))
print('\n'.join(log))
