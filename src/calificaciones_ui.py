from calificaciones import *

def solicita_notas() -> tuple[str, float|None, float|None, float|None, float|None,
                              float|None, float|None, float|None]:
    datos = []
    datos.append(input("Introduzca su nombre: "))
    
    for i in range(1, 5):
        n = input(f"Introduzca la nota del examen teórico {i} (- si no se ha presentado): ")
        datos.append(float(n) if n != '-' else None)
    
    for i in range(1, 3):
        p = input(f"Introduzca la nota del examen práctico {i} (- si no se ha presentado): ")
        datos.append(float(p) if p != '-' else None)
    
    return tuple(datos)

def mostrar_notas(d: tuple[str, float|None, float|None, float|None, float|None,
                           float|None, float|None, float|None]):
    print(f"Hola, {d[0]}.")
    print(f"Tus notas del primer cuatrimestre son:")
    print(f"> Teoría: {nota_teoria(d[1], d[2])} > Práctica: {d[5]} > Cuatrimestre: {nota_cuatrimestre((d[1], d[2]), d[5])}")
    
    print(f"Tus notas del segundo cuatrimestre son:")
    print(f"> Teoría: {nota_teoria(d[3], d[4])} > Práctica: {d[6]} > Cuatrimestre: {nota_cuatrimestre((d[3], d[4]), d[6])}")
    
    print(f"Tu nota final de la asignatura es: {nota_continua((d[1], d[2], d[3], d[4]), (d[5], d[6]))}")    
    
if __name__ == '__main__':
    mostrar_notas(solicita_notas())