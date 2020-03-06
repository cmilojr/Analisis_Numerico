from Busqueda_incremental import Busqueda_incremental
from Funciones import Funciones
from Graficador import Graficador

class Ejecutable:
    
    def ejecutar(self):
        funciones=Funciones("(x**3)+4*(x**2)-9.47")
        incrementar=Busqueda_incremental()
        incrementar.Operacion(-5,1,10,funciones)

        

valor=Ejecutable()
valor.ejecutar()