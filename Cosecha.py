from ManejadorCamiones import ListaC
class Matriz:

    __matriz = []

    def __init__(self):
        self.__matriz = []

    def cargarArchivo(self,lista):
        d = int(input('Ingrese la cantidad de dias:'))
        c = int(input('Ingrgese la cantidad de camiones:'))
        for i in range(d):
            self.__matriz.append([0]*c)

        dia = int(input('Ingrese dia a cargar(0 para terminar):'))
        while dia != 0:
            if dia <= d:
                camion = int(input('Ingrese camion a cargar(0 para terminar):'))
                while camion != 0:
                    if camion <= c:
                        carga = int(input('Ingrese carga en kilogramos:'))
                        unCamion = lista.getCamion(camion-1)
                        carga = carga - unCamion.getTara()
                        self.__matriz[dia-1][camion-1] += carga
                    else:
                        print('Numero de camion incorrecto')
                    camion = int(input('Ingrese camion a cargar(0 para terminar):'))
            else:
                print('Dia ingresado incorrecto')
            dia = int(input('Ingrese dia a cargar(0 para terminar):'))

        import csv
        m = self.__matriz
        with open ('Cosechas.csv','w') as csvfile:
            writer = csv.writer(csvfile)
            for row in m:
                writer.writerow(row)

    def crearMatriz(self):
        import numpy as np
        self.__matriz = np.genfromtxt('Cosechas.csv', delimiter = ',')
        #print(self.__matriz)

    def totalCamion(self,numero):
        total = 0
        m = self.__matriz
        for i in range(len(self.__matriz)):
            total += m[i][numero]
        return total

    def cargaDia(self,dia,lista):
        m = self.__matriz
        s = 'PATENTE CONDUCTOR CANTIDAD DE KILOS\n'
        for i in range(len(m)):
            carga = m[dia][i]
            unCamion = lista.getCamion(i)
            p = unCamion.getPatente()
            n = (unCamion.getNombre())
            t= str(unCamion)
            s += '{}'.format(t) + '{0:16}'.format(carga) + '\n'
        return s
