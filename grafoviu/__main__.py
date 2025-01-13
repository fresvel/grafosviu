import sys

from grafoviu.arista import Arista
from grafoviu.grafo import GrafoListasAdyacencia
from grafoviu.grafo import GrafoMatrizAdyacencia
def main():
    print("Bienvenido a grafoviu!")
    
    grafo_lista = GrafoListasAdyacencia("grafoviu/assets/grafo.txt")
    print(grafo_lista)
    
    grafo_matriz = GrafoMatrizAdyacencia("grafoviu/assets/grafo.txt")
    print(grafo_matriz)
    
    print("-----------------Testing Lists----------------")

    aristas_true = [
    Arista("a", "b", 1),
    Arista("a", "c", 3),
    Arista("b", "e", 3),
    Arista("c", "a", 2),
    Arista("c", "d", 1),
    Arista("d", "a", 1),
    Arista("d", "e", 2),
    Arista("d", "f", 1),
    Arista("e", "c", 3),
    Arista("e", "f", 4),
    Arista("f", "g", 1),
    Arista("g", "b", 2)
    ]

    aristas_false = [
    Arista("a", "d", 5),
    Arista("b", "f", 7),
    Arista("c", "e", 4),
    Arista("d", "g", 6),
    Arista("e", "b", 2),
    Arista("f", "a", 8),
    Arista("g", "c", 9),
    Arista("a", "f", 3),
    Arista("t", "u", 2),
    Arista("k", "y", 7),
    Arista("f", "h", 1),
    Arista("h", "d", 5)
    ]

    print("Testing True cases...")
    for arista in aristas_true:
        buscar_arista(grafo_lista, arista)
    print("Testing False cases...")
    for arista in aristas_false:
        buscar_arista(grafo_lista, arista)

    print("-----------------Testing Matrices----------------")
    print("Testing True cases...")
    for arista in aristas_true:
        buscar_arista(grafo_matriz, arista)
    print("Testing False cases...")
    for arista in aristas_false:
        buscar_arista(grafo_matriz, arista)
    


if __name__ == "__main__":
    sys.exit(main())


def buscar_arista(grafo, arista):
    if grafo.contiene_arista(arista):
        print("Arista encontrada en el grafo")
    else:
        print("Arista no encontrada en el grafo")
