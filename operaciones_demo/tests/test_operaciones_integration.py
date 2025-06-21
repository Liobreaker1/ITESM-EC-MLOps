import pytest
from operaciones import suma, multiplicacion, division

def test_operacion_compuesta():
    resultado = division(multiplicacion(suma(3, 2), 4), 2)
    assert resultado == 10.0

def test_operacion_negativa():
    resultado = division(multiplicacion(suma(-1, 6), 2), 1)
    assert resultado == 10.0