def potencia(a, b):
    try:
        return a ** b
    except TypeError:
        raise TypeError("Os valores informados devem ser numéricos.")
    except Exception as e:
        raise ValueError(f"Erro ao calcular potência: {e}")
