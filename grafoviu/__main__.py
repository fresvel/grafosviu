import sys

from grafoviu.arista import Arista
from grafoviu.grafo import GrafoListasAdyacencia
from grafoviu.grafo import GrafoMatrizAdyacencia
def main():
    print("Bienvenido a grafoviu!")
    
    grafo = GrafoListasAdyacencia("grafoviu/assets/grafo.txt")
    print(grafo)

    arista_1 = Arista('d', 'a', 1) 
    arista_2 = Arista('d', 'b', 1) 

    ret=grafo.contiene_arista(arista_1) # Devuelve True, dado que la arista existe en el grafo.
    print(ret) 
    ret=grafo.contiene_arista(arista_2) # Devuelve False, dado que la arista no existe en el grafo. 
    print(ret)

    print("---------------------------------")
    
    grafo = GrafoMatrizAdyacencia("grafoviu/assets/grafo.txt")
    print(grafo)
    
    arista_1 = Arista('d', 'a', 1) 
    arista_2 = Arista('d', 'b', 1) 

    ret=grafo.contiene_arista(arista_1) # Devuelve True, dado que la arista existe en el grafo.
    print(ret) 
    ret=grafo.contiene_arista(arista_2) # Devuelve False, dado que la arista no existe en el grafo. 
    print(ret)

if __name__ == "__main__":
    sys.exit(main())