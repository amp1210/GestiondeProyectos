import tkinter as tk
from tkinter import CENTER, END, ttk

class Establecimientos(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.informacionsedes = tk.Frame(self.master, bg='blue')
        self.informacionsedes.place(relx=0.915, rely=0.005, relwidth=0.08, relheight=0.99)
        
        self.tablasedes = tk.Frame(self.master, bg='orange')
        self.tablasedes.place(relx=0.005, rely=0.005, relwidth=0.91, relheight=0.99)
        
        self.controlTabla = tk.Frame(self.tablasedes, bg='yellow')
        self.controlTabla.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.05)
        
        self.btnIngresarSede = tk.Button(self.informacionsedes, text='Ingresar sede', width=10, height=2)
        self.btnIngresarSede.pack(side='top',  padx=5, pady=15)
        
        self.btnActualizarSede = tk.Button(self.informacionsedes, text='Actualizar Sede', width=10, height=2)
        self.btnActualizarSede.pack(side='top',  padx=5, pady=15)
        
        #Se Agrega contenido en el FRAME controlTabla, aqui se colocara un boton de buscar (ya sea por municipio o nombre de la sede o codigo dane).
        self.btnClearTreeView = tk.Button(self.controlTabla, text="Clear Tree View")
        self.btnClearTreeView.pack()
        
        #Se crea un estilo que se aplicara al treeview
        self.styletreeview = ttk.Style()
        self.styletreeview.configure("mystyle.treeview",highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body)
        self.styletreeview.configure("mystyle.treeview.Heading",font=('Calibri', 13,'bold')) # Modify the font of the headings
        #self.styletreeview.layout("mystyle.treeview", [('self.styletreeview.self.treeviewSedesarea', {'sticky': 'nswe'})]) # Remove the borders
        
        #Se crea el treeview que mostrara los datos de la base de datos de las sedes
        self.treeviewSedes = ttk.Treeview(self.tablasedes, columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"))
        
        #Se crean las columnas que contendran los datos
        self.treeviewSedes.column("#0",width=5)
        self.treeviewSedes.column("col1",width=60)
        self.treeviewSedes.column("col2",width=140)
        self.treeviewSedes.column("col3",width=100)
        self.treeviewSedes.column("col4",width=140)
        self.treeviewSedes.column("col5",width=80)
        self.treeviewSedes.column("col6",width=80)
        self.treeviewSedes.column("col7",width=100)
        self.treeviewSedes.column("col8",width=25,anchor=CENTER)
        self.treeviewSedes.column("col9",width=25,anchor=CENTER)
        self.treeviewSedes.column("col10",width=25,anchor=CENTER)
        #Se colocan nombre a las columnas
        self.treeviewSedes.heading("#0", text=" ")
        self.treeviewSedes.heading("col1", text="Dane Sede")
        self.treeviewSedes.heading("col2", text="Nombre Sede")
        self.treeviewSedes.heading("col3", text="Dane Institucion")
        self.treeviewSedes.heading("col4", text="Nombre Institucion")
        self.treeviewSedes.heading("col5", text="Departamento")
        self.treeviewSedes.heading("col6", text="Subregion")
        self.treeviewSedes.heading("col7", text="Municipio")
        self.treeviewSedes.heading("col8", text="Dane Municipio")
        self.treeviewSedes.heading("col9", text="Matricula")
        self.treeviewSedes.heading("col10", text="Activo")
        #Configuramdo colores de acuerdo si es par o  impar
        """self.treeviewSedes.tag_configure('odd', background='Gray91')
        self.treeviewSedes.tag_configure('even', background='gray')"""
        #Se inserta el treeview al frame.
        self.treeviewSedes.place(relx=0.005, rely=0.06, relwidth=0.99, relheight=0.93)
        #Se realiza un iterante para mosntrar la base de datos.
        """i = 0
        for sede in self.dbSedes:
            i += 1
            num = str(i)
            my_iid = num
            if check(i):
                color = 'even'
            else:
                color = 'odd'
            self.treeviewSedes.insert("",END,text=my_iid,values=sede,iid=my_iid)"""
        scrollBarTreeView = ttk.Scrollbar(self.treeviewSedes, orient='vertical', command=self.treeviewSedes.yview)
        scrollBarTreeView.pack(side='right', fill='y')
        self.treeviewSedes.configure(yscrollcommand=scrollBarTreeView.set)
        self.treeviewSedes.bind("<Double-1>")