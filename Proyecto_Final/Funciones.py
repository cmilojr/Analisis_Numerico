import sympy
from sympy.parsing.sympy_parser import parse_expr

class Funciones:
    def __init__(self,entrada):
        self.funcion=parse_expr(entrada,evaluate=False)
    
    def evaluar(self,valor):
        print(self.funcion)
        return  self.funcion.evalf(subs=dict(x=valor))








