from tkinter import messagebox
import tkinter as tk
from models.models import Auto
from utils.ajuste import ParametroAjuste
from utils.crear import Crear


class ViewFormHeader(tk.Frame):
    def __init__(self,master=None,navegacion=None,model=None,user=None,guardar=None,ir_action_back=None):
        self.ParametroAjuste = ParametroAjuste()
        self.Crear = Crear()
        super().__init__(master, bg=self.ParametroAjuste.color_fondo)
        self.frame_contenido_header = master
        self.navegacion = navegacion
        self.ir_action_back = ir_action_back
        self.guardar = guardar
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
            btn_Guardar.config(command=self._guardar)

    def ir_back_view(self,event):
        widget = event.widget
        navegacion =  self.navegacion[widget.navegacion_id]
        if navegacion['descripcion'] == 'Menu principal':
            navegacion['funcion']()
        else:
            navegacion['funcion']([navegacion['model'].id],model=navegacion['model'],navegacion=self.navegacion,nuevo=False,back=True)

    def _guardar(self):
        if self.guardar:
            self.guardar()

    def eliminar_model(self):
        self.model.eliminar_datos_models_rel(self.model.id)
        model = self.model
        self.model.delete_instance()
        if self.ir_action_back:
            self.ir_action_back()