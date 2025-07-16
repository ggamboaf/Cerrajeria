import tkinter as tk
import calendar
import json
from datetime import date
from tkinter import font

import numpy as np
from tkinter import PhotoImage
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry
from utils.ajuste import ParametroAjuste
from models import models
from views.view_form import *
from views.view_tree import *
from views.view_ajuste import *

from utils.crear import Crear
from models.models import *

class ViewPrincipal:
    def __init__(self, root,user):
        self.menu_vertical_frame = None
        self.Crear = Crear()
        self.ParametroAjuste = ParametroAjuste()
        self.iconos = None
        self.menu_visible = None
        self.menu_vertical = None
        self.subopciones_frame = None
        self.menu_horizontal = None
        self.boton_mostrar_menu = None
        self.fecha_fin = None
        self.fecha_inicio = None
        self.user = user
        self.permisos = json.loads(json.dumps(self.user.permisos))
        self.root = root
        self.root.state('zoomed')
        self.root.title("Ventana Principal")
        self.root.bg = "#dee2e6"
        self.model = None
        self.subMenu = []
        self.opcion = None

        self.frame_contenido = None

        self.modelos_list = Modelo.obtener_datos_menu(self.user)

        self.submenus_activos = []
        self.crear_area_contenido()
        # self.crear_Dashboard()

    def toggle_menu_vertical(self):
        self._ocultar_submenus()
        self.ocultar_todos_los_submenus()
        x = self.boton_mostrar_menu.winfo_rootx() - self.root.winfo_rootx()
        y = self.boton_mostrar_menu.winfo_rooty() - self.root.winfo_rooty() + self.boton_mostrar_menu.winfo_height()
        self.menu_vertical_frame.lift()
        self.menu_vertical_frame.place(x=x, y=y)
        self.submenus_activos.append(self.menu_vertical_frame)

    def mostrar_menu_horizontal(self, opcion):
        if self.opcion is None:
            self.opcion = opcion
        elif self.opcion != opcion:
            self.opcion = opcion

        for widget in self.subopciones_frame.winfo_children():
            widget.destroy()
        if self.menu_vertical_frame is not None:
            self._ocultar_submenus()

        self.ocultar_todos_los_submenus()

        for texto, submenu_items in  self.modelos_list['menu_Parent'].get(opcion, {}).items():
            btn = tk.Button(
                self.subopciones_frame, text=texto, font=("Helvetica", 11),
                fg="white", bg=self.ParametroAjuste.color_menu, relief="flat"
            )
            btn.pack(side="left", padx=5)
            submenu_frame = tk.Frame(self.root, bg=self.ParametroAjuste.color_menu, bd=1, relief="flat")

            for item in submenu_items:
                def accion(op=item):
                    if op != 'Ajustes':
                        modelo = Modelo.obtener_modelo(op)
                        self.mostrar_vista_tree(model=modelo)
                    else:
                        self.mostrar_vista_ajuste()
                    self.mostrar_menu_horizontal(self.opcion)
                    self._ocultar_submenus()

                sub_btn = tk.Button(
                    submenu_frame, text=item, font=("Helvetica", 11),
                    fg="white", bg=self.ParametroAjuste.color_menu, relief="flat", anchor="w",
                    command=accion
                )
                sub_btn.pack(fill="x", padx=10, pady=2)

            def mostrar_submenu(event, frame=submenu_frame, boton=btn):
                self._ocultar_submenus()
                x = boton.winfo_rootx() - self.root.winfo_rootx()
                y = boton.winfo_rooty() - self.root.winfo_rooty() + boton.winfo_height()
                frame.lift()
                frame.place(x=x, y=y)
                self.submenus_activos.append(frame)

            btn.bind("<Button-1>", mostrar_submenu)

    def ocultar_todos_los_submenus(self, event=None):
        self.root.after(10000, self._ocultar_submenus)

    def _ocultar_submenus(self):
        for submenu in self.submenus_activos:
            submenu.place_forget()
        self.submenus_activos.clear()

    def crear_area_contenido(self):
        self.frame_contenido = tk.Frame(self.root, bg="white")
        self.frame_contenido.pack(fill=tk.BOTH, expand=True)
        
        self.menu_horizontal = tk.Frame(self.frame_contenido, bg=self.ParametroAjuste.color_menu, height=40)
        self.menu_horizontal.pack(fill="x", side="top")
        
        self.boton_mostrar_menu = tk.Button(
            self.menu_horizontal, text="☰ Menú", font=("Helvetica", 12),
            fg="white", bg=self.ParametroAjuste.color_menu, relief="flat", command=self.toggle_menu_vertical
        )
        self.boton_mostrar_menu.pack(side="left", padx=10, pady=5)
        
        self.subopciones_frame = tk.Frame(self.menu_horizontal, bg=self.ParametroAjuste.color_menu)
        self.subopciones_frame.pack(fill=tk.BOTH, expand=True)
        
        self.iconos = {}
        for clave, valor in self.modelos_list['menu_Principal'].items():
            self.iconos[clave] = tk.PhotoImage(file=valor)

        self.menu_vertical_frame = tk.Frame(self.root, bg=self.ParametroAjuste.color_menu, bd=1, relief="flat")
        for texto in self.iconos:
            btn = tk.Button(
                self.menu_vertical_frame, text=texto, image=self.iconos[texto], compound="left",
                font=("Helvetica", 12), fg="white", bg=self.ParametroAjuste.color_menu, relief="flat", anchor="w",
                command=lambda t=texto: self.mostrar_menu_horizontal(t)
            )
            btn.pack(fill="x", padx=10, pady=5)
        # Evento global para ocultar submenús
        self.root.bind("<Button-1>", self.ocultar_todos_los_submenus)

    def limpiar_crear_contenido(self):
        if self.frame_contenido is not None:
            self.frame_contenido.destroy()
        self.crear_area_contenido()

    def mostrar_vista_tree(self, valores=None,model=None,navegacion=None,nuevo=True,back=False):
        self.limpiar_crear_contenido()
        if model is not None:
            self.model = model
        else:
            model = self.model
        navegacion = [{
            'funcion': self.mostrar_vista_tree,
             'descripcion': model.descripcion,
            'model': self.model,
        }]
        vista = ViewTree(self.frame_contenido,model=model, on_select=self.mostrar_vista_form,on_click=self.crear_vista_form,navegacion=navegacion,user=self.user)
        vista.pack(fill=tk.BOTH, expand=True)

    def mostrar_vista_form(self, valores=False,model=None,navegacion=None,nuevo=True,back=False):
        self.limpiar_crear_contenido()
        self.mostrar_menu_horizontal(self.opcion)
        self.model = model
        if nuevo:
            navegacion.append({
            'funcion': self.mostrar_vista_tree,
            'descripcion': "Nuevo",
            'model': self.model,
        })
        elif not back:
            navegacion.append({
            'funcion': self.mostrar_vista_form,
            'descripcion': model.descripcion,
            'model': self.model,
        })
        else:
            del navegacion[-1]
        vista = ViewForm(self.frame_contenido,id=valores[0],model= self.model,ir_action_back=self.mostrar_vista_tree,navegacion=navegacion,on_click_create_Model=self.mostrar_vista_form,user=self.user)
        vista.pack(fill=tk.BOTH, expand=True)

    def crear_vista_form(self,navegacion):
        self.limpiar_crear_contenido()
        self.mostrar_menu_horizontal(self.opcion)
        navegacion.append({
            'funcion': self.mostrar_vista_tree,
            'descripcion': "Nuevo",
            'model': self.model,
        })
        vista = ViewForm(self.frame_contenido,model= self.model,ir_action_back=self.mostrar_vista_tree,navegacion=navegacion,user=self.user)
        vista.pack(fill=tk.BOTH, expand=True)

    def mostrar_vista_ajuste(self,model=None):
        self.limpiar_crear_contenido()
        vista = ViewAjuste(self.frame_contenido)
        vista.pack(fill=tk.BOTH, expand=True)

    def crear_MenuPrincipal(self):
        fuente_menu = font.Font(family="Helvetica", size=14)
        menu_Principal = tk.Menu(self.root,font=fuente_menu)
        self.menu_Principal = menu_Principal
        for index, (nombre_menu, opciones) in enumerate(self.modelos_list[0].items()):
            for opcion in opciones:
                submenu_root = tk.Menu(self.root,font=fuente_menu)
                # submenu_root.menu_id = index

                menu_Principal.add_command(label=opcion, command=lambda opt=submenu_root: self.mostrar_MenuParent(opt))
                self.subMenu.append(menu_Principal)
                submenu_root.add_command(label="Regresar a inicio", command=self.regresar_MenuPrincipal)
                submenuDict = next((item for item in self.modelos_list[1]['menu_Parent'] if item.get('menu_Principal') == opcion), None)
                for clave, valor in submenuDict.items():
                    if isinstance(valor, list):
                        menu = tk.Menu(submenu_root, tearoff=0,font=fuente_menu)
                        for index,menuItem in enumerate(valor):
                            modelo = getattr(models, menuItem['modelo'])
                            if menuItem['menu_nombre'] != 'Ajustes':
                                menu.add_command(label=menuItem['menu_nombre'], command=lambda opt=modelo: self.mostrar_vista_tree(model=opt))
                            else:
                                menu.add_command(label=menuItem['menu_nombre'],command=lambda opt=modelo: self.mostrar_vista_ajuste(model=opt))
                            if len(valor) > 1 and index < len(valor)-1:
                                menu.add_separator()
                        submenu_root.add_cascade(label=f"Menú {clave}", menu=menu)

        self.root.config(menu=menu_Principal)

    def mostrar_MenuParent(self,menu_parent):
        self.root.config(menu=menu_parent)

    def regresar_MenuPrincipal(self):
        self.limpiar_crear_contenido()
        # self.crear_Dashboard()
        self.root.config(menu=self.menu_Principal)

    def dummy_action(self):
        self.label.config(text="Funcionalidad en desarrollo...")

    def crear_Dashboard(self):

        frame_superior = ttk.Frame(self.frame_contenido, padding=10)
        frame_superior.pack(side=tk.TOP, fill=tk.X)

        fecha_inicio_default, fecha_fin_default = self.get_month_range()

        ttk.Label(frame_superior, text="Fecha de inicio:").pack(side=tk.LEFT, padx=(0, 5))
        self.fecha_inicio = DateEntry(frame_superior, width=12, background='darkblue',foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.fecha_inicio.set_date(fecha_inicio_default)
        self.fecha_inicio.pack(side=tk.LEFT, padx=(0, 15))

        ttk.Label(frame_superior, text="Fecha final:").pack(side=tk.LEFT, padx=(0, 5))
        self.fecha_fin = DateEntry(frame_superior, width=12, background='darkblue',foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        self.fecha_fin.set_date(fecha_fin_default)
        self.fecha_fin.pack(side=tk.LEFT, padx=(0, 15))

        btn_aplicar = ttk.Button(frame_superior, text="Aplicar", command=self.aplicar_filtro)
        btn_aplicar.pack(side=tk.LEFT)

        x = np.arange(1, 6)
        y = np.random.randint(1, 10, size=5)
        categorias = ['A', 'B', 'C', 'D', 'E']
        valores_pastel = [20, 30, 25, 15, 10]
        colores = ['red', 'green', 'blue', 'orange', 'purple']

        fig, axs = plt.subplots(2, 2, figsize=(10, 6))

        # Gráfico de línea
        axs[0, 0].plot(x, y, marker='o', linestyle='-', color='blue')
        axs[0, 0].set_title("Gráfico de Línea")

        # Gráfico de barras
        axs[0, 1].bar(categorias, y, color='green')
        axs[0, 1].set_title("Gráfico de Barras")

        # Gráfico de pastel
        axs[1, 0].pie(valores_pastel, labels=categorias, colors=colores, autopct='%1.1f%%')
        axs[1, 0].set_title("Gráfico de Pastel")

        # Gráfico de dispersión
        axs[1, 1].scatter(x, y, color='purple')
        axs[1, 1].set_title("Gráfico de Dispersión")

        plt.tight_layout()

        frame_graficos = ttk.Frame(self.frame_contenido)
        frame_graficos.pack(fill=tk.BOTH, expand=True)

        canvas = FigureCanvasTkAgg(fig, master=frame_graficos)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def mostrar_grafico_ampliado(self,titulo, productos, ventas):
        ventana_grafico = tk.Toplevel()
        ventana_grafico.title(titulo)
        ventana_grafico.geometry("600x400")

        fig, ax = plt.subplots()
        ax.bar(productos, ventas, color='cornflowerblue')
        ax.set_title(titulo)
        ax.set_xlabel('Producto')
        ax.set_ylabel('Ventas')

        canvas = FigureCanvasTkAgg(fig, master=ventana_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def get_month_range(self):
        today = date.today()
        first_day = today.replace(day=1)
        last_day = today.replace(day=calendar.monthrange(today.year, today.month)[1])
        return first_day, last_day

    def aplicar_filtro(self):
        inicio = self.fecha_inicio.get_date()
        fin = self.fecha_fin.get_date()

    def mantener_frente(self):
        self.menu_vertical.lift()
        self.root.after(100, self.mantener_frente)

