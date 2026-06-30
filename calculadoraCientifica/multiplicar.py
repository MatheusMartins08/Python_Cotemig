def multiplicar(a, b):
    try:
        return a * b
    except TypeError:
        raise TypeError("Os valores informados devem ser numéricos.")