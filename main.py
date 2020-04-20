from ManejadorCamiones import ListaC
from Cosecha import  Matriz


def opcion0():
    print("Adiós")

def opcion1():
    numero = int(input('Ingrese identificacion:'))
    t = int(listaCosecha.totalCamion(numero-1))
    print('Identificacion: {} Total descargado: {}'.format(numero,t))

def opcion2():
    dia = int(input('Ingrese el dia:'))
    t = listaCosecha.cargaDia(dia-1,listaCamion)
    print(t)

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()


if __name__ == '__main__':

    listaCamion = ListaC()
    listaCamion.testArchivo()

    listaCosecha = Matriz()
    #listaCosecha.cargarArchivo(listaCamion)
    listaCosecha.crearMatriz()

    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print('MENU')
        print("0 Salir")
        print("1. Ingrse el numero de identificacion de un camion para mostrar la cantidad de kilos descargados")
        print("2. Ingrese un dia para conocer las descargas")
        opcion= int(input("Ingrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú
