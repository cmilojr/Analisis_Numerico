import math

class Busqueda_incremental:
    
    def Operacion(self, valor_inicial,incremento,item,Funciones):
        valor_evaluado_actual=Funciones.evaluar(valor_inicial)
        if valor_evaluado_actual==0:
            print(f"{valor_inicial} es una raiz")
        else:
            if incremento == 0:
                print("El valor asignado al incremento es incorrecto")
            else:
                if item<=0:
                    print("El valor del iterador es incorrecto")
                else:
                    contador=0
                    valor_nuevo=valor_inicial+incremento
                    while (contador<item):

                        valor_evaluado_nuevo=Funciones.evaluar(valor_nuevo)
                        
                        if(valor_evaluado_actual*valor_evaluado_nuevo<0):
                            break

                        valor_evaluado_actual=valor_evaluado_nuevo
                        valor_inicial=valor_nuevo

                        valor_nuevo+=incremento

                        contador+=1

                        
                    if valor_evaluado_actual*valor_evaluado_nuevo<0:
                        print(f"Los valores [{round(valor_inicial,2)},{round(valor_nuevo,2)}] definen un intervalo")
                    else:
                        if valor_evaluado_actual==0:
                            print(f"{round(valor_inicial,2)} es una raiz")
                        else:
                            print("Se presento un fraso en las iteraciones")
    
    

