from calificaciones import *

def test_nota_teoria():
    print(nota_teoria(9.1, 7.2))
    print(nota_teoria(4.0, 6.0))
    print(nota_teoria(4.0, 3.0))
    print(nota_teoria(None, 3.0))
    print(nota_teoria(9.0, None))
    print(nota_teoria(None, None))

def test_nota_cuatrimestre():
    print(nota_cuatrimestre((9.1, 7.2), 8.1))
    print(nota_cuatrimestre((4.0, 6.0), 5.0))
    print(nota_cuatrimestre((4.0, 3.0), None))
    print(nota_cuatrimestre((None, 3.0), None))
    print(nota_cuatrimestre((9.0, None), 4.5))
    
    
if __name__ == '__main__':
    #test_nota_teoria()
    test_nota_cuatrimestre()