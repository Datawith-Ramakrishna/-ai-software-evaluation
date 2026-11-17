import pytest
from calculator import calculate

@pytest.mark.parametrize("a,b,op,expected", [
    (4, 2, "add", 6),
    (4, 2, "subtract", 2),
    (4, 2, "multiply", 8),
    (4, 2, "divide", 2),
    (-4, 2, "add", -2),
    (5, 2, "divide", 2.5),
    (0, 5, "multiply", 0),
])
def test_operations(a, b, op, expected):
    assert calculate(a, b, op) == expected

def test_zero_division():
    with pytest.raises(ValueError):
        calculate(1, 0, "divide")

def test_unknown_operation():
    with pytest.raises(ValueError):
        calculate(1, 2, "power")
