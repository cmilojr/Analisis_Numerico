from Funciones import Funciones
import math
class Regla_falsa:
    def __init__(self):
        self.valores=[]
        self.raiz=""

    def algorimo_Regla_falsa(self,xi,xu,Funcion,tolerancia):
        if((Funcion.evaluar(xi))*(Funcion.evaluar(xu))>0 or tolerancia<0):
            self.raiz="Valores ingresados invalidos"
        else:
            
            contador=1
            xm=1-((Funcion.evaluar(xi)*(xi-xu))/(Funcion.evaluar(xi)-Funcion.evaluar(xu)))
            xm_anterior=0

            while (Funcion.evaluar(xm)!=0):
                error=0.0
                xm=1-((Funcion.evaluar(xi)*(xi-xu))/(Funcion.evaluar(xi)-Funcion.evaluar(xu)))
                valor=Funcion.evaluar(xm)
                if(contador>1):
                    error=math.fabs(xm-xm_anterior)
                self.valores.append([contador,xi,xu,xm,valor,error])
                if(error<=tolerancia and contador>1):
                    break
                if((Funcion.evaluar(xi)*Funcion.evaluar(xm))>0):
                    xi=xm
                else:
                    xu=xm
                xm_anterior=xm
                contador+=1
            self.raiz=f"[{xi},{xu}]"

    def tabla_valores(self):
        for x in self.valores:
            print(x)
        print(self.raiz)
    def get_raiz(self):
        return str(self.raiz)

prueba=Regla_falsa()
funcion=Funciones("exp(-(x**2)+1)-4*(x**3)+25")
prueba.algorimo_Regla_falsa(1,2,funcion,0.001)
prueba.tabla_valores()