import sys,json,pathlib
sys.path.insert(0,'/home/user/_work/m06')
from m06_dex import M06
OUT=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06/EVIDENCE/DISASM')
a=M06(); idx=json.loads((OUT/'INDEX.json').read_text())
T={
 'DSL_LessonParser':'Lte/c;','DSL_CodeModuleParser':'Lte/a;','DSL_ParagraphModuleParser':'Lte/d;',
 'DSL_SelectionModuleParser':'Lte/e;','DSL_DatabaseModuleParser':'Lte/b;','DSL_TableParser':'Lte/f;',
 'DSL_WebviewModuleParser':'Lte/g;','LessonInteractionTypeMapper':'Lgm/h;',
 'InteractiveLessonBaseVM_onLessonRun':'Lcom/getmimo/ui/lesson/interactive/base/InteractiveLessonBaseViewModel$onLessonRun$1;',
 'ValidatedInput_ResultCollector':'Lcom/getmimo/ui/lesson/interactive/validatedinput/InteractiveLessonValidatedInputFragment$setupViews$2;',
 'ValidatedInput_TextWatcher':'Lqm/b;','ValidatedInput_InputAccessor':'Lcom/getmimo/ui/lesson/interactive/validatedinput/a;',
 'GetPathMapState_Invoke':'Lcom/getmimo/interactors/path/GetPathMapState$invoke$3;',
 'ChapterFinishedVM_handleOfflineState':'Lcom/getmimo/ui/chapter/chapterendview/main/ChapterFinishedViewModel$handleOfflineState$1;',
 'LessonProgress':'Lcom/getmimo/data/model/room/LessonProgress;',
 'AnswersInChapter':'Lcom/getmimo/data/source/remote/progress/AnswersInChapter;',
 'LessonInteractionType':'Lcom/getmimo/ui/lesson/interactive/model/LessonInteractionType;',
 'WebViewActivityResult':'Lcom/getmimo/ui/lesson/interactive/webview/WebViewActivityResult;',
 'ContentLocale':'Lcom/getmimo/data/content/model/track/ContentLocale;',
 'RunButtonState':'Lcom/getmimo/ui/common/runbutton/RunButton$State;',
 'ModuleVisibility':'Lcom/getmimo/data/content/lessonparser/interactive/model/ModuleVisibility;',
 'TutorialType':'Lcom/getmimo/data/content/model/track/TutorialType;',
 'ChapterType':'Lcom/getmimo/data/content/model/track/ChapterType;',
 'DataStoreUserPreferences':'Lcom/getmimo/data/local/a;',
}
for label,cn in T.items():
    if cn not in a.classes: print('MISSING',label,cn);continue
    lines=['MISSION 06 — verbatim DEX disassembly (androguard 4.1.4, read-only)',
           'APK sha256=48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a',
           'class=%s semantic=%s'%(cn,label),'']
    n=0
    for s in sorted(a.methods_of(cn)):
        inf=a.info(s)
        lines.append('===== %s ====='%s)
        lines.append('dex=%s code_offset=%s instructions=%d access=%s callers=%d callees=%d'%(
            inf['dex'],inf['code_offset'],inf['instructions'],inf['access'],len(a.callers(s)),len(a.callees(s))))
        for l in a.disasm(s): lines.append('  '+l)
        lines.append('');n+=1
    fn=OUT/(label+'.smali.txt');fn.write_text('\n'.join(lines),encoding='utf-8')
    idx[label]=dict(class_name=cn,file=str(fn.relative_to(pathlib.Path('/home/user/game'))),methods=n)
    print('wrote',label,n)
(OUT/'INDEX.json').write_text(json.dumps(idx,indent=1),encoding='utf-8')
