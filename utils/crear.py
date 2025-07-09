import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from utils.ajuste import ParametroAjuste
from utils.generar_reporte import GenerarReporte
from utils.enviar_correo import EnviarCorreo
from models import *

popup = None

class Crear:
    def __init__(self):
        self.guardar = None
        self.frame_contenido_report = None
        self.load = None
        self.navegacion = None
        self.on_click_create_Model = None
        self.master = None
        self.filtered_data = None
        self.labelFrames = []
        self.ParametroAjuste = ParametroAjuste()
        self.model = None
        self.modelCreate = {}
        self.modelPadre = None
        self.frame_contenido_tab = None
        self.frame_contenido_labelFrame = None
        self.frame_contenido = None
        self.frame_contenido_genral = None
        self.datos_ids = {}
        self.ochange_widget = {}

    def crear_btn(self,text,ajsutes,contenedor=None):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure(
            "Custom.TButton",
            font=('Arial', 12, 'bold'),
            background=ajsutes.color_btn_1,
            foreground=ajsutes.color_btn_2,
            borderwidth=0,
            padding=10
        )

        style.map(
            "Custom.TButton",
            background=[("active", ajsutes.color_btn_3)],
            foreground=[("active", ajsutes.color_btn_4)],
            highlightcolor=[("focus", "WHITE")],
            highlightbackground=[("focus", ajsutes.color_btn_1)]
        )
        return ttk.Button(
            contenedor,
            text=text,
            style="Custom.TButton"
        )

    def crear_btn_navegacion(self,text,ajsutes):
        return tk.Button(
            text=text,
            relief="flat",
            borderwidth=0,
            bg=ajsutes.color_frame,
            highlightthickness=0,
            fg="black",
            font=('Arial', 12, 'bold'),
        )

    def crear_form(self,frame_contenido,model,ventana_Emer=False,load=None,on_click_create_Model=None,navegacion=None,guardar=None):
        self.model = model
        self.modelCreate = {}
        if self.modelPadre is None:
            self.modelPadre = model
        if self.load is None:
            self.load = load
        if self.guardar is None:
            self.guardar = guardar
        if self.on_click_create_Model is None:
            self.on_click_create_Model = on_click_create_Model
        if self.navegacion is None:
            self.navegacion = navegacion

        width = 200

        if ventana_Emer:
            self.frame_contenido = frame_contenido
            self.frame_contenido_labelFrame = frame_contenido
            width = 100
        else:
            self.frame_contenido_genral = frame_contenido
            self.frame_contenido = frame_contenido
            if self.model.accion_Config['reporte']:
                self.frame_contenido_report = tk.Frame(self.frame_contenido, bg=self.ParametroAjuste.color_frame)
                self.frame_contenido_report.pack(padx=10, pady=10, fill='both', expand=True)
                if self.model.accion_Config['reporte_Correo']:
                    btn_Enviar_Correo = self.crear_btn(text=self.model.accion_Config['reporte_CorreoDescripcion'], contenedor=self.frame_contenido_report,ajsutes=self.ParametroAjuste)
                    btn_Enviar_Correo.pack(side="left", padx=10)
                    btn_Enviar_Correo.config(command= self.enviar_reporte_Correo)

                if self.model.accion_Config['reporte_Descargar']:
                    btn_Descargar = self.crear_btn(text=self.model.accion_Config['reporte_DescargarDescripcion'], contenedor=self.frame_contenido_report,ajsutes=self.ParametroAjuste)
                    btn_Descargar.pack(side="left", padx=10)
                    btn_Descargar.config(command= self.descargar_Reporte)

                if self.model.accion_Config['crear_Modelo']:
                    btn_Crear_Modelo = self.crear_btn(text=self.model.accion_Config['crear_Modelo_Descripcion'], contenedor=self.frame_contenido_report,ajsutes=self.ParametroAjuste)
                    btn_Crear_Modelo.pack(side="left", padx=10)
                    btn_Crear_Modelo.config(command= self._on_click_create_Model)

                canvas = tk.Canvas(self.frame_contenido, height=1, bg=self.ParametroAjuste.color_frame)
                canvas.pack(fill="both", expand=True)

                canvas.bind("<Configure>",self.dibujar_linea)

            self.frame_contenido_labelFrame = tk.Frame(self.frame_contenido,bg=self.ParametroAjuste.color_frame)
            self.frame_contenido_labelFrame.pack(pady=10)

        self.crear_labelframe()
        campos = self.model._meta.sorted_fields
        espaciador = tk.Frame(self.frame_contenido_labelFrame, width=width, height=100, bg="white")
        espaciador.grid(row=0, column=0)
        espaciador = tk.Frame(self.frame_contenido_labelFrame, width=width, height=100, bg="white")
        espaciador.grid(row=0, column=1)
        for index,field in enumerate(campos):
            self.marco = self.labelFrames[field.numero_Grupo]
            if field.choices:
                self.crear_select(field)
            elif field.index:
                self.crear_autocompletar(field)
            elif isinstance(field, Boolean):
                self.crear_boolean(field)
            elif isinstance(field, Date):
                self.crear_date(field)
            else:
                self.crear_char(field)

        if hasattr(self.model, "models_Rels"):
            self.frame_contenido_tab = tk.Frame(self.frame_contenido,bg=self.ParametroAjuste.color_frame)
            self.frame_contenido_tab.pack(padx=10, pady=10, fill='both', expand=True)
            self.crear_tab()

    def crear_labelframe(self):
        row = 1
        column = 1
        self.labelFrames = []
        for x in range(self.model.cant_grupo):
            style = ttk.Style()
            style.configure("Custom.TLabelframe", background=self.ParametroAjuste.color_frame)
            marco = ttk.LabelFrame(self.frame_contenido_labelFrame, text="Datos", style="Custom.TLabelframe")
            titulo = tk.Label(marco, text=self.model.grupo_nombres[x], fg="black", bg=self.ParametroAjuste.color_frame, font=("Arial", 12, "bold"))
            marco.configure(labelwidget=titulo)
            marco.grid(row=row,column=column, padx=10, pady=10, sticky="nsew")
            self.labelFrames.append(marco)
            if column % 2 == 0:
                row += 1
                column = 1
            else:
                column += 1

    def crear_select(self,field):
        label = tk.Label(self.marco, text=f"{field.help_text}:", bg="white",font=('TkTextFont', 13, 'bold'))
        label.grid(row=field.posicion, column=1, padx=10, pady=5, sticky="w")
        opciones = [op[0] for op in field.choices]
        self.tipo_var = tk.StringVar()
        entry = ttk.Combobox(self.marco, textvariable=self.tipo_var,values=opciones,width=40)
        entry.grid(row=field.posicion,  column=2, padx=10, pady=5, sticky="ew")
        if not field.mostrar_Form:
            entry.grid_remove()
            label.grid_remove()
        if type(self.model.id) is int:
            entry.insert(0, getattr(self.model, field.name))
        setattr(self.frame_contenido, f"{field.name}_field", entry)

    def crear_char(self,field):
        label = tk.Label(self.marco, text=f"{field.help_text}:", bg="white",font=('TkTextFont', 13, 'bold'))
        label.grid(row=field.posicion, column=1, padx=10, pady=5, sticky="w")
        entry = ttk.Entry(self.marco,width=40)
        entry.grid(row=field.posicion, column=2, padx=10, pady=5, sticky="ew")
        entry.field_nombre = field.name
        entry.help_text = field.help_text
        if not field.mostrar_Form:
            entry.grid_remove()
            label.grid_remove()
        if type(self.model.id) is int:
            if getattr(self.model, field.name):
                entry.insert(0, getattr(self.model, field.name))

        if  field.default is not None:
            entry.insert(0, field.default)

        if field.lectura:
            entry.config(state="readonly")

        if field.valor_maximo is not None:
            entry.valor_maximo = field.valor_maximo

        if field.ochange:
            entry.bind("<KeyRelease>", self.ochange)
        setattr(self.frame_contenido, f"{field.name}_field", entry)

    def crear_boolean(self,field):
        label = tk.Label(self.marco, text=f"{field.help_text}:", bg=self.ParametroAjuste.color_frame,font=('TkTextFont', 13, 'bold'))
        label.grid(row=field.posicion, column=1, padx=10, pady=5, sticky="w")
        boolean_var = tk.BooleanVar()
        boolean = tk.Checkbutton(self.marco, variable=boolean_var,bg=self.ParametroAjuste.color_frame)
        boolean.grid(row=field.posicion, column=2, padx=10, pady=5, sticky="ew")
        if not field.mostrar_Form:
            boolean.grid_remove()
            label.grid_remove()
        if type(self.model.id) is int:
            boolean_var.set(getattr(self.model, field.name))
        setattr(self.frame_contenido, f"{field.name}_field", boolean_var)

    def crear_date(self,field):
        label = tk.Label(self.marco, text=f"{field.help_text}:", bg="white",font=('TkTextFont', 13, 'bold'))
        label.grid(row=field.posicion, column=1, padx=10, pady=5, sticky="w")
        entry = DateEntry(self.marco, width=12, background='darkblue',foreground='white', borderwidth=2, date_pattern='yyyy-mm-dd')
        entry.grid(row=field.posicion, column=2, padx=10, pady=5, sticky="ew")
        if not field.mostrar_Form:
            entry.grid_remove()
            label.grid_remove()
        if type(self.model.id) is int:
            if getattr(self.model, field.name):
                entry.set_date(getattr(self.model, field.name))

        if field.lectura:
            entry.config(state="readonly")

        if field.ochange:
            entry.bind("<KeyRelease>", self.ochange)

        setattr(self.frame_contenido, f"{field.name}_field", entry)

    def crear_autocompletar(self,field):
        label = tk.Label(self.marco, text=f"{field.help_text}:", bg="white",font=('TkTextFont', 13, 'bold'))
        label.grid(row=field.posicion, column=1, padx=10, pady=5, sticky="w")
        lista = field.rel_model.obtener_datos_para_atucompleteview()
        entry = ttk.Entry(self.marco,width=40)
        entry.grid(row=field.posicion, column=2, padx=10, pady=5, sticky="ew")
        entry.data_list = lista
        entry.marco = self.marco
        entry.listbox = None
        entry.referencia_id = 0
        entry.ochange = field.ochange
        entry.bind("<KeyRelease>", self.check_input)
        if not field.mostrar_Form:
            entry.grid_remove()
            label.grid_remove()
        if type(self.model.id) is int:
            if getattr(self.model, field.name):
                entry.insert(0, getattr(self.model, field.name).nombre)
                entry.referencia_id = getattr(self.model, field.name).id

        if isinstance(field, ForeignKey):
            if field.rel_model.descripcion == self.modelPadre.descripcion:
                entry.insert(0, self.modelPadre.id)
                entry.referencia_id = self.modelPadre.id

        if field.valor_maximo is not None:
            entry.valor_maximo = field.valor_maximo
        else:
            entry.valor_maximo = None

        setattr(self.frame_contenido, f"{field.name}_field", entry)

    def crear_tab(self):
        datos = self.model.obtener_datos_models_rel(self.model.id)
        style = ttk.Style()
        style.theme_use('default')  # Asegúrate de usar un tema que permita personalización
        style.configure('TNotebook', background=self.ParametroAjuste.color_frame, borderwidth=0)
        style.configure('TNotebook.Tab', background=self.ParametroAjuste.color_frame, padding=10)
        notebook_frame = tk.Frame(self.frame_contenido_tab, bg=self.ParametroAjuste.color_frame)
        notebook_frame.pack(padx=10, pady=10, fill='both', expand=True)
        notebook = ttk.Notebook(notebook_frame, style='TNotebook')
        notebook.pack(side='bottom', fill='both', expand=True)
        for dato in datos:
            columnas = dato['model'].obtener_columnas_para_treeviewrel()
            tab = tk.Frame(notebook,bg=self.ParametroAjuste.color_frame)
            notebook.add(tab, text=dato['tab_Name'])
            self.crear_tabla(tab, dato['records'],columnas,dato['model'],dato['model_name'])

    def crear_tabla(self,tab, records,columnas,model,model_name):
        button_frame = tk.Frame(tab,bg=self.ParametroAjuste.color_frame)
        button_frame.pack(fill='x')

        btn_Agregar = self.crear_btn(text="Agregar",ajsutes=self.ParametroAjuste)
        btn_Agregar.pack(anchor='nw', padx=5, pady=5,in_=button_frame)
        btn_Agregar.config(command=lambda: self.modal_Agregar(model))

        style = ttk.Style()
        style.theme_use("clam")
        # style.configure("Custom.Treeview.Heading",
        #                 background="#4caf50",  # Fondo del encabezado
        #                 foreground="white",  # Color del texto
        #                 font=("Arial", 14, "bold"))  # Fuente del encabezado

        tree = ttk.Treeview(tab,style="Custom.Treeview", columns=columnas, show="headings")

        vertical = ttk.Scrollbar(tab, orient="vertical", command=tree.yview)
        vertical.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscrollcommand=vertical.set)

        horizontal = ttk.Scrollbar(tab, orient="horizontal", command=tree.xview)
        horizontal.pack(side=tk.BOTTOM, fill=tk.X)
        tree.configure(xscrollcommand=horizontal.set)

        for columna in columnas:
            tree.heading(columna, text=columna[0])
            if not columna[1]:
                tree.column(columna, width=0, stretch=False)
            else:
                tree.column(columna, width=200, anchor="center")

        for fila in records:
            tree.insert("", tk.END,iid=fila[0], tags=(model_name), values=fila)

        tree.pack(fill=tk.BOTH, expand=True)

        tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        
    def check_input(self, event):
        widget = event.widget
        typed = widget.get()
        if typed == "":
            self.hide_listbox(widget)
        else:
            self.filtered_data = [
                (id_, name) for id_, name in widget.data_list if typed.lower() in name.lower()
            ]
            if self.filtered_data:
                self.show_listbox(widget)
            else:
                self.hide_listbox(widget)

    def show_listbox(self,widget):
        if widget.listbox:
            widget.listbox.destroy()
        global popup
        if popup:
            popup.destroy()
        popup = tk.Toplevel(self.frame_contenido)
        x = widget.winfo_rootx()
        y = widget.winfo_rooty() + widget.winfo_height()
        popup.geometry(f"200x100+{x}+{y}")

        popup.wm_overrideredirect(True)
        widget.listbox = tk.Listbox(popup)
        widget.listbox.entry = widget
        widget.listbox.bind("<<ListboxSelect>>", self.on_select)
        for _, name in self.filtered_data:
            widget.listbox.insert(tk.END, name)
        widget.listbox.pack(fill=tk.BOTH, expand=True)

        popup.bind("<FocusOut>", lambda e: popup.destroy())
        popup.focus_set()

    def hide_listbox(self,widget):
        if widget.listbox:
            widget.listbox.destroy()
            widget.listbox = None
        if popup:
            popup.destroy()

    def on_select(self, event):
        widget = event.widget
        if widget.entry.listbox:
            index = widget.curselection()[0]
            selected_id, selected_name = self.filtered_data[index]
            widget.entry.delete(0, tk.END)
            widget.entry.insert(0, selected_name)
            widget.entry.referencia_id = selected_id
            if widget.entry.ochange:
                self.ochange(event)
            if widget.entry.valor_maximo is not None:
                self.set_valor_maximo(widget)
            self.hide_listbox( widget.entry)
        if popup:
            popup.destroy()

    def modal_Agregar(self,model):
        try:
            self.verificar_fields_required()
            self.popup = tk.Toplevel(self.frame_contenido.master,bg=self.ParametroAjuste.color_frame)
            self.popup.title("Agregar")
            self.popup.geometry("1200x800")
            self.popup.transient(self.frame_contenido.master)
            self.popup.grab_set()
            self.datosExcel = None
            self.tree = None

            self.popup.update_idletasks()
            width = self.popup.winfo_width()
            height = self.popup.winfo_height()
            x = (self.popup.winfo_screenwidth() // 2) - (width // 2)
            y = (self.popup.winfo_screenheight() // 2) - (height // 2)
            self.popup.geometry(f"{width}x{height}+{x}+{y}")

            fields_frame = tk.Frame( self.popup,bg=self.ParametroAjuste.color_frame)
            fields_frame.pack(fill=tk.BOTH, expand=True)

            button_frame = tk.Frame( self.popup,bg=self.ParametroAjuste.color_frame)
            button_frame.pack(fill='x',pady=20)

            btn_Agregar =  self.crear_btn(text="Agregar",contenedor=button_frame,ajsutes=self.ParametroAjuste)
            btn_Agregar.pack(side="left", padx=10)
            btn_Agregar.config(command= self.agregar_model)

            if type(model.id) is int:
                btn_Eliminar = self.crear_btn(text="Eliminar", contenedor=button_frame, ajsutes=self.ParametroAjuste)
                btn_Eliminar.pack(side="left", padx=10)
                btn_Eliminar.config(command=self.eliminar_model)

            btn_Agregar =  self.crear_btn(text="Cancelar",contenedor=button_frame,ajsutes=self.ParametroAjuste)
            btn_Agregar.pack(side="left", padx=10)
            btn_Agregar.config(command=lambda: self.cancelar(self.popup))


            self.crear_form(fields_frame,model,True)
        except ValueError as e:
            return

    def agregar_model(self):
        try:
            self.verificar_fields_required()
            record = {}
            sel = self.frame_contenido
            for attr in sel.__dict__:
                if attr.endswith("_field"):
                    valor = getattr(sel, attr).get()
                    entry = getattr(sel, attr)
                    key = attr.replace('_field', '')
                    if hasattr(entry, "referencia_id"):
                        if entry.referencia_id != 0:
                            record[f"{key}"] = entry.referencia_id
                    else:
                        record[f"{key}"] = valor
            if record['id'] == '':
                del record["id"]
            self.model = self.model.crear_actualizar_desde_dict(record)
            self.popup.destroy()
            self.load()
        except ValueError as e:
            return

    def eliminar_model(self):
        self.model.delete_instance()
        self.popup.destroy()
        self.load()

    def cancelar(self,popup):
        self.frame_contenido = self.frame_contenido_genral
        popup.destroy()

    def ochange(self,event):
        widget = event.widget
        widget_name = widget._name
        campos = self.model.obtener_campos_ochange()
        sel = self.frame_contenido
        msg = ""
        for attr in sel.__dict__:
            if attr.endswith("_field"):
                if attr in campos:
                    entry = getattr(sel, attr)
                    if hasattr(entry, 'referencia_id'):
                        if entry.referencia_id != 0:
                            self.modelCreate[f"{attr.replace('_field','')}"] = entry.referencia_id
                            # setattr(self.model, attr.replace('_field',''), entry.referencia_id)
                    elif entry.get() != '':
                        if hasattr(entry, "valor_maximo"):
                            if float(entry.get()) <= entry.valor_maximo and isinstance(entry.valor_maximo, float):
                                self.modelCreate[f"{attr.replace('_field', '')}"] = entry.get()
                            else:
                                msg += f"El campo {entry.help_text} supera el valor maximo el cual es {entry.valor_maximo}"
                                break
                        else:
                            self.modelCreate[f"{attr.replace('_field', '')}"] = entry.get()

        if msg == "":
            campos_nulos = [campo for campo in campos if campo.replace('_field', '') not in self.modelCreate]

            if not campos_nulos:
                self.modelCreate = self.model.obtener_resultado_ochange(self.modelCreate)

                for attr in sel.__dict__:
                    if attr.endswith("_field"):
                        entry = getattr(sel, attr)
                        field = getattr(self.model, attr.replace('_field', ''))
                        if not isinstance(field, (int, float, str, bool, bytes)) and isinstance(field,Auto):
                            continue
                        if hasattr(entry, 'referencia_id'):
                            if attr.replace('_field', '') in self.modelCreate:
                                entry.delete(0, tk.END)
                                entry.insert(0, self.modelCreate[f"{attr.replace('_field', '')}"].nombre)
                                entry.referencia_id = self.modelCreate[f"{attr.replace('_field', '')}"].id
                        elif attr.replace('_field', '') in self.modelCreate and attr not in campos:
                            entry.delete(0, tk.END)
                            entry.insert(0, self.modelCreate[f"{attr.replace('_field', '')}"])
        else:
            messagebox.showerror("Error", msg)

    def on_tree_select(self,event):
        widget = event.widget
        selected_item = widget.focus()  # Obtiene el iid del ítem seleccionado
        values = widget.item(selected_item, "values")
        tags = widget.item(selected_item, "tags")
        model = getattr(models.models, tags[0])
        model = model.get(model.id == int(selected_item))
        self.modal_Agregar(model)

    def dibujar_linea(self,event):
        canvas = event.widget
        canvas.delete("linea")  # Elimina la línea anterior
        ancho = event.width
        canvas.create_line(0, 1, ancho, 1, fill="black", width=3, tags="linea")

    def enviar_reporte_Correo(self):
        return EnviarCorreo.enviar_correo_reporte(EnviarCorreo(),self.model)

    def descargar_Reporte(self):
        return GenerarReporte.descargar_plantilla_pdf(GenerarReporte(),self.model)

    def set_valor_maximo(self,widget):
        campos = widget.entry.valor_maximo.split(",")
        valor_maximo = self.model.obtener_valor_maximo(widget.entry.referencia_id)
        sel = self.frame_contenido
        for campo in campos:
            entry = getattr(sel, f"{campo}_field")
            entry.valor_maximo = valor_maximo

    def _on_click_create_Model(self):
        if self.on_click_create_Model:
            model = self.model.buscar_crear_model()
            valores = [model.id]
            self.on_click_create_Model(valores,model,self.navegacion,nuevo=False)

    def verificar_fields_required(self):
        msg = ""
        campos_no_nulos = [campo for nombre, campo in self.model._meta.fields.items()if campo.null is False or campo.required]
        sel = self.frame_contenido
        for field in campos_no_nulos:
            if not isinstance(field,Auto):
                entry = getattr(sel, f"{field.name}_field")
                if entry.get() == "":
                    msg += f"El campo {field.help_text} es requerido \n"

        if msg != "":
            messagebox.showerror("Error", msg)
            raise ValueError("Campo vacío")
        else:
            if not type(self.modelPadre.id) is int:
                self.guardar()






