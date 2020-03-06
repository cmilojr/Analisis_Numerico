from scitools.StringFunction import StringFunction

class Funciones:
    def __init__(self,entrada):
        self.funcion=StringFunction(entrada)
    
    def evaluar(self,valor):
       return self.funcion(valor)









