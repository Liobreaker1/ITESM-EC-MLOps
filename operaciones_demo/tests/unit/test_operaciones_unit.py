import pytest
from operaciones import suma, resta, multiplicacion, division


def test_suma():
    assert suma(2, 6) == 5

def test_resta():
    assert resta(5, 2) == 3

def test_multiplicacion():
    assert multiplicacion(5, 2) == 10

def test_division():
    assert division(10, 2) == 5

def test_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        division(8,0)