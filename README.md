# Código de `Grafoviu`

from abc import ABC
from abc import abstractmethod

class Grafo(ABC):

    def __init__(self, path_file):
        self._nodes = set()
        aristas = []
        with open(path_file, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    origen, destino, peso = line.split(' ')
                    self._nodes.add(origen)
                    self._nodes.add(destino)
                    aristas.append((origen, destino, int(peso)))
        self._nodes = sorted(self._nodes)
        self._node_index = {node: index for index, node in enumerate(self._nodes)}
        for arista in aristas:
            self.aniadir_arista(arista)
        
    @abstractmethod
    def aniadir_arista(self, arista):
        pass

    @abstractmethod
    def contiene_arista(self, arista):
        pass


class GrafoListasAdyacencia(Grafo):
    def __init__(self, path_file):
        self.__grafo = {}  
        super().__init__(path_file)
    
    def aniadir_arista(self, arista):
        origen, destino, peso = arista
        self.__grafo.setdefault(origen, []).append((destino, peso))

    def contiene_arista(self, arista):
        return (arista.destino, arista.peso) in self.__grafo.get(arista.origen, [])

    def __str__(self):
        strgrafo = "{\n"
        for key in self.__grafo.keys():
            strgrafo += f"{key} : {self.__grafo[key]}\n"
        strgrafo += "}"  
        return strgrafo


class GrafoMatrizAdyacencia(Grafo):
    def __init__(self, path_file):
        self.__grafo = None  
        super().__init__(path_file)

    def aniadir_arista(self, arista):
        if self.__grafo is None:
            self.__grafo = [[0] * len(self._nodes) for _ in range(len(self._nodes))]
        origen, destino, peso = arista
        self.__grafo[self._node_index[origen]][self._node_index[destino]] = peso

    def contiene_arista(self, arista):
        origen_idx = self._node_index.get(arista.origen)
        destino_idx = self._node_index.get(arista.destino)
    
        if origen_idx is not None and destino_idx is not None:
            return self.__grafo[origen_idx][destino_idx] != 0
        else:
            return False
    
    def __str__(self):
        strgrafo = "  "
        for node in self._nodes:
            strgrafo += f"{node} "
        strgrafo += "\n"
        for index, node in enumerate(self._nodes):
            strgrafo += f"{node} "
            for weight in self.__grafo[index]:
                strgrafo += f"{weight} "
            strgrafo += "\n"
        return strgrafo


## `arista.py`

```python
class Arista:
    def __init__(self, origen, destino, peso):
        self.__peso = peso
        self.__origen = origen
        self.__destino = destino

    def __str__(self):
        return f"|{(self.__origen, self.__destino, self.__peso)}|"
    
    def get_arista(self):
        return (self.__origen, self.__destino, self.__peso)

    @property
    def peso(self):
        return self.__peso
    
    @property
    def origen(self):
        return(self.__origen)
    
    @property
    def destino(self):
        return(self.__destino)



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
    
def buscar_arista(grafo, arista):
    if grafo.contiene_arista(arista):
        print("Arista encontrada en el grafo")
    else:
        print("Arista no encontrada en el grafo")

if __name__ == "__main__":
    sys.exit(main())
