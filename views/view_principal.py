import tkinter as tk
import calendar
import json
from datetime import date
from idlelib.debugger_r import frametable

from matplotlib.ticker import FuncFormatter

import models.models
from tkinter import font

import numpy as np
from tkinter import PhotoImage
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry
from utils.ajuste import ParametroAjuste
from views.view_form import *
from views.view_tree import *
from views.view_ajuste import *

from utils.crear import Crear
from models.models import *


class ViewPrincipal:
    def __init__(self, root, user):
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
        self.crear_Dashboard()

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

        for texto, submenu_items in self.modelos_list['menu_Parent'].get(opcion, {}).items():
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
        self.frame_contenido.pack(fill="both", expand=True)

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
        self.iconos['MenuPrincipal'] = tk.PhotoImage(file='assets/icon/MenuPrincipal.png')
        btn = tk.Button(
            self.menu_vertical_frame, text="Menu principal", image=self.iconos['MenuPrincipal'], compound="left",
            font=("Helvetica", 12), fg="white", bg=self.ParametroAjuste.color_menu, relief="flat", anchor="w",
            command=self.regresar_MenuPrincipal
        )
        btn.pack(fill="x", padx=10, pady=5)

        for texto in self.iconos:
            if texto != 'MenuPrincipal':
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
            self.frame_contenido = self.frame_contenido.destroy()
        self.crear_area_contenido()

    def mostrar_vista_tree(self, valores=None, model=None, navegacion=None, nuevo=True, back=False):
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
        vista = ViewTree(self.frame_contenido, model=model, on_select=self.mostrar_vista_form,
                         on_click=self.crear_vista_form, navegacion=navegacion, user=self.user)
        vista.pack(fill=tk.BOTH, expand=True)

    def mostrar_vista_form(self, valores=False, model=None, navegacion=None, nuevo=True, back=False):
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
        vista = ViewForm(self.frame_contenido, id=valores[0], model=self.model, ir_action_back=self.mostrar_vista_tree,
                         ir_action_back_delete_model=self.mostrar_vista_form, navegacion=navegacion,
                         on_click_create_Model=self.mostrar_vista_form, user=self.user)
        vista.pack(fill=tk.BOTH, expand=True)

    def crear_vista_form(self, navegacion):
        self.limpiar_crear_contenido()
        self.mostrar_menu_horizontal(self.opcion)
        navegacion.append({
            'funcion': self.mostrar_vista_tree,
            'descripcion': "Nuevo",
            'model': self.model,
        })
        vista = ViewForm(self.frame_contenido, model=self.model, ir_action_back=self.mostrar_vista_tree,
                         navegacion=navegacion, user=self.user)
        vista.pack(fill=tk.BOTH, expand=True)

    def mostrar_vista_ajuste(self, model=None):
        self.limpiar_crear_contenido()
        vista = ViewAjuste(self.frame_contenido)
        vista.pack(fill=tk.BOTH, expand=True)

    def crear_MenuPrincipal(self):
        fuente_menu = font.Font(family="Helvetica", size=14)
        menu_Principal = tk.Menu(self.root, font=fuente_menu)
        self.menu_Principal = menu_Principal
        for index, (nombre_menu, opciones) in enumerate(self.modelos_list[0].items()):
            for opcion in opciones:
                submenu_root = tk.Menu(self.root, font=fuente_menu)

                menu_Principal.add_command(label=opcion, command=lambda opt=submenu_root: self.mostrar_MenuParent(opt))
                self.subMenu.append(menu_Principal)
                submenu_root.add_command(label="Regresar a inicio", command=self.regresar_MenuPrincipal)
                submenuDict = next(
                    (item for item in self.modelos_list[1]['menu_Parent'] if item.get('menu_Principal') == opcion),
                    None)
                for clave, valor in submenuDict.items():
                    if isinstance(valor, list):
                        menu = tk.Menu(submenu_root, tearoff=0, font=fuente_menu)
                        for index, menuItem in enumerate(valor):
                            modelo = getattr(models, menuItem['modelo'])
                            if menuItem['menu_nombre'] != 'Ajustes':
                                menu.add_command(label=menuItem['menu_nombre'],
                                                 command=lambda opt=modelo: self.mostrar_vista_tree(model=opt))
                            else:
                                menu.add_command(label=menuItem['menu_nombre'],
                                                 command=lambda opt=modelo: self.mostrar_vista_ajuste(model=opt))
                            if len(valor) > 1 and index < len(valor) - 1:
                                menu.add_separator()
                        submenu_root.add_cascade(label=f"Menú {clave}", menu=menu)

        self.root.config(menu=menu_Principal)

    def mostrar_MenuParent(self, menu_parent):
        self.root.config(menu=menu_parent)

    def regresar_MenuPrincipal(self):
        self.limpiar_crear_contenido()
        self.crear_Dashboard()

    def dummy_action(self):
        self.label.config(text="Funcionalidad en desarrollo...")

    def crear_Dashboard(self):
        frame_titulo = tk.Frame(self.frame_contenido,bg=self.ParametroAjuste.color_frame)
        frame_titulo.pack(side='top',fill="x")
        label = tk.Label(frame_titulo, text="Dashboard",font=("Arial", 20, "bold"),bg=self.ParametroAjuste.color_frame)
        label.pack()

        dasboards = Modelo.obtener_dashboard()

        style = ttk.Style()
        style.theme_use('default')  # Asegúrate de usar un tema que permita personalización
        style.configure('TNotebook', background=self.ParametroAjuste.color_frame, borderwidth=0)
        style.configure('TNotebook.Tab', background=self.ParametroAjuste.color_frame, padding=10)
        notebook = ttk.Notebook(self.frame_contenido, style='TNotebook')
        notebook.pack(side='top', fill='both', expand=True)

        for dasboard in dasboards:
            tab = tk.Frame(notebook,bg=self.ParametroAjuste.color_frame)
            notebook.add(tab, text=dasboard['index_nombre'])
            model = Modelo.obtener_modelo_nombre(dasboard['modelo'])
            for tipo in dasboard['tipo']:
                tipo_titulo = tk.Frame(tab, bg=self.ParametroAjuste.color_frame)
                tipo_titulo.pack(side='top', fill="x")
                label = tk.Label(tipo_titulo, text=tipo['titulo'], font=("Arial", 15, "bold"),bg=self.ParametroAjuste.color_frame)
                label.pack()

                frame_datos = tk.Frame(tab, bg=self.ParametroAjuste.color_frame)
                frame_datos.pack(side='top', fill="x")

                if tipo['filtro']:
                    self.crear_filtro_dashboard(tipo['filtro_conf'],frame_datos,model,tipo['tabla_conf'],tipo['grafico_conf'])

                if tipo['grafico']:
                    self.crear_grafico_dashboard(tipo['grafico_conf'],frame_datos,model)

                if tipo['tabla']:
                    self.crear_tabla_dashboard(tipo['tabla_conf'],frame_datos,model)

    def crear_filtro_dashboard(self,tipo,tab,model,tabla_conf,grafico_conf):
        metodo = getattr(model, tipo['valores_defecto'])
        valores = metodo()
        filtro_frame = tk.Frame(tab, bg=self.ParametroAjuste.color_frame)
        filtro_frame.pack(side='top', fill="x")
        entrys = []
        if tipo['tipo'] == 'valor_unico':
            tk.Label(filtro_frame, text=tipo['textos'][0], font=("Arial", 12, "bold"), bg=self.ParametroAjuste.color_frame).pack(side=tk.LEFT, padx=(0, 5))
            if tipo['entrada'] == 'entry':
                entry = ttk.Entry(filtro_frame, width=40)
                entry.insert(0, valores[0])
                entry.pack(side=tk.LEFT, padx=(0, 15))
                entrys.append(entry)

        elif tipo['tipo'] == 'rango':
            for index,texto in enumerate(tipo['textos']):
                tk.Label(filtro_frame, text=tipo['textos'][index], font=("Arial", 12, "bold"),bg=self.ParametroAjuste.color_frame).pack(side=tk.LEFT, padx=(0, 5))

                if tipo['entrada'] == 'entry':
                    entry = ttk.Entry(filtro_frame, width=40)
                    entry.insert(0, valores[index])
                    entry.pack(side=tk.LEFT, padx=(0, 15))
                    entrys.append(entry)

                elif tipo['entrada'] == 'date':
                    entry = DateEntry(filtro_frame, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
                    if valores[index]:
                        entry.set_date(valores[index])
                    entry.pack(side=tk.LEFT, padx=(0, 15))
                    entrys.append(entry)

        btn_aplicar = self.Crear.crear_btn(text="Aplicar", ajsutes=self.ParametroAjuste)
        btn_aplicar.config(command=lambda tp=tipo, md=model, enty=entrys, tb=tab, tbl_conf=tabla_conf,grap_conf=grafico_conf: self.accion_filtro(tp, md, enty, tb, tbl_conf,grap_conf))
        btn_aplicar.pack(side=tk.LEFT, padx=10, pady=10, in_=filtro_frame)

        btn_reiniciar = self.Crear.crear_btn(text="Reiniciar", ajsutes=self.ParametroAjuste)
        btn_reiniciar.config(command=lambda tp=tipo, md=model, enty=entrys, tb=tab, tbl_conf=tabla_conf,grap_conf=grafico_conf: self.accion_filtro(tp, md, enty, tb, tbl_conf,grap_conf))
        btn_reiniciar.pack(side=tk.LEFT, padx=10, pady=10, in_=filtro_frame)

        btn_exportar = self.Crear.crear_btn(text="Exportar", ajsutes=self.ParametroAjuste)
        btn_exportar.config(command=lambda tp=tipo, md=model, enty=entrys, tb=tab, tbl_conf=tabla_conf,grap_conf=grafico_conf: self.accion_filtro(tp, md, enty, tb, tbl_conf,grap_conf))
        btn_exportar.pack(side=tk.LEFT, padx=10, pady=10, in_=filtro_frame)





        # frame_inferior = tk.Frame(self.frame_contenido,bg=self.ParametroAjuste.color_frame)
        # frame_inferior.pack(fill="both", expand=True)
        #
        # canvas = tk.Canvas(frame_inferior,bg=self.ParametroAjuste.color_frame)
        # scrollbar = tk.Scrollbar(frame_inferior, orient="vertical", command=canvas.yview)
        # scrollable_frame = tk.Frame(canvas,bg=self.ParametroAjuste.color_frame)
        #
        # def on_canvas_configure(event):
        #     canvas.itemconfig("scrollable_window", width=event.width)
        #
        # def on_frame_configure(event):
        #     canvas.configure(scrollregion=canvas.bbox("all"))
        #
        # scrollable_frame.bind("<Configure>", on_frame_configure)
        # canvas.bind("<Configure>", on_canvas_configure)
        #
        # canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", tags="scrollable_window")
        # canvas.configure(yscrollcommand=scrollbar.set)
        #
        # canvas.pack(side="left", fill="both", expand=True)
        # scrollbar.pack(side="right", fill="y")
        #
        # for _ in range(6):
        #     self.create_scrollable_treeview(scrollable_frame)

    def accion_filtro(self, tp, md,entys,tb,tbl_conf,grap_conf):
        tree = self.obtener_treeview(tb)
        grafico = self.obtener_grafico(tb)
        for item in tree.get_children():
            tree.delete(item)
        if grafico is not None:
            grafico.destroy()
        metodo = getattr(md, tp['valores_defecto'])
        valores = []
        for enty in entys:
            if tp['tipo_valor'] == float:
                valores.append(tp['tipo_valor'](enty.get()))
            elif tp['tipo_valor'] ==  datetime.date:
                valores.append(enty.get_date())
        if tbl_conf:
            self.crear_tabla_dashboard(tbl_conf,tb,md,filtro=True,valor=valores,tree=tree)
        if grap_conf:
            self.crear_grafico_dashboard(grap_conf, tb, md, filtro=True, valor=valores, tree=tree)


    def crear_grafico_dashboard(self,tipo=None,tab=None,model=None,filtro=False,valor=None,tree=None):
        x,y = None, None
        if not filtro:
            metodo = getattr(model, tipo['metodo'])
            x,y = metodo()
        else:
            metodo = getattr(model, tipo['metodo'])
            x,y = metodo(*valor)

        fig2 = plt.Figure(figsize=(4, 2), dpi=100)
        ax2 = fig2.add_subplot(111)
        if tipo['tipo'] == 'barn':
            ax2.barh(x, y)
        elif tipo['tipo'] == 'plot':
            ax2.plot(x, y, marker='o', linestyle='-', color='b')
            fig2.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x):,}'))
            ax2.set_xticks(x)
        canvas2 = FigureCanvasTkAgg(fig2, master=tab)
        canvas2.draw()
        canvas2.get_tk_widget().pack(side="left",fill="both", expand=True)
        fig2.tight_layout()


    def crear_tabla_dashboard(self,tipo=None,tab=None,model=None,filtro=False,valor=None,tree=None):
        df = None
        if not filtro:
            metodo = getattr(model, tipo['metodo'])
            valores = metodo()
            df = pd.DataFrame(valores)
            tree = ttk.Treeview(tab, style="Custom.Treeview", columns=list(df.columns), show="headings")

            vertical = ttk.Scrollbar(tab, orient="vertical", command=tree.yview)
            vertical.pack(side=tk.RIGHT, fill=tk.Y)
            tree.configure(yscrollcommand=vertical.set)

            horizontal = ttk.Scrollbar(tab, orient="horizontal", command=tree.xview)
            horizontal.pack(side=tk.BOTTOM, fill=tk.X)
            tree.configure(xscrollcommand=horizontal.set)
        else:
            metodo = getattr(model, tipo['metodo'])
            valores = metodo(*valor)
            df = pd.DataFrame(valores)

        for columna in df.columns:
            tree.heading(columna, text=columna)
            if columna in ('ID','MODEL'):
                tree.column(columna, width=0, stretch=False)
            else:
                tree.column(columna, width=200, anchor="center")

        for _, row in df.iterrows():
            tree.insert("", "end", iid=row['ID'],tags=row['MODEL'], values=list(row))

        tree.pack(side="right",fill="both", expand=True)
        if tipo['redirige']:
            tree.bind("<<TreeviewSelect>>",self._on_select_row)

    def obtener_treeview(self,frame):
        for widget in frame.winfo_children():
            if isinstance(widget, ttk.Treeview):
                return widget
        return None

    def obtener_grafico(self,frame):
        for widget in frame.winfo_children():
            if isinstance(widget, tk.Canvas):
                return widget
        return None

    def create_scrollable_treeview(self,parent):
        frame_tabla = tk.Frame(parent,bg=self.ParametroAjuste.color_frame)
        frame_tabla.pack(fill="x", expand=True, pady=10, padx=10)

        frame_filtro_titulo = tk.Frame(frame_tabla,bg=self.ParametroAjuste.color_frame)
        frame_filtro_titulo.pack(fill="both", expand=True)
        label = tk.Label(frame_filtro_titulo, text="Aplicación única en ejecución")
        label.pack(fill="both", expand=True)


        fig1 = plt.Figure(figsize=(2, 1), dpi=100)
        ax1 = fig1.add_subplot(111)
        ax1.plot([1, 2, 3], [1, 4, 9])
        ax1.set_title("Gráfico 1")
        canvas1 = FigureCanvasTkAgg(fig1, master=frame_tabla)
        canvas1.draw()
        canvas1.get_tk_widget().pack(side="left",padx=10, pady=10, fill="both", expand=True)

        datos = OrdenVenta.obtener_ordenes_sin_factura()
        df = pd.DataFrame(datos)

        tree = ttk.Treeview(frame_tabla, style="Custom.Treeview", columns=list(df.columns), show="headings")

        vertical = ttk.Scrollbar(frame_tabla, orient="vertical", command=tree.yview)
        vertical.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscrollcommand=vertical.set)

        horizontal = ttk.Scrollbar(frame_tabla, orient="horizontal", command=tree.xview)
        horizontal.pack(side=tk.BOTTOM, fill=tk.X)
        tree.configure(xscrollcommand=horizontal.set)

        for columna in df.columns:
            tree.heading(columna, text=columna)
            if columna == 'ID':
                tree.column(columna, width=0, stretch=False)
            else:
                tree.column(columna, width=200, anchor="center")

        for _, row in df.iterrows():
            tree.insert("", "end", iid=row['ID'], values=list(row))

        tree.pack(side="right",fill="both", expand=True)
        tree.bind("<<TreeviewSelect>>", self._on_select_orden_venta)

    def mantener_frente(self):
        self.menu_vertical.lift()
        self.root.after(100, self.mantener_frente)

    def _on_select_row(self,event):
        widget = event.widget
        selected_item = widget.focus()
        tags = widget.item(selected_item, "tags")
        model = getattr(models, tags[0])
        navegacion = [{
            'funcion': self.regresar_MenuPrincipal,
            'descripcion': "Menu principal",
            'model': model,
        }]
        self.mostrar_vista_form(valores=[int(selected_item)],model=model,nuevo=False,navegacion=navegacion)


