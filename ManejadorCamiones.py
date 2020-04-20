from Camion import Camion

class ListaC:

    __camiones = []

    def __init__(self):
        self.__camiones = []

    def agregarCamion(self,camion):
        self.__camiones.append(camion)

    def testArchivo(self):
        import csv
        archivo = open('Camiones.csv')
        reader = csv.reader(archivo, delimiter=';')
        for fila in reader:
            ide = fila[0]
            nom = fila[1]
            patente = fila[2]
            marca = fila[3]
            tara = int(fila[4])
            unCamion = Camion(ide,nom,patente,marca,tara)
            self.agregarCamion(unCamion)
        archivo.close()

    def buscaCamion(self,id):
        for indice, camion in enumerate(self.__camiones):
            if camion.getNumero() == id:
                return indice

    def getCamion(self,indice):
        return self.__camiones[indice]

    def __str__(self):
        for camion in self.__camiones:
            s = '{0:6}'.format(str(camion)) + '\n'
        return s