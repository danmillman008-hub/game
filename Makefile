# Makefile — the four verbs you actually say out loud.
#
#   make verify                # is the repo healthy? (writes REPO_STATUS.md)
#   make check                 # everything that must pass before a batch
#   make plan SCENE=...        # scene file -> job file (+ estimate, + lint)
#   make shot JOBS=...         # housecheck -> dry-run -> dispatch (refuses a bad shot)
#   make dry JOBS=...          # show the DAG and the wall-clock guess
#   make film NAME=anime_ten   # assemble the cut
#
# Dispatch is a git push: the workflows read the trigger files at the repo root.

PY      ?= python3
SCENE   ?= studio/motions/scenes/gate.json
JOBS    ?= films/short16/gen_jobs_gate.json
OUT     ?= films/short16/clips_gen
NAME    ?= anime_ten
PAR     ?= 4

.PHONY: help verify check plan dry gen audit film wiring clean trig shot style light

help:
	@grep -E '^#   ' Makefile

verify:
	$(PY) studio/verify.py            # inventory, data, triggers, compile, smoke
	@echo "verify: report -> REPO_STATUS.md"

# `check` is the pre-batch gate: verify already compiles everything, checks every
# reference and runs every test, so it is not repeated here.
check:
	$(MAKE) --no-print-directory verify
	$(PY) studio/knowledge/bank.py check
	$(PY) studio/knowledge/banktest.py

plan:
	$(PY) studio/shotplan.py plan $(SCENE) --out $(JOBS) --parallel $(PAR)

dry:
	$(PY) studio/mivi_shot.py $(JOBS) --out $(OUT) --dry-run --parallel $(PAR)

audit:
	$(PY) studio/mivi_shot.py $(JOBS) --out $(OUT) --dry-run --parallel $(PAR) 2>&1 | grep -c WARN || true

style:
	@echo "studio/knowledge/method/HOUSE_STYLE.md"

# Every generated clip loses light across its four seconds (54 % on one take), so four
# clips cut together pump. This measures it and normalises before the edit, not after.
light:
	$(PY) studio/lumatch.py measure $(CLIPS)

# The gate that stopped costing us takes: a shot that breaks the house style never
# reaches the provider, because housecheck exits non-zero first.
# The trigger's FIRST line is what mivi.yml reads. The second line is a stamp: the
# workflow is triggered by a change to this file, so dispatching the same job file
# twice needs the file to differ (on 2026-10-31 a corrected batch silently did not
# run because only this file's *content* mattered and it had not changed).
shot:
	$(PY) studio/housecheck.py $(JOBS)
	$(PY) studio/mivi_shot.py $(JOBS) --out $(OUT) --dry-run --parallel $(PAR)
	@printf '%s\n# dispatched %s\n' "$(JOBS)" "$$(date -u +%Y-%m-%dT%H:%M:%SZ)" > .mivi-trigger
	@echo "trigger written — git add .mivi-trigger && commit && push"

gen:
	@printf '%s\n# dispatched %s\n' "$(JOBS)" "$$(date -u +%Y-%m-%dT%H:%M:%SZ)" > .mivi-trigger
	@echo "trigger written — now: git add .mivi-trigger && git commit && git push"

film:
	$(PY) studio/filmkit.py assemble $(NAME) --crossfade 0.2

trig:
	@ls -1 .*-trigger 2>/dev/null | while read f; do printf '%-20s %s\n' "$$f" "$$(head -1 $$f)"; done

wiring:
	$(PY) studio/tests/test_mivi_shot.py   # offline: scheduler, chain, report flags

clean:
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
