# Makefile — the four verbs you actually say out loud.
#
#   make verify                # is the repo healthy? (writes REPO_STATUS.md)
#   make check                 # everything that must pass before a batch
#   make plan SCENE=...        # scene file -> job file (+ estimate, + lint)
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

.PHONY: help verify check plan dry gen audit film wiring clean trig

help:
	@grep -E '^#   ' Makefile

verify:
	$(PY) studio/verify.py            # inventory, data, triggers, compile, smoke
	@echo "verify: report -> REPO_STATUS.md"

check:
	$(PY) -m py_compile studio/*.py studio/toolbox/*.py studio/knowledge/*.py bridge/*.py
	$(PY) studio/links.py                 # no dangling paths after a move
	$(PY) studio/knowledge/bank.py check
	$(PY) studio/knowledge/banktest.py
	@echo "verify:
	$(PY) studio/verify.py            # inventory, data, triggers, compile, smoke
	@echo "verify: report -> REPO_STATUS.md"

check: ok"

plan:
	$(PY) studio/shotplan.py plan $(SCENE) --out $(JOBS) --parallel $(PAR)

dry:
	$(PY) studio/mivi_shot.py $(JOBS) --out $(OUT) --dry-run --parallel $(PAR)

audit:
	$(PY) studio/mivi_shot.py $(JOBS) --out $(OUT) --dry-run --parallel $(PAR) 2>&1 | grep -c WARN || true

gen:
	@echo "$(JOBS)" > .mivi-trigger
	@echo "trigger written — now: git add .mivi-trigger && git commit && git push"

film:
	$(PY) studio/filmkit.py assemble $(NAME) --crossfade 0.2

trig:
	@ls -1 .*-trigger 2>/dev/null | while read f; do printf '%-20s %s\n' "$$f" "$$(head -1 $$f)"; done

wiring:
	$(PY) studio/tests/test_mivi_shot.py   # offline: scheduler, chain, report flags

clean:
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
