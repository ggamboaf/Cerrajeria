import tkinter as tk
from tkinter import ttk

def create_scrollable_treeview(parent):
    container = tk.Frame(parent)
    container.pack(fill="x", expand=True, pady=10, padx=10)

    # Scrollbars
    x_scroll = tk.Scrollbar(container, orient="horizontal")
    y_scroll = tk.Scrollbar(container, orient="vertical")

    tree = ttk.Treeview(
        container,
        columns=("A", "B", "C"),
        show="headings",
        xscrollcommand=x_scroll.set,
        yscrollcommand=y_scroll.set
    )

    x_scroll.config(command=tree.xview)
    y_scroll.config(command=tree.yview)

    # Posicionar elementos
    tree.grid(row=0, column=0, sticky="nsew")
    y_scroll.grid(row=0, column=1, sticky="ns")
    x_scroll.grid(row=1, column=0, sticky="ew")

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    # Configurar columnas
    for col in ("A", "B", "C"):
        tree.heading(col, text=col)
        tree.column(col, width=200, anchor="center")

    # Insertar datos de ejemplo
    for i in range(30):
        tree.insert("", "end", values=(f"Fila {i}", f"Dato {i}", f"Más {i}"))

    return tree

root = tk.Tk()
root.geometry("900x600")

# Frame principal
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# Frame superior
top_frame = tk.Frame(main_frame, height=100, bg="lightblue")
top_frame.pack(fill="x")

# Frame inferior con scroll general
bottom_frame = tk.Frame(main_frame)
bottom_frame.pack(fill="both", expand=True)

canvas = tk.Canvas(bottom_frame)
scrollbar = tk.Scrollbar(bottom_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

# Asegurar que el ancho del scrollable_frame se ajuste al canvas
def on_canvas_configure(event):
    canvas.itemconfig("frame", width=event.width)

canvas.bind("<Configure>", on_canvas_configure)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas_window = canvas.create_window((0, 0), window=scrollable_frame, anchor="nw", tags="frame")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# Crear 4 tablas con scroll individual
for _ in range(4):
    create_scrollable_treeview(scrollable_frame)

root.mainloop()