from tkinter import messagebox
import tkinter as tk
from models.models import Auto
from utils.ajuste import ParametroAjuste
from utils.crear import Crear


class ViewFormBody(tk.Frame):
    def __init__(self,master=None,navegacion=None,model=None):
        self.ParametroAjuste = ParametroAjuste()
        self.Crear = Crear()
        super().__init__(master, bg=self.ParametroAjuste.color_fondo)
        self.frame_contenido_header = master
        self.navegacion = navegacion
        self.model = model
        self.crear_header()