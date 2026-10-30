import sys,re
from androguard.core.dex import DEX
USAGE = "usage: fields.py <classes.dex> <class-regex>\n\nprint the fields of every class whose name matches the regex"
if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
    print(USAGE); raise SystemExit(0)
if len(sys.argv) < 3:
    print(USAGE, file=sys.stderr); raise SystemExit(2)
d=DEX(open(sys.argv[1],'rb').read())
pat=re.compile(sys.argv[2])
for c in d.get_classes():
    if not pat.search(c.get_name()): continue
    print('CLASS',c.get_name())
    for f in c.get_fields():
        print('   field',f.get_name(),':',f.get_descriptor())
