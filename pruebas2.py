from tkinter import Tk, Label, Button
from tkfontchooser import askfont

def elegir_fuente():
    fuente = askfont(root)
    if fuente:
        fuente_str = f"{fuente['family']} {fuente['size']} {fuente['weight']} {fuente['slant']}"
        if fuente['underline']:
            fuente_str += " underline"
        if fuente['overstrike']:
            fuente_str += " overstrike"
        etiqueta.config(font=fuente_str, text="Fuente elegida: " + fuente_str)

root = Tk()
etiqueta = Label(root, text="Fuente elegida:")
etiqueta.pack(pady=10)

Button(root, text="Elegir fuente", command=elegir_fuente).pack(pady=10)
root.mainloop()