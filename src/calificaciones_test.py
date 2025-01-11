from calificaciones import *

def test_nota_teoria():
    print(nota_teoria(9.1, 7.2))
    print(nota_teoria(4.0, 6.0))
    print(nota_teoria(4.0, 3.0))
    print(nota_teoria(None, 3.0))
    print(nota_teoria(9.0, None))
    print(nota_teoria(None, None))


if __name__ == '__main__':
    test_nota_teoria()