import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.autocomplete_entry import AutocompleteEntry
from models import *
from utils.ajuste import ParametroAjuste
from utils.crear import Crear
from models.models import *
from views.view_form_header import *
popup = None

class ViewForm(tk.Frame):
    def __init__(self, master=None,model=None,id=False,ir_action_back=None,navegacion=None,on_click_create_Model=None):
        self.ParametroAjuste = ParametroAjuste()
        self.Crear = Crear()
        super().__init__(master, bg=self.ParametroAjuste.color_fondo)
        self.baseModel = model
        self.modelrel_ids = {}
        self.model = model
        self.labelFrames = []
        self.id = id
        self.ir_back = None
        self.ir_action_back = ir_action_back
        self.on_click_create_Model = on_click_create_Model
        self.navegacion = navegacion
        self.Guardado = False
        self.pack(fill=tk.BOTH, expand=True)
        self.frame_contenido_header = self.crear_area_contenido_header()
        self.canvas, self.frame_contenido = self.crear_area_contenido()
        self.frame_contenido_labelFrame = None
        self.frame_contenido_tab = None
        self.load()

    def load(self):
        if hasattr(self.model, 'auto_Guardar') and  not self.id:
            self.model = self.model.crear_actualizar_desde_dict()
            self.id = self.model.id
        if not self.id:
            self.crear_header()
            self.Crear.crear_form(self.frame_contenido, self.model,load=self.load,on_click_create_Model=self.on_click_create_Model,navegacion=self.navegacion,guardar=self.guardar)
        else:
            self.frame_contenido.destroy()
            self.frame_contenido_header.destroy()
            self.canvas, self.frame_contenido = self.crear_area_contenido()
            self.frame_contenido_header = self.crear_area_contenido_header()
            self.model =  self.baseModel.obtener_con_accion(self.id)
            self.navegacion[-1]['descripcion'] = self.model.nombre
            self.navegacion[-1]['model'] = self.model
            self.crear_header()
            self.Crear.crear_form(self.frame_contenido, self.model,load=self.load,on_click_create_Model=self.on_click_create_Model,navegacion=self.navegacion,guardar=self.guardar)

    def crear_area_contenido_header(self):
        frame_contenido_header = tk.Frame(self, height=100, bg="white")
        frame_contenido_header.pack(side="top", fill="x")
        return frame_contenido_header

    def crear_area_contenido(self):
        canvas = tk.Canvas(self,bg=self.ParametroAjuste.color_frame)
        canvas.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

        scrollbar_y = tk.Scrollbar(self, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar_y.place(relx=0.85, rely=0.15, relheight=0.7)

        canvas.configure(yscrollcommand=scrollbar_y.set)

        frame_contenido = tk.Frame(canvas, bg=self.ParametroAjuste.color_frame)
        canvas_window = canvas.create_window((0, 0), window=frame_contenido, anchor="nw")

        def actualizar_scrollregion(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            canvas.itemconfig(canvas_window, width=canvas.winfo_width())

        frame_contenido.bind("<Configure>", actualizar_scrollregion)

        return canvas, frame_contenido

    def crear_header(self):
        ViewFormHeader(self.frame_contenido_header,self.navegacion,self.model)

    def crear_form(self):
        ViewFormHeader(self.frame_contenido_header,self.navegacion,self.model)

    def guardar(self):
        try:
            self.verificar_fields_required()
            cliente = {}
            sel = self.frame_contenido
            for attr in sel.__dict__:
                if attr.endswith("_field"):
                    valor = getattr(sel, attr).get()
                    entry = getattr(sel, attr)
                    key = attr.replace('_field','')
                    if hasattr(entry,"referencia_id"):
                        if entry.referencia_id != 0:
                         cliente[f"{key}"] = entry.referencia_id
                    else:
                        cliente[f"{key}"] = valor
            if cliente['id'] == '':
                del cliente["id"]
            self.model = self.model.crear_actualizar_desde_dict(cliente)
            self.id = self.model.id
            self.load()
        except ValueError as e:
            return

    def regresar(self):
        if self.ir_action_back:
            self.ir_action_back(self.baseModel)

    def eliminar_model(self):
        self.model.eliminar_datos_models_rel(self.model.id)
        model = self.model
        self.model.delete_instance()
        if self.ir_action_back:
            self.ir_action_back(self.model)

    def ir_back_view(self,event):
        widget = event.widget
        navegacion =  self.navegacion[widget.navegacion_id]
        navegacion['funcion']([navegacion['model'].id],model=navegacion['model'],navegacion=self.navegacion,nuevo=False,back=True)

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







