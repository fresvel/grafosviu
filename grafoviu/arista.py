
class Arista:
    def __init__(self, origen, destino, peso):
        self.__peso = peso
        self.__origen = origen
        self.__destino = destino

    def __str__(self):
        return f"Arista: |{self.__origen}, {self.__destino}, {self.__peso}|"