from ManejadorInscripcion import ArreInscripciones

class Taller:
    __idTaller=0
    __nombre=''
    __vacantes=0
    __montoInscripcion=0
    __inscripciones=ArreInscripciones(0,5)

    def __init__(self,ident,nom,vacantes,monto):
        self.__idTaller=ident
        self.__nombre=nom
        self.__vacantes=vacantes
        self.__montoInscripcion=monto
        self.__inscrpiciones=ArreInscripciones(vacantes,5)

    def getId(self):
        return self.__idTaller
    def getVacantes(self):
        return self.__vacantes
    def getMonto(self):
        return self.__montoInscripcion
    def getNom(self):
        return self.__nombre
    def getPago(self,dni):
        return self.__inscripciones.pago(dni)

    def setPago(self,dni):
        self.__inscripciones.Pagar(dni)

    def Inscribir(self,persona,fecha):
        self.__vacantes-=1
        inscripcion=self.__inscripciones.crearInscripcion(persona,fecha,self)
        return inscripcion

    def lista(self,id):
        self.__inscripciones.inscriptos(id)

    def mostrarDatos(self):
        print('{} {:12} ${}'.format(self.__idTaller,self.__nombre,self.__montoInscripcion))