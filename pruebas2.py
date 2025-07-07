import tkinter as tk
from tkinter import ttk

# Datos de ejemplo
datos = [
    ("001", "Juan", "Ventas"),
    ("002", "Ana", "Marketing"),
    ("003", "Luis", "Ventas"),
    ("004", "Marta", "TI"),
    ("005", "Carlos", "Marketing"),
]

filtros_activos = {}

def aplicar_filtros():
    items = tree.get_children()
    for item in tree.get_children():
        valores = tree.item(item, "values")
        texto = " ".join(valores).lower()
        visible = all(f.lower() in texto for f in filtros_activos.values())
        if visible:
            tree.reattach(item, '', 'end')
        else:
            tree.detach(item)

def agregar_filtro():
    texto = entrada_filtro.get().strip()
    if texto and texto not in filtros_activos.values():
        clave = f"filtro_{len(filtros_activos)}"
        filtros_activos[clave] = texto
        mostrar_filtros()
        aplicar_filtros()
    entrada_filtro.delete(0, tk.END)

def eliminar_filtro(clave):
    if clave in filtros_activos:
        del filtros_activos[clave]
        mostrar_filtros()
        aplicar_filtros()

def mostrar_filtros():
    for widget in frame_filtros.winfo_children():
        widget.destroy()
    for clave, texto in filtros_activos.items():
        subframe = tk.Frame(frame_filtros, bd=1, relief="solid", padx=5, pady=2)
        tk.Label(subframe, text=texto).pack(side="left")
        tk.Button(subframe, text="❌", command=lambda c=clave: eliminar_filtro(c)).pack(side="right")
        subframe.pack(side="left", padx=5)

# Ventana principal
root = tk.Tk()
root.title("Filtros dinámicos en Treeview")

entrada_filtro = tk.Entry(root)
entrada_filtro.pack(pady=5)

boton_agregar = tk.Button(root, text="Agregar filtro", command=agregar_filtro)
boton_agregar.pack(pady=5)

frame_filtros = tk.Frame(root)
frame_filtros.pack(pady=5)

columnas = ("ID", "Nombre", "Departamento")
tree = ttk.Treeview(root, columns=columnas, show="headings")
for col in columnas:
    tree.heading(col, text=col)
tree.pack()

# Insertar datos
for fila in datos:
    tree.insert("", "end", values=fila)

root.mainloop()