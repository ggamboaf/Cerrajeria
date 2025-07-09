import tkinter as tk
import calendar
import json
from datetime import date
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry

from views.view_form import *
from views.view_tree import *
from views.view_ajuste import *
from models import *

class ViewPrincipal:
    def __init__(self, root,user):
        self.fecha_fin = None
        self.fecha_inicio = None
        self.user = user
        self.permisos = json.loads(json.dumps(self.user.permisos))
        self.root = root
        self.root.state('zoomed')
        self.root.title("Ventana Principal")
        self.root.bg = "#dee2e6"
        self.model = None

        self.frame_contenido = None

        self.menu_Principal = tk.Menu(root)
        self.menu_Ventas = tk.Menu(root)
        self.menu_Compras = tk.Menu(root)
        self.menu_Contabilidad = tk.Menu(root)
        self.menu_Configuracion = tk.Menu(root)

        self.crear_MenuPrincipal()
        self.crear_MenuVentas()
        self.crear_MenuCompras()
        self.crear_MenuContabilidad()
        self.crear_Configuracion()

        self.crear_area_contenido()
        # self.crear_Dashboard()

        self.root.config(menu=self.menu_Principal)

    def crear_area_contenido(self):
        self.frame_contenido = tk.Frame(self.root, bg="white")
        self.frame_contenido.pack(fill=tk.BOTH, expand=True)

    def limpiar_crear_contenido(self):
        if self.frame_contenido is not None:
            self.frame_contenido.destroy()
        self.crear_area_contenido()


    def mostrar_vista_tree(self, valores=None,model=None,navegacion=None,nuevo=True,back=False):
        self.limpiar_crear_contenido()
        self.model = model
        navegacion = [{
            'funcion': self.mostrar_vista_tree,
             'descripcion': model.descripcion,
            'model': self.model,
        }]
        vista = ViewTree(self.frame_contenido,model=model, on_select=self.mostrar_vista_form,on_click=self.crear_vista_form,navegacion=navegacion)
        vista.pack(fill=tk.BOTH, expand=True)

    def mostrar_vista_form(self, valores=False,model=None,navegacion=None,nuevo=True,back=False):
        self.limpiar_crear_contenido()
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
        vista = ViewForm(self.frame_contenido,id=valores[0],model= self.model,ir_action_back=self.mostrar_vista_tree,navegacion=navegacion,on_click_create_Model=self.mostrar_vista_form)
        vista.pack(fill=tk.BOTH, expand=True)

    def crear_vista_form(self,navegacion):
        self.limpiar_crear_contenido()
        navegacion.append({
            'funcion': self.mostrar_vista_tree,
            'descripcion': "Nuevo",
            'model': self.model,
        })
        vista = ViewForm(self.frame_contenido,model= self.model,ir_action_back=self.mostrar_vista_tree,navegacion=navegacion)
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
            self.menu_Principal.add_command(label="Compras", command=self.mostrar_MenuCompras)
        if self.permisos.get("menu_contabilidad", False) or self.permisos.get("admin", False):
            self.menu_Principal.add_command(label="Contabilidad", command=self.mostrar_MenuContabilidad)
        if self.permisos.get("menu_configuracion", False) or self.permisos.get("admin", False):
            self.menu_Principal.add_command(label="Configuración", command=self.mostrar_MenuConfiguracion)

    def crear_MenuVentas(self):
        self.menu_Ventas = tk.Menu(self.root)
        self.menu_Ventas.add_command(label="Regresar a inicio", command=self.regresar_MenuPrincipal)
        ventas_menu = tk.Menu(self.menu_Ventas, tearoff=0)
        if self.permisos.get("menu_venta_nueva", False) or self.permisos.get("admin", False):
            ventas_menu.add_command(label="Ventas", command=lambda: self.mostrar_vista_tree(model=OrdenVenta))
        self.menu_Ventas.add_cascade(label="Menú Ventas", menu=ventas_menu)

    def crear_MenuCompras(self):
        self.menu_Compras = tk.Menu(self.root)
        self.menu_Compras.add_command(label="Regresar a inicio", command=self.regresar_MenuPrincipal)
        ventas_menu = tk.Menu(self.menu_Compras, tearoff=0)
        if self.permisos.get("menu_compra_nueva", False) or self.permisos.get("admin", False):
            ventas_menu.add_command(label="Compras", command=lambda: self.mostrar_vista_tree(model=OrdenCompra))
        self.menu_Compras.add_cascade(label="Menú Compras", menu=ventas_menu)

    def crear_MenuContabilidad(self):
        self.menu_Contabilidad = tk.Menu(self.root)
        self.menu_Contabilidad.add_command(label="Regresar a inicio", command=self.regresar_MenuPrincipal)
        menu_Contabilidad = tk.Menu(self.menu_Contabilidad, tearoff=0)
        if self.permisos.get("menu_contabilidad_clientes_facturas", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Facturas", command=lambda: self.mostrar_vista_tree(model=FacturaCliente))
            menu_Contabilidad.add_separator()
        if self.permisos.get("menu_contabilidad_clientes_productos", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Productos", command=lambda: self.mostrar_vista_tree(model=Producto))
            menu_Contabilidad.add_separator()
        if self.permisos.get("menu_contabilidad_clientes_clientes", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Clientes", command=lambda: self.mostrar_vista_tree(model=Cliente))
        self.menu_Contabilidad.add_cascade(label="Clientes", menu=menu_Contabilidad)

        menu_Contabilidad = tk.Menu(self.menu_Contabilidad, tearoff=0)
        if self.permisos.get("menu_contabilidad_proveedores_facturas", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Facturas", command=lambda: self.mostrar_vista_tree(model=FacturaProveedor))
            menu_Contabilidad.add_separator()
        if self.permisos.get("menu_contabilidad_proveedores_productos", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Productos", command=lambda: self.mostrar_vista_tree(model=Producto))
            menu_Contabilidad.add_separator()
        if self.permisos.get("menu_contabilidad_proveedores_proveedores", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Proveedores", command=lambda: self.mostrar_vista_tree(model=Proveedor))

        self.menu_Contabilidad.add_cascade(label="Proveedores", menu=menu_Contabilidad)

        menu_Contabilidad = tk.Menu(self.menu_Contabilidad, tearoff=0)
        if self.permisos.get("menu_contabilidad_configuracion_impuesto_venta", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Impuestos de venta", command=lambda: self.mostrar_vista_tree(model=ImpuestoVenta))
            menu_Contabilidad.add_separator()
        if self.permisos.get("menu_contabilidad_configuracion_impuesto_compra", False) or self.permisos.get("admin", False):
            menu_Contabilidad.add_command(label="Impuestos de compra",command=lambda: self.mostrar_vista_tree(model=ImpuestoCompra))

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

    def mostrar_MenuCompras(self):
        self.root.config(menu=self.menu_Compras)

    def mostrar_MenuContabilidad(self):
        self.root.config(menu=self.menu_Contabilidad)

    def mostrar_MenuConfiguracion(self):
        self.root.config(menu=self.menu_Configuracion)

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

