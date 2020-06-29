from tkinter.constants import *
from tkinter import ttk,Tk,StringVar,font
import requests
import datetime

class Aplicacion():
    __ventana=None
    __nombre=None
    __compra=None
    __venta=None

    def __init__(self):

        self.__ventana = Tk()
        self.__ventana.resizable(0,0)
        self.__ventana.title('Cotizacion del Dolar')
    
        #mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        #mainframe.grid(column=0, row=0, sticky= (N,W,E,S))
        #mainframe.columnconfigure(0, weight=1)
        #mainframe.rowconfigure(0, weight=1)
        #mainframe['borderwidth'] = 2
        #mainframe['relief'] = 'sunken'
        #self.separ1 = ttk.Separator(mainframe, orient=HORIZONTAL)

        self.__nombre= StringVar()
        self.__compra= StringVar()
        self.__venta= StringVar()
        self.__actualizacion= StringVar()

        fuente = font.Font(size=10,weight='bold')

        ttk.Label(self.__ventana, text='Moneda',font=fuente). \
            grid(column=1, row=1, sticky=W)
        ttk.Label(self.__ventana, text='Compra',font=fuente). \
            grid(column=2, row=1, sticky=W)
        ttk.Label(self.__ventana, text='Venta',font=fuente). \
            grid(column=3, row=1, sticky=W)

        f = datetime.datetime.now()
        date='%s/%s/%s %s:%s:%s' % (f.day, f.month, f.year, f.hour, f.minute, f.second)
        self.__actualizacion.set(date)

        complete_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        r = requests.get(complete_url)
        x = r.json()
        cant = len(x)
        fila = 2
        for i in range(cant):
            columna = 1
            nombre = str(x[i]['casa']['nombre'])
            if nombre.find('Dolar') >= 0:
                self.__nombre = nombre
                if (x[i]['casa']['compra'] != 'No Cotiza') or (x[i]['casa']['venta'] != '0'):
                    self.__compra = str(x[i]['casa']['compra'])
                    self.__venta = str(x[i]['casa']['venta'])
                    self.nombre =ttk.Label(self.__ventana, text=self.__nombre). \
                        grid(column=columna, row=fila, sticky=(W, E))
                    columna += 1
                    self.compra =ttk.Label(self.__ventana, text=self.__compra). \
                        grid(column=columna, row=fila, sticky=(W, E))
                    columna += 1
                    self.venta =ttk.Label(self.__ventana, text=self.__venta). \
                        grid(column=columna, row=fila, sticky=(W, E))
                    fila += 1

        ttk.Label(self.__ventana, text='Ultima actualizacion:'). \
            grid(column=1, row=8, sticky=W)
        ttk.Label(self.__ventana, textvariable=self.__actualizacion). \
            grid(column=2, row=8, sticky=(W, E))
        ttk.Button(self.__ventana, text='Actualizar', command=self.actualizar).\
            grid(column=2, row=9, sticky=(W,E))

        for child in self.__ventana.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.__ventana.mainloop()

    def actualizar(self):
        f = datetime.datetime.now()
        date = '%s/%s/%s %s:%s:%s' % (f.day, f.month, f.year, f.hour, f.minute, f.second)
        self.__actualizacion.set(date)

        complete_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        r = requests.get(complete_url)
        x = r.json()
        cant = len(x)
        fila = 2
        for i in range(cant):
            columna = 1
            nombre = str(x[i]['casa']['nombre'])
            if nombre.find('Dolar') >= 0:
                self.__nombre = nombre
                print(nombre)
                if (x[i]['casa']['compra'] != 'No Cotiza') or (x[i]['casa']['venta'] != '0'):
                    self.__compra = str(x[i]['casa']['compra'])
                    self.__venta = str(x[i]['casa']['venta'])
                    self.nombre = ttk.Label(self.__ventana, text=self.__nombre). \
                        grid(column=columna, row=fila, sticky=(W, E))
                    columna += 1
                    self.compra = ttk.Label(self.__ventana, text=self.__compra). \
                        grid(column=columna, row=fila, sticky=(W, E))
                    columna += 1
                    self.venta = ttk.Label(self.__ventana, text=self.__venta). \
                        grid(column=columna, row=fila, sticky=(W, E))
                    fila += 1