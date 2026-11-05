import sys,re,json,collections,pathlib
sys.path.insert(0,'/home/user/_work/m06')
from m06_dex import M06
OUT=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06')
a=M06()
# ---- obfuscation map ----
mapping=collections.defaultdict(collections.Counter)
for cn in a.classes:
    if '$' not in cn: continue
    stem=cn.split('$')[0]; leaf=stem.split('/')[-1]
    if not re.search(r'(ViewModel|Fragment|Repository|Loader|Activity|Queue|State|Helper|Engine|UseCase|Interactor|Manager|Controller|Module|Api|Dao)',leaf): continue
    for s in a.methods_of(cn):
        if ';-><init>' in s:
            m=re.match(r'(L[^;]+;)',s.split('(')[-1])
            if m and m.group(1).startswith('Lcom/getmimo/'):
                mapping[m.group(1)][leaf]+=1
            break
omap=[]
for outer,c in sorted(mapping.items()):
    best,n=c.most_common(1)[0]
    omap.append(dict(obfuscated=outer,semantic=best,votes=n,all_votes=dict(c)))
(OUT/'SCHEMAS/OBFUSCATION_MAP.json').write_text(json.dumps(dict(
 document='Mimo 9.35 — R8 class-name reconstruction from Kotlin inner-class names',
 method='For each inner class X$foo$N, parse X from its DEX class name and read the first <init> parameter (the outer instance); the modal X is the original class name.',
 classification='VERIFIED_STATIC',apk_sha256='48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a',
 count=len(omap),mappings=omap),indent=1,ensure_ascii=False),encoding='utf-8')
print('obfuscation map',len(omap))
SEM={x['obfuscated']:x['semantic'] for x in omap}
# ---- method catalog for Mimo classes ----
cat=[]
mimo_classes=[c for c in a.classes if c.startswith('Lcom/getmimo/')]
for cn in sorted(mimo_classes):
    for s in sorted(a.methods_of(cn)):
        dn,m=a.methods[s]
        try: n=len(list(m.get_instructions()))
        except Exception: n=0
        try: co=m.get_code_off()
        except Exception: co=None
        cat.append(dict(signature=s,class_name=cn,semantic_class=SEM.get(cn,cn.split('/')[-1].rstrip(';')),
                        method=m.get_name(),descriptor=m.get_descriptor(),access=m.get_access_flags_string(),
                        dex=dn,code_offset=co,instructions=n,
                        callers=len(a.xref_to.get(s,[])),callees=len(a.xref_from.get(s,[])),
                        strings=a.strings_by_method.get(s,[])[:8]))
(OUT/'SCHEMAS/METHOD_CATALOG_MIMO.json').write_text(json.dumps(dict(
 document='Mimo 9.35 — method catalog from all 12 original DEX files',
 classification='VERIFIED_STATIC',tool='androguard 4.1.4 DEX disassembler',
 apk_sha256='48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a',
 totals=dict(classes=len(mimo_classes),methods=len(cat),
             with_code=sum(1 for x in cat if x['instructions']>0),
             total_instructions=sum(x['instructions'] for x in cat)),
 methods=cat),indent=1,ensure_ascii=False),encoding='utf-8')
print('method catalog',len(cat),'classes',len(mimo_classes),'insns',sum(x['instructions'] for x in cat))
# ---- class catalog ----
cc=[]
for cn in sorted(mimo_classes):
    cc.append(dict(class_name=cn,semantic=SEM.get(cn,cn.split('/')[-1].rstrip(';')),
                   dex=a.classes[cn],methods=len(a.methods_of(cn)),
                   fields=[dict(name=f[0],descriptor=f[1],access=f[2]) for f in a.class_fields.get(cn,[])]))
(OUT/'SCHEMAS/CLASS_CATALOG_MIMO.json').write_text(json.dumps(dict(
 document='Mimo 9.35 — class catalog (fields + method counts)',classification='VERIFIED_STATIC',
 count=len(cc),classes=cc),indent=1,ensure_ascii=False),encoding='utf-8')
print('class catalog',len(cc))
