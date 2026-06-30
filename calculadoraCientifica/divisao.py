def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ValueError("Divisão por zero não é permitida.")
    except TypeError:
        raise TypeError("Os valores informados devem ser numéricos.")