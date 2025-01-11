def nota_teoria(n1: float|None, n2:float|None) -> float:
    return ((n1 if type(n1) is float else 0) + (n2 if type(n2) is float else 0)) / 2