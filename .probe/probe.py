"""A three-shot mini film, built entirely through the MCP server.

The only input is a tiny "screenplay". Everything after that is the agent's job:
animate a still, take its last frame, animate that (so the shots are chained),
join them with a crossfade, burn subtitles, verify the result.

This is the same loop an agent would run for a real script — just shorter.
"""
import json, os, subprocess, sys, pathlib

ROOT = pathlib.Path(".").resolve()
OUT = ROOT / "probe_out"
OUT.mkdir(exist_ok=True)
LOG = []
def p(*a):
    s = " ".join(str(x) for x in a); print(s, flush=True); LOG.append(s)

SCREENPLAY = """
SCENE 1 — INT. WORKSHOP — NIGHT
   A watchmaker lifts his head from the bench. Dust in a shaft of lamplight.
   He turns the tiny screw one last time.

SCENE 2 — SAME
   He looks up, straight into the lens. The lamp flickers once.

SCENE 3 — SAME
   He closes the case, stands, and the room goes dark.

VO: "Every second he saved cost him one of his own."
"""

SHOTS = [
    ("A watchmaker in a dim workshop lifts his head from the bench, dust drifting "
     "through a shaft of lamplight, slow cinematic push in", "shot1.mp4"),
    ("The same watchmaker now looks straight into the camera, the lamp behind him "
     "flickers once, subtle handheld drift", "shot2.mp4"),
    ("He closes a small watch case and the room slowly fades to darkness, "
     "camera holds still", "shot3.mp4"),
]


class MCP:
    """Minimal MCP client over stdio."""
    def __init__(self, script):
        self.p = subprocess.Popen([sys.executable, str(ROOT / "bridge/mivi_mcp.py")],
                                  stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                  stderr=subprocess.DEVNULL, text=True, bufsize=1)
        self.id = 0
        self.rpc("initialize", {"protocolVersion": "2024-11-05", "capabilities": {},
                                "clientInfo": {"name": "film-test", "version": "1"}})
        self.p.stdin.write('{"jsonrpc":"2.0","method":"notifications/initialized"}\n')
        self.p.stdin.flush()

    def rpc(self, method, params=None):
        self.id += 1
        self.p.stdin.write(json.dumps({"jsonrpc": "2.0", "id": self.id,
                                       "method": method, "params": params or {}}) + "\n")
        self.p.stdin.flush()
        d = json.loads(self.p.stdout.readline())
        if "error" in d:
            raise RuntimeError(d["error"])
        return d

    def call(self, name, **args):
        r = self.rpc("tools/call", {"name": name, "arguments": args})["result"]
        txt = r["content"][0]["text"]
        if r.get("isError"):
            raise RuntimeError(f"{name}: {txt}")
        return json.loads(txt)

    def close(self):
        self.p.terminate()


m = MCP("bridge/mivi_mcp.py")
try:
    p("[screenplay]", len([l for l in SCREENPLAY.strip().splitlines() if l.strip()]), "lines ->",
      len(SHOTS), "shots")

    # opening still: a real image from Mivi's CDN (stands in for the script's first frame)
    still = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
    clip_paths = []

    for i, (prompt, fname) in enumerate(SHOTS, 1):
        p(f"\n[shot {i}] prompt: {prompt[:70]}…")
        created = m.call("mivi_video", image=still, prompt=prompt, model="mivi-gx-720p")
        p(f"   task {created['task_id']}")
        done = m.call("mivi_video_wait", task_id=created["task_id"],
                      out=str(OUT / fname), timeout_s=300)
        if not done.get("video_url"):
            p("   FAILED", json.dumps(done)[:200]); break
        p(f"   ready -> {done.get('saved')}")
        clip_paths.append(done["saved"])

        # chain: the last frame of this shot is the first frame of the next
        lf = OUT / f"shot{i}_last.jpg"
        m.call("film_last_frame", video=done["saved"], out=str(lf))
        still = str(lf)
        p(f"   chained on {lf.name} ({lf.stat().st_size} bytes)")

    if len(clip_paths) < 2:
        raise SystemExit("not enough clips to assemble")

    p("\n[assemble] crossfade")
    final = OUT / "film.mp4"
    try:
        res = m.call("film_concat", clips=clip_paths, out=str(final), crossfade_s=0.4)
    except Exception as e:
        p("   xfade failed, plain concat:", str(e)[:120])
        res = m.call("film_concat", clips=clip_paths, out=str(final), crossfade_s=0)
    p("   ", json.dumps(res))

    srt = OUT / "vo.srt"
    srt.write_text("1\n00:00:00,400 --> 00:00:04,200\nEvery second he saved\n\n"
                   "2\n00:00:04,400 --> 00:00:08,000\ncost him one of his own.\n",
                   encoding="utf-8")
    subbed = OUT / "film_subbed.mp4"
    try:
        m.call("film_subtitle", video=str(final), srt=str(srt), out=str(subbed))
        p("[subtitles] burned")
    except Exception as e:
        p("[subtitles] skipped:", str(e)[:140])

    for f in (final, subbed):
        if f.exists():
            p("[probe]", f.name, json.dumps(m.call("film_probe", path=str(f))))
finally:
    m.close()
    (OUT / "out.txt").write_text("\n".join(LOG), encoding="utf-8")
