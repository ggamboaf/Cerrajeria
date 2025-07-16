import shutil
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from models import *
from models.models import Auto, ForeignKey
from utils.ajuste import ParametroAjuste
from utils.crear import Crear
import pandas as pd
import shutil

class ViewTree(tk.Frame):
    def __init__(self, master=None,model=None,on_select=None,on_click=None,navegacion=None,user=None):
        self.entry_filtro = None
        self.frame_filtro = None
        self.tree = None
        self.ParametroAjuste = ParametroAjuste()
        self.Crear = Crear()
        super().__init__(master, bg=self.ParametroAjuste.color_fondo)
        self.on_select = on_select
        self.on_click = on_click
        self.model = model
        self.user = user
        self.navegacion = navegacion
        self.items = None
        self.filtros_activos = {}
        self.pack(fill=tk.BOTH, expand=True)
        self.frame_contenido_header = self.crear_area_contenido_header()
        self.frame_contenido = self.crear_area_contenido()
        self.load()

    def load(self):
        if hasattr(self,"frame_contenido_header"):
            self.frame_contenido_header.destroy()
            self.frame_contenido_header = self.crear_area_contenido_header()
        if hasattr(self,"frame_contenido"):
            self.frame_contenido.destroy()
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
        permiso = self.user.get_permiso(self.model)
        self.frame_contenido_header.lower()
        frame_labels = tk.Frame(self.frame_contenido_header,bg=self.ParametroAjuste.color_frame)
        frame_labels.pack(fill=tk.BOTH,pady=10)
        frame_labels.lower()
        count = len(self.navegacion)-1
        for index,navegacion in enumerate(self.navegacion):
            entry = Crear.crear_btn_navegacion(self.Crear, text=navegacion['descripcion'], ajsutes=self.ParametroAjuste)
            if index == count:
                entry.config(state="disabled")
            entry.pack(side="left", padx=10, in_=frame_labels)

        btn_agregar_filtro = Crear.crear_btn(self.Crear, text="+", ajsutes=self.ParametroAjuste)
        btn_agregar_filtro.pack(side="right",  padx=10, pady=0, in_=frame_labels)
        btn_agregar_filtro.config(command=self.agregar_filtro,width=1)
        self.entry_filtro = ttk.Entry(frame_labels,width=20)
        self.entry_filtro.pack(side="right", padx=0, pady=0)
        label = tk.Label(frame_labels, text="Agregar filtro", bg=self.ParametroAjuste.color_frame, font=('Arial', 12, 'bold'),fg='#4f4e4d')
        label.pack(side="right", padx=0, pady=0)



        frame_buttons = tk.Frame(self.frame_contenido_header,bg=self.ParametroAjuste.color_frame)
        frame_buttons.pack(fill=tk.BOTH,pady=10)

        if permiso['creacion']:
            btn_crear = Crear.crear_btn(self.Crear,text="Crear",ajsutes=self.ParametroAjuste)
            btn_crear.pack(side="left", padx=10, in_=frame_buttons)
            btn_crear.config(command=self.crear)

        btn_crear = Crear.crear_btn(self.Crear,text="Importar",ajsutes=self.ParametroAjuste)
        btn_crear.pack(side="left", padx=10,in_=frame_buttons)
        btn_crear.config(command=self.importar)

        btn_crear = Crear.crear_btn(self.Crear,text="Exportar",ajsutes=self.ParametroAjuste)
        btn_crear.pack(side="left", padx=10, in_=frame_buttons)
        btn_crear.config(command=self.exportar)

        self.frame_filtro = frame_buttons

    def crear_tabla(self):
        df = pd.DataFrame(self.model.obtener_datos_para_treeview())

        style = ttk.Style()
        style.theme_use("clam")

        self.tree = ttk.Treeview(self.frame_contenido,style="Custom.Treeview", columns=list(df.columns), show="headings")

        vertical = ttk.Scrollbar(self.frame_contenido, orient="vertical", command=self.tree.yview)
        vertical.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=vertical.set)

        horizontal = ttk.Scrollbar(self.frame_contenido, orient="horizontal", command=self.tree.xview)
        horizontal.pack(side=tk.BOTTOM, fill=tk.X)
        self.tree.configure(xscrollcommand=horizontal.set)

        for columna in df.columns:
            field = next(filter(lambda x: x.help_text == columna, self.model._meta.sorted_fields))
            self.tree.heading(columna, text=f"{field.help_text}")
            if not field.mostrar_Tree:
                self.tree.column(columna, width=0, stretch=False)
            else:
                self.tree.column(columna, width=200, anchor="center")

        for _, row in df.iterrows():
            self.tree.insert("", "end", values=list(row))

        self.tree.pack(fill=tk.BOTH, expand=True)

        self.tree.bind("<<TreeviewSelect>>", self._on_select)

    def _on_select(self, event):
        if self.on_select:
            item = self.tree.focus()
            valores = self.tree.item(item, "values")
            self.on_select(valores,self.model,self.navegacion,nuevo=False)

    def crear(self):
        if self.on_click:
            self.on_click(self.navegacion)

    def importar(self):
        self.popup = tk.Toplevel(self.master)
        self.popup.title("Importar Excel")
        self.popup.geometry("1000x800")
        self.popup.transient(self.master)
        self.popup.grab_set()
        self.datosExcel = None
        self.tree = None

        self.popup.update_idletasks()
        width = self.popup.winfo_width()
        height = self.popup.winfo_height()
        x = (self.popup.winfo_screenwidth() // 2) - (width // 2)
        y = (self.popup.winfo_screenheight() // 2) - (height // 2)
        self.popup.geometry(f"{width}x{height}+{x}+{y}")


        btn_seleccionar = Crear.crear_btn(self.Crear,contenedor=self.popup,text="Seleccionar archivo Excel",ajsutes=self.ParametroAjuste)
        btn_seleccionar.pack(pady=10,side=tk.TOP)
        btn_seleccionar.config(command=self.seleccionar_archivo)

        btn_descargar = Crear.crear_btn(self.Crear,contenedor=self.popup,text="Descargar plantilla Excel",ajsutes=self.ParametroAjuste)
        btn_descargar.pack(pady=10,side=tk.TOP)
        btn_descargar.config(command=self.descargar_archivo)

        self.btn_importar  =  Crear.crear_btn(self.Crear,contenedor=self.popup,text="Importar datos",ajsutes=self.ParametroAjuste)
        self.btn_importar.config(command=self.importar_datos)


        self.tree = ttk.Treeview(self.popup)
        self.tree.pack(fill=tk.BOTH, expand=True)

    def seleccionar_archivo(self):
        file_path = filedialog.askopenfilename(defaultextension=".xlsx",filetypes=[("Archivos Excel", "*.xlsx")],title="Guardar como")
        if file_path:
            self.datosExcel = pd.read_excel(file_path, engine='openpyxl')
            self.mostrar_tabla()

    def descargar_archivo(self):
        archivo_origen = f"plantillas/excel/{self.model.plantilla_Name}"
        archivo_destino = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx *.xls")])
        if archivo_destino:
            try:
                shutil.copy(archivo_origen, archivo_destino)
                messagebox.showinfo("Éxito", "Archivo descargado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo descargar el archivo:\n{e}")

    def mostrar_tabla(self):
        if self.tree:
            self.tree.destroy()

        self.tree = ttk.Treeview(self.popup)
        self.tree["columns"] = list(self.datosExcel.columns) + ["Eliminar"]
        self.tree["show"] = "headings"
        self.tree.pack(fill=tk.BOTH, expand=True)

        for column in self.tree["columns"]:
            self.tree.heading(column, text=column)
            if column == "Eliminar":
                self.tree.column(column, width=80, anchor="center")
            else:
                self.tree.column(column, width=100)

        for index, row in self.datosExcel.iterrows():
            self.tree.insert("", "end", iid=index, values=list(row) + ["🗑"])

        self.tree.pack(pady=20)

        self.tree.bind("<Button-1>", self.eliminar_fila)

        self.btn_importar.pack(pady=10, side=tk.TOP)

    def eliminar_fila(self, event):
        region = self.tree.identify_region(event.x, event.y)
        if region == "cell":
            column = self.tree.identify_column(event.x)
            column_index = int(column.replace("#", "")) - 1
            if column_index == len(self.datosExcel.columns):
                selected_item = self.tree.identify_row(event.y)
                if selected_item:
                    self.tree.delete(selected_item)
                    self.datosExcel = self.datosExcel.drop(index=int(selected_item)).reset_index(drop=True)
                    self.mostrar_tabla()

    def importar_datos(self):
        columnas = self.tree["columns"]
        columnas = tuple(item for item in columnas if item != 'Eliminar')
        datos = []
        for item_id in self.tree.get_children():
            valores = self.tree.item(item_id)["values"]
            fila = dict(zip(columnas, valores))
            datos.append(fila)

        msg = ""
        for producto in datos:
            for clave, valor in list(producto.items()):
                field = next((campo for campo in self.model._meta.fields.values() if getattr(campo, 'help_text', None) == clave),None)
                if not issubclass(type(field), Auto) and not isinstance(field, ForeignKey):
                    producto[f"{field.name}"] = producto.pop(clave)
                elif isinstance(field, ForeignKey):
                    try:
                        registro = field.rel_model.get(getattr(field.rel_model, field.campo_busqueda) == valor)
                        producto.pop(clave)
                        producto[f"{field.name}"] = registro.id
                    except field.rel_model.DoesNotExist:
                        msg += f"¡No se encontro  {field.rel_model.descripcion} con el valor {valor}! \n"

        if msg != "":
            messagebox.showerror("Error", msg)
        else:
            [self.model.crear_actualizar_desde_dict(registro) for registro in datos]

        self.popup.destroy()
        self.load()

    def exportar(self):
        datos = self.model.obtener_datos_para_exportar()
        df = pd.DataFrame(datos)

        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",filetypes=[("Archivos Excel", "*.xlsx")],title="Guardar como",initialfile=f"{self.model.xlsx_Name}")

        if file_path:
            df.to_excel(file_path, index=False)
            messagebox.showinfo("Éxito", f"Datos exportados correctamente a:\n{file_path}")

    def aplicar_filtros(self):
        if self.filtros_activos:
            if self.items is None:
                self.items = self.tree.get_children()
            for item in  self.items:
                valores = self.tree.item(item, "values")
                texto = " ".join(valores).lower()
                visible = any(f.lower() in texto for f in self.filtros_activos.values())
                if visible:
                    self.tree.reattach(item, '', 'end')
                else:
                    self.tree.detach(item)

    def agregar_filtro(self):
        texto = self.entry_filtro.get().strip()
        if texto and texto not in self.filtros_activos.values():
            clave = f"filtro_{len(self.filtros_activos)}"
            if self.filtros_activos:
                self.desaplicar_filtros()
            self.filtros_activos[clave] = texto
            self.mostrar_filtros()
            self.aplicar_filtros()
        self.entry_filtro.delete(0, tk.END)

    def eliminar_filtro(self,clave):
        if clave in self.filtros_activos:
            del self.filtros_activos[clave]
            self.mostrar_filtros()
            self.desaplicar_filtros()
            self.aplicar_filtros()

    def mostrar_filtros(self):
        for widget in self.frame_filtro.winfo_children():
            widget.destroy()
        for clave, texto in self.filtros_activos.items():
            subframe = tk.Frame(self.frame_filtro, bd=1, relief="solid", padx=5, pady=2)
            tk.Label(subframe, text=texto).pack(side="right")
            tk.Button(subframe, text="❌", command=lambda c=clave: self.eliminar_filtro(c)).pack(side="right")
            subframe.pack(side="right", padx=5)

    def desaplicar_filtros(self):
        for item in  self.items:
            self.tree.reattach(item, '', 'end')