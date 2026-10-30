import sys,glob
from androguard.core.dex import DEX
USAGE = "usage: staticdump.py <a.dex[,b.dex]> <string> [<string> ...]\n\nprint the static string fields of classes containing any of the strings"
if len(sys.argv) > 1 and sys.argv[1] in ('-h', '--help'):
    print(USAGE); raise SystemExit(0)
if len(sys.argv) < 3:
    print(USAGE, file=sys.stderr); raise SystemExit(2)
TARGET=set(sys.argv[2:])
def val(ev):
    try: return ev.get_value()
    except Exception: return None
for f in sys.argv[1].split(','):
    d=DEX(open(f,'rb').read())
    for c in d.get_classes():
        try: sv=c.get_static_values()
        except Exception: continue
        if not sv: continue
        vals=[val(e) for e in sv]
        hit=[v for v in vals if isinstance(v,str) and v in TARGET]
        if hit:
            print('='*90)
            print('CLASS',c.get_name())
            flds=[fl.get_name() for fl in c.get_fields()]
            for n,v in zip(flds,vals):
                if isinstance(v,str) and ('/algo/' in v or '/common/' in v or '/style/' in v or '/file/' in v or '/storyart' in v):
                    print('   ',n,'=',v)
