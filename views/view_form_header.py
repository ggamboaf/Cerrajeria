from tkinter import messagebox
import tkinter as tk
from models.models import Auto
from utils.ajuste import ParametroAjuste
from utils.crear import Crear


class ViewFormHeader(tk.Frame):
    def __init__(self,master=None,navegacion=None,model=None,user=None):
        self.ParametroAjuste = ParametroAjuste()
        self.Crear = Crear()
        super().__init__(master, bg=self.ParametroAjuste.color_fondo)
        self.frame_contenido_header = master
        self.navegacion = navegacion
        self.user = user
        self.model = model
        self.crear_header()

    def crear_header(self):
        permiso = self.user.get_permiso(self.model)
        self.frame_contenido_header.lower()
        frame_labels = tk.Frame(self.frame_contenido_header, bg=self.ParametroAjuste.color_frame)
        frame_labels.pack(fill=tk.BOTH, pady=10)
        count = len(self.navegacion) - 1
        for index, navegacion in enumerate(self.navegacion):
            entry = Crear.crear_btn_navegacion(self.Crear, text=navegacion['descripcion'], ajsutes=self.ParametroAjuste)
            entry.pack(side="left", padx=10, in_=frame_labels)
            if index == count:
                entry.config(state="disabled")
            else:
                entry.navegacion_id = index
                entry.bind("<Button-1>", self.ir_back_view)
                label = tk.Label(frame_labels, text="/", bg=self.ParametroAjuste.color_frame,
                                 font=('Arial', 12, 'bold'), fg='#4f4e4d')
                label.pack(side="left", padx=10)
            setattr(frame_labels, f"{index}_field", entry)

        frame_buttons = tk.Frame(self.frame_contenido_header, bg=self.ParametroAjuste.color_frame)
        frame_buttons.pack(fill=tk.BOTH, pady=10)

        if type(self.model.id) is int and permiso['eliminacion']:
            btn_Eliminar = Crear.crear_btn(self.Crear, text="Eliminar", ajsutes=self.ParametroAjuste)
            btn_Eliminar.pack(side="left", padx=10, in_=frame_buttons)
            btn_Eliminar.config(command=self.eliminar_model)

        if permiso['escritura']:
            btn_Guardar = Crear.crear_btn(self.Crear, text="Guardar", ajsutes=self.ParametroAjuste)
            btn_Guardar.pack(side="left", padx=10, in_=frame_buttons)
            btn_Guardar.config(command=self.guardar)

    def ir_back_view(self,event):
        widget = event.widget
        navegacion =  self.navegacion[widget.navegacion_id]
        navegacion['funcion']([navegacion['model'].id],model=navegacion['model'],navegacion=self.navegacion,nuevo=False,back=True)

    def guardar(self):
        try:
            self.verificar_fields_required()
            cliente = {}
            sel = self.master.master.frame_contenido
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
            self.master.master.load()
        except ValueError as e:
            return

    def eliminar_model(self):
        self.model.eliminar_datos_models_rel(self.model.id)
        model = self.model
        self.model.delete_instance()
        if self.ir_action_back:
            self.ir_action_back(self.model)

    def verificar_fields_required(self):
        msg = ""
        campos_no_nulos = [campo for nombre, campo in self.model._meta.fields.items()if campo.null is False or campo.required]
        sel = self.frame_contenido_header.master.frame_contenido
        for field in campos_no_nulos:
            if not isinstance(field,Auto):
                entry = getattr(sel, f"{field.name}_field")
                if entry.get() == "":
                    msg += f"El campo {field.help_text} es requerido \n"

        if msg != "":
            messagebox.showerror("Error", msg)
            raise ValueError("Campo vacío")