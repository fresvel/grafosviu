from abc import ABC
from abc import abstractmethod

class Grafo(ABC):

    def __init__(self, path_file):
        self._nodes =set()
        aristas = []
        with open(path_file, 'r') as file:
            for line  in file:
                line = line.strip()
                if line:
                    origen, destino, peso = line.split(' ')
                    self._nodes.add(origen)
                    self._nodes.add(destino)
                    aristas.append((origen, destino, int(peso)))
        self._nodes=sorted(self._nodes)
        self._node_index = {node: index for index, node in enumerate(self._nodes)}
        for arista in aristas:
            self.aniadir_arista(arista)
        
    @abstractmethod
    def aniadir_arista(self, arista): #añade arista al grafo
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
       self.__grafo.setdefault(origen,[]).append((destino, peso))

    def contiene_arista(self, arista):
        return (arista.destino, arista.peso) in self.__grafo.get(arista.origen, [])

    def __str__(self):
        strgrafo="{\n"
        for key in self.__grafo.keys():
            strgrafo+=f"{key} : {self.__grafo[key]}\n"
        strgrafo+="}"  
        return strgrafo
    
class GrafoMatrizAdyacencia(Grafo):
    def __init__(self,path_file):      
        self.__grafo = None  
        super().__init__(path_file)

    def aniadir_arista(self, arista):
        if self.__grafo is None:
            self.__grafo=[[0]*len(self._nodes) for _ in range(len(self._nodes))]
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
        strgrafo="  "
        for node in self._nodes:
            strgrafo+=f"{node} "
        strgrafo+="\n"
        for index, node in enumerate(self._nodes):
            strgrafo+=f"{node} "
            for weight in self.__grafo[index]:
                strgrafo+=f"{weight} "
            strgrafo+="\n"
        return strgrafo