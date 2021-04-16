class Motorista:
    def __init__(self, id, nome, restaurante):
        self.__id = id
        self.__nome = nome
        self.__restaurante = restaurante
        
    @property
    def id(self):
        return self.__id
        
    @property
    def nome(self):
        return self.__nome
        
    @property
    def restaurante(self):
        return self.__restaurante
