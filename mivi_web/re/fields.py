import sys,re
from androguard.core.dex import DEX
d=DEX(open(sys.argv[1],'rb').read())
pat=re.compile(sys.argv[2])
for c in d.get_classes():
    if not pat.search(c.get_name()): continue
    print('CLASS',c.get_name())
    for f in c.get_fields():
        print('   field',f.get_name(),':',f.get_descriptor())
