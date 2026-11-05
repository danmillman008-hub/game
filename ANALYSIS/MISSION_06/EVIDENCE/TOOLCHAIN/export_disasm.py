import sys,json,pathlib,re
sys.path.insert(0,'/home/user/_work/m06')
from m06_dex import M06
OUT=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06/EVIDENCE/DISASM');OUT.mkdir(parents=True,exist_ok=True)
a=M06()
MM={x['obfuscated_method']:x['semantic'] for x in json.load(open('/home/user/game/ANALYSIS/MISSION_06/SCHEMAS/METHOD_NAME_MAP.json'))['mappings']}
CC={x['obfuscated']:x['semantic'] for x in json.load(open('/home/user/game/ANALYSIS/MISSION_06/SCHEMAS/OBFUSCATION_MAP.json'))['mappings']}
TARGETS={
 'InteractiveLessonBaseViewModel':'Lcom/getmimo/ui/lesson/interactive/base/c;',
 'LessonProgressQueue':'Lcom/getmimo/data/source/remote/progress/LessonProgressQueue;',
 'LessonProgressRepository':'Lcom/getmimo/data/source/remote/progress/LessonProgressRepository;',
 'DefaultTracksRepository':'Lcom/getmimo/data/content/tracks/c;',
 'FillTheGapViewModel':'Lcom/getmimo/ui/lesson/interactive/fillthegap/a;',
 'SelectionViewModel':'Lcom/getmimo/ui/lesson/interactive/selection/a;',
 'SpellViewModel':'Lcom/getmimo/ui/lesson/interactive/spell/a;',
 'WebViewLessonViewModel':'Lcom/getmimo/ui/lesson/interactive/webview/c;',
 'ExecutableLessonViewModel':'Lcom/getmimo/ui/lesson/executable/q;',
 'PathMapViewModel':'Lcom/getmimo/ui/path/map/j;',
 'ChapterFinishedViewModel':'Lcom/getmimo/ui/chapter/chapterendview/main/f;',
 'InteractiveLessonViewModel':'Lcom/getmimo/ui/lesson/interactive/d;',
 'ParserModule':'Lcom/getmimo/data/content/lessonparser/interactive/ParserModule;',
 'Option':'Lcom/getmimo/data/content/lessonparser/interactive/model/Option;',
 'SelectionItem':'Lcom/getmimo/data/content/lessonparser/interactive/model/SelectionItem;',
 'Interaction':'Lcom/getmimo/data/content/lessonparser/interactive/model/Interaction;',
 'LessonModule':'Lcom/getmimo/data/content/lessonparser/interactive/model/LessonModule;',
 'ModuleVisibility':'Lcom/getmimo/data/content/lessonparser/interactive/model/ModuleVisibility;',
}
index={}
for label,cn in TARGETS.items():
    if cn not in a.classes: print('MISSING CLASS',label,cn);continue
    lines=['MISSION 06 — verbatim DEX disassembly (androguard 4.1.4, read-only)',
           'APK sha256=48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a',
           'class=%s  semantic=%s'%(cn,label),
           'NOTE: interleaved `const/4 vN, <junk>` instructions are Smob-style no-op decoys;',
           '      they clobber registers that are not subsequently read. Trailing',
           '      fill-array-data-payload is a linear-decode artefact, not executed code.','']
    entries=[]
    for s in sorted(a.methods_of(cn)):
        info=a.info(s); sem=MM.get(s,'')
        lines.append('===== %s ====='%s)
        if sem: lines.append('semantic_name=%s'%sem)
        lines.append('dex=%s code_offset=%s instructions=%d access=%s callers=%d callees=%d'%(
            info['dex'],info['code_offset'],info['instructions'],info['access'],
            len(a.callers(s)),len(a.callees(s))))
        cls,rest=s.split('->',1)
        callee_key=cls+';->'+rest
        cs=a.callers(callee_key) or a.callers(s)
        if cs: lines.append('callers: '+', '.join(sorted(set(c[0] for c in cs))[:8]))
        for l in a.disasm(s): lines.append('  '+l)
        lines.append('')
        entries.append(dict(signature=s,semantic=sem,**info))
    fn=OUT/(label+'.smali.txt');fn.write_text('\n'.join(lines),encoding='utf-8')
    index[label]=dict(class_name=cn,file=str(fn.relative_to(pathlib.Path('/home/user/game'))),methods=len(entries))
    print('wrote',label,len(entries),'methods',fn.stat().st_size)
pathlib.Path('/home/user/game/ANALYSIS/MISSION_06/EVIDENCE/DISASM/INDEX.json').write_text(json.dumps(index,indent=1),encoding='utf-8')
