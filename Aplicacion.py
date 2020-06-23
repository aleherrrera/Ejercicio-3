from tkinter.constants import *
from tkinter import ttk,Tk,StringVar,font
import requests

class Aplicacion():
    __ventana=None
    __nombre=None
    __compra=None
    __venta=None

    def __init__(self):

        self.__ventana = Tk()
        self.__ventana.resizable(0,0)
        self.__ventana.title('Cotizacion del Dolar')

        mainframe = ttk.Frame(self.__ventana, padding="5 5 12 5")
        mainframe.grid(column=0, row=0, sticky= (N,W,E,S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.separ1 = ttk.Separator(mainframe, orient=HORIZONTAL)

        self.__nombre= StringVar()
        self.__compra= StringVar()
        self.__venta= StringVar()

        fuente = font.Font(size=10,weight='bold')

        ttk.Label(mainframe, text='Moneda',font=fuente). \
            grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, text='Compra',font=fuente). \
            grid(column=2, row=1, sticky=W)
        ttk.Label(mainframe, text='Venta',font=fuente). \
            grid(column=3, row=1, sticky=W)

        complete_url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        r = requests.get(complete_url)
        x = r.json()
        cant = len(x)
        fila = 2
        for i in range(cant):
            columna = 1
            nombre = str(x[i]['casa']['nombre'])
            if nombre.find('Dolar') >= 0:
                self.__nombre=nombre
                if (x[i]['casa']['compra']!='No Cotiza') or (x[i]['casa']['venta']!='0'):
                    self.__compra = str(x[i]['casa']['compra'])
                    self.__venta = str(x[i]['casa']['venta'])
                    ttk.Label(mainframe, text=self.__nombre). \
                        grid(column=columna, row=fila, sticky=(W, E))
                    columna +=1
                    ttk.Label(mainframe, text=self.__compra). \
                        grid(column=columna, row=fila, sticky=(W, E))
                    columna +=1
                    ttk.Label(mainframe, text=self.__venta).\
                        grid(column=columna,row=fila,sticky=(W,E))
                    fila +=1

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.__ventana.mainloop()