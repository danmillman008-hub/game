"""Layer-B reference: reproduce data/grading_vectors.json exactly.

These tests are the executable form of HANDOFF/04. A build of `mimo/` is Mimo-faithful only when its own tests
make the same assertions.
"""

import pytest

import reference_engine as re
from conftest import load

G = load("grading_vectors.json")


@pytest.mark.parametrize("vec", G["normaliser"]["vectors"], ids=lambda v: repr(v["input"])[:24])
def test_normaliser(vec):
    assert re.normalise(vec["input"]) == vec["expected"]


@pytest.mark.parametrize("vec", G["validated_input_verdict"]["vectors"],
                         ids=lambda v: f"{v['user']!r}vs{v['expected']!r}"[:40])
def test_validated_input_verdict(vec):
    assert re.validated_input(vec["user"], vec["expected"]) == vec["verdict"]


@pytest.mark.parametrize("vec", G["selection_verdict"]["vectors"],
                         ids=lambda v: f"{len(v['items'])}items")
def test_selection_verdict(vec):
    assert re.selection_verdict(vec["items"]) == vec["verdict"]


@pytest.mark.parametrize("vec", G["fill_the_gap_verdict"]["vectors"], ids=lambda v: str(v["selected"])[:24])
def test_fill_the_gap_verdict(vec):
    assert re.fill_the_gap(vec["selected"], vec["expected"]) == vec["verdict"]


@pytest.mark.parametrize("vec", G["spell_verdict"]["vectors"], ids=lambda v: "".join(v["selected"]))
def test_spell_verdict(vec):
    assert re.spell(vec["selected"], vec["expected"]) == vec["verdict"]


@pytest.mark.parametrize("vec", G["module_visibility"]["vectors"],
                         ids=lambda v: f"{v['visibility']}-{v['verdict']}")
def test_module_visibility(vec):
    assert re.visibility(vec["visibility"], vec["verdict"]) is vec["rendered"]


def test_partial_exists_only_for_validated_input():
    """qm.f has exactly one construction site: PARTIAL must not leak into other graders."""
    assert re.validated_input("a = 1", "a=1") == "PARTIAL"
    for items in ([{"correct": True, "selected": True}],):
        assert re.selection_verdict(items) == "CORRECT"
    assert re.fill_the_gap(["<p>"], ["<p>"]) == "CORRECT"


def test_normaliser_keeps_only_nine_punctuation_marks():
    assert re.normalise("{}[](),.:;") == "{}(),.:"
