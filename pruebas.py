import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Visor de Imágenes")

        # Marco para la imagen
        self.frame = tk.Frame(root, width=200, height=200, bg="gray")
        self.frame.pack(padx=10, pady=10)

        # Etiqueta donde se mostrará la imagen
        self.label_imagen = tk.Label(self.frame)
        self.label_imagen.pack()

        # Botón para cambiar la imagen
        self.boton = tk.Button(root, text="Seleccionar imagen", command=self.cambiar_imagen)
        self.boton.pack(pady=10)

        # Imagen inicial (opcional)
        self.imagen_actual = None

    def cambiar_imagen(self):
        ruta = filedialog.askopenfilename(filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.gif")])
        if ruta:
            imagen = Image.open(ruta)
            imagen.thumbnail((200, 200))  # Redimensionar para que quepa en el recuadro
            self.imagen_actual = ImageTk.PhotoImage(imagen)
            self.label_imagen.config(image=self.imagen_actual)

# Crear la ventana principal
root = tk.Tk()
app = App(root)
root.mainloop()