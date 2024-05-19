from tkinter import messagebox
from tkinter import *
import frmPrincipal
from gui import frmdashboard
import os, errno

if (__name__ == "__main__"):
    if os.path.isfile(r'listadosedes.csv'):
        #ventana = Tk()
        #w, h = ventana.winfo_screenwidth(), ventana.winfo_screenheight()
        #ventana.geometry("%dx%d+0+0" % (w, h))
        #ventana.state('zoomed')
        #ventana.overrideredirect(0)
        #ventana.resizable(0,0)
        app = frmdashboard.DashBoard()
        app.mainloop()
    else:
        municipios = open('municipios.csv', "w")
        municipios.close()
        listadosedes = open('listadosedes.csv', "w")
        listadosedes.close()
        sedescambios = open('sedescambios.csv', "w")
        sedescambios.close()
        cronograma = open('cronograma.csv', "w")
        cronograma.close()
        liquidacionvisitas = open('liquidacionvisitas.csv', "w")
        liquidacionvisitas.close()
        sedesDocumental = open('documental.csv', "w")
        sedesDocumental.close()
        sedesRemota = open('remotas.csv', "w")
        sedesRemota.close()
        interventores = open('interventores.csv', "w")
        interventores.close()
        visitasdecampo = open('visitascampo.csv', "w")
        visitasdecampo.close()
        
        messagebox.showinfo("Informacion","Ha terminado la instalacion. Reiniciara...")
        quit()