import sys
from androguard.core.dex import DEX
TARGETS=sys.argv[2:]
data=open(sys.argv[1],'rb').read()
d=DEX(data)
idx={}
for c in d.get_classes():
    if c.get_name() in TARGETS:
        idx[c.get_name()]=c
for name,c in idx.items():
    print("="*100)
    print("CLASS",name, "methods:",len(list(c.get_methods())))
    for m in c.get_methods():
        code=m.get_code()
        if code is None:
            print(f"\n  -- {m.get_name()}{m.get_descriptor()}  [abstract/native]")
            continue
        strs=[]
        for ins in m.get_instructions():
            op=ins.get_name()
            if op.startswith('const-string'):
                try: strs.append(repr(ins.get_output()))
                except Exception: pass
        print(f"\n  -- {m.get_name()}{m.get_descriptor()}  ")
        if strs:
            print("     strings:", ", ".join(strs))
