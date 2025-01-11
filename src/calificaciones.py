def nota_teoria(n1: float|None, n2:float|None) -> float:
    return ((n1 if type(n1) is float else 0) + (n2 if type(n2) is float else 0)) / 2

def nota_cuatrimestre(ntt: tuple[float|None, float|None], np: float|None) -> float:
    nt = nota_teoria(ntt[0], ntt[1])
    return (0.2 * nt + 0.8 * (np if type(np) is float else 0)) if nt >= 4 else 0