#!/usr/bin/env python3
"""Bounded fresh offline UI exploration; no asserted completion without evidence."""
import os, subprocess, time, re, sqlite3, xml.etree.ElementTree as ET
from pathlib import Path
out=Path(os.environ['RUNNER_TEMP'])/'webview-probe'/os.environ['PROFILE'];out.mkdir(parents=True,exist_ok=True)
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
  if m:
   x1,y1,x2,y2=map(int,m.groups())
   if text:nodes.append((text,(x1+x2)//2,(y1+y2)//2,n.get('class','')))
   elif n.get('class')=='android.widget.FrameLayout' and n.get('clickable')=='true' and y1>=320:
    label=' '.join((d.get('text') or '') for d in n.iter('node')).strip()
    if label:nodes.append(('[snippet] '+label,(x1+x2)//2,(y1+y2)//2,n.get('class','')))
   elif n.get('class')=='android.widget.Button' and n.get('enabled')=='true' and x1>=240 and y1>250:
    nodes.append(('[editor submit]',(x1+x2)//2,(y1+y2)//2,n.get('class','')))
 return a,nodes
import hashlib
with open(os.environ['RUNNER_TEMP']+'/candidate.apk','rb') as f:
 apk_sha=hashlib.file_digest(f,'sha256').hexdigest()
log=['candidate_sha256='+apk_sha, 'WARNING: diagnostic build; not verified fully offline']
def snap(name):
 a,n=capture(name);log.append(name+' '+a+' TEXT: '+' | '.join(t[:120] for t,_,_,_ in n));return n
adb('root'); adb('wait-for-device')
adb('shell','wm','size',os.environ['SCREEN_SIZE']);adb('shell','wm','density','160');adb('shell','settings','put','system','font_scale',os.environ['FONT_SCALE'])
adb('shell','svc','wifi','disable');adb('shell','svc','data','disable')
adb('uninstall','com.getmimo');adb('install','-r',os.environ['RUNNER_TEMP']+'/candidate.apk')
adb('shell','monkey','-p','com.getmimo','-c','android.intent.category.LAUNCHER','1');time.sleep(15)
n=snap('00_map');icon=next((x for x in n if x[0]=='Path Icon'),None)
if icon:adb('shell','input','tap',str(icon[1]),str(icon[2]));time.sleep(8)
last='';same=0
for i in range(1,65):
 n=snap(f'{i:02}');texts='|'.join(t for t,_,_,_ in n)
 if texts==last:same+=1
 else:same=0
 last=texts
 if 'Guess the letter' in texts:
  d=next((x for x in n if x[0]=='D' and x[3]=='android.widget.Button'),None)
  if not d:
   log.append('STOP letter D not visible');break
  log.append('TAP ANSWER '+repr(d));adb('shell','input','tap',str(d[1]),str(d[2]));time.sleep(5)
  n=snap('guess_answered'); found=next((x for x in n if x[0]=='Continue'),None)
  log.append('CONTINUE_AFTER_WEBVIEW_ANSWER='+repr(found))
  if found:
   adb('shell','input','tap',str(found[1]),str(found[2]));time.sleep(5);snap('guess_next')
  else:
   adb('shell','input','swipe','160','430','160','180','500');time.sleep(4);snap('guess_after_scroll')
  break
 # Exact labels or short actionable code; no guess at answer correctness.
 target=next((x for x in n if x[0] in ('Continue','Start','Start lesson','Run code','Run','Next','Got it','[editor submit]')),None)
 if not target:
  snippets=[x for x in n if x[0].startswith('[snippet]')]
  if len(snippets)==1:target=snippets[0]
  elif 'Add the text Like to the button.' in texts:
   target=next((x for x in snippets if x[0]=='[snippet] Like'),None)
  elif 'Time to create the first button.' in texts:
   code=next((x[0] for x in n if x[0].startswith('<button>') and 'W' in x[0]),'WWW')
   wanted = '<button>' if code == 'WWW' else ('Q' if code == '<button>WW' else '</button>')
   target=next((x for x in snippets if x[0]=='[snippet] '+wanted),None)
  elif 'label R.' in texts or 'label D.' in texts:
   letter = 'R' if 'label R.' in texts else 'D'
   editor=next((x[0] for x in n if '\n' in x[0] and 'W' in x[0]),'')
   line=editor.split('\n')[-1]
   wanted='<button>' if line=='WWW' else (letter if line=='<button>WW' else '</button>')
   target=next((x for x in snippets if x[0]=='[snippet] '+wanted),None)
 if not target or same>=2:log.append('STOP no actionable progression or repeated screen');break
 log.append('TAP '+repr(target));adb('shell','input','tap',str(target[1]),str(target[2]));time.sleep(5)
def db_summary(stage):
 # Force-stopped fresh emulator test DB only; copy WAL if present. Do not commit DB.
 import tempfile
 with tempfile.TemporaryDirectory() as td:
  for suffix in ('','-wal','-shm'):
   subprocess.run(['adb','pull','/data/data/com.getmimo/databases/mimo.db'+suffix,td+'/mimo.db'+suffix],capture_output=True)
  try:
   con=sqlite3.connect('file:'+td+'/mimo.db?mode=ro',uri=True)
   rows=con.execute('SELECT lesson_id,tutorial_id,in_queue FROM lesson_progress ORDER BY lesson_id,tutorial_id').fetchall()
   log.append(stage+' progress_rows='+repr(rows));con.close()
  except Exception as e:log.append(stage+' DB_UNAVAILABLE '+str(e))
adb('shell','am','force-stop','com.getmimo');db_summary('before_restart')
adb('shell','monkey','-p','com.getmimo','-c','android.intent.category.LAUNCHER','1');time.sleep(15);snap('restart')
adb('shell','am','force-stop','com.getmimo');db_summary('after_restart')
(out/'summary.txt').write_text('\n'.join(log)+'\n',encoding='utf-8')
(out/'crash.txt').write_text(adb('logcat','-d','-b','crash','-v','brief'))
print('\n'.join(log))
