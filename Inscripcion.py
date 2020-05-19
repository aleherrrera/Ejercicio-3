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
    def getid(self):
        return self.__persona.getId()
    def getPersona(self,id):
        if self.__persona.getId()==id:
            print(self.__persona)

    def setPago(self):
        self.__pago=True