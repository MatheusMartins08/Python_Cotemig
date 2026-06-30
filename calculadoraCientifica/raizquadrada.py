import math
def raizquadrada(a):
    try:
        if a < 0:
            raise ValueError("Não é possível calcular raiz de número negativo.")
        return math.sqrt(a)
    except TypeError:
        raise TypeError("O valor deve ser numérico.")


