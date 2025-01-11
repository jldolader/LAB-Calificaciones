def nota_teoria(n1: float|None, n2:float|None) -> float:
    return ((n1 if type(n1) is float else 0) + (n2 if type(n2) is float else 0)) / 2

def nota_cuatrimestre(ntt: tuple[float|None, float|None], np: float|None) -> float:
    nt = nota_teoria(ntt[0], ntt[1])
    return (0.2 * nt + 0.8 * (np if type(np) is float else 0)) if nt >= 4 else 0

def nota_continua(nt: tuple[float|None, float|None, float|None, float|None],
                  np: tuple[float|None, float|None]) -> float:
    nc1 = nota_cuatrimestre((nt[0], nt[1]), np[0])
    nc2 = nota_cuatrimestre((nt[2], nt[3]), np[1])
    
    return (nc1 + nc2) / 2 if nc1 >= 4 and nc2 >= 4 else min(4, (nc1 + nc2) / 2)