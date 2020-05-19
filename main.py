import csv
from ManejadorPersonas import ListaPersona
from ManejadorTaller import ArreTalleres
from ManejadorInscripcion import ArreInscripciones

def opcion0():
    print("Adiós")

def opcion1():
    Talleres.MostrarTalleres()
    persona=Talleres.InscribirPersona(Inscripciones)
    Personas.cargarPersona(persona)

def opcion2():
    dni=str(input('Ingresar DNI: '))
    id=Personas.BuscarPersona(dni)
    if id != None:
        Talleres.Nom_Monto(id,dni)
    else:
        print('La persona con DNI:{} no esta inscripta'.format(dni))

def opcion3():
    Talleres.ListarPersonas()

def opcion4():
    dni=str(input('Ingresar DNI: '))
    id=Personas.BuscarPersona(dni)
    if id!=None:
        Talleres.RegistrarPago(id,dni)
        Inscripciones.Pagar(dni)
    else:
        print('La persona con DNI:{} no esta inscripta'.format(dni))

def opcion5():
    lista=Inscripciones.generarLista()

    archivo=open('Inscriptos.csv','w')
    with archivo:
        writer=csv.writer(archivo)
        writer.writerows(lista)
    print('Inscriptos guardados')

switcher = {
    0: opcion0,
    1: opcion1,
    2: opcion2,
    3: opcion3,
    4: opcion4,
    5: opcion5
}

def switch(argument):
    func = switcher.get(argument, lambda: print("Opción incorrecta"))
    func()

if __name__ == '__main__':

    Personas=ListaPersona()
    Talleres=ArreTalleres(3,5)
    Inscripciones=ArreInscripciones(0,5)

    Talleres.CargarTaller()

    bandera = False # pongo la bandera en falso para forzar a que entre al bucle la primera vez
    while not bandera:
        print("")
        print("0 Salir")
        print("1. Inscribir una persona")
        print("2. Consultar inscripcion de una persona")
        print("3. Consultar inscriptos en un taller")
        print('4. Registrar pago')
        print('5. Guardar inscripciones')
        opcion= int(input("\nIngrese una opción: "))
        switch(opcion)
        bandera = int(opcion)==0 # Si lee el 0 cambia la bandera a true y sale del menú