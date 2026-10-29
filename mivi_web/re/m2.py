import sys
from androguard.core.dex import DEX
d=DEX(open(sys.argv[1],'rb').read())
want=set(sys.argv[2].split(','))
filt=sys.argv[3] if len(sys.argv)>3 else None
for c in d.get_classes():
    if c.get_name() not in want: continue
    print('='*90); print('CLASS',c.get_name())
    for m in c.get_methods():
        if filt and filt not in m.get_name(): continue
        code=m.get_code()
        if code is None: continue
        print('  METHOD',m.get_name()+m.get_descriptor())
        for ins in m.get_instructions():
            o=ins.get_output(); n=ins.get_name()
            if 'const-string' in n or 'invoke-interface' in n or 'JSONObject;->put' in str(o):
                print('     ',n,'|',o)
