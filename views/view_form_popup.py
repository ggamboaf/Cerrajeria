import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.autocomplete_entry import AutocompleteEntry
from models import *
from utils.ajuste import ParametroAjuste
from utils.crear import Crear
from models.models import *

popup = None

class ViewFormPopup(tk.Frame):
    def __init__(self,master=None,model=None,modelPadre=None,user=None,load=None):
        self.modelCreate = {}
        self.ParametroAjuste = ParametroAjuste()
        self.Crear = Crear()
        super().__init__(master, bg=self.ParametroAjuste.color_fondo)
        self.load = load
        self.modelPadre = modelPadre
        self.model = model
        self.user = user
        self.frame_contenido = master
        self.modal_Agregar()



    def modal_Agregar(self):
        try:
            permiso = self.user.get_permiso(self.model)
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

            self.frame_contenido_labelFrame = tk.Frame( self.popup,bg=self.ParametroAjuste.color_frame)
            self.frame_contenido_labelFrame.pack(padx=10, pady=10, fill='both', expand=True)

            button_frame = tk.Frame( self.popup,bg=self.ParametroAjuste.color_frame)
            button_frame.pack(fill='x',pady=20)

            if  permiso['creacion']:
                btn_Agregar =  self.Crear.crear_btn(text="Agregar",contenedor=button_frame,ajsutes=self.ParametroAjuste)
                btn_Agregar.pack(side="left", padx=10)
                btn_Agregar.config(command= self.agregar_model)

            if type(self.model.id) is int and permiso['eliminacion']:
                btn_Eliminar = self.Crear.crear_btn(text="Eliminar", contenedor=button_frame, ajsutes=self.ParametroAjuste)
                btn_Eliminar.pack(side="left", padx=10)
                btn_Eliminar.config(command=self.eliminar_model)

            btn_Agregar =  self.Crear.crear_btn(text="Cancelar",contenedor=button_frame,ajsutes=self.ParametroAjuste)
            btn_Agregar.pack(side="left", padx=10)
            # btn_Agregar.config(command=lambda: self.cancelar(self.popup))

            for i in range(4):
                self.frame_contenido_labelFrame.grid_rowconfigure(i, weight=1)
                self.frame_contenido_labelFrame.grid_columnconfigure(i, weight=1)

            self.labelFrames = self.Crear.crear_labelframe(self.ParametroAjuste, self.model,self.frame_contenido_labelFrame)
            self.crear_body_fields()

            # if not permiso['escritura']:
            #     sel = self.frame_contenido
            #     for attr in sel.__dict__:
            #         if attr.endswith("_field"):
            #             try:
            #                 entry = getattr(sel, attr)
            #                 if isinstance(entry, tk.BooleanVar):
            #                     entry.boolean.config(state='disabled')
            #                 else:
            #                     entry.config(state='disabled')
            #             except tk.TclError:
            #                 pass
        except ValueError as e:
            return

    def agregar_model(self):
        try:
            self.verificar_fields_required()
            record = {}
            sel = self.frame_contenido_labelFrame
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

    def crear_body_fields(self):
        for index, field in enumerate(self.model._meta.sorted_fields):
            self.marco = self.labelFrames[field.numero_Grupo]
            if field.choices:
                self.Crear.crear_select(field,self.marco,self.model,self.frame_contenido_labelFrame)
            elif field.index:
                self.Crear.crear_autocompletar(field,self.marco,self.model,self.frame_contenido_labelFrame,self.check_input,modelPadre=self.modelPadre)
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
        popup = tk.Toplevel(self.frame_contenido_labelFrame)
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
        sel = self.frame_contenido_labelFrame
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

    def set_valor_maximo(self,widget):
        campos = widget.entry.valor_maximo.split(",")
        valor_maximo = self.model.obtener_valor_maximo(widget.entry.referencia_id)
        sel = self.frame_contenido_labelFrame
        for campo in campos:
            entry = getattr(sel, f"{campo}_field")
            entry.valor_maximo = valor_maximo

    def verificar_fields_required(self):
        msg = ""
        campos_no_nulos = [campo for nombre, campo in self.model._meta.fields.items()if campo.null is False or campo.required]
        sel = self.frame_contenido_labelFrame
        for field in campos_no_nulos:
            if not isinstance(field,Auto):
                entry = getattr(sel, f"{field.name}_field")
                if entry.get() == "":
                    msg += f"El campo {field.help_text} es requerido \n"

        if msg != "":
            messagebox.showerror("Error", msg)
            raise ValueError("Campo vacío")