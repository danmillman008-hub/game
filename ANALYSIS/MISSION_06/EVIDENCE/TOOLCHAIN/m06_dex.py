"""MISSION 06 read-only DEX analysis harness (Androguard 4.1.4).
Indexes all 12 original DEX files; provides disassembly, xrefs, fields, strings.
Nothing is written into the APK/DEX or into Git unless explicitly exported."""
import os, sys, json, glob, pickle, collections, logging
from androguard.core.dex import DEX
try:
    from loguru import logger
    logger.remove()
except Exception:
    pass

DEXDIR='/home/user/game/ANALYSIS/_INPUT'
CACHE='/home/user/_work/m06/cache.pkl'
FILES=sorted(glob.glob(DEXDIR+'/classes*.dex'), key=lambda p:(len(p),p))

class M06:
    def __init__(self, build_xref=True):
        self.dex={}
        for p in FILES:
            n=os.path.basename(p)
            self.dex[n]=DEX(open(p,'rb').read())
        self.methods={}       # full "Lclass;->name(proto)Ret" -> (dex, obj)
        self.class_methods=collections.defaultdict(list)
        self.class_fields=collections.defaultdict(list)
        self.classes={}
        for dn,d in self.dex.items():
            for c in d.get_classes():
                cn=c.get_name()
                self.classes.setdefault(cn,[]).append(dn)
                for f in c.get_fields():
                    self.class_fields[cn].append((f.get_name(),f.get_descriptor(),f.get_access_flags_string()))
                for m in c.get_methods():
                    sig=str(m.get_class_name())+'->'+str(m.get_name())+str(m.get_descriptor())
                    self.methods[sig]=(dn,m)
                    self.class_methods[cn].append(sig)
        self.xref_to=collections.defaultdict(list)   # callee -> [(caller, opcode, off)]
        self.xref_from=collections.defaultdict(list) # caller -> [(callee, opcode, off)]
        self.field_xref=collections.defaultdict(list)
        self.strings_by_method=collections.defaultdict(list)
        if build_xref:
            if os.path.exists(CACHE):
                with open(CACHE,'rb') as f:
                    (self.xref_to,self.xref_from,self.field_xref,self.strings_by_method)=pickle.load(f)
            else:
                self._build()
                with open(CACHE,'wb') as f:
                    pickle.dump((self.xref_to,self.xref_from,self.field_xref,self.strings_by_method),f)

    def _build(self):
        import re
        # Method/field refs are the LAST operand of the instruction text. Descriptors
        # may contain spaces (e.g. `(Ljava/util/List; Z)V`), so capture to end-of-line.
        RX = re.compile(r'(L[A-Za-z0-9_/$<>\-]+;->.*)$')
        for dn, d in self.dex.items():
            for c in d.get_classes():
                for m in c.get_methods():
                    caller = str(m.get_class_name()) + '->' + str(m.get_name()) + str(m.get_descriptor())
                    try:
                        ins = list(m.get_instructions())
                    except Exception:
                        continue
                    pc = 0
                    try: co = m.get_code_off()
                    except Exception: co = 0
                    for i in ins:
                        op = i.get_name(); off = pc; txt = str(i)
                        if op.startswith('invoke'):
                            mm = RX.search(txt)
                            if mm:
                                callee = mm.group(1).strip()
                                self.xref_to[callee].append((caller, op, off, dn))
                                self.xref_from[caller].append((callee, op, off, dn))
                        elif op.startswith(('iget','iput','sget','sput')):
                            mm = RX.search(txt)
                            if mm:
                                self.field_xref[mm.group(1)].append((caller, op, off, dn))
                        elif op in ('const-string','const-string/jumbo'):
                            q = txt.find('"')
                            if q >= 0:
                                self.strings_by_method[caller].append(txt[q:][:300])
                        pc += i.get_length()

    def find_classes(self,*needles):
        return sorted(cn for cn in self.classes if any(n in cn for n in needles))
    def methods_of(self,cn):
        return self.class_methods.get(cn,[])
    def find_methods(self,*needles):
        return sorted(s for s in self.methods if any(n in s for n in needles))
    def disasm(self,sig):
        dn,m=self.methods[sig]
        out=[]
        try: ins=list(m.get_instructions())
        except Exception as e: return ['<decode error %s>'%e]
        pc=0
        for i in ins:
            try: txt=str(i)
            except Exception: txt=i.get_name()
            out.append('%06x  %s'%(pc,txt))
            pc += i.get_length()
        return out
    def info(self,sig):
        dn,m=self.methods[sig]
        try: n=len(list(m.get_instructions()))
        except Exception: n=-1
        try: regs=m.get_registers_size()
        except Exception: regs=-1
        return dict(dex=dn,class_name=m.get_class_name(),name=m.get_name(),descriptor=m.get_descriptor(),
                    access=m.get_access_flags_string(),instructions=n,registers=regs,
                    code_offset=getattr(m,'get_code_off',lambda:None)())
    def callers(self,sig): return sorted(set((c,op,off,dn) for c,op,off,dn in self.xref_to.get(sig,[])))
    def callees(self,sig): return sorted(set((c,op,off,dn) for c,op,off,dn in self.xref_from.get(sig,[])))

if __name__=='__main__':
    import time
    t=time.time(); a=M06(); print('loaded in %.1fs dex=%d classes=%d methods=%d xrefs=%d'%(time.time()-t,len(a.dex),len(a.classes),len(a.methods),len(a.xref_to)),file=sys.stderr)
