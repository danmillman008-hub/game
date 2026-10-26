#!/usr/bin/env python3
"""End-to-end test of serve.py against a local mock face-api server."""
import json
import threading
import urllib.request
import urllib.error
from http.server import HTTPServer, BaseHTTPRequestHandler

import serve

# allow localhost mock through the proxy allow-list
serve.ALLOWED_SUFFIXES = ("localhost", "127.0.0.1")


class MockUpstream(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass

    def _send(self, code, payload, ctype="application/json"):
        body = json.dumps(payload).encode() if isinstance(payload, dict) else payload
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(n)
        assert self.headers.get("sign"), "sign header missing"
        assert self.headers.get("timeStamp"), "timeStamp missing"
        if self.path.startswith("/algo/v1/aiGenerate-aigc/multipleUpload"):
            assert self.headers.get("ifHttps") == "true"
            assert self.headers.get("sign")  # md5(signKey+ts)
            assert b"name=\"files\"" in raw, "multipart field must be 'files'"
            self._send(200, {"c": 200, "m": "ok", "d": ["https://cdn/x.jpg"]})
        elif self.path.endswith("image2video/unifiedTaskCreate"):
            assert self.headers.get("userId"), "g.l uses capital 'userId'"
            assert "ifWise" not in self.headers
            body = json.loads(raw)
            assert body["imageUrls"] == ["https://cdn/x.jpg"]
            assert body["level"] == 1 and body["example"] == ""
            self._send(200, {"c": 200, "m": "ok",
                             "d": {"taskId": "T-1", "taskStatus": "queued"}})
        elif self.path.endswith("image2video/queryTask"):
            assert self.headers.get("userid"), "g.k uses lowercase 'userid'"
            assert self.headers.get("ifWise") == "true"
            assert json.loads(raw) == {"taskId": "T-1"}
            self._send(200, {"c": 200, "m": "ok", "d": {
                "taskId": "T-1", "taskStatus": "success",
                "videoUrl": "http://127.0.0.1:%d/v.mp4" % MOCK_PORT}})
        else:
            self._send(404, {"c": 404, "m": "unknown"})

    def do_GET(self):
        if self.path == "/v.mp4":
            self._send(200, b"FAKEMP4DATA", "video/mp4")
        else:
            self._send(404, b"nf")


def free_port():
    s = HTTPServer(("127.0.0.1", 0), BaseHTTPRequestHandler)
    p = s.server_address[1]
    s.server_close()
    return p


MOCK_PORT = free_port()
PROXY_PORT = free_port()
mock = HTTPServer(("127.0.0.1", MOCK_PORT), MockUpstream)
proxy = HTTPServer(("127.0.0.1", PROXY_PORT), serve.Handler)
threading.Thread(target=mock.serve_forever, daemon=True).start()
threading.Thread(target=proxy.serve_forever, daemon=True).start()

base = f"http://127.0.0.1:{PROXY_PORT}"
# 1) HTML
r = urllib.request.urlopen(base + "/")
assert b"Mivi AI" in r.read() and r.status == 200
print("OK  GET / serves html")

# 2) preflight
req = urllib.request.Request(base + "/proxy?u=x", method="OPTIONS")
r = urllib.request.urlopen(req)
assert r.status == 204 and r.headers.get("Access-Control-Allow-Origin") == "*"
print("OK  OPTIONS preflight 204 + CORS")

# 3) upload through proxy
boundary = "----test"
mp = (f"--{boundary}\r\nContent-Disposition: form-data; name=\"files\"; "
      f"filename=\"a.jpg\"\r\nContent-Type: image/jpg\r\n\r\nJPEG\r\n"
      f"--{boundary}--\r\n").encode()
req = urllib.request.Request(
    base + "/proxy?u=" + urllib.parse.quote(
        f"http://127.0.0.1:{MOCK_PORT}/algo/v1/aiGenerate-aigc/multipleUpload"),
    data=mp, method="POST",
    headers={"Content-Type": f"multipart/form-data; boundary={boundary}",
             "cp": "instagram.story.art.collage", "version": "407",
             "platform": "1", "sign": "x", "timeStamp": "1",
             "userId": "u", "ifHttps": "true"})
up = json.loads(urllib.request.urlopen(req).read())
assert up["d"] == ["https://cdn/x.jpg"]
print("OK  proxy upload ->", up["d"][0])

# 4) create
req = urllib.request.Request(
    base + "/proxy?u=" + urllib.parse.quote(
        f"http://127.0.0.1:{MOCK_PORT}/algo/v1/faceFusion/aigc/image2video/unifiedTaskCreate"),
    data=json.dumps({"imageUrls": ["https://cdn/x.jpg"], "level": 1,
                     "deviceToken": "", "example": ""}).encode(),
    method="POST", headers={"Content-Type": "application/json",
                            "userId": "u", "sign": "x", "timeStamp": "1",
                            "cp": "c", "version": "407", "platform": "1"})
cr = json.loads(urllib.request.urlopen(req).read())
assert cr["d"]["taskId"] == "T-1"
print("OK  proxy create task ->", cr["d"]["taskId"])

# 5) query
req = urllib.request.Request(
    base + "/proxy?u=" + urllib.parse.quote(
        f"http://127.0.0.1:{MOCK_PORT}/algo/v1/faceFusion/aigc/image2video/queryTask"),
    data=json.dumps({"taskId": "T-1"}).encode(), method="POST",
    headers={"Content-Type": "application/json", "userid": "u",
             "sign": "x", "timeStamp": "1", "cp": "c", "version": "407",
             "platform": "1", "ifWise": "true"})
qr = json.loads(urllib.request.urlopen(req).read())
assert qr["d"]["taskStatus"] == "success"
print("OK  proxy query ->", qr["d"]["taskStatus"])

# 6) video bytes through proxy
r = urllib.request.urlopen(
    base + "/proxy?u=" + urllib.parse.quote(qr["d"]["videoUrl"]))
assert r.read() == b"FAKEMP4DATA" and r.headers["Content-Type"] == "video/mp4"
print("OK  proxy video passthrough (video/mp4)")

# 7) allow-list enforcement
try:
    urllib.request.urlopen(
        base + "/proxy?u=" + urllib.parse.quote("http://evil.example.com/x"))
    raise SystemExit("allow-list not enforced")
except urllib.error.HTTPError as e:
    assert e.code == 403
    print("OK  non-allowlisted host blocked (403)")

mock.shutdown(); proxy.shutdown()
print("\nALL SERVE.PY TESTS PASSED")
