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

    def crearInscripcion(self,persona,fecha,taller):
        pago = False
        unaInscripcion = Inscripcion(fecha, pago, persona, taller)
        self.agregarInscripcion(unaInscripcion)
        return unaInscripcion

    def  agregarInscripcion(self,unaInscripcion):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__inscripciones.resize(self.__dimension)
        self.__inscripciones[self.__cantidad]=unaInscripcion
        self.__cantidad+=1

    def Busca(self,dni):
        i = 0
        while i < self.__cantidad and self.__inscripciones[i].getdni() != dni:
            i += 1
        return i

    def pago(self,dni):
        i=self.Busca(dni)
        return self.__inscripciones[i].getpago()

    def Pagar(self,dni):
        i=self.Busca(dni)
        self.__inscripciones[i].setPago()

    def inscriptos(self,id):
        for i in range(self.__cantidad):
            self.__inscripciones[i].getPersona(id)

    def generarLista(self):
        lista=[]
        for i in range(self.__cantidad):
            dni = self.__inscripciones[i].getdni()
            id = self.__inscripciones[i].getid()
            fecha = self.__inscripciones[i].getfecha()
            pago = self.__inscripciones[i].getpago()
            inscripto = (dni, id, fecha, pago)
            lista.append(inscripto)
        return lista