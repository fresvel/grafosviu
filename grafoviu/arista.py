
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