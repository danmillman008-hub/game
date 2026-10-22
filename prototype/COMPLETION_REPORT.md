# Completion report — Stage 3: *Neon Alley*

**Deliverable:** a small, original, playable 2.5D beat-'em-up built on the verified behaviour
recovered in Stage 2. Source, tests, tools, recorded data and screenshots are in `prototype/`.

**Headline numbers** (all reproduced by commands in §6):

| measurement | result |
| --- | --- |
| Prototype integration tests | **52 passed, 0 failed, 0 errors, 0 skipped** |
| Original Stage-2 verification, re-run unchanged | **37 passed, 0 failed**, 7,740 ROM differential comparisons |
| ROM forensics, re-run unchanged | 11 ROMs verified, Kosinski cross-check OK |
| Deterministic recorded encounter | **VICTORY** at frame 875, 3/3 knockouts, 56/80 health, first damage at frame 208 |
| Same simulation with no input | **DEFEAT** at frame 1025 |
| Recorded-input replay | replay matches recording exactly (`True`) |
| Verified-component calls on the drawn path (875 frames) | `integrate` 1,775 · `build_boxes` 2,298 · `aabb` 1,165 · `gravity` 28 · `clamp` 28 · `air_control` 16 · `project` 6,984 |
| Throughput (simulation + draw + 3× upscale, headless) | ≈ 400 FPS; draw alone ≈ 1,960 FPS (target 60) |
| Game code | 1,542 lines across 7 modules; 859 lines of tests (incl. package init); 1 dependency (pygame 2.6.1) |

---

## 1. Scope statement — read this before quoting anything

This is **a new game**. It is not *Streets of Rage*, not a remake, not a port, not a level
reconstruction. Its characters, arena, art, effects, HUD, enemy behaviour, attack frame data,
health values, waves and hit reactions were all written for this prototype and are tagged
`[PROTO]`.

What it genuinely reuses is the **verified behavioural layer** from Stage 2 — fixed-point
conventions, the gravity/air-control/clamp/integration chain, the ROM-derived body boxes, the
AABB predicate, the projection and the cull test — and it calls them from its real update,
collision and render paths, not from a side channel. `ARCHITECTURE.md` lists every call site,
and the tests monkey-patch the component functions to prove the calls are live.

Nothing here was promoted into the original game's specifications. `BEHAVIORAL_SPECIFICATIONS/`,
`EVIDENCE_DATABASE.md`, the ROMs and the Stage-2 evidence files are untouched
(`git status` shows only `prototype/` as new).

## 2. Acceptance criteria

The brief's criteria, restated, each with the evidence that decides it.

| # | Criterion | Result | Evidence |
| --- | --- | --- | --- |
| 1 | One playable character with a readable state set (idle, walk, jump, attack, hurt, down) | **PASS** | `render.py::_pose` + `screenshots/02,03,04,05,08`; `test_draw_every_state_without_error` |
| 2 | One compact neon night arena, with **horizontal and depth-lane** movement | **PASS** | `config.py` arena `X 48…1360`, `Z 20…170`; `test_walks_right_and_left`, `test_depth_movement_is_smaller_than_horizontal`, `test_arena_bounds_hold` |
| 3 | Three enemies, wave/encounter structure | **PASS** | `config.WAVES` = 2 thugs → 1 brute; `test_start_spawns_first_wave`, `test_second_wave_spawns_after_first_is_cleared`; `screenshots/02,06` |
| 4 | Jump with **air control**, and ground-plane collision | **PASS** | `test_jump_leaves_ground_and_lands` (apex −35 px, 17 air frames, lands, `vy=0`), `test_air_control_changes_horizontal_speed`, `test_no_double_jump`; screenshot `03_jump.png` |
| 5 | Depth-aware render ordering | **PASS** | `render.py::_draw_actors` sorts by `(Z, Y, id)`; `test_depth_order_far_to_near` asserts the actual draw order is `[40, 75, 120]` |
| 6 | Responsive combat: punch, kick with longer recovery, startup/active/recovery, direction + depth checks, per-attack hit tracking, damage, hitstun, knockback, i-frames, on-hit visual | **PASS** | `test_valid_punch_lands`, `test_kick_lands_and_hits_harder`, `test_out_of_range_punch_misses`, `test_wrong_depth_punch_misses`, `test_punching_away_from_the_enemy_misses`, `test_one_attack_deals_damage_once`, `test_hitstun_and_iframes`, `test_player_attack_cooldown_blocks_spam`; screenshots `04,05` |
| 7 | Deterministic enemy AI: approach, lane adjust, attack, take damage, die, never stuck at bounds | **PASS** | `game.py::_update_enemy`; `test_enemies_never_stick_to_bounds` (1,200 frames in a corner, bounds hold, player still gets hit); no RNG in the codebase |
| 8 | Health/damage/defeat/victory, restart, title/start screen, on-screen control guide, HUD | **PASS** | `test_player_can_be_defeated` (DEFEAT), `test_autopilot_reaches_victory` (VICTORY), `test_restart_returns_to_a_clean_run`, `test_title_does_not_simulate`; controls on the title card and in the HUD strip; screenshots `01,07,08` |
| 9 | Ground shadows that stay grounded during a jump, impact effects, procedural art | **PASS** | `test_shadow_stays_on_the_ground_during_a_jump` (shadow `sy` identical airborne, body `sy` lower/above); spark/ring/dust/KO/popup effects; screenshot `03_jump.png` shows the body airborne over a grounded shadow |
| 10 | 60 FPS target and responsive scaling | **PASS** | fixed 1/60 s step with an accumulator, `clock.tick(60)`; ≈400 FPS sim+draw; `test_window_scales_without_changing_the_canvas` at 640×400, 1280×720, 1920×1080 |
| 11 | **Demonstrable reuse**: fixed-point, gravity/vertical velocity, air control, velocity limits, integration + freeze predicate, ROM body boxes, AABB collision, projection and culling all called by the real paths; attack hitboxes distinct from body boxes | **PASS** | `ARCHITECTURE.md` §1 call-site table; `test_import_identity` (`assertIs`), `test_patching_integrate_breaks_the_game`, `test_patching_projection_breaks_rendering`, `test_update_path_calls_every_component`, `test_frozen_actor_is_not_integrated_and_does_not_land`, `test_body_box_values_are_rom_table_outputs`, `test_attack_box_differs_from_body_boxes`; `tools/measure_components.py` |
| 12 | Testing: original verification re-run, full existing suite, integration tests for every listed scenario, headless smoke test, deterministic scripted encounter with a reported result, nothing weakened | **PASS** | §3 and §6; `TEST_REPORT.md`; `data/scripted_run.json` |
| 13 | Deliverables: runnable source, original assets, README with exact install/launch commands, controls guide, architecture doc naming every reused component + call path, prototype-rules list, test report with real output, screenshots, completion report with limitations | **PASS** | `README.md`, `ARCHITECTURE.md`, `RULES.md`, `TEST_REPORT.md`, `COMPLETION_REPORT.md` (this file), `screenshots/` (8 images), `data/` |

No criterion is FAIL. No criterion is BLOCKED: every one of them is exercised by a command
that ran in this workspace and whose output is quoted below or stored in `TEST_REPORT.md`.

Two honest qualifiers on criterion 11, because "reuse" is where a prototype can quietly cheat:

- **`soft_gravity` (`$0038A6`) is not exercised.** The component implements it and Stage 2
  verified it, but this game has no throw/arc state that should use it (`U-GRAV-01` is still
  open). Rather than route an arbitrary actor through it to inflate a counter, it is unused
  and reported as unused.
- **The freeze predicate is called inside `integrate`**, not separately, and the game consumes
  `integrate`'s return value so a frozen frame is never read as a landing. That is the real
  call path; the test sets the engine's actual freeze state to prove it.

## 3. Test evidence (real output)

```
$ SDL_VIDEODRIVER=dummy .venv/bin/python -m prototype.tools.run_tests
...
Ran 52 tests in 2.2 s
OK
52 passed, 0 failed, 0 errors, 0 skipped

$ /tmp/re_venv/bin/python tools/verify_stage2.py
Ran 37 tests in 6.919s
OK
tests: 37 passed, 0 failed, 0 errors, 0 skipped
differential comparisons vs original ROM code: 7740

$ /tmp/re_venv/bin/python tools/verify_sor_forensics.py
Verified 11 ROMs -> /home/user/game/evidence/verification_results.json
Z80 Driver Kosinski cross-check (Py == M68000 Unicorn): OK (07cabd01…fd2)
```

The Stage-2 suite numbers are identical to the pre-existing baseline (37 / 7,740 / 11 ROMs,
ROM `dd44f120…95c0`, 524,288 bytes). No test was weakened, skipped, re-baselined or deleted,
and no evidence file was edited.

### The deterministic scripted encounter

`prototype/data/scripted_run.json` holds 875 frames of recorded input (one `Command` per
frame). It is replayed from a fresh game:

```
$ SDL_VIDEODRIVER=dummy .venv/bin/python -m prototype.tools.record_encounter
recorded 875 command frames -> prototype/data/scripted_run.json
recorded run : {"component_calls": {"aabb": 1165, "air_control": 16, "build_boxes": 2298,
                "clamp": 28, "gravity": 28, "integrate": 1775, "project": 0},
                "first_frame_without_hp": 208, "frames": 875, "kills": 3,
                "player_hp": 56, "player_position": [886, 25], "state": "victory",
                "total_enemies": 3}
replayed run : {"frame": 875, "kills": 3, "player_hp": 56,
                "player_position": [886, 25], "state": "victory"}
replay matches recording: True
```

The opposite ending is reachable from the same simulation with no input at all:

```
[passive encounter] state=defeat frames=1025 hp=0
```

### Component call counts

```
$ SDL_VIDEODRIVER=dummy .venv/bin/python -m prototype.tools.measure_components
path                                      integrate  build_boxes    aabb   gravity  clamp  air_control  project
simulation only (875 frames)                   1775         2298    1165        28     28           16        0
simulation + rendering (875 frames)            1775         2298    1165        28     28           16     6984
jump script + rendering (90 frames)             234          546     276        38     38           38      840
never called on the drawn path: none
```

## 4. What it plays like

- Close the distance with `A`/`D` — the arena is 1,312 px wide, ~2.25 px per frame.
- Line up in the right lane with `W`/`S` — a punch only reaches 22 px of depth, a kick 26.
- `J` is safe and fast (7 damage, 13 frames); `K` hits for 13 but commits you for 29 frames.
- Enemies telegraph for 16 frames with an amber spark at the shoulder — that is your window to
  step out of the lane, walk out of range, or jump.
- They cannot be interrupted mid-swing (armour), so trading punches is a losing plan: measured
  over a recorded run, a passive player loses at frame 1,025 while the demo pilot finishes with
  56/80 health.

## 5. Limitations

1. **One arena, one player, three enemies.** Deliberately small: the brief asked for a compact
   prototype, not a game.
2. **No audio.** No sound effects or music, so nothing has to be shipped, licensed or
   downloaded.
3. **Keyboard only, single-player.** No gamepad, no remapping, no pause menu.
4. **Prototype combat rules are not ROM rules.** Hit reactions, hit-stop, armour, i-frames,
   health and attack frame data are new (`U-CBT-01` remains open). They are labelled `[PROTO]`
   everywhere.
5. **Enemy AI is intentionally simple**: approach → lane adjust → one attacker at a time →
   cooldown. No flanking, no blocking, no grabs, no juggles.
6. **`soft_gravity` unused** (see §2).
7. **Arena bounds are a hard clamp**, not the original's per-round bands; the original's band
   logic was not in the recovered slice.
8. **Visual style is procedural pixel art**, sized to the authentic projection scale. It is
   readable rather than elaborate: no sprite sheets, no tweened animation — poses are drawn
   per frame from a small pose set.
9. **pygame is a new dependency** for this repository (Stage 2 needed none). It installs
   offline afterwards, but the first install needs the network. Headless runs need
   `SDL_VIDEODRIVER=dummy`.
10. **Scaling is a single blit** (`smoothscale`), not a letterboxed integer-only scaler; at odd
    window sizes a few pixels of shimmer are possible.
11. **The pipeline was verified headless.** All screenshots and measurements come from SDL's
    dummy driver; the interactive window and audio path were exercised through the same code
    but not on a physical display in this environment.

## 6. Reproduce everything from a clean checkout

```bash
cd <repository>
python3 -m venv .venv && .venv/bin/pip install pygame

# 1. the original verification, unchanged
/tmp/re_venv/bin/python tools/verify_stage2.py            # 37 passed, 7,740 comparisons
/tmp/re_venv/bin/python tools/verify_sor_forensics.py     # 11 ROMs

# 2. the prototype's integration suite (regenerates TEST_REPORT.md)
SDL_VIDEODRIVER=dummy .venv/bin/python -m prototype.tools.run_tests

# 3. the deterministic encounter (re-records data/scripted_run.json)
SDL_VIDEODRIVER=dummy .venv/bin/python -m prototype.tools.record_encounter

# 4. component call counts
SDL_VIDEODRIVER=dummy .venv/bin/python -m prototype.tools.measure_components

# 5. screenshots
SDL_VIDEODRIVER=dummy .venv/bin/python -m prototype.tools.capture_screens

# 6. play it
.venv/bin/python -m prototype.neon_alley
```

## 7. Screenshots

| file | shows |
| --- | --- |
| `screenshots/01_title.png` | title card, control guide, animated prompt |
| `screenshots/02_street.png` | the arena: skyline, neon signs, depth lanes, HUD |
| `screenshots/03_jump.png` | airborne body, shadow still on the ground, ground marker |
| `screenshots/04_punch_hit.png` | punch connecting: spark, ring, damage number, hit-stop |
| `screenshots/05_kick.png` | kick connecting for 13 |
| `screenshots/06_wave2.png` | wave 2: the brute closing in, depth separation visible |
| `screenshots/07_victory.png` | `AREA CLEARED`, 3/3 knockouts |
| `screenshots/08_defeat.png` | `YOU ARE DOWN` |

## 8. What changed in the repository

New, and nothing else:

```
prototype/__init__.py
prototype/neon_alley/{__init__,__main__,config,adapter,entities,game,render,autopilot,main}.py
prototype/tests/{__init__,support,test_components,test_movement,test_combat,test_flow,
                 test_render,test_scripted_encounter,test_smoke}.py
prototype/tools/{__init__,run_tests,record_encounter,measure_components,capture_screens}.py
prototype/data/scripted_run.json
prototype/screenshots/*.png
prototype/{README,ARCHITECTURE,RULES,COMPLETION_REPORT,TEST_REPORT}.md
```

`RESEARCH_LOG.md` gets one appended Stage-3 entry that points here and states explicitly that
nothing in the prototype is evidence about the original game. No existing file was modified.
