import tkinter as tk

import json

from views.view_form import *
from views.view_tree import *
from views.view_ajuste import *
from models.models import *

class ViewPrincipal:
    def __init__(self, root,user):
        self.user = user
        self.permisos = json.loads(json.dumps(self.user.permisos))
        self.root = root
        self.root.state('zoomed')
        self.root.title("Ventana Principal")
        self.root.bg = "#dee2e6"
        self.model = None
        self.data = None

        self.frame_contenido = None

        self.menu_Principal = tk.Menu(root)
        self.menu_Ventas = tk.Menu(root)
        self.menu_Contabilidad = tk.Menu(root)
        self.menu_Configuracion = tk.Menu(root)

        self.crear_MenuPrincipal()
        self.crear_MenuVentas()
        self.crear_MenuContabilidad()
        self.crear_Configuracion()

        self.root.config(menu=self.menu_Principal)

    def crear_area_contenido(self):
        self.frame_contenido = tk.Frame(self.root, bg="white")
        self.frame_contenido.pack(fill=tk.BOTH, expand=True)

    def limpiar_crear_contenido(self):
        if self.frame_contenido is not None:
            self.frame_contenido.destroy()
        self.crear_area_contenido()


    def mostrar_vista_tree(self,model=None,data=None):
        self.limpiar_crear_contenido()
        self.model = model
        self.data = data
        navegacion = [(model,data['tipo'])]
        vista = ViewTree(self.frame_contenido,model=model, on_select=self.mostrar_vista_form,on_click=self.crear_vista_form,data=data,navegacion=navegacion)
        vista.pack(fill=tk.BOTH, expand=True)

    def mostrar_vista_form(self, valores,model=None,data=None,navegacion=None):
        self.limpiar_crear_contenido()
        self.model = model
        navegacion.append((self.model,"Nuevo"))
        vista = ViewForm(self.frame_contenido,id=valores[0],model= self.model,ir_action_back=self.mostrar_vista_tree,data=self.data,navegacion=navegacion)
        vista.pack(fill=tk.BOTH, expand=True)

    def crear_vista_form(self,navegacion):
        self.limpiar_crear_contenido()
        navegacion.append((self.model,"Nuevo"))
        vista = ViewForm(self.frame_contenido,model= self.model,ir_action_back=self.mostrar_vista_tree,data=self.data,navegacion=navegacion)
        vista.pack(fill=tk.BOTH, expand=True)


    def mostrar_vista_ajuste(self,model=None):
        self.limpiar_crear_contenido()
        vista = ViewAjuste(self.frame_contenido)
        vista.pack(fill=tk.BOTH, expand=True)

    def crear_MenuPrincipal(self):
        self.menu_Principal = tk.Menu(self.root)
        if self.permisos.get("menu_ventas", False) or self.permisos.get("admin", False):
            self.menu_Principal.add_command(label="Ventas", command=self.mostrar_MenuVentas)
        if self.permisos.get("menu_compras", False) or self.permisos.get("admin", False):
            self.menu_Principal.add_command(label="Compras", command=self.mostrar_MenuVentas)
        if self.permisos.get("menu_contabilidad", False) or self.permisos.get("admin", False):
            self.menu_Principal.add_command(label="Contabilidad", command=self.mostrar_MenuContabilidad)
        if self.permisos.get("menu_configuracion", False) or self.permisos.get("admin", False):
            self.menu_Principal.add_command(label="Configuración", command=self.mostrar_MenuConfiguracion)

    def crear_MenuVentas(self):
        self.menu_Ventas = tk.Menu(self.root)
        self.menu_Ventas.add_command(label="Regresar a inicio", command=self.regresar_MenuPrincipal)
        ventas_menu = tk.Menu(self.menu_Ventas, tearoff=0)
        ventas_menu.add_command(label="Regresar a inicio", command=self.regresar_MenuPrincipal)
        ventas_menu.add_separator()
        ventas_menu.add_command(label="Nueva venta", command=self.dummy_action)
        ventas_menu.add_separator()
        ventas_menu.add_command(label="Historial de ventas", command=self.dummy_action)
        ventas_menu.add_separator()
        self.menu_Ventas.add_cascade(label="Menú Ventas", menu=ventas_menu)

    def crear_MenuContabilidad(self):
        self.menu_Contabilidad = tk.Menu(self.root)
        self.menu_Contabilidad.add_command(label="Regresar a inicio", command=self.regresar_MenuPrincipal)
        menu_Contabilidad = tk.Menu(self.menu_Contabilidad, tearoff=0)
        if self.permisos.get("menu_contabilidad_clientes_facturas", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Facturas", command=self.dummy_action)
            menu_Contabilidad.add_separator()
        if self.permisos.get("menu_contabilidad_clientes_pagos", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Pagos", command=self.dummy_action)
            menu_Contabilidad.add_separator()
        if self.permisos.get("menu_contabilidad_clientes_productos", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Productos", command=self.dummy_action)
            menu_Contabilidad.add_separator()
        if self.permisos.get("menu_contabilidad_clientes_clientes", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Clientes", command=lambda: self.mostrar_vista_tree(ClienteProveedor,data={'tipo': 'Cliente'}))
        self.menu_Contabilidad.add_cascade(label="Clientes", menu=menu_Contabilidad)

        menu_Contabilidad = tk.Menu(self.menu_Contabilidad, tearoff=0)
        if self.permisos.get("menu_contabilidad_proveedores_facturas", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Facturas", command=self.regresar_MenuPrincipal)
            menu_Contabilidad.add_separator()
        if self.permisos.get("menu_contabilidad_proveedores_pagos", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Pagos", command=self.dummy_action)
            menu_Contabilidad.add_separator()
        if self.permisos.get("menu_contabilidad_proveedores_productos", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Productos", command=self.dummy_action)
            menu_Contabilidad.add_separator()
        if self.permisos.get("menu_contabilidad_proveedores_proveedores", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Proveedores", command=self.dummy_action)

        self.menu_Contabilidad.add_cascade(label="Proveedores", menu=menu_Contabilidad)

        menu_Contabilidad = tk.Menu(self.menu_Contabilidad, tearoff=0)
        if self.permisos.get("menu_contabilidad_configuracion_impuesto_venta", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Impuestos de venta", command=lambda: self.mostrar_vista_tree(Impuesto,data={'tipo': 'Venta'}))
            menu_Contabilidad.add_separator()
        if self.permisos.get("menu_contabilidad_configuracion_impuesto_compra", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Impuestos de compra",command=lambda: self.mostrar_vista_tree(Impuesto,data={'tipo': 'Compra'}))

        self.menu_Contabilidad.add_cascade(label="Configuraciones", menu=menu_Contabilidad)


    def crear_Configuracion(self):
        self.menu_Configuracion = tk.Menu(self.root)
        self.menu_Configuracion.add_command(label="Regresar a inicio", command=self.regresar_MenuPrincipal)
        menu_Configuracion = tk.Menu(self.menu_Configuracion, tearoff=0)
        if self.permisos.get("menu_configuracion_ajuste", False) or self.permisos.get("admin", False):
            menu_Configuracion.add_command(label="Ajustes", command=lambda: self.mostrar_vista_ajuste(Ajuste))
            menu_Configuracion.add_separator()
        if self.permisos.get("menu_configuracion_usuario", False) or self.permisos.get("admin", False):
            menu_Configuracion.add_command(label="Usuarios", command=self.dummy_action)

        self.menu_Configuracion.add_cascade(label="Menú configuración", menu=menu_Configuracion)

    def mostrar_MenuVentas(self):
        self.root.config(menu=self.menu_Ventas)

    def mostrar_MenuContabilidad(self):
        self.root.config(menu=self.menu_Contabilidad)

    def mostrar_MenuConfiguracion(self):
        self.root.config(menu=self.menu_Configuracion)

    def regresar_MenuPrincipal(self):
        self.root.config(menu=self.menu_Principal)

    def dummy_action(self):
        self.label.config(text="Funcionalidad en desarrollo...")

# def show_main_window():
#     root = tk.Tk()
#     app = ViewPrincipal(root,user)
#     root.mainloop()

