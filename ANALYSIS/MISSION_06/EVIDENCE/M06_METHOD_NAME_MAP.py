import sys,re,json,collections,pathlib
sys.path.insert(0,'/home/user/_work/m06')
from m06_dex import M06
OUT=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06')
a=M06()
# For each Kotlin inner class named SEMANTIC$N, find calls to the OUTER obfuscated class.
sem=collections.defaultdict(collections.Counter)
detail=collections.defaultdict(list)
for cn in a.classes:
    if '$' not in cn or not cn.startswith('Lcom/getmimo/'): continue
    stem=cn.split('$')[0]; leaf=stem.split('/')[-1]
    # semantic label = text between '$' markers (e.g. lessonSolvedCorrectly$1 -> lessonSolvedCorrectly)
    m=re.search(r'\$([A-Za-z][A-Za-z0-9_]*)\$\d+;$',cn)
    if not m: continue
    label=m.group(1)
    for s in a.methods_of(cn):
        if '->invokeSuspend' not in s and '->invoke' not in s: continue
        for line in a.disasm(s):
            mm=re.search(r'(L[A-Za-z0-9_/$<>]+;->[A-Za-z0-9_$]+)\(',line)
            if mm:
                target=mm.group(1)
                if target.startswith('Lcom/getmimo/') and target.split('->')[0]!=cn:
                    sem[target][label]+=1
                    detail[target].append((cn,label,line.strip()[:200]))
mapping=[]
for t,c in sorted(sem.items()):
    best,n=c.most_common(1)[0]
    mapping.append(dict(obfuscated_method=t,semantic=best,votes=n,all_votes=dict(c),
                        evidence=[dict(inner=x[0],label=x[1],call=x[2]) for x in detail[t][:6]]))
(OUT/'SCHEMAS/METHOD_NAME_MAP.json').write_text(json.dumps(dict(
 document='Mimo 9.35 — R8 method-name reconstruction from Kotlin coroutine inner classes',
 method='For each SEMANTIC$N inner class, disassemble invokeSuspend/invoke and record calls into the outer obfuscated class; modal label = original method name.',
 classification='VERIFIED_STATIC',apk_sha256='48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a',
 count=len(mapping),mappings=mapping),indent=1,ensure_ascii=False),encoding='utf-8')
print('method name map',len(mapping))
# print base VM mapping
print('\n=== InteractiveLessonBaseViewModel (c) method names ===')
for x in mapping:
    if 'interactive/base/c;->' in x['obfuscated_method']:
        print('  %-10s -> %-45s votes=%d'%(x['obfuscated_method'].split('->')[1].split('(')[0],x['semantic'],x['votes']))
print('\n=== PathMapViewModel (j) ===')
for x in mapping:
    if 'path/map/j;->' in x['obfuscated_method']:
        print('  %-10s -> %-45s'%(x['obfuscated_method'].split('->')[1].split('(')[0],x['semantic']))
print('\n=== ChapterFinishedViewModel (f) ===')
for x in mapping:
    if 'chapterendview/main/f;->' in x['obfuscated_method']:
        print('  %-10s -> %-45s'%(x['obfuscated_method'].split('->')[1].split('(')[0],x['semantic']))
print('\n=== ExecutableLessonViewModel (q) ===')
for x in mapping:
    if 'executable/q;->' in x['obfuscated_method']:
        print('  %-10s -> %-45s'%(x['obfuscated_method'].split('->')[1].split('(')[0],x['semantic']))
