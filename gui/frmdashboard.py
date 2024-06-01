import tkinter as tk
from gui import frmestablecimientos, frmmunicipios, frmsubregiones, frmtrafico

class DashBoard(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Gestion De Proyectos")
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d+0+0" % (w, h))

        container = tk.Frame(self, background='red')
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        frmnavegacion = tk.Frame(container, background='green', width=100, height=h)
        frmnavegacion.place(x=5, y=25, height=675, width=200)

        self.frmprincipal = tk.Frame(container, background='yellow')
        self.frmprincipal.place(x=255, y=25, relwidth=0.85, relheight=0.9)

        btnestablecimientos = tk.Button(frmnavegacion, text='Establecimientos', command=self.establecimiento)
        btnestablecimientos.pack(pady=5)

        btnsubregiones = tk.Button(frmnavegacion, text='SubRegiones')
        btnsubregiones.pack(pady=5)

        btnmunicipios = tk.Button(frmnavegacion, text='Municipios')
        btnmunicipios.pack(pady=5)

        btntrafico = tk.Button(frmnavegacion, text='Trafico', command=self.trafico)
        btntrafico.pack(pady=5)

        #se almacenan las vistas generadas por los usuarios si ya han sido generadas.
        self.gui = {}

    def limpiar_vista(self):
        # Elimina todos los widgets de frmprincipal
        for widget in self.frmprincipal.winfo_children():
            widget.destroy()

    def establecimiento(self):
        page_name = 'Establecimientos'
        self.limpiar_vista()
        frame = frmestablecimientos.Establecimientos(parent=self.frmprincipal, controller=self)
        self.gui[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.mostrar_vista(page_name)

    def trafico(self):
        page_name = 'Trafico'
        self.limpiar_vista()
        frame = frmtrafico.Trafico(parent=self.frmprincipal, controller=self)
        self.gui[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")
        self.mostrar_vista(page_name)

    def mostrar_vista(self, page_name):
        frame = self.gui[page_name]
        frame.tkraise()