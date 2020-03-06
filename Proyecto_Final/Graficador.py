from matplotlib import pyplot

class Graficador:

    def dibujar_funciones(self):
        x = range(-10, 15)
        pyplot.plot(x, [self.funciones(i) for i in x])

        pyplot.axhline(0, color="black")
        pyplot.axvline(0, color="black")

        pyplot.xlim(-10, 10)
        pyplot.ylim(-10, 10)

        pyplot.show()
