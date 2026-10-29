import sys,re
from androguard.core.dex import DEX
TARGETS=set(x for x in sys.argv[2:] if x)
out={}
RX=re.compile(r'"([^"]*)"\s*$')
for f in sys.argv[1].split(','):
    d=DEX(open(f,'rb').read())
    for c in d.get_classes():
        cn=c.get_name()
        for m in c.get_methods():
            code=m.get_code()
            if code is None: continue
            try:
                for ins in m.get_instructions():
                    if ins.get_name().startswith('const-string'):
                        try: o=ins.get_output()
                        except Exception: continue
                        mm=RX.search(str(o))
                        if mm and mm.group(1) in TARGETS:
                            out.setdefault(mm.group(1),set()).add((cn,m.get_name()+m.get_descriptor()))
            except Exception: pass
for k in sorted(out):
    print('\n### '+k)
    for cn,mn in sorted(out[k])[:12]:
        print('    ',cn,'::',mn)
