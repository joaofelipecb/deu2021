class Usuario:
    def __init__(self,id,especie):
        self.__id = id
        self.__especie = especie
        self.motoristaCache = None
    
    @property
    def id(self):
        return self.__id
        
    @property
    def especie(self):
        return self.__especie
