from abc import ABC
from abc import abstractmethod

class Grafo(ABC):

    def __init__(self, path_file):
        with open(path_file, 'r') as file:
            for index, line  in enumerate(file):
                line = line.strip()
                if line:
                    origen, destino, peso = line.split(' ')
                    self.aniadir_arista((origen, destino, int(peso)))

        
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
        print(arista.get_arista())
        origen, destino, peso=arista.get_arista()
        return (destino, peso) in self.__grafo[origen]
        pass

    def __str__(self):
        strgrafo="{\n"
        for key in self.__grafo.keys():
            strgrafo+=f"{key} : {self.__grafo[key]}\n"
        strgrafo+="}"  
        return strgrafo
    
class GrafoMatrizAdyacencia(Grafo):
    def __init__(self,path_file):
        self.__nodes =set() 
        with open(path_file, 'r') as file:
            for line  in file:
                line = line.strip()
                if line:
                    origen, destino, _ = line.split(' ')
                    self.__nodes.add(origen)
                    self.__nodes.add(destino)
        self.__nodes=sorted(self.__nodes)
        self.__node_index = {node: index for index, node in enumerate(self.__nodes)}
        self.__grafo = [[0]*len(self.__nodes) for _ in range(len(self.__nodes))]  
        super().__init__(path_file)

    def aniadir_arista(self, arista):
        origen, destino, peso = arista
        self.__grafo[self.__node_index[origen]][self.__node_index[destino]] = peso

    def contiene_arista(self, arista):
        origen, destino, peso=arista.get_arista()
        return self.__grafo[self.__node_index[origen]][self.__node_index[destino]]!=0