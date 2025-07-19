# tests/integration/test_operaciones_integration.py

from operaciones import suma, multiplicacion, division

def test_operacion_compuesta():
    # (3 + 2) * 4 / 2 = 10
    resultado = division(multiplicacion(suma(3, 2), 4), 2)
    assert resultado == 10

def test_operacion_con_negativos():
    # (-1 + 6) * 2 / 1 = 10
    resultado = division(multiplicacion(suma(-1, 6), 2), 1)
    assert resultado == 10
