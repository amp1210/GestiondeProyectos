import tkinter as tk

class Municipios(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="Esta es la vista de municipios")
        label.pack(pady=10, padx=10)