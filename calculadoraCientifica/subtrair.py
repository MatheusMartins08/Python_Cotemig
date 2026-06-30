def subtrair(a, b):
    try:
        return a - b
    except TypeError:
        raise TypeError("Os valores informados devem ser numéricos.")
