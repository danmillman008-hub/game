import sys,json,pathlib
sys.path.insert(0,'/home/user/_work/m06')
from m06_dex import M06
OUT=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06/EVIDENCE/DISASM');OUT.mkdir(parents=True,exist_ok=True)
a=M06()
idx=json.loads((OUT/'INDEX.json').read_text())
T={
 'AssetTracksLoader':'Lye/b;','AssetTracksLoaderImpl':'Lye/d;','DefaultTrackLoader':'Lcom/getmimo/data/content/tracks/b;',
 'GetPathMapState':'Lcom/getmimo/interactors/path/d;','GetPathMapDialogs':'Lcom/getmimo/interactors/path/c;',
 'CompletionRepository':'Lcom/getmimo/data/source/local/completion/a;','CanOpenChapterWithKeys':'Lcom/getmimo/interactors/chapter/a;',
 'GetChapterEndSuccessState':'Lcom/getmimo/interactors/chapter/d;','NetworkUtils':'Lcom/getmimo/network/a;',
 'ConnectivityManagerNetworkMonitor':'Lcom/getmimo/network/b;','LessonProgressDao':'Lcg/a;',
 'ExecutableLessonViewModel2':'Lcom/getmimo/ui/lesson/executable/q;','CodeDiffViewModel':'Lam/o;',
 'CodeEditViewModel':'Lcom/getmimo/ui/codeeditor/view/b;','SplashViewModel':'Lcom/getmimo/ui/a;',
 'ChapterViewModel':'Lcom/getmimo/ui/chapter/ChapterViewModel;','DefaultRewardRepository':'Lcom/getmimo/data/source/remote/reward/a;',
 'DefaultKeysRepository':'Lcom/getmimo/data/source/remote/keys/a;','DefaultStreakRepository':'Lcom/getmimo/data/user/streak/a;',
 'SetDailyGoalViewModel':'Lcom/getmimo/ui/profile/b;','OnboardingSetDailyGoalViewModel':'Lcom/getmimo/ui/onboarding/dailygoal/OnboardingSetDailyGoalViewModel;',
 'ValidatedInputViewModel':'Lqm/d;','ValidatedInputNormalizer':'Lqm/i;','SelectionValidator':'Lkm/f;',
 'FillTheGapFragmentRunHandler':'Lim/d;','SpellFragmentRunHandler':'Lpm/b;','SelectionFragmentRunHandler':'Lnm/b;',
 'WebViewInteractionRunHandler':'Lmm/b;','OtherInteractionRunHandler':'Lkm/c;','OtherInteractionRunHandler2':'Lom/d;',
 'DataStoreUserPreferences':'Lcom/getmimo/data/local/a;','InteractiveLessonBaseFragment':'Lcom/getmimo/ui/lesson/interactive/base/b;',
 'NonInteractiveLessonFragment':'Lcom/getmimo/ui/lesson/interactive/nointeraction/a;',
 'InteractiveWebViewLessonFragment':'Lcom/getmimo/ui/lesson/interactive/webview/b;',
 'LessonBundle':'Lcom/getmimo/ui/lesson/interactive/LessonBundle;','LessonContent':'Lcom/getmimo/data/content/model/track/LessonContent;',
 'ExecuteFilesResponse':'Lcom/getmimo/data/model/codeeditor/ExecuteFilesResponse;','ExecuteLessonResponse':'Lcom/getmimo/data/model/codeeditor/ExecuteLessonResponse;',
 'TracksJson':'Lcom/getmimo/data/content/model/track/TracksJson;','TutorialJson':'Lcom/getmimo/data/content/model/track/TutorialJson;',
 'Chapter':'Lcom/getmimo/data/content/model/track/Chapter;','Lesson':'Lcom/getmimo/data/content/model/track/Lesson;',
 'SectionJson':'Lcom/getmimo/data/content/model/track/SectionJson;','TrackJson':'Lcom/getmimo/data/content/model/track/TrackJson;',
 'TutorialType':'Lcom/getmimo/data/content/model/track/TutorialType;','ChapterType':'Lcom/getmimo/data/content/model/track/ChapterType;',
 'ModuleVisibility':'Lcom/getmimo/data/content/lessonparser/interactive/model/ModuleVisibility;',
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
    print('wrote',label,n,fn.stat().st_size)
(OUT/'INDEX.json').write_text(json.dumps(idx,indent=1),encoding='utf-8')
