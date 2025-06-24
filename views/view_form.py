import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from utils.autocomplete_entry import AutocompleteEntry
from models.models import *
from utils.ajuste import ParametroAjuste
from utils.crear import Crear

popup = None

class ViewForm(tk.Frame):
    def __init__(self, master=None,model=None,id=False,ir_action_back=None,navegacion=None):
        self.ParametroAjuste = ParametroAjuste()
        self.Crear = Crear()
        super().__init__(master, bg=self.ParametroAjuste.color_fondo)
        self.baseModel = model
        self.model = model
        self.id = id
        self.ir_action_back = ir_action_back
        self.navegacion = navegacion
        self.Guardado = False
        self.pack(fill=tk.BOTH, expand=True)
        self.frame_contenido_header = self.crear_area_contenido_header()
        self.frame_contenido = self.crear_area_contenido()
        self.load()


    def load(self):
        if not self.id:
            self.crear_header()
            self.crear_form()
        else:
            self.model =  self.baseModel.get(self.baseModel.id == self.id)
            self.crear_header()
            self.crear_form()

    def crear_area_contenido_header(self):
        frame_contenido_header = tk.Frame(self, height=100, bg="white")
        frame_contenido_header.pack(side="top", fill="x")
        return frame_contenido_header

    def crear_area_contenido(self):
        frame_contenido = tk.Frame(self, bg="white")
        frame_contenido.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
        return frame_contenido

    def crear_header(self):
        x = 5
        y = 5
        for index, navegacion in enumerate(self.navegacion):
            if x != 5:
                x += 15
            entry = Crear.crear_btn_navegacion(self.Crear, text=navegacion, ajsutes=self.ParametroAjuste)
            entry.config(command=self.regresar)
            entry.place(x=x, y=15,in_=self.frame_contenido_header)
            x += len(navegacion)*9
            if index == len(self.navegacion)-1:
                text = "Nuevo"
                if type(self.model.id) is int:
                    text = getattr(self.model, "nombre")

                entry.config(state="disabled", text=text)

            else:
                label = tk.Label(self.frame_contenido_header, text="/", bg="white", font=('Arial', 12, 'bold'), fg='#4f4e4d')
                label.place(x=x+5, y=15)

        btn_Guardar = Crear.crear_btn(self.Crear,text="Guardar",ajsutes=self.ParametroAjuste)
        btn_Guardar.place(x=5, y=50,in_=self.frame_contenido_header)
        btn_Guardar.config(command=self.guardar)

    def crear_form(self):
        row = 1
        rowLabel = 1
        column = 0
        campos = self.model._meta.sorted_fields
        total_campos = self.cantidad_labelframe(campos)
        self.crear_labelframe(column,rowLabel)
        espaciador = tk.Frame(self.frame_contenido, width=200, height=100, bg="white")
        espaciador.grid(row=0, column=0)
        espaciador = tk.Frame(self.frame_contenido, width=200, height=100, bg="white")
        espaciador.grid(row=0, column=1)
        for index,field in enumerate(campos):
            if field.choices:
                self.crear_select(field,row,column)
                if field.mostrar_Form:
                    row += 1
            elif field.index:
                self.crear_autocompletar(field,row,column)
                if field.mostrar_Form:
                    row += 1
            else:
                self.crear_char(field,row,column)
                if field.mostrar_Form:
                    row += 1

            if row == total_campos+1 and index+1 < len(campos):
                if rowLabel  % 2 == 0:
                    self.crear_labelframe(0, rowLabel)
                else:
                    self.crear_labelframe(1, rowLabel)
                row = 1
                rowLabel += 1
                column += 1

    def crear_select(self,field,row,column):
        label = tk.Label(self.marco, text=f"{field.help_text}:", bg="white",font=('TkTextFont', 13, 'bold'))
        label.grid(row=row, column=column+1, padx=10, pady=5, sticky="w")
        opciones = [op[0] for op in field.choices]
        self.tipo_var = tk.StringVar()
        entry = ttk.Combobox(self.marco, textvariable=self.tipo_var,values=opciones,width=40)
        entry.grid(row=row, column=column+2, padx=10, pady=5, sticky="ew")
        if not field.mostrar_Form:
            entry.grid_remove()
            label.grid_remove()
        if type(self.model.id) is int:
            entry.insert(0, getattr(self.model, field.name))
        setattr(self, f"{field.name}_field", entry)

    def crear_char(self,field,row,column):
        label = tk.Label(self.marco, text=f"{field.help_text}:", bg="white",font=('TkTextFont', 13, 'bold'))
        label.grid(row=row, column=column+1, padx=10, pady=5, sticky="w")
        entry = ttk.Entry(self.marco,width=40)
        entry.grid(row=row, column=column+2, padx=10, pady=5, sticky="ew")
        if not field.mostrar_Form:
            entry.grid_remove()
            label.grid_remove()
        if type(self.model.id) is int:
            entry.insert(0, getattr(self.model, field.name))
        setattr(self, f"{field.name}_field", entry)

    def crear_autocompletar(self,field,row,column):
        label = tk.Label(self.marco, text=f"{field.help_text}:", bg="white",font=('TkTextFont', 13, 'bold'))
        label.grid(row=row, column=column+1, padx=10, pady=5, sticky="w")
        lista = field.rel_model.obtener_datos_para_atucompleteview()
        entry = ttk.Entry(self.marco,width=40)
        entry.grid(row=row, column=column+2, padx=10, pady=5, sticky="ew")
        entry.data_list = lista
        entry.marco = self.marco
        entry.listbox = None
        entry.bind("<KeyRelease>", self.check_input)
        if not field.mostrar_Form:
            entry.grid_remove()
            label.grid_remove()
        if type(self.model.id) is int:
            entry.insert(0, getattr(self.model, field.name).nombre)
            entry.refeencia_id = getattr(self.model, field.name).id
        setattr(self, f"{field.name}_field", entry)

    def crear_labelframe(self,column,rowLabel):
        style = ttk.Style()
        style.configure("Custom.TLabelframe", background="white")  # Color de fondo del marco
        self.marco = ttk.LabelFrame(self.frame_contenido, text="Datos", style="Custom.TLabelframe")
        self.marco.grid(column=column+1, row=rowLabel+1, padx=10, pady=10, sticky="nsew")

    def cantidad_labelframe(self,campos):
        cant = len(list(filter(lambda x: x.mostrar_Form == True, campos)))
        print(str(cant))
        if cant == 1:
            return 1
        elif cant > 1 and cant <= 5:
            return 2
        elif cant > 5 and cant <= 7:
            return 3
        elif cant >= 8:
            return 4

    def guardar(self):
        cliente = {}
        for attr in self.__dict__:
            if attr.endswith("_field"):
                valor = getattr(self, attr).get()
                entry = getattr(self, attr)
                key = attr.replace('_field','')
                if hasattr(entry,"refeencia_id"):
                    cliente[f"{key}"] = entry.refeencia_id
                else:
                    cliente[f"{key}"] = valor
        if cliente['id'] == '':
            del cliente["id"]
        self.model = self.model.crear_actualizar_desde_dict(cliente)
        self.id = self.model.id
        self.load()

    def regresar(self):
        if self.ir_action_back:
            self.ir_action_back(self.baseModel)

    def check_input(self, event):
        widget = event.widget
        typed = widget.get()
        if typed == "":
            self.hide_listbox()
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
            widget.entry.refeencia_id = selected_id
            self.hide_listbox( widget.entry)
        if popup:
            popup.destroy()








