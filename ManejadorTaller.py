import numpy as np
import csv
from datetime import date
from TallerCapacitacion import Taller
from ManejadorInscripcion import ArreInscripciones
from Persona import Persona

class ArreTalleres:
    __cantidad=0
    __dimension=0
    __incremento=3

    def __init__(self,dimension,incremento=5):
        self.__talleres=np.empty(dimension,dtype=Taller)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento

    def CargarTaller(self):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__talleres.resize(self.__dimension)
        archivo=open('Talleres.csv')
        reader=csv.reader(archivo,delimiter=',')
        bandera=True
        for fila in reader:
            if bandera:
                self.__dimension = fila[0]
                bandera=not bandera
            else:
                id=int(fila[0])
                nom=str(fila[1])
                vacantes=int(fila[2])
                monto=int(fila[3])
                unTaller=Taller(id,nom,vacantes,monto)
                self.__talleres[self.__cantidad]=unTaller
                self.__cantidad+=1

    def MostrarTalleres(self):
        print('Id  Nombre     Monto')
        for i, taller in enumerate(self.__talleres):
            taller.mostrarDatos()

    def BuscarTaller(self,id):
        i=0
        while i<self.__cantidad and id != self.__talleres[i].getId():
            i+=1
        if i<self.__cantidad:
            return i


    def InscribirPersona(self,Inscripciones):
        id=int(input('Ingresar Id de taller: '))
        i=self.BuscarTaller(id)
        if i!=None:
            if self.__talleres[i].getVacantes() > 0:
                nom=str(input('Ingrese nombre: '))
                direc=str(input('Ingrese direccion: '))
                dni=str(input('Ingrese DNI: '))
                fecha=date.today()
                unaPersona=Persona(nom,direc,dni,id)
                inscripcion=self.__talleres[i].Inscribir(unaPersona,fecha)
                Inscripciones.agregarInscripcion(inscripcion)
                return unaPersona
            else:
                print('No hay vacantes')
        else:
            print('Taller ingresado incorrecto')

    def Nom_Monto(self,id,dni):
        i=self.BuscarTaller(id)
        if self.__talleres[i].getPago(dni)!=True:
            print('Taller: {}\nMonto: ${}'.format(self.__talleres[i].getNom(),self.__talleres[i].getMonto()))
        else:
            print('Taller: {}\nMonto: $0'.format(self.__talleres[i].getNom()))

    def RegistrarPago(self,id,dni):
        i=self.BuscarTaller(id)
        self.__talleres[i].setPago(dni)

    def ListarPersonas(self):
        id = int(input('Ingresar Id del taller: '))
        i=self.BuscarTaller(id)
        if i !=None:
            print('Nombre  DNI      Direccion ')
            self.__talleres[i].lista(id)
        else:
            print('Taller ingresado incorrecto')