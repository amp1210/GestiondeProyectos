import tkinter as tk
from tkinter import ttk

class Subregiones(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        self.frmtitulo = tk.Frame(self.master, background='orange')
        self.frmtitulo.place(x=0, y=0, relwidth=1, relheight=0.04)

        self.frmcuerpo = tk.Frame(self.master, background='deep sky blue')
        self.frmcuerpo.place(x=0, y=50, relwidth=1, relheight=0.925)

        self.titulo = tk.Label(self.frmtitulo, text="Aqui va el titulo de la tabla")
        self.titulo.pack(padx=5, pady=5, side='left')

        self.btnnuevo = tk.Button(self.frmtitulo, text='+')
        self.btnnuevo.pack(padx=5, pady=5, anchor='w')

        self.tabla = ttk.Treeview(self.frmcuerpo, columns=("col1","col2","col3"))
        self.tabla.grid(row=0, column=0, sticky='nsew')
        
        self.barradesplazamiento = ttk.Scrollbar(self.frmcuerpo, orient='vertical', command=self.tabla.yview)
        self.barradesplazamiento.grid(row=0, column=1, sticky='ns')
        self.tabla.configure(yscrollcommand = self.barradesplazamiento.set)

        # Configurar expansión del Treeview y scrollbar en el frame
        self.frmcuerpo.grid_rowconfigure(0, weight=1)
        self.frmcuerpo.grid_columnconfigure(0, weight=1)