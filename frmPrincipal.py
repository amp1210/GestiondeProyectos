import json
from tabnanny import check
from tkinter import messagebox
import danemunicipio, manejosedes
from msilib.schema import ComboBox
from tkinter import *
from tkinter import ttk
import main, actualizarTabla

class frmMain(Frame):
    def __init__(self, master, *args):
        super().__init__(master, *args)
        self.dbSedes = manejosedes.actualizarSedes()
        self.widgets()
    
    def sedes(self):
        self.informacionsedes = Frame(self.master, bg='blue')
        self.informacionsedes.place(relx=0.915, rely=0.005, relwidth=0.08, relheight=0.99)
        
        self.tablasedes = Frame(self.master, bg='orange')
        self.tablasedes.place(relx=0.005, rely=0.005, relwidth=0.91, relheight=0.99)
        
        self.controlTabla = Frame(self.tablasedes, bg='yellow')
        self.controlTabla.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.05)
        
        self.btnIngresarSede = Button(self.informacionsedes, text='Ingresar sede', width=10, height=2, command=self.nuevasede)
        self.btnIngresarSede.pack(side='top',  padx=5, pady=15)
        
        self.btnActualizarSede = Button(self.informacionsedes, text='Actualizar Sede', width=10, height=2, command=self.actualizarsede)
        self.btnActualizarSede.pack(side='top',  padx=5, pady=15)
        
        #Se Agrega contenido en el FRAME controlTabla, aqui se colocara un boton de buscar (ya sea por municipio o nombre de la sede o codigo dane).
        self.btnClearTreeView = Button(self.controlTabla, text="Clear Tree View", command=self.borrarTabla)
        self.btnClearTreeView.pack()
        self.btnClearTreeView = Button(self.controlTabla, text="Clear Tree View", command=actualizarTabla.mostrarTabla)
        self.btnClearTreeView.pack()
        
        #Se crea un estilo que se aplicara al treeview
        self.styletreeview = ttk.Style()
        self.styletreeview.configure("mystyle.treeview",highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body)
        self.styletreeview.configure("mystyle.treeview.Heading",font=('Calibri', 13,'bold')) # Modify the font of the headings
        self.styletreeview.layout("mystyle.treeview", [('self.styletreeview.self.treeviewSedesarea', {'sticky': 'nswe'})]) # Remove the borders
        
        #Se crea el treeview que mostrara los datos de la base de datos de las sedes
        self.treeviewSedes = ttk.Treeview(self.tablasedes,style="mystyle.treeview",columns=("col1","col2","col3","col4","col5","col6","col7","col8","col9","col10"))
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
        i = 0
        for sede in self.dbSedes:
            i += 1
            num = str(i)
            my_iid = num
            """if check(i):
                color = 'even'
            else:
                color = 'odd'"""
            self.treeviewSedes.insert("",END,text=my_iid,values=sede,iid=my_iid)
        scrollBarTreeView = ttk.Scrollbar(self.treeviewSedes, orient='vertical', command=self.treeviewSedes.yview)
        scrollBarTreeView.pack(side='right', fill='y')
        self.treeviewSedes.configure(yscrollcommand=scrollBarTreeView.set)
        self.treeviewSedes.bind("<Double-1>", self.OnDoubleClick)
    
    def borrarTabla(self):
        self.treeviewSedes.delete(*self.treeviewSedes.get_children())
    
    def OnDoubleClick(self, event):
        item = self.treeviewSedes.selection()[0]
        messagebox.showinfo("Información", self.treeviewSedes.item(item, "text"))
    
    def listmunicipios(self,event):
        if self.subregion.get()=="BAJO CAUCA":
            self.cbxMunicipios.set(" ")
            self.cbxMunicipios.config(values=["Caceres", "Caucasia", "El Bagre", "Nechi", "Taraza", "Zaragoza"])
        if self.subregion.get()=="MAGDALENA MEDIO":
            self.cbxMunicipios.set(" ")
            self.cbxMunicipios.config(values=["Caracoli", "Maceo", "Puerto Berrio", "Puerto Nare", "Puerto Triunfo", "Yondo"])
        if self.subregion.get()=="NORDESTE":
            self.cbxMunicipios.set(" ")
            self.cbxMunicipios.config(values=["Amalfi", "Anori", "Cisneros", "Remedios", "San Roque", "Santo Domingo", "Segovia",
                                            "Vegachi", "Yali", "Yolombo"])
        if self.subregion.get()=="NORTE":
            self.cbxMunicipios.set(" ")
            self.cbxMunicipios.config(values=["Angostura", "Belmira", "Briceno", "Campamento", "Carolina", "Don Matias", "Entrerrios",
                                            "Gomez Plata", "Guadalupe", "Ituango", "San Andres", "San Jose De La Montana", "San Pedro",
                                            "Santa Rosa De Osos", "Toledo", "Valdivia", "Yarumal"])
        if self.subregion.get()=="OCCIDENTE":
            self.cbxMunicipios.set(" ")
            self.cbxMunicipios.config(values=["Abriaqui", "Anza", "Armenia", "Buritica", "Caicedo", "Canasgordas", "Dabeiba", "Ebejico", "Frontino",
                                            "Giraldo", "Heliconia", "Liborina", "Olaya", "Peque",  "Sabanalarga", "San Jeronimo",
                                            "Santafe De Antioquia", "Sopetran", "Uramita"])
        if self.subregion.get()=="ORIENTE":
            self.cbxMunicipios.set(" ")
            self.cbxMunicipios.config(values=["Abejorral", "Alejandria", "Argelia", " Carmen De Viboral", "Cocorna", "Concepcion",
                                            "Granada", "Guarne", "Guatape", "La Ceja", "La Union", "Marinilla",
                                            "Narino", "Penol", "Retiro", "Rionegro", "San Carlos", "San Francisco",
                                            "San Luis", "San Rafael", "San Vicente", "Santuario", "Sonson"])
        if self.subregion.get()=="SUROESTE":
            self.cbxMunicipios.set(" ")
            self.cbxMunicipios.config(values=["Amaga", "Andes", "Angelopolis", "Betania", "Betulia", "Caramanta",
                                            "Ciudad Bolivar", "Concordia", "Fredonia", "Hispania", "Jardin", "Jerico",
                                            "La Pintada", "Montebello", "Pueblorrico", "Salgar", "Santa Barbara", "Tamesis",
                                            "Tarso", "Titiribi", "Urrao", "Valparaiso", "Venecia"])
        if self.subregion.get()=="URABA":
            self.cbxMunicipios.set(" ")
            self.cbxMunicipios.config(values=["Apartado", "Arboletes", "Carepa", "Chigorodo", "Murindo", "Mutata",
                                            "Necocli", "San Juan De Uraba", "San Pedro De Uraba", "Turbo", "Vigia Del Fuerte"])
        if self.subregion.get()=="VALLE DEL ABURRA":
            self.cbxMunicipios.set(" ")
            self.cbxMunicipios.config(values=["Barbosa", "Bello", "Caldas", "Copacabana",  "Envigado", "Girardota",
                                            "Itagui", "La Estrella", "Medellin", "Sabaneta"])
        if self.subregion.get()==" ":
            self.cbxMunicipios.set("")
            self.cbxMunicipios.config(values=" ")
    
    def codigoDaneMunicipio(self,event):
        global numMunicipio
        municipio = self.municipio.get()
        numMunicipio = danemunicipio.denesmunicipio(municipio)
        self.daneMunicipio.set(numMunicipio)
    
    def nuevasede(self):
        self.btnIngresarSede['state'] = DISABLED
        self.btnActualizarSede['state'] = DISABLED
        self.frmSedes = Toplevel()
        self.frmSedes.geometry("{}x{}+{}+{}".format(700, 300, 400, 200))
        self.frmSedes.transient(self.master)
        self.frmSedes.title('Nueva Sede')
        #self.frmSedes.overrideredirect(1)
        self.frmSedes.resizable(0,0)
        self.frmSedes.focus()
        self.frmnuevasede = Frame(self.frmSedes)
        self.frmnuevasede.pack(fill=BOTH, expand=True)
        
        self.codigoDaneSede = StringVar()
        Label(self.frmnuevasede, text="Codigo Dane Sede:", font=self.letraTipo).place(relx=0.025, rely=0.05)
        Entry(self.frmnuevasede, textvariable=self.codigoDaneSede, justify='left', width=15, font= self.letraTipo).place(relx=0.34, rely=0.05)
        
        self.nombreSede = StringVar()
        Label(self.frmnuevasede, text="Nombre Sede:", font=self.letraTipo).place(relx=0.025, rely=0.15)
        Entry(self.frmnuevasede, textvariable=self.nombreSede, justify='left', width=50, font= self.letraTipo).place(relx=0.34, rely=0.15)
        
        self.codigoDaneInstitucion = StringVar()
        Label(self.frmnuevasede, text="Codigo Dane Institucion:", font=self.letraTipo).place(relx=0.025, rely=0.25)
        Entry(self.frmnuevasede, textvariable=self.codigoDaneInstitucion, justify='left', width=15, font= self.letraTipo).place(relx=0.34, rely=0.25)
        
        self.nombreInstitucion = StringVar()
        Label(self.frmnuevasede, text="Nombre Institucion:", font=self.letraTipo).place(relx=0.025, rely=0.35)
        Entry(self.frmnuevasede, textvariable=self.nombreInstitucion, justify='left', width=50, font= self.letraTipo).place(relx=0.34, rely=0.35)
        
        self.departamento = StringVar()
        Label(self.frmnuevasede, text="Departamento:", font=self.letraTipo).place(relx=0.025, rely=0.45)
        ttk.Combobox(self.frmnuevasede, textvariable=self.departamento, value="Antioquia", justify='left', width=25, font= self.letraTipo).place(relx=0.34, rely=0.45)

        self.subregion = StringVar()
        Label(self.frmnuevasede, text="Subregion:", font=self.letraTipo).place(relx=0.025, rely=0.55)
        self.cbxSubregion = ttk.Combobox(self.frmnuevasede, textvariable=self.subregion, value=["BAJO CAUCA", "MAGDALENA MEDIO", "NORDESTE", "NORTE", "OCCIDENTE", "ORIENTE", "SUROESTE", "URABA", "VALLE DEL ABURRA"], justify='left', width=25, font= self.letraTipo)
        self.cbxSubregion.place(relx=0.34, rely=0.55)
        self.cbxSubregion.bind("<<ComboboxSelected>>", self.listmunicipios)
        
        self.municipio = StringVar()
        Label(self.frmnuevasede, text="Municipio:", font=self.letraTipo).place(relx=0.025, rely=0.65)
        self.cbxMunicipios = ttk.Combobox(self.frmnuevasede, textvariable=self.municipio, value=self.listmunicipios, justify='left', width=25, font= self.letraTipo)
        self.cbxMunicipios.place(relx=0.34, rely=0.65)
        self.cbxMunicipios.bind("<<ComboboxSelected>>", self.codigoDaneMunicipio)
        
        self.daneMunicipio = StringVar()
        self.daneMunicipio.set(" ")
        Label(self.frmnuevasede, textvariable=self.daneMunicipio, font=self.letraTipo, width=15).place(relx=0.7, rely=0.65)
        
        self.matricula = StringVar()
        Label(self.frmnuevasede, text="Cantidad de Estudiantes:", font=self.letraTipo).place(relx=0.025, rely=0.75)
        Entry(self.frmnuevasede, textvariable=self.matricula, justify='left', width=10, font= self.letraTipo).place(relx=0.34, rely=0.75)
        
        self.estadoSede = StringVar()
        Label(self.frmnuevasede, text="Estado:", font=self.letraTipo).place(relx=0.50, rely=0.75)
        self.cbxestado = ttk.Combobox(self.frmnuevasede, textvariable=self.estadoSede, value=["Activo","Inactivo"], justify='left', width=10, font= self.letraTipo)
        self.cbxestado.place(relx=0.60, rely=0.75)
        
        self.btnGuardar = Button(self.frmnuevasede, text='Guardar', command=self.guardarnuevasede, font=self.letraTipo)
        self.btnGuardar.place(relx=0.5, rely=0.85)
        
        self.btnSalir = Button(self.frmnuevasede, text='Cerrar', command=self.salirnuevasede,  font=self.letraTipo)
        self.btnSalir.place(relx=0.75, rely=0.85)
    
    def actualizarsede(self):
        self.btnIngresarSede['state'] = DISABLED
        self.btnActualizarSede['state'] = DISABLED
        self.frmActualizarSedes = Toplevel()
        self.frmActualizarSedes.geometry("{}x{}+{}+{}".format(700, 300, 400, 200))
        self.frmActualizarSedes.transient(self.master)
        self.frmActualizarSedes.title('Actualizar Sede')
        self.frmActualizarSedes.resizable(0,0)
        self.frmbuscarsede = Frame(self.frmActualizarSedes, bg='blue')
        self.frmbuscarsede.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.125)
        self.frmactualizarsede = Frame(self.frmActualizarSedes, bg='orange')
        self.frmactualizarsede.place(relx=0.005, rely=0.15, relwidth=0.99, relheight=0.825)
    
        self.buscarDaneSede = StringVar()
        Label(self.frmbuscarsede, text="Codigo Dane Sede:", font=self.letraTipo).place(relx=0.025, rely=0.05)
        Entry(self.frmbuscarsede, textvariable=self.buscarDaneSede, justify='left', width=15, font= self.letraTipo).place(relx=0.25, rely=0.05)
        
        self.btnBuscar = Button(self.frmbuscarsede, text='Buscar', command=self.buscarsede, font=self.letraTipo)
        self.btnBuscar.place(relx=0.5, rely=0.05)
        
        self.nombreSede = StringVar()
        Label(self.frmactualizarsede, text="Nombre Sede:", font=self.letraTipo).place(relx=0.025, rely=0.05)
        #Entry(self.frmnuevasede, textvariable=self.nombreSede, justify='left', width=50, font= self.letraTipo).place(relx=0.34, rely=0.15)
        
        self.codigoDaneInstitucion = StringVar()
        Label(self.frmactualizarsede, text="Codigo Dane Institucion:", font=self.letraTipo).place(relx=0.025, rely=0.15)
        #Entry(self.frmnuevasede, textvariable=self.codigoDaneInstitucion, justify='left', width=15, font= self.letraTipo).place(relx=0.34, rely=0.25)
        
        self.nombreInstitucion = StringVar()
        Label(self.frmactualizarsede, text="Nombre Institucion:", font=self.letraTipo).place(relx=0.025, rely=0.25)
        #Entry(self.frmnuevasede, textvariable=self.nombreInstitucion, justify='left', width=50, font= self.letraTipo).place(relx=0.34, rely=0.35)
        
        self.departamento = StringVar()
        Label(self.frmactualizarsede, text="Departamento:", font=self.letraTipo).place(relx=0.025, rely=0.35)
        #ttk.Combobox(self.frmnuevasede, textvariable=self.departamento, value="Antioquia", justify='left', width=25, font= self.letraTipo).place(relx=0.34, rely=0.45)

        self.subregion = StringVar()
        Label(self.frmactualizarsede, text="Subregion:", font=self.letraTipo).place(relx=0.025, rely=0.45)
        #self.cbxSubregion = ttk.Combobox(self.frmnuevasede, textvariable=self.subregion, value=["BAJO CAUCA", "MAGDALENA MEDIO", "NORDESTE", "NORTE", "OCCIDENTE", "ORIENTE", "SUROESTE", "URABA", "VALLE DEL ABURRA"], justify='left', width=25, font= self.letraTipo)
        #self.cbxSubregion.place(relx=0.34, rely=0.55)
        #self.cbxSubregion.bind("<<ComboboxSelected>>", self.listmunicipios)
        
        self.municipio = StringVar()
        Label(self.frmactualizarsede, text="Municipio:", font=self.letraTipo).place(relx=0.025, rely=0.5525)
        #self.cbxMunicipios = ttk.Combobox(self.frmnuevasede, textvariable=self.municipio, value=self.listmunicipios, justify='left', width=25, font= self.letraTipo)
        #self.cbxMunicipios.place(relx=0.34, rely=0.65)
        #self.cbxMunicipios.bind("<<ComboboxSelected>>", self.codigoDaneMunicipio)
        
        self.daneMunicipio = StringVar()
        self.daneMunicipio.set(" ")
        Label(self.frmactualizarsede, textvariable=self.daneMunicipio, font=self.letraTipo, width=15).place(relx=0.7, rely=0.5525)
        
        self.matricula = StringVar()
        Label(self.frmactualizarsede, text="Cantidad de Estudiantes:", font=self.letraTipo).place(relx=0.025, rely=0.6525)
        #Entry(self.frmnuevasede, textvariable=self.matricula, justify='left', width=10, font= self.letraTipo).place(relx=0.34, rely=0.75)
        
        self.estadoSede = StringVar()
        Label(self.frmactualizarsede, text="Estado:", font=self.letraTipo).place(relx=0.50, rely=0.6525)
        #self.cbxestado = ttk.Combobox(self.frmnuevasede, textvariable=self.estadoSede, value=["Activo","Inactivo"], justify='left', width=10, font= self.letraTipo)
        #self.cbxestado.place(relx=0.60, rely=0.75)
        
        self.btnSalir = Button(self.frmactualizarsede, text='Cerrar', command=self.saliractualizarsede,  font=self.letraTipo)
        self.btnSalir.place(relx=0.75, rely=0.85)

    def guardarnuevasede(self):
        global mtzsede
        self.btnGuardar['state'] = DISABLED
        mtzsede = [self.codigoDaneSede.get(),self.nombreSede.get(),self.codigoDaneInstitucion.get(),
                    self.nombreInstitucion.get(),self.departamento.get(),self.subregion.get(),
                    self.municipio.get(),numMunicipio,self.matricula.get(),self.estadoSede.get()]
        existe = manejosedes.validarSede(mtzsede)
        if existe==False:
            ingresado = manejosedes.guardarSede(mtzsede)
            if ingresado==True:
                self.frmSedes.destroy()
                messagebox.showinfo("Información","Sede Agregada con Exito")
                self.dbSedes = manejosedes.actualizarSedes()
                self.sedes()
            else:
                messagebox.showinfo("Información","No se completo la actualizacion")
                self.sedeexiste()
        else:
            self.frmSedes.destroy()
            self.btnIngresarSede['state'] = NORMAL
            self.btnActualizarSede['state'] = NORMAL
            messagebox.showinfo("Informacion","Sede ya se encuentra registrada")
    
    def buscarsede(self):
        global buscarDaneSede
        buscarDaneSede = self.buscarDaneSede.get()
        danesede = manejosedes.buscarSede(buscarDaneSede)
    
    def actualizarSede(self):
        pass
    
    def serviciosedes(self):
        self.frmServicio = Toplevel()
        self.frmServicio.geometry('600x100')
    
    def interventores(self):
        pass
    
    def salir(self):
        self.master.destroy()
        self.master.quit()
    
    def salirnuevasede(self):
        self.frmSedes.destroy()
        self.btnIngresarSede['state'] = NORMAL
        self.btnActualizarSede['state'] = NORMAL
        
    def saliractualizarsede(self):
        self.frmActualizarSedes.destroy()
        self.btnIngresarSede['state'] = NORMAL
        self.btnActualizarSede['state'] = NORMAL
    
    def ordenVentanas(self):
        if self.estadoVentana == 1:
            if self.nextVentana==2:
                self.frmInformacionBasica.destroy()
                self.estadoVentana = 2
                self.sedes()
            if self.nextVentana == 3:
                #Aqui van los frame que se deben eliminar antes de montar la siguiente ventana.
                self.estadoVentana = 3
                self.serviciosedes()
    
    def menusedes(self):
        self.nextVentana = 2
        self.ordenVentanas()
    
    def menuservicio(self):
        self.nextVentana = 3
        self.ordenVentanas()
    
    def widgets(self):
        self.estadoVentana = 1
        self.letraTipo = ('Arial', 12)
        (numSedes,mtzSubRegion) = manejosedes.cantidadSedes()
        self.cantidad = StringVar()
        self.cantidad.set(numSedes)
        
        #Creacion de Frame para informacion Basica
        self.frmInformacionBasica = Frame(self.master, bg='grey')
        self.frmInformacionBasica.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.frmInformacionSubRegion = Frame(self.frmInformacionBasica, bg='grey')
        self.frmInformacionSubRegion.place(relx=0.005, rely=0.15)
        #Creacion de la barra de menu para las diferentes opciones
        self.menubar = Menu(self.master)
        self.master.config(menu=self.menubar)
        self.sedesmenu = Menu(self.menubar, tearoff=0)
        self.sedesmenu.add_command(label="Sedes", command=self.menusedes, font=self.letraTipo)
        self.sedesmenu.add_separator()
        self.sedesmenu.add_command(label="Salir", command=self.salir, font=self.letraTipo)
        self.serviciosmenu = Menu(self.menubar, tearoff=0)
        self.serviciosmenu.add_command(label="Servicios", font=self.letraTipo, command=self.menuservicio)
        self.visitasmenu =  Menu(self.menubar, tearoff=0)
        self.visitasmenu.add_command(label="Interventores", font=self.letraTipo, command=self.interventores)
        self.menubar.add_cascade(label='Sedes', menu=self.sedesmenu, font=self.letraTipo)
        self.menubar.add_cascade(label='Servicios', menu=self.serviciosmenu, font=self.letraTipo)
        self.menubar.add_cascade(label='Visitas', menu=self.visitasmenu, font=self.letraTipo)
        #Informacion que se muestra en la pantalla inicial
        Label(self.frmInformacionBasica, text='Cantidad de Sedes', font=('Castellar', 18), bg='grey').place(relx=0.005, rely=0.005)
        Label(self.frmInformacionBasica, textvariable=self.cantidad, font=('Castellar', 24), bg='grey').place(relx=0.09, rely=0.05)
        Label(self.frmInformacionSubRegion, text="Cantidad de Sedes Por Subregion", font=('Castellar', 14), bg='grey').grid(column=0, row=0, columnspan=2)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[0][0], font=self.letraTipo, bg='grey').grid(column=0, row=1, sticky=W)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[0][1], font=self.letraTipo, bg='grey').grid(column=1, row=1)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[1][0], font=self.letraTipo, bg='grey').grid(column=0, row=2, sticky=W)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[1][1], font=self.letraTipo, bg='grey').grid(column=1, row=2)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[2][0], font=self.letraTipo, bg='grey').grid(column=0, row=3, sticky=W)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[2][1], font=self.letraTipo, bg='grey').grid(column=1, row=3)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[3][0], font=self.letraTipo, bg='grey').grid(column=0, row=4, sticky=W)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[3][1], font=self.letraTipo, bg='grey').grid(column=1, row=4)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[4][0], font=self.letraTipo, bg='grey').grid(column=0, row=5, sticky=W)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[4][1], font=self.letraTipo, bg='grey').grid(column=1, row=5)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[5][0], font=self.letraTipo, bg='grey').grid(column=0, row=6, sticky=W)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[5][1], font=self.letraTipo, bg='grey').grid(column=1, row=6)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[6][0], font=self.letraTipo, bg='grey').grid(column=0, row=7, sticky=W)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[6][1], font=self.letraTipo, bg='grey').grid(column=1, row=7)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[7][0], font=self.letraTipo, bg='grey').grid(column=0, row=8, sticky=W)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[7][1], font=self.letraTipo, bg='grey').grid(column=1, row=8)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[8][0], font=self.letraTipo, bg='grey').grid(column=0, row=9, sticky=W)
        Label(self.frmInformacionSubRegion, text=mtzSubRegion[8][1], font=self.letraTipo, bg='grey').grid(column=1, row=9)