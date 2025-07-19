from tkinter import messagebox, ttk
import tkinter as tk
from models.models import Auto, Boolean, Date
from utils.ajuste import ParametroAjuste
from utils.crear import Crear
from utils.enviar_correo import EnviarCorreo
from utils.generar_reporte import GenerarReporte

popup = None

class ViewFormBody(tk.Frame):
    def __init__(self,master=None,navegacion=None,model=None,user=None,on_click_create_Model=None,modal_Agregar=None):
        self.frame_contenido_tab = None
        self.marco = None
        self.labelFrames = None
        self.frame_contenido_labelFrame = None
        self.frame_contenido_report = None
        self.ParametroAjuste = ParametroAjuste()
        self.Crear = Crear()
        super().__init__(master, bg=self.ParametroAjuste.color_fondo)
        self.on_click_create_Model = on_click_create_Model
        self.modal_Agregar = modal_Agregar
        self.frame_contenido_body = None
        self.model = model
        self.navegacion = navegacion
        self.user = user
        self.crear_body()

    def crear_body(self):
        canvas = tk.Canvas(self.master,bg=self.ParametroAjuste.color_frame)
        scrollbar = ttk.Scrollbar(self.master, orient="vertical", command=canvas.yview)
        self.frame_contenido_body = tk.Frame(canvas,bg=self.ParametroAjuste.color_frame)

        self.frame_contenido_body.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.frame_contenido_body, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.crear_body_header()
        self.crear_body_model_field()
        self.crear_body_xx()

    def crear_body_header(self):
        if self.model.accion_Config['reporte']:
            self.frame_contenido_report = tk.Frame(self.frame_contenido_body, bg=self.ParametroAjuste.color_frame)
            self.frame_contenido_report.pack(padx=10, pady=10, fill='x')
            if self.model.accion_Config['reporte_Correo']:
                btn_Enviar_Correo = Crear.crear_btn(self.Crear,text=self.model.accion_Config['reporte_CorreoDescripcion'],
                                                    contenedor=self.frame_contenido_report, ajsutes=self.ParametroAjuste)
                btn_Enviar_Correo.pack(side="left", padx=10)
                btn_Enviar_Correo.config(command=self.enviar_reporte_correo)

            if self.model.accion_Config['reporte_Descargar']:
                btn_Descargar = Crear.crear_btn(self.Crear,text=self.model.accion_Config['reporte_DescargarDescripcion'],
                                                contenedor=self.frame_contenido_report, ajsutes=self.ParametroAjuste)
                btn_Descargar.pack(side="left", padx=10)
                btn_Descargar.config(command=self.descargar_reporte)

            if self.model.accion_Config['crear_Modelo'] and not self.model.terminada:
                btn_Crear_Modelo =Crear.crear_btn(self.Crear,text=self.model.accion_Config['crear_Modelo_Descripcion'],contenedor=self.frame_contenido_report, ajsutes=self.ParametroAjuste)
                btn_Crear_Modelo.pack(side="left", padx=10)
                btn_Crear_Modelo.config(command=self._on_click_create_model)

        if 'otras_acciones' in self.model.accion_Config:
            self.frame_contenido_report = tk.Frame(self.frame_contenido_body, bg=self.ParametroAjuste.color_frame)
            self.frame_contenido_report.pack(padx=10, pady=10, fill='x')
            for accion in self.model.accion_Config['otras_acciones']:
                btn_Crear_Modelo = Crear.crear_btn(self.Crear, text=accion['accion_Nombre'], contenedor=self.frame_contenido_report, ajsutes=self.ParametroAjuste)
                btn_Crear_Modelo.pack(side="left", padx=10)
                btn_Crear_Modelo.metodo = accion['metodo']
                btn_Crear_Modelo.bind("<Button-1>", self.otras_acciones)

    def otras_acciones(self,event):
        widget = event.widget
        metodo = getattr(self.model, widget.metodo)
        metodo()

    def enviar_reporte_correo(self):
        return EnviarCorreo.enviar_correo_reporte(EnviarCorreo(),self.model)

    def descargar_reporte(self):
        return GenerarReporte.descargar_plantilla_pdf(GenerarReporte(),self.model)

    def _on_click_create_model(self):
        if self.on_click_create_Model:
            model = self.model.buscar_crear_model()
            valores = [model.id]
            self.on_click_create_Model(valores,model,self.navegacion,nuevo=False)

    def crear_body_model_field(self):
        self.frame_contenido_labelFrame = tk.Frame(self.frame_contenido_body, bg=self.ParametroAjuste.color_frame)
        self.frame_contenido_labelFrame.pack(padx=10, pady=10, fill='both', expand=True)
        for i in range(4):
            self.frame_contenido_labelFrame.grid_rowconfigure(i, weight=1)
            self.frame_contenido_labelFrame.grid_columnconfigure(i, weight=1)

        self.labelFrames = self.Crear.crear_labelframe(self.ParametroAjuste,self.model,self.frame_contenido_labelFrame)
        self.crear_body_fields()
        self.crear_body_rel()

    def crear_body_fields(self):
        for index, field in enumerate(self.model._meta.sorted_fields):
            self.marco = self.labelFrames[field.numero_Grupo]
            if field.choices:
                self.Crear.crear_select(field,self.marco,self.model,self.frame_contenido_labelFrame)
            elif field.index:
                self.Crear.crear_autocompletar(field,self.marco,self.model,self.frame_contenido_labelFrame,self.check_input)
            elif isinstance(field, Boolean):
                self.Crear.crear_boolean(field,self.marco,self.model,self.frame_contenido_labelFrame)
            elif isinstance(field, Date):
                self.Crear.crear_date(field,self.marco,self.model,self.frame_contenido_labelFrame,self.ochange)
            else:
                self.Crear.crear_char(field,self.marco,self.model,self.frame_contenido_labelFrame,self.ochange)

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
        popup = tk.Toplevel(self.frame_contenido_body)
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

    def crear_body_rel(self):
        if hasattr(self.model, "models_Rels"):
            self.frame_contenido_tab = tk.Frame(self.frame_contenido_body, bg=self.ParametroAjuste.color_frame)
            self.frame_contenido_tab.pack(padx=10, pady=10, fill='x')
            self.Crear.crear_tab(self.model,self.frame_contenido_tab,self.user,self._modal_Agregar)

    def _modal_Agregar(self,model):
        if self.modal_Agregar:
            self.modal_Agregar(model)

    def crear_body_xx(self):
        # fff = tk.Frame(self.frame_contenido_body, bg=self.ParametroAjuste.color_frame)
        # fff.pack(padx=10, pady=10, fill='x')

        for a in range(100):
            label = tk.Label(self.frame_contenido_body, text="Nombre", bg=self.ParametroAjuste.color_frame,font=('Arial', 12, 'bold'))
            label.pack(side='bottom', fill='both', expand=True)