class Inscripcion:
    __fechaInscripcion=''
    __pago=bool
    __persona=None
    __taller=None

    def __init__(self,fecha,pago,persona,taller):
        self.__fechaInscripcion=fecha
        self.__pago=pago
        self.__persona=persona
        self.__taller=taller

    def getdni(self):
        return self.__persona.getDni()
    def getpago(self):
        return self.__pago
    def getfecha(self):
        return self.__fechaInscripcion

    def setPago(self):
        self.__pago=True