import sys,struct,json

class Dex:
    def __init__(s,buf):
        s.b=buf
        assert buf[:3]==b'dex'
        s.string_ids_size, s.string_ids_off = struct.unpack_from('<II',buf,0x38)
        s.type_ids_size, s.type_ids_off     = struct.unpack_from('<II',buf,0x40)
        s.proto_ids_size,s.proto_ids_off    = struct.unpack_from('<II',buf,0x48)
        s.field_ids_size,s.field_ids_off    = struct.unpack_from('<II',buf,0x50)
        s.method_ids_size,s.method_ids_off  = struct.unpack_from('<II',buf,0x58)
        s.class_defs_size,s.class_defs_off  = struct.unpack_from('<II',buf,0x60)
        s._str={}
    def uleb(s,off):
        r=0;sh=0
        while True:
            b=s.b[off];off+=1
            r|=(b&0x7f)<<sh
            if not b&0x80: break
            sh+=7
        return r,off
    def string(s,i):
        if i in s._str: return s._str[i]
        o=struct.unpack_from('<I',s.b,s.string_ids_off+4*i)[0]
        n,o=s.uleb(o)
        # utf16 length then MUTF8 bytes
        end=s.b.index(b'\x00',o)
        v=s.b[o:end].decode('utf-8','replace')
        s._str[i]=v; return v
    def type_name(s,i):
        idx=struct.unpack_from('<I',s.b,s.type_ids_off+4*i)[0]
        return s.string(idx)
    def method_name(s,i):
        cls,proto,name=struct.unpack_from('<HHI',s.b,s.method_ids_off+8*i)
        return s.type_name(cls), s.string(name)
    def class_defs(s):
        for k in range(s.class_defs_size):
            o=s.class_defs_off+32*k
            cls,acc,sup,ifaces,src,ann,data,sv=struct.unpack_from('<IIIIIIII',s.b,o)
            yield dict(class_idx=cls,access=acc,annotations_off=ann,class_data_off=data,static_values_off=sv)
    def annvalue(s,off):
        h=s.b[off];off+=1
        vt=h&0x1f; arg=h>>5
        if vt==0x17:  # string
            idx,off=s.uleb(off); return s.string(idx),off
        if vt==0x18:  # type
            idx,off=s.uleb(off); return s.type_name(idx),off
        if vt==0x1b:  # enum
            tidx,off=s.uleb(off); nidx,off=s.uleb(off)
            return s.type_name(tidx)+'.'+s.string(nidx),off
        if vt==0x1c:  # array
            n,off=s.uleb(off); out=[]
            for _ in range(n):
                v,off=s.annvalue(off); out.append(v)
            return out,off
        if vt==0x1d:  # annotation
            return s.encoded_annotation(off)
        if vt==0x1e: return None,off
        if vt==0x1f: return bool(arg),off
        if vt in (0x00,0x02,0x03,0x04,0x06):
            size=arg+1; raw=s.b[off:off+size]; off+=size
            return int.from_bytes(raw,'little',signed=(vt not in (0x03,))),off
        size=arg+1; off+=size; return '<raw>',off
    def encoded_annotation(s,off):
        tidx,off=s.uleb(off); n,off=s.uleb(off)
        els={}
        for _ in range(n):
            nidx,off=s.uleb(off)
            v,off=s.annvalue(off)
            els[s.string(nidx)]=v
        return (s.type_name(tidx),els),off
    def annotation_set(s,off):
        n=struct.unpack_from('<I',s.b,off)[0]
        out=[]
        for k in range(n):
            aoff=struct.unpack_from('<I',s.b,off+4+4*k)[0]
            vis=s.b[aoff]
            ann,_=s.encoded_annotation(aoff+1)
            out.append(ann)
        return out
    def annotations_dir(s,off):
        cls_ann,fsz,msz,psz=struct.unpack_from('<IIII',s.b,off)
        p=off+16
        fields=[];methods=[];params=[]
        for _ in range(fsz):
            fi,ao=struct.unpack_from('<II',s.b,p);p+=8
            fields.append((fi,s.annotation_set(ao)))
        for _ in range(msz):
            mi,ao=struct.unpack_from('<II',s.b,p);p+=8
            methods.append((mi,s.annotation_set(ao)))
        for _ in range(psz):
            mi,ao=struct.unpack_from('<II',s.b,p);p+=8
            n=struct.unpack_from('<I',s.b,ao)[0]
            lst=[]
            for k in range(n):
                so=struct.unpack_from('<I',s.b,ao+4+4*k)[0]
                lst.append(s.annotation_set(so))
            params.append((mi,lst))
        return cls_ann,fields,methods,params

if __name__=='__main__':
    d=Dex(open(sys.argv[1],'rb').read())
    want=sys.argv[2] if len(sys.argv)>2 else None
    for cd in d.class_defs():
        cn=d.type_name(cd['class_idx'])
        if want and want not in cn: continue
        if not cd['annotations_off']: continue
        try: ca,f,m,p=d.annotations_dir(cd['annotations_off'])
        except Exception as e:
            print('ERR',cn,e); continue
        if not m and not p: continue
        print('='*90); print('CLASS',cn)
        for mi,anns in m:
            t,nm=d.method_name(mi)
            paths=[a for a in anns if any(k in a[0] for k in ('retrofit2/http/POST','retrofit2/http/GET','retrofit2/http/FormUrlEncoded','retrofit2/http/Multipart'))]
            if paths:
                print('  METHOD',nm,'->',[(a[0].split('/')[-1],a[1]) for a in paths])
        for mi,plist in p:
            t,nm=d.method_name(mi)
            names=[]
            for i,anns in enumerate(plist):
                for a in anns:
                    if 'retrofit2/http/' in a[0]:
                        names.append((i,a[0].split('/')[-1],a[1]))
            if names:
                print('  PARAMS',nm,'->',names)
