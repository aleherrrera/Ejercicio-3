
class ListaPersona:
    __lista=[]

    def __init__(self):
        self.__lista=[]

    def cargarPersona(self,unaPersona):
        self.__lista.append(unaPersona)

    def longitud(self):
        return len(self.__lista)

    def BuscarPersona(self,dni):
        i=0
        c=self.longitud()
        while i < c and self.__lista[i].getDni() != dni:
            i+=1
        return self.__lista[i].getId()

    def ListarPersonas(self,id):
        print('Nombre  DNI      Direccion ')
        for i, persona in enumerate(self.__lista):
            if persona.getId()==id:
                print(persona)

    def Dni(self,i):
        return self.__lista[i].getDni()
    def Id(self,i):
        return self.__lista[i].getId()