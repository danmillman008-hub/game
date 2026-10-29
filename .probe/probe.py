import json, hashlib, time, urllib.request, urllib.error, sys

HOST="https://cpi.ufotosoft.com"
USER="7da75eed37c61d33"
IMG="http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"

def headers():
    t=str(int(time.time()))
    return {"userid":USER,"timeStamp":t,"cp":"instagram.story.art.collage",
            "version":"407","platform":"1","ifWise":"true",
            "Content-Type":"application/json",
            "sign":hashlib.md5(("m3snil"+t).encode()).hexdigest()}

def call(method,path,body=None,host=HOST):
    url=host+path
    data=json.dumps(body).encode() if body is not None else (b"{}" if method=="POST" else None)
    req=urllib.request.Request(url,data=data,headers=headers(),method=method)
    try:
        with urllib.request.urlopen(req,timeout=45) as r:
            return r.status, r.read().decode("utf-8","replace")[:600]
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8","replace")[:600]
    except Exception as e:
        return 0, "ERR "+str(e)

def show(tag,res):
    print(f"[{tag}] HTTP {res[0]} :: {res[1]}")

print("=== hello from the runner ===")
show("pose POST", call("POST","/algo/v1/faceFusion/aigc/getAllPoseSequenceId",{}))
show("pose GET",  call("GET", "/algo/v1/faceFusion/aigc/getAllPoseSequenceId"))
show("pose GET q",call("GET", "/algo/v1/faceFusion/aigc/getAllPoseSequenceId?userid="+USER))
