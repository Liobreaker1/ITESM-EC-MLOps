def suma(a, b):
    return a+b

def resta(a, b):
    return a-b

def multiplicacion(a, b):
    return a*b

def division(a, b):
    if b==0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a/b