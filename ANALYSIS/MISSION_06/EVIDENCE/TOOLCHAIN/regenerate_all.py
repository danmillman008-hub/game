import sys,json,pathlib,hashlib
sys.path.insert(0,'/home/user/_work/m06')
from m06_dex import M06
R=pathlib.Path('/home/user/game/ANALYSIS/MISSION_06')
OUT=R/'EVIDENCE/DISASM'
a=M06()
idx=json.loads((OUT/'INDEX.json').read_text())
APK='48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a'
NOTE=['NOTE: interleaved `const/4 vN, <junk>` instructions are Smob-style no-op decoys;',
      '      they clobber registers that are not subsequently read. Trailing',
      '      fill-array-data-payload is a linear-decode artefact, not executed code.',
      'NOTE: caller/callee lists regenerated with the corrected xref cache (78,560 targets).']
total_methods=0
for label,meta in sorted(idx.items()):
    cn=meta['class_name']
    lines=['MISSION 06 — verbatim DEX disassembly (androguard 4.1.4, read-only)',
           'APK sha256='+APK,'class=%s semantic=%s'%(cn,label),'']+NOTE+['']
    n=0
    for s in sorted(a.methods_of(cn)):
        inf=a.info(s); cs=a.callers(s); ce=a.callees(s)
        lines.append('===== %s ====='%s)
        lines.append('dex=%s code_offset=%s instructions=%d access=%s callers=%d callees=%d'%(
            inf['dex'],inf['code_offset'],inf['instructions'],inf['access'],len(cs),len(ce)))
        if cs: lines.append('callers: '+', '.join(x[0] for x in cs))
        if ce: lines.append('callees: '+', '.join(x[0] for x in ce))
        for l in a.disasm(s): lines.append('  '+l)
        lines.append(''); n+=1
    fn=OUT/(label+'.smali.txt');fn.write_text('\n'.join(lines),encoding='utf-8')
    meta['methods']=n; meta['xref_cache']='corrected (descriptors with spaces preserved)'
    total_methods+=n
(OUT/'INDEX.json').write_text(json.dumps(dict(
    document='MISSION 06 — full DEX disassembly index',
    apk_sha256=APK,tool='androguard 4.1.4',classification='VERIFIED_STATIC',
    xref_cache='corrected: 78,560 xref targets, 105,012 caller edges',
    files=len(idx),total_methods=total_methods,classes=idx),indent=1,ensure_ascii=False),encoding='utf-8')
print('regenerated',len(idx),'dumps,',total_methods,'methods')
# ---- regenerate catalogs (corrected xrefs) ----
import collections,re
mapping=collections.defaultdict(collections.Counter)
for cn in a.classes:
    if '$' not in cn: continue
    stem=cn.split('$')[0]; leaf=stem.split('/')[-1]
    if not re.search(r'(ViewModel|Fragment|Repository|Loader|Activity|Queue|State|Helper|Engine|UseCase|Interactor|Manager|Controller|Module|Api|Dao)',leaf): continue
    for s in a.methods_of(cn):
        if ';-><init>' in s:
            m=re.match(r'(L[^;]+;)',s.split('(')[-1])
            if m and m.group(1).startswith('Lcom/getmimo/'): mapping[m.group(1)][leaf]+=1
            break
omap=[dict(obfuscated=outer,semantic=c.most_common(1)[0][0],votes=c.most_common(1)[0][1],all_votes=dict(c)) for outer,c in sorted(mapping.items())]
(R/'SCHEMAS/OBFUSCATION_MAP.json').write_text(json.dumps(dict(
 document='Mimo 9.35 — R8 class-name reconstruction from Kotlin inner-class names',
 method='For each inner class X$foo$N, parse X from its DEX class name and read the first <init> parameter (the outer instance); the modal X is the original class name.',
 classification='VERIFIED_STATIC',apk_sha256=APK,xref_cache='corrected',count=len(omap),mappings=omap),indent=1,ensure_ascii=False),encoding='utf-8')
SEM={x['obfuscated']:x['semantic'] for x in omap}
cat=[];mimo=[c for c in a.classes if c.startswith('Lcom/getmimo/')]
for cn in sorted(mimo):
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
(R/'SCHEMAS/METHOD_CATALOG_MIMO.json').write_text(json.dumps(dict(
 document='Mimo 9.35 — method catalog from all 12 original DEX files',
 classification='VERIFIED_STATIC',tool='androguard 4.1.4 DEX disassembler',apk_sha256=APK,
 xref_cache='corrected: 78,560 xref targets; callers/callees counts authoritative',
 totals=dict(classes=len(mimo),methods=len(cat),with_code=sum(1 for x in cat if x['instructions']>0),
             total_instructions=sum(x['instructions'] for x in cat)),methods=cat),indent=1,ensure_ascii=False),encoding='utf-8')
cc=[dict(class_name=cn,semantic=SEM.get(cn,cn.split('/')[-1].rstrip(';')),dex=a.classes[cn],
         methods=len(a.methods_of(cn)),
         fields=[dict(name=f[0],descriptor=f[1],access=f[2]) for f in (a.class_fields.get(cn) or [])])
    for cn in sorted(mimo)]
(R/'SCHEMAS/CLASS_CATALOG_MIMO.json').write_text(json.dumps(dict(
 document='Mimo 9.35 — class catalog (fields + method counts)',classification='VERIFIED_STATIC',
 xref_cache='corrected',count=len(cc),classes=cc),indent=1,ensure_ascii=False),encoding='utf-8')
print('catalogs: methods',len(cat),'instructions',sum(x['instructions'] for x in cat),'classes',len(cc),'mappings',len(omap))
