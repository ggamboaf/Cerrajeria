import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.autocomplete_entry import AutocompleteEntry
from models import *
from utils.ajuste import ParametroAjuste
from utils.crear import Crear
from models.models import *
from views.view_form_header import *
from views.view_form_body import *
from views.view_form_popup import *

popup = None

class ViewForm(tk.Frame):
    def __init__(self, master=None,model=None,id=False,ir_action_back=None,navegacion=None,on_click_create_Model=None,user=None,ir_action_back_delete_model=None):
        self.ParametroAjuste = ParametroAjuste()
        self.Crear = Crear()
        super().__init__(master, bg=self.ParametroAjuste.color_fondo)
        self.baseModel = model
        self.modelrel_ids = {}
        self.model = model
        self.labelFrames = []
        self.id = id
        self.user = user
        self.ir_back = None
        self.ir_action_back = ir_action_back
        self.on_click_create_Model = on_click_create_Model
        self.ir_action_back_delete_model = ir_action_back_delete_model
        self.navegacion = navegacion
        self.Guardado = False
        self.pack(fill=tk.BOTH, expand=True)
        self.frame_contenido_header = None
        self.frame_contenido = None
        self.frame_contenido_labelFrame = None
        self.frame_contenido_tab = None
        self.load()

    def load(self):
        self.frame_contenido_header = self.crear_area_contenido_header()
        self.frame_contenido = self.crear_area_contenido()
        if hasattr(self.model, 'auto_Guardar') and  not self.id:
            self.model = self.model.crear_actualizar_desde_dict()
            self.id = self.model.id
        if not self.id:
            self.crear_header()
            self.crear_form()
        else:
            self.model =  self.baseModel.obtener_con_accion(self.id)
            self.navegacion[-1]['descripcion'] = self.model.nombre
            self.navegacion[-1]['model'] = self.model
            self.crear_header()
            self.crear_form()
        self.permiso()

    def permiso(self):
        permiso = self.user.get_permiso(self.model)
        if not permiso['escritura']:
            sel = self.frame_contenido
            for attr in sel.__dict__:
                if attr.endswith("_field"):
                    try:
                        entry = getattr(sel, attr)
                        if isinstance(entry, tk.BooleanVar):
                            entry.boolean.config(state='disabled')
                        else:
                            entry.config(state='disabled')
                    except tk.TclError:
                        pass

    def crear_area_contenido_header(self):
        if self.frame_contenido_header is not None:
            self.frame_contenido_header.destroy()
        frame_contenido_header = tk.Frame(self, height=100, bg="white")
        frame_contenido_header.pack(side="top", fill="x")

        return frame_contenido_header

    def crear_area_contenido(self):
        if self.frame_contenido is not None:
            self.frame_contenido.destroy()

        frame_contenido = tk.Frame(self, bg=self.ParametroAjuste.color_frame)
        frame_contenido.pack(fill="both", expand=True)

        return frame_contenido

    def crear_header(self):
        ViewFormHeader(self.frame_contenido_header,self.navegacion,self.model,self.user,guardar=self.guardar,ir_action_back=self.regresar)

    def crear_form(self):
        ViewFormBody(self.frame_contenido,self.navegacion,self.model,self.user,on_click_create_Model=self.on_click_create_Model,modal_Agregar=self.modal_Agregar)

    def modal_Agregar(self,model):
        ViewFormPopup(self.frame_contenido,model,self.model,self.user,load=self.load)

    def guardar(self):
        try:
            self.verificar_fields_required()
            cliente = {}
            sel = self.obtener_entries_en_frame(self.frame_contenido)
            entries = {enrty.field_nombre: enrty for enrty in sel}
            for campo, entry in entries.items():
                if hasattr(entry, "referencia_id"):
                    if entry.referencia_id != 0:
                        cliente[f"{campo}"] = entry.referencia_id
                else:
                    cliente[f"{campo}"] = entry.get()
            if cliente['id'] == '':
                del cliente["id"]
            self.model = self.model.crear_actualizar_desde_dict(cliente)
            self.id = self.model.id
            self.load()
        except ValueError as e:
            return

    def regresar(self):
        if self.ir_action_back:
            if len(self.navegacion) < 3:
                self.ir_action_back(self.baseModel)
            else:
                model = self.navegacion.copy()
                model.pop()
                self.ir_action_back_delete_model(valores=[model[-1]['model'].id],model=model[-1]['model'],navegacion=self.navegacion,back=True,nuevo=False)

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
        sel = self.obtener_entries_en_frame(self.frame_contenido)
        entries = {enrty.field_nombre: enrty for enrty in sel}
        for field in campos_no_nulos:
            if not isinstance(field,Auto):
                entry = entries.get(field.name)
                if entry.get() == "":
                    msg += f"El campo {field.help_text} es requerido \n"

        if msg != "":
            messagebox.showerror("Error", msg)
            raise ValueError("Campo vacío")

    def obtener_entries_en_frame(self,parent_frame):
        entries_encontrados = []
        for widget in parent_frame.winfo_children():
            if isinstance(widget, ttk.Entry):
                entries_encontrados.append(widget)
            elif isinstance(widget, tk.Checkbutton):
                entries_encontrados.append(widget.boolean_var)
            elif isinstance(widget, tk.Frame) or isinstance(widget, tk.LabelFrame) or isinstance(widget, ttk.LabelFrame):
                # Si el widget es un Frame o LabelFrame, llamamos a la función recursivamente
                entries_encontrados.extend(self.obtener_entries_en_frame(widget))
        return entries_encontrados






