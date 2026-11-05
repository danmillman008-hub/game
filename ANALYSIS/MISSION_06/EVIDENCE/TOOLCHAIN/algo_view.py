import sys,re,pathlib
path=sys.argv[1]; key=sys.argv[2]; maxn=int(sys.argv[3]) if len(sys.argv)>3 else 400
p=pathlib.Path(path); blocks={};cur=None
for l in p.read_text().split('\n'):
    if l.startswith('===== '): cur=l.strip('= ');blocks[cur]=[]
    elif cur is not None: blocks[cur].append(l)
k=[x for x in blocks if key in x]
if not k: print('MISSING',key);sys.exit()
print('########',k[0])
KEEP=re.compile(r'\b(invoke|if-|iget|iput|sget|sput|const-string|const/4 v[0-4],|const/high16|const/16|new-instance|move-result|return|add-int|sub-int|and-int|or-int|xor-int|cmp|aget|aput|check-cast|instance-of|goto|move-object|move v|array-length|filled-new-array)\b')
n=0
for l in blocks[k[0]]:
    if 'fill-array-data-payload' in l: break
    if l.startswith('  ') and not KEEP.search(l): continue
    print(l[:215]);n+=1
    if n>maxn: print('...[truncated]');break
