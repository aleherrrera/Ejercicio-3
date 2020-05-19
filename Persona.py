class Persona:
    __nombre=''
    __direccion=''
    __dni=''
    __idTaller=0

    def __init__(self,nombre,direc,dni,id):
        self.__nombre=nombre
        self.__direccion=direc
        self.__dni=dni
        self.__idTaller=id

    def getDni(self):
        return self.__dni
    def getId(self):
        return self.__idTaller

    def __str__(self):
        return '%s     %s %s'% (self.__nombre,self.__dni,self.__direccion)

