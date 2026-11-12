#!/usr/bin/env python3
"""Fresh install, offline, fixed first HTML exercise at varied viewport/font sizes."""
import hashlib, os, re, subprocess, time, xml.etree.ElementTree as ET
from pathlib import Path
root=Path(os.environ['RUNNER_TEMP']); out=root/'viewport-probe'; out.mkdir(exist_ok=True)
def adb(*x):
 p=subprocess.run(['adb',*x],capture_output=True,text=True);return p.stdout

def snap(name):
 adb('shell','uiautomator','dump','/sdcard/view.xml')
 xml=subprocess.run(['adb','exec-out','cat','/sdcard/view.xml'],capture_output=True).stdout
 (out/(name+'.xml')).write_bytes(xml)
 (out/(name+'.png')).write_bytes(subprocess.run(['adb','exec-out','screencap','-p'],capture_output=True).stdout)
 nodes=[]
 for n in ET.fromstring(xml).iter('node'):
  m=re.fullmatch(r'\[(\d+),(\d+)\]\[(\d+),(\d+)\]',n.get('bounds',''))
  if not m:continue
  a,b,c,d=map(int,m.groups());t=(n.get('text') or n.get('content-desc') or '').strip()
  if t:nodes.append((t,a,b,c,d,n.get('class',''),n.get('enabled','')))
  elif n.get('class')=='android.widget.FrameLayout' and n.get('clickable')=='true':
   label=' '.join((x.get('text') or '') for x in n.iter('node')).strip()
   if label:nodes.append(('[snippet] '+label,a,b,c,d,n.get('class',''),n.get('enabled','')))
  elif n.get('class')=='android.widget.Button' and n.get('enabled')=='true' and a>=230 and b>200:
   nodes.append(('[editor submit]',a,b,c,d,n.get('class',''),n.get('enabled','')))
 log.append(name+' '+repr(nodes));return nodes

def click(n, name):
 target=next((v for v in n if v[0]==name and v[3]>v[1] and v[4]>v[2]),None)
 if not target:log.append('NO VISIBLE '+name);return False
 _,x,y,x2,y2,_,_=target;adb('shell','input','tap',str((x+x2)//2),str((y+y2)//2));time.sleep(4);return True

log=['sha256='+hashlib.sha256((root/'candidate.apk').read_bytes()).hexdigest()]
adb('root');adb('wait-for-device');adb('shell','svc','wifi','disable');adb('shell','svc','data','disable')
for label,size,font in [('normal','320x640','1.0'),('small','320x480','1.0'),('largefont','320x640','1.5')]:
 adb('shell','wm','size',size);adb('shell','wm','density','160');adb('shell','settings','put','system','font_scale',font)
 adb('uninstall','com.getmimo');r=adb('install',str(root/'candidate.apk'));log.append(label+' install '+r.strip())
 adb('shell','monkey','-p','com.getmimo','-c','android.intent.category.LAUNCHER','1');time.sleep(15)
 n=snap(label+'_map')
 if not click(n,'Path Icon'):continue
 n=snap(label+'_intro1')
 if not click(n,'Continue'):continue
 n=snap(label+'_intro2')
 if not click(n,'Continue'):continue
 n=snap(label+'_question')
 if not click(n,'[snippet] <button>Like</button>'):continue
 n=snap(label+'_selected')
 if not click(n,'[editor submit]'):continue
 n=snap(label+'_feedback')
 if click(n,'Continue'):
  n=snap(label+'_next');log.append(label+' PROGRESSED_TO_NEXT='+str(any('step by step' in x[0] for x in n)))
 adb('shell','am','force-stop','com.getmimo')
adb('shell','wm','size','reset');adb('shell','wm','density','reset');adb('shell','settings','put','system','font_scale','1.0')
(out/'summary.txt').write_text('\n'.join(log)+'\n');print('\n'.join(log))
