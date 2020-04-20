
class Camion:

    __identificador = ''
    __nombreConductor = ''
    __patente =''
    __marcaCamion = ''
    __tara = 0

    def __init__(self,identificador,nombre,patente,marca,tara=0):
        self.__identificador = identificador
        self.__nombreConductor = nombre
        self.__patente = patente
        self.__marcaCamion = marca
        self.__tara = tara

    def getNumero(self):
        return self.__identificador

    def getTara(self):
        return self.__tara

    def getNombre(self):
        return self.__nombreConductor

    def getPatente(self):
        return self.__patente

    def __str__(self):
        return '%s %6s' % (self.__patente,self.__nombreConductor)