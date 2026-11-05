import sys,json,pathlib,re,collections
sys.path.insert(0,'/home/user/_work/m06')
from m06_dex import M06
OUT=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06/CALL_GRAPHS');OUT.mkdir(parents=True,exist_ok=True)
a=M06()
CG=json.loads(pathlib.Path('/home/user/game/ANALYSIS/MISSION_06/SCHEMAS/METHOD_CATALOG_MIMO.json').read_text())
INFO={m['signature']:m for m in CG['methods']}

def build(name,title,roots,maxnodes=40,maxdepth=6,include=None,exclude=None):
    """BFS over real invoke xrefs from roots."""
    q=collections.deque((r,0) for r in roots)
    seen=set(); edges=[]; nodes=set()
    while q and len(seen)<maxnodes:
        s,d=q.popleft()
        if s in seen: continue
        seen.add(s); nodes.add(s)
        if exclude and any(s.split('->')[0].startswith(x) for x in exclude): continue
        if d>=maxdepth: continue
        for c in a.callees(s):
            t=c[0]
            if include and not any(t.split('->')[0].startswith(x) for x in include): continue
            if exclude and any(t.split('->')[0].startswith(x) for x in exclude): continue
            edges.append((s,t,c[1]))
            if t not in seen: q.append((t,d+1))
    # mermaid
    SEM={x['obfuscated']:x['semantic'] for x in json.loads(pathlib.Path('/home/user/game/ANALYSIS/MISSION_06/SCHEMAS/OBFUSCATION_MAP.json').read_text())['mappings']}
    MM={x['obfuscated_method']:x['semantic'] for x in json.loads(pathlib.Path('/home/user/game/ANALYSIS/MISSION_06/SCHEMAS/METHOD_NAME_MAP.json').read_text())['mappings']}
    def label(s):
        cn=s.split('->')[0]; raw=s.split('->')[1].split('(')[0]
        leaf=cn.split('/')[-1].rstrip(';')
        cls=SEM.get(cn,leaf)
        # Only high-confidence method renames; low-vote heuristic labels are kept
        # in SCHEMAS/METHOD_NAME_MAP.json but NOT shown as fact in a call graph.
        VERIFIED={
          'Lcom/getmimo/ui/lesson/interactive/base/c;':{
            'V':'lessonSolvedCorrectly','X':'lessonSolvedIncorrectly','W':'lessonSolvedCorrectlyWithPartialMatch',
            'U':'lessonSolvedAndProceedToNextLesson','d0':'showWrongFeedbackBlock',
            'b0':'onValidatedInputExecuted','h0':'configureInteraction','f0':'trackLessonResult',
            'e0':'storeLessonProgressInMemory','c0':'updateSolutionFeedback','Y':'onLessonRun',
            'H':'createLessonProgress','Z':'emitValidationResult'},
          'Lcom/getmimo/ui/lesson/executable/q;':{'I':'executeLessonAndStoreProgress','E':'doOnLessonCorrectlySolved',
            'F':'configureHints','K':'updateCodeExecutionState','J':'trackRunResult'},
          'Lcom/getmimo/ui/chapter/chapterendview/main/f;':{'G':'handleOnlineState','F':'getChapterEndSuccessStateWithRetry',
            'R':'handleChapterAlreadyCompletedState','O':'onContinue','E':'consumeKeyIfNeeded'},
          'Lcom/getmimo/ui/path/map/j;':{'L':'refreshPathMapState','M':'init','N':'shouldStartChapterInHardMode'},
        }
        m=VERIFIED.get(cn,{}).get(raw)
        if not m: m=raw
        return '%s.%s'%(cls if cls!=leaf else leaf,m)
    ids={};mmd=['```mermaid','flowchart TD']
    for i,s in enumerate(sorted(nodes)):
        ids[s]='N%d'%i
        inf=INFO.get(s,{})
        off=inf.get('code_offset')
        mmd.append('  %s["%s<br/><small>%s @%s</small>"]'%(ids[s],label(s),s.split('->')[0].split('/')[-2] if '/' in s.split('->')[0] else '', off if off is not None else 'ext'))
    for s,t,op in edges:
        if s in ids and t in ids and s!=t: mmd.append('  %s --> %s'%(ids[s],ids[t]))
    mmd.append('```')
    fn=OUT/(name+'.mmd');fn.write_text('# '+title+'\n\n'+'\n'.join(mmd)+'\n\nEdges are real `invoke-*` xrefs extracted from the 12 original DEX files (androguard 4.1.4).\n',encoding='utf-8')
    jf=OUT/(name+'.json')
    jf.write_text(json.dumps(dict(title=title,classification='VERIFIED_STATIC',
        apk_sha256='48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a',
        method='BFS over invoke-* xrefs from the listed root methods, bounded at depth %d / %d nodes'%(maxdepth,maxnodes),
        roots=roots,node_count=len(nodes),edge_count=len(edges),
        nodes=[dict(signature=s,dex=INFO.get(s,{}).get('dex'),code_offset=INFO.get(s,{}).get('code_offset'),
                    instructions=INFO.get(s,{}).get('instructions')) for s in sorted(nodes)],
        edges=[dict(caller=s,callee=t,opcode=op) for s,t,op in edges]),indent=1),encoding='utf-8')
    print('%-52s nodes=%-4d edges=%-4d'%(name,len(nodes),len(edges)))

B='Lcom/getmimo/ui/lesson/interactive/base/c;'
GENERIC=['Lcom/getmimo/','Lye/','Lte/','Lgm/','Lqm/','Lkm/','Lim/','Lnm/','Lpm/','Lmm/','Lom/','Lcg/','Lri/','Lze/','Lsk/','Ljm/','Lym/']
EXC=['Ljava/','Lkotlin/','Landroid/','Lkotlinx/','Landroidx/','Lorg/joda','Lcom/google/','Lorg/xmlpull','Lj$/']
build('01_answer_validation_core','USER INPUT → RUN → CORRECT/INCORRECT → PROGRESS RECORD',
 [B+'->Y(Z)V',
  'Lcom/getmimo/ui/lesson/interactive/base/InteractiveLessonBaseViewModel$onLessonRun$1;->invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object;'],
 maxnodes=36,maxdepth=5,include=GENERIC,exclude=EXC)
build('02_fillthegap_path','fillTheGap: content module → state → run handler → validation',
 ['Lcom/getmimo/ui/lesson/interactive/fillthegap/a;->E(Lcom/getmimo/data/content/model/track/LessonContent$Interactive;)V',
  'Lim/d;->E0()V'],maxnodes=34,maxdepth=5,include=GENERIC,exclude=EXC)
build('03_selection_path','selection: content module → state → run handler → km/f.b validator',
 ['Lcom/getmimo/ui/lesson/interactive/selection/a;->E(Lcom/getmimo/data/content/model/track/LessonContent$Interactive;)V',
  'Lnm/b;->E0()V','Lkm/c;->E0()V','Lom/d;->E0()V'],maxnodes=34,maxdepth=5,include=GENERIC,exclude=EXC)
build('04_spell_path','spell: content module → state → run handler → validation',
 ['Lcom/getmimo/ui/lesson/interactive/spell/a;->E(Lcom/getmimo/data/content/model/track/LessonContent$Interactive;)V','Lpm/b;->E0()V'],
 maxnodes=32,maxdepth=5,include=GENERIC,exclude=EXC)
build('05_validatedinput_path','validatedInput: typed text → normalizer → Correct/Partial/Incorrect → V/W/X',
 ['Lcom/getmimo/ui/lesson/interactive/validatedinput/InteractiveLessonValidatedInputFragment$setupViews$2;->invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object;',
  'Lcom/getmimo/ui/lesson/interactive/base/InteractiveLessonBaseViewModel$onValidatedInputExecuted$1;->invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object;',
  'Lqm/i;->a(Ljava/lang/String;)Ljava/lang/String;'],maxnodes=34,maxdepth=5,include=GENERIC,exclude=EXC)
build('06_content_pipeline','APK assets → AssetManager → JSON → XmlPullParser DSL → LessonModule → renderer',
 ['Lye/b;->d()Ljava/io/InputStream;','Lye/b;->b(J)Ljava/io/InputStream;',
  'Lcom/getmimo/data/content/tracks/b;->a(J I I)Lkotlinx/serialization/json/c;',
  'Lte/c;->b(Ljava/lang/String;)Ljava/util/ArrayList;','Lgm/h;->a(Ljava/util/List;)Lcom/getmimo/ui/lesson/interactive/model/LessonInteractionType;'],
 maxnodes=40,maxdepth=5,include=GENERIC+['Lorg/xmlpull/'],exclude=[x for x in EXC if x!='Lorg/xmlpull']+['Lkotlinx/'])
build('07_progress_persistence','correct/incorrect → LessonProgress → local Room queue → sync attempt',
 [B+'->V(Lkotlin/coroutines/jvm/internal/ContinuationImpl;)Ljava/lang/Object;',
  B+'->X(Lkotlin/coroutines/jvm/internal/ContinuationImpl;)Ljava/lang/Object;',
  'Lcom/getmimo/data/source/remote/progress/LessonProgressQueue;->storeLessonProgress(Lcom/getmimo/data/model/room/LessonProgress; Z Z Ld70/b;)Ljava/lang/Object;',
  'Lcom/getmimo/data/source/remote/progress/LessonProgressRepository;->postUnsyncedLessonProgress(Ld70/b;)Ljava/lang/Object;'],
 maxnodes=40,maxdepth=5,include=GENERIC,exclude=EXC)
build('08_executable_lesson','executableFiles → solvedContent comparison → progress / browser output',
 ['Lcom/getmimo/ui/lesson/executable/q;->I(Ldm/i; Lcom/getmimo/ui/lesson/interactive/LessonBundle; Ljava/util/ArrayList; Lcom/getmimo/data/content/model/track/LessonContent$Executable; Z)Ldm/i;',
  'Lcom/getmimo/ui/lesson/executable/q;->E(Lorg/orbitmvi/orbit/syntax/b;)Lcom/getmimo/data/model/room/LessonProgress;'],
 maxnodes=36,maxdepth=5,include=GENERIC+['Ldm/','Lzl/','Lep/','Lcm/'],exclude=EXC)
build('09_progression_and_offline','GetPathMapState / chapter completion / offline gate',
 ['Lcom/getmimo/interactors/path/GetPathMapState$invoke$3;->invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object;',
  'Lcom/getmimo/ui/chapter/chapterendview/main/ChapterFinishedViewModel$handleOfflineState$1;->invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object;',
  'Lcom/getmimo/network/a;->a()Z',
  'Lcom/getmimo/interactors/chapter/CanOpenChapterWithKeys$invoke$1;->invokeSuspend(Ljava/lang/Object;)Ljava/lang/Object;'],
 maxnodes=40,maxdepth=5,include=GENERIC+['Lvn/','Lcc/','Lri/','Lyg/','Lds/'],exclude=EXC)
