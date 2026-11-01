# Mission 5 — Unified System Graph

## Scope
One dependency graph spanning UI, view models, grading, parser, repositories, persistence,
network, analytics, native and remote config — as an editable artifact (JSON + Mermaid + DOT).

## Sources
`evidence/API_CATALOG_V2.csv`, `evidence/DTO_CATALOG.csv`, and the class/method reads cited in the
per-domain documents of this mission.

## Method
Nodes were admitted only if a class/method/endpoint was read this mission; edges carry their own
evidence label inside `system_graph.json`. Inference-only edges are kept and marked, never merged
into verified ones.

## Findings
- 34 nodes, 28 edges.
- Verified edges: 22 of 28.
- The lesson engine is a *fan-in* structure: four per-type view models converge on one base class,
  and the base class is the only writer of progress and the only emitter of lesson analytics.
- The parser (`te/*`) sits entirely outside `com.getmimo` — the single most consequential structural
  fact of this mission, because it is why the first decompilation pass missed it.

## Mermaid
```mermaid
graph TD
  ui_lesson["ui.lesson"] -->|binds| vm_base["vm.base"]
  vm_base["vm.base"] -->|specialised-by| vm_fillthegap["vm.fillthegap"]
  vm_base["vm.base"] -->|specialised-by| vm_selection["vm.selection"]
  vm_base["vm.base"] -->|specialised-by| vm_spell["vm.spell"]
  vm_base["vm.base"] -->|specialised-by| vm_validated["vm.validated"]
  vm_validated["vm.validated"] -->|produces| grade_verdict["grade.verdict"]
  grade_verdict["grade.verdict"] -->|uses| grade_normalizer["grade.normalizer"]
  parser_tie["parser.tie"] -->|constructs| model_ast["model.ast"]
  content_repo["content.repo"] -->|feeds| parser_tie["parser.tie"]
  vm_base["vm.base"] -->|writes-progress| prog_repo["prog.repo"]
  prog_repo["prog.repo"] -->|uses| db_room["db.room"]
  db_room["db.room"] -->|contains| db_lp["db.lp"]
  db_room["db.room"] -->|contains| db_cc["db.cc"]
  db_room["db.room"] -->|contains| db_tc["db.tc"]
  prog_repo["prog.repo"] -->|enqueues| prog_queue["prog.queue"]
  prog_queue["prog.queue"] -->|posts| api_progress["api.progress"]
  prog_queue["prog.queue"] -->|deletes-after-ack| db_lp["db.lp"]
  vm_base["vm.base"] -->|emits| analytics_facade["analytics.facade"]
  analytics_facade["analytics.facade"] -->|forwards| analytics_firebase["analytics.firebase"]
  analytics_facade["analytics.facade"] -->|forwards| analytics_adjust["analytics.adjust"]
  aitutor_repo["aitutor.repo"] -->|posts| api_aitutor_post["api.aitutor.post"]
  aitutor_repo["aitutor.repo"] -->|queries-quota| api_aitutor_count["api.aitutor.count"]
  api_package["api.package"] -->|delivers-packs| content_repo["content.repo"]
  api_code_run["api.code.run"] -->|exec-verdict| vm_base["vm.base"]
  native_rive["native.rive"] -->|renders-animation| ui_lesson["ui.lesson"]
  native_signer["native.signer"] -->|signs-requests| analytics_adjust["analytics.adjust"]
  native_yrf["native.yrf"] -->|blocking-dialog| ui_lesson["ui.lesson"]
  rc_clientconfig["rc.clientconfig"] -->|gates-events| analytics_facade["analytics.facade"]
```

## DOT
```dot
digraph mimo_lesson {
  "ui.lesson" -> "vm.base" [label="binds"];
  "vm.base" -> "vm.fillthegap" [label="specialised-by"];
  "vm.base" -> "vm.selection" [label="specialised-by"];
  "vm.base" -> "vm.spell" [label="specialised-by"];
  "vm.base" -> "vm.validated" [label="specialised-by"];
  "vm.validated" -> "grade.verdict" [label="produces"];
  "grade.verdict" -> "grade.normalizer" [label="uses"];
  "parser.tie" -> "model.ast" [label="constructs"];
  "content.repo" -> "parser.tie" [label="feeds"];
  "vm.base" -> "prog.repo" [label="writes-progress"];
  "prog.repo" -> "db.room" [label="uses"];
  "db.room" -> "db.lp" [label="contains"];
  "db.room" -> "db.cc" [label="contains"];
  "db.room" -> "db.tc" [label="contains"];
  "prog.repo" -> "prog.queue" [label="enqueues"];
  "prog.queue" -> "api.progress" [label="posts"];
  "prog.queue" -> "db.lp" [label="deletes-after-ack"];
  "vm.base" -> "analytics.facade" [label="emits"];
  "analytics.facade" -> "analytics.firebase" [label="forwards"];
  "analytics.facade" -> "analytics.adjust" [label="forwards"];
  "aitutor.repo" -> "api.aitutor.post" [label="posts"];
  "aitutor.repo" -> "api.aitutor.count" [label="queries-quota"];
  "api.package" -> "content.repo" [label="delivers-packs"];
  "api.code.run" -> "vm.base" [label="exec-verdict"];
  "native.rive" -> "ui.lesson" [label="renders-animation"];
  "native.signer" -> "analytics.adjust" [label="signs-requests"];
  "native.yrf" -> "ui.lesson" [label="blocking-dialog"];
  "rc.clientconfig" -> "analytics.facade" [label="gates-events"];
}
```

## Evidence labels
Node existence: **VERIFIED_STATIC** unless the node id ends in a documented inference. Edge labels are
per-edge in the JSON.

## Limitations
This is a *lesson-and-progress* centred graph; auth, subscription purchase flow and the full UI
navigation graph are not included (see `22_FINAL_AUDIT/` for their status).

## Reproduction
`python3 -c "import json;d=json.load(open('18_SYSTEM_GRAPH/system_graph.json'));print(len(d['nodes']),len(d['edges']))"`

## Unresolved
`U-26` the graph omits auth, purchase flow and navigation; edges marked INFERRED were not promoted.
