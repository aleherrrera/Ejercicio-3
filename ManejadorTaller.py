import numpy as np
import csv
from TallerCapacitacion import Taller
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
        return i

    def InscribirPersona(self):
        id=int(input('Ingresar Id de taller: '))
        i=self.BuscarTaller(id)
        if self.__talleres[i].getVacantes() > 0:
            nom=str(input('Ingrese nombre: '))
            direc=str(input('Ingrese direccion: '))
            dni=str(input('Ingrese DNI: '))
            print('Ingrese Fecha')
            dia=str(input('Ingrese dia: '))
            mes=str(input('Ingrese mes: '))
            anio=str(input('Ingrese año: '))
            fecha=dia+'/'+mes+'/'+anio
            unaPersona=Persona(nom,direc,dni,id)
            self.__talleres[i].Inscribir(unaPersona,fecha)
            return unaPersona
        else:
            print('No hay vacantes')

    def Nom_Monto(self,id):
        i=self.BuscarTaller(id)
        print('Taller: {}\nMonto: ${}'.format(self.__talleres[i].getNom(),self.__talleres[i].getMonto()))

    def RegistrarPago(self,id,dni):
        i=self.BuscarTaller(id)
        self.__talleres[i].setPago(dni)

    def Fecha(self,id,dni):
        i=self.BuscarTaller(id)
        fecha=self.__talleres[i].getFecha(dni)
        return fecha
    def Pago(self,id,dni):
        i=self.BuscarTaller(id)
        pago=self.__talleres[i].getPago(dni)
        return pago