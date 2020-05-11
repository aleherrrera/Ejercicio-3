import numpy as np
from Inscripcion import Inscripcion

class ArreInscripciones:
    __cantidad=0
    __dimension=0
    __incremento=5

    def __init__(self,dimension,incremento=5):
        self.__inscripciones=np.empty(dimension,dtype=Inscripcion)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento

    def  agregarInscripcion(self,persona,fecha,taller):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__inscripciones.resize(self.__dimension)
        pago=False
        unaInscripcion=Inscripcion(fecha,pago,persona,taller)
        self.__inscripciones[self.__cantidad]=unaInscripcion
        self.__cantidad+=1
        print('Inscripto correctamente')

    def Busca(self,dni):
        i = 0
        while i < self.__cantidad and self.__inscripciones[i].getdni() != dni:
            i += 1
        return i

    def Pagar(self,dni):
        i=self.Busca(dni)
        self.__inscripciones[i].setPago()
        if self.__inscripciones[i].getpago()==True:
            print('Pago realizado')

    def fecha(self,dni):
        i=self.Busca(dni)
        return self.__inscripciones[i].getfecha()
    def pago(self,dni):
        i=self.Busca(dni)
        return self.__inscripciones[i].getpago()