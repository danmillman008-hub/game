import sys,re,pathlib
sys.path.insert(0,'/home/user/_work/m06')
from m06_dex import M06
a=M06()
SEL=[
 ('Lkm/f;','b('),('Lkm/f;','d('),
 ('Lcom/getmimo/data/source/remote/progress/LessonProgressQueue;','storeLessonProgress('),
 ('Lcom/getmimo/data/source/remote/progress/LessonProgressQueue;','updateCorrectAnswersCount('),
 ('Lcom/getmimo/data/source/remote/progress/LessonProgressQueue;','getCorrectLessonProgressCount('),
 ('Lcom/getmimo/data/source/remote/progress/LessonProgressQueue;','getCorrectLessonsFirstTryCount('),
 ('Lcom/getmimo/data/source/remote/progress/LessonProgressQueue;','storeAndPostAllLessonProgress('),
 ('Lcom/getmimo/data/source/local/completion/a;','b('),
 ('Lcom/getmimo/interactors/path/d;','a('),
 ('Lcom/getmimo/interactors/chapter/a;','a('),
 ('Lcom/getmimo/network/a;','a('),('Lcom/getmimo/network/a;','b('),
 ('Lcom/getmimo/ui/lesson/executable/q;','I('),('Lcom/getmimo/ui/lesson/executable/q;','E('),
 ('Lcom/getmimo/ui/chapter/chapterendview/main/f;','G('),
 ('Lcom/getmimo/ui/chapter/chapterendview/main/f;','F('),
 ('Lcom/getmimo/data/content/tracks/c;','d('),('Lcom/getmimo/data/content/tracks/c;','g('),('Lcom/getmimo/data/content/tracks/c;','i('),
 ('Lcom/getmimo/data/content/tracks/b;','a('),
 ('Lcom/getmimo/data/content/model/track/ContentLocale;','<clinit>'),
 ('Lye/f;',None),
]
out=pathlib.Path('/home/user/_work/m06/digest.txt');f=out.open('w')
def emit(s):
    inf=a.info(s)
    f.write('\n######## %s\ndex=%s code_offset=%s insns=%d callers=%d callees=%d\n'%(
        s,inf['dex'],inf['code_offset'],inf['instructions'],len(a.callers(s)),len(a.callees(s))))
    for l in a.disasm(s):
        if re.search(r'\b(invoke|if-|iget|iput|sget|sput|const-string|const/4 v[0-4],|const/16 v[0-4],|new-instance|move-result|return|check-cast|instance-of|goto|add-int|xor-int|and-int|cmp|const/high16)\b',l):
            f.write('  '+l[:220]+'\n')
for cn,meth in SEL:
    ms=sorted(a.methods_of(cn))
    if meth is None:
        f.write('\n========== CLASS %s methods:'%cn)
        for s in ms: f.write('\n  '+s)
        f.write('\n')
        continue
    for s in ms:
        if '->'+meth in s: emit(s)
f.close();print(out,out.stat().st_size)
