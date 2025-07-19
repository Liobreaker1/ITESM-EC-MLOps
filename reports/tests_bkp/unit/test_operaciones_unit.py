# tests/unit/test_operaciones_unit.py

import pytest
from operaciones import suma, resta, multiplicacion, division

def test_suma():
    assert suma(3, 2) == 5

def test_resta():
    assert resta(5, 2) == 3

def test_multiplicacion():
    assert multiplicacion(4, 3) == 12

def test_division():
    assert division(10, 2) == 5

def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        division(8, 0)
