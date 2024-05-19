import tkinter as tk
from gui import frmestablecimientos, frmmunicipios, frmsubregiones

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

        containerancho, containeralto = container.winfo_screenwidth, container.winfo_screenheight
        print(containerancho)
        print(containeralto)
        print(w)
        print(h)
        frmnavegacion = tk.Frame(container, background='green', width=100, height=h)
        frmnavegacion.place(x=5, y=25, height=675, width=200)

        tk.Label(frmnavegacion, text="Este es la vista de navegacion").pack()

        frmprincipal = tk.Frame(container, background='yellow')
        frmprincipal.place(x=255, y=25, width=1100, height=675)

        tk.Label(frmprincipal, text="Este es la vista principal que cambia").pack()

        #label = tk.Label(container, text="Este es la vista de dashboard").pack()

        """
        self.gui = {}
        for vista in (frmestablecimientos.Establecimientos, frmmunicipios.Municipios, frmsubregiones.Subregiones):
            page_name = vista.__name__
            frame = vista(parent=container, controller=self)
            self.gui[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        print(self.gui)
        for vista in range(len(self.gui)):
            print(vista)
        #self.mostrar_vista("Establecimientos")
        """

    def mostrar_vista(self, page_name):
        frame = self.gui[page_name]
        frame.tkraise()