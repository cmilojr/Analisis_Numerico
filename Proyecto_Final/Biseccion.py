from Funciones import Funciones
import math
class Biseccion:
    def __init__(self):
        self.valores=[]
        self.raiz=""

    def algorimo_biseccion(self,xi,xu,Funcion,tolerancia):
        if((Funcion.evaluar(xi))*(Funcion.evaluar(xu))>0 or tolerancia<0):
            self.raiz="Valores ingresados invalidos"
        else:
            
            contador=1
            xm=(xi+xu)/2
            xm_anterior=0

            while (Funcion.evaluar(xm)!=0):
                error=0.0
                xm=(xi+xu)/2
                valor=Funcion.evaluar(xm)
                if(contador>1):
                    error=math.fabs(xm-xm_anterior)
                self.valores.append([contador,xi,xu,xm,valor,error])
                if(error<=tolerancia and contador>1):
                    break
                if(valor>0):
                    xi=xm
                else:
                    xu=xm
                xm_anterior=xm
                contador+=1
            self.raiz=f"[{xi},{xu}]"

    def tabla_valores(self):
        return self.valores
    def get_raiz(self):
        return str(self.raiz)

