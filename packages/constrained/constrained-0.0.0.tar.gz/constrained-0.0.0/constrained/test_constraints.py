import pytest
from constrained import Float, Int, Regex, CFG, enforce_annotation_constraints

@enforce_annotation_constraints
def test_func(x: Float[0, 'inf']) -> Float[0, 'inf']:
    return x / 2

def test_float():
    assert test_func(10.0) == 5.0
    with pytest.raises(ValueError):
        test_func(-10.0)

@enforce_annotation_constraints
def test_func(x: Int[0, 100]) -> Int[0, 100]:
    return x // 2

def test_int():
    assert test_func(10) == 5
    with pytest.raises(ValueError):
        test_func(101)

@enforce_annotation_constraints
def test_func(s: Regex['^[a-z]*$']) -> Regex['^[a-z]*$']:
    return s.lower()

def test_regex():
    assert test_func("abc") == "abc"
    with pytest.raises(ValueError):
        test_func("ABC")

@enforce_annotation_constraints
def test_func(s: CFG['start: "a" "b" "c"']) -> CFG['start: "a" "b" "c"']:
    return s

def test_cfg():
    assert test_func("abc") == "abc"
    with pytest.raises(ValueError):
        test_func("abcd")
