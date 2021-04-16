class Condition:
    def __init__(self, operator, operands):
        self.__operator = operator
        self.__operands = operands
        
    @property
    def operator(self):
        return self.__operator
        
    @property
    def operands(self):
        return self.__operands
