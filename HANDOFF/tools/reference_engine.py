"""Reference implementation of the behaviour recovered in HANDOFF/04 and HANDOFF/05.

This module exists so that the vectors in HANDOFF/data/*.json can be executed, and so that a builder of the
independent `mimo/` project has a small, readable statement of the rules. It contains no decompiled code: it is a
clean-room re-statement of behaviour that was read from bytecode (VERIFIED_STATIC, never executed).

Rules implemented
-----------------
normalise(s)            qm.i.a  — lower-case (Locale.US), keep letters/digits and < > ( ) : { } , .
validated_input(...)           — three-way verdict; PARTIAL only on raw != expected with equal normalised forms
selection_verdict(...)         — set equality (all-or-nothing)
fill_the_gap(...)              — count equality then index-wise text equality
visibility(...)         jm.m/n/o — ALWAYS / CORRECT / WRONG gating
apply_submission(...)   V/W/X/U  — attempts++ and the 0/1 tries flag
queue_*                        — outbox store / move / post / clear
derived metrics                — isSolvedCorrectly, firstTryCount, AnswersInChapter
"""

from __future__ import annotations

KEEP_PUNCTUATION = set("<>():{},.")
CORRECT, PARTIAL, INCORRECT = "CORRECT", "PARTIAL", "INCORRECT"


def normalise(text: str) -> str:
    """qm.i.a — qm.i.a(String)String.

    Lower-cases with Locale.US semantics (so 'I' -> 'i' regardless of the host locale), keeps Unicode
    letters and digits, keeps nine punctuation characters < > ( ) : { } , . and drops everything else.
    """
    out = []
    for ch in text:
        low = _lower_us(ch)
        if low.isalnum():
            out.append(low)
        elif low in KEEP_PUNCTUATION:
            out.append(low)
    return "".join(out)


def _lower_us(ch: str) -> str:
    # Python's str.lower() follows Unicode, which matches Kotlin's Locale.US behaviour for the characters
    # Mimo's content uses. The explicit table covers the classic Locale.US-vs-default trap (Turkish I).
    if ch == "I":
        return "i"
    if ch == "\u0130":  # dotted capital I
        return "i"
    return ch.lower()


def validated_input(user: str, expected: str) -> str:
    """qm.f/qm.e/qm.g — the only interaction that can produce PARTIAL."""
    if normalise(user) != normalise(expected):
        return INCORRECT
    if user == expected:
        return CORRECT
    return PARTIAL


def selection_verdict(items: list[dict]) -> str:
    """Selection single/multiple: chosen set must equal the correct set. Empty selection is incorrect."""
    if not items:
        return "INCORRECT (empty guard)"
    correct = {i for i, it in enumerate(items) if it.get("correct")}
    chosen = {i for i, it in enumerate(items) if it.get("selected")}
    if not chosen or len(chosen) != len(correct):
        return INCORRECT
    return CORRECT if chosen == correct else INCORRECT


def fill_the_gap(selected: list[str], expected: list[str]) -> str:
    """All-or-nothing: count equality first, then index-wise text equality."""
    if len(selected) != len(expected):
        return INCORRECT
    return CORRECT if all(a == b for a, b in zip(selected, expected)) else INCORRECT


def spell(selected: list[str], expected: list[str]) -> str:
    """Character spelling: joined with '' and compared as one string (two-way, never PARTIAL)."""
    return CORRECT if "".join(selected) == "".join(expected) else INCORRECT


def visibility(declared: str, verdict: str) -> bool:
    """`visible-if` gating. PARTIAL renders ALWAYS only (dm.n state)."""
    declared = declared.upper()
    if declared == "ALWAYS":
        return True
    if declared == "CORRECT":
        return verdict == CORRECT
    if declared == "WRONG":
        return verdict == INCORRECT
    raise ValueError(f"unknown visibility {declared!r}")


def apply_submission(verdict: str, c_before, d_before: int) -> dict:
    """The V/W/X/U update sites. `C` = "the previous answer was wrong"; `d` = attempts.

    V (CORRECT)     attempts+1, tries = 0 if C else 1, C := False
    W (PARTIAL)     attempts+1, tries = 0 if C else 1, C := False
    X (INCORRECT)   attempts+1, tries = 0,            C := True
    U (PROCEED)     attempts+1, tries = 1 if C else 0, C unchanged
    """
    c = bool(c_before is True)
    attempts = d_before + 1
    result = {"attempts": attempts}
    if verdict == CORRECT:
        result.update(tries=1 if not c else 0, C_after=False)
    elif verdict == PARTIAL:
        result.update(tries=1 if not c else 0, C_after=False)
    elif verdict == INCORRECT:
        result.update(tries=0, C_after=True)
    elif verdict == "PROCEED":
        result.update(tries=1 if c else 0)
    else:
        raise ValueError(verdict)
    return result


def is_solved(tries: int) -> bool:
    return tries >= 1


def first_try_count(rows: list[dict]) -> int:
    return sum(1 for r in rows if is_solved(r["tries"]) and r["attempts"] == 1)


def answers_in_chapter(rows: list[dict]) -> dict:
    return {"answeredCorrectly": sum(1 for r in rows if is_solved(r["tries"])),
            "answeredTotal": len(rows)}


# --- outbox ---------------------------------------------------------------------------------------------

def queue_store(rows: list[dict], row_id: int) -> list[dict]:
    return rows + [{"id": row_id, "in_queue": 1}]


def queue_move(rows: list[dict]) -> list[dict]:
    return [{"id": r["id"], "in_queue": 0} for r in rows]


def queue_post(rows: list[dict]) -> tuple[list[dict], list[int]]:
    """A successful upload posts every row and deletes the posted ids."""
    return [], [r["id"] for r in rows]


def queue_clear(rows: list[dict]) -> list[dict]:
    return [r for r in rows if r["in_queue"] != 1]


def pending(rows: list[dict]) -> list[int]:
    return [r["id"] for r in rows if r["in_queue"] == 1]


def local_completion(lesson_tries: list[int]) -> bool:
    """ADD-04 — the engine's replacement for the server-derived completion of Mimo."""
    return bool(lesson_tries) and all(is_solved(t) for t in lesson_tries)
