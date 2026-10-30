import pytest
from calculate.calculator_program import calculate

def test_calculate_addition():
    assert calculate(1, 1, '+') == 2

def test_calculate_division():
    assert calculate(8, 2, '/') == 4

def test_calculate_unknown_operation():
    assert calculate(5, 5, 'tidak diketahui') == "Operasi tidak dikenal."

def test_calculate_subtraction():
    assert calculate(10, 5, '-') == 5

def test_calculate_multiplication():
    assert calculate(3, 4, '*') == 12
