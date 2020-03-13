import numpy
from matplotlib import pyplot
from Funciones import Funciones
class Graficar:
    def dibujar_funciones(self,funcion,posicion_inicial,posicion_final,incremento):
        Funcion=Funciones(funcion)
        
        x = numpy.arange(posicion_inicial, posicion_final,incremento)
        pyplot.plot(x, [Funcion.evaluar(i) for i in x])

        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")


        pyplot.show()