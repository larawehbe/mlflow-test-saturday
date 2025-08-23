# tests/test_add.py
import math

def add(a, b):
    return a + b    

def test_add_integers():
    assert add(1, 1) == 2

def test_add_negatives():
    assert add(-3, -7) == -10

def test_add_mixed_signs():
    assert add(-5, 12) == 7

def test_add_floats():
    assert math.isclose(add(0.1, 0.2), 0.3, rel_tol=1e-9, abs_tol=1e-12)

def test_add_bigints():
    assert add(10**12, 10**12) == 2 * 10**12
