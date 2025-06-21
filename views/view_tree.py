import tkinter as tk
from tkinter import ttk, messagebox
from models.models import *
from utils.ajuste import ParametroAjuste
from utils.crear import Crear

class ViewTree(tk.Frame):
    def __init__(self, master=None,model=None,on_select=None,on_click=None,data=None,navegacion=None):
        self.ParametroAjuste = ParametroAjuste()
        self.Crear = Crear()
        super().__init__(master, bg=self.ParametroAjuste.color_fondo)
        self.on_select = on_select
        self.on_click = on_click
        self.model = model
        self.data = data
        self.navegacion = navegacion
        self.pack(fill=tk.BOTH, expand=True)
        self.frame_contenido_header = self.crear_area_contenido_header()
        self.frame_contenido = self.crear_area_contenido()
        self.crear_header()
        self.crear_tabla()


    def crear_area_contenido_header(self):
        frame_contenido_header = tk.Frame(self, height=100, bg=self.ParametroAjuste.color_frame)
        frame_contenido_header.pack(side="top", fill="x")
        return frame_contenido_header

    def crear_area_contenido(self):
        frame_contenido = tk.Frame(self, bg="white")
        frame_contenido.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
        return frame_contenido

    def crear_header(self):
        x = 5
        y = 5
        for navegacion in self.navegacion:
            if x != 5:
                x += 15
            entry = Crear.crear_btn_navegacion(self.Crear, text=navegacion[1], ajsutes=self.ParametroAjuste)
            entry.config(state="disabled")
            entry.place(x=x, y=15,in_=self.frame_contenido_header)

        btn_crear = Crear.crear_btn(self.Crear,text="Crear",ajsutes=self.ParametroAjuste)
        btn_crear.place(x=5, y=50,in_=self.frame_contenido_header)
        btn_crear.config(command=self.crear)

    def crear_tabla(self):
        columnas = self.model.obtener_columnas_para_treeview()

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview.Heading",
                        background="#4caf50",  # Fondo del encabezado
                        foreground="white",  # Color del texto
                        font=("Arial", 14, "bold"))  # Fuente del encabezado

        self.tree = ttk.Treeview(self.frame_contenido,style="Custom.Treeview", columns=columnas, show="headings")
        for columna in columnas:
            field = next(filter(lambda x: x.name == columna, self.model._meta.sorted_fields))
            self.tree.heading(columna, text=f"{field.help_text}")
            if not field.mostrar_Tree:
                self.tree.column(columna, width=0, stretch=False)
            else:
                self.tree.column(columna, width=200, anchor="center")


        datos = self.model.obtener_datos_para_treeview(tipo=self.data['tipo'])

        for fila in datos:
            self.tree.insert("", tk.END, values=fila)

        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.bind("<<TreeviewSelect>>", self._on_select)

    def _on_select(self, event):
        if self.on_select:
            item = self.tree.focus()
            valores = self.tree.item(item, "values")
            self.on_select(valores,self.model,self.data,self.navegacion)

    def crear(self):
        if self.on_click:
            self.on_click(self.navegacion)



